"""Algorithmic identities, independent equilibrium references and scoped runs."""
import json
import math
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
from scipy.linalg import solve_discrete_lyapunov
from thermostats import (RUNNERS, canonical_reference, canonical_positions,
                         coordinate_energy, csvr_bath, csvr_rescale, force,
                         harmonic_langevin_reference, kinetic, md_step,
                         turning_point, verlet_step)
from run import run

HERE = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def fixed_results():
    config = json.loads((HERE/'inputs.json').read_text())['cases']
    return {name: runner(config[name]) for name, runner in RUNNERS.items()}


@pytest.mark.parametrize('name', list(RUNNERS))
def test_fixed_inputs_pass_all_separate_acceptance_checks(name, fixed_results):
    case = fixed_results[name]
    assert case['passed'] and len(case['checks']) >= 7
    assert all(value is True for value in case['checks'].values())
    assert case['records'] and all(math.isfinite(x) for x in case['metrics'].values())


@pytest.mark.parametrize('momentum', [-2.0, -0.01, 0.01, 2.0])
def test_scalar_signed_csvr_is_pathwise_ou_with_physical_noise_sign(momentum):
    # R is a radial-coordinate Gaussian, so physical OU noise is sign(p)*R.
    h, tau, temperature, mass, radial_noise = 0.7, 0.4, 1.3, 2.1, -3.0
    actual = csvr_rescale([momentum], h, tau, temperature, radial_noise, 0., mass)[0]
    expected = (math.exp(-h/(2*tau))*momentum+
                math.copysign(1., momentum)*math.sqrt(mass*temperature*(-math.expm1(-h/tau)))*radial_noise)
    assert actual == pytest.approx(expected, rel=2e-14, abs=2e-14)


def test_same_gaussian_controls_alpha_magnitude_and_sign():
    original = np.array([1., 2.])
    actual = csvr_rescale(original, 1., .25, 1., -4., 0.2)
    assert np.dot(original, actual) < 0, 'A negative radial draw must permit global flips'
    np.testing.assert_allclose(actual/actual[0], original/original[0], atol=1e-14)


def test_kinetic_transition_matches_completed_square_with_nonunit_masses():
    p = np.array([[.4, -.7, .2], [1., -.3, .8]])
    masses = np.array([2., .5, 1.2]);normal = np.array([-.4, 1.3]);chi = np.array([2.7, .8])
    h, tau, temperature = .3, .9, 1.7
    actual = csvr_rescale(p, h, tau, temperature, normal, chi, masses)
    initial = .5*np.sum(p*p/masses, axis=-1);final = .5*np.sum(actual*actual/masses, axis=-1)
    c = math.exp(-h/tau);a = temperature*(1-c)/2
    expected = (np.sqrt(c*initial)+math.sqrt(a)*normal)**2+a*chi
    np.testing.assert_allclose(final, expected, rtol=3e-14)


def test_exact_cold_global_momentum_is_rejected_without_inventing_direction():
    with pytest.raises(ValueError, match='Zero kinetic'):
        csvr_rescale(np.zeros((3, 2)), .1, 1., 1., np.zeros(3), np.ones(3))


def test_tiny_nonzero_momentum_avoids_kinetic_ratio_overflow():
    result = csvr_rescale(np.array([[1e-300, -2e-300]]), .1, 1., 1., [0.3], [1.2])
    assert np.all(np.isfinite(result)) and np.linalg.norm(result) > 0
    np.testing.assert_allclose(result[0, 1]/result[0, 0], -2., rtol=1e-14)


def test_zero_duration_is_an_identity_even_for_zero_momentum():
    original = np.zeros((2, 3))
    np.testing.assert_array_equal(csvr_rescale(original, 0., 1., 1., [0., 0.], [0., 0.]), original)


@pytest.mark.parametrize('bad', [
    {'step': -.1}, {'step': True}, {'tau': 0.}, {'temperature': float('nan')},
    {'temperature': -1.}, {'masses': [-1., 1.]}, {'normal': float('inf')}, {'chi_square': -1.}
])
def test_invalid_bath_parameters_have_explicit_failure(bad):
    kwargs = {'momentum': np.array([.2, .4]), 'step': .1, 'tau': 1., 'temperature': 1.,
              'normal': .5, 'chi_square': 1., 'masses': 1.}
    kwargs.update(bad)
    with pytest.raises(ValueError):
        csvr_rescale(**kwargs)


def test_single_degree_of_freedom_rejects_spurious_chi_square_noise():
    with pytest.raises(ValueError, match='Nf=1'):
        csvr_rescale([1.], .1, 1., 1., .5, .01)


def test_verlet_matrix_preserves_its_harmonic_shadow_quadratic_form():
    h = .3;frequencies = np.array([1., 1.7])
    q = np.array([[.7, -.3], [.9, .1]]);p = np.array([[.2, .8], [-.2, .5]])
    before = .5*np.sum(p*p+frequencies**2*(1-h*h*frequencies**2/4)*q*q, axis=-1)
    q1, p1 = verlet_step(q, p, h, frequencies, 0.)
    after = .5*np.sum(p1*p1+frequencies**2*(1-h*h*frequencies**2/4)*q1*q1, axis=-1)
    np.testing.assert_allclose(after, before, rtol=2e-14, atol=2e-14)


@pytest.mark.parametrize('tau', [.25, 1., 3.])
def test_obabo_lyapunov_covariance_matches_independently_derived_shadow_density(tau):
    h, temperature = .2, 1.3;frequencies = [1., 1.7]
    numerical = harmonic_langevin_reference(h, tau, frequencies, temperature, 0.)['covariance']
    expected = [np.diag([temperature/(w*w*(1-h*h*w*w/4)), temperature]) for w in frequencies]
    np.testing.assert_allclose(numerical, expected, rtol=2e-13, atol=2e-13)


def test_global_bath_cannot_escape_a_separable_unexcited_coordinate_axis():
    q, p = np.array([[1., 0.]]), np.array([[.3, 0.]])
    rng = np.random.default_rng(94)
    for _ in range(80):
        q, p = md_step(q, p, .05, [1., 1.7], .2, .5, 1., rng, 'csvr')
    assert q[0, 1] == p[0, 1] == 0., 'Global scaling is not a universal ergodicity guarantee'
    local_q, local_p = md_step(q, p, .05, [1., 1.7], .2, .5, 1., np.random.default_rng(94), 'langevin')
    assert abs(local_q[0, 1])+abs(local_p[0, 1]) > 0


def test_quartic_force_is_the_negative_energy_gradient():
    q = np.array([[.2, -.6]]);omega = np.array([1., 1.7]);lam = .2
    h = 1e-5
    from thermostats import potential
    for axis in range(2):
        shift = np.zeros_like(q);shift[0, axis] = h
        derivative = (potential(q+shift, omega, lam)-potential(q-shift, omega, lam))/(2*h)
        assert derivative[0] == pytest.approx(-force(q, omega, lam)[0, axis], rel=2e-9)


@pytest.mark.parametrize('quartic', [0., .2])
def test_turning_point_inverts_the_potential_stably(quartic):
    for omega in [1., 1.7]:
        for energy in [1e-10, .5, 4.]:
            q = turning_point(energy, omega, quartic)
            assert coordinate_energy(q, omega, quartic) == pytest.approx(energy, rel=5e-15)


def test_boltzmann_quadrature_recovers_exact_harmonic_canonical_moments():
    ref = canonical_reference([1., 1.7], 0., 1.3, [-1., 0., 1.], [.5, 2., 5.], 1e-11)
    np.testing.assert_allclose(ref['q_variance'], [1.3, 1.3/1.7**2], atol=2e-13)
    for name in ['k', 'u']:
        assert ref[name+'_mean'] == pytest.approx(1.3, abs=2e-13)
        assert ref[name+'_variance'] == pytest.approx(1.3**2, abs=2e-13)
    assert ref['h_mean'] == pytest.approx(2.6, abs=2e-13)
    assert ref['h_variance'] == pytest.approx(2*1.3**2, abs=2e-13)


def test_quartic_full_energy_cdf_is_monotone_and_not_a_harmonic_gamma_claim(fixed_results):
    ref = fixed_results['csvr-langevin-quartic']['canonical_reference']
    assert np.all(np.diff(ref['energy_cdf']) > 0)
    assert ref['u_mean'] < ref['k_mean']
    assert 'maximum_langevin_acf_absolute_error' not in fixed_results['csvr-langevin-quartic']['metrics']


def test_comparison_records_keep_ensembles_tau_dt_methods_and_uncertainty_separate(fixed_results):
    for name in ['csvr-langevin-harmonic', 'csvr-langevin-quartic']:
        rows = fixed_results[name]['records']
        distributions = [row for row in rows if row['series'] == 'distribution']
        assert len(distributions) == 16
        assert {row['method'] for row in distributions} == {'csvr', 'langevin'}
        assert {row['initial_ensemble'] for row in distributions} == {'canonical', 'heated'}
        correlations = [row for row in rows if row['series'] == 'correlation']
        assert len(correlations) == 40
        assert all('h_acf_standard_error' in row and 'k_acf_standard_error' in row for row in correlations)
        assert not any('exact_acf' in row for row in correlations), 'exp(-lag/tau) is only a bath-only identity'


def test_fixed_seed_reproduces_the_exact_stochastic_kernel_and_changes_with_seed():
    p = np.array([[.2, -.4], [.7, .1]])
    first = csvr_bath(p, .2, .5, 1., np.random.default_rng(77))
    second = csvr_bath(p, .2, .5, 1., np.random.default_rng(77))
    different = csvr_bath(p, .2, .5, 1., np.random.default_rng(78))
    np.testing.assert_array_equal(first, second)
    assert not np.array_equal(first, different)


def test_runner_preserves_input_hash_and_refuses_overwrite(tmp_path):
    result = run(HERE/'inputs.json', tmp_path/'results', 'csvr-kinetic-kernel')
    assert result['passed'] and result['termination'] == 'fixed_budget_completed'
    assert (tmp_path/'results/csvr-kinetic-kernel.csv').is_file()
    with pytest.raises(ValueError, match='new or empty'):
        run(HERE/'inputs.json', tmp_path/'results')


def test_runner_rejects_missing_case_and_nonfinite_json(tmp_path):
    source = json.loads((HERE/'inputs.json').read_text());del source['cases']['csvr-langevin-quartic']
    path = tmp_path/'missing.json';path.write_text(json.dumps(source))
    with pytest.raises(ValueError, match='complete'):
        run(path, tmp_path/'out')
    path.write_text('{"schema_version":1,"number":NaN}')
    with pytest.raises(ValueError, match='Nonfinite'):
        run(path, tmp_path/'out2')


def test_quartic_energy_quadrature_matches_independent_rejection_ensemble():
    from thermostats import potential
    rng = np.random.default_rng(2026112299)
    ref = canonical_reference([1., 1.7], .2, 1., [-1., 0., 1.], [.5, 1., 2., 4., 6.], 1e-11)
    q = canonical_positions(rng, 32768, [1., 1.7], .2, 1.)
    p = rng.normal(size=q.shape)
    h = kinetic(p)+potential(q, [1., 1.7], .2)
    empirical = np.mean(h[:, None] <= np.array([.5, 1., 2., 4., 6.]), axis=0)
    assert np.max(abs(empirical-ref['energy_cdf'])) < .015
    assert abs(h.mean()-ref['h_mean']) < .04


@pytest.mark.parametrize('case,field,value', [
    ('csvr-kinetic-kernel', 'replicas', 10**10),
    ('csvr-kinetic-kernel', 'step', 1e-8),
    ('csvr-langevin-harmonic', 'steps', [1e-8, 5e-9]),
    ('csvr-langevin-quartic', 'canonical_replicas', 10**10),
    ('csvr-langevin-harmonic', 'quartic', .2),
    ('csvr-langevin-quartic', 'quartic', 0.),
])
def test_invalid_or_excessive_work_is_rejected_before_state_allocation(case, field, value, monkeypatch):
    from thermostats import validate_config
    config = json.loads((HERE/'inputs.json').read_text())['cases'][case]
    config[field] = value
    kind = 'kernel' if case == 'csvr-kinetic-kernel' else ('harmonic' if case.endswith('harmonic') else 'quartic')
    monkeypatch.setattr(np, 'zeros', lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError('allocation must not start')))
    with pytest.raises(ValueError):
        validate_config(config, kind)
