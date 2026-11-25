"""Join immutable historical references with explicitly reviewed new cards.

This module reads metadata only. It evaluates no reference or numerical solver.
"""
import json
import copy
import hashlib
from pathlib import Path
import re

BASE_SOURCE = 'numerical-methods-atlas/assets/reference-solutions.json'
SUPPLEMENT_SOURCE = 'catalog/atlas-reference-supplements.json'
ANNOTATION_SOURCE = 'catalog/atlas-reference-metadata.json'


def load_reference_cases(root, read=None):
    root = Path(root)
    if read is None:
        read = lambda path: json.loads((root/path).read_text())
    historical = read(BASE_SOURCE)['cases']
    additional = read(SUPPLEMENT_SOURCE)['cases'] if (root/SUPPLEMENT_SOURCE).is_file() else []
    cases = [dict(case) for case in [*historical, *additional]]
    identifiers = [case['id'] for case in cases]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Reference supplements must not replace historical case identities')
    for case in additional:
        if not re.fullmatch(r'[a-z][a-z0-9-]+', case['id']):
            raise ValueError('Unsafe supplementary reference identity')
        for key in ['title', 'assumptions', 'formula']:
            if not isinstance(case.get(key), str) or not case[key].strip():
                raise ValueError('Missing reference metadata: '+key)
        if case.get('kind') not in {'analytic', 'semi-analytic', 'manufactured', 'numerical-reference'}:
            raise ValueError('Unknown supplementary reference kind')
        if not case.get('citations') or not all(row.get('role') and row.get('title') and row.get('url') for row in case['citations']):
            raise ValueError('Supplementary references need explicit citation roles')
        for kind in ['view', 'reading']:
            if set(case.get(kind, {})) != {'ja', 'en'} or not all(case[kind].values()):
                raise ValueError('Missing localized supplementary reference route')
    if (root/ANNOTATION_SOURCE).is_file():
        annotation = read(ANNOTATION_SOURCE)
        expected_base = annotation.get('base_source', {})
        if (annotation.get('schema_version') != 1 or expected_base.get('path') != '/'+BASE_SOURCE or
                expected_base.get('sha256') != hashlib.sha256((root/BASE_SOURCE).read_bytes()).hexdigest()):
            raise ValueError('Reference annotation source binding differs')
        by_id = {case['id']:case for case in cases}
        source_ids = {BASE_SOURCE:{case['id'] for case in historical}, SUPPLEMENT_SOURCE:{case['id'] for case in additional}}
        seen = set()
        allowed = {'citations', 'reference_scope', 'reference_class', 'reference_contract'}
        vocabulary = {'continuous-exact', 'semi-analytic', 'manufactured', 'discrete-exact', 'independent-numerical', 'self-convergence'}
        for row in annotation.get('cases', []):
            ident, source, metadata = row.get('id'), row.get('source'), row.get('metadata', {})
            if ident in seen or ident not in source_ids.get(source, set()) or not metadata or set(metadata)-allowed:
                raise ValueError('Unsafe or duplicate reference annotation')
            original = by_id[ident]
            checksum = hashlib.sha256(json.dumps(original, sort_keys=True, ensure_ascii=False, separators=(',',':')).encode()).hexdigest()
            if checksum != row.get('source_case_sha256'):
                raise ValueError('Historical reference annotation binding differs: '+ident)
            if metadata.get('reference_class') not in vocabulary or metadata.get('reference_contract', {}).get('class') != metadata['reference_class']:
                raise ValueError('Unknown or mismatched refined reference class')
            if 'citations' in metadata and (not metadata['citations'] or not all(c.get('role') and c.get('title') and c.get('url') and c.get('note') for c in metadata['citations'])):
                raise ValueError('Annotated citations require explicit roles and read limits')
            original.update(copy.deepcopy(metadata));seen.add(ident)
        unclassified = annotation.get('unclassified_ids', [])
        if len(unclassified) != len(set(unclassified)) or not set(unclassified) <= set(by_id) or set(unclassified)&seen:
            raise ValueError('Invalid unclassified reference coverage')
    return cases
