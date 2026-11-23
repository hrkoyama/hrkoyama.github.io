#!/usr/bin/env python3
"""Run six fixed nonperiodic wall-flow grids and three separate pressure operators."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import wall_flow as s
from references.qualify_reference import ghia, qualify

ROOT = Path(__file__).resolve().parent


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path, value): Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def verify_contract():
    contract = json.loads((ROOT/'pre-run-contract.json').read_text())
    for name, expected in contract['files_sha256'].items():
        if sha(ROOT/name) != expected: raise ValueError('changed scientific contract: '+name)
    return contract


def boundary_max(q):
    return max(float(np.max(abs(q[0]))), float(np.max(abs(q[-1]))), float(np.max(abs(q[:, 0]))), float(np.max(abs(q[:, -1]))))


def rms(q): return float(np.sqrt(np.mean(q*q)))
def order(coarse, fine): return float(np.log2(coarse/fine))


def measure(out, lid):
    n = len(out['x']); h = out['h']; u = out['u']; v = out['v']; psi = out['psi']
    target = np.zeros_like(u); target[-1, 1:-1] = lid
    bmask = np.zeros_like(u, dtype=bool); bmask[[0, -1]] = True; bmask[:, [0, -1]] = True
    divergence = (u[1:-1, 2:]-u[1:-1, :-2]+v[2:, 1:-1]-v[:-2, 1:-1])/(2*h)
    return dict(n=n, h=h, time=out['time'], steps=out['steps'], dt=out['dt'],
                converged=out['converged'], steady_residual=out['residual'],
                poisson_residual=float(np.max(abs(s.laplacian(psi, h)+out['omega'][1:-1, 1:-1]))),
                divergence_maximum=float(np.max(abs(divergence))),
                u_boundary_error=float(np.max(abs((u-target)[bmask]))),
                v_boundary_error=float(np.max(abs(v[bmask]))),
                psi_boundary_error=boundary_max(psi),
                maximum_recorded_courant=float(out['history'][:, 3].max()),
                finite=all(bool(np.all(np.isfinite(out[k]))) for k in ['psi', 'omega', 'u', 'v', 'history']),
                repairs=out['state_clip_count']+out['retries'])


def base_checks(rows, limits):
    checks = {}
    for r in rows:
        p = 'n'+str(r['n'])+': '
        checks.update({
            p+'steady stop reached': r['converged'],
            p+'steady PDE residual': r['steady_residual'] <= limits['steady_residual'],
            p+'streamfunction Poisson residual': r['poisson_residual'] <= limits['poisson_residual'],
            p+'discrete divergence': r['divergence_maximum'] <= limits['discrete_divergence'],
            p+'u wall values': r['u_boundary_error'] <= limits['boundary_value'],
            p+'v wall values': r['v_boundary_error'] <= limits['boundary_value'],
            p+'psi wall values': r['psi_boundary_error'] <= limits['boundary_value'],
            p+'finite states and history': r['finite'],
            p+'no clipping or retry': r['repairs'] == 0,
            p+'recorded advective Courant': r['maximum_recorded_courant'] <= limits['maximum_recorded_courant'],
        })
    return checks


def cavity(cfg, limits, output):
    rows = []; table = ghia()
    for n in cfg['nodes']:
        out = s.solve(n, cfg['viscosity'], cfg['cavity_lid_speed'], 0., cfg['steady_stop_residual'], cfg['maximum_pseudo_time'], cfg['check_every_steps'], cfg['diffusive_dt_safety'])
        r = measure(out, cfg['cavity_lid_speed']); center = n//2
        for component in ['u', 'v']:
            profile = out[component][:, center] if component == 'u' else out[component][center]
            predicted = np.interp(table[component][:, 0], out['x'], profile)
            r[component+'_ghia_maximum'] = float(np.max(abs(predicted-table[component][:, 1])))
            r[component+'_ghia_rms'] = rms(predicted-table[component][:, 1])
            out[component+'_ghia_prediction'] = predicted
        iy, ix = np.unravel_index(np.argmin(out['psi']), out['psi'].shape)
        r['vortex_center_grid'] = [float(out['x'][ix]), float(out['y'][iy])]
        r['vortex_center_distance'] = float(np.hypot(out['x'][ix]-.6172, out['y'][iy]-.7344))
        r['streamfunction_minimum'] = float(out['psi'].min())
        r['centerline_maximum_error'] = max(r['u_ghia_maximum'], r['v_ghia_maximum'])
        r['field_file'] = f'cavity-n{n}.npz'
        np.savez_compressed(output/r['field_file'], **out)
        rows.append(r)
        print('cavity', n, 'residual', r['steady_residual'], 'Ghia max', r['centerline_maximum_error'], flush=True)
    checks = base_checks(rows, limits)
    fine = rows[-1]
    for c in ['u', 'v']:
        checks['finest '+c+' primary-table maximum error'] = fine[c+'_ghia_maximum'] <= limits['finest_ghia_'+c+'_maximum']
    for i in [1, 2]:
        checks['Ghia centerline refinement '+str(i)] = rows[i]['centerline_maximum_error']/rows[i-1]['centerline_maximum_error'] <= limits['consecutive_cavity_error_ratio']
    checks['finest primary-vortex grid location'] = fine['vortex_center_distance'] <= limits['finest_vortex_center_distance']
    return dict(id='cavity-ghia-re100', passed=all(checks.values()), checks=checks,
                metrics=dict(finest_u_ghia_maximum=fine['u_ghia_maximum'], finest_v_ghia_maximum=fine['v_ghia_maximum'], finest_vortex_center=fine['vortex_center_grid'], finest_steady_residual=fine['steady_residual']), records=rows)


def mms(cfg, limits, output):
    rows = []
    reference = qualify(s.manufactured, cfg['manufactured_amplitude'], cfg['viscosity'])
    for n in cfg['nodes']:
        out = s.solve(n, cfg['viscosity'], 0., cfg['manufactured_amplitude'], cfg['steady_stop_residual'], cfg['maximum_pseudo_time'], cfg['check_every_steps'], cfg['diffusive_dt_safety'])
        r = measure(out, 0.); X, Y = np.meshgrid(out['x'], out['y'])
        exact = s.manufactured(X, Y, cfg['manufactured_amplitude'], cfg['viscosity'])
        for k in ['psi', 'u', 'v', 'omega']:
            out[k+'_exact'] = exact[k]
            r[k+'_l2'] = rms((out[k]-exact[k])[1:-1, 1:-1])
        r['velocity_l2'] = float(np.hypot(r['u_l2'], r['v_l2']))
        r['wall_omega_maximum'] = max(float(np.max(abs((out['omega']-exact['omega'])[j, 1:-1]))) for j in [0, -1])
        _, du_dy = s.gradient(out['u'], out['h'])
        exact_shear = cfg['manufactured_amplitude']*X**2*(1-X)**2*(2-12*Y+12*Y**2)
        r['wall_shear_maximum'] = max(float(np.max(abs((du_dy-exact_shear)[j, 1:-1]))) for j in [0, -1])
        out['du_dy'] = du_dy; out['du_dy_exact'] = exact_shear
        imposed_from_exact = s.thom_wall(np.zeros_like(X), exact['psi'], out['h'], 0.)
        r['thom_exact_psi_wall_truncation'] = max(float(np.max(abs((imposed_from_exact-exact['omega'])[j, 1:-1]))) for j in [0, -1])
        pressure = s.pressure_manufactured(n)
        mask = np.zeros_like(X, dtype=bool); mask[[0, -1]] = True; mask[:, [0, -1]] = True
        r['pressure_l2'] = rms(pressure['p']-pressure['p_exact'])
        r['pressure_gradient_l2'] = float(np.hypot(rms(pressure['px']-pressure['px_exact']), rms(pressure['py']-pressure['py_exact'])))
        r['pressure_boundary_gradient_l2'] = float(np.hypot(rms((pressure['px']-pressure['px_exact'])[mask]), rms((pressure['py']-pressure['py_exact'])[mask])))
        r['pressure_boundary_error'] = boundary_max(pressure['p']-pressure['p_exact'])
        r['pressure_poisson_residual'] = float(np.max(abs(s.laplacian(pressure['p'], out['h'])+pressure['rhs'][1:-1, 1:-1])))
        r['pressure_finite'] = all(bool(np.all(np.isfinite(v))) for v in pressure.values())
        out.update({'pressure_'+k: v for k, v in pressure.items()})
        r['field_file'] = f'manufactured-n{n}.npz'
        np.savez_compressed(output/r['field_file'], **out)
        rows.append(r)
        print('manufactured', n, 'residual', r['steady_residual'], 'velocity L2', r['velocity_l2'], flush=True)
    checks = base_checks(rows, limits)
    for i in [1, 2]:
        for key in ['psi_l2', 'velocity_l2']:
            checks[key+' refinement '+str(i)] = rows[i][key]/rows[i-1][key] <= limits['maximum_consecutive_mms_error_ratio']
        for key in ['wall_omega_maximum', 'wall_shear_maximum']:
            checks[key+' refinement '+str(i)] = rows[i][key]/rows[i-1][key] <= limits['maximum_consecutive_wall_error_ratio']
    orders = {key: [order(rows[i-1][key], rows[i][key]) for i in [1, 2]] for key in ['psi_l2', 'velocity_l2', 'wall_omega_maximum', 'wall_shear_maximum', 'thom_exact_psi_wall_truncation', 'pressure_l2', 'pressure_gradient_l2', 'pressure_boundary_gradient_l2']}
    checks['finest streamfunction order'] = orders['psi_l2'][-1] >= limits['minimum_mms_streamfunction_order']
    checks['finest velocity order'] = orders['velocity_l2'][-1] >= limits['minimum_mms_velocity_order']
    checks['finest streamfunction accuracy'] = rows[-1]['psi_l2'] <= limits['finest_mms_streamfunction_l2']
    checks['finest velocity accuracy'] = rows[-1]['velocity_l2'] <= limits['finest_mms_velocity_l2']
    for r in rows:
        p = 'n'+str(r['n'])+': '
        checks[p+'separate pressure Dirichlet boundary'] = r['pressure_boundary_error'] <= limits['boundary_value']
        checks[p+'separate pressure Poisson residual'] = r['pressure_poisson_residual'] <= limits['poisson_residual']
        checks[p+'finite separate pressure solution'] = r['pressure_finite']
    for key, limit in [('pressure_l2', 'minimum_pressure_order'), ('pressure_gradient_l2', 'minimum_pressure_gradient_order'), ('pressure_boundary_gradient_l2', 'minimum_pressure_boundary_gradient_order')]:
        checks['finest separate '+key+' order'] = orders[key][-1] >= limits[limit]
    checks.update(reference['checks'])
    return dict(id='wall-manufactured', passed=all(checks.values()), checks=checks,
                metrics=dict(finest_velocity_l2=rows[-1]['velocity_l2'], finest_streamfunction_l2=rows[-1]['psi_l2'], observed_orders=orders, reference_qualification=reference, pressure_scope='Separate manufactured Dirichlet operator; cavity pressure not computed.'), records=rows)


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('--input', type=Path, default=ROOT/'inputs.json'); p.add_argument('--output', type=Path, required=True); args = p.parse_args()
    start = time.monotonic(); contract = verify_contract()
    cfg = json.loads(args.input.read_text()); limits = json.loads((ROOT/'acceptance.json').read_text())['limits']
    if sha(args.input) != sha(ROOT/'inputs.json'): raise ValueError('only frozen fixed input accepted')
    args.output.mkdir(parents=True, exist_ok=True)
    cases = [cavity(cfg, limits, args.output), mms(cfg, limits, args.output)]
    for case in cases:
        rows = case['records']; keys = list(dict.fromkeys(k for r in rows for k, v in r.items() if not isinstance(v, (dict, list))))
        with (args.output/(case['id']+'.csv')).open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=keys, extrasaction='ignore'); writer.writeheader(); writer.writerows(rows)
    checks = {'frozen scientific source contract': True, 'all fixed cases passed': all(c['passed'] for c in cases), 'six fixed flow grids completed': sum(len(c['records']) for c in cases) == 6}
    result = dict(schema_version=1, group='wall-flow', input_sha256=sha(args.input), acceptance_sha256=sha(ROOT/'acceptance.json'), source_sha256={name: sha(ROOT/name) for name in [*contract['files_sha256'], 'pre-run-contract.json']}, passed=all(checks.values()), checks=checks, cases=cases, numerical_gate_count=sum(len(c['checks']) for c in cases), seconds=time.monotonic()-start)
    dump(args.output/'result.json', result)
    print(json.dumps(dict(passed=result['passed'], numerical_gates=result['numerical_gate_count'], seconds=result['seconds'])), flush=True)
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__': main()
