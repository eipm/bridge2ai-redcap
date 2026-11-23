#!/usr/bin/env python3
"""Build the Task Timeline page: when each questionnaire and acoustic task entered and left the
Bridge2AI-Voice iOS app, aligned with REDCap data dictionary releases.

Usage: python3 scripts/build_task_timeline.py <app_checkout> [repo] [out_dir]
  app_checkout  path to a local git checkout of the iOS app, with its release tags fetched
  repo          defaults to the repository that contains this script
  out_dir       defaults to repo (page is written to <out_dir>/docs/REDCap/Data Dictionary/Task Timeline.md)

The app's source is not public, so the page shows app versions as plain text, without links.

Sources
  App:    src/**/Items.swift at every app release tag. `enum Items` lists the tasks, `description`
          gives display names, `taskName` gives version suffixes such as " (v2)", and
          `struct ItemGroups` says which protocol each task belongs to and whether it is a
          questionnaire or an acoustic task.
  REDCap: the data dictionary at every release tag of this repo (same snapshot rules as
          scripts/build_data_dictionary_docs.py).
  Catalog: data/bridge2ai_voice_task_catalog.csv maps app items to display names, types and
          REDCap forms. A non-empty `protocols` value overrides the protocols read from the app.

App and REDCap version numbers stop matching after about v4.4 (the app moves to v2025.10.x,
v26.x, v27.x), so releases are aligned by date: the REDCap release in effect for an app release
is the latest REDCap release tagged on or before the app release date.
"""
import csv, collections, datetime, io, os, re, subprocess, sys

if len(sys.argv) < 2:
    sys.exit('Usage: python3 scripts/build_task_timeline.py <app_checkout> [repo] [out_dir]\n'
             '  app_checkout: path to a local git checkout of the iOS app, with its release tags fetched')
APP = os.path.abspath(sys.argv[1])
REPO = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[3] if len(sys.argv) > 3 else REPO
DOC_DIR = 'docs/REDCap/Data Dictionary'
UP = '../../..'
GH_REDCAP = 'https://github.com/eipm/bridge2ai-redcap'
CATALOG = 'data/bridge2ai_voice_task_catalog.csv'


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, check=True).stdout.decode('utf-8-sig', 'replace')


def tag_list(repo):
    out = []
    for line in git(repo, 'for-each-ref', '--sort=creatordate', '--format=%(refname:short)|%(creatordate:short)', 'refs/tags').split():
        t, d = line.split('|')
        out.append((t.replace('tags/', ''), d))
    return out


ref = lambda t: f'refs/tags/{t}'

# ---------------------------------------------------------------- REDCap dictionary snapshots
r_tags = tag_list(REPO)
r_idx = {t: i for i, (t, _) in enumerate(r_tags)}
r_date = dict(r_tags)
r_ls = lambda t: git(REPO, 'ls-tree', '-r', '--name-only', ref(t)).split('\n')
folder_tag = next(t for t, _ in reversed(r_tags) if any(f.startswith('v1.0.0/') for f in r_ls(t)))
folder_files = r_ls(folder_tag)
r_forms = []  # per REDCap tag: {form: set(variables)}
for t, _ in r_tags:
    folder = [f for f in folder_files if f.startswith(t + '/') and 'DataDictionary' in f and f.endswith('.csv')]
    rev, path = (ref(folder_tag), sorted(folder)[-1]) if folder else \
        (ref(t), [f for f in r_ls(t) if f.startswith('data/') and f.endswith('data_dictionary.csv')][0])
    forms = collections.defaultdict(set)
    for row in list(csv.reader(io.StringIO(git(REPO, 'show', f'{rev}:{path}'))))[1:]:
        if len(row) > 1:
            forms[row[1]].add(row[0])
    r_forms.append(forms)
all_vars = [set().union(*f.values()) for f in r_forms]


def form_intro(form):
    """First REDCap release that had any of the form's variables (covers instrument renames)."""
    present = [i for i, f in enumerate(r_forms) if form in f]
    if not present:
        return None
    vars_ = r_forms[present[-1]][form]
    return r_tags[next(i for i, av in enumerate(all_vars) if av & vars_)][0]


def nearest_redcap(date):
    """REDCap release closest in date (ties go to the earlier release). Release tags are often
    created a few days before or after a change goes live, so the closest one is used."""
    day = datetime.date.fromisoformat(date)
    gap = lambda i: abs((datetime.date.fromisoformat(r_tags[i][1]) - day).days)
    return r_tags[min(range(len(r_tags)), key=lambda i: (gap(i), i))][0]


# First REDCap release whose protocol, questionnaire or acoustic-task docs list a task as retired.
docs_retired_at = {}
for t, _ in r_tags:
    for f in r_ls(t):
        if not (f.endswith('.md') and re.search(r'protocol|questionnaires|acoustic tasks', f, re.I)):
            continue
        in_ret = False
        for line in git(REPO, 'show', f'{ref(t)}:{f}').split('\n'):
            if line.startswith('#'):
                in_ret = 'Retired' in line
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if in_ret and len(cells) > 2 and cells[0].isdigit():
                docs_retired_at.setdefault(re.sub(r'[^a-z0-9]', '', cells[1].lower()), t)


def form_status(form):
    """Status badge from the form's field-history page, if it has one."""
    p = os.path.join(REPO, DOC_DIR, form + '.md')
    if not os.path.exists(p):
        return ''
    m = re.search(r'\*\*Status:\*\* (\S+)', open(p, encoding='utf-8').read())
    return m[1] if m else ''


# ---------------------------------------------------------------- app snapshots
def block(src, start_re):
    m = re.search(start_re, src, re.M)
    if not m:
        return ''
    i = src.index('{', m.start())
    depth = 0
    for j in range(i, len(src)):
        if src[j] == '{':
            depth += 1
        elif src[j] == '}':
            depth -= 1
            if depth == 0:
                return src[i + 1:j]
    return src[i + 1:]


def parse_items(src):
    enum = block(src, r'^enum Items\b')
    head = re.split(r'\n\s*(?:var|func|init)\b', enum)[0]
    cases = []
    for ln in head.split('\n'):
        m = re.match(r'\s*case\s+(.+)', ln)
        if m:
            cases += [c.split('=')[0].strip() for c in m[1].split(',') if c.strip()]
    desc = dict(re.findall(r'case \.(\w+):\s*return "([^"]*)"', block(enum, r'var description\b')))
    ver = dict(re.findall(r'case \.(\w+):\s*return description \+ " \((v\d+)\)"', block(enum, r'var taskName\b')))
    groups = {}
    for name, body in re.findall(r'static let (\w+)(?:\s*:\s*\[Items\])?\s*=\s*\[(.*?)\]', block(src, r'^struct ItemGroups\b'), re.S):
        groups[name] = re.findall(r'(?:Items)?\.(\w+)', body)
    return cases, desc, ver, groups


a_tags, app = [], []
for t, d in tag_list(APP):
    files = [f for f in git(APP, 'ls-tree', '-r', '--name-only', ref(t)).split('\n') if f.endswith('/Items.swift')]
    if not files:
        continue
    cases, desc, ver, groups = parse_items(git(APP, 'show', f'{ref(t)}:{files[0]}'))
    a_tags.append((t, d))
    app.append({'cases': cases, 'desc': desc, 'ver': {c: ver.get(c, 'v1') for c in cases},
                'groups': {c: [g for g, items in groups.items() if c in items] for c in cases}})
latest = len(a_tags) - 1

catalog = {r['app_item']: r for r in csv.DictReader(open(os.path.join(REPO, CATALOG), encoding='utf-8'))}
for i, s in enumerate(app):
    for c in s['cases']:
        if c not in catalog:
            print(f'WARN: app item {c} (from {a_tags[i][0]}) is not in {CATALOG}', file=sys.stderr)
for item, r in catalog.items():
    if r['redcap_form'] and not any(r['redcap_form'] in f for f in r_forms):
        print(f'WARN: {CATALOG}: form {r["redcap_form"]} for {item} is not in any REDCap release', file=sys.stderr)


def protocol_label(g):
    gl = g.lower()
    if gl.startswith('pediatricgeneric'):
        return 'All pediatric ages'
    m = re.match(r'pediatric(\d+)to(\d+)', gl)
    if m:
        return f'Ages {m[1]}–{m[2]}'
    if gl.startswith('pediatric10plus'):
        return 'Ages 10+'
    for k, lab in [('generic', 'All adult protocols'), ('setup', 'All protocols'), ('voicedisorder', 'Voice'),
                   ('mooddisorder', 'Mood & Psychiatric'), ('respiratorydisorder', 'Respiratory'),
                   ('neurologicaldisorder', 'Neurological & Neurodegenerative')]:
        if gl.startswith(k):
            return lab
    return g


# ---------------------------------------------------------------- task rows (one per task version)
rows = []
for item, cat in catalog.items():
    if cat['type'] == 'internal':
        continue
    present = [i for i, s in enumerate(app) if item in s['cases']]
    if not present:
        continue
    # contiguous segments of (presence, version)
    segs = []
    for i in present:
        v = app[i]['ver'][item]
        if segs and segs[-1]['end'] == i - 1 and segs[-1]['ver'] == v:
            segs[-1]['end'] = i
        else:
            segs.append({'ver': v, 'start': i, 'end': i})
    versioned = len({s['ver'] for s in segs}) > 1
    pediatric = item.startswith('Pediatric') or any(g.startswith('Pediatric') for s in app for g in s['groups'].get(item, []))
    for k, s in enumerate(segs):
        groups = app[s['end']]['groups'][item]
        protos = cat['protocols'] or ', '.join(dict.fromkeys(protocol_label(g) for g in groups))
        nxt = segs[k + 1] if k + 1 < len(segs) else None
        retired_at = None if s['end'] == latest and not nxt else (s['end'] + 1)
        rows.append({
            'item': item, 'name': cat['display_name'] + (f' ({s["ver"]})' if versioned else ''),
            'base': cat['display_name'], 'type': cat['type'], 'form': cat['redcap_form'], 'note': cat['note'],
            'audience': 'Setup' if cat['type'] == 'Setup' else ('Pediatric' if pediatric else 'Adult'),
            'protocols': protos, 'start': s['start'], 'retired': retired_at,
            'replaced_by_version': nxt['ver'] if nxt and nxt['start'] == s['end'] + 1 else None,
            'first_version': k == 0,
        })

# ---------------------------------------------------------------- compare with the task docs in this repo
DOCS = {
    'Adult': ['docs/Adults/Acoustic Tasks/Adult Acoustic Tasks.md', 'docs/Adults/Questionnaires/Adult Questionnaires.md'],
    'Pediatric': ['docs/Pediatrics/Acoustic Tasks/Pediatric Acoustic Tasks.md', 'docs/Pediatrics/Questionnaires/Pediatric Questionnaires.md'],
}
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
docs = {a: {'active': {}, 'retired': {}} for a in DOCS}
for aud, paths in DOCS.items():
    for p in paths:
        full = os.path.join(REPO, p)
        if not os.path.exists(full):
            continue
        sec = None
        for line in open(full, encoding='utf-8'):
            if line.startswith('## '):
                sec = 'retired' if 'Retired' in line else 'active'
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if sec and len(cells) > 2 and cells[0].isdigit():
                docs[aud][sec][norm(cells[1])] = (cells[1], p)

active_names = {(r['audience'], norm(r['name'])) for r in rows if r['retired'] is None}
for r in rows:
    flags = []
    key = norm(r['name'])
    if r['audience'] in docs:
        dd = docs[r['audience']]
        if r['retired'] is None and key in dd['retired'] and key not in dd['active']:
            flags.append('⚠️ Active in the app, but the task docs list it as retired.')
        elif r['retired'] is not None and key in dd['active'] and (r['audience'], key) not in active_names:
            flags.append('⚠️ Retired in the app, but the task docs list it as active.')
        elif key not in dd['active'] and key not in dd['retired']:
            flags.append(f'ℹ️ Not on the {r["audience"].lower()} task pages.')
    r['form_intro'] = form_intro(r['form']) if r['form'] else None
    r['flags'] = flags

# Place every app change on the REDCap timeline (app release versions and dates are not published).
# Each app release maps to ONE REDCap release: the one closest in date, or an earlier one when the
# REDCap docs already list a task retired by that app release as retired.
anchor = {}
for i in {r['start'] for r in rows} | {r['retired'] for r in rows if r['retired'] is not None}:
    retired_here = [r for r in rows if r['retired'] == i]
    cands = [nearest_redcap(a_tags[i][1])] + \
            [docs_retired_at[norm(r['name'])] for r in retired_here if norm(r['name']) in docs_retired_at]
    anchor[i] = min(cands, key=r_idx.get)
for r in rows:
    # Introduced: the app change's REDCap release, or the release that added the task's form if later.
    intro = anchor[r['start']]
    if r['first_version'] and r['form_intro'] and r_idx[r['form_intro']] > r_idx[intro]:
        intro = r['form_intro']
    r['intro_rc'] = intro
    r['retired_rc'] = anchor[r['retired']] if r['retired'] is not None else None

docs_only = []
for aud, dd in docs.items():
    names = {norm(r['name']) for r in rows if r['audience'] == aud} | {norm(r['base']) for r in rows if r['audience'] == aud}
    for sec in ('active', 'retired'):
        for key, (label, p) in dd[sec].items():
            if key not in names:
                docs_only.append((aud, sec, label, p))

# ---------------------------------------------------------------- rendering
used_rc = set()


def rc_rel(t, date=False):
    if not t:
        return '—'
    used_rc.add(t)
    return f'[{t}][redcap-{t}]' + (f' ({r_date[t]})' if date else '')


HEADER = f'''<p align="center">
    <img src="{UP}/images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="{UP}/images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>
'''
status = lambda r: '🟢 Active' if r['retired'] is None else '🗄️ Retired'
n_act = sum(1 for r in rows if r['retired'] is None)
by_type = collections.Counter((r['type'], 'active' if r['retired'] is None else 'retired') for r in rows)

P = [HEADER, '[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)\n',
     '# 🗓️ Task Timeline\n',
     'When each questionnaire and acoustic task was introduced and retired, placed on the REDCap release timeline of '
     'this repository.\n',
     f'**Tasks:** 🟢 {n_act} active · 🗄️ {len(rows) - n_act} retired (counting each task version separately) · '
     f'**REDCap releases:** {len(r_tags)} ({rc_rel(r_tags[0][0])} → {rc_rel(r_tags[-1][0])})\n',
     '## How to Read This\n',
     '- **Introduced:** the REDCap release that was current when the task was introduced, or the release that added '
     'its REDCap form if that came later. Tasks available from the start show the first release, '
     f'{rc_rel(r_tags[0][0], True)}.',
     '- **Retired:** the REDCap release that was current when the task was retired.',
     '- **REDCap form:** questionnaires, and acoustic tasks that also store responses in REDCap (e.g. Word-Color Stroop), '
     'link to their field-history page. Other acoustic tasks have no form; their recordings are labeled with '
     '`acoustic_task_name`.',
     '- **Task versions:** when a task gets a new version, e.g. Loudness (v1) → (v2), the earlier version shows as 🗄️ Retired '
     'in the release where the new one starts.',
     '- **Notes:** ⚠️ marks a task whose status differs from the task pages in this repository. ℹ️ marks a task that is '
     'not on those pages.',
     '- Releases are matched by date, so a change made shortly before a REDCap release may show under the previous one.\n',
     '## Summary\n',
     '| Type | 🟢 Active | 🗄️ Retired |\n| :-- | :-: | :-: |']
for ty in ('Questionnaire', 'Acoustic task', 'Setup'):
    P.append(f'| {ty} | {by_type[(ty, "active")] or "—"} | {by_type[(ty, "retired")] or "—"} |')
P.append('')

type_order = {'Questionnaire': 0, 'Acoustic task': 1, 'Setup': 2}
for aud, title in (('Adult', 'Adult Tasks'), ('Pediatric', 'Pediatric Tasks'), ('Setup', 'Setup Tasks')):
    rs = sorted([r for r in rows if r['audience'] == aud],
                key=lambda r: (r['retired'] is not None, type_order.get(r['type'], 9), r_idx[r['intro_rc']], r['name']))
    if not rs:
        continue
    P.append(f'## {title}\n')
    P.append('| Task | Type | Protocols | Introduced | REDCap form | Retired | Status | Notes |')
    P.append('| :-- | :-- | :-- | :-: | :-- | :-: | :-- | :-- |')
    for r in rs:
        form = f'[`{r["form"]}`]({r["form"]}.md) {form_status(r["form"])}'.strip() if r['form'] else '—'
        notes = [n for n in [r['note']] if n] + r['flags']
        retired = rc_rel(r['retired_rc'], True) if r['retired_rc'] else '—'
        if r['replaced_by_version']:
            retired += f'<br><sub>replaced by ({r["replaced_by_version"]})</sub>'
        P.append(f'| {r["name"]} | {r["type"]} | {r["protocols"] or "—"} | {rc_rel(r["intro_rc"], True)} | '
                 f'{form} | {retired} | {status(r)} | {"<br>".join(notes) or "—"} |')
    P.append('')

# per-release changes (pediatric tasks that share an adult name get a suffix here)
shared = {r['base'] for r in rows if r['audience'] == 'Adult'} & {r['base'] for r in rows if r['audience'] == 'Pediatric'}
for r in rows:
    r['label'] = r['name'] + (' (pediatric)' if r['audience'] == 'Pediatric' and r['base'] in shared else '')
P.append('## REDCap Releases with Task Changes\n')
P.append('Only releases where a task was introduced, retired or given a new version are listed.\n')
P.append('| REDCap release | Date | ➕ Tasks introduced | 🗄️ Tasks retired | 🔁 Version changes |')
P.append('| :-: | :-: | :-- | :-- | :-- |')
for t, d in r_tags:
    added = [r['label'] for r in rows if r['intro_rc'] == t and r['first_version']]
    retired = [r['label'] for r in rows if r['retired_rc'] == t and not r['replaced_by_version']]
    changes = [f'{r["base"]}: ({r["name"].rsplit("(", 1)[1].rstrip(")")}) → ({r["replaced_by_version"]})'
               for r in rows if r['retired_rc'] == t and r['replaced_by_version']]
    if added or retired or changes:
        P.append(f'| {rc_rel(t)} | {d} | {", ".join(added) or "—"} | {", ".join(retired) or "—"} | {"<br>".join(changes) or "—"} |')
P.append('')

if docs_only:
    P.append('## On the Task Pages but Not in the App\n')
    P.append('Listed on the task pages in this repository with no matching app task. They may be collected another way '
             '(for example by a clinician) or named differently in the app.\n')
    P.append('| Audience | Name | Listed as | Page |\n| :-- | :-- | :-- | :-- |')
    for aud, sec, label, p in docs_only:
        P.append(f'| {aud} | {label} | {"🟢 Active" if sec == "active" else "🗄️ Retired"} | '
                 f'[{os.path.basename(p)[:-3]}]({UP}/{p.replace(" ", "%20")}) |')
    P.append('')

defs = [f'[redcap-{t}]: {GH_REDCAP}/releases/tag/{t}' for t, _ in r_tags if t in used_rc]
os.makedirs(os.path.join(OUT, DOC_DIR), exist_ok=True)
open(os.path.join(OUT, DOC_DIR, 'Task Timeline.md'), 'w', encoding='utf-8').write(
    '\n'.join(P) + '\n<!-- release links -->\n' + '\n'.join(defs) + '\n')
print('rows:', len(rows), 'by type/status:', dict(by_type), 'docs-only:', [(a, l) for a, _, l, _ in docs_only])
