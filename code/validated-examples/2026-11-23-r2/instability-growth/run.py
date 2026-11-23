#!/usr/bin/env python3
"""Fixed, independently referenced nonlinear KH/RT initial-growth experiments."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flow import solve, velocity, streamfunction, StageFailure
from references.linear import trajectory, fields, modal_amplitude
ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def rms(q):
    return float(np.sqrt(np.mean(q*q)))


def relative_fields(case, a, b):
    value = float(np.sqrt(np.mean((a['u']-b['u'])**2+(a['v']-b['v'])**2))
                  /max(1e-30, np.sqrt(np.mean(b['u']**2+b['v']**2))))
    if case == 'rt-initial-growth':
        value = max(value, rms(a['theta']-b['theta'])/max(1e-30, rms(b['theta'])))
    return value


def qualify(case, controls, limits):
    times = np.linspace(0., controls['final_time'][case], controls['snapshots'])
    series = [trajectory(case, k, controls, controls['epsilon'], times)
              for k in controls['reference_truncations']]
    measurements = []
    for index, (modes, states, eigenvalue) in enumerate(series):
        amplitudes = [modal_amplitude(case, modes, state) for state in states]
        item = {'truncation': int(controls['reference_truncations'][index]),
                'amplitudes': amplitudes, 'maximum_real_eigenvalue': eigenvalue}
        if index:
            low = fields(case, series[index-1][0], series[index-1][1][-1], 128)
            high = fields(case, modes, states[-1], 128)
            item['field_relative_increment'] = relative_fields(case, low, high)
            item['growth_relative_increment'] = abs(amplitudes[-1]/amplitudes[0]
                /(measurements[-1]['amplitudes'][-1]/measurements[-1]['amplitudes'][0])-1.)
        measurements.append(item)
    last = measurements[-1]
    checks = {
        'reference_state_sensitivity': bool(last['field_relative_increment'] <= limits['reference_state_sensitivity_max']),
        'reference_growth_sensitivity': bool(last['growth_relative_increment'] <= limits['reference_growth_sensitivity_max']),
        'reference_positive_eigen_growth': bool(last['maximum_real_eigenvalue'] >= limits['reference_eigen_growth_min']),
    }
    return series[-1], {'passed': all(checks.values()), 'checks': checks,
                        'records': measurements, 'times': times.tolist(),
                        'scope': 'Continuous linearized Fourier-Galerkin IVPs. Linearization and finite truncation errors are separately controlled; no nonlinear independent-engine or sharp-interface formula claim.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reference-only', action='store_true')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Output must be fresh to retain every prior attempt')
    args.output.mkdir(parents=True)
    controls = json.loads(args.input.read_text())
    contract = json.loads((ROOT/'pre-run-contract.json').read_text())
    for relative, expected in contract['files_sha256'].items():
        if sha(ROOT/relative) != expected:
            raise ValueError('Changed fixed scientific source: '+relative)
    if sha(args.input) != contract['files_sha256']['inputs.json']:
        raise ValueError('Input differs from the declared fixed experiment')
    limits = json.loads((ROOT/'acceptance.json').read_text())
    start = time.monotonic()
    references, qualifications = {}, {}
    try:
        for case in controls['case_ids']:
            references[case], qualifications[case] = qualify(case, controls, limits)
    except Exception as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        save(args.output/'result.json', {'schema_version': 1, 'group': 'instability-growth',
            'input_sha256': sha(args.input), 'passed': False, 'termination': 'reference_failure',
            'failure': failure, 'checks': {case: False for case in controls['case_ids']},
            'cases': [], 'partial_reference_qualifications': qualifications})
        raise
    save(args.output/'reference-qualification.json', qualifications)
    if args.reference_only:
        return 0 if all(q['passed'] for q in qualifications.values()) else 1
    results, failure = [], None
    try:
        if not all(q['passed'] for q in qualifications.values()):
            raise ValueError('Independent reference did not qualify; no nonlinear PDE was run')
        for case in controls['case_ids']:
            checks = dict(qualifications[case]['checks'])
            modes, reference_states, eigenvalue = references[case]
            rows, saved = [], {}
            settings = [(f'n{n}', n, controls['epsilon'], 1.) for n in controls['grid_sizes']]
            settings += [('time-half', controls['probe_grid'], controls['epsilon'], .5),
                         ('epsilon-half', controls['probe_grid'], controls['epsilon']/2, 1.)]
            for name, n, epsilon, cfl_factor in settings:
                data = solve(n, epsilon, case, controls, cfl_factor)
                computed = []
                for omega, theta in zip(data['omega'], data['theta']):
                    u, v = velocity(streamfunction(omega, data['h']), data['h'])
                    computed.append(dict(omega=omega, theta=theta, u=u, v=v))
                scaled_reference = reference_states*(epsilon/controls['epsilon'])
                exact = [fields(case, modes, state, n) for state in scaled_reference]
                amplitudes = [rms(q['theta']) if case == 'rt-initial-growth'
                              else float(np.sqrt(np.mean(q['u']**2+q['v']**2))) for q in computed]
                ref_amplitudes = [modal_amplitude(case, modes, state) for state in scaled_reference]
                filename = case+'-'+name+'.npz'
                arrays = {key: data[key] for key in ['omega', 'theta', 'times']}
                arrays.update({key: value for key, value in computed[-1].items() if key not in arrays})
                arrays.update({'reference_'+key: value for key, value in exact[-1].items()})
                arrays.update(amplitudes=np.array(amplitudes), reference_amplitudes=np.array(ref_amplitudes))
                np.savez_compressed(args.output/filename, **arrays)
                row = {'id': name, 'n': n, 'epsilon': epsilon, 'cfl_factor': cfl_factor,
                       'steps': data['steps'], 'relative_field_error': relative_fields(case, computed[-1], exact[-1]),
                       'amplitudes': amplitudes, 'reference_amplitudes': ref_amplitudes,
                       'file': filename, 'sha256': sha(args.output/filename),
                       **{key: data[key] for key in ['finite', 'max_divergence', 'max_poisson_residual', 'max_mean_omega', 'max_mean_theta']}}
                rows.append(row)
                saved[name] = computed[-1]
                checks[name+'_finite'] = bool(data['finite'])
                checks[name+'_divergence'] = bool(data['max_divergence'] <= limits['absolute_divergence_max'])
                checks[name+'_poisson'] = bool(data['max_poisson_residual'] <= limits['absolute_poisson_residual_max'])
                checks[name+'_mean_omega'] = bool(data['max_mean_omega'] <= limits['absolute_mean_drift_max'])
                checks[name+'_mean_theta'] = bool(data['max_mean_theta'] <= limits['absolute_mean_drift_max'])
                save(args.output/(case+'-completed-runs.json'), rows)
            primary = rows[:len(controls['grid_sizes'])]
            errors = [row['relative_field_error'] for row in primary]
            orders = [float(np.log(errors[i]/errors[i+1])/np.log(primary[i+1]['n']/primary[i]['n']))
                      for i in range(len(primary)-1)]
            checks['spatial_decrease_1'] = bool(errors[1] < errors[0])
            checks['spatial_decrease_2'] = bool(errors[2] < errors[1])
            checks['minimum_spatial_order'] = bool(min(orders) >= limits['minimum_spatial_order'])
            checks['finest_field_error'] = bool(errors[-1] <= limits['finest_relative_field_error_max'])
            finest = primary[-1]
            reference_curve = np.array(finest['reference_amplitudes'])
            measured_curve = np.array(finest['amplitudes'])
            curve_error = float(np.max(abs(measured_curve/measured_curve[0]-reference_curve/reference_curve[0])
                                       /(reference_curve/reference_curve[0])))
            rate = float(np.log(measured_curve[-1]/measured_curve[0])/controls['final_time'][case])
            rate_reference = float(np.log(reference_curve[-1]/reference_curve[0])/controls['final_time'][case])
            growth = float(measured_curve[-1]/measured_curve[0])
            checks['growth_curve'] = bool(curve_error <= limits['growth_curve_relative_error_max'])
            checks['finite_window_growth_rate'] = bool(abs(rate-rate_reference) <= limits['finite_window_rate_absolute_error_max'])
            checks['observable_growth'] = bool(growth >= limits['finite_window_growth_min'])
            normal = saved['n'+str(controls['probe_grid'])]
            time_difference = relative_fields(case, saved['time-half'], normal)
            coarse_error = next(row['relative_field_error'] for row in primary if row['n'] == controls['probe_grid'])
            time_fraction = time_difference/coarse_error
            doubled_half = {key: 2*value for key, value in saved['epsilon-half'].items()}
            linearity = relative_fields(case, doubled_half, normal)
            checks['time_contamination'] = bool(time_fraction <= limits['time_probe_fraction_of_spatial_error_max'])
            checks['amplitude_linearity'] = bool(linearity <= limits['amplitude_halving_scaled_difference_max'])
            item = {'id': case, 'passed': all(checks.values()), 'checks': checks,
                    'records': rows, 'metrics': {'spatial_orders': orders, 'finest_relative_field_error': errors[-1],
                    'finite_window_growth_rate': rate, 'reference_finite_window_growth_rate': rate_reference,
                    'finest_growth_factor': growth, 'maximum_growth_curve_error': curve_error,
                    'time_contamination_fraction': time_fraction, 'amplitude_scaled_difference': linearity,
                    'linear_operator_maximum_real_eigenvalue': eigenvalue}}
            results.append(item)
            columns = ['id', 'n', 'epsilon', 'cfl_factor', 'steps',
                       'relative_field_error', 'max_divergence',
                       'max_poisson_residual', 'max_mean_omega', 'max_mean_theta']
            with (args.output/(case+'.csv')).open('w', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=columns, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(rows)
    except Exception as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        if isinstance(error, StageFailure):
            np.savez_compressed(args.output/'failed-stage.npz', omega=error.omega, theta=error.theta)
    result = {'schema_version': 1, 'group': 'instability-growth',
              'input_sha256': sha(args.input), 'passed': failure is None and len(results) == len(controls['case_ids']) and all(c['passed'] for c in results),
              'termination': 'fixed_budget_completed' if failure is None else 'scientific_failure',
              'failure': failure, 'checks': {case: next((c['passed'] for c in results if c['id'] == case), False) for case in controls['case_ids']},
              'cases': results, 'duration_seconds': time.monotonic()-start,
              'created_at_utc': datetime.now(timezone.utc).isoformat()}
    save(args.output/'result.json', result)
    print(json.dumps({'passed': result['passed'], 'gates': sum(len(c['checks']) for c in results),
                      'failed': {c['id']: [k for k, v in c['checks'].items() if not v] for c in results},
                      'failure': failure, 'seconds': result['duration_seconds']}), flush=True)
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
