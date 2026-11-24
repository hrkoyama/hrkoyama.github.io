"""Run all fixed small models; independent qualification is a separate stage."""
import argparse
import json
from pathlib import Path
from io_utils import Deadline, fresh, sha, write_json
import experiments


def cache_ready(root):
    cache = root/'references/cache'
    q = json.loads((cache/'qualification.json').read_text())
    inputs = json.loads((root/'inputs.json').read_text())
    if q['passed'] is not True or set(q['checks']) != set(inputs['reference_check_ids']) or not all(q['checks'].values()):
        raise ValueError('Exact complete component/reference qualification required')
    if q['input_sha256'] != sha(root/'inputs.json') or q['acceptance_sha256'] != sha(root/'acceptance.json'):
        raise ValueError('Qualified cache inputs or acceptance changed')
    dependencies = {'pinn.py', 'fno.py', 'data_family.py', 'io_utils.py',
        'references/reference_models.py', 'references/oracles.py', 'references/qualify.py'}
    if set(q['source_sha256']) != dependencies:
        raise ValueError('Reference dependency inventory differs')
    for name, expected in q['source_sha256'].items():
        if sha(root/name) != expected:
            raise ValueError('Qualified reference dependency changed: '+name)
    provenance = json.loads((cache/'cache-manifest.json').read_text())
    expected = {'qualification.json', 'heat-data.npz', 'heat-problems.json',
        'enzyme-01-qualified.npz', 'enzyme-002-qualified.npz', 'lv-qualified.npz',
        'seir-1e-4-qualified.npz', 'seir-5e-5-qualified.npz',
        'mm-200-qualified.npz', 'mm-400-qualified.npz'}
    if set(provenance['files_sha256']) != expected:
        raise ValueError('Complete qualified cache inventory required')
    for name, expected in provenance['files_sha256'].items():
        if sha(cache/name) != expected:
            raise ValueError('Qualified cache file changed: '+name)
    return cache


def main(input_file, output, seconds=120):
    root = Path(__file__).resolve().parent
    output = fresh(output); budget = Deadline(seconds)
    config = json.loads(Path(input_file).read_text())
    if sha(input_file) != sha(root/'inputs.json'):
        raise ValueError('Only the frozen complete input is supported')
    acceptance = json.loads((root/'acceptance.json').read_text())
    data = {'schema_version': 1, 'passed': False, 'termination': 'incomplete',
        'input_sha256': sha(input_file), 'checks': {}, 'cases': []}
    def checkpoint():
        write_json(output/'result.json', data)
    checkpoint()
    try:
        cache = cache_ready(root)
        for ident in config['case_ids']:
            case = experiments.newcase(ident); data['cases'].append(case); checkpoint()
            if ident == 'pinn-poisson':
                experiments.pinn_case(config['pinn'], acceptance, output, budget, case, checkpoint, sha(root/'acceptance.json'))
            elif ident == 'fno-periodic-heat':
                experiments.fno_case(config['fno'], acceptance, cache, output, budget, case, checkpoint, sha(root/'acceptance.json'))
            else:
                experiments.biology_case(ident, config, acceptance, cache, output, budget, case, checkpoint, sha(root/'acceptance.json'))
            data['checks'][ident] = case['passed']; checkpoint()
        data['termination'] = 'completed_fixed_protocol'
        data['passed'] = all(data['checks'].values())
        checkpoint()
        return data
    except BaseException as error:
        data['exception'] = {'type': type(error).__name__, 'message': str(error)}
        checkpoint()
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True); parser.add_argument('--max-seconds', type=float, default=120)
    args = parser.parse_args(); result = main(args.input, args.output, args.max_seconds)
    raise SystemExit(0 if result['passed'] else 1)

