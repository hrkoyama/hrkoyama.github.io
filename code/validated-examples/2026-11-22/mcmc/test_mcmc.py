"""Meaningful equation, independent-fixture, sampler and failure-guard tests."""
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
import pytest
from scipy.integrate import quad
from diagnostics import (METRICS, autocovariance, basic_rhat, diagnose,
                         direct_autocovariance, rank_normalize, split_chains)
from experiments import load_reference, validate
from fixtures import ar1_chains, edge_fixtures
from sampler import (Budget, array_sha256, log_target, proposal_density,
                     sample_chains, target_cdf, validate_sampler)
from run import run

HERE = Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def inputs():
    return json.loads((HERE/'inputs.json').read_text())


@pytest.fixture(scope='module')
def reference():
    return json.loads((HERE/'reference.json').read_text())


def test_predeclared_inputs_and_reference_recipe_hashes(inputs, reference):
    assert hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest() == 'b20b594ab2d001426fbc58d1fe86fe4719bd42455f6a10f502966f85fb6eb49a'
    assert reference['version'] == '0.20.0' and reference['provenance']['actually_executed'] is True
    assert len(reference['datasets']) == 62
    for name, expected in reference['provenance']['source_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected


def test_reference_tampering_and_missing_datasets_cannot_silently_pass(tmp_path, monkeypatch, inputs, reference):
    import experiments
    corrupted = deepcopy(reference);corrupted['datasets'] = []
    path = tmp_path/'reference.json';path.write_text(json.dumps(corrupted))
    config = inputs['cases']['mcmc-diagnostic-reference']
    with pytest.raises(ValueError, match='SHA256 mismatch'):
        load_reference(config, path)
    # Independently test completeness after simulating a newly recorded digest.
    monkeypatch.setattr(experiments, 'REFERENCE_SHA256', hashlib.sha256(path.read_bytes()).hexdigest())
    with pytest.raises(ValueError, match='completeness mismatch'):
        load_reference(config, path)


def test_nonconstant_diagnostic_null_regression_cannot_pass_as_a_policy_exception(monkeypatch, inputs):
    import experiments
    monkeypatch.setattr(experiments, 'diagnose', lambda values: {
        **{key: None for key in METRICS}, 'status': 'zero_global_variance'})
    with pytest.raises(ValueError, match='Contradictory constant'):
        experiments.diagnostic_case(inputs['cases']['mcmc-diagnostic-reference'])


def test_analytic_mixture_cdf_moments_and_occupancy_by_independent_quadrature():
    density = lambda x: math.exp(float(log_target(x)))
    assert quad(density, -np.inf, np.inf, epsabs=1e-10)[0] == pytest.approx(1., abs=1e-10)
    assert quad(lambda x: x*density(x), -np.inf, np.inf, epsabs=1e-10)[0] == pytest.approx(0., abs=1e-10)
    assert quad(lambda x: x*x*density(x), -np.inf, np.inf, epsabs=1e-10)[0] == pytest.approx(37., abs=1e-9)
    assert quad(density, 0., np.inf, epsabs=1e-10)[0] == pytest.approx(.5, abs=1e-10)
    assert target_cdf(0.) == .5


@pytest.mark.parametrize('x,y', [(-6., 6.), (-5.7, 6.3), (-6.1, -4.8), (.2, -.4)])
def test_reflection_mixture_proposal_symmetry_and_mh_detailed_balance(x, y):
    qxy = proposal_density(y, x);qyx = proposal_density(x, y)
    assert qxy == pytest.approx(qyx, rel=1e-15)
    px, py = np.exp(log_target(x)), np.exp(log_target(y))
    assert px*qxy*min(1., py/px) == pytest.approx(py*qyx*min(1., px/py), rel=2e-14)


def test_sampler_retains_rejections_and_is_fixed_seed_reproducible(inputs):
    config = deepcopy(inputs['cases']['mcmc-multimodal-mixing']['sampler'])
    config.update(samples=512, budgets=[128, 256, 512], burn=64)
    x, acceptance = sample_chains(config, 'same_mode', 19)
    same, _ = sample_chains(config, 'same_mode', 19)
    other, _ = sample_chains(config, 'same_mode', 20)
    np.testing.assert_array_equal(x, same)
    assert not np.array_equal(x, other)
    assert np.count_nonzero(np.diff(x, axis=1) == 0) > 100
    assert x.shape == (4, 512) and np.all((acceptance > .3) & (acceptance < .95))


def test_split_odd_draws_drops_only_the_center():
    x = np.arange(2*9).reshape(2, 9)
    actual = split_chains(x)
    np.testing.assert_array_equal(actual, np.array([[0,1,2,3],[9,10,11,12],[5,6,7,8],[14,15,16,17]]))


def test_blom_ranks_use_average_ties_and_corrected_denominator():
    x = np.array([[1., 1.], [2., 4.]])
    from scipy.special import ndtri
    expected = ndtri((np.array([[1.5, 1.5], [3., 4.]])-3/8)/(4+1/4))
    np.testing.assert_array_equal(rank_normalize(x), expected)


@pytest.mark.parametrize('name', ['iid','odd','ties','scale','shift','antithetic'])
def test_actual_independent_arviz_fixtures_match_on_finite_diagnostics(name, reference):
    x = edge_fixtures()[name]
    entry = next(row for row in reference['datasets'] if row['id'] == 'edge__'+name)
    assert array_sha256(x) == entry['sha256']
    actual = diagnose(x)
    for key in METRICS:
        expected = entry['metrics'][key]['value']
        assert actual[key] == pytest.approx(expected, rel=2e-8, abs=2e-10)


def test_positive_rescaling_preserves_rank_diagnostics_at_tiny_nonzero_scales():
    x = edge_fixtures()['iid']
    original, small = diagnose(x), diagnose(1e-20*x)
    for key in ['rhat_rank','rhat_z','rhat_folded','ess_bulk','ess_tail']:
        assert small[key] == pytest.approx(original[key], rel=2e-13)
    assert small['status'] == 'ok'


@pytest.mark.parametrize('name,status', [('constant','zero_global_variance'),('separated_constants','infinite_separation')])
def test_degenerate_observables_are_explicit_nulls_not_false_convergence(name, status):
    result = diagnose(edge_fixtures()[name])
    assert result['status'] == status and result['rhat_rank'] is None
    if name == 'constant':
        assert all(result[key] is None for key in METRICS)
    json.dumps(result, allow_nan=False)


def test_exact_constant_rows_avoid_roundoff_created_variance():
    x = np.repeat(np.array([[-.6744897501960817], [.6744897501960817]]), 8192, axis=1)
    value, status = basic_rhat(x)
    assert value is None and status == 'infinite_separation'


@pytest.mark.parametrize('bad', [np.ones((1,128)), np.ones((4,7)), np.full((4,8), np.nan), np.full((4,8), np.inf)])
def test_insufficient_or_nonfinite_data_has_no_numeric_success_values(bad):
    result = diagnose(bad)
    assert result['status'] != 'ok' and all(result[key] is None for key in METRICS)
    json.dumps(result, allow_nan=False)


@pytest.mark.parametrize('draws', [257, 512])
def test_fft_covariance_matches_direct_sums_with_declared_divisor(draws):
    values = np.random.default_rng(81).normal(size=(4, draws))
    lags = [0,1,2,17,64]
    np.testing.assert_allclose(autocovariance(values)[:, lags], direct_autocovariance(values, lags), atol=8e-16)


@pytest.mark.parametrize('rho', [-.5, .8])
def test_stationary_ar1_mean_ess_tracks_analytic_tau_and_allows_antithetic_gain(rho):
    values = ar1_chains(rho, 8, 4096, 713)
    result = diagnose(values)
    tau = values.size/result['ess_mean']
    assert abs(tau/((1+rho)/(1-rho))-1) < .25
    if rho < 0:
        assert result['ess_mean'] > 2*values.size


@pytest.mark.parametrize('key,value', [
    ('samples', 100000000), ('chains', 1000000), ('burn', -1),
    ('proposal_scale', 0), ('mode_distance', float('nan')),
    ('jump_probability', 2), ('chains', True), ('budgets', [1,2,3])
])
def test_sampler_budget_and_nonfinite_guards_before_state_allocation(inputs, key, value):
    config = deepcopy(inputs['cases']['mcmc-multimodal-mixing']['sampler']);config[key] = value
    with pytest.raises(ValueError):
        validate_sampler(config)


def test_wall_clock_guard_and_no_overwrite(tmp_path):
    budget = Budget();budget.deadline = time.perf_counter()-1
    with pytest.raises(RuntimeError, match='budget exhausted'):
        budget.check()
    with pytest.raises(ValueError):
        Budget(True)
    (tmp_path/'keep.txt').write_text('keep')
    with pytest.raises(ValueError, match='new or empty'):
        run(HERE/'inputs.json', tmp_path)
    assert (tmp_path/'keep.txt').read_text() == 'keep'


def test_bilingual_metadata_and_existing_method_only():
    cases = json.loads((HERE/'cases.json').read_text())
    assert {case['id'] for case in cases} == {'mcmc-multimodal-mixing','mcmc-diagnostic-reference'}
    for case in cases:
        assert case['method_ids'] == ['mcmc']
        for key in ['summary','assumptions','algorithm','validation','limits']:
            assert set(case[key]) == {'ja','en'} and all(case[key].values())
        for name in case['code_files']:
            assert (HERE/name).is_file()
