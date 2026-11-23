#!/usr/bin/env python3
"""Execute only the frozen strong double-rarefaction refinement family."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import euler_positivity as solver
from references import double_rarefaction as exact
from references.numart_reference_riemann import RiemannSolution

ROOT = Path(__file__).resolve().parent
CASE = 'euler-double-rarefaction-positivity'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def relative_l1(value, reference, dx):
    return float(dx*np.sum(abs(value-reference))/(dx*np.sum(abs(reference))))


def reference_checks():
    independent = RiemannSolution('euler', (1., -2., .4), (1., 2., .4), 1.4)
    center = exact.conserved(np.array([.5]), .15)[0]
    star_pressure_difference = abs(float(solver.pressure(center))-independent.star)
    points = np.array([.13, .23, .37, .49, .51, .63, .77, .87])
    direct = exact.conserved(points, .15)
    independent_difference = float(abs(direct-independent.point(points, .15, origin=.5)).max())
    h = 1e-6
    qt = (exact.conserved(points, .15+h)-exact.conserved(points, .15-h))/(2*h)
    fx = (solver.physical_flux(exact.conserved(points+h, .15))
          - solver.physical_flux(exact.conserved(points-h, .15)))/(2*h)
    residual = float(np.max(abs(qt+fx)/np.maximum(1., abs(qt)+abs(fx))))
    return {'star_pressure_absolute_difference': float(star_pressure_difference),
            'independent_root_point_maximum_difference': independent_difference,
            'maximum_scaled_euler_residual': residual,
            'independent_root_diagnostics': independent.diagnostics,
            'derivative_step': h, 'residual_points': points.tolist(),
            'star_density': float(center[0]), 'star_pressure': float(solver.pressure(center))}


def measure(out, cfg):
    n, dx = len(out['q']), 1./len(out['q'])
    ref = exact.cell_averages(out['edges'], out['time'], order=cfg['reference_order'])
    refcheck = exact.cell_averages(out['edges'], out['time'], order=cfg['reference_check_order'])
    q, stages = out['q'], out['stage_history']
    residual = out['final_integral']-out['initial_integral']-out['boundary_net_integral']
    scale = np.maximum(1., abs(out['initial_integral'])+abs(out['boundary_net_integral']))
    minima = {name: min(s[name] for s in stages) for name in (
        'raw_endpoint_min_density', 'raw_endpoint_min_pressure', 'endpoint_min_density',
        'endpoint_min_pressure', 'fe_mean_min_density', 'fe_mean_min_pressure',
        'rk_mean_min_density', 'rk_mean_min_pressure', 'minimum_theta')}
    return {'n': n, 'time': out['time'], 'steps': out['steps'], 'stages': len(stages),
            'density_l1': relative_l1(q[:, 0], ref[:, 0], dx),
            'pressure_l1': relative_l1(solver.pressure(q), solver.pressure(ref), dx),
            'density_linf': float(abs(q[:, 0]-ref[:, 0]).max()),
            'pressure_linf': float(abs(solver.pressure(q)-solver.pressure(ref)).max()),
            'velocity_linf': float(abs(q[:, 1]/q[:, 0]-ref[:, 1]/ref[:, 0]).max()),
            'reference_quadrature_maximum': float(abs(ref-refcheck).max()),
            'scaled_cells': sum(s['scaled_cells'] for s in stages),
            'maximum_face_spectral_radius': max(s['maximum_face_spectral_radius'] for s in stages),
            'maximum_courant': max(s['courant'] for s in stages),
            'maximum_mean_preservation_defect': max(s['maximum_mean_preservation_defect'] for s in stages),
            'maximum_fe_boundary_balance_defect': max(s['maximum_fe_boundary_balance_defect'] for s in stages),
            'maximum_rk_boundary_balance_defect': max(s['maximum_rk_boundary_balance_defect'] for s in stages),
            'raw_endpoint_nonpositive_density_count': sum(s['raw_endpoint_nonpositive_density_count'] for s in stages),
            'initial_integral': out['initial_integral'].tolist(),
            'final_integral': out['final_integral'].tolist(),
            'boundary_net_integral': out['boundary_net_integral'].tolist(),
            'conservation_residual': residual.tolist(),
            'conservation_relative': (abs(residual)/scale).tolist(),
            'state_floor_count': out['state_floor_count'], 'rejected_steps': out['rejected_steps'],
            'retries': out['retries'], **minima}, ref


def decisions(rows, reference, cfg, limits):
    checks = []
    def add(name, value, bound, passed):
        checks.append({'name': name, 'value': value, 'bound': bound, 'passed': bool(passed)})
    add('all fixed refinements completed', [r['n'] for r in rows], cfg['grids'],
        [r['n'] for r in rows] == cfg['grids'])
    for row in rows:
        prefix = 'N'+str(row['n'])+': '
        add(prefix+'final time', row['time'], cfg['final_time'], row['time'] == cfg['final_time'])
        add(prefix+'three records per full SSP step', row['stages'], 3*row['steps'],
            row['stages'] == 3*row['steps'])
        for key in ('rk_mean_min_density', 'rk_mean_min_pressure', 'endpoint_min_density',
                    'endpoint_min_pressure', 'fe_mean_min_density', 'fe_mean_min_pressure'):
            add(prefix+key, row[key], 0, row[key] > 0)
        for key, bound in (('maximum_face_spectral_radius', cfg['fixed_lf_alpha']),
                           ('maximum_courant', cfg['positivity_cfl_bound']),
                           ('maximum_mean_preservation_defect', limits['mean_preservation']),
                           ('maximum_fe_boundary_balance_defect', limits['balance']),
                           ('maximum_rk_boundary_balance_defect', limits['balance'])):
            add(prefix+key, row[key], bound, row[key] <= bound)
        add(prefix+'zero mass/energy floor injections', row['state_floor_count'], 0,
            row['state_floor_count'] == 0)
        add(prefix+'zero retries or rejected steps', row['retries']+row['rejected_steps'], 0,
            row['retries']+row['rejected_steps'] == 0)
        add(prefix+'scaling actually exercised', row['scaled_cells'], 0, row['scaled_cells'] > 0)
        add(prefix+'raw nonadmissible reconstruction retained', row['raw_endpoint_min_pressure'], 0,
            row['raw_endpoint_min_pressure'] < 0)
        for component, value in zip(('mass', 'momentum', 'energy'), row['conservation_relative']):
            add(prefix+component+' boundary budget', value, limits['balance'], value <= limits['balance'])
        add(prefix+'split Gauss8/16 reference', row['reference_quadrature_maximum'],
            limits['reference_quadrature'], row['reference_quadrature_maximum'] <= limits['reference_quadrature'])
    if len(rows) == 3:
        for key in ('density_l1', 'pressure_l1'):
            add('finest '+key, rows[-1][key], limits['finest_'+key],
                rows[-1][key] <= limits['finest_'+key])
            for index in (1, 2):
                ratio = rows[index][key]/rows[index-1][key]
                add(key+' refinement ratio '+str(index), ratio, limits['refinement_ratio'],
                    ratio <= limits['refinement_ratio'])
    for key, bound in (('star_pressure_absolute_difference', 2e-13),
                       ('independent_root_point_maximum_difference', 2e-12),
                       ('maximum_scaled_euler_residual', limits['reference_euler_residual'])):
        value = reference.get(key)
        add('reference: '+key, value, bound, value is not None and value <= bound)
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=ROOT/'inputs.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())['cases'][CASE]
    limits = json.loads((ROOT/'acceptance.json').read_text())['limits']
    contract = json.loads((ROOT/'pre-run-contract.json').read_text())
    for name, expected in contract['files_sha256'].items():
        if sha(ROOT/name) != expected:
            raise ValueError('Frozen pre-run source hash mismatch: '+name)
    if cfg != json.loads((ROOT/'inputs.json').read_text())['cases'][CASE]:
        raise ValueError('Use the frozen qualified inputs without alteration')
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Use a new empty results directory')
    args.output.mkdir(parents=True, exist_ok=True)
    start, rows, files, failure, qualification = time.monotonic(), [], {}, None, {}
    try:
        qualification = reference_checks()
        for n in cfg['grids']:
            out = solver.solve(n, cfg['final_time'], cfg['fixed_lf_alpha'], cfg['cfl'],
                               cfg['reconstruction_epsilon'], cfg['max_steps_per_run'],
                               cfg['history_stride'])
            row, reference = measure(out, cfg)
            field, history = args.output/f'field-n{n}.npz', args.output/f'stages-n{n}.json'
            np.savez_compressed(field, q=out['q'], q_initial=out['initial'],
                                q_reference=reference, edges=out['edges'], time=out['time'],
                                q_history=out['snapshots'],
                                history_times=np.array([x['time'] for x in out['history']]))
            save(history, out['stage_history'])
            row.update(field=field.name, history=history.name)
            files[field.name], files[history.name] = sha(field), sha(history)
            rows.append(row)
    except Exception as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        if hasattr(error, 'failed_state'):
            np.savez_compressed(args.output/'failed-stage.npz', q=error.failed_state)
            save(args.output/'failed-completed-history.json', error.completed_history)
            failure['context'] = error.failed_context
    checks = decisions(rows, qualification, cfg, limits)
    passed = failure is None and all(c['passed'] for c in checks)
    with (args.output/(CASE+'.csv')).open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['n', 'steps', 'density_l1', 'pressure_l1',
                  'density_linf', 'pressure_linf', 'minimum_theta', 'scaled_cells'], extrasaction='ignore')
        writer.writeheader(); writer.writerows(rows)
    sources = {name: sha(ROOT/name) for name in [*contract['files_sha256'], 'pre-run-contract.json']}
    case = {'id': CASE, 'passed': passed, 'records': rows,
            'metrics': {k: v for k, v in rows[-1].items() if isinstance(v, (int, float))} if rows else {},
            'checks': {c['name']: c['passed'] for c in checks}, 'check_details': checks,
            'reference_qualification': qualification,
            'scope': 'One-dimensional Euler strong double rarefaction. Gallery heatmaps are saved x-t fields, not two-dimensional flow.'}
    result = {'schema_version': 1, 'passed': passed, 'checks': {CASE: passed}, 'cases': [case],
              'termination': 'calculation_failed' if failure else 'fixed_budget_completed',
              'input_sha256': sha(args.input), 'files_sha256': files, 'source_sha256': sources,
              'failure': failure, 'duration_seconds': time.monotonic()-start}
    save(args.output/'result.json', result)
    print(json.dumps({'passed': passed, 'runs': len(rows), 'gates': len(checks),
                      'failed': [c for c in checks if not c['passed']], 'failure': failure}), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
