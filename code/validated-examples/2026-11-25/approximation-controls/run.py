#!/usr/bin/env python3
"""Run one complete fixed approximation protocol into a fresh directory."""
import argparse
import json
from pathlib import Path
import sys
import time
import numpy as np
from experiments import Study, interpolation_study, spline_study, haar_study
from io_contract import write_json, write_csv, source_hashes, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    before = source_hashes(root)
    contract = json.loads((root/'pre-run-contract.json').read_text())
    if sha(args.input) != contract['input_sha256']:
        raise ValueError('Input differs from frozen protocol')
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Output directory must be fresh or empty')
    args.output.mkdir(parents=True, exist_ok=True)
    inputs = json.loads(args.input.read_text())
    limits = json.loads((root/'acceptance.json').read_text())
    result = {'schema_version': 1, 'group': 'approximation-controls', 'passed': False,
              'termination': 'incomplete', 'input_sha256': sha(args.input),
              'acceptance_sha256': sha(root/'acceptance.json'), 'source_sha256': before,
              'checks': {}, 'cases': []}
    started, failed = time.monotonic(), False
    routines = [('runge-barycentric-clenshaw', interpolation_study),
                ('spline-shape-controls', spline_study),
                ('haar-mallat-boundary-threshold', haar_study)]
    for ident, routine in routines:
        study = Study(ident, args.output)
        result['cases'].append(study.result)
        try:
            routine(inputs['cases'][ident], limits[ident], study)
        except Exception as error:
            # The active arrays belong to this Study, not to caller-owned inputs.
            if study.active:
                np.savez_compressed(args.output/(ident+'-failed-candidate.npz'), **study.active)
            study.result['error'] = {'type': type(error).__name__, 'message': str(error)}
            failed = True
        finally:
            if study.result['records']:
                write_csv(args.output/(ident+'-records.csv'), study.result['records'])
            write_json(args.output/(ident+'-checkpoint.json'), study.result)
            write_json(args.output/'result.json', result)
        if failed:
            break
    after = source_hashes(root)
    result['source_post_sha256'] = after
    result['wall_seconds'] = time.monotonic()-started
    result['termination'] = 'failed_exception' if failed else 'completed_fixed_protocol'
    result['checks'] = {case['id']: bool(case['passed']) for case in result['cases']}
    result['check_inventory_matches'] = all(
        set(case['checks']) == set(contract['expected_case_check_ids'][case['id']])
        for case in result['cases'])
    result['passed'] = (not failed and before == after and len(result['cases']) == len(routines)
                        and result['check_inventory_matches'] and all(result['checks'].values()))
    write_json(args.output/'result.json', result)
    print(json.dumps({'passed': result['passed'], 'termination': result['termination'],
                      'records': sum(len(c['records']) for c in result['cases']),
                      'checks': sum(len(c['checks']) for c in result['cases'])}))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
