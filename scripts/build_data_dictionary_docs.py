#!/usr/bin/env python3
"""Build per-field history docs for the Bridge2AI-Voice REDCap data dictionary.

Usage: python3 scripts/build_data_dictionary_docs.py [repo] [out_dir] [--json=<file>]
  repo     defaults to the repository that contains this script
  out_dir  defaults to repo (pages are written to <out_dir>/docs/REDCap/Data Dictionary/)
  --json   also write every variable and its history as JSON (used by the website's
           Variable Explorer)

Milestones = git release tags. For v1.0.0–v3.3.0 the dictionary lived in
per-version folders (vX.Y.Z/*_DataDictionary_*.csv); we read the *final*
export in each folder (from the last tag that still has them) because some
folders were re-exported after tagging. From v3.4.0 on we read
data/*data_dictionary.csv.

Instrument status (one of):
  active   – in the dictionary and collected under a current protocol
  retired  – still in the dictionary, but listed under "Retired Questionnaires"
             in docs/*/Questionnaires/*.md (no new data collected)
  previous – still in the dictionary, superseded by a newer version
             (older eConsent versions not published in docs/REDCap/Instruments.md)
  removed  – no longer in the dictionary at all

Variable renames come from data/bridge2ai_voice_redcap_variable_renames.csv.
Each run also prints likely renames that are not in that file yet.
"""
import csv, collections, html, io, json, os, re, subprocess, sys

JSON_OUT = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--json=')), None)
ARGS = [a for a in sys.argv[1:] if not a.startswith('--json=')]
REPO = ARGS[0] if ARGS else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ARGS[1] if len(ARGS) > 1 else REPO
GH = 'https://github.com/eipm/bridge2ai-redcap'
DOC_DIR = 'docs/REDCap/Data Dictionary'  # where pages will live in the repo
UP = '../../..'                           # relative path from DOC_DIR to repo root

# Release in which an instrument was retired from its protocol. The dictionary
# cannot tell us this; derived from the protocol docs' "Retired Questionnaires"
# sections, where all four first appear at v4.0.0 (they were active at v3.27.0).
RETIRED_IN = {
    'q_voice_voice_problem_severity': 'v4.0.0',
    'q_mood_ptsd_adult': 'v4.0.0',
    'q_mood_participant_history': 'v4.0.0',
    'q_neuro_winograd_schemas': 'v4.0.0',
}

STATUS = {
    'active': ('🟢', 'Active'),
    'retired': ('🗄️', 'Retired'),
    'previous': ('🗂️', 'Previous version'),
    'removed': ('⚫', 'Removed'),
}


def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, check=True).stdout.decode('utf-8-sig')


# ---------------------------------------------------------------- snapshots
tags = []
for line in git('for-each-ref', '--sort=creatordate', '--format=%(refname:short)|%(creatordate:short)', 'refs/tags').split():
    t, d = line.split('|')
    tags.append((t.replace('tags/', ''), d))
tagdate = dict(tags)
tag_idx = {t: i for i, (t, _) in enumerate(tags)}
ref = lambda t: f'refs/tags/{t}'  # explicit: some tags share a name with a branch
ls = lambda t: git('ls-tree', '-r', '--name-only', ref(t)).split('\n')

# last tag that still carries the per-version folders (v1.0.0/ … v3.3.0/)
folder_tag = next(t for t, _ in reversed(tags) if any(f.startswith('v1.0.0/') for f in ls(t)))
folder_files = ls(folder_tag)


def read_csv(rev, path):
    rows = list(csv.reader(io.StringIO(git('show', f'{rev}:{path}'))))
    hdr = rows[0]
    out = collections.OrderedDict()
    for r in rows[1:]:
        if r:
            r += [''] * (len(hdr) - len(r))
            out[r[0]] = dict(zip(hdr, r))
    return out


snaps = []
for t, d in tags:
    folder = [f for f in folder_files if f.startswith(t + '/') and 'DataDictionary' in f and f.endswith('.csv')]
    if folder:
        fields = read_csv(ref(folder_tag), sorted(folder)[-1])
    else:
        fields = read_csv(ref(t), [f for f in ls(t) if f.startswith('data/') and f.endswith('data_dictionary.csv')][0])
    snaps.append({'tag': t, 'date': d, 'fields': fields})

# commits per milestone (for the milestone table)
commits = collections.defaultdict(list)
log = git('log', '--reverse', '--format=%h|%s', '--', 'data/bridge2ai_voice_project_data_dictionary.csv',
          'data/bridge2ai_voice_redcap_project_data_dictionary.csv')
for line in log.split('\n'):
    if not line:
        continue
    h, msg = line.split('|', 1)
    tag = git('describe', '--contains', '--tags', h).strip().split('~')[0].split('^')[0].replace('tags/', '')
    commits[tag].append((h, msg))

formnames = {}
for t, _ in tags:
    for f in ls(t):
        if f.endswith('.xml'):
            for oid, name in re.findall(r'<FormDef OID="Form\.([^"]+)" Name="([^"]+)"', git('show', f'{ref(t)}:{f}')):
                formnames[oid] = html.unescape(name)

# ---------------------------------------------------------------- categories
# Reuse the categories + display names already curated in docs/REDCap/Instruments.md
CATEGORY_ORDER, form_cat, form_disp, form_rank = [], {}, {}, {}
cat = None
for line in open(os.path.join(REPO, 'docs/REDCap/Instruments.md'), encoding='utf-8'):
    if line.startswith('## '):
        cat = line[3:].strip()
        CATEGORY_ORDER.append(cat)
    m = re.match(r'\| (\d+) \| ([^|]+) \| `([^`]+)` \|', line)
    if m and cat:
        form_cat[m[3]] = cat
        form_disp[m[3]] = m[2].strip()
        form_rank[m[3]] = len(form_rank)

# Retired-from-protocol instruments: read from the questionnaire pages' "Retired" tables
RETIRED = {}
disp_to_form = {v.lower(): k for k, v in form_disp.items()}
for qdoc in ('docs/Adults/Questionnaires/Adult Questionnaires.md',
             'docs/Pediatrics/Questionnaires/Pediatric Questionnaires.md'):
    path = os.path.join(REPO, qdoc)
    if not os.path.exists(path):
        continue
    in_retired = False
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            in_retired = 'Retired' in line
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not in_retired or len(cells) < 5 or not cells[0].isdigit():
            continue
        form = disp_to_form.get(cells[1].lower()) or disp_to_form.get(('Pediatric — ' + cells[1]).lower())
        if not form:
            print('WARN: retired questionnaire not matched to a form:', cells[1], file=sys.stderr)
            continue
        pdf = re.search(r'\]\(<?([^)>]+)>?\)', cells[4])
        pdf_path = os.path.normpath(os.path.join(os.path.dirname(qdoc), pdf[1])) if pdf else None
        RETIRED[form] = {'from': cells[3], 'pdf': f'{UP}/{pdf_path}' if pdf_path else None,
                         'doc': f'{UP}/' + qdoc.replace(' ', '%20') + '#%EF%B8%8F-retired-questionnaires'}


def category_for(form):
    if form in form_cat:
        return form_cat[form]
    f = form
    if 'consent' in f: return 'Consents'
    if f.startswith(('pediatric', 'd_peds', 'q_peds', 'peds')): return 'Pediatric'
    if f.startswith(('d_', 'diagnosis_')): return 'Adult Diagnoses'
    if f.startswith('questionnaire_across_all_cohorts'): return 'Adult Questionnaires (Generic)'
    for k, c in [('q_generic', 'Adult Questionnaires (Generic)'), ('q_voice', 'Adult Questionnaires (Voice)'),
                 ('q_mood', 'Adult Questionnaires (Mood & Psychiatric)'), ('q_resp', 'Adult Questionnaires (Respiratory)'),
                 ('q_neuro', 'Adult Questionnaires (Neurological & Neurodegenerative)')]:
        if f.startswith(k): return c
    if f in ('session', 'acoustic_task', 'recording'): return 'Sessions and Recordings'
    return 'General'


SITE_ORDER = ['usf', 'mit', 'wcm', 'vumc']  # eConsent lineage order


def consent_key(form):
    site = next((s for s in SITE_ORDER if f'_{s}_' in form + '_'), None)
    return (site, 'spanish' if 'spanish' in form else 'english') if site else None


def sort_key(form):
    if form in form_rank:
        return (0, form_rank[form], 0, False, '')
    site = next((i for i, s in enumerate(SITE_ORDER) if f'_{s}_' in form + '_'), 9)
    m = re.search(r'version_(\d+)', form)
    return (1, site, -(int(m[1]) if m else 1), 'spanish' in form, form)


def display(form):
    return form_disp.get(form) or formnames.get(form) or form


# ---------------------------------------------------------------- history
ATTR = {'Form Name': 'Instrument', 'Section Header': 'Section header', 'Field Type': 'Type', 'Field Label': 'Label',
        'Choices, Calculations, OR Slider Labels': 'Choices / calculation', 'Field Note': 'Field note',
        'Text Validation Type OR Show Slider Number': 'Validation', 'Text Validation Min': 'Min',
        'Text Validation Max': 'Max', 'Identifier?': 'Identifier (PHI)',
        'Branching Logic (Show field only if...)': 'Branching logic', 'Required Field?': 'Required',
        'Custom Alignment': 'Alignment', 'Question Number (surveys only)': 'Question number',
        'Matrix Group Name': 'Matrix group', 'Matrix Ranking?': 'Matrix ranking', 'Field Annotation': 'Annotation'}

# instrument-level renames: a form-name change applied to (nearly) every field of the old form
form_renames = {}  # (tag, old) -> new
for i in range(1, len(snaps)):
    a, b = snaps[i - 1]['fields'], snaps[i]['fields']
    moves = collections.Counter((a[v]['Form Name'], b[v]['Form Name']) for v in b if v in a and a[v]['Form Name'] != b[v]['Form Name'])
    old_sizes = collections.Counter(r['Form Name'] for r in a.values())
    old_still = {r['Form Name'] for r in b.values()}
    for (old, new), n in moves.items():
        if old not in old_still or n >= 0.5 * old_sizes[old]:
            form_renames[(snaps[i]['tag'], old)] = new

hist = collections.OrderedDict()  # var -> list of events
last_row = {}
prev = {}
for s in snaps:
    cur = s['fields']
    for v, row in cur.items():
        if v not in prev:
            kind = 'reintroduced' if v in hist else 'introduced'
            hist.setdefault(v, []).append({'tag': s['tag'], 'kind': kind, 'form': row['Form Name']})
        else:
            ch = []
            for k in row:
                if k == 'Variable / Field Name':
                    continue
                old, new = (prev[v].get(k) or '').strip(), (row.get(k) or '').strip()
                if old != new:
                    if k == 'Form Name' and (s['tag'], old) in form_renames:
                        continue  # shown once at instrument level
                    ch.append((k, old, new))
            if ch:
                hist[v].append({'tag': s['tag'], 'kind': 'changed', 'changes': ch})
        last_row[v] = row
    for v in prev:
        if v not in cur:
            hist[v].append({'tag': s['tag'], 'kind': 'removed', 'form': prev[v]['Form Name']})
    prev = cur

current = snaps[-1]['fields']

# ---------------------------------------------------------------- variable renames
# Reviewed list in data/bridge2ai_voice_redcap_variable_renames.csv (milestone, old, new, relation, note).
#   renamed  – same question and coding, new name        → one merged history
#   recoded  – same question, new name, type/codes changed → one merged history
#   replaced – question changed, or split / merged         → separate histories, linked both ways
#   unrelated – false positive; only silences the detector
REL = {'renamed': ('✏️', 'Renamed'), 'recoded': ('🔁', 'Renamed & recoded'), 'replaced': ('↪️', 'Replaced')}
snap_at = {s['tag']: s['fields'] for s in snaps}
prev_tag = {tags[i][0]: tags[i - 1][0] for i in range(1, len(tags))}
RENAMES_CSV = 'data/bridge2ai_voice_redcap_variable_renames.csv'
rename_rows = []
if os.path.exists(os.path.join(REPO, RENAMES_CSV)):
    rename_rows = list(csv.DictReader(open(os.path.join(REPO, RENAMES_CSV), encoding='utf-8')))
rename_rows.sort(key=lambda r: tag_idx[r['milestone']])
lineage = []                                 # applied rows, for the crosswalk tables
alias = {}                                   # old name -> current name (renamed / recoded)
former = collections.defaultdict(list)       # name -> [(old, tag, relation)], oldest first
replaced_by = collections.defaultdict(list)  # old -> [(new, tag, note)]
replaces = collections.defaultdict(list)     # new -> [(old, tag, note)]
for r in rename_rows:
    t, old, new, rel, note = r['milestone'], r['old_variable'], r['new_variable'], r['relation'], r['note'].strip()
    if rel == 'unrelated':
        continue
    a_snap, b_snap = snap_at[prev_tag[t]], snap_at[t]
    if not (old in a_snap and old not in b_snap and new in b_snap and new not in a_snap):
        print(f'WARN: rename row does not match the dictionary at {t}: {old} -> {new}', file=sys.stderr)
        continue
    lineage.append(r)
    if rel in ('renamed', 'recoded'):
        ho, hn = hist[old], hist[new]
        if not (ho[-1]['kind'] == 'removed' and ho[-1]['tag'] == t and hn[0]['kind'] == 'introduced' and hn[0]['tag'] == t):
            print(f'WARN: cannot merge history for {old} -> {new}', file=sys.stderr)
            continue
        a, b = a_snap[old], b_snap[new]
        diffs = [(k, (a.get(k) or '').strip(), (b.get(k) or '').strip()) for k in b
                 if k != 'Variable / Field Name' and (a.get(k) or '').strip() != (b.get(k) or '').strip()]
        diffs = [x for x in diffs if not (x[0] == 'Form Name' and (t, x[1]) in form_renames)]
        hist[new] = ho[:-1] + [{'tag': t, 'kind': rel, 'old': old, 'new': new, 'note': note, 'changes': diffs}] + hn[1:]
        del hist[old]
        former[new] = former.pop(old, []) + [(old, t, rel)]
        for k in [k for k, v in alias.items() if v == old]:
            alias[k] = new
        alias[old] = new
    else:
        replaced_by[old].append((new, t, note))
        replaces[new].append((old, t, note))


def suggest_renames():
    """Print likely renames that are not in the reviewed CSV yet (removed + added in the same
    release and instrument, with a similar label, choices, name and position)."""
    import difflib
    reviewed = {(r['milestone'], r['old_variable'], r['new_variable']) for r in rename_rows}
    reviewed_old = {(r['milestone'], r['old_variable']) for r in rename_rows}
    norm = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip().lower()
    out = []
    for i in range(1, len(snaps)):
        t, a, b = snaps[i]['tag'], snaps[i - 1]['fields'], snaps[i]['fields']
        rem = [v for v in a if v not in b and (t, v) not in reviewed_old]
        add = [v for v in b if v not in a]
        ka, kb = list(a), list(b)
        scored = []
        for r in rem:
            ra = a[r]
            rform = form_renames.get((t, ra['Form Name']), ra['Form Name'])
            if ra['Field Type'] == 'descriptive' and not norm(ra['Field Label']):
                continue
            for n in add:
                nb = b[n]
                if nb['Form Name'] != rform:
                    continue
                lab = difflib.SequenceMatcher(None, norm(ra['Field Label']), norm(nb['Field Label'])).ratio()
                ch = difflib.SequenceMatcher(None, ra['Choices, Calculations, OR Slider Labels'], nb['Choices, Calculations, OR Slider Labels']).ratio()
                nm = difflib.SequenceMatcher(None, r, n).ratio()
                ia, ib = ka.index(r), kb.index(n)
                pos = len(set(ka[max(0, ia - 2):ia + 3]) & set(kb[max(0, ib - 2):ib + 3])) / 4
                score = 0.4 * lab + 0.2 * ch + 0.2 * nm + 0.15 * pos + 0.05 * (ra['Field Type'] == nb['Field Type'])
                scored.append((score, r, n))
        used_r, used_n = set(), set()
        for score, r, n in sorted(scored, reverse=True):
            if score >= 0.6 and r not in used_r and n not in used_n and (t, r, n) not in reviewed:
                used_r.add(r); used_n.add(n)
                out.append(f'{t},{r},{n},?,score {score:.2f}')
    if out:
        print(f'{len(out)} possible renames not in {RENAMES_CSV} (review, then add with a relation):', file=sys.stderr)
        print('\n'.join('  ' + x for x in out), file=sys.stderr)


suggest_renames()


# ---------------------------------------------------------------- rendering helpers
def clean(s, limit=None):
    s = re.sub(r'<br\s*/?>|</p>|</div>', ' ', s or '', flags=re.I)
    s = html.unescape(re.sub(r'<[^>]+>', '', s))
    s = re.sub(r'\s+', ' ', s).strip()
    if limit and len(s) > limit:
        s = s[:limit - 1].rstrip() + '…'
    return s.replace('|', '\\|')


def code(s, limit=None):
    s = clean(s, limit)
    return f'`{s}`' if s else '∅'


USED_TAGS = set()


def mtag(t):
    """Milestone link. Reference-style; definitions are appended per page by ref_defs()."""
    if not t:
        return '—'
    USED_TAGS.add(t)
    return f'[{t}]'


def ref_defs():
    defs = [f'[{t}]: {GH}/releases/tag/{t}' for t in sorted(USED_TAGS, key=tag_idx.get)]
    USED_TAGS.clear()
    return '\n<!-- milestone links -->\n' + '\n'.join(defs) + '\n'


def parse_choices(s):
    out = collections.OrderedDict()
    for part in (s or '').split('|'):
        if ',' in part:
            k, lab = part.split(',', 1)
            out[k.strip()] = lab.strip()
    return out


def values_summary(r):
    t, ch, val = r['Field Type'], r['Choices, Calculations, OR Slider Labels'], r['Text Validation Type OR Show Slider Number']
    if t in ('radio', 'checkbox', 'dropdown'):
        c = parse_choices(ch)
        items = [f'{k}={clean(v, 40)}' for k, v in c.items()]
        s = ' · '.join(items[:4])
        return s + (f' … ({len(c)} options)' if len(items) > 4 else '')
    if t == 'yesno': return '1=Yes · 0=No'
    if t == 'truefalse': return '1=True · 0=False'
    if t == 'slider': return 'slider' + (f': {clean(ch, 60)}' if ch else ' 0–100')
    if t == 'calc': return f'calc: {code(ch, 60)}'
    if t == 'text':
        rng = f" [{r['Text Validation Min']}–{r['Text Validation Max']}]" if r['Text Validation Min'] or r['Text Validation Max'] else ''
        return (f'`{val}`' + rng) if val else 'free text'
    if t == 'notes': return 'free text (long)'
    if t == 'file': return 'file upload' if val != 'signature' else 'signature'
    if t == 'descriptive': return '_display only — no data_'
    return ''


YN = lambda x: 'Yes' if x.strip().lower() == 'y' else 'No'


def change_cells(k, old, new):
    if k in ('Required Field?', 'Identifier?', 'Matrix Ranking?'):
        return YN(old), YN(new)
    if k == 'Choices, Calculations, OR Slider Labels' and '|' in old + new and ',' in old + new:
        a, b = parse_choices(old), parse_choices(new)
        added = [f'`{k2}`={clean(b[k2], 40)}' for k2 in b if k2 not in a]
        removed = [f'`{k2}`={clean(a[k2], 40)}' for k2 in a if k2 not in b]
        relab = [f'`{k2}`: {clean(a[k2], 30)} → {clean(b[k2], 30)}' for k2 in b if k2 in a and a[k2] != b[k2]]
        parts = ([f'➕ {", ".join(added[:6])}' + (' …' if len(added) > 6 else '')] if added else []) + \
                ([f'➖ {", ".join(removed[:6])}' + (' …' if len(removed) > 6 else '')] if removed else []) + \
                ([f'✏️ {"; ".join(relab[:4])}' + (' …' if len(relab) > 4 else '')] if relab else [])
        if list(a) != list(b) and set(a) == set(b) and not relab:
            parts.append('🔀 reordered')
        return f'{len(a)} options', '<br>'.join(parts) or f'{len(b)} options'
    if k == 'Form Name':
        return display(old), display(new)
    return code(old, 160), code(new, 160)


# ---------------------------------------------------------------- grouping + stats
os.makedirs(os.path.join(OUT, DOC_DIR), exist_ok=True)
by_form = collections.defaultdict(lambda: {'fields': [], 'removed': []})
for v in hist:
    if v in current:
        by_form[current[v]['Form Name']]['fields'].append(v)
    else:
        by_form[last_row[v]['Form Name']]['removed'].append(v)
order = {v: i for i, v in enumerate(current)}
for f in by_form.values():
    f['fields'].sort(key=lambda v: order[v])


def intro_of(v):
    return hist[v][0]['tag']


CHANGE_KINDS = ('changed', 'renamed', 'recoded')


def page_of(v):
    v = alias.get(v, v)
    return slug(current[v]['Form Name'] if v in current else last_row[v]['Form Name'])


def vlink(v, here):
    """Link to a variable's entry, on this page or another instrument page."""
    target = alias.get(v, v)
    page = page_of(target)
    return f'[`{v}`](#{target})' if page == here else f'[`{v}`]({page}#{target})'


def last_change(v):
    ch = [e['tag'] for e in hist[v] if e['kind'] in CHANGE_KINDS]
    return ch[-1] if ch else None


def removed_in(v):
    return [e['tag'] for e in hist[v] if e['kind'] == 'removed'][-1]


def status_of(form):
    if not by_form[form]['fields']:
        return 'removed'
    if form in RETIRED:
        return 'retired'
    if form not in form_rank:
        return 'previous'
    return 'active'


def superseded_by(form):
    key = consent_key(form)
    if not key:
        return None
    return next((f for f in form_rank if consent_key(f) == key), None)


form_stats = {}
for form, d in by_form.items():
    allv = d['fields'] + d['removed']
    lc = [t for v in allv for t in ([last_change(v)] + [e['tag'] for e in hist[v]]) if t]
    form_stats[form] = {
        'intro': min((intro_of(v) for v in allv), key=tag_idx.get),
        'last': max(lc, key=tag_idx.get),
        'fields': len(d['fields']), 'removed': len(d['removed']),
        'changed': sum(1 for v in allv if last_change(v)),
        'status': status_of(form),
        'removed_in': max((removed_in(v) for v in d['removed']), key=tag_idx.get) if d['removed'] else None,
    }

HEADER = f'''<p align="center">
    <img src="{UP}/images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="{UP}/images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>
'''


def slug(form):
    return form + '.md'


def badge(st):
    e, label = STATUS[st]
    return f'{e} {label}'


# ---------------------------------------------------------------- per-instrument pages
for form, d in by_form.items():
    fs = form_stats[form]
    st = fs['status']
    allv = d['fields'] + d['removed']
    chain, seen, frontier = [], set(), [form]
    while frontier:
        f = frontier.pop()
        for (t, old), new in form_renames.items():
            if new == f and old not in seen:
                seen.add(old); chain.append((t, old, new)); frontier.append(old)
    chain.sort(key=lambda x: tag_idx[x[0]])

    USED_TAGS.clear()
    L = [HEADER, '[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)\n',
         f'# {display(form)}\n']

    if st == 'retired':
        r = RETIRED[form]
        when = f' in {mtag(RETIRED_IN[form])} ({tagdate[RETIRED_IN[form]]})' if form in RETIRED_IN else ''
        pdf = f' · [Retired PDF (English)](<{r["pdf"]}>)' if r['pdf'] else ''
        L.append(f'> 🗄️ **Retired** from the {r["from"]} protocol{when}. No new data is collected, but the fields '
                 f'stay in REDCap so data from earlier participants remains valid.{pdf}\n')
    elif st == 'previous':
        sup = superseded_by(form)
        sup_txt = f' Superseded by [{display(sup)}]({slug(sup)}).' if sup else ''
        L.append(f'> 🗂️ **Previous version.**{sup_txt} This version is still defined in REDCap for participants who '
                 f'consented with it, but only the current version is published as an instrument ZIP.\n')
    elif st == 'removed':
        L.append(f'> ⚫ **Removed** from the REDCap dictionary in {mtag(fs["removed_in"])} ({tagdate[fs["removed_in"]]}). '
                 f'None of these variables exist in the current project; they are listed for data collected before then.\n')

    L += [f'**Form name:** `{form}` · **Category:** {category_for(form)} · **Status:** {badge(st)}  ',
          f'**Introduced:** {mtag(fs["intro"])} ({tagdate[fs["intro"]]}) · '
          f'**Last changed:** {mtag(fs["last"])} ({tagdate[fs["last"]]})  ',
          f'**Fields:** 📋 {fs["fields"]} in REDCap · ⚫ {fs["removed"]} removed · ✏️ {fs["changed"]} changed since introduction\n']
    if chain:
        L.append('**Instrument renames** (field variables were unchanged):\n')
        L.append('| Milestone | Date | Previous form name | New form name |\n| :-: | :-: | :-- | :-- |')
        for t, old, new in chain:
            L.append(f'| {mtag(t)} | {tagdate[t]} | `{old}` | `{new}` |')
        L.append('')

    if d['fields']:
        L.append('## 📋 Fields\n')
        if st != 'active':
            L.append(f'_All fields below share the instrument\'s status: {badge(st)}._\n')
        L.append('| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |')
        L.append('| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |')
        sec = None
        for i, v in enumerate(d['fields'], 1):
            r = current[v]
            lc = last_change(v)
            n = sum(1 for e in hist[v] if e['kind'] in CHANGE_KINDS)
            lc_cell = f'{mtag(lc)} ([{n}×](#{v}))' if lc else '—'
            label = clean(r['Field Label'], 140) or '_(no label)_'
            if r['Section Header'].strip() and r['Section Header'] != sec:
                sec = r['Section Header']
                L.append(f'| | **{clean(sec, 120)}** | | | | | | | |')
            notes = [f'formerly `{o}` ({mtag(t)})' for o, t, _ in former.get(v, [])] + \
                    [f'replaces {vlink(o, slug(form))} ({mtag(t)})' for o, t, _ in replaces.get(v, [])]
            var_cell = f'`{v}`' + ''.join(f'<br><sub>{x}</sub>' for x in notes)
            L.append(f'| {i} | {var_cell} | {label} | {r["Field Type"]} | {values_summary(r)} | '
                     f'{"✔" if r["Required Field?"] == "y" else ""} | {"🔒" if r["Identifier?"] == "y" else ""} | '
                     f'{mtag(intro_of(v))} | {lc_cell} |')
        L.append('')

    here = slug(form)
    olds = [(o, v, t, rel) for v in d['fields'] + d['removed'] for o, t, rel in former.get(v, [])]
    if olds:
        L.append('## ✏️ Former Variable Names\n')
        L.append('Variables in this instrument that had a different name in earlier releases. '
                 'Their history before the rename is included under the current name.\n')
        L.append('| # | Former name | Current name | Relation | Renamed in |\n| :-: | :-- | :-- | :-- | :-: |')
        for i, (o, v, t, rel) in enumerate(olds, 1):
            em, lab = REL[rel]
            L.append(f'| {i} | `{o}` | [`{v}`](#{v}) | {em} {lab} | {mtag(t)} |')
        L.append('')

    changed = [v for v in allv if any(e['kind'] != 'introduced' for e in hist[v]) or v in replaces]
    if changed:
        L.append('## 🕘 Change History\n')
        L.append('Fields listed in dictionary order. Each entry shows every release where that field changed.\n')
        for v in changed:
            evs = hist[v]
            n = sum(1 for e in evs if e['kind'] != 'introduced')
            L.append(f'### `{v}`\n')
            summ = clean(last_row[v]["Field Label"], 90) or v
            summ += f' — {n} change{"s" if n > 1 else ""}' if n else ' — introduced as a replacement'
            if former.get(v):
                summ += ' · formerly ' + ', '.join(f'<code>{o}</code>' for o, _, _ in former[v])
            L.append(f'<details><summary>{summ}</summary>\n')
            L.append('| Milestone | Date | What changed | Before | After |\n| :-: | :-: | :-- | :-- | :-- |')
            first = True
            for e in evs:
                t = e['tag']
                if e['kind'] == 'introduced':
                    name = f'as `{former[v][0][0]}` in ' if first and former.get(v) else ''
                    rep = ''.join(f'<br>↪️ replaces {vlink(o, here)}' + (f' — {clean(nt)}' if nt else '')
                                  for o, tt, nt in replaces.get(v, []) if tt == t)
                    L.append(f'| {mtag(t)} | {tagdate[t]} | 🆕 Introduced | | {name}{display(e["form"])}{rep} |')
                elif e['kind'] == 'reintroduced':
                    L.append(f'| {mtag(t)} | {tagdate[t]} | ♻️ Re-introduced | | {display(e["form"])} |')
                elif e['kind'] == 'removed':
                    rep = '<br>'.join(f'↪️ replaced by {vlink(nw, here)}' + (f' — {clean(nt)}' if nt else '')
                                      for nw, tt, nt in replaced_by.get(v, []) if tt == t)
                    L.append(f'| {mtag(t)} | {tagdate[t]} | ⚫ Removed | {display(e["form"])} | {rep} |')
                elif e['kind'] in ('renamed', 'recoded'):
                    em, lab = REL[e['kind']]
                    nt = f'<br><sub>{clean(e["note"])}</sub>' if e['note'] else ''
                    L.append(f'| {mtag(t)} | {tagdate[t]} | {em} {lab} | `{e["old"]}` | `{e["new"]}`{nt} |')
                    for k, old, new in e['changes']:
                        b, a = change_cells(k, old, new)
                        L.append(f'| | | {ATTR.get(k, k)} | {b} | {a} |')
                else:
                    for j, (k, old, new) in enumerate(e['changes']):
                        b, a = change_cells(k, old, new)
                        mt, dt = (mtag(t), tagdate[t]) if j == 0 else ('', '')
                        L.append(f'| {mt} | {dt} | {ATTR.get(k, k)} | {b} | {a} |')
            L.append('\n</details>\n')

    if d['removed']:
        L.append('## ⚫ Removed Fields\n')
        L.append('Variables that were once in this instrument and are no longer in the REDCap dictionary.\n')
        L.append('| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |\n| :-: | :-- | :-- | :-- | :-: | :-: | :-- |')
        for i, v in enumerate(d['removed'], 1):
            rb = ', '.join(vlink(nw, here) for nw, _, _ in replaced_by.get(v, [])) or '—'
            L.append(f'| {i} | [`{v}`](#{v}) | {clean(last_row[v]["Field Label"], 120)} | {last_row[v]["Field Type"]} | '
                     f'{mtag(intro_of(v))} | {mtag(removed_in(v))} | {rb} |')
        L.append('')
    open(os.path.join(OUT, DOC_DIR, slug(form)), 'w', encoding='utf-8').write('\n'.join(L) + ref_defs())

# ---------------------------------------------------------------- index
cats = collections.defaultdict(list)
for form in by_form:
    cats[category_for(form)].append(form)
cat_order = CATEGORY_ORDER + sorted(set(cats) - set(CATEGORY_ORDER))
n_by_status = collections.Counter(s['status'] for s in form_stats.values())
n_fields, n_removed = len(current), len(hist) - len(current)

I = [HEADER, f'[![Back to Main Document](https://img.shields.io/badge/back%20to%20main%20document-8A2BE2)]({UP}/README.md)\n',
     '# 📖 REDCap Data Dictionary — Field History\n',
     f'Every variable in the [REDCap data dictionary]({UP}/data/bridge2ai_voice_redcap_project_data_dictionary.csv): '
     'what it captures, which release introduced it, and every release where it changed. '
     'Milestones are the tagged releases of this repository; every milestone links to its GitHub release page. '
     'History is rebuilt from each release\'s dictionary.\n',
     '🗓️ **[Task Timeline](Task%20Timeline.md):** when each questionnaire and acoustic task was added to and retired '
     'from the Bridge2AI-Voice app, lined up with these REDCap releases.\n',
     f'**Instruments:** 🟢 {n_by_status["active"]} active · 🗄️ {n_by_status["retired"]} retired · '
     f'🗂️ {n_by_status["previous"]} previous versions · ⚫ {n_by_status["removed"]} removed  ',
     f'**Fields:** 📋 {n_fields} in REDCap · ⚫ {n_removed} removed · '
     f'{len(tags)} milestones ({mtag(tags[0][0])} → {mtag(tags[-1][0])}, {tags[0][1]} → {tags[-1][1]})\n',
     '## How to Read This\n',
     'Every instrument has one status. Fields inherit the status of their instrument, except removed fields, which are listed separately.\n',
     '| Status | Meaning |\n| :-- | :-- |',
     '| 🟢 **Active** | In REDCap and collected under a current protocol. |',
     '| 🗄️ **Retired** | No longer collected under any protocol. Still in REDCap so data from earlier participants remains valid. '
     'Matches the Retired Questionnaires tables on the [Adult](../../Adults/Questionnaires/Adult%20Questionnaires.md) and '
     '[Pediatric](../../Pediatrics/Questionnaires/Pediatric%20Questionnaires.md) questionnaire pages. |',
     '| 🗂️ **Previous version** | Superseded by a newer version of the same instrument (older eConsent versions). Still in REDCap. |',
     '| ⚫ **Removed** | No longer in the REDCap dictionary. Kept here for data collected before the removal. |',
     '',
     '- **Category → Instrument → Field.** Pick a category below, then open an instrument page. Fields are listed in dictionary order.',
     '- **Fields** table: variable name, label (what the field captures), type, allowed values, required (✔), '
     'identifier/PHI (🔒), the release that introduced it, and the release of its last change.',
     '- **Last changed** links to the field\'s entry under **Change History**: one row per attribute that changed, with before → after values. '
     'For choice lists, the entry shows options added (➕), removed (➖), or relabeled (✏️), not the whole list.',
     f'- **Instrument renames** (e.g., `diagnosis_*` → `d_*` in {mtag("v3.1.0")}) are shown once at the top of the instrument page, not on every field.',
     '- **Variable renames** are tracked in the [variable renames crosswalk](#️-renamed--replaced-variables). '
     'A ✏️ renamed or 🔁 recoded variable keeps one history under its current name, starting from its original name. '
     'A ↪️ replaced variable keeps its own history, linked to the variable that replaced it.\n',
     '## By Category\n',
     '| Category | 🟢 Active | 🗄️ Retired | 🗂️ Previous | ⚫ Removed | 📋 Fields in REDCap | ⚫ Removed fields |',
     '| :-- | :-: | :-: | :-: | :-: | :-: | :-: |']
for c in cat_order:
    fs = cats.get(c, [])
    if not fs:
        continue
    anchor = re.sub(r'[^a-z0-9 -]', '', c.lower()).replace(' ', '-')
    cnt = collections.Counter(form_stats[f]['status'] for f in fs)
    z = lambda n: n or '—'
    I.append(f'| [{c}](#{anchor}) | {z(cnt["active"])} | {z(cnt["retired"])} | {z(cnt["previous"])} | {z(cnt["removed"])} | '
             f'{sum(form_stats[f]["fields"] for f in fs)} | {z(sum(form_stats[f]["removed"] for f in fs))} |')
I.append('')

for c in cat_order:
    fs = sorted(cats.get(c, []), key=sort_key)
    if not fs:
        continue
    group = lambda s: [f for f in fs if form_stats[f]['status'] == s]
    act, ret, prv, rem = group('active'), group('retired'), group('previous'), group('removed')
    I.append(f'## {c}\n')
    if act:
        I.append('| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |')
        I.append('| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |')
        for i, f in enumerate(act, 1):
            s = form_stats[f]
            I.append(f'| {i} | [{display(f)}]({slug(f)}) | `{f}` | {s["fields"]} | {s["removed"] or "—"} | {s["changed"] or "—"} | {mtag(s["intro"])} | {mtag(s["last"])} |')
        I.append('')
    if ret:
        I.append(f'<details><summary>🗄️ {len(ret)} retired (no longer collected, still in REDCap)</summary>\n')
        I.append('| # | Instrument | Form Name | 📋 Fields | Retired from | Retired in | Introduced |\n| :-: | :-- | :-- | :-: | :-- | :-: | :-: |')
        for i, f in enumerate(ret, 1):
            s = form_stats[f]
            I.append(f'| {i} | [{display(f)}]({slug(f)}) | `{f}` | {s["fields"]} | {RETIRED[f]["from"]} | {mtag(RETIRED_IN.get(f))} | {mtag(s["intro"])} |')
        I.append('\n</details>\n')
    if prv:
        I.append(f'<details><summary>🗂️ {len(prv)} previous versions (superseded, still in REDCap)</summary>\n')
        I.append('| # | Instrument | Form Name | 📋 Fields | Superseded by | Introduced |\n| :-: | :-- | :-- | :-: | :-- | :-: |')
        for i, f in enumerate(prv, 1):
            s, sup = form_stats[f], superseded_by(f)
            I.append(f'| {i} | [{display(f)}]({slug(f)}) | `{f}` | {s["fields"]} | {f"[{display(sup)}]({slug(sup)})" if sup else "—"} | {mtag(s["intro"])} |')
        I.append('\n</details>\n')
    if rem:
        I.append(f'<details><summary>⚫ {len(rem)} removed (no longer in REDCap)</summary>\n')
        I.append('| # | Instrument | Form Name | Fields | Introduced | Removed in |\n| :-: | :-- | :-- | :-: | :-: | :-: |')
        for i, f in enumerate(rem, 1):
            s = form_stats[f]
            I.append(f'| {i} | [{display(f)}]({slug(f)}) | `{f}` | {s["removed"]} | {mtag(s["intro"])} | {mtag(s["removed_in"])} |')
        I.append('\n</details>\n')

# renames crosswalk
I.append('## ✏️ Renamed & Replaced Variables\n')
I.append(f'Crosswalk from earlier variable names to current ones, maintained in [`{RENAMES_CSV.split("/")[-1]}`]({UP}/{RENAMES_CSV}). '
         'Use it to line up data exported under different releases.\n')
I.append('| Relation | Meaning | Merge data across releases? |\n| :-- | :-- | :-- |')
I.append('| ✏️ Renamed | Same question and coding; only the variable name changed. | Yes, directly. |')
I.append('| 🔁 Renamed & recoded | Same question; field type or choice codes changed. | Yes, after mapping the codes shown in the change history. |')
I.append('| ↪️ Replaced | Question changed, or the variable was split or merged. | Only with study-specific rules. |\n')
I.append('| Milestone | Instrument | Former variable | Current variable | Relation | Note |\n| :-: | :-- | :-- | :-- | :-- | :-- |')
for r in lineage:
    em, lab = REL[r['relation']]
    new = r['new_variable']
    pg = page_of(new)
    I.append(f'| {mtag(r["milestone"])} | [{display(current.get(alias.get(new, new), last_row.get(new, {})).get("Form Name", ""))}]({pg}) | '
             f'`{r["old_variable"]}` | [`{new}`]({pg}#{alias.get(new, new)}) | {em} {lab} | {clean(r["note"]) or "—"} |')
I.append('')

# milestone table
retired_at = collections.defaultdict(list)
for f, t in RETIRED_IN.items():
    retired_at[t].append(display(f))
I.append('## Milestones\n')
I.append('Counts are fields. Instrument renames are not counted as field changes. '
         'Protocol retirements don\'t change the dictionary, so they are listed separately.\n')
I.append('| Milestone | Date | ➕ Added | ✏️ Changed | 🔤 Renamed | ⚫ Removed | 🗄️ Retired from protocol | Dictionary commits |')
I.append('| :-: | :-: | :-: | :-: | :-: | :-: | :-- | :-- |')
renamed_at = collections.Counter(r['milestone'] for r in lineage)
for i, (t, d) in enumerate(tags):
    add = sum(1 for evs in hist.values() for e in evs if e['tag'] == t and e['kind'] in ('introduced', 'reintroduced'))
    chg = sum(1 for evs in hist.values() for e in evs if e['tag'] == t and e['kind'] == 'changed')
    rem = sum(1 for evs in hist.values() for e in evs if e['tag'] == t and e['kind'] == 'removed')
    cs = commits.get(t, [])
    if i <= 5 and all(m.startswith(('init', 'update to')) for _, m in cs):
        cs_cell = '_archived export_'
    else:
        cs_cell = '<br>'.join(f'[`{h}`]({GH}/commit/{h}) {clean(m, 60)}' for h, m in cs) or '—'
    I.append(f'| {mtag(t)} | {d} | {add or "—"} | {chg or "—"} | {renamed_at.get(t) or "—"} | {rem or "—"} | '
             f'{", ".join(retired_at.get(t, [])) or "—"} | {cs_cell} |')
I.append('')
open(os.path.join(OUT, DOC_DIR, 'Data Dictionary.md'), 'w', encoding='utf-8').write('\n'.join(I) + ref_defs())


# ---------------------------------------------------------------- JSON export (Variable Explorer)
def plain(s, limit=None):
    return clean(s, limit).replace('\\|', '|')


def change_text(k, old, new):
    name = ATTR.get(k, k)
    if k in ('Required Field?', 'Identifier?', 'Matrix Ranking?'):
        return f'{name}: {YN(old)} → {YN(new)}'
    if k == 'Form Name':
        return f'Moved from {display(old)} to {display(new)}'
    if k == 'Choices, Calculations, OR Slider Labels' and '|' in old + new and ',' in old + new:
        a, b = parse_choices(old), parse_choices(new)
        parts = []
        added = [f'{c}={plain(b[c], 30)}' for c in b if c not in a]
        removed = [f'{c}={plain(a[c], 30)}' for c in a if c not in b]
        relab = [f'{c}: {plain(a[c], 25)} → {plain(b[c], 25)}' for c in b if c in a and a[c] != b[c]]
        if added: parts.append('added ' + ', '.join(added[:4]) + (' …' if len(added) > 4 else ''))
        if removed: parts.append('removed ' + ', '.join(removed[:4]) + (' …' if len(removed) > 4 else ''))
        if relab: parts.append('relabeled ' + '; '.join(relab[:3]) + (' …' if len(relab) > 3 else ''))
        if not parts and list(a) != list(b): parts.append('reordered')
        return 'Choices: ' + ('; '.join(parts) or 'changed')
    return f'{name}: {plain(old, 70) or "∅"} → {plain(new, 70) or "∅"}'


if JSON_OUT:
    records = []
    for form, d in by_form.items():
        fstat = form_stats[form]['status']
        for v in d['fields'] + d['removed']:
            row = current.get(v) or last_row[v]
            evs = []
            for e in hist[v]:
                t, kind = e['tag'], e['kind']
                if kind == 'introduced':
                    as_old = f' as {former[v][0][0]}' if former.get(v) else ''
                    rep = ''.join(f'; replaces {o}' for o, tt, _ in replaces.get(v, []) if tt == t)
                    evs.append([t, tagdate[t], 'Introduced', f'Added to {display(e["form"])}{as_old}{rep}'])
                elif kind == 'reintroduced':
                    evs.append([t, tagdate[t], 'Re-introduced', f'Added back to {display(e["form"])}'])
                elif kind == 'removed':
                    rep = ''.join(f'; replaced by {nw}' for nw, tt, _ in replaced_by.get(v, []) if tt == t)
                    evs.append([t, tagdate[t], 'Removed', f'Removed from {display(e["form"])}{rep}'])
                elif kind in ('renamed', 'recoded'):
                    txt = f'{e["old"]} → {e["new"]}' + (f'. {e["note"]}' if e['note'] else '')
                    evs.append([t, tagdate[t], REL[kind][1], txt])
                    for k, old, new in e['changes']:
                        evs.append([t, tagdate[t], 'Changed', change_text(k, old, new)])
                else:
                    evs.append([t, tagdate[t], 'Changed', '; '.join(change_text(k, o, n) for k, o, n in e['changes'])])
            if form in RETIRED and form in RETIRED_IN and v in current:
                rt = RETIRED_IN[form]
                evs.append([rt, tagdate[rt], 'Retired', f'{display(form)} was retired from the {RETIRED[form]["from"]} protocol'])
                evs.sort(key=lambda x: tag_idx[x[0]])
            vs = values_summary(row).replace('`', '')
            if vs.startswith('_') and vs.endswith('_'):
                vs = vs[1:-1]
            has_entry = any(e['kind'] != 'introduced' for e in hist[v]) or v in replaces
            records.append({
                'n': v, 'l': plain(row['Field Label'], 200), 'i': display(form), 'f': form,
                'c': category_for(form), 's': 'removed' if v not in current else fstat,
                't': row['Field Type'], 'v': vs, 'in': intro_of(v),
                'fo': [o for o, _, _ in former.get(v, [])],
                'p': f'{DOC_DIR}/{slug(form)}', 'a': v if has_entry else None, 'e': evs,
            })
    os.makedirs(os.path.dirname(os.path.abspath(JSON_OUT)), exist_ok=True)
    json.dump({'releases': [[t, d] for t, d in tags], 'variables': records},
              open(JSON_OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('json:', JSON_OUT, len(records), 'variables', file=sys.stderr)

print('pages:', len(by_form) + 1, 'fields:', len(hist), 'statuses:', dict(n_by_status), 'retired:', sorted(RETIRED))
