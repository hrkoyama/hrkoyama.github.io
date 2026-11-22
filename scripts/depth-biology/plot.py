#!/usr/bin/env python3
"""Plot saved nonlinear biology results only; no scientific solver is imported."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw(data, output):
    output = Path(output);output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 9, 'axes.titlesize': 10})
    for case in data['cases']:
        fig, axes = plt.subplots(2, 3, figsize=(13, 7), constrained_layout=True)
        final = case['snapshots'][-1]
        for ax, species in zip(axes[0, :2], ['u', 'v']):
            ax.plot(final['x'], final['reference_'+species], 'k--', label='Independent Galerkin/Radau')
            ax.plot(final['x'], final[species], color='#235b83', linewidth=1.5, label='FD / midpoint Strang')
            ax.set(xlabel='x (dimensionless)', ylabel=species, title=f'Raw {species}(x), t={final["time"]:g}; fixed origin')
        selected = case['snapshots'][1:]
        for snapshot in selected:
            axes[0, 2].plot(snapshot['x'], snapshot['u'], label=f't={snapshot["time"]:g}', alpha=.8)
        axes[0, 2].set(xlabel='x (dimensionless)', ylabel='u', title='Selected-symmetry 1D evolution')
        rows = [r for r in case['records'] if r['series'] == 'evolution']
        axes[1, 0].plot([r['time'] for r in rows], [r['amplitude_u'] for r in rows], 'o-', label='Primary amplitude')
        axes[1, 0].plot([r['time'] for r in rows], [r['reference_amplitude_u'] for r in rows], 'k--', label='Independent reference')
        axes[1, 0].set(xlabel='Time (dimensionless)', ylabel='(max u - min u) / 2', title='Finite-time pattern growth')
        for ax, sequence, scale in [(axes[1, 1], 'space', 'n'), (axes[1, 2], 'time', 'inverse_dt')]:
            rows = [r for r in case['records'] if r['series'] == sequence]
            xx = np.array([r[scale] for r in rows])
            for norm, style in [('l1', 'o-'), ('l2', 's-'), ('linf', '^-')]:
                ax.loglog(xx, [r[norm] for r in rows], style, label=norm.upper())
            ax.loglog(xx, rows[0]['linf']*(xx[0]/xx)**2, 'k--', alpha=.5, label='Slope -2 guide')
            ax.set(xlabel='N' if sequence == 'space' else '1 / timestep', ylabel='Raw error (dimensionless)',
                   title='Space: independent Galerkin/Radau' if sequence == 'space' else 'Time: same-FD Radau reference')
        for ax in axes.ravel():
            ax.grid(alpha=.2);ax.legend(fontsize=7)
        fig.suptitle(case['id']+' — reflection-even, pi-periodic IC; no phase alignment', fontsize=11)
        fig.savefig(output/(case['id']+'.png'), dpi=140)
        plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    draw(json.loads(Path(args.results).read_text()), args.output)
