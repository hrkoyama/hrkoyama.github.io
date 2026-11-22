"""Scientific invariants, independent references and explicit failure budgets."""
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest
from scipy import linalg, sparse
from scipy.sparse.linalg import spsolve

from run import diffusion_problem, krylov_matrix, validate_input
from solvers import (adaptive_simpson, arnoldi, back_substitute, dominant_ritz,
                     gauss_legendre, householder_qr, jacobi_svd, lanczos,
                     matrix_product, matrix_vector, smoothed_aggregation, solve_amg)


@pytest.mark.parametrize('n', [5, 9, 17])
def test_amg_matches_direct_and_discrete_sine_eigenmode(n):
    a, rhs, continuum, h = diffusion_problem(n)
    level = smoothed_aggregation(a)
    x, info = solve_amg(level, rhs, 1e-10)
    discrete_eigenvalue = 8 * math.sin(math.pi*h/2)**2 / h**2
    discrete = rhs / discrete_eigenvalue
    assert info['converged'] and info['termination'] == 'residual_tolerance'
    assert np.linalg.norm(x-discrete) / np.linalg.norm(discrete) < 1e-8
    assert np.linalg.norm(x-spsolve(a, rhs)) / np.linalg.norm(x) < 1e-8


def test_amg_is_coordinate_free_under_node_permutation():
    a, rhs, _, _ = diffusion_problem(11)
    order = np.random.default_rng(52).permutation(len(rhs))
    matrix = a[order][:, order]
    level = smoothed_aggregation(matrix)
    x, info = solve_amg(level, rhs[order], 1e-10)
    assert info['converged']
    assert np.linalg.norm(x-spsolve(matrix, rhs[order])) / np.linalg.norm(x) < 1e-8


def test_amg_budget_and_zero_rhs_are_distinct():
    a, rhs, _, _ = diffusion_problem(7)
    level = smoothed_aggregation(a)
    _, exhausted = solve_amg(level, rhs, max_cycles=0)
    zero, satisfied = solve_amg(level, np.zeros_like(rhs), max_cycles=0)
    assert not exhausted['converged'] and exhausted['termination'] == 'cycle_budget'
    assert satisfied['converged'] and satisfied['cycles'] == 0 and np.all(zero == 0)


def test_amg_rejects_nonsymmetric_and_indefinite_inputs():
    with pytest.raises(ValueError):
        smoothed_aggregation(sparse.csr_matrix([[2., 1.], [0., 2.]]))
    with pytest.raises(np.linalg.LinAlgError):
        smoothed_aggregation(sparse.csr_matrix([[1., 2.], [2., 1.]]))


@pytest.mark.parametrize('shape', [(3, 3), (9, 4), (5, 1)])
def test_householder_reconstruction_and_least_squares(shape):
    rng = np.random.default_rng(853)
    a, b = rng.normal(size=shape), rng.normal(size=shape[0])
    q, r = householder_qr(a)
    assert np.linalg.norm(q @ r - a) < 1e-12 * np.linalg.norm(a)
    assert np.linalg.norm(q.T @ q - np.eye(shape[1])) < 1e-12
    x = back_substitute(r, q.T @ b)
    reference = linalg.lstsq(a, b, lapack_driver='gelsy')[0]
    assert np.linalg.norm(x-reference) < 1e-10 * max(1., np.linalg.norm(reference))


def test_qr_zero_columns_and_triangular_singularity():
    a = np.zeros((5, 3)); q, r = householder_qr(a)
    assert np.linalg.norm(q @ r - a) == 0
    assert np.linalg.norm(q.T @ q - np.eye(3)) == 0
    with pytest.raises(ValueError):
        back_substitute(r, np.ones(3))
    with pytest.raises(ValueError):
        householder_qr(np.ones((2, 3)))


@pytest.mark.parametrize('rank', [0, 2, 4])
def test_jacobi_rank_and_minimum_norm_against_lapack(rank):
    rng = np.random.default_rng(456)
    left = rng.normal(size=(9, rank)); right = rng.normal(size=(rank, 4))
    a = left @ right
    u, s, vt, info = jacobi_svd(a)
    expected = linalg.svdvals(a)
    assert info['converged'] and info['rank'] == rank
    assert np.linalg.norm((u*s) @ vt - a) < 1e-11 * max(1., np.linalg.norm(a))
    assert np.linalg.norm(s - expected[:rank]) < 1e-11 * max(1., np.linalg.norm(expected))
    assert np.linalg.norm(u.T @ u - np.eye(rank)) < 1e-10
    assert np.linalg.norm(vt @ vt.T - np.eye(rank)) < 1e-10
    b = rng.normal(size=9)
    answer = vt.T @ ((u.T @ b)/s) if rank else np.zeros(4)
    reference = linalg.lstsq(a, b, cond=1e-12, lapack_driver='gelsd')[0]
    assert np.linalg.norm(answer-reference) < 1e-10 * max(1., np.linalg.norm(reference))


def test_jacobi_budget_exhaustion_is_not_success():
    a = np.random.default_rng(12).normal(size=(10, 5))
    *_, info = jacobi_svd(a, max_sweeps=0)
    assert not info['converged'] and info['termination'] == 'sweep_budget'
    assert info['sweeps'] == 0


@pytest.mark.parametrize('method', ['lanczos', 'arnoldi'])
def test_krylov_eigenpair_residual_against_dense_reference(method):
    a, start = krylov_matrix(32, 63, method == 'arnoldi')
    value, vector, info = dominant_ritz(a, start, 16, method, 1e-8)
    reference = linalg.eigvals(a)
    assert info['converged']
    assert min(abs(value-reference)) < 1e-10
    assert np.linalg.norm(matrix_vector(a, vector)-value*vector) < 1e-8
    assert info['orthogonality'] < 1e-11


def test_arnoldi_represents_complex_conjugate_eigenpairs():
    a = np.array([[2., -1.], [1., 2.]])
    q, h, info = arnoldi(a, np.array([1., 0.]), 2)
    assert info['happy_breakdown']
    assert np.max(abs(np.sort_complex(np.linalg.eigvals(h))-np.array([2-1j, 2+1j]))) < 1e-12
    assert np.linalg.norm(matrix_product(a, q)-matrix_product(q, h)) < 1e-12


def test_lanczos_happy_breakdown_and_invalid_inputs():
    q, t, info = lanczos(3*np.eye(6), np.ones(6), 4)
    assert info['happy_breakdown'] and info['dimensions'] == 1
    assert abs(t[0, 0]-3) < 1e-12
    with pytest.raises(ValueError):
        lanczos(np.array([[1., 1.], [0., 2.]]), np.ones(2), 2)
    with pytest.raises(ValueError):
        arnoldi(np.eye(2), np.zeros(2), 1)


@pytest.mark.parametrize('order', [1, 2, 5, 9])
def test_gauss_legendre_polynomial_exactness(order):
    x, w = gauss_legendre(order)
    assert np.all(w > 0) and np.all(abs(x) < 1)
    for degree in range(2*order):
        exact = 0 if degree % 2 else 2/(degree+1)
        assert abs(w @ x**degree-exact) < 1e-12


def test_gauss_legendre_known_two_point_rule():
    x, w = gauss_legendre(2)
    np.testing.assert_allclose(x, [-1/math.sqrt(3), 1/math.sqrt(3)], atol=1e-15)
    np.testing.assert_allclose(w, [1., 1.], atol=1e-15)
    with pytest.raises(ValueError):
        gauss_legendre(0)


@pytest.mark.parametrize('function,left,right,exact', [
    (math.exp, -1, 1, math.e-1/math.e),
    (math.sin, 0, math.pi, 2.),
    (lambda x: 1/(1+100*x*x), -1, 1, 2*math.atan(10)/10)])
def test_adaptive_simpson_matches_analytic_values(function, left, right, exact):
    r = adaptive_simpson(function, left, right, 1e-9)
    assert r['converged'] and r['termination'] == 'estimated_tolerance'
    assert abs(r['value']-exact) < 1e-9
    assert r['estimated_error'] <= 1e-9


def test_adaptive_budgets_and_nonfinite_integrand():
    for controls, reason in [({'max_evaluations': 5}, 'evaluation_budget'),
                             ({'max_depth': 0}, 'depth_budget')]:
        result = adaptive_simpson(math.exp, -1, 1, 1e-12, **controls)
        assert not result['converged'] and result['termination'] == reason
    with pytest.raises(ValueError):
        adaptive_simpson(lambda x: float('nan'), 0, 1)
    with pytest.raises(ValueError):
        adaptive_simpson(math.exp, 0, 1, float('inf'))


def test_fixed_input_cli_outputs_all_cases_and_rejects_reuse(tmp_path):
    here = Path(__file__).resolve().parent
    output = tmp_path/'output'
    command = [sys.executable, '-W', 'error', str(here/'run.py'), '--input', str(here/'inputs.json'), '--output', str(output)]
    process = subprocess.run(command, capture_output=True, text=True)
    assert process.returncode == 0, process.stderr
    result = json.loads((output/'result.json').read_text())
    assert result['passed'] and len(result['cases']) == 4
    assert all(c['passed'] for c in result['cases'])
    assert len(list(output.glob('*.csv'))) == 5
    repeat = subprocess.run(command, capture_output=True, text=True)
    assert repeat.returncode == 2 and 'empty output directory' in repeat.stderr


def test_nonfinite_acceptance_is_rejected_before_computation():
    data = json.loads((Path(__file__).parent/'inputs.json').read_text())
    data['amg']['acceptance']['relative_residual'] = float('inf')
    with pytest.raises(ValueError, match='nonfinite'):
        validate_input(data)
