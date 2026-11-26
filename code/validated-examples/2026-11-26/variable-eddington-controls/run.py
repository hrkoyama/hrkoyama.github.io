"""Run the fixed VEF/VET protocol only after a reviewed relative-file freeze."""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import importlib.metadata
import json
import math
import os
import platform
from pathlib import Path
import re
import sys
import time


IDS = ('vef-fourier-scattering1d', 'vet-fourier-source2d')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_freeze(root):
    freeze = json.loads((root/'freeze.json').read_text())
    if freeze.get('schema_version') != 1 or not isinstance(freeze.get('files'), dict):
        raise ValueError('A reviewed source freeze is required')
    files = freeze['files']
    required = {'primary.py', 'run.py', 'analytic_reference.py', 'test_cases.py', 'inputs.json', 'acceptance.json', 'PROTOCOL.md'}
    if not required <= set(files):
        raise ValueError('Incomplete explicit source freeze')
    for name, expected in files.items():
        relative = Path(name)
        if (relative.is_absolute() or '..' in relative.parts or not relative.parts
                or relative.parts[0] in ('results', 'execution-attempts') or name == 'freeze.json'
                or not re.fullmatch(r'[0-9a-f]{64}', expected)):
            raise ValueError('Unsafe/recursive source-freeze entry')
        path = root/relative
        if path.is_symlink() or not path.is_file() or root not in path.resolve().parents or digest(path) != expected:
            raise ValueError('Reviewed source bytes differ: '+name)
    return digest(root/'freeze.json')


class Deadline:
    def __init__(self, seconds):
        self.started = time.monotonic()
        self.seconds = seconds
        self.state = {'phase': 'initialized'}

    def __call__(self, state):
        self.state = dict(state)
        self.state['elapsed_seconds'] = time.monotonic()-self.started
        if self.state['elapsed_seconds'] > self.seconds:
            raise TimeoutError('Fixed cooperative runner budget exhausted')


def rms(value):
    import numpy as np
    return float(np.sqrt(np.mean(np.abs(value)**2)))


def reference_at(case, coordinates, settings):
    # The primary module never imports this oracle. Only validation calls it.
    from analytic_reference import reference_fields
    return reference_fields(case, coordinates, st=settings['st'], ss=settings['ss'])


def arrays_for_row(case, row, solution, settings, state=None):
    import numpy as np
    from primary import coordinates
    points = coordinates(tuple(row['shape']))
    if state is not None:state.update(phase='independent-reference', reference_points=points)
    reference = reference_at(case, points, settings)
    if state is not None:state['reference_candidate']=reference
    arrays = {'x': points[0], 'q': solution['q'], 'E_LO': solution['E_LO'], 'E_HO': solution['E'],
              'H_HO': solution['H'], 'K_HO': solution['K'], 'D': solution['D'], 'I': solution['I'],
              'omega': solution['omega'], 'weights': solution['weights'], 'H_LO_center': solution['H_LO_center'],
              'E_reference': reference['E'], 'H_reference': reference['H'],
              'K_reference': reference['K'], 'D_reference': reference['D']}
    if case['dimension'] == 2:
        arrays['y'] = points[1]
    for axis, face in enumerate(solution['faces']):
        shifted = list(points)
        shifted[axis] = shifted[axis]+0.5/row['shape'][axis]
        face_reference = reference_at(case, tuple(shifted), settings)['H'][..., axis]
        arrays[('Fx_face', 'Fy_face')[axis]] = face
        arrays[('Hx_reference_face', 'Hy_reference_face')[axis]] = face_reference
    if state is not None:state.update(phase='saved-array-assessment', arrays_candidate=arrays)
    if not all(np.all(np.isfinite(value)) for value in arrays.values()):
        raise ValueError('Nonfinite saved field or independent reference')
    return arrays


def row_metrics(case, row, solution, arrays):
    import numpy as np
    E, reference = arrays['E_LO'], arrays['E_reference']
    face_keys = ['Fx_face']+(['Fy_face'] if case['dimension'] == 2 else [])
    reference_keys = ['Hx_reference_face']+(['Hy_reference_face'] if case['dimension'] == 2 else [])
    error = np.concatenate([(arrays[k]-arrays[r]).ravel() for k, r in zip(face_keys, reference_keys)])
    signal = np.concatenate([arrays[k].ravel() for k in reference_keys])
    H_absolute, H_signal = rms(error), rms(signal)
    points = (arrays['x'],) if case['dimension'] == 1 else (arrays['x'], arrays['y'])
    modes = []
    for mode in case['source']['modes']:
        phase = sum(2*np.pi*k*x for k, x in zip(mode['wave_numbers'], points))
        kernel = np.exp(-1j*phase)
        actual = complex(2*np.mean(E*kernel))
        expected = complex(2*np.mean(reference*kernel))
        if abs(expected) == 0:
            raise ValueError('A prescribed nonzero source mode has zero analytic response')
        modes.append({'wave_numbers': mode['wave_numbers'],
                      'computed_real': actual.real, 'computed_imag': actual.imag,
                      'reference_real': expected.real, 'reference_imag': expected.imag,
                      'complex_relative_error': abs(actual-expected)/abs(expected),
                      'magnitude_relative_error': abs(abs(actual)-abs(expected))/abs(expected),
                      'phase_error_radians': abs(float(np.angle(actual/expected)))})
    D = arrays['D']
    from analytic_reference import m1_tensor
    M1_reference = m1_tensor(arrays['E_reference'], arrays['H_reference'])
    latest = solution['history'][-1]
    result = {**latest, 'E_relative_rms_error': rms(E-reference)/rms(reference),
              'E_absolute_max_error': float(np.max(np.abs(E-reference))),
              'face_H_relative_rms_error': H_absolute/H_signal if H_signal > 0 else None,
              'face_H_absolute_rms_error': H_absolute,
              'face_H_absolute_max_error': float(np.max(np.abs(error))),
              'D_component_max_abs_error': float(np.max(np.abs(D-arrays['D_reference']))),
              'M1_closure_reference_max_abs_difference': float(np.max(np.abs(M1_reference-arrays['D_reference']))),
              'tensor_symmetry_error': float(np.max(np.abs(D-np.swapaxes(D, -1, -2)))),
              'LO_flux_realizability_excess': float(np.max(np.sqrt(np.sum(arrays['H_LO_center']**2, axis=-1))-E)),
              'HO_flux_realizability_excess': float(np.max(np.sqrt(np.sum(arrays['H_HO']**2, axis=-1))-arrays['E_HO'])),
              'VET_z_parity': max(float(np.max(np.abs(arrays['H_HO'][..., 2]))),
                                  float(np.max(np.abs(D[..., 0, 2]))), float(np.max(np.abs(D[..., 1, 2])))),
              'nonconstant_f_span': float(np.max(D[..., 0, 0])-np.min(D[..., 0, 0])),
              'max_abs_Dxy': float(np.max(np.abs(D[..., 0, 1]))),
              'source_modes': modes,
              'maximum_source_mode_complex_relative_error': max((m['complex_relative_error'] for m in modes), default=None),
              'work': solution['work']}
    return result


def numerical_checks(metrics, required):
    return {'outer_E_converged': metrics['LOE_relative_update'] <= required['outer_LOE_relative_update_max'],
            'outer_D_converged': metrics['D_max_update'] <= required['outer_D_absolute_update_max'],
            'true_LO_residual': metrics['true_LO_relative_residual'] <= required['LO_true_relative_inf_residual_max'],
            'formal_HO_residual': metrics['formal_transport_residual'] <= required['HO_formal_relative_residual_max'],
            'imaginary_roundoff': metrics['imaginary_residue'] <= required['imaginary_ifft_residue_max'],
            'global_balance': metrics['discrete_global_balance'] <= required['discrete_global_balance_max'],
            'positive_intensity': metrics['minimum_I'] > 0,
            'positive_LO_energy': metrics['minimum_LOE'] > 0,
            'LO_realizability': metrics['LO_flux_realizability_excess'] <= required['flux_realizability_absolute_slack'],
            'HO_realizability': metrics['HO_flux_realizability_excess'] <= required['flux_realizability_absolute_slack'],
            'tensor_symmetry': metrics['tensor_symmetry_error'] <= required['tensor_symmetry_trace1_max'],
            'tensor_trace': metrics['tensor_trace_error'] <= required['tensor_symmetry_trace1_max'],
            'tensor_PSD': metrics['tensor_min_eigenvalue'] >= required['tensor_min_eigenvalue_allowed'],
            'HO_covariance_PSD': metrics['HO_covariance_min_eigenvalue'] >= required['HO_D_minus_hh_min_eigenvalue_allowed'],
            'z_parity': metrics['VET_z_parity'] <= required['VET_z_parity_max']}


def ratio(numerator, denominator):
    return numerator/denominator if denominator > 0 else None


def case_decision(case, records, acceptance, saved_arrays):
    import numpy as np
    table = {r['role']: r for r in records}
    coarse, fine, probe, constant = [table[k] for k in ['coarse', 'fine', 'angle-probe', 'constant']]
    c, f, p = [r['metrics'] for r in [coarse, fine, probe]]
    allowed = acceptance['required_case_checks']
    a, b = saved_arrays['space-fine'], saved_arrays['angle-probe']
    metrics = {'finest_E_relative_rms_error': p['E_relative_rms_error'],
               'finest_face_H_relative_rms_error': p['face_H_relative_rms_error'],
               'finest_mode_complex_relative_error': p['maximum_source_mode_complex_relative_error'],
               'finest_D_component_max_abs_error': p['D_component_max_abs_error'],
               'E_error_refinement_ratio': ratio(f['E_relative_rms_error'], c['E_relative_rms_error']),
               'face_H_error_refinement_ratio': ratio(f['face_H_relative_rms_error'], c['face_H_relative_rms_error']),
               'HO_LO_gap_refinement_ratio': ratio(f['HOE_minus_LOE_rms'], c['HOE_minus_LOE_rms']),
               'angle_probe_E_relative_rms_difference': rms(a['E_LO']-b['E_LO'])/rms(b['E_LO']),
               'angle_probe_D_max_abs_difference': float(np.max(np.abs(a['D']-b['D']))),
               'finest_nonconstant_f_span': p['nonconstant_f_span'], 'finest_max_abs_Dxy': p['max_abs_Dxy'],
               'main_rows': 3, 'constant_control_rows': 1,
               'outer_iterations_by_row': {r['row_id']: r['metrics']['work']['outer_iterations'] for r in records}}
    checks = {'all_row_solver_checks': all(all(r['checks'].values()) for r in records),
              'finest_E_accuracy': metrics['finest_E_relative_rms_error'] <= allowed['finest_LOE_relative_RMS_error_max'],
              'finest_face_H_accuracy': metrics['finest_face_H_relative_rms_error'] is not None and metrics['finest_face_H_relative_rms_error'] <= allowed['finest_faceH_relative_RMS_error_max'],
              'complex_source_modes_include_phase': metrics['finest_mode_complex_relative_error'] is not None and metrics['finest_mode_complex_relative_error'] <= allowed['finest_complex_mode_relative_amplitude_error_max'],
              'tensor_reference_accuracy': metrics['finest_D_component_max_abs_error'] <= allowed['finest_tensor_component_absolute_error_max'],
              'E_refines': metrics['E_error_refinement_ratio'] is not None and metrics['E_error_refinement_ratio'] <= allowed['fine_to_coarse_E_error_ratio_max'],
              'face_H_refines': metrics['face_H_error_refinement_ratio'] is not None and metrics['face_H_error_refinement_ratio'] <= allowed['fine_to_coarse_faceH_error_ratio_max'],
              'HO_LO_gap_refines_not_zero': metrics['HO_LO_gap_refinement_ratio'] is not None and metrics['HO_LO_gap_refinement_ratio'] <= allowed['fine_to_coarse_HOLO_E_gap_ratio_max'],
              'angle_probe_E': metrics['angle_probe_E_relative_rms_difference'] <= allowed['angle_probe_LOE_relative_difference_max'],
              'angle_probe_D': metrics['angle_probe_D_max_abs_difference'] <= allowed['angle_probe_D_component_difference_max'],
              'variable_closure': (metrics['finest_nonconstant_f_span'] >= allowed['VEF_nonconstant_f_span_min'] if case['dimension'] == 1 else metrics['finest_max_abs_Dxy'] >= allowed['VET_max_abs_Dxy_min'])}
    return metrics, checks


def safe_json(value):
    if isinstance(value, dict):
        return {str(k): safe_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [safe_json(v) for v in value]
    if hasattr(value, 'item'):
        return safe_json(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, complex):
        return {'real': safe_json(value.real), 'imag': safe_json(value.imag)}
    return value


def write_json(path, value):
    path.write_text(json.dumps(safe_json(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def save_failure_arrays(output, state):
    import numpy as np
    arrays = {}
    def collect(value, name):
        if isinstance(value, np.ndarray):
            arrays[name] = value
        elif isinstance(value, dict):
            for key, child in value.items():
                if key != 'history':
                    collect(child, name+'__'+str(key))
        elif isinstance(value, (list, tuple)):
            for i, child in enumerate(value):
                collect(child, name+'__'+str(i))
    collect(state, 'active')
    path = output/'failure-state.npz'
    np.savez(path, **arrays)
    return {'file': path.name, 'sha256': digest(path), 'arrays': {k: {'shape': list(v.shape), 'dtype': str(v.dtype), 'nonfinite_count': int(np.count_nonzero(~np.isfinite(v)))} for k, v in arrays.items()}}


def execute(input_path, output):
    root = Path(__file__).resolve().parent
    freeze_sha = check_freeze(root)
    for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:
        if os.environ.get(key) != '1':raise ValueError(key+'=1 required before scientific imports')
    import numpy as np
    from primary import solve
    document = json.loads(input_path.read_text())
    acceptance = json.loads((root/'acceptance.json').read_text())
    if tuple(c['id'] for c in document['cases']) != IDS or document['expected_primary_rows'] != 6 or document['expected_constant_rows'] != 2:
        raise ValueError('Fixed case/row inventory differs')
    if output.exists():
        raise ValueError('Output must be a new directory; retain previous attempts')
    if input_path.resolve() != (root/'inputs.json').resolve():
        raise ValueError('Execute only the reviewed local input file')
    output.mkdir(parents=True)
    settings = document['settings']
    deadline = Deadline(document['budget']['runner_cooperative_seconds'])
    result = {'schema_version': 1, 'input_sha256': digest(input_path), 'acceptance_sha256': digest(root/'acceptance.json'),
              'freeze_sha256': freeze_sha, 'group': document['group'], 'cases': [], 'checks': {i: False for i in IDS},
              'passed': False, 'termination': 'not-completed',
              'environment': {'python': platform.python_version(), 'platform': platform.platform(),
                              'dependencies': {k: importlib.metadata.version(k) for k in ['numpy', 'scipy', 'pytest']}}}
    csv_rows = []
    try:
        with np.errstate(all='raise'):
            for case in document['cases']:
                case_result = {'id': case['id'], 'passed': False, 'checks': {}, 'metrics': {}, 'records': []}
                result['cases'].append(case_result)
                component = next(c for c in document['constant_controls'] if c['case_id'] == case['id'])
                scheduled = [(row, case, role) for row, role in zip(case['rows'], ['coarse', 'fine', 'angle-probe'])]
                constant_case = copy.deepcopy(case)
                constant_case['source'] = component['source']
                scheduled.append((component['row'], constant_case, 'constant'))
                saved_arrays = {}
                for row, actual_case, role in scheduled:
                    deadline({'case_id': case['id'], 'row_id': row['id'], 'phase': 'before-row'})
                    solution = solve(actual_case, row, settings, deadline)
                    arrays = arrays_for_row(actual_case, row, solution, settings, deadline.state)
                    metrics = row_metrics(actual_case, row, solution, arrays)
                    name = case['id']+'--'+row['id']+'.npz'
                    destination = output/name
                    if destination.exists():
                        raise ValueError('Refuse to overwrite row arrays')
                    np.savez_compressed(destination, **arrays)
                    checks = numerical_checks(metrics, acceptance['required_solver_checks'])
                    if role == 'constant':
                        control = acceptance['constant_control_absolute_checks']
                        checks.update(constant_I=bool(np.max(np.abs(arrays['I']-1)) <= control['I_E_max_error']),
                                      constant_E=metrics['E_absolute_max_error'] <= control['I_E_max_error'],
                                      constant_H=metrics['face_H_absolute_max_error'] <= control['H_face_max_error'],
                                      constant_D=metrics['D_component_max_abs_error'] <= control['D_max_error'])
                    record = {'row_id': row['id'], 'role': role, 'input': row, 'source': actual_case['source'],
                              'arrays': name, 'arrays_sha256': digest(destination), 'metrics': metrics,
                              'checks': checks, 'passed': all(checks.values()), 'history': solution['history']}
                    case_result['records'].append(record)
                    saved_arrays[row['id']] = arrays
                    csv_rows.append([case['id'], row['id'], role, metrics['E_relative_rms_error'],
                                     metrics['face_H_relative_rms_error'] if metrics['face_H_relative_rms_error'] is not None else 'not-applicable',
                                     metrics['D_component_max_abs_error'], metrics['true_LO_relative_residual'], metrics['HOE_minus_LOE_rms'], record['passed']])
                    deadline({**deadline.state, 'phase': 'saved-row', 'saved_row': name})
                metrics, checks = case_decision(case, case_result['records'], acceptance, saved_arrays)
                case_result.update(metrics=metrics, checks=checks, passed=all(checks.values()))
                result['checks'][case['id']] = case_result['passed']
            if check_freeze(root) != freeze_sha:raise ValueError('Source freeze changed during the fixed run')
            deadline({**deadline.state,'phase':'final-source-check'})
            result.update(passed=all(result['checks'].values()), termination='fixed-protocol-complete')
    except Exception as error:
        state = getattr(error, 'state', deadline.state)
        # Preserve original arrays, including failed/nonfinite candidates, BEFORE JSON.
        failure = save_failure_arrays(output, state)
        result.update(passed=False, termination='failed-state-preserved', failure={'type': type(error).__name__, 'message': str(error),
                      'case_id': state.get('case_id'), 'row_id': state.get('row_id'), 'phase': state.get('phase'),
                      'arrays': failure, 'history': state.get('history', []), 'last_valid_angular_directions': state.get('I_valid_directions')})
    result['elapsed_seconds'] = time.monotonic()-deadline.started
    result['completed_records'] = sum(len(c['records']) for c in result['cases'])
    with (output/'measurements.csv').open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['case_id', 'row_id', 'role', 'E_relative_rms_error', 'face_H_relative_rms_error', 'D_component_max_abs_error', 'true_LO_relative_residual', 'HO_LO_gap_rms', 'row_passed'])
        writer.writerows(csv_rows)
    write_json(output/'result.json', result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('inputs.json'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    # Validate the source freeze before importing scientific modules in execute().
    check_freeze(Path(__file__).resolve().parent)
    result = execute(args.input.resolve(), args.output.resolve())
    print(json.dumps({'passed': result['passed'], 'termination': result['termination'], 'completed_records': result['completed_records']}))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
