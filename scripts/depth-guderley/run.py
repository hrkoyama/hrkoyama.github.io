#!/usr/bin/env python3
"""Execute three frozen pre-collapse spherical Guderley Euler refinements."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import guderley_solver as solver
from references.precollapse import GuderleyReference, TABULATED_LAMBDA

ROOT = Path(__file__).resolve().parent
CASE = 'guderley-implosion'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2,
                                    allow_nan=False) + '\n')


def norm(value, exact, volumes, mask=None):
    if mask is not None:
        value, exact, volumes = value[mask], exact[mask], volumes[mask]
    denominator = float(np.dot(abs(exact), volumes))
    if denominator <= 0 or not np.isfinite(denominator):
        raise ValueError('A finite nonzero reference norm is required')
    return float(np.dot(abs(value-exact), volumes)/denominator)


def shock_position(q, edges, radius, factors):
    """Finite-resolution pressure-gradient peak in a predetermined window."""
    pressure = solver.primitive(q)[2]
    centers = .5*(edges[1:]+edges[:-1])
    interfaces = .5*(centers[1:]+centers[:-1])
    window = ((interfaces >= factors[0]*radius)
              & (interfaces <= factors[1]*radius))
    if not np.any(window):
        raise ValueError('Empty shock-search window')
    gradient = abs(np.diff(pressure))
    if not np.all(np.isfinite(gradient)) or not np.any(gradient[window] > 0):
        raise ValueError('No resolved pressure jump in the fixed window')
    return float(interfaces[np.argmax(np.where(window, gradient, -1.))])


def reference_checks(reference, cfg):
    t = cfg['reference_residual_time']
    radius = reference.shock_radius(t)
    points = radius*np.array(cfg['reference_residual_radius_ratios'])
    h = cfg['reference_derivative_relative_step']*radius
    dt = cfg['reference_derivative_relative_step']*abs(t)
    q = reference.conserved_point(points, t)
    qt = (reference.conserved_point(points, t+dt)
          - reference.conserved_point(points, t-dt))/(2*dt)
    derivative = (solver.physical_flux(reference.conserved_point(points+h, t))
                  - solver.physical_flux(reference.conserved_point(points-h, t)))/(2*h)
    geometric_flux = 2*solver.physical_flux(q)/points[:, None]
    pressure = reference.point_state(points, t)[2]
    source = np.zeros_like(q)
    source[:, 1] = 2*pressure/points
    residual = qt + derivative + geometric_flux - source
    scale = np.maximum(1., abs(qt)+abs(derivative)+abs(geometric_flux)+abs(source))
    post = reference.conserved_point(np.array([radius*(1+1e-8)]), t)
    pre = reference.conserved_point(np.array([radius*(1-1e-8)]), t)
    speed = reference.shock_speed(t)
    left = solver.physical_flux(pre)-speed*pre
    right = solver.physical_flux(post)-speed*post
    jump = float(np.max(abs(left-right)/np.maximum(1., abs(left)+abs(right))))
    return {'maximum_scaled_euler_residual': float(np.max(abs(residual)/scale)),
            'maximum_scaled_jump_residual': jump,
            'lambda_table_relative_difference': abs(reference.lambda_/TABULATED_LAMBDA-1),
            'euler_residual_radii': points.tolist(), 'euler_residual_time': t,
            'radial_derivative_step': h, 'time_derivative_step': dt,
            'jump_state_radius_relative_offset': 1e-8,
            'metadata': reference.metadata()}


def measure(out, reference, cfg):
    q, edges, volumes = out['q'], out['edges'], out['volumes']
    rho, velocity, pressure, _ = solver.primitive(q)
    qr, pr = reference.cell_means(edges, out['time'], cfg['reference_order'])
    qc, pc = reference.cell_means(edges, out['time'], cfg['reference_check_order'])
    radius = reference.shock_radius(out['time'])
    centers = .5*(edges[:-1]+edges[1:])
    active = centers >= cfg['active_radius_factor']*radius
    if not np.any(active) or np.all(active):
        raise ValueError('Active norm must separate the nonzero-flow/shock region')
    shock = shock_position(q, edges, radius, cfg['shock_search_factors'])
    residual = (out['final_integral']-out['initial_integral']
                - out['boundary_net_integral']-out['geometric_source_integral'])
    scale = np.maximum(1., abs(out['initial_integral'])
                       + abs(out['boundary_net_integral'])
                       + abs(out['geometric_source_integral']))
    trajectory = []
    for history, state in zip(out['history'], out['snapshots']):
        exact_radius = reference.shock_radius(history['time'])
        measured = shock_position(state, edges, exact_radius, cfg['shock_search_factors'])
        trajectory.append({'time': history['time'], 'shock_radius': measured,
                           'reference_shock_radius': exact_radius,
                           'error_cells': abs(measured-exact_radius)/(edges[1]-edges[0])})
    record = {'n': len(q), 'time': out['time'], 'steps': out['steps'],
              'density_l1': norm(rho, qr[:, 0], volumes),
              'pressure_l1': norm(pressure, pr, volumes),
              'active_density_l1': norm(rho, qr[:, 0], volumes, active),
              'active_pressure_l1': norm(pressure, pr, volumes, active),
              'density_linf': float(np.max(abs(rho-qr[:, 0]))/np.max(qr[:, 0])),
              'pressure_linf': float(np.max(abs(pressure-pr))/np.max(pr)),
              'maximum_velocity_error': float(np.max(abs(velocity-qr[:, 1]/qr[:, 0]))),
              'active_volume_fraction': float(volumes[active].sum()/volumes.sum()),
              'active_inner_radius': cfg['active_radius_factor']*radius,
              'shock_radius': shock, 'reference_shock_radius': radius,
              'shock_error_cells': abs(shock-radius)/(edges[1]-edges[0]),
              'maximum_history_shock_error_cells': max(x['error_cells'] for x in trajectory),
              'minimum_density_all_stages': out['minimum_density_all_stages'],
              'minimum_pressure_all_stages': out['minimum_pressure_all_stages'],
              'minimum_internal_energy_all_stages': out['minimum_internal_energy_all_stages'],
              'sound_speed_roundoff_guard_evaluations': out['sound_speed_roundoff_guard_evaluations'],
              'minimum_pressure_at_sound_speed_guard': out['minimum_pressure_at_sound_speed_guard'],
              'state_floor_count': out['state_floor_count'], 'rejected_steps': out['rejected_steps'],
              'minimum_dt': out['minimum_dt'], 'maximum_dt': out['maximum_dt'],
              'reference_quadrature_density_l1': norm(qr[:, 0], qc[:, 0], volumes),
              'reference_quadrature_pressure_l1': norm(pr, pc, volumes),
              'initial_integral': out['initial_integral'].tolist(),
              'final_integral': out['final_integral'].tolist(),
              'boundary_net_integral': out['boundary_net_integral'].tolist(),
              'geometric_source_integral': out['geometric_source_integral'].tolist(),
              'conservation_residual': residual.tolist(),
              'conservation_relative': (abs(residual)/scale).tolist(),
              'shock_trajectory': trajectory}
    return record, qr, pr


def decisions(rows, reference, cfg, limits):
    checks = []
    def add(name, value, bound, passed):
        checks.append({'name': name, 'value': value, 'bound': bound, 'passed': bool(passed)})
    add('all three fixed spherical runs completed', [r['n'] for r in rows],
        cfg['grids'], [r['n'] for r in rows] == cfg['grids'])
    for row in rows:
        key = 'N'+str(row['n'])+': '
        add(key+'final time before collapse', row['time'], cfg['final_time'],
            row['time'] == cfg['final_time'])
        add(key+'strictly positive density all stages', row['minimum_density_all_stages'],
            0, row['minimum_density_all_stages'] > 0)
        for metric, bound in [('minimum_internal_energy_all_stages', 'minimum_internal_energy'),
                              ('minimum_pressure_at_sound_speed_guard', 'minimum_sound_guard_pressure')]:
            add(key+metric, row[metric], limits[bound], row[metric] >= limits[bound])
        for metric in ['state_floor_count', 'rejected_steps']:
            add(key+metric, row[metric], 0, row[metric] == 0)
        for index, component in enumerate(['mass', 'radial momentum including geometric source', 'energy']):
            add(key+component+' discrete balance', row['conservation_relative'][index],
                limits['balance'], row['conservation_relative'][index] <= limits['balance'])
        for metric in ['reference_quadrature_density_l1', 'reference_quadrature_pressure_l1',
                       'initial_reference_quadrature_density_l1', 'initial_reference_quadrature_pressure_l1']:
            add(key+metric, row[metric], limits['reference_quadrature'],
                row[metric] <= limits['reference_quadrature'])
        finite = all(np.isfinite(row[x]) for x in ['density_linf', 'pressure_linf',
                     'maximum_history_shock_error_cells', 'maximum_velocity_error'])
        add(key+'maximum and trajectory diagnostics retained', finite, True, finite)
    for metric, bound in [('maximum_scaled_euler_residual', 'reference_euler_residual'),
                          ('maximum_scaled_jump_residual', 'reference_jump_residual')]:
        value = reference.get(metric)
        add('similarity qualification: '+metric, value, limits[bound],
            value is not None and value <= limits[bound])
    value = reference.get('lambda_table_relative_difference')
    add('similarity exponent agrees with tabulated lambda', value, 2e-9,
        value is not None and value <= 2e-9)
    if len(rows) == len(cfg['grids']):
        fine = rows[-1]
        for metric in ['density_l1', 'pressure_l1', 'active_density_l1', 'active_pressure_l1', 'shock_error_cells']:
            bound = limits['finest_shock_cells' if metric == 'shock_error_cells' else 'finest_'+metric]
            add('finest '+metric, fine[metric], bound, fine[metric] <= bound)
        for metric in ['density_l1', 'active_density_l1', 'pressure_l1']:
            decreasing = all(a[metric] > b[metric] for a, b in zip(rows, rows[1:]))
            add(metric+' decreases across the three grids', decreasing, True, decreasing)
        order = float(np.log2(rows[-2]['active_density_l1']/fine['active_density_l1']))
        add('last-pair active density L1 slope', order, limits['minimum_last_pair_density_order'],
            order >= limits['minimum_last_pair_density_order'])
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())['cases'][CASE]
    limits = json.loads((ROOT/'acceptance.json').read_text())['limits']
    if (cfg['gamma'], cfg['dimension'], cfg['rho0'], cfg['upstream_pressure'],
        cfg['upstream_velocity'], cfg['radius'], cfg['shock_radius_at_minus_one'],
        cfg['initial_time'], cfg['final_time'], cfg['grids'], cfg['cfl']) != (
        1.4, 3, 1., 0., 0., .75, .6, -1., -.85, [128, 256, 512], .4):
        raise ValueError('Use the fixed qualified pre-collapse input family')
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Use a new empty output directory')
    args.output.mkdir(parents=True, exist_ok=True)
    started, rows, files, failure, qualification = time.monotonic(), [], {}, None, {}
    try:
        reference = GuderleyReference()
        qualification = reference_checks(reference, cfg)
        for n in cfg['grids']:
            edges, _, volumes = solver.geometry(n, cfg['radius'])
            initial, pi = reference.cell_means(edges, cfg['initial_time'], cfg['reference_order'])
            check, pc = reference.cell_means(edges, cfg['initial_time'], cfg['reference_check_order'])
            boundary = lambda t: reference.conserved_point(np.array([cfg['radius']]), t)[0]
            out = solver.solve(initial, edges, cfg['initial_time'], cfg['final_time'], cfg['cfl'],
                               boundary, cfg['max_steps_per_run'], cfg['history_stride'])
            row, qr, pr = measure(out, reference, cfg)
            row['initial_reference_quadrature_density_l1'] = norm(initial[:, 0], check[:, 0], volumes)
            row['initial_reference_quadrature_pressure_l1'] = norm(pi, pc, volumes)
            field, history = args.output/f'field-n{n}.npz', args.output/f'history-n{n}.json'
            np.savez_compressed(field, q=out['q'], q_initial=initial, q_reference=qr,
                                pressure_reference=pr, edges=edges, time=out['time'],
                                q_history=out['snapshots'],
                                history_times=np.array([x['time'] for x in out['history']]))
            save(history, out['history'])
            row.update(field=field.name, history=history.name)
            rows.append(row)
            files[field.name], files[history.name] = sha(field), sha(history)
    except Exception as error:
        failure = {'type': type(error).__name__, 'message': str(error),
                   'completed_grids': [r['n'] for r in rows]}
        if hasattr(error, 'failed_state'):
            np.savez_compressed(args.output/'failed-stage.npz', q=error.failed_state)
            save(args.output/'failed-completed-history.json', error.completed_history)
            failure['stage'] = error.failed_context
    checks = decisions(rows, qualification, cfg, limits)
    passed = failure is None and all(x['passed'] for x in checks)
    with (args.output/(CASE+'.csv')).open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['n', 'steps', 'density_l1', 'pressure_l1',
                     'active_density_l1', 'active_pressure_l1', 'shock_radius',
                     'reference_shock_radius', 'shock_error_cells'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    contract = json.loads((ROOT/'pre-run-contract.json').read_text())
    sources = {name: sha(ROOT/name) for name in [*contract['files_sha256'], 'pre-run-contract.json']}
    case = {'id': CASE, 'passed': passed, 'records': rows,
            'metrics': {key: value for key, value in rows[-1].items()
                        if isinstance(value, (int, float))} if rows else {},
            'checks': {c['name']: c['passed'] for c in checks}, 'check_details': checks,
            'reference_qualification': qualification,
            'scope': 'One-dimensional spherical radial Euler before collapse; a revolved meridional visualization is not a two-dimensional Cartesian evolution.'}
    result = {'schema_version': 1, 'passed': passed,
              'termination': 'calculation_failed' if failure else 'fixed_budget_completed',
              'input_sha256': sha(args.input), 'checks': {CASE: passed}, 'cases': [case],
              'files_sha256': files, 'source_sha256': sources, 'failure': failure,
              'duration_seconds': time.monotonic()-started}
    save(args.output/'result.json', result)
    print(json.dumps({'passed': passed, 'runs': len(rows), 'gates': len(checks),
                      'failed': [c for c in checks if not c['passed']], 'failure': failure}), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
