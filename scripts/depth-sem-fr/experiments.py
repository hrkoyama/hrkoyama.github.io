"""Fixed comparisons; all decisions use the input's predeclared tolerances."""
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from numpy.polynomial.legendre import legvander
from sem import solve, errors, exact, gradient
from fr import Operator, evolve
from legacy.fem import poisson_2d, error_norms
from legacy.advection import dg_advection


class Budget:
    def __init__(self, seconds):
        if not np.isfinite(seconds) or not 0 < seconds <= 90:
            raise ValueError('Require a positive budget of at most 90 seconds')
        self.deadline = time.monotonic()+seconds

    def check(self):
        if time.monotonic() >= self.deadline:
            raise RuntimeError('Fixed execution budget exhausted')


def check_baselines():
    root = Path(__file__).resolve().parent
    provenance = json.loads((root/'baseline-provenance.json').read_text())
    for name, source in provenance['files'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest() != source['sha256']:
            raise ValueError('Changed published baseline: '+name)


def validate(config):
    if config.get('schema_version') != 1 or list(config.get('cases', {})) != ['sem-poisson-2d', 'fr-periodic-advection']:
        raise ValueError('Use the complete two-case configuration')
    a, b = config['cases'].values()
    if a['elements'] != [2, 4, 8] or a['h_degree'] != 2 or a['p_elements'] != 2 or a['degrees'] != [1, 2, 3, 4, 5, 6] or a['p1_grids'] != [4, 8, 16]:
        raise ValueError('Unsupported SEM protocol')
    if b['grids'] != [8, 16, 32] or b['degrees'] != [1, 2] or b['speed'] != 1 or b['time'] != .25 or b['cfl'] != .15:
        raise ValueError('Unsupported FR protocol')
    for case in config['cases'].values():
        if not case['acceptance'] or not all(type(v) in (int, float) and np.isfinite(v) and v > 0 for v in case['acceptance'].values()):
            raise ValueError('Invalid acceptance criteria')
    if not np.isfinite(config['maximum_total_seconds']) or not 0 < config['maximum_total_seconds'] <= 90:
        raise ValueError('Invalid execution budget')


def order(coarse, fine):
    return float(np.log2(coarse/fine))


def sem_case(config, budget):
    rows = []; solutions = {}
    for kind, pairs in [('h', [(n, config['h_degree']) for n in config['elements']]),
                        ('p', [(config['p_elements'], p) for p in config['degrees']])]:
        for n, p in pairs:
            budget.check(); solution = solve(n, p); l2, h1 = errors(solution)
            rows.append({'series': kind, 'method': 'GLL-SEM', 'elements_per_axis': n, 'degree': p,
                         'total_dofs': int(solution.values.size), 'free_dofs': len(solution.free),
                         'l2_error': l2, 'h1_seminorm_error': h1, 'relative_residual': solution.residual})
            solutions[n, p] = solution
    p1_last = None
    for n in config['p1_grids']:
        budget.check(); baseline = poisson_2d(n)
        l2, h1 = error_norms(baseline, lambda xy: exact(xy[:, 0], xy[:, 1]),
                            lambda xy: np.column_stack(gradient(xy[:, 0], xy[:, 1])))
        rows.append({'series': 'h', 'method': 'published-P1-FEM', 'elements_per_axis': n, 'degree': 1,
                     'total_dofs': len(baseline.u), 'free_dofs': (n-1)**2, 'l2_error': l2,
                     'h1_seminorm_error': h1, 'relative_residual': baseline.residual/max(np.linalg.norm(baseline.rhs), np.finfo(float).tiny)})
        p1_last = baseline
    sh = [r for r in rows if r['method'] == 'GLL-SEM' and r['series'] == 'h']
    sp = [r for r in rows if r['method'] == 'GLL-SEM' and r['series'] == 'p']
    bh = [r for r in rows if r['method'] == 'published-P1-FEM']
    last = solutions[config['elements'][-1], config['h_degree']]
    metrics = {'sem_h_l2_order': order(sh[-2]['l2_error'], sh[-1]['l2_error']),
               'sem_h_h1_order': order(sh[-2]['h1_seminorm_error'], sh[-1]['h1_seminorm_error']),
               'p1_h_l2_order': order(bh[-2]['l2_error'], bh[-1]['l2_error']),
               'p1_h_h1_order': order(bh[-2]['h1_seminorm_error'], bh[-1]['h1_seminorm_error']),
               'p_refinement_l2_reduction': sp[0]['l2_error']/sp[-1]['l2_error'],
               'p6_l2_error': sp[-1]['l2_error'], 'same_dof_free_unknowns': len(last.free),
               'sem_finest_l2_error': sh[-1]['l2_error'], 'p1_finest_l2_error': bh[-1]['l2_error'],
               'same_dof_l2_ratio_sem_over_p1': sh[-1]['l2_error']/bh[-1]['l2_error'],
               'maximum_relative_residual': max(r['relative_residual'] for r in rows)}
    a = config['acceptance']
    checks = {'sem_h_l2_convergence': a['sem_l2_order_min'] < metrics['sem_h_l2_order'] < a['sem_l2_order_max'],
              'sem_h_h1_convergence': a['sem_h1_order_min'] < metrics['sem_h_h1_order'] < a['sem_h1_order_max'],
              'p1_h_l2_convergence': a['p1_l2_order_min'] < metrics['p1_h_l2_order'] < a['p1_l2_order_max'],
              'p1_h_h1_convergence': a['p1_h1_order_min'] < metrics['p1_h_h1_order'] < a['p1_h1_order_max'],
              'p_refinement_monotone': all(r['l2_error'] > s['l2_error'] for r, s in zip(sp, sp[1:])),
              'p_refinement_resolved': metrics['p_refinement_l2_reduction'] > a['p_reduction_min'] and metrics['p6_l2_error'] < a['p6_l2_max'],
              'equal_free_dofs': all(s['free_dofs'] == b['free_dofs'] for s, b in zip(sh, bh)),
              'same_dof_error_comparison': metrics['same_dof_l2_ratio_sem_over_p1'] < a['same_dof_ratio_max'],
              'linear_residuals': metrics['maximum_relative_residual'] < a['relative_residual_max'],
              'zero_dirichlet_boundary': bool(np.all(last.values[[0, -1], :] == 0) and np.all(last.values[:, [0, -1]] == 0))}
    checks = {name: bool(flag) for name, flag in checks.items()}
    result = {'id': 'sem-poisson-2d', 'passed': all(checks.values()), 'metrics': metrics, 'checks': checks, 'records': rows}
    x, y = np.meshgrid(last.nodes, last.nodes, indexing='ij')
    fields = {'x': x, 'y': y, 'sem': last.values, 'reference': exact(x, y),
              'p1_points': p1_last.points, 'p1_triangles': p1_last.cells, 'p1_values': p1_last.u}
    return result, fields


def fr_case(config, budget):
    rows = []; last_fields = {}; histories = []
    for p in config['degrees']:
        for n in config['grids']:
            op = Operator(n, p, config['speed'])
            u, start, stats = evolve(op, config['time'], config['cfl'], budget)
            qx, _, modes = dg_advection(n, p, config['time'], config['speed'], config['cfl'], initial=lambda x: .4+np.sin(2*np.pi*x))
            dg = modes@legvander(op.z, p).T
            exponential = op.exponential(start, config['time'])
            time_error = float(np.sqrt(np.sum((u-exponential)**2*op.w)/(2*n)))
            rows.append({'series': 'h', 'degree': p, 'cells': n, 'total_dofs': n*(p+1),
                         'l2_error': op.error(u, config['time']), 'exponential_l2_error': op.error(exponential, config['time']),
                         'rk3_vs_exponential_l2': time_error, 'fr_vs_published_dg_max': float(np.max(np.abs(u-dg))),
                         **{k: v for k, v in stats.items() if k != 'history'}})
            histories.append({'degree': p, 'cells': n, 'samples': stats['history']})
            if p == config['degrees'][-1] and n == config['grids'][-1]:
                last_fields = {'x': op.x, 'initial': start, 'fr': u, 'dg': dg,
                               'exponential': exponential, 'reference': .4+np.sin(2*np.pi*(op.x-config['speed']*config['time']))}
                last_op, last_start, last_exp = op, start, exponential
    half, _, half_stats = evolve(last_op, config['time'], config['cfl']/2, budget)
    half_error = float(np.sqrt(np.sum((half-last_exp)**2*last_op.w)/(2*last_op.n)))
    metrics = {}
    for p in config['degrees']:
        series = [r for r in rows if r['degree'] == p]
        metrics['p'+str(p)+'_l2_order'] = order(series[-2]['l2_error'], series[-1]['l2_error'])
        metrics['p'+str(p)+'_exponential_l2_order'] = order(series[-2]['exponential_l2_error'], series[-1]['exponential_l2_error'])
    metrics.update({'finest_l2_error': rows[-1]['l2_error'],
                    'maximum_fr_vs_published_dg': max(r['fr_vs_published_dg_max'] for r in rows),
                    'maximum_stage_mass_drift': max(r['max_mass_drift'] for r in rows),
                    'maximum_step_energy_increase': max(r['max_energy_increase'] for r in rows),
                    'maximum_scaled_courant': max(r['max_scaled_courant'] for r in rows),
                    'finest_rk3_time_error': rows[-1]['rk3_vs_exponential_l2'],
                    'halved_cfl_time_error': half_error,
                    'time_error_halving_ratio': half_error/rows[-1]['rk3_vs_exponential_l2'],
                    'actual_transport_l2_change': float(np.sqrt(np.sum((last_fields['fr']-last_start)**2*last_op.w)/(2*last_op.n)))})
    a = config['acceptance']
    checks = {'p1_l2_convergence': a['p1_order_min'] < metrics['p1_l2_order'] < a['p1_order_max'],
              'p2_l2_convergence': a['p2_order_min'] < metrics['p2_l2_order'] < a['p2_order_max'],
              'semidiscrete_spatial_convergence': a['p2_order_min'] < metrics['p2_exponential_l2_order'] < a['p2_order_max'],
              'finest_analytic_error': metrics['finest_l2_error'] < a['finest_l2_max'],
              'published_dg_agreement': metrics['maximum_fr_vs_published_dg'] < a['dg_difference_max'],
              'periodic_stage_mass': metrics['maximum_stage_mass_drift'] < a['mass_drift_max'],
              'nonincreasing_step_energy': metrics['maximum_step_energy_increase'] < a['energy_increase_max'],
              'scaled_courant_bound': metrics['maximum_scaled_courant'] <= config['cfl']*(1+1e-12),
              'time_error_control': metrics['finest_rk3_time_error'] < a['time_error_max'] and metrics['time_error_halving_ratio'] < a['halving_ratio_max'],
              'nontrivial_translation': metrics['actual_transport_l2_change'] > a['transport_change_min']}
    checks = {name: bool(flag) for name, flag in checks.items()}
    return {'id': 'fr-periodic-advection', 'passed': all(checks.values()), 'metrics': metrics,
            'checks': checks, 'records': rows, 'mass_energy_histories': histories,
            'time_refinement': {'cfl': config['cfl']/2, 'time_error': half_error, 'steps': half_stats['steps']}}, last_fields
