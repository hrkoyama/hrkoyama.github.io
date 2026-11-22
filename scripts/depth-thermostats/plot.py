#!/usr/bin/env python3
"""Render figures from stored result.json only; never rerun the experiments."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COLORS = {'csvr': '#235b83', 'langevin': '#ad5c2c'}


def draw(data, output):
    output = Path(output);output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 11})
    for case in data['cases']:
        if case['id'] == 'csvr-kinetic-kernel':
            fig, axes = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
            for dof in [1, 2, 6]:
                rows = [r for r in case['records'] if r['series'] == 'stationary-acf' and r['dof'] == dof]
                x = [r['lag'] for r in rows]
                axes[0].errorbar(x, [r['measured_acf'] for r in rows],
                                 yerr=[2*r['acf_standard_error'] for r in rows], marker='o',
                                 capsize=2, label=f'CSVR Nf={dof}')
                if dof == 1:
                    axes[0].plot(x, [r['exact_acf'] for r in rows], 'k--', label='Exact bath exp(-t/tau)')
                axes[1].plot(x, [r['sample_variance']/r['exact_variance'] for r in rows],
                             marker='o', label=f'CSVR Nf={dof}')
            axes[1].axhline(1, color='k', linestyle='--', label='Canonical variance')
            axes[0].set(xlabel='Lag time (reduced units)', ylabel='Normalized K correlation', title='Bath-only kinetic correlation; error bars +/-2 SE')
            axes[1].set(xlabel='Time (reduced units)', ylabel='Var(K) / [Nf T^2/2]', title='Kinetic fluctuations across degree counts')
            for ax in axes:ax.legend(fontsize=8);ax.grid(alpha=.2)
        else:
            fig, axes = plt.subplots(2, 3, figsize=(13, 7.2), constrained_layout=True)
            ref = case['canonical_reference']
            distribution = [r for r in case['records'] if r['series'] == 'distribution' and r['initial_ensemble'] == 'canonical']
            q_points = np.array([-2., -1., 0., 1., 2.]);e_points = np.array([.5, 1., 2., 4., 6.])
            axes[0, 0].plot(q_points, ref['position_cdf'][0], 'k--', label='Boltzmann reference')
            axes[0, 1].plot(e_points, ref['energy_cdf'], 'k--', label='Canonical H reference')
            for method in ['csvr', 'langevin']:
                row = next(r for r in distribution if r['method'] == method and r['tau'] == 1. and r['dt'] == .05)
                axes[0, 0].plot(q_points, np.array(row['q_cdf'])[0], 'o-', color=COLORS[method], label=method.upper())
                axes[0, 1].plot(e_points, row['h_cdf'], 'o-', color=COLORS[method], label=method.upper())
                for tau, style in [(.25, '-'), (1., '--')]:
                    rows = [r for r in case['records'] if r['series'] == 'correlation' and r['method'] == method and r['tau'] == tau and r['dt'] == .05]
                    x = np.array([r['lag'] for r in rows])
                    for ax, observable in [(axes[1, 0], 'q'), (axes[1, 1], 'h')]:
                        y = np.array([r[observable+'_acf'] for r in rows]);error = np.array([r[observable+'_acf_standard_error'] for r in rows])
                        ax.plot(x, y, style, marker='o', color=COLORS[method], label=f'{method.upper()}, tau={tau}')
                        ax.fill_between(x, y-2*error, y+2*error, color=COLORS[method], alpha=.10)
                    selected = [r for r in distribution if r['method'] == method and r['tau'] == tau]
                    axes[1, 2].plot([r['dt'] for r in selected], [max(r[k] for k in r if k.endswith('_cdf_error')) for r in selected],
                                    style, marker='o', color=COLORS[method], label=f'{method.upper()}, tau={tau}')
            labels, variances = [], []
            for method in ['csvr', 'langevin']:
                for tau in [.25, 1.]:
                    row = next(r for r in distribution if r['method'] == method and r['tau'] == tau and r['dt'] == .05)
                    labels.append(f'{method.upper()}\ntau={tau}');variances.append(row['temperature_variance'])
            axes[0, 2].bar(np.arange(4), variances, color=[COLORS['csvr']]*2+[COLORS['langevin']]*2)
            axes[0, 2].axhline(1, color='k', linestyle='--', label='Canonical T variance')
            axes[0, 2].set_xticks(np.arange(4), labels, fontsize=8)
            axes[0, 0].set(xlabel='q_1 (reduced units)', ylabel='P(q_1 <= q)', title='Position CDF at h=.05, tau=1')
            axes[0, 1].set(xlabel='Physical H (reduced energy)', ylabel='P(H <= E)', title='Physical total-energy CDF at h=.05, tau=1')
            axes[0, 2].set(xlabel='Thermostat / coupling', ylabel='Var(Tinst), reduced temperature^2', title='Temperature fluctuations: Nf=2, target T=1')
            axes[1, 0].set(xlabel='Lag time (reduced units)', ylabel='q correlation / canonical variance', title='Position correlation; shaded +/-2 replica SE')
            axes[1, 1].set(xlabel='Lag time (reduced units)', ylabel='H correlation / canonical variance', title='Energy correlation; global/local need not match')
            axes[1, 2].set(xlabel='Timestep h (reduced time)', ylabel='Maximum declared-point CDF error', title='Step comparison includes sampling error')
            for ax in axes.ravel():ax.legend(fontsize=7);ax.grid(alpha=.2)
        fig.suptitle(case['id']+' — fixed seeds; see JSON for heated starts and all records', fontsize=11)
        fig.savefig(output/(case['id']+'.png'), dpi=130)
        plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args();draw(json.loads(Path(args.results).read_text()), args.output)
