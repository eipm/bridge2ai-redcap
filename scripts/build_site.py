#!/usr/bin/env python3
"""Build or serve the Bridge2AI-Voice Protocols & REDCap website (MkDocs + Material).

Usage:
  pip install -r website/requirements.txt
  python3 scripts/build_site.py serve            # local preview at http://127.0.0.1:8000/
  python3 scripts/build_site.py build            # static site in build/site/ (what CI deploys)
  python3 scripts/build_site.py serve --addr 127.0.0.1:8001

The repository's markdown stays the source of truth. This script assembles a site source in
build/site-src/ that mirrors the repository layout (so every relative link keeps working):
  - docs/**/*.md are copied with GitHub-only bits adjusted: the logo header and "back to" badges
    are dropped (the site has its own header and navigation), badge images become styled chips,
    <details> blocks get markdown="1" so the markdown inside them renders, and links to README.md
    point to the matching site page.
  - every other file under docs/, plus images/ and data/, is linked in as-is.
  - index.md (landing page), redcap.md and about.md are generated from README.md, and
    explorer.md is the Variable Explorer, fed by a JSON export of the field history.
  - build/mkdocs.yml is generated, including the navigation, from README.md and the
    data dictionary index.
"""
import json, os, re, shutil, subprocess, sys
from urllib.parse import quote, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
SRC = os.path.join(BUILD, 'site-src')
WEB = os.path.join(ROOT, 'website')
DD = 'docs/REDCap/Data Dictionary'
GH = 'https://github.com/eipm/bridge2ai-redcap'
SITE_URL = 'https://eipm.github.io/bridge2ai-redcap/'

mode = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ('build', 'serve') else 'build'
addr = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--addr' and i + 1 < len(sys.argv)), '127.0.0.1:8000')


def read(path):
    return open(os.path.join(ROOT, path), encoding='utf-8').read()


def write(rel, text):
    p = os.path.join(SRC, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


# ---------------------------------------------------------------- markdown adjustments for the site
HEADER_RE = re.compile(r'\A\s*<p align="center">.*?</p>\s*', re.S)
BACK_RE = re.compile(r'^\[!\[Back to [^\]]*\]\(https://img\.shields\.io/[^)]*\)\]\([^)]*\)\s*$\n?', re.M)
BADGE_RE = re.compile(r'\[!\[([^\]]*)\]\(https://img\.shields\.io/badge/(?:[^()]|\([^()]*\))*\)\]\(((?:[^()]|\([^()]*\))*)\)')
README_RE = re.compile(r'((?:\.\./)*)README\.md(#[^)\s"\'>]*)?')


def readme_target(m):
    anchor = (m.group(2) or '').lower()
    if 'redcap' in anchor:
        page = 'redcap.md'
    elif any(k in anchor for k in ('cite', 'credit', 'license')):
        page = 'about.md'
    else:
        page = 'index.md'
    return m.group(1) + page


LINK_RE = re.compile(r'\]\(<?([^)\s>#]+)(#[^)\s>]*)?>?\)')


def folder_links(md, rel):
    """A link to a repository folder works on GitHub (it lists the folder) but not on a static
    site, so point it at the folder on GitHub."""
    def fix(m):
        target = m.group(1)
        if re.match(r'[a-z]+:', target) or '.' in os.path.basename(unquote(target)):
            return m.group(0)
        path = os.path.normpath(os.path.join(os.path.dirname(rel), unquote(target)))
        if os.path.isdir(os.path.join(ROOT, path)) and not path.startswith('..'):
            return f']({GH}/tree/main/{quote(path)})'
        return m.group(0)
    return LINK_RE.sub(fix, md)


RAW_ATTR_RE = re.compile(r'(<(?:img|source|video|audio|a)\b[^>]*?\b(?:src|href|srcset)=")([^"]+)"')


def raw_html_paths(md):
    """MkDocs rewrites markdown links for its page URLs (docs/x.md is served at docs/x/), but not
    paths inside raw HTML, so give those the extra '../' themselves."""
    def fix(m):
        url = m.group(2)
        if re.match(r'^([a-z]+:|/|#)', url):
            return m.group(0)
        path, sep, frag = url.partition('#')
        if path.endswith('.md'):
            path = path[:-3] + '/'
        return f'{m.group(1)}../{path}{sep}{frag}"'
    return RAW_ATTR_RE.sub(fix, md)


def adjust(md, rel=''):
    md = folder_links(md, rel)
    md = HEADER_RE.sub('', md, count=1)
    if rel and not rel.endswith('/index.md'):
        md = raw_html_paths(md)
    md = BACK_RE.sub('', md)
    md = BADGE_RE.sub(lambda m: f'[{m[1]}]({m[2]}){{ .b2ai-chip }}', md)
    md = re.sub(r'<details>', '<details markdown="1">', md)
    md = md.replace('#gh-light-mode-only', '#only-light').replace('#gh-dark-mode-only', '#only-dark')
    md = README_RE.sub(readme_target, md)
    md = re.sub(r'\]\((?:\./)?LICENSE\)', f']({GH}/blob/main/LICENSE)', md)
    return md


# ---------------------------------------------------------------- assemble build/site-src
shutil.rmtree(SRC, ignore_errors=True)
os.makedirs(SRC)
for d, _, files in os.walk(os.path.join(ROOT, 'docs')):
    for f in files:
        if f == '.DS_Store':
            continue
        src = os.path.join(d, f)
        rel = os.path.relpath(src, ROOT)
        dst = os.path.join(SRC, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if f.endswith('.md'):
            write(rel, adjust(open(src, encoding='utf-8').read(), rel))
        else:
            os.symlink(src, dst)
for d in ('images', 'data'):
    os.symlink(os.path.join(ROOT, d), os.path.join(SRC, d))
shutil.copytree(os.path.join(WEB, 'assets'), os.path.join(SRC, 'assets'))

# Variable Explorer data: every variable and its history, from the release tags
subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'build_data_dictionary_docs.py'), ROOT,
                os.path.join(BUILD, 'dd-check'), f'--json={os.path.join(SRC, "assets", "data", "variables.json")}'],
               check=True, stdout=subprocess.DEVNULL)

# Warn (don't fail) when the committed field-history pages are older than the release tags
stale = subprocess.run(['diff', '-rq', '-x', 'Task Timeline.md', os.path.join(BUILD, 'dd-check', DD), os.path.join(ROOT, DD)],
                       capture_output=True, text=True).stdout.strip()
if stale:
    msg = 'The field-history pages are out of date; run scripts/build_data_dictionary_docs.py and commit the result.'
    print(f'::warning::{msg}' if os.environ.get('GITHUB_ACTIONS') else f'WARNING: {msg}', file=sys.stderr)

# ---------------------------------------------------------------- facts for the landing page
readme = read('README.md')
version = re.search(r'^version:\s*(\S+)', read('CITATION.cff'), re.M)[1]
released = re.search(r'^date-released:\s*(\S+)', read('CITATION.cff'), re.M)[1]
redcap_ver = (re.search(r'badge/REDCap-([0-9.]+)-', readme) or [None, ''])[1]
dd_index = read(f'{DD}/Data Dictionary.md')
n_fields = re.search(r'📋 (\d+) in REDCap', dd_index)[1]
n_active = re.search(r'🟢 (\d+) active', dd_index)[1]
n_releases = len(subprocess.run(['git', '-C', ROOT, 'tag'], capture_output=True, text=True).stdout.split())


def md_to_url(path):
    """Site URL (relative to the site root) of a markdown page, for MkDocs directory URLs."""
    stem = unquote(path)[:-3]
    stem = stem[:-len('index')] if stem.endswith('/index') or stem == 'index' else stem + '/'
    return quote(stem, safe='/')


def tiles(section_title):
    """Protocol / resource tiles from a README section (### heading up to the next ###)."""
    m = re.search(rf'^### [^\n]*{re.escape(section_title)}\n(.*?)(?=^### |^## )', readme, re.S | re.M)
    out = []
    for td in re.findall(r'<td[^>]*>(.*?)</td>', m[1], re.S):
        href = re.search(r'href="([^"]+)"', td)[1]
        name = re.sub(r'<[^>]+>', '', re.search(r'<strong>(.*?)</strong>', td, re.S)[1]).replace('&amp;', '&').strip()
        icon = re.search(r'<img src="([^"]+)"', td)
        subs = [re.sub(r'<[^>]+>', '', s).strip() for s in re.findall(r'<sub>(.*?)</sub>', td, re.S)]
        out.append({'name': name, 'href': href, 'url': md_to_url(href), 'icon': icon[1] if icon else None,
                    'facts': [re.sub(r'^\W+', '', s).strip() for s in subs]})
    return out


adult = tiles('Adult Protocols')
peds = tiles('Pediatric Protocols')
res_blocks = re.findall(r'#### Additional Resources\n(.*?)(?=^### |^## )', readme, re.S | re.M)
adult_res = [t for t in re.findall(r'<td[^>]*>(.*?)</td>', res_blocks[0], re.S)]
peds_res = [t for t in re.findall(r'<td[^>]*>(.*?)</td>', res_blocks[1], re.S)]


def res_tiles(tds):
    out = []
    for td in tds:
        href = re.search(r'href="([^"]+)"', td)[1]
        name = re.sub(r'<[^>]+>', '', re.search(r'<strong>(.*?)</strong>', td, re.S)[1]).strip()
        name = re.sub(r'^All (Adult|Pediatric) ', '', name)
        out.append({'name': name, 'href': href, 'url': md_to_url(href)})
    return out


adult_res, peds_res = res_tiles(adult_res), res_tiles(peds_res)
tags = subprocess.run(['git', '-C', ROOT, 'for-each-ref', '--sort=-creatordate', '--count=3',
                       '--format=%(refname:short)|%(creatordate:short)', 'refs/tags'], capture_output=True, text=True).stdout.split()
releases = [{'tag': t.split('|')[0].replace('tags/', ''), 'date': t.split('|')[1]} for t in tags]
if releases and releases[0]['tag'] != f'v{version}':
    releases.insert(0, {'tag': f'v{version}', 'date': released, 'upcoming': True})
    releases = releases[:3]

landing = {
    'template': 'home.html', 'title': 'Home', 'hide': ['navigation', 'toc'],
    'version': f'v{version}', 'released': released, 'redcap_version': redcap_ver,
    'stats': [[f'{int(n_fields):,}', 'fields in REDCap'], [n_active, 'active instruments'],
              [str(len(adult) + len(peds)), 'protocols'], [str(n_releases), 'tagged releases since 2023']],
    'adult': adult, 'pediatric': peds, 'adult_resources': adult_res, 'pediatric_resources': peds_res,
    'releases': releases, 'repo': GH,
}
write('index.md', '---\n' + json.dumps(landing, ensure_ascii=False, indent=1) + '\n---\n')


# ---------------------------------------------------------------- README sections as site pages
def readme_section(title_word):
    m = re.search(rf'^## [^\n]*{title_word}[^\n]*\n(.*?)(?=^## |\Z)', readme, re.S | re.M)
    return m[1].strip() + '\n'


redcap_md = readme_section('REDCap')
redcap_md = re.sub(r'^### ', '## ', redcap_md, flags=re.M)
write('redcap.md', adjust('# REDCap Project\n\n' + redcap_md, 'redcap.md'))
about = '# About\n\n## How to Cite\n\n' + readme_section('How to Cite') + '\n## Credits\n\n' + readme_section('Credits') + \
        '\n## License\n\n' + readme_section('License')
write('about.md', adjust(about, 'about.md'))
write('CREDITS.md', adjust(read('CREDITS.md'), 'CREDITS.md'))
write('explorer.md', '---\ntemplate: explorer.html\ntitle: Variable Explorer\nhide:\n  - navigation\n  - toc\n---\n')


# ---------------------------------------------------------------- navigation
def dd_nav():
    nav, cat, group = [], None, 'active'
    for line in dd_index.split('\n'):
        if line.startswith('## '):
            t = line[3:].strip()
            if t in ('How to Read This', 'By Category', 'Milestones') or 'Renamed & Replaced' in t:
                cat = None
                continue
            cat = {'title': t, 'groups': {'active': [], 'retired': [], 'previous': [], 'removed': []}}
            nav.append(cat)
            group = 'active'
        elif cat and line.startswith('<details><summary>'):
            group = 'retired' if '🗄️' in line else 'previous' if '🗂️' in line else 'removed'
        elif cat:
            m = re.match(r'\| \d+ \| \[([^\]]+)\]\(([^)]+)\) \| `[^`]+` \|', line)
            if m:
                cat['groups'][group].append({m[1]: f'{DD}/{m[2]}'})
    out = [{'Overview': f'{DD}/Data Dictionary.md'}, {'Task Timeline': f'{DD}/Task Timeline.md'}]
    for c in nav:
        items = list(c['groups']['active'])
        for g, label in (('retired', 'Retired'), ('previous', 'Previous versions'), ('removed', 'Removed')):
            if c['groups'][g]:
                items.append({label: c['groups'][g]})
        out.append({c['title']: items})
    return out


def protocol_nav(tiles_, res):
    return [{'Protocols': [{t['name']: unquote(t['href'])} for t in tiles_]}] + \
           [{r['name']: unquote(r['href'])} for r in res]


nav = [
    {'Home': 'index.md'},
    {'Protocols': [{'Adults': protocol_nav(adult, adult_res)}, {'Pediatrics': protocol_nav(peds, peds_res)}]},
    {'Data Dictionary': dd_nav()},
    {'Variable Explorer': 'explorer.md'},
    {'REDCap': [{'REDCap Project': 'redcap.md'}, {'Instruments': 'docs/REDCap/Instruments.md'}]},
    {'About': [{'About': 'about.md'}, {'Credits': 'CREDITS.md'}]},
]


# ---------------------------------------------------------------- mkdocs.yml
class Raw(str):
    """A YAML value written as-is (e.g. a !!python/name tag)."""


def yaml(v, ind=0):
    pad = '  ' * ind
    if isinstance(v, dict):
        return ''.join(f'{pad}{json.dumps(k) if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", k) else k}:'
                       + (('\n' + yaml(x, ind + 1)) if isinstance(x, (dict, list)) and x else ' ' + scalar(x) + '\n')
                       for k, x in v.items())
    if isinstance(v, list):
        out = ''
        for x in v:
            if isinstance(x, (dict, list)) and x:
                body = yaml(x, ind + 1)
                out += f'{pad}- ' + body.lstrip()
            else:
                out += f'{pad}- {scalar(x)}\n'
        return out
    return pad + scalar(v) + '\n'


def scalar(x):
    if isinstance(x, Raw):
        return str(x)
    if isinstance(x, bool):
        return 'true' if x else 'false'
    if isinstance(x, (int, float)):
        return str(x)
    if x == [] or x == {}:
        return json.dumps(x)
    return json.dumps(x, ensure_ascii=False)


config = {
    'site_name': 'Bridge2AI-Voice Protocols & REDCap',
    'site_description': 'Protocols, questionnaires, acoustic tasks and the REDCap project of the Bridge2AI-Voice consortium.',
    'site_url': SITE_URL,
    'repo_url': GH, 'repo_name': 'eipm/bridge2ai-redcap', 'edit_uri': '',
    # footer text (copyright, NIH project, license): website/overrides/partials/copyright.html
    'docs_dir': 'site-src', 'site_dir': 'site',
    'theme': {
        'name': 'material', 'custom_dir': '../website/overrides',
        'logo': 'images/main_logo_white.svg', 'favicon': 'images/main_logo_black.svg',
        'font': {'text': 'Open Sans', 'code': 'JetBrains Mono'},
        'palette': [
            {'media': '(prefers-color-scheme: light)', 'scheme': 'default', 'primary': 'custom', 'accent': 'custom',
             'toggle': {'icon': 'material/weather-night', 'name': 'Switch to dark mode'}},
            {'media': '(prefers-color-scheme: dark)', 'scheme': 'slate', 'primary': 'custom', 'accent': 'custom',
             'toggle': {'icon': 'material/weather-sunny', 'name': 'Switch to light mode'}},
        ],
        'features': ['navigation.tabs', 'navigation.top', 'navigation.tracking', 'search.suggest',
                     'search.highlight', 'toc.follow'],
        'icon': {'repo': 'fontawesome/brands/github'},
    },
    'extra_css': ['assets/stylesheets/b2ai.css'],
    'extra': {'generator': False, 'social': [{'icon': 'fontawesome/brands/github', 'link': GH}]},
    'plugins': ['search'],
    'markdown_extensions': ['tables', 'attr_list', 'md_in_html', 'admonition', 'pymdownx.superfences',
                            {'toc': {'permalink': True, 'slugify': Raw('!!python/name:b2ai_slug.slugify')}}],
    'exclude_docs': '.DS_Store\n',
    'not_in_nav': '/docs/**\n',
    'validation': {'omitted_files': 'info', 'absolute_links': 'info', 'unrecognized_links': 'info',
                   'anchors': 'info', 'links': {'not_found': 'warn'}},
    'nav': nav,
}
open(os.path.join(BUILD, 'mkdocs.yml'), 'w', encoding='utf-8').write(
    '# Generated by scripts/build_site.py — edit that script, not this file.\n' + yaml(config))

# ---------------------------------------------------------------- run MkDocs
env = dict(os.environ, PYTHONPATH=WEB + os.pathsep + os.environ.get('PYTHONPATH', ''))
cmd = [sys.executable, '-m', 'mkdocs', mode, '-f', os.path.join(BUILD, 'mkdocs.yml')]
if mode == 'serve':
    cmd += ['-a', addr]
print('Running:', ' '.join(cmd), file=sys.stderr)
sys.exit(subprocess.call(cmd, env=env, cwd=BUILD))
