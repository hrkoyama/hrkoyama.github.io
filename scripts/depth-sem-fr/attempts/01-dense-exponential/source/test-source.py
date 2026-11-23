"""Representative mathematical, solver, provenance and driver checks."""
import json
from pathlib import Path
import numpy as np
import pytest
from numpy.polynomial.legendre import Legendre, leggauss
from polynomials import cardinal, degree, gll
from sem import solve, errors
from fr import Operator, corrections, evolve
from experiments import Budget, check_baselines, fr_case, sem_case, validate
from legacy.advection import dg_advection
from numpy.polynomial.legendre import legvander
from run import run

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT/'inputs.json').read_text())


def test_gll_moments():
    for p in range(1, 7):
        x, w = gll(p)
        assert np.all(w > 0) and x[0] == -1 and x[-1] == 1
        for k in range(2*p):
            assert abs(w@x**k-(0 if k % 2 else 2/(k+1))) < 2e-14


def test_cardinal_partition():
    for p in range(1, 7):
        x, _ = gll(p); q = np.linspace(-1, 1, 19)
        np.testing.assert_allclose(cardinal(x, x), np.eye(p+1), atol=2e-14)
        np.testing.assert_allclose(cardinal(x, q).sum(axis=1), 1, atol=2e-14)


def test_exact_polynomial_derivatives():
    for p in range(1, 7):
        x, _ = gll(p); q = np.linspace(-1, 1, 17); d = cardinal(x, q, derivative=True)
        for k in range(p+1):
            np.testing.assert_allclose(d@(x**k), k*q**(k-1) if k else np.zeros_like(q), atol=2e-13)


def test_gll_summation_by_parts():
    for p in range(1, 7):
        x, w = gll(p); d = cardinal(x, x, derivative=True); b = np.zeros((p+1, p+1)); b[0, 0] = -1; b[-1, -1] = 1
        np.testing.assert_allclose(w[:, None]*d+d.T*w[None, :], b, atol=3e-13)


def test_invalid_polynomial_inputs():
    for p in [0, 7, 1.5, True]:
        with pytest.raises(ValueError): degree(p)
    with pytest.raises(ValueError): cardinal([0., 0.], [0.])
    with pytest.raises(ValueError): cardinal([0., np.nan], [0.])


def test_sem_nonzero_dirichlet_affine_patch():
    s = solve(2, 1, forcing=lambda x, y: x*0, boundary=lambda x, y: 1+x+2*y)
    x, y = np.meshgrid(s.nodes, s.nodes, indexing='ij')
    np.testing.assert_allclose(s.values, 1+x+2*y, atol=2e-13)


def test_sem_quadratic_tensor_patch():
    value = lambda x, y: x*(1-x)*y*(1-y)
    grad = lambda x, y: ((1-2*x)*y*(1-y), x*(1-x)*(1-2*y))
    s = solve(2, 2, forcing=lambda x, y: 2*(x*(1-x)+y*(1-y)))
    l2, h1 = errors(s, value=value, derivative=grad)
    assert l2 < 2e-14 and h1 < 2e-13


def test_sem_symmetric_positive_reduced_operator():
    s = solve(2, 3); a = s.stiffness[s.free][:, s.free].toarray()
    np.testing.assert_allclose(a, a.T, atol=3e-14)
    assert np.linalg.eigvalsh(a)[0] > 0
    assert s.residual < 1e-12


def test_sem_error_quadrature_is_resolved():
    s = solve(2, 3)
    np.testing.assert_allclose(errors(s, quadrature=7), errors(s, quadrature=10), rtol=1e-8, atol=1e-13)


def test_sem_error_is_continuous_not_only_at_nodes():
    s = solve(2, 1, forcing=lambda x, y: x*0)
    value = lambda x, y: np.sin(2*np.pi*x)*np.sin(2*np.pi*y)
    grad = lambda x, y: (2*np.pi*np.cos(2*np.pi*x)*np.sin(2*np.pi*y), 2*np.pi*np.sin(2*np.pi*x)*np.cos(2*np.pi*y))
    l2, h1 = errors(s, value=value, derivative=grad, quadrature=12)
    assert abs(l2-.5) < 1e-12 and abs(h1-np.sqrt(2)*np.pi) < 1e-10


def test_unmodified_published_baseline_hashes():
    check_baselines()


def test_complete_sem_protocol_and_same_dof_comparison():
    result, fields = sem_case(CONFIG['cases']['sem-poisson-2d'], Budget(30))
    assert result['passed'], result['checks']
    assert len(result['records']) == 12 and fields['sem'].shape == (17, 17)
    assert result['metrics']['same_dof_free_unknowns'] == 225


def test_radau_correction_endpoints():
    for p in [1, 2]:
        left, right = corrections(p, np.array([-1., 1.]))
        np.testing.assert_allclose(left, [1, 0], atol=2e-15)
        np.testing.assert_allclose(right, [0, 1], atol=2e-15)


def test_radau_derivatives_are_dg_liftings():
    for p in [1, 2]:
        op = Operator(4, p)
        np.testing.assert_allclose(op.w*op.gl, -op.left, atol=3e-14)
        np.testing.assert_allclose(op.w*op.gr, op.right, atol=3e-14)


def test_fr_constant_preservation_both_directions():
    for speed in [1., -1.]:
        op = Operator(4, 2, speed)
        np.testing.assert_allclose(op(np.full_like(op.x, 2.3)), 0, atol=2e-13)


def test_fr_weighted_mass_of_rhs_for_nonuniform_state():
    for speed in [1., -1.]:
        op = Operator(5, 2, speed); u = np.random.default_rng(37).normal(size=op.x.shape)
        assert abs(op.mass(op(u))) < 2e-13


def test_fr_semidiscrete_upwind_energy_identity():
    for speed in [1., -1.]:
        op = Operator(5, 2, speed); u = np.random.default_rng(41).normal(size=op.x.shape)
        jumps = np.roll(u@op.left, -1)-u@op.right
        derivative = np.sum(u*op(u)*op.w)/(2*op.n)
        np.testing.assert_allclose(derivative, -.5*abs(speed)*np.sum(jumps*jumps), atol=2e-12, rtol=2e-13)


def test_fr_negative_speed_transports():
    op = Operator(8, 2, -1); u, start, _ = evolve(op, .125, .15, Budget(10))
    assert op.error(u, .125) < .01 and np.max(np.abs(u-start)) > .5


def test_fr_matches_the_actual_published_modal_dg():
    for p in [1, 2]:
        op = Operator(8, p); u, _, _ = evolve(op, .125, .15, Budget(10))
        _, _, modes = dg_advection(8, p, .125, 1, .15, initial=lambda x: .4+np.sin(2*np.pi*x))
        np.testing.assert_allclose(u, modes@legvander(op.z, p).T, atol=2e-12, rtol=2e-12)


def test_fr_exponential_propagator_preserves_mass_and_composes():
    op = Operator(4, 2); u = op.project(); full = op.exponential(u, .1)
    np.testing.assert_allclose(full, op.exponential(op.exponential(u, .04), .06), atol=2e-13)
    assert abs(op.mass(full)-op.mass(u)) < 2e-14


def test_fr_error_norm_uses_interior_reconstruction():
    op = Operator(8, 2); u = op.project()
    a, b = op.error(u, 0, quadrature=7), op.error(u, 0, quadrature=11)
    assert a > 1e-5 and abs(a-b) < 1e-12


def test_complete_fr_protocol_and_time_error_separation():
    result, fields = fr_case(CONFIG['cases']['fr-periodic-advection'], Budget(30))
    assert result['passed'], result['checks']
    assert len(result['records']) == 6 and fields['fr'].shape == (32, 3)
    assert result['metrics']['time_error_halving_ratio'] < .3


def test_input_and_output_guardrails(tmp_path):
    bad = json.loads(json.dumps(CONFIG)); bad['cases']['fr-periodic-advection']['grids'] = [1000000]
    with pytest.raises(ValueError): validate(bad)
    (tmp_path/'keep.txt').write_text('keep')
    with pytest.raises(ValueError): run(ROOT/'inputs.json', tmp_path)
    assert (tmp_path/'keep.txt').read_text() == 'keep'


def test_exhausted_budget_stops_without_retry(monkeypatch):
    import experiments
    monkeypatch.setattr(experiments.time, 'monotonic', lambda: 10.)
    budget = Budget(1)
    monkeypatch.setattr(experiments.time, 'monotonic', lambda: 12.)
    with pytest.raises(RuntimeError, match='budget'): budget.check()
