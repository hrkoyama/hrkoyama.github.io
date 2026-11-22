#!/usr/bin/env python3
"""Plot stored numerical records only; never rerun sampling, ODEs or PDEs."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw(case, output):
    name, rows, metrics = case['id'], case['records'], case['metrics']
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), constrained_layout=True)
    if name == 'gaussian-mcmc':
        cdf = [r for r in rows if 'cdf_point' in r]
        budget = [r for r in rows if 'samples_per_chain' in r]
        axes[0].plot([r['cdf_point'] for r in cdf], [r['normal_cdf'] for r in cdf], 'k--', label='Normal reference')
        axes[0].plot([r['cdf_point'] for r in cdf], [r['empirical_cdf'] for r in cdf], 'o-', label='Metropolis')
        axes[0].set(xlabel='x', ylabel='CDF', title='Stored CDF checkpoints')
        axes[0].legend(fontsize=8)
        axes[1].loglog([r['samples_per_chain'] for r in budget], [r['mean_rmse_across_chains'] for r in budget], 'o-')
        axes[1].set(xlabel='Samples per chain', ylabel='Mean RMSE across 32 chains', title='Fixed-seed budget sequence')
        axes[2].plot([r['samples_per_chain'] for r in budget], [r['ess'] for r in budget], 'o-')
        axes[2].set(xlabel='Samples per chain', ylabel='Mean-observable ESS', title='Initial-positive estimate')
    elif name == 'langevin-harmonic':
        steps = [r['dt'] for r in rows]
        axes[0].loglog(steps, [r['discrete_covariance_bias'] for r in rows], 'o-', label='Discrete stationary bias')
        axes[0].loglog(steps, [r['covariance_sampling_error'] for r in rows], 's-', label='Sample vs discrete reference')
        axes[0].set(xlabel='dt', ylabel='Max covariance difference', title='Bias and sampling are separate')
        axes[0].legend(fontsize=7)
        for key, label in [('position_cdf_error', 'Position'), ('momentum_cdf_error', 'Momentum'), ('energy_cdf_error', 'Energy')]:
            axes[1].plot(steps, [r[key] for r in rows], 'o-', label=label)
        axes[1].set(xlabel='dt', ylabel='ECDF sup error', title='Canonical-distribution checks')
        axes[1].legend(fontsize=8)
        for key, label, style in [('q_correlation_sample', 'Replicas', 'o-'), ('q_correlation_discrete', 'Discrete map', 's--'), ('q_correlation_continuum', 'Continuous reference', 'k:')]:
            axes[2].plot(steps, [r[key] for r in rows], style, label=label)
        axes[2].set(xlabel='dt', ylabel='Position correlation, lag 2', title='Time correlation')
        axes[2].legend(fontsize=7)
    elif name == 'reaction-diffusion-fourier':
        space = [r for r in rows if r['sequence'] == 'space']
        time = [r for r in rows if r['sequence'] == 'time']
        axes[0].loglog([r['n'] for r in space], [r['max_error'] for r in space], 'o-')
        axes[0].set(xlabel='Spatial cells', ylabel='Max error vs continuum', title='Second-order space')
        axes[1].loglog([r['dt'] for r in time], [r['max_error'] for r in time], 'o-')
        axes[1].set(xlabel='dt', ylabel='Max error vs semidiscrete exact', title='Fourth-order time')
        axes[2].bar(['Space', 'Time'], [metrics['spatial_minimum_order'], metrics['temporal_minimum_order']])
        axes[2].set(ylabel='Minimum observed order', title='Separate refinement axes', ylim=(0, 4.5))
    elif name == 'turing-schnakenberg':
        space = [r for r in rows if r['sequence'] == 'linear-space']
        profile = [r for r in rows if r['sequence'] == 'nonlinear-profile']
        axes[0].loglog([r['n'] for r in space], [r['max_error'] for r in space], 'o-')
        axes[0].set(xlabel='Spatial cells', ylabel='Error / initial amplitude', title='Linear mode vs matrix exponential')
        axes[1].plot([r['n'] for r in space], [r['growth_rate'] for r in space], 'o-', label='FD/RK4 growth')
        axes[1].axhline(metrics['continuum_mode_growth_rate'], linestyle='--', color='k', label='Continuum reference')
        axes[1].set(xlabel='Spatial cells', ylabel='Growth rate', title='Diffusion-driven growth')
        axes[1].legend(fontsize=8)
        axes[2].plot([r['x'] for r in profile], [r['u']-1 for r in profile], label='u-1')
        axes[2].plot([r['x'] for r in profile], [r['v']-.9 for r in profile], label='v-0.9')
        axes[2].set(xlabel='x', ylabel='Small nonlinear perturbation', title='Early pattern, t=4')
        axes[2].legend(fontsize=8)
    elif name == 'fitzhugh-nagumo':
        time = [r for r in rows if r['sequence'] == 'time']
        trajectory = [r for r in rows if r['sequence'] == 'trajectory']
        axes[0].plot([r['t'] for r in trajectory], [r['reference_v'] for r in trajectory], 'k--', label='DOP853')
        axes[0].plot([r['t'] for r in trajectory], [r['v'] for r in trajectory], label='RK4 finest')
        axes[0].axvspan(10, 20, alpha=.1, label='Current pulse')
        axes[0].set(xlabel='Dimensionless time', ylabel='v', title='Excitation and recovery')
        axes[0].legend(fontsize=7)
        axes[1].loglog([r['dt'] for r in time], [r['max_error'] for r in time], 'o-')
        axes[1].set(xlabel='dt', ylabel='Max error vs DOP853', title='Temporal convergence')
        axes[2].plot([r['t'] for r in trajectory], [abs(r['v']-r['reference_v']) for r in trajectory])
        axes[2].set(xlabel='Dimensionless time', ylabel='Absolute v error', title='All output-time comparison')
    else:
        raise ValueError('Unknown case '+name)
    for ax in axes:
        ax.grid(alpha=.2)
    fig.savefig(output/(name+'.png'), dpi=140)
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = json.loads(Path(args.results).read_text())
    if not result['passed']:
        raise ValueError('Refuse to illustrate an unaccepted run as verified')
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    for case in result['cases']:
        draw(case, output)
