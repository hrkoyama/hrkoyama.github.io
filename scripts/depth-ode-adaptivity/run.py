"""Frozen single-input main; fresh output, checkpointed failure, no oracle regeneration."""
import argparse
import json
from pathlib import Path
import sys
import traceback
import experiments
from io_contract import digest, save_json
from reference_eval import Cache


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    if args.output.exists() or args.output.is_symlink():raise FileExistsError('Fresh output directory required; retain failed attempts')
    raw = args.input.read_bytes()
    if raw != (source/'inputs.json').read_bytes():raise ValueError('Only exact frozen input bytes are accepted')
    contract = json.loads((source/'pre-run-contract.json').read_text())
    hashes = {name: digest(source/name) for name in contract['files_sha256']}
    if hashes != contract['files_sha256']:raise ValueError('Frozen source/reference binding mismatch')
    inputs = json.loads(raw)
    limits = json.loads((source/'acceptance.json').read_text())
    if len(inputs['runs']) != 60 or len({r['id'] for r in inputs['runs']}) != 60:raise ValueError('Exact60 unique frozen run rows required')
    args.output.mkdir(parents=True)
    result = {'schema_version': 1, 'passed': False, 'termination': 'incomplete',
              'input_sha256': digest(args.input), 'source_sha256': hashes,
              'checks': {case: False for case in experiments.CASE_IDS}, 'cases': []}
    def original_summary():
        values = [v for c in result['cases'] for v in c['original_target_results'].values()]
        result['original_target_summary'] = {'met': sum(v is True for v in values), 'total': len(values),
            'all_met': bool(values) and all(values), 'acceptance_sha256': digest(source/'acceptance.json')}
    original_summary()
    save_json(args.output/'result.json', result)
    try:
        cache = Cache(source)
        for ident in experiments.CASE_IDS:
            case = experiments.new_case(ident, digest(source/'acceptance.json'))
            result['cases'].append(case)  # mutable entered case survives later diagnostic failure
            save_json(args.output/'result.json', result)
            rows = [r for r in inputs['runs'] if r['case_id'] == ident]
            if ident in experiments.CASE_IDS[:2]:
                experiments.run_stiff(case, rows, inputs, limits, cache, args.output)
            elif ident == 'rk45-dense-events':
                experiments.run_rk45(case, rows, inputs, limits, args.output)
            else:
                experiments.run_boundary(case, rows, inputs, limits, cache, args.output)
            result['checks'][ident] = case['passed']
            original_summary()
            save_json(args.output/'result.json', result)
        result['passed'] = all(result['checks'].values())
        result['termination'] = 'completed_fixed_protocol'
        result['failure'] = None
    except BaseException as exc:
        result['failure'] = {'type': type(exc).__name__, 'message': str(exc), 'traceback': traceback.format_exc()}
        if result['cases']:
            result['cases'][-1]['passed'] = False
            result['cases'][-1]['failure'] = dict(result['failure'])
        # Per-run/checkpoint files contain each completed row/check; keep top-level entered cases too.
    original_summary()
    save_json(args.output/'result.json', result)
    return 0 if result['passed'] else 1


if __name__ == '__main__':sys.exit(main())
