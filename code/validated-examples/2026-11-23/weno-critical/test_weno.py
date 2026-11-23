"""Small independent identities, cell-mean consistency and solver regressions."""
import json
from pathlib import Path
import shutil
import numpy as np
import pytest
from numpy.polynomial.legendre import leggauss
import run
import weno
from references import analytic


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
@pytest.mark.parametrize('epsilon', [1e-40, 1e-6, .01])
def test_constant_preservation(method, epsilon):
    trace, weights, beta, _ = weno.reconstruct(np.full(5, 2.5), method, epsilon)
    assert trace == 2.5
    np.testing.assert_array_equal(beta, [0., 0., 0.])
    np.testing.assert_allclose(weights, [.1, .6, .3], atol=1e-16, rtol=0)


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
@pytest.mark.parametrize('degree', [0, 1, 2])
def test_each_quadratic_candidate_from_gauss_cell_means(method, degree):
    h = .13;nodes, weights = leggauss(4)
    centers = np.arange(-2, 3)*h
    means = .5*np.sum(weights*(centers[:, None]+.5*h*nodes)**degree, axis=1)
    trace, _, _, candidates = weno.reconstruct(means, method, 1e-40)
    np.testing.assert_allclose(candidates, (h/2)**degree, rtol=0, atol=3e-15)
    assert abs(float(trace)-(h/2)**degree) < 3e-15


@pytest.mark.parametrize('degree', range(5))
def test_linear_optimal_combination_degree_four(degree):
    h = .17
    means = analytic.polynomial_means(np.arange(-2, 3)*h, h, [0]*degree+[1])
    _, _, _, candidates = weno.reconstruct(means, 'weno-js', 1e-6)
    assert abs(float(np.dot(weno.LINEAR, candidates))-(h/2)**degree) < 2e-15


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
def test_reference_mean_is_not_a_point_sample(method):
    n = 32
    means = analytic.periodic_means(n)
    points = analytic.periodic_value((np.arange(n)+.5)/n)
    assert np.max(abs(means-points)) > 1e-3
    np.testing.assert_allclose(means, analytic.quadrature_means(n), atol=2e-14, rtol=0)


@pytest.mark.parametrize('n,time', [(7, .137), (32, .5), (128, .75)])
def test_independent_reference_quadrature(n, time):
    np.testing.assert_allclose(analytic.periodic_means(n, time),
                               analytic.quadrature_means(n, time), atol=3e-14, rtol=0)


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
def test_positive_weights_and_shared_flux_conservation(method):
    q = np.array([.2, -.1, .5, .7, .1, -1., .9, .3])
    rhs, weights, beta = weno.periodic_rhs(q, 1/len(q), method, 1e-40)
    assert abs(rhs.sum()/len(q)) < 3e-15
    assert np.min(weights) >= 0 and np.min(beta) >= 0
    np.testing.assert_allclose(weights.sum(axis=1), 1, atol=3e-16, rtol=0)


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
def test_amplitude_scaling_requires_epsilon_scaling(method):
    q = np.array([.1, -.2, 0., .5, 1.1])
    trace, weights, _, _ = weno.reconstruct(q, method, 1e-6)
    scaled, scaled_weights, _, _ = weno.reconstruct(1e-3*q, method, 1e-12)
    np.testing.assert_allclose(scaled_weights, weights, atol=5e-16, rtol=0)
    assert abs(float(scaled)-1e-3*float(trace)) < 1e-18


@pytest.mark.parametrize('method', ['weno-js', 'weno-z'])
def test_transport_constant_and_requested_time(method):
    out = weno.transport(np.full(8, .5), method, 1e-40, .1, .1, [0, .05, .1], 100)
    np.testing.assert_array_equal(out['q_history'], np.full((3, 8), .5))
    assert out['time'] == .1 and out['steps'] > 0 and out['clip_count'] == out['retries'] == 0


def test_reference_transport_direction_and_nontrivial_shift():
    q = analytic.periodic_means(32, .25)
    np.testing.assert_allclose(q, np.roll(analytic.periodic_means(32), 8), atol=2e-15, rtol=0)
    assert np.mean(abs(q-analytic.periodic_means(32))) > .5


def test_second_critical_polynomial_has_first_two_zero_derivatives():
    coefficients = analytic.PROFILES['second-critical']
    assert coefficients[1] == coefficients[2] == 0 and coefficients[3] != 0


@pytest.mark.parametrize('epsilon', [0, -1, float('inf'), float('nan')])
def test_invalid_epsilon_rejected(epsilon):
    with pytest.raises(ValueError):weno.reconstruct(np.zeros(5), 'weno-js', epsilon)


def test_unknown_method_rejected():
    with pytest.raises(ValueError):weno.reconstruct(np.zeros(5), 'bogus', 1e-6)


def test_frozen_input_mutation_rejected(tmp_path):
    contract = json.loads((run.ROOT/'pre-run-contract.json').read_text())
    for name in [*contract['files_sha256'], 'pre-run-contract.json']:
        target = tmp_path/name;target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(run.ROOT/name, target)
    run.check_frozen_sources(tmp_path)
    (tmp_path/'inputs.json').write_text('{}\n')
    with pytest.raises(ValueError, match='inputs.json'):run.check_frozen_sources(tmp_path)
