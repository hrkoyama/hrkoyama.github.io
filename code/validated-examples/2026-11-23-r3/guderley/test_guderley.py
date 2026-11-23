"""Small physical identities, geometry, time stages and explicit failure paths."""
from pathlib import Path
import hashlib
import json
from unittest.mock import patch
import warnings
import numpy as np
import pytest
import guderley_solver as s
from references import precollapse as ref
from references.precollapse import GuderleyReference, TABULATED_LAMBDA

ROOT = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def reference():
    return GuderleyReference()


def uniform(n, pressure=.2, velocity=0.):
    return s.conserved(np.ones(n), np.full(n, velocity), np.full(n, pressure))


def test_spherical_shell_volumes_and_areas():
    edges, areas, volumes = s.geometry(73, .75)
    assert areas[0] == 0
    assert np.isclose(areas[-1], 4*np.pi*.75**2, rtol=2e-15)
    assert np.isclose(volumes.sum(), 4*np.pi*.75**3/3, rtol=2e-15)
    assert np.all(np.diff(edges) > 0)


def test_invalid_geometry_is_rejected():
    for n, radius in [(7, .75), (9.5, .75), (16, 0), (16, float('nan'))]:
        with pytest.raises(ValueError):
            s.geometry(n, radius)


def test_conserved_primitive_round_trip():
    rho, velocity, pressure = np.array([1., 6.]), np.array([0., -.35]), np.array([0., .15])
    q = s.conserved(rho, velocity, pressure)
    got = s.primitive(q)
    np.testing.assert_array_equal(got[0], rho)
    np.testing.assert_allclose(got[1], velocity, atol=0, rtol=2e-15)
    np.testing.assert_allclose(got[2], pressure, atol=0, rtol=2e-15)


def test_cold_upstream_has_exactly_zero_flux_without_division_warning():
    q = uniform(4, pressure=0.)
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        with np.errstate(all='raise'):
            np.testing.assert_array_equal(s.hll(q, q), np.zeros((4, 3)))
    np.testing.assert_array_equal(s.primitive(q)[2], np.zeros(4))


def test_nonpositive_density_is_rejected():
    for rho in [0., -1.]:
        with pytest.raises(ValueError):
            s.primitive(np.array([[rho, 0., 1.]]))


def test_nonfinite_state_is_rejected():
    for value in [np.nan, np.inf, -np.inf]:
        with pytest.raises(ValueError):
            s.primitive(np.array([[1., 0., value]]))


def test_negative_internal_energy_outside_fixed_band_fails():
    with pytest.raises(ValueError):
        s.primitive(np.array([[1., 2., 1.]]))


def test_roundoff_band_is_not_a_state_or_pressure_floor():
    q = np.array([[1., 0., -np.finfo(float).eps]])
    original = q.copy()
    rho, _, pressure, internal = s.primitive(q)
    assert pressure[0] < 0 and internal[0] < 0
    guard = {'evaluations': 0, 'minimum_pressure': 0.}
    np.testing.assert_array_equal(s.sound_speed(rho, pressure, guard), [0.])
    np.testing.assert_array_equal(q, original)
    assert guard['evaluations'] == 1 and guard['minimum_pressure'] == pressure[0]


def test_sound_speed_rejects_pressure_beyond_cancellation_band():
    with pytest.raises(ValueError):
        s.sound_speed(np.array([1.]), np.array([-.01]))


def test_physical_flux_matches_mass_momentum_and_enthalpy_transport():
    q = s.conserved(np.array([2.]), np.array([-.3]), np.array([.4]))
    np.testing.assert_allclose(s.physical_flux(q)[0], [-.6, .58, -.447], rtol=2e-15)


def test_hll_identical_states_are_consistent():
    q = s.conserved(np.array([1., 2.]), np.array([.3, -.4]), np.array([.2, .5]))
    np.testing.assert_allclose(s.hll(q, q), s.physical_flux(q), atol=2e-16, rtol=2e-15)


def test_hll_supersonic_upwind_both_directions():
    left = s.conserved(np.array([1.]), np.array([4.]), np.array([.1]))
    right = s.conserved(np.array([.8]), np.array([3.]), np.array([.2]))
    np.testing.assert_allclose(s.hll(left, right), s.physical_flux(left))
    reflect = np.array([1., -1., 1.])
    np.testing.assert_allclose(s.hll(left*reflect, right*reflect), s.physical_flux(right*reflect))


def test_hll_respects_radial_velocity_reflection():
    left = s.conserved(np.array([1.]), np.array([-.2]), np.array([.3]))
    right = s.conserved(np.array([.6]), np.array([.4]), np.array([.1]))
    reflection = np.array([1., -1., 1.])
    np.testing.assert_allclose(s.hll(right*reflection, left*reflection),
                               s.hll(left, right)*[-1., 1., -1.], atol=2e-16)


def test_uniform_static_pressure_cancels_geometric_flux_divergence():
    _, areas, volumes = s.geometry(64, .75)
    q = uniform(64)
    rhs, boundary, source = s.rhs(q, -.9, areas, volumes, lambda t: q[-1])
    np.testing.assert_allclose(rhs, 0., atol=5e-12, rtol=0)
    assert source[1] > 0 and boundary[1] < 0
    np.testing.assert_allclose(boundary+source, 0., atol=3e-15)


def test_shared_fluxes_telescope_in_all_three_discrete_budgets():
    edges, areas, volumes = s.geometry(37, .75)
    radius = .5*(edges[:-1]+edges[1:])
    q = s.conserved(1+.2*radius, -.1*radius, .2+.03*radius)
    rhs, boundary, source = s.rhs(q, -.9, areas, volumes, lambda t: q[-1])
    np.testing.assert_allclose(np.sum(rhs*volumes[:, None], axis=0), boundary+source,
                               atol=2e-15, rtol=2e-14)


def test_actual_outer_hll_flux_is_the_recorded_boundary_term():
    _, areas, volumes = s.geometry(16, .75)
    q, outer = uniform(16), uniform(1, pressure=.3, velocity=-.1)[0]
    _, boundary, _ = s.rhs(q, -.9, areas, volumes, lambda t: outer)
    expected = -areas[-1]*s.hll(q[-1:], outer[None, :])[0]
    np.testing.assert_array_equal(boundary, expected)


def test_heun_uses_both_actual_stage_times_for_outer_boundary():
    edges, _, _ = s.geometry(16, .75)
    q, calls = uniform(16), []
    def outer(t):
        calls.append(t)
        return q[-1]
    out = s.solve(q, edges, -1., -.99999, .4, outer)
    assert calls == [-1., -.99999]
    assert out['steps'] == 1 and out['time'] == -.99999


def test_small_static_run_has_actual_rk_weighted_balances():
    edges, _, _ = s.geometry(32, .75)
    q = uniform(32)
    out = s.solve(q, edges, -1., -.999, .4, lambda t: q[-1])
    residual = (out['final_integral']-out['initial_integral']
                - out['boundary_net_integral']-out['geometric_source_integral'])
    np.testing.assert_allclose(residual, 0., atol=3e-15)
    assert out['state_floor_count'] == out['rejected_steps'] == 0
    assert out['history'][-1]['time'] == -.999


def test_solver_does_not_mutate_supplied_initial_cell_means():
    edges, _, _ = s.geometry(16, .75)
    q = uniform(16)
    saved = q.copy()
    s.solve(q, edges, -1., -.99999, .4, lambda t: saved[-1])
    np.testing.assert_array_equal(q, saved)


def test_invalid_predictor_keeps_raw_state_and_stops_without_retry():
    edges, _, _ = s.geometry(16, .75)
    q = uniform(16)
    def bad(state, *args, **kwargs):
        update = np.zeros_like(state)
        update[:, 0] = -1e100
        return update, np.zeros(3), np.zeros(3)
    with patch.object(s, 'rhs', side_effect=bad) as called:
        with pytest.raises(s.InvalidStage) as got:
            s.solve(q, edges, -1., -.999, .4, lambda t: q[-1])
    assert called.call_count == 1
    assert np.any(got.value.failed_state[:, 0] < 0)
    assert got.value.failed_context['stage'] == 'predictor'
    assert got.value.completed_history[0]['time'] == -1.


def test_invalid_corrector_keeps_raw_state_and_stops_without_retry():
    edges, _, _ = s.geometry(16, .75)
    q, calls = uniform(16), []
    def bad(state, *args, **kwargs):
        calls.append(1)
        update = np.zeros_like(state)
        if len(calls) == 2:
            update[:, 2] = -1e100
        return update, np.zeros(3), np.zeros(3)
    with patch.object(s, 'rhs', side_effect=bad) as called:
        with pytest.raises(s.InvalidStage) as got:
            s.solve(q, edges, -1., -.999, .4, lambda t: q[-1])
    assert called.call_count == 2
    assert np.any(got.value.failed_state[:, 2] < 0)
    assert got.value.failed_context['stage'] == 'update'


def test_step_budget_exhaustion_is_explicit_and_retains_state():
    edges, _, _ = s.geometry(32, .75)
    q = uniform(32)
    with pytest.raises(s.InvalidStage) as got:
        s.solve(q, edges, -1., -.85, .4, lambda t: q[-1], max_steps=1)
    assert got.value.failed_context['stage'] == 'step-budget'
    assert got.value.failed_context['step'] == 1
    assert np.all(np.isfinite(got.value.failed_state))


def test_cfl_zero_and_subnormal_speeds_do_not_overflow():
    width = np.full(4, .25)
    tiny = np.nextafter(0., 1.)
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        with np.errstate(over='raise', divide='raise', invalid='raise'):
            assert s.cfl_step(np.zeros(4), width, .4, .05) == .05
            assert s.cfl_step(np.full(4, tiny), width, .4, .05) == .05
            assert s.cfl_step(np.array([1., tiny, 0., 0.]), width, .4, 1.) == .1


def test_postcollapse_or_reversed_intervals_are_rejected():
    edges, _, _ = s.geometry(16, .75)
    q = uniform(16)
    for start, stop in [(-1., 0.), (-.85, -1.), (-1., -1.)]:
        with pytest.raises(ValueError):
            s.solve(q, edges, start, stop, .4, lambda t: q[-1])


def test_reference_reuses_source_bound_eigenvalue_checks_phase_and_rejects_tampering(reference, tmp_path):
    cache_path = ROOT/'references/eigenvalue-cache.json'
    cache = json.loads(cache_path.read_text())
    proof = ref.load_eigenvalue_cache()
    qualification_path = ROOT/'references'/cache['qualification']['file']
    qualification = json.loads(qualification_path.read_text())
    assert qualification['passed'] and all(qualification['checks'].values())
    assert proof['qualification_sha256'] == hashlib.sha256(qualification_path.read_bytes()).hexdigest()
    assert proof['cache_sha256'] == hashlib.sha256(cache_path.read_bytes()).hexdigest()
    assert proof['eigenvalue_recomputed'] is False
    assert reference.lambda_ == proof['lambda'] == qualification['metadata']['lambda']
    assert abs(reference.lambda_/TABULATED_LAMBDA-1) < 2e-9
    assert abs(reference.alpha*reference.lambda_-1) < 2e-15
    # Default verification must not repeat the costly nonlinear shooting
    # already recorded in the immutable qualification. The fresh residual
    # still exercises the actual pinned critical-phase ODE once.
    with patch.object(ref.exponent_module, 'eexp', side_effect=AssertionError('Unexpected full eigenvalue shooting')):
        ref.eigenvalue.cache_clear()
        assert ref.eigenvalue() == qualification['metadata']['lambda']
        ref.critical_phase_residual.cache_clear()
        assert abs(ref.critical_phase_residual()) < 2e-7
    tampered = tmp_path/'tampered-eigenvalue-cache.json'
    cache['lambda'] += 1e-3
    tampered.write_text(json.dumps(cache)+'\n')
    with pytest.raises(RuntimeError):
        ref.load_eigenvalue_cache(tampered)


def test_reference_cold_upstream_is_exactly_unseeded(reference):
    radius = reference.shock_radius(-.9)
    rho, velocity, pressure = reference.point_state(np.array([0., .3*radius, .999*radius]), -.9)
    np.testing.assert_array_equal(rho, [1., 1., 1.])
    np.testing.assert_array_equal(velocity, [0., 0., 0.])
    np.testing.assert_array_equal(pressure, [0., 0., 0.])


def test_reference_strong_shock_jump_from_mass_momentum_energy(reference):
    t = -.925
    radius, speed = reference.shock_radius(t), reference.shock_speed(t)
    rho, velocity, pressure = reference.point_state(np.array([radius*(1+1e-9)]), t)
    np.testing.assert_allclose([rho[0], velocity[0]/speed, pressure[0]/speed**2],
                               [6., 5/6, 5/6], rtol=2e-8)
    pre, post = np.array([[1., 0., 0.]]), s.conserved(rho, velocity, pressure)
    np.testing.assert_allclose(s.physical_flux(pre)-speed*pre,
                               s.physical_flux(post)-speed*post, atol=2e-8, rtol=2e-8)


def test_reference_similarity_radius_and_speed_normalization(reference):
    assert reference.shock_radius(-1.) == .6
    assert np.isclose(reference.shock_radius(-.85)/.6, .85**reference.alpha, rtol=2e-15)
    t, dt = -.925, 1e-6
    derivative = (reference.shock_radius(t+dt)-reference.shock_radius(t-dt))/(2*dt)
    assert np.isclose(derivative, reference.shock_speed(t), rtol=2e-8)


def test_split_shock_cell_means_converge_in_conserved_volume_measure(reference):
    edges = np.linspace(0., .75, 73)
    a, pa = reference.cell_means(edges, -.925, 16)
    b, pb = reference.cell_means(edges, -.925, 32)
    np.testing.assert_allclose(a, b, rtol=2e-9, atol=2e-11)
    np.testing.assert_allclose(pa, pb, rtol=2e-9, atol=2e-11)
    assert np.all(a[:, 0] > 0) and np.all(pa >= 0)


def test_pressure_from_conserved_mean_is_not_mean_primitive_pressure(reference):
    edges = np.array([.59, .61])
    q, pressure = reference.cell_means(edges, -1., 32)
    assert pressure[0] == pytest.approx(s.primitive(q)[2][0], rel=2e-15)
    z, weights = np.polynomial.legendre.leggauss(32)
    radii = .605+.005*z
    primitive_pressure = reference.point_state(radii, -1.)[2]
    shell_volume = (.61**3-.59**3)/3
    mean_primitive_pressure = .005*np.dot(weights, primitive_pressure*radii**2)/shell_volume
    assert pressure[0] > mean_primitive_pressure + 1e-5


def test_preregistered_input_is_short_spherical_and_distinguishes_active_region():
    cfg = json.loads((ROOT/'inputs.json').read_text())['cases']['guderley-implosion']
    assert cfg['grids'] == [128, 256, 512]
    assert cfg['dimension'] == 3 and cfg['gamma'] == 1.4
    assert cfg['initial_time'] == -1. and cfg['final_time'] == -.85
    assert cfg['radius'] == .75 and cfg['shock_radius_at_minus_one'] == .6
    assert cfg['upstream_pressure'] == 0 and cfg['upstream_velocity'] == 0
    assert cfg['active_radius_factor'] == .8
    assert cfg['reference_order'] == 16 and cfg['reference_check_order'] == 32


def test_euler_algorithm_does_not_import_the_similarity_reference():
    source = (ROOT/'guderley_solver.py').read_text()
    assert 'import references' not in source and 'from references' not in source
    assert 'eexp(' not in source and 'GuderleyReference(' not in source


def test_pre_run_contract_binds_sources_and_unchanged_physical_acceptance():
    contract = json.loads((ROOT/'pre-run-contract.json').read_text())
    assert contract['declared_before_first_pde_run'] is False
    assert contract['declared_before_this_revision_pde_execution'] is True
    assert contract['declared_before_this_revision_pytest_execution'] is True
    for name, digest in contract['files_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    previous = json.loads((ROOT/'attempts/02/pre-run-contract.json').read_text())
    for name in ['inputs.json', 'acceptance.json', 'guderley_solver.py', 'run.py']:
        assert contract['files_sha256'][name] == previous['files_sha256'][name], name
    acceptance = json.loads((ROOT/'acceptance.json').read_text())
    assert acceptance['declared_before_first_pde_run'] is True
    assert acceptance['limits']['minimum_internal_energy'] == -64*np.finfo(float).eps
