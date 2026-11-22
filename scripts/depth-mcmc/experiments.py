"""Fixed multimodal scenarios and separate independent-diagnostic calibration."""
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from diagnostics import (METRICS, autocovariance, diagnose, direct_autocovariance,
                         split_chains, within_chain_summary)
from fixtures import ar1_chains, edge_fixtures
from sampler import Budget, array_sha256, sample_chains, target_cdf, validate_sampler

HERE = Path(__file__).resolve().parent
REFERENCE_SHA256 = '8383a59e2e23e4c0f6b64560194c9fb0b2c68b2a42f7c4f42d905eac66b2fad4'


def validate(config):
    validate_sampler(config['sampler'])
    for value in config['acceptance'].values():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError('Invalid finite nonnegative acceptance threshold')
    if 'ar1' in config:
        ar = config['ar1']
        if (ar['rhos'] != [-.5, .8] or len(ar['seeds']) != 2 or
            type(ar['chains']) is not int or not 4 <= ar['chains'] <= 16 or
            type(ar['samples']) is not int or not 128 <= ar['samples'] <= 8192 or
            any(type(s) is not int or not 0 <= s < 2**32 for s in ar['seeds']) or
            any(type(lag) is not int or lag < 0 or lag >= ar['samples'] for lag in ar['lags'])):
            raise ValueError('Invalid fixed bounded AR(1) calibration')


def scenario_measurements(x, c):
    dx = diagnose(x)
    mode = (x > 0).astype(float)
    dm = diagnose(mode)
    cdf = np.array([np.mean(x <= point) for point in c['cdf_points']])
    exact = target_cdf(c['cdf_points'], c['mode_distance'], c['component_sigma'])
    transitions = np.sum(np.diff(mode, axis=1) != 0, axis=1)
    return {'mean': float(x.mean()), 'variance': float(x.var()),
            'mean_absolute_error': abs(float(x.mean())),
            'variance_absolute_error': abs(float(x.var())-(c['mode_distance']**2+c['component_sigma']**2)),
            'cdf_max_error': float(np.max(np.abs(cdf-exact))), 'cdf': cdf.tolist(),
            'cdf_points': c['cdf_points'], 'exact_cdf': exact.tolist(), 'cdf_point_errors': (cdf-exact).tolist(),
            'pooled_occupancy': float(mode.mean()), 'per_chain_occupancy': mode.mean(axis=1).tolist(),
            'occupancy_absolute_error': abs(float(mode.mean())-.5),
            'per_chain_transitions': transitions.tolist(),
            'minimum_transitions_per_chain': int(transitions.min()), 'total_transitions': int(transitions.sum()),
            'x_diagnostics': dx, 'mode_diagnostics': dm,
            'within_chain': within_chain_summary(x, c['acf_lags']),
            'array_sha256': array_sha256(x)}


def mixing_case(config, budget=None):
    validate(config);budget = budget or Budget()
    c, a = config['sampler'], config['acceptance']
    records, final_rows, checks, plots = [], [], {}, {}
    max_acov_error = 0.
    for scenario in c['scenarios']:
        for seed in c['seeds']:
            x, acceptance = sample_chains(c, scenario, seed, budget)
            for n in c['budgets']:
                budget.check()
                y = x[:, :n]
                row = {'series': 'scenario-budget', 'scenario': scenario, 'seed': seed, 'draws_per_chain': n,
                       'expected_behavior': 'mixing_check' if scenario == 'mixed' else 'intentional_nonmixing_control',
                       **scenario_measurements(y, c)}
                records.append(row)
                direct = direct_autocovariance(y, c['acf_lags'])
                max_acov_error = max(max_acov_error, float(np.max(np.abs(autocovariance(y)[:, c['acf_lags']]-direct))))
                if n == c['samples']:
                    row['acceptance_per_chain'] = acceptance.tolist();final_rows.append(row)
                    prefix = f'{scenario}-{seed}-'
                    checks[prefix+'acceptance'] = bool(np.all(acceptance >= a['minimum_acceptance']) and np.all(acceptance <= a['maximum_acceptance']))
                    d = row['x_diagnostics']
                    if scenario == 'mixed':
                        for key in ['mean_absolute_error', 'variance_absolute_error', 'cdf_max_error', 'occupancy_absolute_error']:
                            checks[prefix+key] = row[key] <= a['mixed_'+key]
                        checks[prefix+'rank_rhat'] = d['rhat_rank'] is not None and d['rhat_rank'] <= a['mixed_maximum_rhat']
                        for key in ['bulk', 'tail']:
                            checks[prefix+key+'_ess'] = d['ess_'+key] >= a['mixed_minimum_'+key+'_ess']
                        checks[prefix+'mode_ess'] = row['mode_diagnostics']['ess_mean'] is not None and row['mode_diagnostics']['ess_mean'] >= a['mixed_minimum_mode_ess']
                        checks[prefix+'per_chain_mode_transitions'] = row['minimum_transitions_per_chain'] >= a['mixed_minimum_transitions_per_chain']
                    else:
                        checks[prefix+'intentionally_trapped'] = row['total_transitions'] <= a['trapped_maximum_transitions']
                        if scenario == 'dispersed':
                            checks[prefix+'between_chain_failure_detected'] = d['rhat_rank'] >= a['dispersed_minimum_rhat'] and d['ess_bulk'] <= a['dispersed_maximum_bulk_ess']
                            checks[prefix+'mode_variance_failure_explicit'] = row['mode_diagnostics']['status'] == 'infinite_separation'
                        else:
                            checks[prefix+'apparently_benign_diagnostics'] = d['rhat_rank'] <= a['same_mode_maximum_rhat'] and d['ess_bulk'] >= a['same_mode_minimum_bulk_ess']
                            for key in ['cdf', 'mean', 'occupancy']:
                                measure = row[key+'_max_error'] if key == 'cdf' else row[key+'_absolute_error']
                                checks[prefix+'wrong_target_'+key] = measure >= a['same_mode_minimum_'+key+'_error']
                            checks[prefix+'constant_mode_indicator_undefined'] = row['mode_diagnostics']['status'] == 'zero_global_variance'
            if seed == c['seeds'][0]:
                grid = np.linspace(-10, 10, 81)
                plots[scenario] = {'trace': x[:, :1024].tolist(), 'trace_draws': list(range(1024)),
                                   'cdf_x': grid.tolist(), 'cdf': [float(np.mean(x <= z)) for z in grid],
                                   'exact_cdf': target_cdf(grid, c['mode_distance'], c['component_sigma']).tolist(),
                                   'acf_lags': c['acf_lags'], 'within_chain_acf': final_rows[-1]['within_chain']['acf']}
    checks['fft_vs_direct_autocovariance'] = max_acov_error <= a['maximum_fft_direct_acov_error']
    mixed = [r for r in final_rows if r['scenario'] == 'mixed']
    metrics = {'maximum_fft_direct_acov_error': max_acov_error,
               'mixed_maximum_mean_error': max(r['mean_absolute_error'] for r in mixed),
               'mixed_maximum_variance_error': max(r['variance_absolute_error'] for r in mixed),
               'mixed_maximum_cdf_error': max(r['cdf_max_error'] for r in mixed),
               'mixed_maximum_occupancy_error': max(r['occupancy_absolute_error'] for r in mixed),
               'mixed_maximum_rank_rhat': max(r['x_diagnostics']['rhat_rank'] for r in mixed),
               'mixed_minimum_bulk_ess': min(r['x_diagnostics']['ess_bulk'] for r in mixed),
               'mixed_minimum_tail_ess': min(r['x_diagnostics']['ess_tail'] for r in mixed),
               'mixed_minimum_mode_ess': min(r['mode_diagnostics']['ess_mean'] for r in mixed),
               'mixed_minimum_transitions_per_chain': min(r['minimum_transitions_per_chain'] for r in mixed),
               'intentionally_trapped_scenarios': 6.}
    return {'id': 'mcmc-multimodal-mixing', 'passed': all(checks.values()), 'checks': checks,
            'metrics': metrics, 'records': records, 'plot_data': plots,
            'scope': 'Scenario pass means expected behavior was detected; controls do not claim sampler convergence. Prefixes are nested, not independent repetitions.'}


def load_reference(config, reference_path=None):
    path = Path(reference_path) if reference_path is not None else HERE/'reference.json'
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != REFERENCE_SHA256:
        raise ValueError('Independent reference file SHA256 mismatch')
    reference = json.loads(payload)
    if reference['version'] != '0.20.0' or reference['reference'] != 'ArviZ':
        raise ValueError('Unexpected independent diagnostic reference version')
    provenance = reference['provenance']
    if provenance['actually_executed'] is not True or provenance['generator_sha256'] != hashlib.sha256((HERE/'generate-arviz-reference.py').read_bytes()).hexdigest():
        raise ValueError('Independent reference execution/generator binding mismatch')
    upstream = json.loads((HERE/'arviz-upstream-source.json').read_text())
    if provenance['upstream'] != upstream or upstream['commit'] != '94113176cae99a05ba41d1e93739ee2d5bdbe9b1':
        raise ValueError('Independent upstream source binding mismatch')
    for name, value in upstream['files'].items():
        if provenance['environment']['source_sha256'][name] != value['upstream_sha256']:
            raise ValueError('Independent installed source mismatch')
    for name, expected in reference['provenance']['source_sha256'].items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != expected:
            raise ValueError('Reference recipe source hash mismatch: '+name)
    if reference['provenance']['input_sha256'] != hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest():
        raise ValueError('Independent reference input hash mismatch')
    c = config['sampler']
    expected = {f'{scenario}__{seed}__{n}__{observable}': [c['chains'],n]
                for scenario in c['scenarios'] for seed in c['seeds'] for n in c['budgets']
                for observable in ['x','positive_indicator']}
    expected.update({'edge__'+key: list(value.shape) for key,value in edge_fixtures().items()})
    rows = reference['datasets']
    if len(rows) != 62 or len({row['id'] for row in rows}) != 62 or {row['id'] for row in rows} != set(expected):
        raise ValueError('Independent reference dataset completeness mismatch')
    if any(row['shape'] != expected[row['id']] or set(row['metrics']) != set(METRICS) for row in rows):
        raise ValueError('Independent reference shape/metric completeness mismatch')
    return reference


def diagnostic_case(config, budget=None):
    validate(config);budget = budget or Budget()
    reference = load_reference(config)
    arrays = {'edge__'+key: value for key, value in edge_fixtures().items()}
    c, a = config['sampler'], config['acceptance']
    for scenario in c['scenarios']:
        for seed in c['seeds']:
            arrays[f'{scenario}__{seed}'] = sample_chains(c, scenario, seed, budget)[0]
    records, checks = [], {}
    max_rhat, max_ess, max_acov, max_reference_acf = 0., 0., 0., 0.
    counts = {'finite_rhat_comparisons': 0, 'finite_ess_comparisons': 0,
              'global_constant_datasets': 0, 'global_constant_metric_exclusions': 0,
              'exact_row_rhat_policy_checks': 0, 'nonfinite_classification_checks': 0,
              'raw_nonfinite_reference_metrics': 0}
    for entry in reference['datasets']:
        budget.check()
        values = arrays[entry['key']][:, :entry['prefix']]
        if entry['observable'] == 'positive_indicator':
            values = (values > 0).astype(float)
        if list(values.shape) != entry['shape'] or array_sha256(values) != entry['sha256']:
            raise ValueError('Actual regenerated chain differs from independent reference: '+entry['id'])
        measured = diagnose(values)
        globally_constant = bool(np.all(values == values.flat[0]))
        if (measured['status'] == 'zero_global_variance') != globally_constant:
            raise ValueError('Contradictory constant-observable diagnostic status')
        halves = split_chains(values)
        exactly_constant_rows = bool(np.all(halves == halves[:, :1]))
        row = {'series': 'arviz-comparison', 'dataset': entry['id'], 'draws_per_chain': values.shape[1],
               'array_sha256': entry['sha256'], 'atlas_status': measured['status'],
               'comparison_status': {}, 'reference_nonfinite_kinds': {k:v['nonfinite_kind'] for k,v in entry['metrics'].items()}}
        counts['global_constant_datasets'] += measured['status'] == 'zero_global_variance'
        for metric in METRICS:
            ref = entry['metrics'][metric]
            counts['raw_nonfinite_reference_metrics'] += ref['nonfinite_kind'] is not None
            actual = measured[metric]
            row[metric] = actual;row['reference_'+metric] = ref['value']
            if measured['status'] == 'zero_global_variance':
                # ArviZ's raw constant-ESS convention is recorded, not adopted as mixing evidence.
                checks[entry['id']+'-constant-undefined'] = all(measured[k] is None for k in METRICS)
                counts['global_constant_metric_exclusions'] += 1
                row['comparison_status'][metric] = 'global_constant_undefined_policy'
                continue
            if actual is None:
                status = measured['metric_status'][metric]
                if status == 'infinite_separation' and exactly_constant_rows and not globally_constant:
                    # Mathematically W=0. ArviZ can return a huge finite rank-Rhat
                    # from roundoff in var(constant_float); retain the raw value,
                    # classify the exact degeneracy, and do not call it numeric agreement.
                    checks[entry['id']+'-'+metric+'-degeneracy-policy'] = True
                    counts['exact_row_rhat_policy_checks'] += 1
                    row['comparison_status'][metric] = 'exact_zero_within_variance_policy'
                    row['degeneracy_note'] = 'Exact zero within-chain variation: Atlas null/infinite-separation; raw ArviZ may be huge finite or infinity. Not a finite numerical-comparison point.'
                    continue
                checks[entry['id']+'-'+metric] = ref['value'] is None and (
                    (status == 'infinite_separation' and ref['nonfinite_kind'] == 'positive_infinity') or
                    (status == 'zero_variance' and ref['nonfinite_kind'] == 'nan'))
                counts['nonfinite_classification_checks'] += 1
                row['comparison_status'][metric] = 'nonfinite_classification_match'
            else:
                if ref['value'] is None:
                    checks[entry['id']+'-'+metric] = False
                    continue
                difference = abs(actual-ref['value'])
                error = difference if metric.startswith('rhat') else difference/max(abs(ref['value']), 1.)
                limit = a['rhat_absolute_error'] if metric.startswith('rhat') else a['ess_relative_error']
                checks[entry['id']+'-'+metric] = error <= limit
                row['comparison_status'][metric] = 'finite_numeric_comparison'
                if metric.startswith('rhat'):
                    counts['finite_rhat_comparisons'] += 1
                    max_rhat = max(max_rhat, error)
                else:
                    counts['finite_ess_comparisons'] += 1
                    max_ess = max(max_ess, error)
        records.append(row)
        if np.all(np.var(values, axis=1) > 0):
            lags = entry['acf']['lags']
            cov = autocovariance(values)
            acf = cov[:, lags]/cov[:, :1]
            reference_acf = np.asarray(entry['acf']['values'], float)
            error = float(np.max(np.abs(acf-reference_acf)))
            max_reference_acf = max(max_reference_acf, error)
            checks[entry['id']+'-independent-acf'] = error <= a['maximum_fft_direct_acov_error']
    ar = config['ar1'];tau_errors, acf_errors = [], []
    for rho in ar['rhos']:
        for seed in ar['seeds']:
            values = ar1_chains(rho, ar['chains'], ar['samples'], seed)
            cov = autocovariance(values)
            direct = direct_autocovariance(values, ar['lags'])
            max_acov = max(max_acov, float(np.max(np.abs(cov[:, ar['lags']]-direct))))
            empirical_acf = np.mean(cov[:, ar['lags']]/cov[:, :1], axis=0)
            exact_acf = rho**np.asarray(ar['lags'])
            diag = diagnose(values)
            tau = values.size/diag['ess_mean'];exact_tau = (1+rho)/(1-rho)
            tau_error = abs(tau/exact_tau-1);acf_error = float(np.max(np.abs(empirical_acf-exact_acf)))
            tau_errors.append(tau_error);acf_errors.append(acf_error)
            records.append({'series': 'ar1-calibration', 'rho': rho, 'seed': seed, 'exact_stationary_tau': exact_tau,
                            'estimated_mean_tau': tau, 'mean_ess': diag['ess_mean'], 'raw_draws': values.size,
                            'tau_relative_error': tau_error, 'acf_max_error': acf_error,
                            'acf_lags': ar['lags'], 'empirical_acf': empirical_acf.tolist(), 'exact_acf': exact_acf.tolist()})
    fixtures = edge_fixtures()
    iid = diagnose(fixtures['iid']);scale = diagnose(fixtures['scale']);shift = diagnose(fixtures['shift']);anti = diagnose(fixtures['antithetic'])
    checks['iid_effective_size_scale'] = a['iid_minimum_relative_ess'] <= iid['ess_mean']/fixtures['iid'].size <= a['iid_maximum_relative_ess']
    checks['folding_detects_scale_difference'] = scale['rhat_folded'] >= a['scale_minimum_folded_rhat']
    checks['rank_detects_shift'] = shift['rhat_rank'] >= a['shift_minimum_rank_rhat']
    checks['antithetic_ess_can_exceed_draws'] = anti['ess_mean']/fixtures['antithetic'].size >= a['antithetic_minimum_relative_ess']
    checks['ar1_acf'] = max(acf_errors) <= a['ar1_maximum_acf_error']
    checks['ar1_tau'] = max(tau_errors) <= a['ar1_maximum_tau_relative_error']
    checks['ar1_fft_vs_direct'] = max_acov <= a['maximum_fft_direct_acov_error']
    checks['all_reference_metric_slots_accounted_for'] = sum(counts[key] for key in [
        'finite_rhat_comparisons','finite_ess_comparisons','global_constant_metric_exclusions',
        'exact_row_rhat_policy_checks','nonfinite_classification_checks']) == 7*len(reference['datasets'])
    budget.check()
    return {'id': 'mcmc-diagnostic-reference', 'passed': all(checks.values()), 'checks': checks,
            'metrics': {'reference_datasets': float(len(reference['datasets'])), **counts, 'maximum_rhat_absolute_error': max_rhat,
                        'maximum_ess_relative_error': max_ess, 'maximum_fft_direct_acov_error': max_acov,
                        'maximum_independent_acf_error': max_reference_acf,
                        'maximum_ar1_acf_error': max(acf_errors), 'maximum_ar1_tau_relative_error': max(tau_errors)},
            'records': records,
            'scope': 'Same-chain ArviZ0.20.0 values were generated separately; this routine regenerates chains and compares stored references without importing ArviZ.'}


RUNNERS = {'mcmc-multimodal-mixing': mixing_case, 'mcmc-diagnostic-reference': diagnostic_case}
