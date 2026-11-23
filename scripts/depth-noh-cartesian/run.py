#!/usr/bin/env python3
"""Run three fixed 2D Cartesian Noh grids, retaining every failed decision."""
import argparse
import csv
import datetime
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import cartesian_solver as solver
import cartesian_reference as reference

CASE = 'noh-cartesian-2d'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def relative_l1(value, exact, mask=None):
    if mask is not None:
        value, exact = value[mask], exact[mask]
    if not value.size:
        raise ValueError('The declared measurement mask is empty')
    return float(np.sum(abs(value-exact))/np.sum(abs(exact)))


def crossing(distance, pressure):
    idx = np.flatnonzero((pressure[:-1] >= 8/3) & (pressure[1:] < 8/3))
    if not len(idx):
        return None
    i = idx[-1]
    return float(distance[i]+(distance[i+1]-distance[i])*(pressure[i]-8/3)/(pressure[i]-pressure[i+1]))


def parity_error(q):
    rho = q[..., 0]
    scale = max(1., float(abs(q).max()))
    flipx = q[:, ::-1]*np.array([1., -1., 1., 1.])
    flipy = q[::-1]*np.array([1., 1., -1., 1.])
    swap = np.transpose(q, (1, 0, 2))[..., [0, 2, 1, 3]]
    return max(float(abs(q-flipx).max()), float(abs(q-flipy).max()), float(abs(q-swap).max()))/scale


def measure(solution, config):
    q, edges = solution['q'], solution['edges']
    rho, ux, uy, pressure, _ = solver.primitive(q)
    n, t = len(rho), solution['time']
    dx = edges[1]-edges[0]
    centers = .5*(edges[:-1]+edges[1:])
    x, y = np.meshgrid(centers, centers)
    radius = np.hypot(x, y)
    rs = t/3
    exact, mean_pressure = reference.cell_means(edges, t, config['reference_order'])
    finer, _ = reference.cell_means(edges, t, config['reference_check_order'])
    far = np.hypot(abs(x)+dx/2, abs(y)+dx/2)
    near = np.hypot(np.maximum(abs(x)-dx/2, 0), np.maximum(abs(y)-dx/2, 0))
    core = far <= .70*rs
    plateau = core & (near >= .30*rs)
    center = radius <= .25*rs
    axis_p = .5*(pressure[n//2]+pressure[n//2-1])[n//2:]
    diagonal_p = np.diag(pressure)[n//2:]
    axis = crossing(centers[n//2:], axis_p)
    diagonal = crossing(np.sqrt(2)*centers[n//2:], diagonal_p)
    sie = pressure/((solver.GAMMA-1)*rho)
    residual = solution['final_integral']-solution['initial_integral']-solution['boundary_net_integral']
    mass = reference.total_mass(t, config['radius'])
    scales = np.array([mass, mass, mass, .5*mass])
    m = {'n': n, 'steps': solution['steps'], 'time': t,
         'density_l1': relative_l1(rho, exact),
         'density_l2': float(np.sqrt(np.sum((rho-exact)**2)/np.sum(exact**2))),
         'density_linf': float(np.max(abs(rho-exact))/np.max(exact)),
         'core_density_l1': relative_l1(rho, exact, core),
         'plateau_density_relative_error': float(abs(np.mean(rho[plateau])/16-1)),
         'plateau_pressure_relative_error': float(abs(np.mean(pressure[plateau])/(16/3)-1)),
         'center_max_internal_energy_excess': float(np.max(sie[center])/.5-1),
         'center_min_density': float(np.min(rho[center])),
         'density_min': float(rho.min()), 'density_max': float(rho.max()),
         'minimum_density_all_stages': solution['minimum_density'],
         'minimum_pressure_all_stages': solution['minimum_pressure'],
         'minimum_internal_roundoff_units': solution['minimum_internal_roundoff_units'],
         'state_floor_count': solution['state_floor_count'],
         'd4_conserved_parity_relative': parity_error(q),
         'reference_order_relative_l1_difference': relative_l1(exact, finer),
         'reference_mass_relative_error': float(abs(np.sum(exact)*dx**2/mass-1)),
         'mass_vs_analytic_relative': float(abs(solution['final_integral'][0]/mass-1)),
         'energy_vs_analytic_relative': float(abs(solution['final_integral'][3]/(.5*mass)-1)),
         'axis_shock_radius': axis, 'diagonal_shock_radius': diagonal,
         'axis_shock_error_cells': None if axis is None else abs(axis-rs)/dx,
         'diagonal_shock_error_cells': None if diagonal is None else abs(diagonal-rs)/dx,
         'shock_axis_diagonal_difference_cells': None if axis is None or diagonal is None else abs(axis-diagonal)/dx,
         'initial_integral': solution['initial_integral'].tolist(),
         'final_integral': solution['final_integral'].tolist(),
         'boundary_net_integral': solution['boundary_net_integral'].tolist(),
         'conservation_residual': residual.tolist(),
         'conservation_relative': (abs(residual)/scales).tolist()}
    return m, exact, mean_pressure


def decisions(records, acceptance, config):
    rows = []
    def add(name, value, bound, passed):
        rows.append({'name': name, 'value': value, 'bound': bound, 'passed': bool(passed)})
    a = acceptance['limits']
    add('all three Cartesian grids complete', [r['n'] for r in records], config['grids'], [r['n'] for r in records] == config['grids'])
    for r in records:
        stem = 'n'+str(r['n'])+': '
        add(stem+'positive density all stages', r['minimum_density_all_stages'], 0, r['minimum_density_all_stages'] > 0)
        add(stem+'internal energy within roundoff', r['minimum_internal_roundoff_units'], -64, r['minimum_internal_roundoff_units'] >= -64)
        add(stem+'no floors or cell repair', r['state_floor_count'], 0, r['state_floor_count'] == 0)
        for j, label in enumerate(['mass', 'x momentum', 'y momentum', 'energy']):
            v = r['conservation_relative'][j]
            add(stem+label+' discrete balance', v, a['balance'], v <= a['balance'])
        for key, limit in [('mass_vs_analytic_relative', 'balance'), ('energy_vs_analytic_relative', 'balance'),
                           ('d4_conserved_parity_relative', 'parity'),
                           ('reference_order_relative_l1_difference', 'reference_order'),
                           ('reference_mass_relative_error', 'reference_mass')]:
            add(stem+key, r[key], a[limit], r[key] <= a[limit])
        finite = all(np.isfinite(r[k]) for k in ['center_max_internal_energy_excess', 'center_min_density', 'density_l2', 'density_linf'])
        add(stem+'unmasked center and maximum errors reported', finite, True, finite)
    if records:
        r = records[-1]
        for key, limit in [('density_l1','density_l1'), ('core_density_l1','core_density_l1'),
                           ('plateau_density_relative_error','plateau_density'), ('plateau_pressure_relative_error','plateau_pressure'),
                           ('axis_shock_error_cells','shock_cells'), ('diagonal_shock_error_cells','shock_cells'),
                           ('shock_axis_diagonal_difference_cells','angular_cells')]:
            v = r[key]
            add('finest '+key, v, a[limit], v is not None and v <= a[limit])
        decreasing = all(x['density_l1'] > y['density_l1'] for x, y in zip(records[:-1], records[1:]))
        add('density L1 decreases', decreasing, True, decreasing)
        order = None if len(records) < 2 else float(np.log2(records[-2]['density_l1']/r['density_l1']))
        add('last pair density L1 order', order, a['order'], order is not None and order >= a['order'])
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    config = json.loads(args.input.read_text())['cases'][CASE]
    if config['gamma'] != solver.GAMMA or config['p0'] != 0 or config['rho0'] != 1 or config['speed'] != 1:
        raise ValueError('This verification is fixed to gamma5/3, rho1, speed1, p0=0')
    acceptance = json.loads((root/'acceptance.json').read_text())
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Use a new empty output directory')
    args.output.mkdir(parents=True, exist_ok=True)
    records, files, failure = [], {}, None
    started = time.monotonic()
    for n in config['grids']:
        try:
            solution = solver.solve(n, config['radius'], config['final_time'], config['cfl'])
            m, exact, exact_p = measure(solution, config)
            field = args.output/('field-n'+str(n)+'.npz')
            np.savez_compressed(field, q=solution['q'], edges=solution['edges'], density_reference=exact,
                                pressure_physical_mean_reference=exact_p, time=solution['time'])
            history = args.output/('history-n'+str(n)+'.json')
            save(history, solution['history'])
            files[field.name], files[history.name] = sha(field), sha(history)
            m['field'], m['history'] = field.name, history.name
            records.append(m)
        except Exception as error:
            failure = {'n': n, 'type': type(error).__name__, 'message': str(error)}
            if hasattr(error, 'failed_state'):
                np.savez_compressed(args.output/'failed-stage.npz', q=error.failed_state)
                failure['stage'] = error.failed_context
                save(args.output/'failed-completed-history.json', error.completed_history)
            break
    checks = decisions(records, acceptance, config)
    passed = failure is None and all(r['passed'] for r in checks)
    with (args.output/(CASE+'.csv')).open('w', newline='') as handle:
        keys = ['n','steps','density_l1','density_l2','density_linf','core_density_l1','axis_shock_radius','diagonal_shock_radius','shock_axis_diagonal_difference_cells','center_max_internal_energy_excess']
        writer = csv.DictWriter(handle, fieldnames=keys, extrasaction='ignore');writer.writeheader();writer.writerows(records)
    source = {name: sha(root/name) for name in ['cartesian_solver.py','cartesian_reference.py','run.py','inputs.json','acceptance.json','pre-run-contract.json']}
    source['pre-run-envelope-contract.json'] = sha(root/'pre-run-envelope-contract.json')
    case = {'id': CASE, 'passed': passed, 'records': records,
            'checks': {r['name']: r['passed'] for r in checks}, 'check_details': checks,
            'metrics': {k:v for k,v in records[-1].items() if isinstance(v,(int,float))} if records else {},
            'scope': 'Actual full-square 2D Cartesian Euler; three small fixed grids, no radial reduction.'}
    result = {'schema_version':1, 'passed':passed, 'cases':[case], 'checks':{CASE:passed},
              'duration_seconds':time.monotonic()-started, 'failure':failure, 'files_sha256':files,
              'source_sha256':source, 'input_sha256':sha(args.input), 'termination':'fixed_budget_completed'}
    save(args.output/'result.json', result)
    print(json.dumps({'passed':passed,'runs':len(records),'gates':len(checks),'failed':[r for r in checks if not r['passed']],'failure':failure}), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
