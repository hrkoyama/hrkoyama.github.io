#!/usr/bin/env python3
"""Render stored foundation result JSON/CSV only; no scientific solver imports."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


FLOOR = 1e-16


def positive(values):
    return np.maximum(np.asarray(values, dtype=float), FLOOR)


def axes(title):
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.5), layout='constrained')
    fig.suptitle(title, fontsize=12)
    for a in ax:
        a.grid(alpha=0.25)
    return fig, ax


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    data = json.loads(args.results.read_text())
    if not data['passed']:
        raise ValueError('Only accepted stored results may be presented as verified figures')
    args.output.mkdir(parents=True, exist_ok=True)
    records = {r['id']: r for r in data['cases']}
    saved = []

    def save(fig, name):
        destination = args.output/(name+'.png')
        fig.savefig(destination, dpi=160)
        plt.close(fig)
        saved.append(str(destination))

    amg = records['sa-amg']
    fig, ax = axes('Matrix-based smoothed aggregation: residual and continuum error')
    with (args.results.parent/'amg-residuals.csv').open() as handle:
        histories = list(csv.DictReader(handle))
    for n in sorted({int(r['grid_n']) for r in histories}):
        group = [r for r in histories if int(r['grid_n']) == n]
        ax[0].semilogy([int(r['cycle']) for r in group], positive([float(r['relative_residual']) for r in group]), '.-', label=f'{n} x {n}')
    ax[0].set(xlabel='V-cycles', ylabel='||b - A x||2 / ||b||2')
    ax[0].legend(fontsize=8)
    rows = amg['records']; h = np.array([r['h'] for r in rows]); error = np.array([r['pde_relative_l2_error'] for r in rows])
    ax[1].loglog(h, error, 'o-', label='continuum solution error')
    ax[1].loglog(h, error[0]*(h/h[0])**2, '--', label='h^2 reference slope')
    ax[1].set(xlabel='Mesh width h', ylabel='Relative discrete L2 solution error')
    ax[1].legend(fontsize=8)
    save(fig, 'sa-amg')

    fig, ax = axes('Original Householder QR / one-sided Jacobi SVD')
    rows = records['qr-svd-factorization']['records']; labels = [r['matrix'] for r in rows]
    x = np.arange(len(rows))
    for key, label, marker in [('qr_reconstruction', 'QR reconstruction', 'o'),
                               ('svd_reconstruction', 'SVD reconstruction', 's'),
                               ('singular_value_error', 'LAPACK singular-value difference', '^')]:
        ax[0].semilogy(x, positive([r[key] for r in rows]), marker+'-', label=label)
    ax[0].set(xticks=x, xticklabels=labels, ylabel='Relative Frobenius / singular-value error')
    ax[0].tick_params(axis='x', labelsize=8); ax[0].legend(fontsize=7)
    for key, label, marker in [('qr_orthogonality', 'Q', 'o'),
                               ('u_orthogonality', 'U (retained rank)', 's'),
                               ('v_orthogonality', 'V (retained rank)', '^')]:
        ax[1].semilogy(x, positive([r[key] for r in rows]), marker+'-', label=label)
    ax[1].set(xticks=x, xticklabels=labels, ylabel='||W.T W - I||2')
    ax[1].tick_params(axis='x', labelsize=8); ax[1].legend(fontsize=7)
    fig.supxlabel('Zeros, if any, are plotted at 1e-16; numerical ranks: '+', '.join(str(r['rank']) for r in rows), fontsize=8)
    save(fig, 'qr-svd-factorization')

    fig, ax = axes('Reorthogonalized Krylov projections against independent dense eigenvalues')
    rows = records['krylov-eigenvalues']['records']
    for method, n in sorted({(r['method'], r['size']) for r in rows}):
        group = [r for r in rows if r['method'] == method and r['size'] == n]
        dimensions = [r['dimensions'] for r in group]
        label = f'{method}, n={n}'
        ax[0].semilogy(dimensions, positive([r['eigenpair_residual'] for r in group]), 'o-', label=label)
        ax[1].semilogy(dimensions, positive([r['eigenvalue_error'] for r in group]), 'o-', label=label)
    ax[0].set(xlabel='Krylov dimension', ylabel='||A v - lambda v||2')
    ax[1].set(xlabel='Krylov dimension', ylabel='Absolute Ritz eigenvalue error')
    for a in ax:
        a.legend(fontsize=7)
    fig.supxlabel('Zero differences are plotted at 1e-16 (roundoff agreement, not exactness).', fontsize=8)
    save(fig, 'krylov-eigenvalues')

    fig, ax = axes('Gauss order refinement and adaptive-Simpson tolerance sweep')
    rows = records['gauss-adaptive-quadrature']['records']
    group = [r for r in rows if r['method'] == 'gauss-legendre']
    ax[0].semilogy([r['order_or_tolerance'] for r in group], positive([r['analytic_error'] for r in group]), 'o-')
    ax[0].set(xlabel='Gauss-Legendre order', ylabel='Absolute exponential-integral error')
    for method in ['adaptive-simpson-exponential', 'adaptive-simpson-lorentzian']:
        group = [r for r in rows if r['method'] == method]
        ax[1].loglog([r['order_or_tolerance'] for r in group], positive([r['analytic_error'] for r in group]), 'o-', label=method.replace('adaptive-simpson-', ''))
    tolerances = sorted({r['order_or_tolerance'] for r in rows if r['method'].startswith('adaptive')})
    ax[1].loglog(tolerances, tolerances, '--', label='error = requested tolerance')
    ax[1].set(xlabel='Requested absolute tolerance', ylabel='Absolute analytic-integral error')
    ax[1].legend(fontsize=8)
    fig.supxlabel('Zero differences are plotted at 1e-16. Simpson error estimates are not rigorous bounds.', fontsize=8)
    save(fig, 'gauss-adaptive-quadrature')
    print(json.dumps({'stored_results_only': True, 'figures': saved}))


if __name__ == '__main__':
    main()
