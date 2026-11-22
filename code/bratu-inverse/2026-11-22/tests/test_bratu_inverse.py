"""Adjoint inverse fits checked against independent derivatives and data."""
from types import SimpleNamespace
import numpy as np
import pytest
import numart.bratu_inverse as inverse
from numart.autodiff import bratu_jacobian
from numart.bratu_sensitivity import solve_bratu, implicit_sensitivity, adjoint_gradient
from numart.bratu_inverse import (POSITIONS, TRUTH_LAMBDA, FIXED_NOISE,
    continuous_observations, observation_matrix, evaluate, fit_parameter,
    golden_reference)


def test_exact_node_observation_and_transpose_scatter_including_fixed_boundaries():
    h = observation_matrix(15, [0., .125, .375, .75, 1.])
    u = np.arange(15.)
    np.testing.assert_array_equal(h@u, [0., 1., 5., 11., 0.])
    q = h.T@np.array([2., 3., 5., 7., 11.])
    expected = np.zeros(15); expected[[1, 5, 11]] = [3., 5., 7.]
    np.testing.assert_array_equal(q, expected)


def test_continuous_truth_is_independent_exact_bratu_family():
    alpha = 1.5
    x = POSITIONS
    u = continuous_observations()
    np.testing.assert_allclose(TRUTH_LAMBDA*np.exp(u),
        2*alpha**2/np.cosh(alpha*(x-.5))**2, rtol=2e-15)
    np.testing.assert_array_equal(continuous_observations([0., 1.]), [0., 0.])


@pytest.mark.parametrize('lam', [.8, 1.8, 3.])
def test_off_optimum_adjoint_matches_resolved_parameter_difference(lam):
    data = continuous_observations()
    result = evaluate(31, lam, data)
    epsilon = 1e-5
    plus = evaluate(31, lam+epsilon, data, gradient=False)
    minus = evaluate(31, lam-epsilon, data, gradient=False)
    finite = (plus['objective']-minus['objective'])/(2*epsilon)
    assert abs(result['gradient']) > .02
    assert abs(finite-result['gradient']) < 2e-9
    assert result['primal_residual_l2'] <= 1e-10
    assert result['adjoint_residual_relative_l2'] < 1e-11


def test_nonuniform_weights_sparse_transpose_and_explicit_regularization():
    x = np.array([.125, .375, .75, .875])
    weights = np.array([.1, .25, .5, .9])
    data = continuous_observations(x)+np.array([.002, -.003, .001, -.002])
    lam, gamma, prior = 1.8, .03, 1.2
    result = evaluate(31, lam, data, x, weights, gamma, prior)
    matrix = bratu_jacobian(result['state'], lam)
    sensitivity = implicit_sensitivity(matrix, -np.exp(result['state']))
    expected_q = observation_matrix(31, x).T@(weights*result['misfit'])
    np.testing.assert_allclose(result['objective_state'], expected_q, atol=0, rtol=0)
    direct = np.sum(expected_q*sensitivity)+gamma*(lam-prior)
    assert abs(direct-result['gradient']) < 2e-15
    epsilon = 1e-5
    values = [evaluate(31, lam+sign*epsilon, data, x, weights, gamma, prior,
                      gradient=False)['objective'] for sign in (1, -1)]
    assert abs((values[0]-values[1])/(2*epsilon)-direct) < 2e-9
    assert result['explicit_gradient'] == gamma*(lam-prior)


def test_inherited_adjoint_helper_uses_transpose_for_nonsymmetric_system():
    matrix = np.array([[3., 2., -1.], [0., 4., .5], [1., -2., 5.]])
    parameter = np.array([-1., -2., .2])
    q = np.array([.4, -1.2, .7])
    gradient, adjoint = adjoint_gradient(matrix, parameter, q, .3)
    expected = q@np.linalg.solve(matrix, -parameter)+.3
    assert abs(gradient-expected) < 1e-15
    np.testing.assert_allclose(matrix.T@adjoint, q, atol=2e-15)
    assert abs((.3-np.linalg.solve(matrix, q)@parameter)-expected) > .1


@pytest.mark.parametrize('initial', [.5, 1.5, 3.2])
def test_same_discrete_data_multistart_self_consistency_and_armijo(initial):
    data = observation_matrix(31)@solve_bratu(31, TRUTH_LAMBDA).x
    fit = fit_parameter(31, data, initial)
    assert fit['converged'], fit['reason']
    assert abs(fit['lambda_value']-TRUTH_LAMBDA) < 3e-9
    assert fit['history'][-1]['projected_gradient'] <= 1e-10
    for current, following in zip(fit['history'], fit['history'][1:]):
        assert following['objective'] <= current['armijo_rhs']
        assert following['objective'] <= current['objective']
        expected = np.clip(current['lambda_value']-current['accepted_step']*current['gradient'], .2, 3.4)
        assert following['lambda_value'] == expected


def test_continuous_fixed_data_parameter_bias_refines_at_second_order():
    data = continuous_observations()
    errors = []
    for n in (15, 31, 63, 127):
        fit = fit_parameter(n, data, 1.5)
        assert fit['converged']
        errors.append(abs(fit['lambda_value']-TRUTH_LAMBDA))
    ratios = np.array(errors[:-1])/errors[1:]
    assert np.all((ratios > 3.9) & (ratios < 4.1))


def test_fixed_perturbations_shift_fit_and_match_objective_only_reference():
    data = continuous_observations()+FIXED_NOISE
    fit = fit_parameter(63, data, 1.5)
    reference = golden_reference(63, data)
    noiseless = fit_parameter(63, continuous_observations(), 1.5)
    assert fit['converged']
    assert abs(fit['lambda_value']-reference['lambda_value']) < 2e-8
    assert abs(fit['lambda_value']-noiseless['lambda_value']) > 2e-4
    assert fit['result']['data_rms'] > 5e-4
    assert reference['interval_width'] <= 1e-8


def test_golden_reference_is_objective_only(monkeypatch):
    original = inverse.evaluate
    calls = []
    def objective_only(*args, **kwargs):
        assert kwargs.get('gradient') is False
        calls.append(1)
        return original(*args, **kwargs)
    monkeypatch.setattr(inverse, 'evaluate', objective_only)
    result = golden_reference(15, continuous_observations())
    assert result['evaluations'] == len(calls)


def test_boundary_only_data_have_no_parameter_information():
    x, data = [0., 1.], [0., 0.]
    for lam in (.5, 3.):
        out = evaluate(15, lam, data, x)
        assert out['gradient'] == 0 and out['objective'] == 0
    with pytest.raises(ValueError, match='no information'):
        fit_parameter(15, data, 1.5, x)


def test_active_bound_stationarity_does_not_claim_truth_recovery():
    fit = fit_parameter(15, continuous_observations(alpha=2.), 1.5, bounds=(.2, 2.))
    assert fit['converged'] and fit['lambda_value'] == 2.
    assert abs(fit['result']['gradient']) > .01
    assert fit['history'][-1]['projected_gradient'] == 0


def test_iteration_limit_and_failed_forward_solve_are_explicit(monkeypatch):
    fit = fit_parameter(15, continuous_observations(), .5, maxiter=1)
    assert not fit['converged'] and fit['reason'] == 'optimization iteration limit'
    monkeypatch.setattr(inverse, 'solve_bratu', lambda *args:
        SimpleNamespace(x=np.zeros(15), converged=False, reason='test failure'))
    with pytest.raises(RuntimeError, match='test failure'):
        evaluate(15, 1., continuous_observations())


def test_armijo_failure_is_reported_instead_of_stationarity(monkeypatch):
    # A deliberately inconsistent gradient makes every attempted step ascend.
    # This controlled fault exercises failure reporting, not gradient accuracy.
    def inconsistent(n, lam, *args):
        return dict(objective=(lam-2.)**2, gradient=1., primal_residual_l2=0.,
            adjoint_residual_l2=0., adjoint_residual_relative_l2=0.)
    monkeypatch.setattr(inverse, 'evaluate', inconsistent)
    fit = fit_parameter(15, continuous_observations(), 1.5)
    assert not fit['converged'] and fit['reason'] == 'Armijo line search failed'
    assert fit['lambda_value'] == 1.5 and fit['evaluations'] == 51


@pytest.mark.parametrize('options', [dict(bounds=(3., 2.)), dict(bounds=(.2, 3.5)),
    dict(initial_step=float('nan')), dict(maxiter=1.5), dict(gradient_tolerance=0)])
def test_invalid_optimization_controls_are_rejected(options):
    with pytest.raises(ValueError):
        fit_parameter(15, continuous_observations(), 1.5, **options)


def test_invalid_observations_weights_and_primal_controls_are_rejected():
    with pytest.raises(ValueError): observation_matrix(15, [.1])
    with pytest.raises(ValueError): observation_matrix(15, [-.1])
    with pytest.raises(ValueError): evaluate(15, 1., [0.])
    with pytest.raises(ValueError): evaluate(15, 1., continuous_observations(), weights=[1]*4+[-1])
    with pytest.raises(ValueError): evaluate(15, 1., continuous_observations(), gamma=-1)
    with pytest.raises(ValueError): evaluate(15, 1., continuous_observations(), primal_tolerance=0)
