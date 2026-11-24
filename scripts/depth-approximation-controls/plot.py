#!/usr/bin/env python3
"""Render fixed saved arrays; no interpolation, spline fit or transform is rerun."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


COLORS = ['#176b87', '#d26035', '#6b5b95']


def export(fig, target, name):
    for suffix in ('png', 'svg', 'pdf'):
        fig.savefig(target/(name+'.'+suffix), dpi=155, bbox_inches='tight')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result_file = args.results/'result.json' if args.results.is_dir() else args.results
    result = json.loads(result_file.read_text())
    if not result['passed']:
        raise ValueError('Only a completed qualified fixed protocol may be plotted')
    directory = result_file.parent
    args.output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
                         'figure.facecolor': '#fafaf7', 'axes.facecolor': '#fafaf7'})
    ident = 'runge-barycentric-clenshaw'
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    for family, color in zip(('equispaced', 'lobatto'), COLORS):
        d = np.load(directory/('runge-'+family+'-32.npz'))
        ax[0].plot(d['probes'], d['values'], color=color, label=family+' / degree 32')
        ax[1].plot(d['probes'], d['errors'], color=color, label=family)
    ax[0].plot(d['probes'], d['truth'], color='#333333', ls='--', label='target')
    ax[0].set(title='Runge function: sampled interpolation', xlabel='x', ylabel='value')
    ax[1].set(title='Sampled error against the target', xlabel='x', ylabel='signed error', yscale='symlog')
    for a in ax:a.legend(frameon=False);a.grid(alpha=.18)
    fig.suptitle('Nodes, representation and evaluation are separate errors')
    export(fig, args.output, ident);fig.savefig(args.output/(ident+'-preview.png'), dpi=95);plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    for function, a in zip(('runge', 'absolute'), ax):
        for family, color in zip(('equispaced', 'lobatto'), COLORS):
            rows = [r for r in result['cases'][0]['records'] if r['function'] == function and r['nodes'] == family]
            a.semilogy([r['degree'] for r in rows], [r['sampled_max_error'] for r in rows], 'o-', color=color, label=family)
        a.set(title=function, xlabel='polynomial degree', ylabel='sampled maximum error');a.legend(frameon=False);a.grid(alpha=.18)
    export(fig, args.output, ident+'-diagnostics');plt.close(fig)
    ident = 'spline-shape-controls'
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    for kind, color in zip(('natural', 'clamped', 'pchip'), COLORS):
        d = np.load(directory/('plateau-'+kind+'.npz'))
        for a in ax:a.plot(d['probes'], d['values'][0], color=color, label=kind)
    for a in ax:a.plot(d['x'], d['y'], 'o', color='#333333', ms=4);a.grid(alpha=.18)
    ax[0].set(title='Flat-to-flat plateau: three cubic interpolants', xlabel='x', ylabel='value')
    ax[1].set(title='Left plateau: overshoot is visible', xlabel='x', ylabel='value', xlim=(.7, 2.1), ylim=(-.16, .06))
    ax[0].legend(frameon=False)
    fig.suptitle('C2 smoothness and monotone shape preservation')
    export(fig, args.output, ident);fig.savefig(args.output/(ident+'-preview.png'), dpi=95);plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    for kind, color in zip(('natural', 'clamped', 'pchip'), COLORS):
        d = np.load(directory/('plateau-'+kind+'.npz'))
        for order, a in enumerate(ax, 1):a.plot(d['probes'], d['values'][order], color=color, label=kind)
    for order, a in enumerate(ax, 1):a.set(title='Derivative order '+str(order), xlabel='x', ylabel='derivative');a.legend(frameon=False);a.grid(alpha=.18)
    export(fig, args.output, ident+'-diagnostics');plt.close(fig)
    ident = 'haar-mallat-boundary-threshold'
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    for n, a in zip((32, 17), ax):
        d = np.load(directory/(f'step{n}-shift1-periodic-hard.npz'))
        a.step(np.arange(n), d['signal'], where='mid', color='#333333', label='shifted input')
        for mode, color in zip(('periodic', 'symmetric'), COLORS):
            d = np.load(directory/(f'step{n}-shift1-{mode}-soft.npz'))
            a.plot(d['reconstructed'], 'o-', ms=3, color=color, label=mode)
        a.set(title=f'{n} samples / soft threshold 0.2', xlabel='sample index', ylabel='signal');a.legend(frameon=False);a.grid(alpha=.18)
    fig.suptitle('Three-level Haar: shift and boundary conventions matter')
    export(fig, args.output, ident);fig.savefig(args.output/(ident+'-preview.png'), dpi=95);plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
    rows = [r for r in result['cases'][2]['records'] if r['threshold'] != 'none']
    labels = [r['signal']+'/'+r['boundary'][0]+'/'+r['threshold'][0] for r in rows]
    for i, (field, title) in enumerate((('reconstruction_l2_squared', 'Squared reconstruction L2 error'), ('shift_back_equivariance_l2_squared', 'Squared shift-back discrepancy'))):
        ax[i].bar(np.arange(len(rows)), [r[field] for r in rows], color=COLORS[i]);ax[i].set(title=title, xlabel='fixed signal / boundary / threshold', yscale='symlog')
        ax[i].set_xticks(np.arange(len(rows)), labels, rotation=90, fontsize=6)
    export(fig, args.output, ident+'-diagnostics');plt.close(fig)


if __name__ == '__main__':
    main()
