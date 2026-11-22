"""Preregistered finite kinetic convergence and uncertainty experiments.

Inputs and acceptance live in kinetic-design.json; this module never tunes them.
Random-particle observations within a seed are correlated. Uncertainty below
always uses independent seed-level statistics, never an iid-particle KS test.
"""
from math import pi

import numpy as np
from scipy.special import gammainc

from kinetics import (absorption_slab, cic_state, elastic_round, microcanonical_energy_cdf,
                      microcanonical_fourth, microcanonical_sample, photon_survival,
                      plasma_dop853, plasma_verlet, slab_references)


def _case(identifier, checks, metrics, records):
    checks = {key: bool(value) for key, value in checks.items()}
    metrics = {key: float(value) for key, value in metrics.items()}
    if not checks or not metrics or not records or not all(np.isfinite(list(metrics.values()))):
        raise ValueError('Case requires nonempty checks, finite metrics and records')
    return dict(id=identifier, passed=bool(all(checks.values())), checks=checks,
                metrics=metrics, records=records)


def _mean_se(values):
    values = np.asarray(values, dtype=float)
    if len(values) < 2 or not np.isfinite(values).all():
        raise ValueError('At least two finite independent replicate observations required')
    return np.mean(values, axis=0), np.std(values, axis=0, ddof=1)/np.sqrt(len(values))


def _standardized(difference, standard_error):
    difference, standard_error = np.broadcast_arrays(np.abs(difference), standard_error)
    result = np.zeros_like(difference, dtype=float)
    np.divide(difference, standard_error, out=result, where=standard_error > 0)
    result[(standard_error == 0) & (difference != 0)] = np.finfo(float).max
    return result


def pic_case(c):
    a = c['acceptance']
    records = []
    mesh_runs = []
    for grid in c['mesh_grids']:
        result = plasma_verlet(grid, c['mesh_particles'], c['mesh_dt'], c['end_time'], c['amplitude'])
        mesh_runs.append(result)
        records.append(dict(series='mesh', grid=grid, particles=c['mesh_particles'],
                            particles_per_cell=result['particles_per_cell'], dt=result['dt'],
                            mode_error=result['max_mode_error'], charge_error=result['charge_error'],
                            momentum_error=result['momentum_error'],
                            resolved_gauss_error=result['resolved_gauss_error'],
                            nyquist_charge=result['nyquist_charge'],
                            relative_energy_drift=result['relative_energy_drift']))
    mesh_ratios = [left['max_mode_error']/right['max_mode_error']
                   for left, right in zip(mesh_runs[:-1], mesh_runs[1:])]
    for row in mesh_runs[-1]['records']:
        records.append(dict(series='trajectory', grid=c['mesh_grids'][-1], **row))
    references = [plasma_dop853(c['time_grid'], c['time_particles'], c['end_time'], c['amplitude'],
                                c['reference_rtol'], c['reference_atol'], max_step)
                  for max_step in c['reference_max_steps']]
    reference = references[-1]
    sensitivity = max(abs(references[0]['mode']-reference['mode']),
                      np.max(abs(references[0]['final_position']-reference['final_position']))/c['amplitude'],
                      np.max(abs(references[0]['final_velocity']-reference['final_velocity']))/c['amplitude'])
    for max_step, result in zip(c['reference_max_steps'], references):
        records.append(dict(series='time-reference', max_step=max_step,
                            rtol=c['reference_rtol'], atol=c['reference_atol'],
                            mode=result['mode'], evaluations=result['evaluations']))
    time_runs = []
    time_errors = []
    for dt in c['time_steps']:
        result = plasma_verlet(c['time_grid'], c['time_particles'], dt, c['end_time'], c['amplitude'])
        time_runs.append(result)
        error = abs(result['records'][-1]['mode']-reference['mode'])
        time_errors.append(error)
        records.append(dict(series='time', grid=c['time_grid'], particles=c['time_particles'],
                            dt=result['dt'], mode=result['records'][-1]['mode'],
                            reference_mode=reference['mode'], mode_error=error,
                            relative_energy_drift=result['relative_energy_drift']))
    time_orders = [np.log(left/right)/np.log(c['time_steps'][i]/c['time_steps'][i+1])
                   for i, (left, right) in enumerate(zip(time_errors[:-1], time_errors[1:]))]
    shot_rms = []
    grid_shot_rms = []
    scaled_powers = []
    scaled_grid_powers = []
    grid_expectation = (2+np.cos(2*pi/c['shot_grid']))/3
    for level, particles in enumerate(c['shot_particle_counts']):
        powers, grid_powers, fields = [], [], []
        for replicate in range(c['shot_seeds']):
            seed = c['shot_seed_start']+1000*level+replicate
            positions = np.random.default_rng(seed).uniform(0., 2*pi, particles)
            power = float(abs(np.mean(np.exp(1j*positions)))**2)
            _, state = cic_state(positions, c['shot_grid'])
            powers.append(power)
            grid_powers.append(state['grid_charge_mode_power'])
            fields.append(state['grid_field_rms'])
            records.append(dict(series='shot-seed', particles=particles, grid=c['shot_grid'],
                                seed=seed, particle_mode_power=power,
                                grid_mode_power=state['grid_charge_mode_power'],
                                grid_field_rms=state['grid_field_rms']))
        rms, grid_rms = float(np.sqrt(np.mean(powers))), float(np.sqrt(np.mean(grid_powers)))
        shot_rms.append(rms)
        grid_shot_rms.append(grid_rms)
        scaled = particles*np.mean(powers)
        grid_scaled = particles*np.mean(grid_powers)/grid_expectation
        scaled_powers.append(scaled)
        scaled_grid_powers.append(grid_scaled)
        records.append(dict(series='shot-noise', particles=particles, grid=c['shot_grid'],
                            seeds=c['shot_seeds'], particle_mode_rms=rms, grid_mode_rms=grid_rms,
                            normalized_particle_mode_power=float(scaled),
                            normalized_grid_mode_power=float(grid_scaled),
                            exact_grid_power_factor=float(grid_expectation),
                            mean_grid_field_rms=float(np.mean(fields))))
    reductions = [x/y for x, y in zip(shot_rms[:-1], shot_rms[1:])]
    grid_reductions = [x/y for x, y in zip(grid_shot_rms[:-1], grid_shot_rms[1:])]
    all_runs = mesh_runs+time_runs
    metrics = dict(finest_mesh_mode_error=mesh_runs[-1]['max_mode_error'],
                   minimum_mesh_error_ratio=min(mesh_ratios), minimum_time_order=min(time_orders),
                   finest_time_mode_error=time_errors[-1], reference_sensitivity=sensitivity,
                   charge_error=max(r['charge_error'] for r in all_runs),
                   momentum_error=max(r['momentum_error'] for r in all_runs),
                   resolved_gauss_error=max(r['resolved_gauss_error'] for r in all_runs),
                   nyquist_charge=max(r['nyquist_charge'] for r in all_runs),
                   relative_energy_drift=max(r['relative_energy_drift'] for r in all_runs),
                   minimum_shot_scaled_power=min(scaled_powers+scaled_grid_powers),
                   maximum_shot_scaled_power=max(scaled_powers+scaled_grid_powers),
                   minimum_shot_rms_reduction=min(reductions+grid_reductions))
    checks = dict(continuum_reference=metrics['finest_mesh_mode_error'] <= a['finest_continuum_mode_error_max'],
                  mesh_convergence=metrics['minimum_mesh_error_ratio'] >= a['mesh_error_ratio_min'],
                  time_convergence=metrics['minimum_time_order'] >= a['time_order_min'],
                  independent_time_reference=metrics['reference_sensitivity'] <= a['reference_mode_sensitivity_max'],
                  charge=metrics['charge_error'] <= a['charge_max'],
                  momentum=metrics['momentum_error'] <= a['momentum_max'],
                  resolved_gauss=metrics['resolved_gauss_error'] <= a['resolved_gauss_max'],
                  nyquist_charge=metrics['nyquist_charge'] <= a['nyquist_charge_max'],
                  measured_energy_drift=metrics['relative_energy_drift'] <= a['relative_energy_drift_max'],
                  shot_noise_power=a['shot_scaled_power_min'] <= metrics['minimum_shot_scaled_power']
                                  and metrics['maximum_shot_scaled_power'] <= a['shot_scaled_power_max'],
                  shot_noise_scaling=metrics['minimum_shot_rms_reduction'] >= a['shot_rms_reduction_min'])
    return _case('pic-conservation', checks, metrics, records)


def dsmc_case(c):
    a = c['acceptance']
    points = np.asarray(c['cdf_energy_points'])
    records = []
    momentum_error = energy_error = anisotropy_z = cdf_z = sample_z = fourth_z = 0.
    mean_cdf_standard_errors = []
    finite_bias = []
    for level, particles in enumerate(c['particle_counts']):
        initial = np.zeros((particles, 3))
        initial[:, 0] = np.tile([-np.sqrt(3), np.sqrt(3)], particles//2)
        histories, cdfs, fourths, independent_cdfs, independent_fourths = [], [], [], [], []
        for replicate in range(c['seeds']):
            seed = c['seed_start']+1000*level+replicate
            rng = np.random.default_rng(seed)
            v = initial.copy()
            energy = float(np.sum(v*v))
            history = []
            for round_index in range(c['collision_rounds']+1):
                covariance = np.mean(v*v, axis=0)
                if round_index <= c['anisotropy_rounds']:
                    history.append(float(covariance[0]-.5*(covariance[1]+covariance[2])))
                momentum_error = max(momentum_error, float(np.max(abs(v.sum(axis=0)))/particles))
                energy_error = max(energy_error, float(abs(np.sum(v*v)-energy)/energy))
                if round_index < c['collision_rounds']:
                    elastic_round(v, rng)
            histories.append(history)
            cdf = np.mean((.5*np.sum(v*v, axis=1))[:, None] <= points, axis=0)
            fourth = float(np.mean(v[:, 0]**4))
            cdfs.append(cdf)
            fourths.append(fourth)
            eq_seed = c['equilibrium_seed_start']+1000*level+replicate
            independent = microcanonical_sample(particles, np.random.default_rng(eq_seed))
            eq_cdf = np.mean((.5*np.sum(independent*independent, axis=1))[:, None] <= points, axis=0)
            independent_cdfs.append(eq_cdf)
            independent_fourths.append(float(np.mean(independent[:, 0]**4)))
            records.append(dict(series='dsmc-seed', particles=particles, seed=seed,
                                equilibrium_seed=eq_seed, fourth_moment=fourth,
                                independent_fourth_moment=independent_fourths[-1]))
            for index, point in enumerate(points):
                records.append(dict(series='cdf-seed', particles=particles, seed=seed,
                                    equilibrium_seed=eq_seed, energy=float(point),
                                    cdf=float(cdf[index]), independent_cdf=float(eq_cdf[index])))
        expected_cdf = microcanonical_energy_cdf(points, particles)
        maxwell_cdf = gammainc(1.5, points)
        finite_bias.append(float(np.max(abs(expected_cdf-maxwell_cdf))))
        mean_cdf, se_cdf = _mean_se(cdfs)
        eq_mean, eq_se = _mean_se(independent_cdfs)
        mean_cdf_standard_errors.append(float(np.mean(se_cdf)))
        cdf_z = max(cdf_z, float(np.max(_standardized(mean_cdf-expected_cdf, se_cdf))),
                    float(np.max(_standardized(eq_mean-expected_cdf, eq_se))))
        sample_z = max(sample_z, float(np.max(_standardized(mean_cdf-eq_mean, np.hypot(se_cdf, eq_se)))))
        for index, point in enumerate(points):
            records.append(dict(series='cdf', particles=particles, energy=float(point), seeds=c['seeds'],
                                mean=float(mean_cdf[index]), standard_error=float(se_cdf[index]),
                                exact_finite_n=float(expected_cdf[index]), maxwell_limit=float(maxwell_cdf[index]),
                                independent_mean=float(eq_mean[index]), independent_standard_error=float(eq_se[index]),
                                replicate_rmse=float(np.sqrt(np.mean((np.asarray(cdfs)[:, index]-expected_cdf[index])**2)))))
        fourth_mean, fourth_se = _mean_se(fourths)
        eq_fourth_mean, eq_fourth_se = _mean_se(independent_fourths)
        exact_fourth = microcanonical_fourth(particles)
        fourth_z = max(fourth_z, float(_standardized(fourth_mean-exact_fourth, fourth_se)),
                       float(_standardized(eq_fourth_mean-exact_fourth, eq_fourth_se)))
        records.append(dict(series='fourth-moment', particles=particles, seeds=c['seeds'],
                            mean=float(fourth_mean), standard_error=float(fourth_se),
                            exact_finite_n=exact_fourth, maxwell_limit=3.,
                            independent_mean=float(eq_fourth_mean), independent_standard_error=float(eq_fourth_se)))
        factor = (particles-2)/(2*(particles-1))
        history_mean, history_se = _mean_se(histories)
        expected = 3*factor**np.arange(c['anisotropy_rounds']+1)
        # Round zero is deterministic and has no sampling standard error.
        anisotropy_z = max(anisotropy_z, float(np.max(_standardized(history_mean[1:]-expected[1:], history_se[1:]))))
        for index, exact in enumerate(expected):
            records.append(dict(series='anisotropy', particles=particles, round=index, seeds=c['seeds'],
                                mean=float(history_mean[index]), standard_error=float(history_se[index]), expected=float(exact)))
    se_reduction = mean_cdf_standard_errors[0]/mean_cdf_standard_errors[-1]
    metrics = dict(momentum_error=momentum_error, relative_energy_error=energy_error,
                   anisotropy_standard_errors=anisotropy_z, cdf_standard_errors=cdf_z,
                   independent_equilibrium_standard_errors=sample_z, fourth_standard_errors=fourth_z,
                   maximum_finite_n_maxwell_cdf_bias=max(finite_bias),
                   cdf_seed_standard_error_reduction=se_reduction)
    checks = dict(momentum=momentum_error <= a['momentum_max'],
                  energy=energy_error <= a['relative_energy_max'],
                  analytic_anisotropy=anisotropy_z <= a['anisotropy_standard_errors_max'],
                  exact_finite_n_cdf=cdf_z <= a['cdf_standard_errors_max'],
                  independent_equilibrium=sample_z <= a['independent_sample_standard_errors_max'],
                  finite_n_fourth_moment=fourth_z <= a['fourth_standard_errors_max'],
                  finite_n_distinct_from_maxwell=max(finite_bias) >= a['finite_n_maxwell_cdf_bias_min'],
                  statistical_error_scaling=se_reduction >= a['cdf_seed_standard_error_reduction_min'])
    return _case('dsmc-statistics', checks, metrics, records)


def radiation_case(c):
    a = c['acceptance']
    records = []
    reference_difference = quad_error = balance = finest_space = finest_angle = mean_z = 0.
    minimum_intensity, maximum_intensity = 1., 0.
    orders, angular_reductions, rmse_ratios, coverages, rmse_reductions = [], [], [], [], []
    for level, depth in enumerate(c['optical_depths']):
        reference = slab_references(depth, c['quad_epsabs'], c['quad_epsrel'])
        reference_difference = max(reference_difference, abs(reference['quad_flux']-reference['expn_flux']))
        quad_error = max(quad_error, reference['quad_error'])
        records.append(dict(series='characteristic-reference', optical_depth=depth, **reference))
        spatial_errors = []
        for cells in c['spatial_cells']:
            result = absorption_slab(cells, c['spatial_ordinates'], depth)
            spatial_errors.append(result['spatial_flux_error'])
            balance = max(balance, result['balance_error'])
            minimum_intensity = min(minimum_intensity, result['minimum_intensity'])
            maximum_intensity = max(maximum_intensity, result['maximum_intensity'])
            records.append(dict(series='space', optical_depth=depth, cells=cells,
                                ordinates=c['spatial_ordinates'], **result))
        finest_space = max(finest_space, spatial_errors[-1])
        orders.extend(np.log(left/right)/np.log(c['spatial_cells'][i+1]/c['spatial_cells'][i])
                      for i, (left, right) in enumerate(zip(spatial_errors[:-1], spatial_errors[1:])))
        angular_errors = []
        for ordinates in c['angular_ordinates']:
            result = absorption_slab(1, ordinates, depth, 'characteristic')
            error = abs(result['flux']-reference['quad_flux'])
            angular_errors.append(error)
            balance = max(balance, result['balance_error'])
            records.append(dict(series='angle', optical_depth=depth, ordinates=ordinates,
                                angular_flux_error=error, reference_flux=reference['quad_flux'], **result))
        finest_angle = max(finest_angle, angular_errors[-1])
        angular_reductions.append(angular_errors[0]/max(angular_errors[-1], np.finfo(float).eps))
        expected = reference['expn_flux']/pi
        rmses = []
        for history_level, histories in enumerate(c['mc_histories']):
            probabilities, covered = [], []
            for replicate in range(c['mc_seeds']):
                seed = c['mc_seed_start']+10000*level+1000*history_level+replicate
                result = photon_survival(histories, depth, np.random.default_rng(seed), c['mc_confidence'])
                probabilities.append(result['survival'])
                covered.append(result['lower'] <= expected <= result['upper'])
                balance = max(balance, abs(result['count_balance'])/histories)
                records.append(dict(series='photon-seed', optical_depth=depth, histories=histories,
                                    seed=seed, expected_survival=expected,
                                    covered=bool(covered[-1]), **result))
            mean, se = _mean_se(probabilities)
            theoretical = np.sqrt(expected*(1-expected)/histories)
            rmse = float(np.sqrt(np.mean((np.asarray(probabilities)-expected)**2)))
            rmses.append(rmse)
            rmse_ratios.append(rmse/theoretical)
            coverage = float(np.mean(covered))
            coverages.append(coverage)
            mean_z = max(mean_z, float(_standardized(mean-expected, theoretical/np.sqrt(c['mc_seeds']))))
            records.append(dict(series='photon-statistics', optical_depth=depth, histories=histories,
                                seeds=c['mc_seeds'], survival_mean=float(mean), empirical_mean_standard_error=float(se),
                                exact_survival=expected, rmse=rmse, binomial_standard_deviation=float(theoretical),
                                exact_mean_standard_error=float(theoretical/np.sqrt(c['mc_seeds'])),
                                confidence=c['mc_confidence'], measured_coverage=coverage,
                                flux_mean=float(pi*mean)))
        rmse_reductions.extend(left/right for left, right in zip(rmses[:-1], rmses[1:]))
    metrics = dict(reference_difference=reference_difference, quad_reported_error=quad_error,
                   minimum_spatial_order=min(orders), finest_spatial_flux_error=finest_space,
                   finest_angular_flux_error=finest_angle, minimum_angular_reduction=min(angular_reductions),
                   balance_error=balance, minimum_intensity=minimum_intensity, maximum_intensity=maximum_intensity,
                   mc_mean_standard_errors=mean_z, minimum_mc_rmse_ratio=min(rmse_ratios),
                   maximum_mc_rmse_ratio=max(rmse_ratios), minimum_measured_coverage=min(coverages),
                   minimum_mc_rmse_reduction=min(rmse_reductions))
    checks = dict(independent_characteristic_reference=reference_difference <= a['reference_difference_max'],
                  reference_quadrature_error=quad_error <= a['quad_reported_error_max'],
                  spatial_convergence=min(orders) >= a['spatial_order_min'],
                  spatial_accuracy=finest_space <= a['finest_spatial_flux_error_max'],
                  angular_accuracy=finest_angle <= a['finest_angular_flux_error_max'],
                  angular_convergence=min(angular_reductions) >= a['angular_overall_reduction_min'],
                  balance=balance <= a['balance_max'],
                  positivity=a['intensity_min'] <= minimum_intensity and maximum_intensity <= a['intensity_max'],
                  mc_mean=mean_z <= a['mc_mean_standard_errors_max'],
                  mc_binomial_error=a['mc_rmse_to_binomial_min'] <= min(rmse_ratios)
                                    and max(rmse_ratios) <= a['mc_rmse_to_binomial_max'],
                  mc_coverage=min(coverages) >= a['mc_coverage_min'],
                  mc_statistical_scaling=min(rmse_reductions) >= a['mc_rmse_reduction_min'])
    return _case('radiation-convergence', checks, metrics, records)
