"""Independent identities, convergence, rejected inputs and fixed acceptance tests."""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
import pytest
from scipy.integrate import solve_ivp
from biology import (Budget, CosineGalerkin, RUNNERS, evaluate_cosine, fd_split,
                     initial_field, kinetics, midpoint_reaction, norms,
                     observables, periodic_laplacian, product, run_case, validate)
from run import run

HERE = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def inputs():
    return json.loads((HERE/'inputs.json').read_text())


def test_small_finite_amplitude_case_separates_reference_space_and_time_errors(inputs):
    # The complete fixed cases are run by run.py and the public verifier separately.
    # This shorter representative integration avoids repeating the 28-second run.
    config = deepcopy(inputs['cases']['schnakenberg-nonlinear'])
    config.update(time=2., snapshot_times=[0., 1., 2.], grids=[16, 32, 64], space_step=.0025,
                  temporal_grid=64, time_steps=[.05, .025, .0125], reference_modes=[8, 12, 16])
    result = run_case('schnakenberg-nonlinear', config)
    assert result['metrics']['minimum_concentration'] > 0
    assert result['checks']['reference_tolerance_linf']
    assert result['checks']['maximum_reaction_balance_error']
    assert all(math.isfinite(v) for v in result['metrics'].values())
    for sequence in ['spatial_orders', 'temporal_orders']:
        assert set(result[sequence]) == {'l1', 'l2', 'linf'}
        assert all(min(values) >= 1.7 for values in result[sequence].values())
    assert len(result['snapshots']) == 3
    assert {r['series'] for r in result['records']} >= {'space', 'time', 'reference-refinement', 'profile'}


def test_criteria_preserved_while_temporal_resolution_strengthened(inputs):
    old = json.loads((HERE/'inputs-initial.json').read_text())
    assert hashlib.sha256((HERE/'inputs-initial.json').read_bytes()).hexdigest() == 'aa97550f4d965505da9841d2e565b066a02e7af1d7585585e001bea0eb52accb'
    assert hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest() == '375d70f40187400bf812dcd09d4beb0a8f7f3a79baf6a67c818b940bf82bbb84'
    for name, new in inputs['cases'].items():
        original = old['cases'][name]
        assert new['acceptance'] == original['acceptance']
        for key in original:
            if key not in ['space_step', 'time_steps']:
                assert new[key] == original[key]


def test_cosine_projection_and_evaluation_are_inverse_on_retained_basis(inputs):
    system = CosineGalerkin(12, inputs['cases']['schnakenberg-nonlinear'], Budget())
    np.testing.assert_allclose(product(system.project, system.basis), np.eye(13), atol=7e-15)
    assert system.m > 4*12


def test_cubic_projection_is_dealiased_at_top_retained_mode(inputs):
    system = CosineGalerkin(8, inputs['cases']['schnakenberg-nonlinear'], Budget())
    values = system.basis[:, -1]**3
    coefficients = np.einsum('ij,j->i', system.project, values)
    expected = np.zeros(9);expected[-1] = .75
    np.testing.assert_allclose(coefficients, expected, atol=8e-15)


def test_galerkin_analytic_jacobian_matches_independent_directional_difference(inputs):
    system = CosineGalerkin(8, inputs['cases']['schnakenberg-nonlinear'], Budget())
    vector = np.zeros((2, 9));vector[:, :5] = inputs['cases']['schnakenberg-nonlinear']['initial_cosine_coefficients']
    vector = vector.ravel();direction = np.random.default_rng(17).normal(size=len(vector))
    h = 2e-6
    fd = (system.rhs(0, vector+h*direction)-system.rhs(0, vector-h*direction))/(2*h)
    analytic = np.einsum('ij,j->i', system.jac(0, vector), direction)
    np.testing.assert_allclose(analytic, fd, rtol=2e-8, atol=3e-9)


@pytest.mark.parametrize('n,mode', [(16, 1), (32, 7), (64, 13)])
def test_fd_fourier_multiplier_is_the_centered_difference_operator(n, mode):
    dx = 2*math.pi/n;x = np.arange(n)*dx
    y = np.cos(mode*x)
    lam = -4*math.sin(mode*dx/2)**2/(dx*dx)
    np.testing.assert_allclose(periodic_laplacian(y, dx), lam*y, atol=3e-12)
    assert abs(lam+mode**2) > 0, 'FD diagonalization must not silently use continuum eigenvalues'


def test_midpoint_reaction_obeys_nonconserved_source_balance():
    y = np.array([[.4, 1., 2.], [.7, .9, .3]])
    new, mid, info = midpoint_reaction(y, .1, .1, .9)
    np.testing.assert_allclose(np.sum(new-y, axis=0), .1*(1-mid[0]), atol=3e-14)
    assert info['residual'] < 2e-13


def test_midpoint_reaction_has_second_order_against_radau():
    initial = np.array([[1.3], [.5]])
    reference = solve_ivp(lambda t, y: kinetics(y, .1, .9), [0, .8], initial[:, 0], method='Radau', rtol=2e-12, atol=2e-14).y[:, -1]
    errors = []
    for step in [.1, .05, .025]:
        y = initial.copy()
        for _ in range(round(.8/step)):
            y, _, _ = midpoint_reaction(y, step, .1, .9)
        errors.append(np.max(np.abs(y[:, 0]-reference)))
    assert min(np.log2(np.array(errors[:-1])/errors[1:])) > 1.95


def test_tighter_newton_tolerance_does_not_change_the_resolved_field(inputs):
    config = deepcopy(inputs['cases']['schnakenberg-nonlinear'])
    config['time'] = .5;config['snapshot_times'] = [0., .5]
    regular, _ = fd_split(config, 32, .01)
    config['newton_tolerance'] = 8e-16
    tight, _ = fd_split(config, 32, .01)
    np.testing.assert_allclose(regular[.5], tight[.5], atol=2e-12, rtol=0)


def test_failed_newton_is_reported_without_clipping_or_step_adaptation():
    with pytest.raises(RuntimeError, match='Newton'):
        midpoint_reaction(np.array([[4.], [.2]]), 2., .1, .9, iterations=2)


def test_generated_harmonic_indicator_excludes_seeded_mode_four(inputs):
    x = np.arange(256)*2*math.pi/256
    field = initial_field(inputs['cases']['schnakenberg-nonlinear'], x)
    assert observables(field)['higher_harmonic_ratio'] < 1e-13
    field[0] += .04*np.cos(6*x)
    assert observables(field)['higher_harmonic_ratio'] == pytest.approx(.5, abs=1e-13)


def test_raw_field_error_detects_a_translated_identical_shape():
    x = np.arange(128)*2*math.pi/128
    field = np.array([1+.2*np.cos(2*x), .9-.1*np.cos(2*x)])
    assert norms(field-np.roll(field, 4, axis=-1))['linf'] > .07
    assert norms(np.array([[1., -1.], [.5, -.5]])) == {'l1': 1., 'l2': 1., 'linf': 1.}


def test_reflection_even_and_pi_periodic_inputs_are_explicit(inputs):
    config = inputs['cases']['schnakenberg-nonlinear']
    x = np.linspace(0, 2*math.pi, 39)
    np.testing.assert_allclose(initial_field(config, x), initial_field(config, -x), atol=2e-15)
    np.testing.assert_allclose(initial_field(config, x), initial_field(config, x+math.pi), atol=2e-15)


def test_constant_equilibrium_is_stationary_in_independent_galerkin_reference(inputs):
    system = CosineGalerkin(8, inputs['cases']['schnakenberg-nonlinear'], Budget())
    coefficients = np.zeros((2, 9));coefficients[:, 0] = [1., .9]
    np.testing.assert_allclose(system.rhs(0, coefficients.ravel()), 0, atol=3e-15)


@pytest.mark.parametrize('key,value', [
    ('grids', [32, 64, 1000000]), ('reference_modes', [32, 64, 999]),
    ('time', 1000), ('space_step', 1e-12), ('temporal_grid', True),
    ('newton_iterations', 1000), ('diffusion', [.01, -1]),
    ('reference_rtol', float('nan')), ('time_steps', [.1, .05, .03])
])
def test_unbounded_or_invalid_configuration_is_rejected_before_allocation(inputs, key, value):
    config = deepcopy(inputs['cases']['schnakenberg-nonlinear']);config[key] = value
    with pytest.raises(ValueError):
        validate(config)


def test_wall_clock_failure_guard():
    budget = Budget();budget.deadline = time.perf_counter()-1
    with pytest.raises(RuntimeError, match='budget exhausted'):
        budget.check()
    with pytest.raises(ValueError):
        Budget(121)


def test_run_rejects_nonempty_output_before_starting_physics(tmp_path):
    (tmp_path/'keep.txt').write_text('keep')
    with pytest.raises(ValueError, match='new or empty'):
        run(HERE/'inputs.json', tmp_path)
    assert (tmp_path/'keep.txt').read_text() == 'keep'


def test_case_metadata_links_existing_methods_and_states_scope():
    cases = json.loads((HERE/'cases.json').read_text())
    assert {c['id'] for c in cases} == set(RUNNERS)
    for case in cases:
        assert set(case['method_ids']) == {'centered-difference', 'implicit-midpoint'}
        for key in ['summary', 'assumptions', 'algorithm', 'validation', 'limits']:
            assert set(case[key]) == {'ja', 'en'} and all(case[key].values())
        for name in case['code_files']:
            assert (HERE/name).is_file()
