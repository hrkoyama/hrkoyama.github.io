#!/usr/bin/env python3
"""Execute both small, fixed educational cases from this self-contained ZIP."""
import argparse
import csv
import hashlib
import json
import platform
from pathlib import Path
import time
import numpy as np
from experiments import Budget, check_baselines, fr_case, sem_case, validate


def run(input_path, output_path):
    payload = Path(input_path).read_bytes()
    def reject(value):
        raise ValueError('Nonfinite JSON '+value)
    config = json.loads(payload, parse_constant=reject)
    validate(config); check_baselines()
    output = Path(output_path)
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError('Use a new or empty output directory')
    output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic(); budget = Budget(config['maximum_total_seconds']); cases = []
    for function, (ident, parameters) in zip([sem_case, fr_case], config['cases'].items()):
        budget.check(); result, fields = function(parameters, budget)
        result['input_sha256'] = hashlib.sha256(json.dumps(parameters, sort_keys=True).encode()).hexdigest()
        np.savez_compressed(output/(ident+'.npz'), **fields)
        columns = list(dict.fromkeys(k for row in result['records'] for k in row))
        with (output/(ident+'.csv')).open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=columns); writer.writeheader(); writer.writerows(result['records'])
        cases.append(result)
    answer = {'schema_version': 1, 'passed': all(c['passed'] for c in cases),
              'checks': {c['id']: c['passed'] for c in cases}, 'cases': cases,
              'input_sha256': hashlib.sha256(payload).hexdigest(), 'termination': 'fixed_budget_completed',
              'duration_seconds': time.monotonic()-started,
              'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'platform': platform.platform()}}
    (output/'result.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': answer['passed'], 'seconds': answer['duration_seconds'],
                      'cases': [{k: c[k] for k in ['id', 'metrics', 'checks']} for c in cases]}, indent=2))
    return answer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--input', required=True); parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        result = run(args.input, args.output)
    except (OSError, ValueError, ArithmeticError, RuntimeError, KeyError, TypeError) as error:
        print(type(error).__name__+': '+str(error)); raise SystemExit(2)
    raise SystemExit(0 if result['passed'] else 1)
