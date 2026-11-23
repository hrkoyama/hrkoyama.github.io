"""Join immutable historical references with explicitly reviewed new cards.

This module reads metadata only. It evaluates no reference or numerical solver.
"""
import json
from pathlib import Path
import re

BASE_SOURCE = 'numerical-methods-atlas/assets/reference-solutions.json'
SUPPLEMENT_SOURCE = 'catalog/atlas-reference-supplements.json'


def load_reference_cases(root, read=None):
    root = Path(root)
    if read is None:
        read = lambda path: json.loads((root/path).read_text())
    historical = read(BASE_SOURCE)['cases']
    additional = read(SUPPLEMENT_SOURCE)['cases'] if (root/SUPPLEMENT_SOURCE).is_file() else []
    cases = [*historical, *additional]
    identifiers = [case['id'] for case in cases]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Reference supplements must not replace historical case identities')
    for case in additional:
        if not re.fullmatch(r'[a-z][a-z0-9-]+', case['id']):
            raise ValueError('Unsafe supplementary reference identity')
        for key in ['title', 'assumptions', 'formula']:
            if not isinstance(case.get(key), str) or not case[key].strip():
                raise ValueError('Missing reference metadata: '+key)
        if case.get('kind') not in {'analytic', 'semi-analytic', 'manufactured'}:
            raise ValueError('Unknown supplementary reference kind')
        if not case.get('citations') or not all(row.get('role') and row.get('title') and row.get('url') for row in case['citations']):
            raise ValueError('Supplementary references need explicit citation roles')
        for kind in ['view', 'reading']:
            if set(case.get(kind, {})) != {'ja', 'en'} or not all(case[kind].values()):
                raise ValueError('Missing localized supplementary reference route')
    return cases
