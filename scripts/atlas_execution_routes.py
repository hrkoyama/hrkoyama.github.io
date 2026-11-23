"""Execution-owned resource routes, resolved from reviewed sources and receipts.

Never infer an implementation or reference from a shared chapter/model name.
Generated execution pages are outputs, not inputs to this graph.
"""
from atlas_reference_catalog import load_reference_cases
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import struct
from urllib.parse import urlsplit

from atlas_execution_discovery import entry_url, load_discovery
from atlas_goal_availability import load_supplemental_examples
from atlas_problem_links import bilingual
from atlas_problem_routes import load_problem_routes

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = ORIGIN+'/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')


def load_execution_routes(root=ROOT):
    root = Path(root).resolve()
    problem_routes = load_problem_routes(root)
    sources = dict(problem_routes['source_sha256'])

    def read(path):
        raw = (root/path).read_bytes()
        sources[path] = sha256(raw).hexdigest()
        return json.loads(raw)

    catalog = read('catalog/atlas-problem-links.json')
    bindings = {row['id']: row for row in catalog['problems']}
    methods = {row['id']: row for row in read('catalog/atlas-methods.json')['methods']}
    equations = {row['id']: row for row in read('catalog/atlas-equations.json')['equations']}
    references = load_reference_cases(root, read)
    messages = read('numerical-methods-atlas/locales/messages.json')
    translations = {' '.join(row['en'].split()): row for row in messages.values() if row.get('en')}
    reference_records = {}
    for reference in references:
        translated = translations.get(' '.join(reference['title'].split()), {})
        title = {'ja': translated.get('ja'), 'en': reference['title']}
        bilingual(title, 'execution reference title')
        reference_records[reference['id']] = {**reference, 'title': title}

    def method_cards(identifiers):
        if not identifiers or len(identifiers) != len(set(identifiers)) or not set(identifiers) <= methods.keys():
            raise ValueError('Execution methods must be explicit, unique, known IDs')
        cards = []
        for ident in identifiers:
            method = methods[ident]
            if method['status'] != 'educational-example':
                raise ValueError('Execution navigation cannot promote method status: '+ident)
            cards.append({'id': ident, 'name': method['name'], 'status': method['status'],
                          'url': {lang: BASE+'methods/'+ident+'/?lang='+lang for lang in LANGUAGES}})
        return cards

    def physical_problem(ident):
        if ident is None:
            return None, []
        if ident not in problem_routes['problems']:
            raise ValueError('Unknown execution problem: '+ident)
        scoped = []
        for edge in bindings[ident].get('references', []):
            reference = reference_records[edge['id']]
            scoped.append({'id': edge['id'], 'title': reference['title'], 'kind': reference['kind'],
                           'relation': edge['relation'], 'note': deepcopy(edge['note']),
                           'url': {lang: BASE+'solutions/?lang='+lang+'#solution-'+edge['id']+'-'+lang for lang in LANGUAGES}})
        return deepcopy(problem_routes['problems'][ident]), scoped

    executions = {}
    for item in load_discovery(root)['examples']:
        case = item['execution']
        ident = item['id']
        problem, scoped = physical_problem(item['problem_id'])
        note = case.get('reference_notes')
        if note is None:
            actual = [row['description'] for row in case['references'] if row['type'] != 'primary-publication']
            note = {lang: ' '.join(row[lang] for row in actual) for lang in LANGUAGES} if actual else case['scope']
        bilingual(note, 'execution comparison scope')
        executions[ident] = {
            'id': ident, 'kind': 'common', 'name': case['name'],
            'methods': method_cards(case['method_ids']),
            'formulation': {**deepcopy(item['formula']),
                            'url': {lang: BASE+'equations/?lang='+lang+'#execution-'+ident+'-'+lang for lang in LANGUAGES}},
            'equations': [{'id': equation, 'name': equations[equation]['name'],
                           'url': {lang: BASE+'equations/?lang='+lang+'#'+equation+'-'+lang for lang in LANGUAGES}}
                          for equation in item['equation_ids']],
            'problem': problem,
            'figure': {**deepcopy(problem['image']), 'kind': 'problem-representative'},
            'references': {'url': {lang: entry_url(ident, lang)+'#'+ident+'-'+lang+'-validation' for lang in LANGUAGES},
                           'note': note, 'cases': scoped},
        }

    expansion = read('catalog/atlas-depth-expansion.json')
    reviewed_equations = expansion.get('case_equations', {})
    if not isinstance(reviewed_equations, dict) or not set(reviewed_equations) <= expansion['case_problem_ids'].keys():
        raise ValueError('Explicit equation bindings need a registered supplemental case')
    supplements = load_supplemental_examples(root, list(expansion['case_problem_ids']))
    for case in supplements:
        ident = case['id']
        if ident in executions:
            raise ValueError('Duplicate common/supplement execution identity: '+ident)
        sources.update(case['source_sha256'])
        problem, scoped = physical_problem(expansion['case_problem_ids'][ident])
        base = case['download'].rsplit('/', 1)[0]+'/'
        url = ORIGIN+base+'results/'+ident+'.png'
        path = urlsplit(url).path.lstrip('/')
        raw = (root/path).read_bytes()
        sources[path] = sha256(raw).hexdigest()
        if raw[:8] != b'\x89PNG\r\n\x1a\n':
            raise ValueError('Missing saved execution figure: '+ident)
        width, height = struct.unpack('>II', raw[16:24])
        if min(width, height) <= 0:
            raise ValueError('Invalid saved execution figure: '+ident)
        entry = {lang: BASE+'validation/'+ident+'/?lang='+lang for lang in LANGUAGES}
        explicit_equations = reviewed_equations.get(ident, {})
        if not isinstance(explicit_equations, dict):
            raise ValueError('Supplement equation binding must be a record')
        equation_ids = explicit_equations.get('ids', [])
        if not isinstance(equation_ids, list):
            raise ValueError('Supplement equation IDs must be a list')
        if len(equation_ids) != len(set(equation_ids)) or not set(equation_ids) <= equations.keys():
            raise ValueError('Unknown or repeated explicit supplement equation: '+ident)
        if equation_ids:
            bilingual(explicit_equations.get('note'), 'supplement equation scope')
        executions[ident] = {
            'id': ident, 'kind': 'supplement', 'name': case['title'],
            'methods': method_cards(case['method_ids']),
            'formulation': {'role': 'example-definition' if problem else 'diagnostic',
                            'latex': case.get('formulas', case.get('equations', [])), 'note': case['algorithm'],
                            'url': {lang: entry[lang]+'#'+ident+'-'+lang+'-algorithm' for lang in LANGUAGES}},
            # Only reviewed explicit bindings establish a shared model edge.
            # A related physical problem or matching prose never adds one.
            'equations': [{'id': equation, 'name': equations[equation]['name'],
                           'note': explicit_equations['note'],
                           'url': {lang: BASE+'equations/?lang='+lang+'#'+equation+'-'+lang for lang in LANGUAGES}}
                          for equation in equation_ids], 'problem': problem,
            'figure': {'url': url, 'sha256': sha256(raw).hexdigest(), 'width': width, 'height': height,
                       'kind': 'case-validation', 'caption': {
                           'ja': case['title']['ja']+'：この実行例の保存済み検証図。',
                           'en': case['title']['en']+': saved validation figure for this execution.'}},
            'references': {'url': {lang: entry[lang]+'#'+ident+'-'+lang+'-validation' for lang in LANGUAGES},
                           'note': case['validation'], 'cases': scoped},
        }
    return {'schema_version': 1, 'executions': executions, 'source_sha256': dict(sorted(sources.items()))}
