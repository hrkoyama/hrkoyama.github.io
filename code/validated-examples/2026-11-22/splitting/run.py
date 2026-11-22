#!/usr/bin/env python3
"""Run the bounded matched reaction-diffusion comparison, without a network."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import time
from splitting import Budget, CASE_ID, run_case, validate


def run(input_path, output_path):
    payload = Path(input_path).read_bytes()
    def reject(value):
        raise ValueError('Nonfinite JSON: ' + value)
    config = json.loads(payload, parse_constant=reject)
    if config.get('schema_version') != 1 or set(config['cases']) != {CASE_ID}:
        raise ValueError('Expected the complete fixed-case schema-1 input')
    case_config = config['cases'][CASE_ID]
    validate(case_config)
    budget = Budget(config['maximum_total_seconds'])
    output = Path(output_path)
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError('Use a new or empty output directory')
    output.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    case = run_case(case_config, budget)
    case['input_sha256'] = hashlib.sha256(json.dumps(case_config, sort_keys=True).encode()).hexdigest()
    for filename, rows in [(CASE_ID+'.csv', case['records']), ('time-errors.csv', case['time_records'])]:
        fields = list(dict.fromkeys(key for row in rows for key in row))
        with (output/filename).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader(); writer.writerows(rows)
    result = {'schema_version': 1, 'passed': case['passed'], 'checks': {CASE_ID: case['passed']},
              'cases': [case], 'termination': 'fixed_budget_completed',
              'input_sha256': hashlib.sha256(payload).hexdigest(),
              'duration_seconds': time.perf_counter()-started,
              'environment': {'python': platform.python_version(), 'platform': platform.platform(),
                              **{name: importlib.metadata.version(name) for name in ['numpy', 'scipy']}}}
    (output/'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': result['passed'], 'checks': case['checks'], 'duration_seconds': result['duration_seconds']}))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        result = run(args.input, args.output)
    except (OSError, ValueError, ArithmeticError, RuntimeError, KeyError, TypeError) as error:
        print(type(error).__name__+': '+str(error), file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(0 if result['passed'] else 1)
