import json
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import pytest
from references.shooting_decimal import fold, shoot
from references.linear_oracle import bratu, solve
from operators import jac_action, dot, norm, poisson_factor, laplace, hnorm
from krylov import gmres
from newton import state, derivative
import newton
import fold_study

SETTINGS = json.loads((Path(__file__).parents[1]/'inputs.json').read_text())['solver']


def test_shooting_discrete_n1_analytic_fold():
    out = fold(1, 50)
    with localcontext() as c:
        c.prec = 60
        assert abs(out['a']-1) < D('1e-35')
        assert abs(out['lambda']-8/D(1).exp()) < D('1e-35')


def test_shooting_a_lambda_derivatives():
    with localcontext() as c:
        c.prec = 80
        a, lam, h = D('.3'), D('2.2'), D('1e-15')
        value = shoot(3, a, lam)
        plus, minus = shoot(3, a+h, lam), shoot(3, a-h, lam)
        lp, lm = shoot(3, a, lam+h), shoot(3, a, lam-h)
        assert abs((plus['u'][-1]-minus['u'][-1])/(2*h)-value['z'][-1]) < D('1e-25')
        assert abs((lp['u'][-1]-lm['u'][-1])/(2*h)-value['w'][-1]) < D('1e-25')
        assert abs((lp['z'][-1]-lm['z'][-1])/(2*h)-value['t'][-1]) < D('1e-25')


def test_fold_anchor_is_not_continuum_fold():
    out = fold(1, 50)
    assert abs(float(out['lambda'])-3.513830719) > .1
    assert abs(float(out['profile'][-1])) < 1e-35


def test_same_state_tangent_adjoint_sign():
    u, lam = np.array([.2, .3, .2]), 2.
    d, l, r = bratu(u, lam); b, q = np.exp(u), u/4
    s, p = solve(d, l, r, b), solve(d, l, r, q, True)
    assert abs(dot(q, s)-dot(p, b)) < 1e-14
    assert dot(p, b) > 0 and norm(jac_action(u, lam, s)-b) < 1e-13
    # Integration regression from the frozen failed state: exact rational
    # Laplacian at this saved vector, not a new solver or selected iterate.
    saved = np.load(Path(__file__).parents[1]/'history/main-attempt01/failed-state.npz')
    v = saved['last_linear_candidate']; exact = [F.from_float(float(x)) for x in v]
    reference = [(len(v)+1)**2*(2*x-(exact[i-1] if i else 0)-(exact[i+1] if i+1 < len(v) else 0)) for i, x in enumerate(exact)]
    actual = jac_action(saved['u'], np.zeros(len(v)), v)
    assert all(F.from_float(float(a)) == b for a, b in zip(actual, reference))


def test_finite_reference_residual_correction_identity():
    u, lam = np.array([.2, .3, .2]), 2.
    d, l, r = bratu(u, lam); b, q = np.exp(u), u/4
    sd, pd = solve(d, l, r, b)+np.array([1e-4, 0, 0]), solve(d, l, r, q)+np.array([0, 2e-4, 0])
    out = fold_study.identity(u, lam, b, q, sd, pd, sd+.01, pd-.02)
    assert max(out['tangent_defect'], out['adjoint_defect'], out['approximate_cross_defect']) < 1e-14
    assert out['direct_tangent_residual'] > 1e-5 and out['direct_adjoint_residual'] > 1e-5


def test_approximate_adjoint_cross_term_needed():
    u, lam = np.array([.2, .3, .2]), 2.
    d, l, r = bratu(u, lam); b, q = np.exp(u), u/4
    sd, pd = solve(d, l, r, b), solve(d, l, r, q)
    out = fold_study.identity(u, lam, b, q, sd, pd, sd+.01, pd-.02)
    assert abs(out['approximate_adjoint_cross_term']) > 1e-5
    assert out['approximate_cross_defect'] < 1e-14


def test_GMRES_callable_identity_alias_regression():
    b = np.array([1., -2., .3]); original = b.copy()
    out = gmres(lambda v: v, b, lambda v: v, 3, 4, 1e-12)
    assert out['passed'] and np.allclose(out['x'], b, atol=1e-14, rtol=0)
    assert np.array_equal(b, original)


def test_GMRES_true_residual_and_iteration_cap():
    diagonal = np.array([1., 2., 4.]); rhs = np.ones(3)
    out = gmres(lambda v: diagonal*v, rhs, lambda v: v.copy(), 1, 1, 1e-14)
    assert out['iterations'] == 1 and not out['passed']
    assert abs(norm(rhs-diagonal*out['x'])-out['residuals'][-1]) < 1e-14
    settings = {**SETTINGS, 'gmres': {**SETTINGS['gmres'], 'restart': 1, 'max_iterations': 1}}
    item = derivative(np.array([.2, .3, .2]), 2., rhs, 1e-30, settings)
    assert not item['target_met'] and not item['raw_solver_passed']
    assert item['termination_reason'] == 'maximum_iterations'
    assert item['finite_candidate'] and item['cause_proven'] is False


def test_Poisson_preconditioner_boundary_control():
    factor = poisson_factor(7); rhs = np.arange(1., 8.)
    x = factor.solve(rhs)
    assert norm(laplace(x)-rhs) < 1e-12
    assert len(x) == 7


def test_nonlinear_trial_candidate_retained(tmp_path, monkeypatch):
    original, calls = newton.residual, [0]
    def broken(u, a):
        calls[0] += 1
        if calls[0] == 2: raise ArithmeticError('trial diagnostic injected')
        return original(u, a)
    monkeypatch.setattr(newton, 'residual', broken)
    path = tmp_path/'partial.npz'
    with pytest.raises(ArithmeticError): state(7, 2., 1e-11, SETTINGS, path)
    out = np.load(path)
    assert 'trial' in out and 'last_linear_candidate' in out and np.isfinite(out['trial']).all()
    assert 'last_linear_rhs' in out and 'last_linear_requested_target' in out
    assert bool(out['last_linear_raw_passed'])


def test_loose_strict_state_errors_separated():
    loose, strict = state(7, 2., 1e-5, SETTINGS), state(7, 2., 1e-11, SETTINGS)
    assert loose['residual'] <= 1e-5 and strict['residual'] <= 1e-11
    assert strict['residual'] <= loose['residual']
    assert not np.shares_memory(loose['u'], strict['u'])


def test_FD_steps_saved_without_best_selection(tmp_path, monkeypatch):
    cfg = {'state_tolerances': [1e-8, 1e-11], 'linear_rtol': [1e-4, 1e-8, 1e-12],
           'FD_steps': [1e-4, 1e-5, 1e-6], 'FD_state_tolerance': 1e-11}
    out = fold_study.record(3, 2., SETTINGS, cfg, tmp_path/'partial.npz', tmp_path/'raw.npz')
    assert [r['step'] for r in out['FD']] == cfg['FD_steps']
    assert len(out['FD_states']) == 6
    saved = np.load(tmp_path/'raw.npz')
    assert all(f'FD_{i}_{side}' in saved for i in range(3) for side in ['minus', 'plus'])
    def broken(*_args): raise ArithmeticError('condition diagnostic fails after direct candidates')
    monkeypatch.setattr(fold_study, 'smallest', broken)
    with pytest.raises(ArithmeticError):
        fold_study.record(3, 2., SETTINGS, cfg, tmp_path/'p2.npz', tmp_path/'r2.npz')
    retained = np.load(tmp_path/'r2.npz')
    assert 'direct_tangent' in retained and 'direct_adjoint' in retained
