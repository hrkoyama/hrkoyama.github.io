#!/usr/bin/env python3
"""Run all fixed biological, stochastic and thermostat cases without network access."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import time
from models import RUNNERS


def run(input_path, output_path, selected=None):
    payload = Path(input_path).read_bytes()
    def reject_constant(value):
        raise ValueError('Nonfinite JSON number: '+value)
    config = json.loads(payload, parse_constant=reject_constant)
    if config.get('schema_version') != 1 or set(config['cases']) != set(RUNNERS):
        raise ValueError('Expected complete schema-1 fixed-case inputs')
    output = Path(output_path)
    if output.exists() and any(output.iterdir()):
        raise ValueError('Use a new or empty output directory')
    if selected and selected not in RUNNERS:
        raise ValueError('Unknown case')
    output.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    cases = []
    for name, runner in RUNNERS.items():
        if selected and name != selected:
            continue
        start = time.perf_counter()
        case = runner(config['cases'][name])
        case['duration_seconds'] = time.perf_counter()-start
        case['input_sha256'] = hashlib.sha256(json.dumps(config['cases'][name], sort_keys=True).encode()).hexdigest()
        cases.append(case)
        rows = case['records']
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with (output/(name+'.csv')).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for row in rows:
                writer.writerow({k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in row.items()})
    checks = {c['id']: c['passed'] for c in cases}
    result = {'schema_version': 1, 'passed': all(checks.values()), 'checks': checks, 'cases': cases,
              'termination': 'fixed_budget_completed', 'input_sha256': hashlib.sha256(payload).hexdigest(),
              'duration_seconds': time.perf_counter()-started,
              'environment': {'python': platform.python_version(), 'platform': platform.platform(),
                              **{name: importlib.metadata.version(name) for name in ['numpy', 'scipy']}}}
    (output/'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': result['passed'], 'cases': len(cases), 'checks': checks,
                      'duration_seconds': result['duration_seconds']}))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--case', choices=list(RUNNERS))
    args = parser.parse_args()
    try:
        result = run(args.input, args.output, args.case)
    except (OSError, ValueError, ArithmeticError, RuntimeError, KeyError, TypeError) as error:
        print(type(error).__name__+': '+str(error), file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(0 if result['passed'] else 1)
