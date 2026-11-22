"""Checks of analytic identities, failure modes and independent-reference experiments."""
import json
import math
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
from scipy.linalg import solve_discrete_lyapunov
from models import (RUNNERS, baoab_linear_map, baoab_step, chain_diagnostics,
                    gaussian_metropolis, initial_positive_tau, periodic_laplacian)
from run import run

HERE = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def fixed_results():
    inputs = json.loads((HERE/'inputs.json').read_text())['cases']
    return {name: runner(inputs[name]) for name, runner in RUNNERS.items()}


@pytest.mark.parametrize('name', list(RUNNERS))
def test_fixed_inputs_and_independent_references_pass(name, fixed_results):
    case = fixed_results[name]
    assert case['passed']
    assert len(case['checks']) >= 4 and all(case['checks'].values())
    assert case['records']
    assert all(np.isfinite(v) for v in case['metrics'].values())


@pytest.mark.parametrize('rho', [0.2, 0.5, 0.8, 0.95])
def test_positive_sequence_matches_known_ar1_sum(rho):
    tau = initial_positive_tau(rho**np.arange(4096))
    assert tau == pytest.approx((1+rho)/(1-rho), rel=2e-14)


def test_ips_stops_at_first_nonpositive_pair():
    assert initial_positive_tau([1, .5, .1, -.2, 100, 100]) == pytest.approx(2)


def test_zero_variance_chains_are_rejected():
    with pytest.raises(ValueError, match='variance'):
        chain_diagnostics(np.ones((4, 64)))


def test_separated_chains_trigger_split_rhat():
    rng = np.random.default_rng(17)
    chains = rng.normal(size=(4, 256))+np.arange(4)[:, None]*3
    assert chain_diagnostics(chains)['split_rhat'] > 2


def test_mh_reproducibility_and_separate_chain_draws():
    a, acceptance = gaussian_metropolis(10, 4, 128, 32, 1.5)
    b, acceptance_b = gaussian_metropolis(10, 4, 128, 32, 1.5)
    c, _ = gaussian_metropolis(11, 4, 128, 32, 1.5)
    np.testing.assert_array_equal(a, b)
    assert acceptance == acceptance_b
    assert not np.array_equal(a, c)
    assert not np.array_equal(a[0], a[1])


@pytest.mark.parametrize('h', [.1, .4, 1.2])
def test_baoab_covariance_has_exact_harmonic_position_and_biased_momentum(h):
    omega, gamma, temperature = 1.1, .7, 1.3
    matrix, noise = baoab_linear_map(h, omega, gamma, temperature)
    covariance = solve_discrete_lyapunov(matrix, noise)
    analytic = np.diag([temperature/omega**2, temperature*(1-h*h*omega*omega/4)])
    np.testing.assert_allclose(covariance, analytic, rtol=3e-14, atol=3e-14)


def test_baoab_step_agrees_with_linear_map_and_noise_covariance():
    matrix, covariance = baoab_linear_map(.2, 1.2, .8, 1.3)
    q, p = baoab_step(0.7, -0.3, .2, 1.2, .8, 1.3, 0.)
    np.testing.assert_allclose([q, p], matrix@np.array([.7, -.3]), atol=1e-15)
    noise = np.array(baoab_step(0., 0., .2, 1.2, .8, 1.3, 1.))
    np.testing.assert_allclose(covariance, np.outer(noise, noise), atol=1e-15)


@pytest.mark.parametrize('h,gamma,temperature', [(2., 1., 1.), (.1, 0., 1.), (.1, 1., -1.)])
def test_invalid_langevin_parameters_fail(h, gamma, temperature):
    with pytest.raises(ValueError):
        baoab_linear_map(h, 1., gamma, temperature)


def test_periodic_laplacian_fourier_eigenvalue_and_mean_conservation():
    n, mode = 32, 3
    dx = 2*math.pi/n
    initial = np.cos(mode*np.arange(n)*dx)
    lam_h = -4*math.sin(mode*dx/2)**2/dx**2
    np.testing.assert_allclose(periodic_laplacian(initial, dx), lam_h*initial, rtol=0, atol=1e-12)
    assert abs(periodic_laplacian(initial, dx).sum()) < 1e-12


def test_space_time_orders_and_excitation_are_separate(fixed_results):
    assert fixed_results['reaction-diffusion-fourier']['metrics']['spatial_minimum_order'] > 1.9
    assert fixed_results['reaction-diffusion-fourier']['metrics']['temporal_minimum_order'] > 3.8
    turing = fixed_results['turing-schnakenberg']['metrics']
    assert turing['homogeneous_max_real_eigenvalue'] < 0 < turing['continuum_mode_growth_rate']
    assert fixed_results['fitzhugh-nagumo']['metrics']['peak_v'] > 1.5


def test_runner_keeps_input_hash_and_refuses_overwrite(tmp_path):
    output = tmp_path/'result'
    result = run(HERE/'inputs.json', output, 'gaussian-mcmc')
    assert result['passed'] and len(result['input_sha256']) == 64
    assert (output/'gaussian-mcmc.csv').is_file()
    with pytest.raises(ValueError, match='new or empty'):
        run(HERE/'inputs.json', output, 'gaussian-mcmc')


def test_nonfinite_input_is_explicit_failure(tmp_path):
    source = tmp_path/'bad.json'
    source.write_text('{"schema_version":1,"bad":NaN}')
    with pytest.raises(ValueError, match='Nonfinite'):
        run(source, tmp_path/'output')


def test_missing_case_configuration_is_rejected(tmp_path):
    data = json.loads((HERE/'inputs.json').read_text())
    del data['cases']['fitzhugh-nagumo']
    source = tmp_path/'missing.json'
    source.write_text(json.dumps(data))
    with pytest.raises(ValueError, match='complete'):
        run(source, tmp_path/'output')


def test_cli_incomplete_parameters_have_explicit_input_failure_code(tmp_path):
    data = json.loads((HERE/'inputs.json').read_text())
    del data['cases']['gaussian-mcmc']['sampler']
    source = tmp_path/'missing-parameter.json'
    source.write_text(json.dumps(data))
    proc = subprocess.run([sys.executable, str(HERE/'run.py'), '--input', str(source),
                           '--case', 'gaussian-mcmc', '--output', str(tmp_path/'out')],
                          capture_output=True, text=True)
    assert proc.returncode == 2 and 'sampler' in proc.stderr
