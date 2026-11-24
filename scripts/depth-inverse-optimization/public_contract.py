"""Exact selected public verifier functions; no scientific acceptance relaxation.
Original: scripts/verify-depth-public.py, SHA256 67252a082cb929e6c903826a4a5ef2649fd20890afdca5a21e98d7e4995b5915.
"""

import csv
import hashlib
import math
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def check_finite(value):
    if isinstance(value, float):
        require(math.isfinite(value), 'Nonfinite numeric value')
    elif isinstance(value, dict):
        for child in value.values():
            check_finite(child)
    elif isinstance(value, list):
        for child in value:
            check_finite(child)

def validate_result(result, expected_ids, input_sha256, termination):
    check_finite(result)
    require(isinstance(result, dict) and type(result.get('schema_version')) is int and
            result['schema_version'] == 1, 'Unsupported result schema')
    require(result.get('passed') is True, 'Scientific result did not pass')
    require(result.get('input_sha256') == input_sha256, 'Executed input SHA-256 mismatch')
    require(isinstance(termination, str) and termination and result.get('termination') == termination,
            'Missing or changed completion reason')
    checks = result.get('checks')
    require(isinstance(checks, dict) and set(checks) == set(expected_ids) and all(v is True for v in checks.values()),
            'Top-level case decisions are incomplete or failed')
    cases = result.get('cases')
    require(isinstance(cases, list) and len(cases) == len(expected_ids) and
            {c.get('id') for c in cases} == set(expected_ids), 'Executed case IDs differ from registry')
    for case in cases:
        require(case.get('passed') is True and isinstance(case.get('checks'), dict) and case['checks'] and
                all(v is True for v in case['checks'].values()), 'Case numerical checks did not pass')
        require(isinstance(case.get('metrics'), dict) and case['metrics'], 'Missing case metrics')
        require(isinstance(case.get('records'), (list, dict)) and case['records'], 'Missing refinement records')
    return cases

def check_generated_csv(directory):
    files = sorted(Path(directory).glob('*.csv'))
    require(files, 'No generated CSV outputs')
    records = []
    for path in files:
        with path.open(newline='') as handle:
            rows = list(csv.reader(handle))
        require(len(rows) >= 2 and rows[0] and len(rows[0]) == len(set(rows[0])), 'Empty or ambiguous generated CSV')
        for row in rows[1:]:
            require(len(row) == len(rows[0]), 'Ragged generated CSV')
            for value in row:
                try:
                    number = float(value)
                except ValueError:
                    continue
                require(math.isfinite(number), 'Nonfinite generated CSV value')
        records.append({'file': path.name, 'bytes': path.stat().st_size, 'sha256': digest(path.read_bytes())})
    return records
