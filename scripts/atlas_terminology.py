"""Strict editorial Japanese case wording; never alter canonical packet loaders."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re

MAPPING = 'catalog/atlas-terminology.json'
HELPER = 'scripts/atlas_terminology.py'
EXPECTED = {
    'radiation-transport': ('particles', {'title', 'summary', 'assumptions', 'limits'}),
    'radiation-convergence': ('particle-transport', {'title', 'assumptions', 'limits'}),
    'su-olson-diffusion1996': ('radiation-matter', {'summary', 'algorithm'}),
    'kepler-eccentricity': ('geometric-controls', {'algorithm'}),
}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def _sha(path):
    return sha256(path.read_bytes()).hexdigest()


def _local(root, name):
    parts = Path(name)
    path = root/parts
    _require(not parts.is_absolute() and '..' not in parts.parts and path.is_file()
             and not path.is_symlink() and path.resolve().is_relative_to(root), 'Unsafe editorial source')
    return path


def _plan(root):
    mapping = _local(root, MAPPING)
    helper = _local(root, HELPER)
    _require(_sha(helper) == _sha(Path(__file__)), 'Editorial helper differs from the executing source')
    raw = mapping.read_bytes()
    _require(len(raw) <= 65536, 'Editorial mapping exceeds its small fixed scope')
    data = json.loads(raw)
    _require(set(data) == {'schema_version', 'language', 'scope', 'cases'}
             and type(data['schema_version']) is int and data['schema_version'] == 1
             and data['language'] == 'ja' and isinstance(data['scope'], str) and data['scope'].strip(), 'Invalid terminology scope')
    _require(isinstance(data['cases'], dict) and set(data['cases']) == set(EXPECTED), 'Unreviewed terminology case')
    plans = {}
    dependencies = {MAPPING: sha256(raw).hexdigest(), HELPER: _sha(helper)}
    for ident, row in data['cases'].items():
        _require(isinstance(row, dict) and set(row) == {'source', 'fields', 'reason'}, 'Invalid case override')
        _require(isinstance(row['reason'], str) and row['reason'].strip(), 'Editorial reason required')
        group, fields = EXPECTED[ident]
        source = row['source']
        _require(isinstance(source, dict) and set(source) == {'path', 'sha256'}, 'Invalid raw source binding')
        _require(isinstance(source['path'], str) and re.fullmatch(
            r'code/validated-examples/[0-9]{4}-[0-9]{2}-[0-9]{2}(?:-[a-z0-9-]+)?/'+group+r'/cases[.]json', source['path'])
            and isinstance(source['sha256'], str) and re.fullmatch('[0-9a-f]{64}', source['sha256']), 'Wrong raw case source')
        file = _local(root, source['path'])
        _require(_sha(file) == source['sha256'], 'Raw scientific metadata SHA differs')
        document = json.loads(file.read_bytes())
        cases = document['cases'] if isinstance(document, dict) else document
        matches = [(i, case) for i, case in enumerate(cases) if case.get('id') == ident]
        _require(len(matches) == 1, 'Ambiguous raw editorial case')
        index, case = matches[0]
        _require(isinstance(row['fields'], dict) and set(row['fields']) == fields, 'Unreviewed display field')
        for field, replacement in row['fields'].items():
            _require(isinstance(replacement, dict) and set(replacement) == {'before', 'after'}
                     and all(isinstance(replacement[key], str) for key in ['before', 'after']), 'Only exact Japanese text overrides')
            before, after = replacement['before'], replacement['after']
            _require(isinstance(case.get(field), dict) and case[field].get('ja') == before, 'Editorial before-text differs')
            expected = before.replace('正の放射速度交差', '正の動径速度での交差') if ident == 'kepler-eccentricity' else before.replace('放射', '輻射')
            _require(before != after and after == expected, 'Unreviewed terminology edit')
        marker = {'kind': 'Japanese-display-terminology', 'schema_version': 1,
                  'raw_source': {**source, 'case_pointer': ('/cases/' if isinstance(document, dict) else '/')+str(index)},
                  'raw_case_canonical_sha256': sha256(_canonical(case)).hexdigest(),
                  'editorial_source_sha256': dependencies,
                  'fields': {field: {'raw_ja_sha256': sha256(value['before'].encode()).hexdigest(),
                                     'display_ja_sha256': sha256(value['after'].encode()).hexdigest()}
                             for field, value in row['fields'].items()}}
        plans[ident] = (case, row['fields'], marker)
    return plans


def project_case(root, case):
    """Return a copy; reject unproven after-text, unrelated edits and stale sources."""
    _require(isinstance(case, dict) and isinstance(case.get('id'), str), 'Case identity required')
    ident = case['id']
    if ident not in EXPECTED:
        _require('editorial_terminology' not in case, 'Unreviewed editorial provenance')
        return deepcopy(case)
    root = Path(root).resolve(strict=True)
    raw, fields, marker = _plan(root)[ident]
    expected = deepcopy(raw)
    for field, replacement in fields.items():
        expected[field]['ja'] = replacement['after']
    if 'editorial_terminology' in case:
        _require(_canonical(case['editorial_terminology']) == _canonical(marker), 'Unproven editorial idempotency')
        comparison = expected
    else:
        comparison = raw
    _require(all(key in case and _canonical(case[key]) == _canonical(value)
                 for key, value in comparison.items()), 'Editorial input changed outside its proven state')
    result = deepcopy(case)
    for field in fields:
        result[field]['ja'] = expected[field]['ja']
    result['editorial_terminology'] = deepcopy(marker)
    return result


def project_cases(root, cases):
    return [project_case(root, case) for case in cases]


def editorial_sources(case):
    """Additional presentation dependencies; existing raw source hashes stay intact."""
    return deepcopy(case.get('editorial_terminology', {}).get('editorial_source_sha256', {}))
