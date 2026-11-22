"""Independent identities, adverse controls and fixed-scope kinetic checks."""
import json
from math import pi
from pathlib import Path

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.special import betaln, expn
from scipy.stats import binomtest

import kinetic_experiments as experiments
from kinetic_experiments import dsmc_case, pic_case, radiation_case
from kinetics import (absorption_slab, cic_state, elastic_round, microcanonical_energy_cdf,
                      microcanonical_fourth, microcanonical_sample, photon_survival,
                      plasma_dop853, plasma_verlet, slab_references)


@pytest.fixture(scope='module')
def config():
    return json.loads(Path(__file__).with_name('inputs.json').read_text())


@pytest.fixture(scope='module')
def cases(config):
    return [pic_case(config['pic']), dsmc_case(config['dsmc']), radiation_case(config['radiation'])]


def test_all_preregistered_kinetic_checks_are_literal_booleans_and_metrics_finite(cases):
    assert {case['id'] for case in cases} == {'pic-conservation', 'dsmc-statistics', 'radiation-convergence'}
    for case in cases:
        assert case['passed'] is True and case['checks'] and case['records'] and case['metrics']
        assert all(type(value) is bool and value for value in case['checks'].values())
        assert all(np.isfinite(value) for value in case['metrics'].values())
        # Ensure all optional CSV cells can be empty, with no NaN sentinel.
        json.dumps(case, allow_nan=False)


def test_cic_manufactured_integer_loading_gives_analytic_poisson_mode():
    grid = 8
    coordinates = np.arange(grid)*2*pi/grid
    counts = np.array([3, 2, 1, 2, 3, 2, 1, 2])
    position = np.repeat(coordinates, counts)
    acceleration, diagnostics = cic_state(position, grid)
    # rho=-cos(2x)/2, E=-sin(2x)/4, electron acceleration=sin(2x)/4.
    expected = .25*np.sin(2*position)
    assert np.max(abs(acceleration-expected)) < 2e-15
    assert diagnostics['charge_error'] < 1e-14
    assert diagnostics['resolved_gauss_error'] < 1e-14


def test_nyquist_null_charge_is_reported_separately_instead_of_false_full_gauss_claim():
    position = np.repeat(np.arange(8)*2*pi/8, [3, 1]*4)
    acceleration, diagnostics = cic_state(position, 8)
    assert np.max(abs(acceleration)) < 1e-14
    assert diagnostics['resolved_gauss_error'] < 1e-14
    assert abs(diagnostics['nyquist_charge']-.5) < 1e-14


def test_cic_momentum_and_self_force_are_skew_operator_identities():
    position = np.random.default_rng(702).uniform(0., 2*pi, 48)
    acceleration, _ = cic_state(position, 32)
    assert abs(acceleration.sum()) < 1e-13
    # Coincident equal charges still have zero net force, not a force lookup.
    same, _ = cic_state(np.array([.271, .271]), 32)
    assert np.max(abs(same)) < 1e-13


def test_grid_noise_expectation_follows_cell_integral_not_continuum_assignment_assumption():
    theta = 2*pi/32
    integral = quad(lambda f: abs((1-f)+f*np.exp(-1j*theta))**2, 0., 1., epsabs=1e-13)[0]
    assert abs(integral-(2+np.cos(theta))/3) < 2e-15
    assert integral < 1  # Unassigned particle Fourier power has expectation 1/N.


def test_pic_refinement_fixes_particle_count_and_separates_random_loading(cases, config):
    records = cases[0]['records']
    mesh = [r for r in records if r['series'] == 'mesh']
    time = [r for r in records if r['series'] == 'time']
    assert {r['particles'] for r in mesh} == {config['pic']['mesh_particles']}
    assert len({r['particles_per_cell'] for r in mesh}) == len(mesh)
    assert len({r['dt'] for r in mesh}) == 1
    assert len({r['grid'] for r in time}) == len({r['particles'] for r in time}) == 1
    assert len([r for r in records if r['series'] == 'shot-seed']) == 3*64


def test_pic_energy_is_measured_and_not_falsely_claimed_exact(cases):
    drift = cases[0]['metrics']['relative_energy_drift']
    assert 1e-5 < drift < .05
    assert cases[0]['metrics']['momentum_error'] < 1e-12


def test_pic_energy_failure_control_rejects_deliberately_corrupted_diagnostic(config, monkeypatch):
    original = experiments.plasma_verlet
    def bad_energy(*args, **kwargs):
        result = original(*args, **kwargs)
        result['relative_energy_drift'] = .2
        return result
    monkeypatch.setattr(experiments, 'plasma_verlet', bad_energy)
    result = pic_case(config['pic'])
    assert result['passed'] is False
    assert result['checks']['measured_energy_drift'] is False
    assert result['checks']['mesh_convergence'] is True


def test_dop853_and_verlet_reference_have_independent_temporal_orders():
    reference = plasma_dop853(16, 64, .8, .001, 1e-11, 1e-13, .05)
    coarse = plasma_verlet(16, 64, .2, .8, .001)
    fine = plasma_verlet(16, 64, .05, .8, .001)
    coarse_error = abs(coarse['records'][-1]['mode']-reference['mode'])
    fine_error = abs(fine['records'][-1]['mode']-reference['mode'])
    assert coarse_error/fine_error > 15.


@pytest.mark.parametrize('bad', [np.array([np.nan, 0.]), np.ones((4, 2)), np.array([0.])])
def test_cic_rejects_nonfinite_or_wrong_shape_particle_inputs(bad):
    with pytest.raises(ValueError):
        cic_state(bad, 16)


@pytest.mark.parametrize('kwargs', [dict(dt=0.), dict(dt=np.nan), dict(end_time=9.),
                                   dict(amplitude=.1), dict(particles=2), dict(grid=True)])
def test_pic_rejects_invalid_or_excessive_runs(kwargs):
    arguments = dict(grid=16, particles=64, dt=.1, end_time=.8, amplitude=.001)
    arguments.update(kwargs)
    with pytest.raises(ValueError):
        plasma_verlet(**arguments)


def test_each_elastic_round_conserves_general_nonzero_center_of_mass():
    rng = np.random.default_rng(188)
    velocity = rng.normal(size=(32, 3))+[1., -2., .5]
    momentum, energy = velocity.sum(axis=0), np.sum(velocity*velocity)
    for _ in range(20):
        elastic_round(velocity, rng)
        assert np.max(abs(velocity.sum(axis=0)-momentum)) < 1e-12
        assert abs(np.sum(velocity*velocity)-energy) < 2e-12


@pytest.mark.parametrize('bad', [np.ones((5, 3)), np.ones((8, 2)), np.ones((8, 3), int),
                               np.full((8, 3), np.nan)])
def test_collision_round_rejects_bad_particle_arrays(bad):
    with pytest.raises(ValueError):
        elastic_round(bad, np.random.default_rng(1))


def test_independent_equilibrium_sampler_enforces_both_constraints():
    velocity = microcanonical_sample(64, np.random.default_rng(900))
    assert np.max(abs(velocity.sum(axis=0))) < 1e-13
    assert abs(np.sum(velocity*velocity)-192) < 1e-12


def test_finite_n_energy_cdf_matches_independent_radial_density_quadrature():
    n = 16
    upper = 1.5*(n-1)
    b = 1.5*(n-2)
    for energy in [.25, 1.5, 3.]:
        probability = quad(lambda u: np.exp(.5*np.log(u)+(b-1)*np.log1p(-u)-betaln(1.5, b)),
                           0., energy/upper, epsabs=1e-12, epsrel=1e-12)[0]
        assert abs(float(microcanonical_energy_cdf(energy, n))-probability) < 5e-13
    assert float(microcanonical_energy_cdf(-1., n)) == 0.
    assert float(microcanonical_energy_cdf(upper+1, n)) == 1.


def test_finite_n_fourth_is_zero_momentum_sphere_not_maxwell():
    n = 16
    dimension = 3*(n-1)
    # Uniform sphere coordinate fourth moment: 3R^4/[D(D+2)].
    radius_squared = 3*n
    projection_norm_squared = (n-1)/n
    sphere_fourth = 3*radius_squared**2*projection_norm_squared**2/(dimension*(dimension+2))
    assert abs(microcanonical_fourth(n)-sphere_fourth) < 1e-14
    assert 3-microcanonical_fourth(n) > .1


def test_dsmc_uncertainty_uses_independent_replicates_and_rounds_have_no_time(cases):
    cdf = [r for r in cases[1]['records'] if r['series'] == 'cdf']
    histories = [r for r in cases[1]['records'] if r['series'] == 'anisotropy']
    assert all(r['seeds'] == 64 and r['standard_error'] > 0 for r in cdf)
    assert all('round' in r and 'time' not in r for r in histories)
    assert cases[1]['metrics']['cdf_seed_standard_error_reduction'] > 1.2


def test_unequilibrated_two_beam_failure_control_is_not_microcanonical_equilibrium():
    expected = float(microcanonical_energy_cdf(.75, 16))
    # Initial beams have every kinetic energy equal to 1.5; CDF(.75)=0.
    assert expected > .2
    assert abs(9-microcanonical_fourth(16)) > 6.


@pytest.mark.parametrize('particles', [True, 3, 9000])
def test_finite_n_reference_rejects_invalid_counts(particles):
    with pytest.raises(ValueError):
        microcanonical_energy_cdf(1., particles)


def test_radiation_slab_energy_integral_and_references_are_independent():
    depth = .7
    reference = slab_references(depth)
    # Integrate the characteristic absorption source through optical depth first.
    absorbed = 2*pi*quad(lambda mu: mu*(-np.expm1(-depth/mu)), 0., 1., epsabs=1e-12)[0]
    assert abs(pi-reference['quad_flux']-absorbed) < 2e-11
    assert abs(reference['quad_flux']-2*pi*expn(3, depth)) < 1e-12


def test_radiation_characteristics_remove_space_error_but_not_angular_error():
    shallow = absorption_slab(4, 4, .1, 'characteristic')
    reference = slab_references(.1)
    assert shallow['spatial_flux_error'] < 1e-14
    assert abs(shallow['flux']-reference['quad_flux']) > 1e-5
    upstream = absorption_slab(16, 16, .7)
    assert upstream['flux'] > upstream['characteristic_flux']
    assert upstream['balance_error'] < 1e-12
    assert 0 <= upstream['minimum_intensity'] <= upstream['maximum_intensity'] <= 1


def test_wrong_uniform_angle_photon_measure_failure_control_is_detectable():
    # Uniform mu samples intensity, whereas incoming flux samples 2mu.
    depth = .7
    wrong_survival = quad(lambda mu: np.exp(-depth/mu), 0., 1.)[0]
    flux_survival = 2*expn(3, depth)
    assert abs(wrong_survival-flux_survival) > .08


def test_photon_exact_interval_matches_independent_scipy_binomial_api():
    result = photon_survival(1024, .7, np.random.default_rng(778))
    interval = binomtest(result['escaped'], 1024).proportion_ci(confidence_level=.95, method='exact')
    assert abs(result['lower']-interval.low) < 1e-12
    assert abs(result['upper']-interval.high) < 1e-12
    assert result['escaped']+result['absorbed'] == 1024


def test_photon_intervals_handle_all_absorbed_and_all_escaped_without_nan():
    class FixedPaths:
        def __init__(self, path):
            self.path = path
        def random(self, count):
            return np.ones(count)
        def exponential(self, size):
            return np.full(size, self.path)
    absorbed = photon_survival(32, 1., FixedPaths(0.))
    escaped = photon_survival(32, 1., FixedPaths(100.))
    assert absorbed['escaped'] == 0 and absorbed['lower'] == 0.
    assert escaped['absorbed'] == 0 and escaped['upper'] == 1.
    assert absorbed['upper'] < 1. and escaped['lower'] > 0.


@pytest.mark.parametrize('kwargs', [dict(cells=0), dict(ordinates=1), dict(optical_depth=-1.),
                                   dict(optical_depth=np.nan), dict(scheme='scattering')])
def test_radiation_rejects_unsupported_inputs(kwargs):
    arguments = dict(cells=16, ordinates=8, optical_depth=.7)
    arguments.update(kwargs)
    with pytest.raises(ValueError):
        absorption_slab(**arguments)


def test_statistics_do_not_use_zero_standard_error_to_hide_bias():
    assert float(experiments._standardized(0., 0.)) == 0.
    assert float(experiments._standardized(1., 0.)) > 1e100


def test_kinetic_case_constructor_rejects_nonfinite_metrics():
    with pytest.raises(ValueError):
        experiments._case('bad', {'x': True}, {'error': float('nan')}, [{'series': 'bad'}])
