"""Independent references for implicit state derivatives and discrete adjoints."""
import numpy as np
import pytest
from numart.autodiff import bratu_jacobian, bratu_residual
from numart.bratu_sensitivity import (adjoint_gradient, bratu_derivatives,
    family_reference, implicit_sensitivity, objective, objective_partials, solve_bratu)


def test_nonsymmetric_multiple_parameters_detects_transpose_sign_and_explicit_term():
    # F=A*u-B*theta-c, u=A^-1(B*theta+c), L=w*u+.5*theta*R*theta.
    a = np.array([[3., 2., -1.], [0., 4., .5], [1., -2., 5.]])
    b = np.array([[1., -.3], [2., .4], [-.2, 1.3]])
    w = np.array([.4, -1.2, .7])
    theta = np.array([.2, -.6])
    r = np.array([[2., .3], [.3, 1.5]])
    sensitivity = implicit_sensitivity(a, -b)
    gradient, adjoint = adjoint_gradient(a, -b, w, r@theta)
    expected_s = np.linalg.solve(a, b)
    expected_g = w@expected_s+r@theta
    np.testing.assert_allclose(sensitivity, expected_s, rtol=1e-14)
    np.testing.assert_allclose(gradient, expected_g, rtol=1e-14)
    np.testing.assert_allclose(a.T@adjoint, w, atol=2e-15)
    wrong = w@np.linalg.solve(a.T, b)+r@theta
    assert np.linalg.norm(wrong-expected_g) > .1
    def reduced(t):
        state = np.linalg.solve(a, b@t+np.array([1., -.3, .2]))
        return w@state+.5*t@r@t
    finite = np.array([(reduced(theta+1e-5*e)-reduced(theta-1e-5*e))/2e-5
                       for e in np.eye(2)])
    np.testing.assert_allclose(finite, gradient, atol=2e-11)


def test_invalid_shapes_and_singular_systems_fail_explicitly():
    with pytest.raises(ValueError):
        implicit_sensitivity(np.ones((2, 3)), [1., 2.])
    with pytest.raises(ValueError):
        implicit_sensitivity(np.eye(2), [1.])
    with pytest.raises(ValueError):
        adjoint_gradient(np.eye(2), np.ones((2, 3)), [1., 2.], [1., 2.])
    with pytest.raises(ValueError):
        adjoint_gradient(np.eye(2), [1., 2.], [1.])
    with pytest.raises(np.linalg.LinAlgError):
        implicit_sensitivity(np.zeros((2, 2)), [1., 1.])


@pytest.mark.parametrize('alpha', [1., 2.])
def test_exact_continuous_family_sensitivity_uses_parameter_chain_rule(alpha):
    x, u, sensitivity, lam = family_reference(17, alpha)
    delta = 1e-5
    _, up, _, lp = family_reference(17, alpha+delta)
    _, um, _, lm = family_reference(17, alpha-delta)
    np.testing.assert_allclose((up-um)/(lp-lm), sensitivity, rtol=2e-9)
    np.testing.assert_allclose(lam*np.exp(u), 2*alpha**2/np.cosh(alpha*(x-.5))**2,
                               rtol=2e-15)


@pytest.mark.parametrize('alpha', [1., 2.])
def test_bratu_implicit_adjoint_and_continuous_spatial_refinement(alpha):
    errors = []
    for n in (15, 31, 63):
        _, _, reference, lam = family_reference(n, alpha)
        root = solve_bratu(n, lam)
        assert root.converged, root.reason
        assert np.linalg.norm(bratu_residual(root.x, lam)) <= 1e-10
        matrix, parameter = bratu_derivatives(root.x, lam)
        np.testing.assert_allclose(matrix, bratu_jacobian(root.x, lam), atol=1e-13)
        np.testing.assert_allclose(parameter, -np.exp(root.x), rtol=1e-15)
        sensitivity = implicit_sensitivity(matrix, parameter)
        lu, ll = objective_partials(root.x, lam)
        gradient, adjoint = adjoint_gradient(matrix, parameter, lu, ll)
        direct = np.sum(lu*sensitivity)+ll
        assert abs(gradient-direct) < 2e-14
        assert np.linalg.norm(np.einsum('ij,j->i', matrix, sensitivity)+parameter)/np.linalg.norm(parameter) < 2e-12
        assert np.linalg.norm(np.einsum('ji,j->i', matrix, adjoint)-lu)/np.linalg.norm(lu) < 2e-12
        assert abs(gradient-ll) > .01, 'State dependence must contribute'
        errors.append(np.max(abs(sensitivity-reference)))
    ratios = np.array(errors[:-1])/errors[1:]
    assert np.all((ratios > 3.5) & (ratios < 4.5))


@pytest.mark.parametrize('alpha', [1., 2.])
def test_reduced_objective_difference_resolves_again_and_matches_adjoint(alpha):
    n = 31
    _, _, _, lam = family_reference(n, alpha)
    root = solve_bratu(n, lam)
    matrix, parameter = bratu_derivatives(root.x, lam)
    gradient, _ = adjoint_gradient(matrix, parameter, *objective_partials(root.x, lam))
    delta = 1e-4
    plus, minus = solve_bratu(n, lam+delta), solve_bratu(n, lam-delta)
    assert plus.converged and minus.converged
    finite = (objective(plus.x, lam+delta)-objective(minus.x, lam-delta))/(2*delta)
    assert abs(finite-gradient) < 3e-6
    assert np.max(abs((plus.x-minus.x)/(2*delta)-implicit_sensitivity(matrix, parameter))) < 1e-5


def test_loose_primal_tolerance_can_bias_a_reduced_gradient_check():
    n = 31
    _, _, _, lam = family_reference(n, 2.)
    root = solve_bratu(n, lam)
    matrix, parameter = bratu_derivatives(root.x, lam)
    expected, _ = adjoint_gradient(matrix, parameter, *objective_partials(root.x, lam))
    errors = []
    for tol in (1e-2, 1e-10):
        plus, minus = solve_bratu(n, lam+1e-4, tol), solve_bratu(n, lam-1e-4, tol)
        assert plus.converged and minus.converged
        finite = (objective(plus.x, lam+1e-4)-objective(minus.x, lam-1e-4))/2e-4
        errors.append(abs(finite-expected))
    assert errors[0] > 20*errors[1]
