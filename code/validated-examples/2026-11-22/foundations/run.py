#!/usr/bin/env python3
"""Run four fast fixed-input foundation benchmarks, with analytic/library references."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
from scipy import integrate, linalg, sparse, special
from scipy.sparse.linalg import spsolve

from solvers import (adaptive_simpson, back_substitute, dominant_ritz,
                     gauss_legendre, householder_qr, jacobi_svd,
                     matrix_product, smoothed_aggregation, solve_amg)


def case_record(identifier, checks, metrics, records):
    return {'id': identifier, 'passed': bool(all(checks.values())),
            'checks': {k: bool(v) for k, v in checks.items()},
            'metrics': metrics, 'records': records}


def validate_input(data):
    if not isinstance(data, dict) or type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise ValueError('Unsupported fixed-input schema')

    def finite_values(value):
        if isinstance(value, dict):
            for child in value.values():
                finite_values(child)
        elif isinstance(value, list):
            for child in value:
                finite_values(child)
        elif isinstance(value, (float, int)) and not math.isfinite(value):
            raise ValueError('Input contains a nonfinite number')

    finite_values(data)
    for name in ['amg', 'decompositions', 'krylov', 'quadrature']:
        if not isinstance(data.get(name), dict) or not data[name].get('acceptance'):
            raise ValueError('Missing case controls/acceptance: '+name)
        for value in data[name]['acceptance'].values():
            if isinstance(value, bool) or not isinstance(value, (float, int)) or value <= 0:
                raise ValueError('Numerical acceptance widths must be finite and positive')


def diffusion_problem(n):
    """-Laplacian on the open unit square, zero Dirichlet boundary, five points."""
    if not isinstance(n, int) or n < 3:
        raise ValueError('Diffusion interior size must be an integer >=3')
    h = 1 / (n + 1)
    t = sparse.diags([-np.ones(n - 1), 2 * np.ones(n), -np.ones(n - 1)], [-1, 0, 1])
    a = (sparse.kron(sparse.eye(n), t) + sparse.kron(t, sparse.eye(n))).tocsr() / h**2
    x, y = np.meshgrid(np.arange(1, n + 1) * h, np.arange(1, n + 1) * h, indexing='ij')
    exact = (np.sin(np.pi * x) * np.sin(np.pi * y)).ravel()
    return a, 2 * np.pi**2 * exact, exact, h


def run_amg(config):
    controls, accept = config['controls'], config['acceptance']
    records, residual_records = [], []
    max_direct_error = max_residual = max_complexity = 0.0
    successful = True
    previous_error = previous_h = None
    for n in config['grid_sizes']:
        a, rhs, exact, h = diffusion_problem(n)
        hierarchy = smoothed_aggregation(a, strength=controls['strength'],
                                        coarse_size=controls['coarse_size'])
        actual, info = solve_amg(hierarchy, rhs, controls['relative_tolerance'], controls['max_cycles'])
        independent = spsolve(a, rhs)
        direct_error = float(np.linalg.norm(actual - independent) / np.linalg.norm(independent))
        pde_error = float(np.linalg.norm(actual - exact) / np.linalg.norm(exact))
        order = math.log(previous_error / pde_error) / math.log(previous_h / h) if previous_error else None
        levels, nonzeros = [], 0
        current = hierarchy
        while current is not None:
            levels.append(current.matrix.shape[0]); nonzeros += current.matrix.nnz
            current = current.coarse
        complexity = nonzeros / a.nnz
        successful &= info['converged'] and len(levels) >= 2
        max_direct_error, max_residual = max(max_direct_error, direct_error), max(max_residual, info['relative_residual'])
        max_complexity = max(max_complexity, complexity)
        records.append({'grid_n': n, 'unknowns': n*n, 'h': h, 'cycles': info['cycles'],
                        'relative_residual': info['relative_residual'], 'direct_solution_error': direct_error,
                        'pde_relative_l2_error': pde_error, 'observed_order': order,
                        'levels': len(levels), 'operator_complexity': complexity, 'termination': info['termination']})
        residual_records.extend({'grid_n': n, 'cycle': k, 'relative_residual': residual}
                                for k, residual in enumerate(info['history']))
        previous_error, previous_h = pde_error, h
    # A zero cycle budget must report nonconvergence rather than a nominal result.
    _, exhausted = solve_amg(hierarchy, rhs, controls['relative_tolerance'], max_cycles=0)
    orders = [r['observed_order'] for r in records if r['observed_order'] is not None]
    checks = {'all_residual_targets': successful and max_residual <= accept['relative_residual'],
              'independent_sparse_direct': max_direct_error <= accept['direct_solution_error'],
              'second_order_pde_refinement': bool(orders) and min(orders) >= accept['minimum_pde_order'],
              'bounded_operator_complexity': max_complexity <= accept['operator_complexity'],
              'cycle_budget_failure_reported': not exhausted['converged'] and exhausted['termination'] == 'cycle_budget'}
    result = case_record('sa-amg', checks, {'max_relative_residual': max_residual,
            'max_direct_solution_error': max_direct_error, 'minimum_pde_order': min(orders),
            'max_operator_complexity': max_complexity}, records)
    return result, residual_records


def decomposition_matrices(config):
    rng = np.random.default_rng(config['seed'])
    full = rng.normal(size=tuple(config['full_shape']))
    scaled = rng.normal(size=tuple(config['scaled_shape'])) @ np.diag(config['column_scales'])
    base = rng.normal(size=(config['deficient_rows'], 2))
    deficient = np.column_stack([base[:, 0], base[:, 1], base[:, 0] + 2*base[:, 1],
                                2*base[:, 0] - base[:, 1]])
    return [('full-rank', full), ('column-scaled', scaled), ('rank-deficient', deficient)]


def run_decompositions(config):
    accept, controls = config['acceptance'], config['controls']
    records, successful = [], True
    for name, a in decomposition_matrices(config):
        q, r = householder_qr(a)
        scale = np.linalg.norm(a)
        qr_error = float(np.linalg.norm(q @ r - a) / scale)
        qr_orthogonality = float(np.linalg.norm(q.T @ q - np.eye(q.shape[1]), 2))
        u, singular, vt, info = jacobi_svd(a, controls['jacobi_tolerance'],
                                         controls['max_sweeps'], controls['rank_rtol'])
        ref_u, ref_s, ref_vt = linalg.svd(a, full_matrices=False, lapack_driver='gesdd')
        padded = np.zeros(a.shape[1]); padded[:len(singular)] = singular
        singular_error = float(np.linalg.norm(padded - ref_s) / np.linalg.norm(ref_s))
        svd_error = float(np.linalg.norm((u * singular) @ vt - a) / scale)
        u_orth = float(np.linalg.norm(u.T @ u - np.eye(len(singular)), 2))
        v_orth = float(np.linalg.norm(vt @ vt.T - np.eye(len(singular)), 2))
        rhs = np.cos(np.arange(len(a)) + 0.3)
        x = vt.T @ ((u.T @ rhs) / singular) if len(singular) else np.zeros(a.shape[1])
        xref, _, reference_rank, _ = linalg.lstsq(a, rhs, cond=controls['rank_rtol'], lapack_driver='gelsd')
        ls_error = float(np.linalg.norm(x - xref) / max(1.0, np.linalg.norm(xref)))
        normal_residual = float(np.linalg.norm(a.T @ (a @ x - rhs)) /
                                max(1.0, np.linalg.norm(a) * np.linalg.norm(rhs)))
        qr_ls_error = None
        if name != 'rank-deficient':
            xqr = back_substitute(r, q.T @ rhs)
            qr_ls_error = float(np.linalg.norm(xqr - xref) / max(1.0, np.linalg.norm(xref)))
        successful &= info['converged'] and info['rank'] == int(reference_rank)
        records.append({'matrix': name, 'rows': a.shape[0], 'columns': a.shape[1],
                        'qr_reconstruction': qr_error, 'qr_orthogonality': qr_orthogonality,
                        'svd_reconstruction': svd_error, 'singular_value_error': singular_error,
                        'u_orthogonality': u_orth, 'v_orthogonality': v_orth,
                        'least_squares_solution_error': ls_error, 'normal_residual': normal_residual,
                        'qr_least_squares_error': qr_ls_error, 'rank': info['rank'],
                        'reference_rank': int(reference_rank), 'jacobi_sweeps': info['sweeps'],
                        'termination': info['termination']})
    _, _, _, exhausted = jacobi_svd(decomposition_matrices(config)[0][1], max_sweeps=0)
    maximum = lambda key: max(row[key] for row in records if row[key] is not None)
    checks = {'all_jacobi_converged_and_ranks_match': successful,
              'householder_reconstruction': maximum('qr_reconstruction') <= accept['reconstruction'],
              'householder_orthogonality': maximum('qr_orthogonality') <= accept['orthogonality'],
              'jacobi_reconstruction': maximum('svd_reconstruction') <= accept['reconstruction'],
              'jacobi_orthogonality': max(maximum('u_orthogonality'), maximum('v_orthogonality')) <= accept['orthogonality'],
              'independent_lapack_singular_values': maximum('singular_value_error') <= accept['singular_value_error'],
              'independent_minimum_norm_least_squares': maximum('least_squares_solution_error') <= accept['least_squares_error'],
              'qr_least_squares': maximum('qr_least_squares_error') <= accept['least_squares_error'],
              'least_squares_stationarity': maximum('normal_residual') <= accept['normal_residual'],
              'sweep_budget_failure_reported': not exhausted['converged'] and exhausted['termination'] == 'sweep_budget'}
    return case_record('qr-svd-factorization', checks,
        {'max_qr_reconstruction': maximum('qr_reconstruction'),
         'max_svd_reconstruction': maximum('svd_reconstruction'),
         'max_singular_value_error': maximum('singular_value_error'),
         'max_least_squares_error': maximum('least_squares_solution_error'),
         'max_orthogonality': max(maximum('qr_orthogonality'), maximum('u_orthogonality'), maximum('v_orthogonality'))}, records)


def krylov_matrix(n, seed, nonsymmetric=False):
    rng = np.random.default_rng(seed)
    # The reference orthogonal similarity constructs a controlled spectrum only;
    # the eigensolver under test does not call QR or a full-matrix eigensolver.
    rotation, _ = np.linalg.qr(rng.normal(size=(n, n)))
    diagonal = np.r_[np.linspace(-1, 1, n - 1), 5.0]
    core = np.diag(diagonal)
    if nonsymmetric:
        core += np.diag(np.full(n - 1, 0.2), 1)
    return matrix_product(matrix_product(rotation, core), rotation.T), rng.normal(size=n)


def run_krylov(config):
    accept = config['acceptance']; records = []; all_good = True; fine_residuals = []
    for method in ['lanczos', 'arnoldi']:
        for n in config['sizes']:
            a, start = krylov_matrix(n, config['seed'] + n, method == 'arnoldi')
            reference = float(np.max(linalg.eigvalsh(a))) if method == 'lanczos' else max(linalg.eigvals(a), key=lambda z: z.real)
            sequence = []
            for dimensions in config['dimensions']:
                value, _, info = dominant_ritz(a, start, dimensions, method, accept['eigenpair_residual'])
                error = float(abs(value - reference))
                row = {'method': method, 'size': n, 'dimensions': dimensions,
                       'eigenvalue_real': float(value.real), 'eigenvalue_imag': float(value.imag),
                       'reference_real': float(reference.real), 'reference_imag': float(reference.imag),
                       'eigenvalue_error': error, 'eigenpair_residual': info['residual'],
                       'orthogonality': info['orthogonality'], 'termination': info['termination']}
                records.append(row); sequence.append(row)
            fine = sequence[-1]; fine_residuals.append(fine['eigenpair_residual'])
            all_good &= (fine['eigenpair_residual'] <= accept['eigenpair_residual'] and
                         fine['eigenvalue_error'] <= accept['eigenvalue_error'] and
                         fine['eigenpair_residual'] < sequence[0]['eigenpair_residual'])
    _, _, exhausted = dominant_ritz(a, start, 1, 'arnoldi', accept['eigenpair_residual'])
    checks = {'independent_dense_eigenvalues_and_residuals': all_good,
              'krylov_basis_orthogonality': max(x['orthogonality'] for x in records) <= accept['orthogonality'],
              'dimension_budget_failure_reported': not exhausted['converged'] and exhausted['termination'] == 'dimension_budget'}
    return case_record('krylov-eigenvalues', checks,
        {'max_final_eigenpair_residual': max(fine_residuals),
         'max_basis_orthogonality': max(x['orthogonality'] for x in records)}, records)


def run_quadrature(config):
    accept = config['acceptance']; records = []; largest_moment_error = largest_rule_error = 0.0
    exact_exp = math.e - 1 / math.e
    for order in config['gauss_orders']:
        nodes, weights = gauss_legendre(order)
        ref_nodes, ref_weights = special.roots_legendre(order)
        rule_error = max(float(np.max(abs(nodes - ref_nodes))), float(np.max(abs(weights - ref_weights))))
        moment_error = max(abs(float(weights @ nodes**k) - (0 if k % 2 else 2/(k+1))) for k in range(2*order))
        error = abs(float(weights @ np.exp(nodes)) - exact_exp)
        largest_rule_error, largest_moment_error = max(largest_rule_error, rule_error), max(largest_moment_error, moment_error)
        records.append({'method': 'gauss-legendre', 'order_or_tolerance': order, 'integral': float(weights @ np.exp(nodes)),
                        'analytic_error': error, 'scipy_rule_error': rule_error, 'moment_error': moment_error,
                        'evaluations': order, 'estimated_error': None, 'termination': 'fixed_order'})
    gaussian_final_error = records[-1]['analytic_error']
    functions = [('exponential', math.exp, -1.0, 1.0, exact_exp),
                 ('lorentzian', lambda x: 1/(1 + config['peak_scale']**2*x*x), -1.0, 1.0,
                  2*math.atan(config['peak_scale'])/config['peak_scale'])]
    all_adaptive = True; largest_normalized_error = 0.0
    for name, function, left, right, exact in functions:
        independent, _ = integrate.quad(function, left, right, epsabs=1e-13, epsrel=1e-13)
        for tolerance in config['adaptive_tolerances']:
            answer = adaptive_simpson(function, left, right, tolerance, config['max_evaluations'])
            error = abs(answer['value'] - exact)
            reference_error = abs(answer['value'] - independent)
            largest_normalized_error = max(largest_normalized_error, error/tolerance)
            all_adaptive &= answer['converged'] and error <= accept['adaptive_tolerance_factor']*tolerance and reference_error <= accept['adaptive_tolerance_factor']*tolerance
            records.append({'method': 'adaptive-simpson-'+name, 'order_or_tolerance': tolerance,
                            'integral': answer['value'], 'analytic_error': error,
                            'scipy_rule_error': reference_error, 'moment_error': None,
                            'evaluations': answer['evaluations'], 'estimated_error': answer['estimated_error'],
                            'termination': answer['termination']})
    exhausted = adaptive_simpson(math.exp, -1, 1, absolute_tolerance=1e-12, max_evaluations=5)
    checks = {'gauss_polynomial_moments': largest_moment_error <= accept['moment_error'],
              'independent_scipy_gauss_rule': largest_rule_error <= accept['rule_error'],
              'gauss_nonsingular_refinement': gaussian_final_error <= accept['gauss_final_error'] and records[0]['analytic_error'] > gaussian_final_error,
              'adaptive_exact_and_quad_references': all_adaptive,
              'evaluation_budget_failure_reported': not exhausted['converged'] and exhausted['termination'] == 'evaluation_budget'}
    return case_record('gauss-adaptive-quadrature', checks,
        {'max_polynomial_moment_error': largest_moment_error, 'max_scipy_rule_error': largest_rule_error,
         'gauss_final_exp_error': gaussian_final_error, 'max_adaptive_error_over_tolerance': largest_normalized_error,
         'budget_failure_evaluations': exhausted['evaluations']}, records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    validate_input(data)
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Choose a new or empty output directory')
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    amg, residuals = run_amg(data['amg'])
    cases = [amg, run_decompositions(data['decompositions']),
             run_krylov(data['krylov']), run_quadrature(data['quadrature'])]
    for case in cases:
        path = args.output/(case['id']+'.csv')
        with path.open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(case['records'][0])); writer.writeheader(); writer.writerows(case['records'])
    with (args.output/'amg-residuals.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(residuals[0])); writer.writeheader(); writer.writerows(residuals)
    result = {'schema_version': 1, 'family': 'depth-foundations',
              'input_sha256': hashlib.sha256(args.input.read_bytes()).hexdigest(),
              'checks': {x['id']: x['passed'] for x in cases}, 'passed': all(x['passed'] for x in cases),
              'cases': cases, 'duration_seconds': time.perf_counter()-started,
              'termination': 'fixed_cases_completed',
              'environment': {'python': platform.python_version(), **{n: importlib.metadata.version(n) for n in ['numpy', 'scipy']}},
              'reference_scope': 'Analytic manufactured diffusion/integrals and spectra; separate SciPy sparse direct, LAPACK SVD/least-squares/dense eigenvalues, roots_legendre and QUADPACK. No external AMG implementation comparison.'}
    (args.output/'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': result['passed'], 'cases': result['checks'], 'duration_seconds': result['duration_seconds']}))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, OSError) as error:
        print(json.dumps({'error': type(error).__name__, 'message': str(error)}), file=sys.stderr)
        raise SystemExit(2)
