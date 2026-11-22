"""Derivative identities and a shared, independently checked Bratu problem."""
import numpy as np
import pytest

from numart.autodiff import (BRATU_LAMBDA, Dual, bratu_matrix, bratu_residual,
    bratu_jacobian, bratu_reference, finite_difference_jacobian, jacobian, jvp)
from numart.krylov import newton


def test_dual_chain_product_quotient_and_slice_with_nontrivial_seed():
    x = np.array([.3, -.4, .7])
    v = np.array([2., -.5, -3.])
    # Hand differentiated scalar, including a repeated input and slicing.
    function = lambda u: np.exp(u[0]*u[1]) / (2+u[2]**2) + u[0]**3
    value, tangent = jvp(function, x, v)
    exponential = np.exp(x[0]*x[1])
    expected = (exponential*(v[0]*x[1]+x[0]*v[1])/(2+x[2]**2)
                - exponential*2*x[2]*v[2]/(2+x[2]**2)**2 + 3*x[0]**2*v[0])
    np.testing.assert_allclose(value, function(x), rtol=2e-15)
    np.testing.assert_allclose(tangent, expected, rtol=2e-15)
    np.testing.assert_array_equal((Dual([0., 2.], [7., 3.])**0).tangent, [0., 0.])


def test_dual_numpy_broadcasting_and_two_variable_matrix_product():
    a = np.array([[1., 2.], [3., 4.]])
    da = np.array([[.5, -1.], [2., .3]])
    b = np.array([.7, -.4])
    db = np.array([2., 1.])
    result = np.add(1., np.multiply(np.array([2., 3.]), Dual(a, da) @ Dual(b, db)))
    np.testing.assert_allclose(result.value, 1+np.array([2., 3.])*(a@b))
    np.testing.assert_allclose(result.tangent, np.array([2., 3.])*(da@b+a@db))
    np.testing.assert_allclose((2/Dual(b, db)).tangent, -2*db/b**2)


def test_unsupported_ad_and_invalid_inputs_fail_instead_of_losing_tangents():
    with pytest.raises(ValueError):
        Dual([1., 2.], [1.])
    with pytest.raises(TypeError):
        jvp(np.sin, [1.], [1.])
    with pytest.raises(TypeError):
        jvp(lambda u: np.array([2.]), [1.], [1.])
    with pytest.raises(TypeError):
        Dual(2., 1.) ** Dual(3., 0.)
    for step in (0., -1., np.inf, np.nan):
        with pytest.raises(ValueError):
            finite_difference_jacobian(lambda x: x*x, [1.], step)


@pytest.mark.parametrize('n', [1, 7, 31])
def test_bratu_shared_residual_matches_existing_stencil_and_derivatives(n):
    rng = np.random.default_rng(911+n)
    state = rng.uniform(-.1, .4, n)
    direction = rng.normal(size=n)
    padded = np.pad(state, 1)
    expected = -(padded[2:]-2*padded[1:-1]+padded[:-2])*(n+1)**2-BRATU_LAMBDA*np.exp(state)
    np.testing.assert_allclose(bratu_residual(state), expected, atol=2e-13)
    automatic = jacobian(bratu_residual, state)
    analytic = bratu_jacobian(state)
    np.testing.assert_allclose(automatic, analytic, rtol=3e-15, atol=2e-14)
    primal, product = jvp(bratu_residual, state, direction)
    np.testing.assert_array_equal(primal, bratu_residual(state))
    np.testing.assert_allclose(product, analytic@direction, rtol=3e-14, atol=2e-12)


def test_difference_sweep_exposes_truncation_and_small_step_roundoff():
    x, state = bratu_reference(31)
    state = state+.05*np.sin(3*np.pi*x)
    v = np.sin(2*np.pi*x)+.3*np.cos(5*np.pi*x)
    v /= np.linalg.norm(v)
    expected = bratu_jacobian(state)@v
    errors = []
    for step in (1., .5, .25, 1e-3, 1e-14):
        estimated = (bratu_residual(state+step*v)-bratu_residual(state-step*v))/(2*step)
        errors.append(np.linalg.norm(estimated-expected)/np.linalg.norm(expected))
    assert 3.5 < errors[0]/errors[1] < 4.5
    assert 3.5 < errors[1]/errors[2] < 4.5
    assert errors[3] < 1e-6
    assert errors[-1] > 1000*errors[3]
    np.testing.assert_allclose(finite_difference_jacobian(bratu_residual, state, 1e-4),
                               bratu_jacobian(state), rtol=2e-8, atol=3e-8)


def test_bratu_three_derivatives_reach_same_root_and_second_order_spatial_error():
    errors = []
    for n in (15, 31, 63):
        _, exact = bratu_reference(n)
        roots = []
        derivatives = (bratu_jacobian,
            lambda u: finite_difference_jacobian(bratu_residual, u, 1e-5),
            lambda u: jacobian(bratu_residual, u))
        for derivative in derivatives:
            result = newton(bratu_residual, derivative, np.zeros(n), tolerance=1e-10)
            assert result.converged, result.reason
            assert np.linalg.norm(bratu_residual(result.x)) <= 1e-10
            roots.append(result.x)
        for root in roots[1:]:
            np.testing.assert_allclose(root, roots[0], atol=2e-12, rtol=0)
        errors.append(np.max(abs(roots[0]-exact)))
    assert np.all((np.array(errors[:-1])/errors[1:]) > 3.8)
    assert np.all((np.array(errors[:-1])/errors[1:]) < 4.2)
