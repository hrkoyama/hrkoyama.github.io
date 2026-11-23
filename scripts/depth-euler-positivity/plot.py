#!/usr/bin/env python3
"""Render only qualified saved cell means and recorded stage diagnostics."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

CASE = 'euler-double-rarefaction-positivity'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def primitive(q):
    rho, u = q[..., 0], q[..., 1]/q[..., 0]
    return rho, u, .4*(q[..., 2]-.5*rho*u*u)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source, saved = Path(__file__).resolve().parent, args.results.parent
    result = json.loads(args.results.read_text())
    case = result['cases'][0]
    if not result['passed'] or not case['passed'] or not all(case['checks'].values()):
        raise ValueError('Only qualified passed results may be plotted')
    for name, digest in result['source_sha256'].items():
        if sha(source/name) != digest:
            raise ValueError('Changed frozen source: '+name)
    for name, digest in result['files_sha256'].items():
        if Path(name).name != name or sha(saved/name) != digest:
            raise ValueError('Changed saved field/stage history: '+name)
    rows = case['records']
    fields = {}
    for row in rows:
        with np.load(saved/row['field'], allow_pickle=False) as data:
            fields[row['n']] = {key: data[key].copy() for key in data.files}
    finest = rows[-1]
    data = fields[finest['n']]
    stages = json.loads((saved/finest['history']).read_text())
    colors = ['#7c94ae', '#247dac', '#c45034']
    navy = '#173348'
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'text.color': navy,
                         'axes.labelcolor': navy, 'axes.titlecolor': navy,
                         'savefig.facecolor': 'white', 'svg.hashsalt': CASE,
                         'font.family': 'DejaVu Sans'})
    args.output.mkdir(parents=True, exist_ok=True)
    figures = []

    def save(fig, name):
        for extension in ['png', 'svg', 'pdf']:
            path = args.output/(name+'.'+extension)
            if path.exists():
                raise ValueError('Use fresh figure output paths')
            metadata = ({'Date': None} if extension == 'svg' else
                        {'CreationDate': None, 'ModDate': None} if extension == 'pdf' else {})
            fig.savefig(path, dpi=160, facecolor='white', metadata=metadata)
            if extension == 'svg':
                path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
            figures.append({'path': path.name, 'sha256': sha(path)})
        plt.close(fig)

    centers = .5*(data['edges'][:-1]+data['edges'][1:])
    times = data['history_times']
    density, velocity, pressure = primitive(data['q_history'])
    fig = plt.figure(figsize=(8.8, 5.5))
    fig.text(.075, .94, 'EULER / POSITIVITY AT EVERY STAGE', fontsize=18,
             fontweight='bold')
    fig.text(.075, .875, '1D DOUBLE RAREFACTION  |  P1 FV + GLOBAL LF + SSPRK(3,3)', fontsize=10)
    for rect, values, cmap, norm, title, label in [
            ([.075, .24, .34, .54], density, 'magma', None, 'Density', '$\\rho$'),
            ([.565, .24, .34, .54], pressure, 'viridis',
             LogNorm(vmin=float(pressure.min()), vmax=float(pressure.max())),
             'Pressure of conserved means', '$p(\\overline{q})$')]:
        ax = fig.add_axes(rect)
        image = ax.pcolormesh(centers, times, values, shading='nearest',
                              cmap=cmap, norm=norm, rasterized=True)
        ax.set(xlabel='$x$', ylabel='Time $t$', title=title,
               xlim=(0, 1), ylim=(0, float(data['time'])),
               xticks=[0, .5, 1], yticks=[0, .05, .1, .15])
        fig.colorbar(image, ax=ax, location='bottom', shrink=.86,
                     pad=.16, fraction=.055, label=label)
    fig.text(.075, .055, f'{finest["n"]} cells  |  Saved space-time cell means; this is not a 2D-flow calculation.',
             fontsize=9, color='#526476')
    save(fig, CASE+'-preview')

    fig, axes = plt.subplots(2, 3, figsize=(12.0, 7.8))
    fig.subplots_adjust(left=.075, right=.975, bottom=.10, top=.83,
                        wspace=.31, hspace=.42)
    fig.text(.075, .94, 'EULER / A CONSERVATIVE POSITIVITY UPDATE', fontsize=20,
             fontweight='bold')
    fig.text(.075, .875,
             'Strong double rarefaction: three fixed refinements, analytic Riemann reference, all SSP stages recorded.',
             fontsize=10)
    qref = primitive(data['q_reference'])
    for ax, component, title, ylabel in zip(axes[0], (0, 2, 1),
            ('Density at $t=0.15$', 'Low central pressure', 'Separating velocity'),
            ('$\\rho$', '$p(\\overline{q})$', '$u(\\overline{q})$')):
        ax.plot(centers, qref[component], color=navy, lw=1.8, label='Analytic cell reference')
        for row, color in zip(rows, colors):
            d = fields[row['n']]
            x = .5*(d['edges'][:-1]+d['edges'][1:])
            ax.plot(x, primitive(d['q'])[component], color=color, lw=1.0,
                    alpha=.95, label=f'N={row["n"]}')
        ax.set(xlabel='$x$', ylabel=ylabel, title=title, xlim=(0, 1))
        if component == 2:
            ax.set_yscale('log')
        ax.grid(alpha=.15)
    axes[0, 0].legend(fontsize=8, frameon=False)

    index = np.arange(1, len(stages)+1)
    ax = axes[1, 0]
    for key, label, color in [
            ('endpoint_min_pressure', 'Scaled endpoint', '#c45034'),
            ('fe_mean_min_pressure', 'Forward-Euler mean', '#247dac'),
            ('rk_mean_min_pressure', 'SSP convex mean', navy)]:
        ax.semilogy(index, [s[key] for s in stages], label=label, color=color, lw=.85)
    ax.set(xlabel='Forward-Euler substep', ylabel='Minimum pressure',
           title='Every recorded stage remains positive')
    ax.legend(fontsize=8, frameon=False)
    ax.grid(alpha=.15)

    ax = axes[1, 1]
    ax.plot(index, [s['minimum_theta'] for s in stages], color='#c45034', lw=.9)
    ax.set(xlabel='Forward-Euler substep', ylabel='Minimum affine factor $\\theta$',
           title='Conservative reconstruction scaling', ylim=(-.035, 1.035))
    total = sum(s['scaled_cells'] for s in stages)
    ax.text(.04, .10, f'{total:,} cell/substep activations\nNo state floors or retries',
            transform=ax.transAxes, fontsize=9, va='bottom',
            bbox={'facecolor': 'white', 'alpha': .85, 'edgecolor': 'none'})
    ax.grid(alpha=.15)

    ax = axes[1, 2]
    ns = [row['n'] for row in rows]
    ax.loglog(ns, [row['density_l1'] for row in rows], 'o-',
              color='#247dac', label='Density')
    ax.loglog(ns, [row['pressure_l1'] for row in rows], 's-',
              color='#c45034', label='Pressure')
    ax.set(xlabel='Number of cells', ylabel='Relative $L^1$ error',
           title='Fixed-input grid refinement', xticks=ns, xticklabels=[str(n) for n in ns])
    ax.minorticks_off()
    ax.legend(fontsize=8, frameon=False)
    ax.grid(alpha=.15)
    fig.text(.075, .035,
             'Positive non-vacuum central state; no claim for arbitrary inputs, vacuum, multidimensional Euler, TVD or entropy stability.',
             fontsize=9, color='#526476')
    save(fig, CASE)
    manifest = {'case': CASE, 'source_result_sha256': sha(args.results),
                'source_fields_sha256': result['files_sha256'], 'figures': figures,
                'scope': 'Actual saved 1D cell means and stage diagnostics. Preview axes are space and time, not two spatial dimensions.'}
    (args.output/'figure-provenance.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'figures': len(figures), 'source': str(args.results)}))


if __name__ == '__main__':
    main()
