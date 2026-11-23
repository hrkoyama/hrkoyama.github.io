"""Resolve reviewed problem relationships against existing public evidence."""
from atlas_reference_catalog import load_reference_cases
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlsplit, urlunsplit
import ast
import hashlib
import json
import re
import shlex
import zipfile

from atlas_execution_discovery import load_discovery, entry_url
from atlas_goal_availability import load_supplemental_examples

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/problems/'
SOURCE = 'catalog/atlas-problem-links.json'
LANGUAGES = ('ja', 'en')


def problem_path(ident):
    if not isinstance(ident, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', ident):
        raise ValueError('Invalid problem ID: '+repr(ident))
    return BASE+ident+'/'


def problem_url(ident, language=None):
    if language is not None and language not in LANGUAGES:
        raise ValueError('Unsupported language')
    return ORIGIN+problem_path(ident)+('?lang='+language if language else '')


def validate_public_url(value, root=ROOT):
    """Accept a real same-site public file, never credentials or private paths."""
    if not isinstance(value, str) or not value:
        raise ValueError('Missing public URL')
    raw = urlsplit(value)
    raw_path = unquote(raw.path)
    if any(part in {'.', '..'} or part.startswith('.') for part in Path(raw_path).parts if part not in {'/'}):
        raise ValueError('Non-public URL path: '+value)
    url = urlsplit(urljoin(ORIGIN+'/', value))
    if url.scheme != 'https' or url.netloc != 'hrkoyama.github.io' or url.username or url.password:
        raise ValueError('Not an authorized public URL: '+value)
    root = Path(root).resolve()
    target = (root/unquote(url.path).lstrip('/')).resolve()
    if not target.is_relative_to(root):
        raise ValueError('Public URL leaves the site: '+value)
    if target.is_dir():
        target = target/'index.html'
    if not target.is_file():
        raise ValueError('Missing public target: '+value)
    return urlunsplit(url)


def language_url(value, language, root):
    parts = urlsplit(value)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query['lang'] = language
    return validate_public_url(urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment)), root)


def bilingual(value, where):
    if not isinstance(value, dict) or any(not isinstance(value.get(lang), str) or not value[lang].strip() for lang in LANGUAGES):
        raise ValueError('Missing bilingual text: '+where)


def validate_catalog(catalog, problem_ids, equation_ids, reference_ids, method_ids):
    if catalog.get('schema_version') != 1:
        raise ValueError('Unsupported problem-link catalog')
    bilingual(catalog.get('scope'), 'scope')
    rows = catalog.get('problems', [])
    identifiers = [row['id'] for row in rows]
    if len(identifiers) != len(set(identifiers)) or set(identifiers) != set(problem_ids):
        raise ValueError('Problem links must cover every published problem exactly once')
    for row in rows:
        problem_path(row['id'])
        for key, allowed in [('equation_ids', equation_ids), ('method_ids', method_ids)]:
            values = row.get(key, [])
            if not isinstance(values, list) or len(values) != len(set(values)) or not set(values) <= set(allowed):
                raise ValueError('Unknown or duplicate '+key+': '+row['id'])
        for key in ['reference_note', 'method_note']:
            bilingual(row.get(key), row['id']+'.'+key)
        if not row.get('equation_ids'):
            bilingual(row.get('equation_note'), row['id']+'.equation_note')
        refs = row.get('references', [])
        if len(refs) != len({item['id'] for item in refs}):
            raise ValueError('Duplicate reference binding: '+row['id'])
        for item in refs:
            if item['id'] not in reference_ids or item.get('relation') not in {'same-problem', 'related-model'}:
                raise ValueError('Unknown reference or relation: '+row['id'])
            bilingual(item.get('note'), row['id']+'.reference')
        if 'code_evidence' in row:
            evidence = row['code_evidence']
            if not isinstance(evidence, list) or not evidence:
                raise ValueError('Missing curated code evidence: '+row['id'])
            for item in evidence:
                if not isinstance(item.get('path'), str) or not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', item.get('python_symbol', '')):
                    raise ValueError('Invalid curated code evidence: '+row['id'])
                bilingual(item.get('note'), row['id']+'.code_evidence')


def load_problem_links(root=ROOT):
    root = Path(root).resolve()
    receipts = {}

    def read(relative):
        path = root/relative
        data = path.read_bytes()
        receipts[relative] = hashlib.sha256(data).hexdigest()
        return json.loads(data)

    catalog = read(SOURCE)
    inventory = read('numerical-methods-atlas/test-cases/index.json')
    gallery = read('numerical-methods-atlas/gallery/index.json')
    methods_data = read('numerical-methods-atlas/methods/index.json')
    equations_data = read('catalog/atlas-equations.json')
    solutions = read('numerical-methods-atlas/solutions/index.json')
    reference_source = {'cases': load_reference_cases(root, read)}
    if solutions['source_sha256'] != receipts['numerical-methods-atlas/assets/reference-solutions.json']:
        raise ValueError('Refresh the reference-solution index before problem links')
    extra_source = 'catalog/atlas-reference-supplements.json'
    if (root/extra_source).is_file() and solutions.get('supplements_source_sha256') != receipts[extra_source]:
        raise ValueError('Refresh supplementary reference cards before problem links')
    problems = {row['id']: row for row in inventory['problems']}
    visuals = {row['id']: row for row in gallery['items']}
    methods = {row['id']: row for row in methods_data['methods']}
    equations = {row['id']: row for row in equations_data['equations']}
    references = {row['id']: row for row in solutions['cases']}
    if set(visuals) != set(problems) or set(references) != {row['id'] for row in reference_source['cases']}:
        raise ValueError('Stale visual or reference inventory')
    validate_catalog(catalog, problems, equations, references, methods)
    reviewed = {row['id']: row for row in catalog['problems']}

    discovery = load_discovery(root)
    read('catalog/atlas-execution-discovery.json')
    registry = read('numerical-methods-atlas/code-and-data/examples.json')
    receipt_url = validate_public_url(registry['verification_receipt'], root)
    receipt = read(urlsplit(receipt_url).path.lstrip('/'))
    if receipt.get('passed') is not True or receipt['registry_sha256'] != receipts['numerical-methods-atlas/code-and-data/examples.json']:
        raise ValueError('Successful current execution receipt is required')
    checks = {row['id']: row for row in receipt['examples']}
    common = {}
    for row in discovery['examples']:
        if checks[row['id']]['passed'] is not True or row['problem_id'] not in problems:
            raise ValueError('Invalid common problem execution: '+row['id'])
        common.setdefault(row['problem_id'], []).append(row)

    expansion = read('catalog/atlas-depth-expansion.json')
    supplemental_ids = list(dict.fromkeys(extra['id'] for row in problems.values() for extra in row.get('supplemental_examples', [])))
    supplements = {row['id']: row for row in load_supplemental_examples(root, supplemental_ids)}
    for row in supplements.values():
        receipts.update(row['source_sha256'])
    downloads = {ORIGIN+methods_data['code_base']: methods_data['code_release']['download']}
    for row in methods.values():
        if row.get('code_base') and row.get('code_download'):
            downloads[row['code_base']] = row['code_download']

    def public(value):
        return validate_public_url(value, root)

    archive_roots = {}

    def archive_directory(download):
        url = public(download)
        if url not in archive_roots:
            path = root/urlsplit(url).path.lstrip('/')
            with zipfile.ZipFile(path) as archive:
                names = [Path(name) for name in archive.namelist() if name.rstrip('/')]
            roots = {name.parts[0] for name in names}
            if len(roots) != 1 or any(name.is_absolute() or '..' in name.parts or len(name.parts) < 2 for name in names if name.suffix):
                raise ValueError('Ambiguous code archive working directory: '+url)
            archive_roots[url] = roots.pop()+'/'
            receipts[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        return archive_roots[url]

    def reading(chapter, lang):
        edition = lang if (root/'numerical-methods-atlas'/lang/'read'/chapter/'index.html').is_file() else 'en'
        return public('/numerical-methods-atlas/'+edition+'/read/'+chapter+'/')

    def reference_data(record):
        rows = []
        for entry in record.get('references', []):
            if entry.get('type') == 'primary-publication' or urlsplit(entry.get('url', '')).netloc != 'hrkoyama.github.io':
                continue
            bilingual(entry['description'], 'execution reference')
            rows.append({'url': public(entry['url']), 'type': entry['type'], 'description': entry['description']})
        return rows

    output = []
    for problem in inventory['problems']:
        ident = problem['id']
        row, visual = reviewed[ident], visuals[ident]
        image_path = root/visual['image'].lstrip('/')
        if hashlib.sha256(image_path.read_bytes()).hexdigest() != visual['image_sha256']:
            raise ValueError('Problem image differs from its receipt: '+ident)
        runs, formulations = [], []
        for binding in common.get(ident, []):
            record = binding['execution']
            release = record['release']
            base = release['manifest'].rsplit('/', 1)[0]+'/'
            downloads[base] = release['download']
            command = record['commands']
            run_argv = command.get('run_argv') or shlex.split(command.get('run', ''))
            script = run_argv[1] if len(run_argv) > 1 else None
            code = [public(base+script)] if isinstance(script, str) and script.endswith('.py') else []
            tests = [public(base+arg) for arg in (command.get('tests_argv') or shlex.split(command.get('tests', ''))) if arg.endswith('.py')]
            ref_data = reference_data(record)
            reference_note = record.get('reference_notes') or {
                lang: ' '.join(item['description'][lang] for item in ref_data) or record['scope'][lang] for lang in LANGUAGES}
            runs.append({'id': record['id'], 'kind': 'common', 'name': record['name'], 'method_ids': record['method_ids'],
                         'guide': {lang: public(entry_url(record['id'], lang)) for lang in LANGUAGES},
                         'scope': record['scope'], 'assumptions': record['assumptions'], 'limits': record.get('failure_scope', record['scope']),
                         'input': public(record['inputs']['url']), 'download': public(release['download']),
                         'verification': receipt_url, 'manifest': public(release['manifest']),
                         'commands': [command[key] for key in ['install', 'run', 'tests'] if command.get(key)],
                         'reference_note': reference_note, 'reference_data': ref_data,
                         'results': [public(item['url']) for item in record['outputs']],
                         'code_urls': code, 'test_urls': tests, 'source_scope': 'package'})
            formulations.append({'id': 'common-'+record['id'], 'name': record['name'], 'source': 'common',
                                 'role': binding['formula']['role'], 'latex': binding['formula']['latex'], 'note': binding['formula']['note']})
        for extra in problem.get('supplemental_examples', []):
            case = supplements[extra['id']]
            if expansion['case_problem_ids'].get(case['id']) != ident or case['url'] != extra['url'] or case['title'] != extra['name']:
                raise ValueError('Supplement is bound to a different problem: '+case['id'])
            base = (ORIGIN+case['download']).rsplit('/', 1)[0]+'/'
            downloads[base] = ORIGIN+case['download']
            code = [public(base+name) for name in case.get('code_files', [])]
            if not code:
                code = [public(url) for url in case['code_urls'] if urlsplit(url).path.endswith('/run.py')]
            runs.append({'id': case['id'], 'kind': 'supplement', 'name': case['title'], 'method_ids': case['method_ids'],
                         'guide': {lang: language_url(case['url'], lang, root) for lang in LANGUAGES},
                         'scope': case['summary'], 'assumptions': case['assumptions'], 'limits': case['limits'],
                         'input': public(base+'inputs.json'), 'download': public(case['download']),
                         'verification': public(case['verification']), 'manifest': public(base+'source-manifest.json'),
                         'commands': ['python -m pip install -r requirements.txt', 'python -m pytest -q', 'python run.py --input inputs.json --output output'],
                         'reference_note': case['validation'], 'reference_data': [], 'results': [public(case['results'])],
                         'code_urls': code, 'test_urls': [public(url) for url in case['test_urls']], 'source_scope': 'package'})
            latex = case.get('formulas', case.get('equations', []))
            if latex:
                formulations.append({'id': 'supplement-'+case['id'], 'name': case['title'], 'source': 'supplement',
                                     'role': 'example-definition', 'latex': latex, 'note': case['summary']})
        actual_methods = set(method for run in runs for method in run['method_ids'])
        if not actual_methods <= methods.keys():
            raise ValueError('Execution names an unknown method: '+ident)
        selected_methods = list(dict.fromkeys([*row.get('method_ids', []), *sorted(actual_methods)]))
        method_links = [{'id': key, 'name': methods[key]['name'], 'status': methods[key]['status'],
                         'role': 'execution' if key in actual_methods else 'related',
                         'url': {lang: language_url(methods[key]['url'], lang, root) for lang in LANGUAGES}} for key in selected_methods]
        model_links = [{'id': key, 'name': equations[key]['name'], 'formula': equations[key]['formula'], 'note': equations[key]['note'],
                        'url': {lang: public('/numerical-methods-atlas/equations/?lang='+lang+'#'+key+'-'+lang) for lang in LANGUAGES}} for key in row['equation_ids']]
        reference_links = []
        for binding in row.get('references', []):
            ref = references[binding['id']]
            reference_links.append({key: ref[key] for key in ['id', 'kind', 'kind_label', 'title', 'formula', 'assumptions']} |
                                   {'relation': binding['relation'], 'note': binding['note'],
                                    'url': {lang: public(ref['view'][lang]) for lang in LANGUAGES}})
        code_checks = []
        for evidence in row.get('code_evidence', problem['evidence']):
            if not evidence.get('python_symbol'):
                continue
            if evidence['path'] not in {item['path'] for item in problem['evidence']}:
                raise ValueError('Curated code evidence is outside the problem sources: '+ident)
            source = root/evidence['path']
            tree = ast.parse(source.read_text())
            if evidence['python_symbol'] not in {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}:
                raise ValueError('Missing problem validation function: '+ident)
            base = next((directory for directory in source.parents if (directory/'source-manifest.json').is_file()), None)
            if base is None:
                raise ValueError('Validation code has no immutable release: '+str(source))
            base_url = ORIGIN+'/'+base.relative_to(root).as_posix()+'/'
            relative = source.relative_to(base).as_posix()
            download = public(downloads[base_url]) if base_url in downloads else None
            code_checks.append({'url': public('/'+evidence['path']), 'path': evidence['path'], 'symbol': evidence['python_symbol'],
                                'commands': ['python -m pytest -q '+relative+' -k '+evidence['python_symbol']],
                                'run_from': archive_directory(download) if download else base.relative_to(root).as_posix()+'/', 'download': download,
                                **({'note': evidence['note']} if evidence.get('note') else {})})
        output.append({'schema_version': 1, 'id': ident, 'name': problem['name'], 'url': problem_url(ident),
                       'hub': {lang: problem_url(ident, lang) for lang in LANGUAGES},
                       'image': {'url': public(visual['image']), 'sha256': visual['image_sha256'], 'width': visual['width'], 'height': visual['height'],
                                 'caption': visual['caption'], 'source_kind': visual['source_kind']},
                       'reading': {lang: public(problem['reading'][lang]) for lang in LANGUAGES},
                       'conditions': {lang: public('/numerical-methods-atlas/test-cases/?lang='+lang+'#'+ident+('' if lang == 'ja' else '-en')) for lang in LANGUAGES},
                       'equations': model_links, 'equation_note': row.get('equation_note', {
                           'ja': 'この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。',
                           'en': 'Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.'}),
                       'formulations': formulations, 'references': reference_links, 'reference_note': row['reference_note'],
                       'methods': method_links, 'method_note': row['method_note'], 'executions': runs, 'code_checks': code_checks})
    return {'schema_version': 1, 'url': ORIGIN+BASE, 'scope': catalog['scope'], 'problems': output, 'source_sha256': dict(sorted(receipts.items()))}
