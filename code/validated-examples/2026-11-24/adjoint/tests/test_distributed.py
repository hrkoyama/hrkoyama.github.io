import json
from pathlib import Path
import numpy as np
import pytest
from operators import LocalHats, dot, tridiagonal_action, poisson_factor
from distributed import allocation_check, objective_q, adjoint_objectives, affine_control, nonsymmetric_control
from references.linear_oracle import dense_hats
from newton import state
import distributed

SETTINGS = json.loads((Path(__file__).parents[1]/'inputs.json').read_text())['solver']


def test_hat_partition_unity_scalar_golden():
    hats = LocalHats(7, 4)
    assert np.allclose(hats.forward(np.ones(4)), 1, atol=1e-15, rtol=0)
    assert np.all(hats.weight >= 0)


def test_m2_coefficient_offset():
    error, wrong = affine_control(7)
    assert error < 1e-13 and wrong > 1.9


def test_coefficient_endpoint_not_state_boundary():
    hats = LocalHats(7, 2); theta = np.array([1., 0.])
    coefficient_change = hats.forward(theta)
    assert coefficient_change[0] == .875 and coefficient_change[-1] == .125
    assert len(coefficient_change) == 7


def test_Bv_independent_explicit_loop():
    hats = LocalHats(7, 5); theta = np.arange(5.)**2
    actual = hats.forward(theta)
    expected = np.array([sum(max(0., 1-abs((i+1)/8-j/4)*4)*theta[j] for j in range(5)) for i in range(7)])
    assert np.array_equal(actual, expected)


def test_BT_repeated_scatter_golden():
    hats = LocalHats(7, 3); w = np.arange(1., 8.)
    expected = np.array([sum(max(0., 1-abs((i+1)/8-j/2)*2)*w[i] for i in range(7)) for j in range(3)])
    assert np.array_equal(hats.transpose(w), expected)
    theta = np.array([2., -1., 3.])
    assert dot(w, hats.forward(theta)) == dot(theta, hats.transpose(w))


def test_nonsymmetric_J_transpose_action():
    assert nonsymmetric_control()


def test_dense_reference_outside_primary_allocation():
    hats = LocalHats(7, 5)
    assert hats.index.shape == hats.weight.shape == (7, 2)
    dense = dense_hats(7, 5)
    assert dense.shape == (7, 5)
    assert np.allclose(hats.forward(np.arange(5.)), np.einsum('ij,j->i', dense, np.arange(5.), optimize=False), atol=1e-14)
    with pytest.raises(ValueError): allocation_check({'dense_B': dense}, 7, 5)


def test_objective_q_h_weights_and_midpoint():
    u = np.array([.2, .4, .2]); qs = objective_q(u)
    assert np.array_equal(qs[0], np.ones(3)/4)
    assert np.array_equal(qs[1], [0, 1, 0])
    assert np.array_equal(qs[2], u/4)


def test_one_vs_three_RHS_counters(tmp_path, monkeypatch):
    u = state(7, 2., 1e-11, SETTINGS)['u']; hats = LocalHats(7, 5)
    factor = poisson_factor(7); qs = objective_q(u)
    one, oc, count1 = adjoint_objectives(u, 2., hats, qs[:1], SETTINGS, None, factor)
    three, tc, count3 = adjoint_objectives(u, 2., hats, qs, SETTINGS, None, factor)
    assert (count1, count3) == (1, 3)
    assert np.array_equal(one[0], three[0])
    assert all(c['counts']['factor_builds'] == 0 for c in oc+tc)
    assert sum(c['counts']['preconditioner'] for c in tc) > 0
    original, calls = distributed.derivative, [0]
    def broken(*args, **kwargs):
        calls[0] += 1
        if calls[0] == 2: raise ArithmeticError('next RHS failure')
        return original(*args, **kwargs)
    monkeypatch.setattr(distributed, 'derivative', broken)
    with pytest.raises(ArithmeticError):
        adjoint_objectives(u, 2., hats, qs, SETTINGS, tmp_path/'active.npz', factor)
    saved = np.load(tmp_path/'active-completed-RHS.npz')
    assert 'gradient_0' in saved and 'adjoint_0' in saved and 'history_0' in saved


def test_parameter_Jacobian_allocation_negative_control():
    for shape in [(7, 5), (5, 7)]:
        with pytest.raises(ValueError): allocation_check({'hidden': np.zeros(shape)}, 7, 5)
    assert allocation_check({'local': np.zeros((7, 2)), 'Krylov': np.zeros((7, 25))}, 7, 5)
