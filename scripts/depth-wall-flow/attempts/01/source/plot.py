#!/usr/bin/env python3
"""Scientific main and gallery figures from actual saved fields, no solver run."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from references.qualify_reference import ghia


def save(fig, directory, stem):
    for ext in ['png', 'svg', 'pdf']:
        fig.savefig(directory/(stem+'.'+ext), dpi=160, bbox_inches='tight')
    plt.close(fig)


def field(ax, d, title, error=False):
    speed = np.hypot(d['u'], d['v'])
    z = np.hypot(d['u']-d['u_exact'], d['v']-d['v_exact']) if error else speed
    artist = ax.pcolormesh(d['x'], d['y'], z, shading='auto', cmap='magma' if error else 'viridis')
    ax.streamplot(d['x'], d['y'], d['u'], d['v'], color='white', linewidth=.65, density=1.15, arrowsize=.8)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel='x', ylabel='y', title=title, aspect='equal')
    return artist


def main():
    p = argparse.ArgumentParser(); p.add_argument('--results', type=Path, required=True); p.add_argument('--output', type=Path, required=True); args = p.parse_args()
    result = json.loads(args.results.read_text()); directory = args.results.parent; args.output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 11, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    cavity, mms = result['cases']; cr = cavity['records']; mr = mms['records']
    c = np.load(directory/cr[-1]['field_file']); m = np.load(directory/mr[-1]['field_file']); table = ghia()
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), layout='constrained')
    im = field(axes[0, 0], c, f'Re100: computed speed and streamlines ({cr[-1]["n"]} nodes)')
    axes[0, 0].plot(*cr[-1]['vortex_center_grid'], 'r.', ms=8, label='computed vortex')
    axes[0, 0].plot(.6172, .7344, 'wo', ms=5, mfc='none', label='Ghia Table V')
    axes[0, 0].legend(loc='lower left', fontsize=8); fig.colorbar(im, ax=axes[0, 0], label='speed / lid speed')
    for r in cr:
        a = np.load(directory/r['field_file']); mid=r['n']//2
        axes[0, 1].plot(a['u'][:, mid], a['y'], label=str(r['n'])+' nodes')
        axes[1, 0].plot(a['x'], a['v'][mid], label=str(r['n'])+' nodes')
        axes[1, 1].semilogy(a['history'][:, 1], np.maximum(a['history'][:, 2], 1e-16), label=str(r['n'])+' nodes')
    axes[0, 1].plot(table['u'][:, 1], table['u'][:, 0], 'ko', ms=3, mfc='none', label='Ghia Table I')
    axes[1, 0].plot(table['v'][:, 0], table['v'][:, 1], 'ko', ms=3, mfc='none', label='Ghia Table II')
    axes[0, 1].set(xlabel='u(x=0.5,y)', ylabel='y', title='Vertical centerline; printed reference coordinates')
    axes[1, 0].set(xlabel='x', ylabel='v(x,y=0.5)', title='Horizontal centerline; original Re100 column')
    axes[1, 1].axhline(1e-7, color='gray', ls=':', label='acceptance limit')
    axes[1, 1].set(xlabel='pseudo time', ylabel='max |transport RHS|', title='Actual steady PDE residual')
    for ax in [axes[0, 1], axes[1, 0], axes[1, 1]]: ax.grid(alpha=.2); ax.legend(fontsize=8)
    fig.suptitle('Lid-driven cavity: independent centered FD / Heun / Thom solver', fontsize=14)
    save(fig, args.output, cavity['id'])
    fig, ax = plt.subplots(figsize=(6.4, 5.6), layout='constrained')
    im = field(ax, c, 'Lid-driven cavity | Re=100')
    ax.plot(*cr[-1]['vortex_center_grid'], 'r.', ms=10); ax.plot(.6172, .7344, 'wo', ms=7, mfc='none')
    ax.annotate('lid u=1; stationary corners', (.5, 1), xytext=(.5, 1.06), ha='center')
    fig.colorbar(im, ax=ax, label='computed speed'); save(fig, args.output, cavity['id']+'-preview')
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), layout='constrained')
    im = field(axes[0, 0], m, 'Manufactured wall flow: actual velocity error', error=True)
    fig.colorbar(im, ax=axes[0, 0], label='|velocity - analytic velocity|')
    h = np.array([r['h'] for r in mr])
    for key, label in [('velocity_l2', 'velocity L2'), ('psi_l2', 'streamfunction L2'), ('pressure_l2', 'separate pressure L2'), ('pressure_gradient_l2', 'separate pressure gradient L2')]:
        axes[0, 1].loglog(h, [r[key] for r in mr], 'o-', label=label)
    vel = np.array([r['velocity_l2'] for r in mr]); axes[0, 1].loglog(h, vel[-1]*(h/h[-1])**2, 'k:', label='slope 2 guide')
    axes[0, 1].set(xlabel='h', ylabel='absolute error', title='Same Thom wall closure; separate pressure operator')
    for key, label in [('wall_omega_maximum', 'actual wall vorticity'), ('wall_shear_maximum', 'actual velocity-gradient shear'), ('thom_exact_psi_wall_truncation', 'local Thom truncation on exact psi')]:
        axes[1, 0].loglog(h, [r[key] for r in mr], 'o-', label=label)
    axes[1, 0].set(xlabel='h', ylabel='maximum horizontal-wall error', title='Wall derivatives: observed rates, no order promise')
    pe = m['pressure_p']-m['pressure_p_exact']
    im = axes[1, 1].pcolormesh(m['x'], m['y'], pe, shading='auto', cmap='coolwarm')
    axes[1, 1].set(xlabel='x', ylabel='y', aspect='equal', title='Separate nonzero-Dirichlet pressure error')
    fig.colorbar(im, ax=axes[1, 1], label='p - analytic p')
    for ax in [axes[0, 1], axes[1, 0]]: ax.grid(alpha=.2); ax.legend(fontsize=8)
    fig.suptitle('Wall MMS: analytic forcing, velocity/shear refinement, pressure operator', fontsize=14)
    save(fig, args.output, mms['id'])
    fig, ax = plt.subplots(figsize=(6.4, 5.6), layout='constrained')
    im = field(ax, m, 'Manufactured no-slip wall flow | computed velocity error', error=True)
    fig.colorbar(im, ax=ax, label='absolute velocity error')
    save(fig, args.output, mms['id']+'-preview')


if __name__ == '__main__': main()
