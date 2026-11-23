#!/usr/bin/env python3
"""Render only the saved JSON/NPZ results; never run either PDE solver."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def plot(results, output):
    path = Path(results); output = Path(output); output.mkdir(parents=True, exist_ok=True)
    data = json.loads(path.read_text()); by_id = {c['id']: c for c in data['cases']}
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'axes.labelsize': 11})
    sem = by_id['sem-poisson-2d']
    with np.load(path.parent/'sem-poisson-2d.npz') as fields:
        fig, axes = plt.subplots(2, 2, figsize=(11, 8.4), constrained_layout=True)
        for ax, z, title, cmap in [(axes[0, 0], fields['sem'], 'Computed 2D GLL-SEM solution (8 x 8 elements, p=2)', 'viridis'),
                                   (axes[0, 1], fields['sem']-fields['reference'], 'Nodal error; acceptance uses continuous error norms', 'RdBu_r')]:
            image = ax.pcolormesh(fields['x'], fields['y'], z, shading='gouraud', cmap=cmap)
            fig.colorbar(image, ax=ax, shrink=.8); ax.set(xlabel='x', ylabel='y', aspect='equal', title=title)
        for method, label in [('GLL-SEM', 'GLL-SEM, p=2'), ('published-P1-FEM', 'Published triangle P1 FEM')]:
            rows = [r for r in sem['records'] if r['series'] == 'h' and r['method'] == method]
            axes[1, 0].loglog([r['free_dofs'] for r in rows], [r['l2_error'] for r in rows], 'o-', label=label)
        axes[1, 0].set(xlabel='Free unknowns (matched counts)', ylabel='Continuous L2 error', title='Same PDE and Dirichlet data; different spaces/meshes')
        axes[1, 0].legend(); axes[1, 0].grid(alpha=.2)
        rows = [r for r in sem['records'] if r['series'] == 'p']
        axes[1, 1].semilogy([r['degree'] for r in rows], [r['l2_error'] for r in rows], 'o-', label='L2')
        axes[1, 1].semilogy([r['degree'] for r in rows], [r['h1_seminorm_error'] for r in rows], 's--', label='H1 seminorm')
        axes[1, 1].set(xlabel='Polynomial degree p', ylabel='Continuous error', title='p refinement at fixed 2 x 2 elements')
        axes[1, 1].legend(); axes[1, 1].grid(alpha=.2)
        fig.suptitle('Spectral elements: smooth manufactured Poisson solution\nGLL quadrature; independent Gauss error integration; no Nek solver executed', fontsize=14)
        fig.savefig(output/'sem-poisson-2d.png', dpi=150); plt.close(fig)
    fr = by_id['fr-periodic-advection']
    with np.load(path.parent/'fr-periodic-advection.npz') as fields:
        fig, axes = plt.subplots(2, 2, figsize=(11, 8.4), constrained_layout=True)
        x = fields['x'].ravel()
        axes[0, 0].plot(x, fields['initial'].ravel(), ':', color='gray', label='Initial projection')
        axes[0, 0].plot(x, fields['reference'].ravel(), 'k-', label='Analytic at T=0.25')
        axes[0, 0].plot(x, fields['fr'].ravel(), '.', color='#a45730', label='FR, p=2, 32 cells', markersize=4)
        axes[0, 0].set(xlabel='x', ylabel='u', title='An actual quarter-period translation'); axes[0, 0].legend()
        axes[0, 1].plot(x, (fields['fr']-fields['dg']).ravel(), '.', label='FR minus published modal DG')
        axes[0, 1].set(xlabel='x', ylabel='Difference', title='Radau corrections recover this linear DG scheme'); axes[0, 1].ticklabel_format(axis='y', style='sci', scilimits=(0, 0)); axes[0, 1].legend()
        for p in [1, 2]:
            rows = [r for r in fr['records'] if r['degree'] == p]
            axes[1, 0].loglog([r['cells'] for r in rows], [r['l2_error'] for r in rows], 'o-', label='p='+str(p)+', SSPRK3')
            axes[1, 0].loglog([r['cells'] for r in rows], [r['exponential_l2_error'] for r in rows], 'x--', label='p='+str(p)+', matrix exponential')
        axes[1, 0].set(xlabel='Cells', ylabel='Continuous L2 error', title='Analytic error; same spatial operator in dashed lines'); axes[1, 0].legend(fontsize=9); axes[1, 0].grid(alpha=.2)
        history = fr['mass_energy_histories'][-1]['samples']
        axes[1, 1].plot([r['time'] for r in history], [r['mass']-history[0]['mass'] for r in history], label='Mass minus initial')
        axes[1, 1].set(xlabel='Time', ylabel='Mass change', title='Periodic conservation; all stages are also checked'); axes[1, 1].legend(); axes[1, 1].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
        fig.suptitle('Flux reconstruction: constant-speed periodic advection\nGauss points + Radau correction + SSPRK3; no PyFR solver executed', fontsize=14)
        fig.savefig(output/'fr-periodic-advection.png', dpi=150); plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--results', required=True); parser.add_argument('--output', required=True)
    args = parser.parse_args(); plot(args.results, args.output)
