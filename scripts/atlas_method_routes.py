"""Source-first routes from a method to reviewed problems and their evidence."""
from atlas_reference_catalog import load_reference_cases
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

from atlas_problem_links import bilingual, problem_path, validate_catalog
from atlas_problem_routes import load_problem_routes

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')


def build_method_routes(catalog, method_records, problem_cards, equation_records, reference_records):
    """Invert explicit method edges, preserving each problem/reference context."""
    validate_catalog(catalog, problem_cards, equation_records, reference_records, method_records)
    source = {row['id']: row for row in catalog['problems']}
    methods = {ident: {'method_id': ident, 'status': method['status'], 'equations': [], 'problems': [], 'references': []}
               for ident, method in method_records.items()}
    for ident, card in problem_cards.items():
        problem_path(ident)
        row = source[ident]
        actual = {method for run in card['executions'] for method in run['method_ids']}
        if not actual <= method_records.keys():
            raise ValueError('Unknown execution method: '+ident)
        selected = list(dict.fromkeys([*row.get('method_ids', []), *sorted(actual)]))
        for method_id in selected:
            route = methods[method_id]
            runs = [run for run in card['executions'] if method_id in run['method_ids']]
            if runs and route['status'] != 'educational-example':
                raise ValueError('Execution links cannot promote a method status: '+method_id)
            reference_url = {lang: card['hub'][lang]+'#references-'+lang for lang in LANGUAGES}
            problem = {**deepcopy(card), 'role': 'execution' if runs else 'related',
                       'method_note': deepcopy(row['method_note']), 'reference_url': reference_url,
                       'executions': deepcopy(runs)}
            route['problems'].append(problem)
            for equation_id in row.get('equation_ids', []):
                equation = next((item for item in route['equations'] if item['id'] == equation_id), None)
                if equation is None:
                    original = equation_records[equation_id]
                    equation = {'id': equation_id, 'name': original['name'], 'problem_ids': [],
                                'url': {lang: ORIGIN+BASE+'equations/?lang='+lang+'#'+equation_id+'-'+lang for lang in LANGUAGES}}
                    route['equations'].append(equation)
                equation['problem_ids'].append(ident)
            context = {'problem_id': ident, 'problem_name': card['name'], 'reference_url': reference_url, 'cases': []}
            for binding in row.get('references', []):
                ref_id = binding['id']
                reference = reference_records[ref_id]
                context['cases'].append({
                    'id': ref_id, 'title': reference['title'], 'kind': reference['kind'],
                    'relation': binding['relation'], 'note': deepcopy(binding['note']),
                    'url': {lang: ORIGIN+BASE+'solutions/?lang='+lang+'#solution-'+ref_id+'-'+lang for lang in LANGUAGES},
                    'view': {lang: reference.get('view', {}).get(lang) or
                             ORIGIN+BASE+'?lang='+lang+'#/exact-solutions?case='+ref_id
                             for lang in LANGUAGES}})
            route['references'].append(context)
    return methods


def load_method_routes(root=ROOT):
    root = Path(root).resolve()
    routes = load_problem_routes(root)
    sources = dict(routes['source_sha256'])

    def read(path):
        data = (root/path).read_bytes()
        sources[path] = sha256(data).hexdigest()
        return json.loads(data)

    catalog = read('catalog/atlas-problem-links.json')
    methods = {row['id']: row for row in read('catalog/atlas-methods.json')['methods']}
    equations = {row['id']: row for row in read('catalog/atlas-equations.json')['equations']}
    raw_references = load_reference_cases(root, read)
    messages = read('numerical-methods-atlas/locales/messages.json')
    translations = {' '.join(row['en'].split()): row for row in messages.values() if row.get('en')}
    references = {}
    for reference in raw_references:
        translated = translations.get(' '.join(reference['title'].split()), {})
        title = {'ja': translated.get('ja'), 'en': reference['title']}
        bilingual(title, 'method reference title')
        references[reference['id']] = {**reference, 'title': title}
    return {'schema_version': 1,
            'methods': build_method_routes(catalog, methods, routes['problems'], equations, references),
            'source_sha256': dict(sorted(sources.items()))}
