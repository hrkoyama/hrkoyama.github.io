#!/usr/bin/env python3
"""Draw only hash-checked saved 2D cell means and recorded stage diagnostics."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

CASE = 'zalesak-rotation'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source, saved = Path(__file__).resolve().parent, args.results.parent
    result = json.loads(args.results.read_text())
    if not result['passed'] or not result['cases'][0]['passed'] or not all(result['cases'][0]['checks'].values()):
        raise ValueError('Only qualified passed results may be plotted')
    for name, digest in result['source_sha256'].items():
        if sha(source/name) != digest:raise ValueError('Changed frozen scientific source: '+name)
    for name, digest in result['files_sha256'].items():
        if Path(name).name != name or sha(saved/name) != digest:
            raise ValueError('Changed saved numerical field/stage data: '+name)
    rows = result['cases'][0]['records']
    by_id = {row['id']: row for row in rows}
    fields = {}
    for row in rows:
        with np.load(saved/row['field'], allow_pickle=False) as data:
            fields[row['id']] = {key: data[key].copy() for key in data.files}
    donor = by_id['base-donor-cell-n128']
    limited = by_id['base-muscl-minmod-n128']
    d, m = fields[donor['id']], fields[limited['id']]
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'text.color': '#173348', 'axes.labelcolor': '#173348',
                         'axes.titlecolor': '#173348', 'axes.spines.top': False,
                         'axes.spines.right': False, 'savefig.facecolor': 'white',
                         'svg.hashsalt': CASE})
    args.output.mkdir(parents=True, exist_ok=True)
    figures = []
    def save(fig, name):
        for extension in ['png', 'svg', 'pdf']:
            path = args.output/(name+'.'+extension)
            if path.exists():raise ValueError('Use fresh figure output paths')
            metadata = ({'Date': None} if extension == 'svg' else
                        {'CreationDate': None, 'ModDate': None} if extension == 'pdf' else {})
            fig.savefig(path, dpi=160, metadata=metadata)
            if extension == 'svg':
                path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
            figures.append({'path': path.name, 'sha256': sha(path)})
        plt.close(fig)

    def image(ax, values, edges, title, zoom=False):
        mesh = ax.pcolormesh(edges, edges, values, shading='flat', cmap='magma',
                             vmin=0., vmax=1., rasterized=True)
        centers = .5*(edges[:-1]+edges[1:])
        ax.contour(centers, centers, m['q_reference'], levels=[.5],
                   colors=['#5eb5bf'], linewidths=.85, linestyles='--')
        ax.set(title=title, xlabel='$x$', ylabel='$y$', aspect='equal')
        if zoom:
            ax.set(xlim=(.28, .72), ylim=(.53, .97),
                   xticks=[.3, .5, .7], yticks=[.6, .75, .9])
        else:
            ax.set(xlim=(0, 1), ylim=(0, 1), xticks=[0, .5, 1], yticks=[0, .5, 1])
        return mesh

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 5.0))
    fig.subplots_adjust(left=.07, right=.965, bottom=.26, top=.74, wspace=.29)
    fig.text(.07, .925, 'ZALESAK / ONE FULL ROTATION', fontsize=22, fontweight='bold')
    fig.text(.07, .84, 'A SLOTTED DISK  |  128 x 128 CELLS  |  SHARED COLOR SCALE', fontsize=10)
    for ax, values, title in zip(axes, (m['q_reference'], d['q'], m['q']),
            ('Analytic cell-area reference', 'Donor-cell + SSPRK33', 'Minmod MUSCL + SSPRK33')):
        mesh = image(ax, values, m['edges'], title, zoom=True)
    cax = fig.add_axes([.33, .15, .4, .025])
    fig.colorbar(mesh, cax=cax, orientation='horizontal', label='Cell-mean tracer $q$')
    fig.text(.07, .045,
             'Zoom of the saved 2D unit-square fields; cyan dashed line: reference cell-mean 0.5 contour.',
             fontsize=9, color='#526476')
    save(fig, CASE+'-preview')

    fig, axes = plt.subplots(2, 3, figsize=(12., 8.0))
    fig.subplots_adjust(left=.07, right=.975, bottom=.12, top=.82,
                        hspace=.50, wspace=.34)
    fig.text(.07, .945, 'ZALESAK / SHAPE, BOUNDS AND CONSERVATION', fontsize=20, fontweight='bold')
    fig.text(.07, .88, 'One full turn of an isolated slotted disk: actual 2D finite-volume fields and whole-domain diagnostics.', fontsize=10)
    for ax, values, title in zip(axes[0], (m['q_reference'], d['q'], m['q']),
            ('Reference at $t=2\\pi$', 'Donor-cell, N=128', 'Minmod MUSCL, N=128')):
        mesh = image(ax, values, m['edges'], title)
        ax.set_xlabel('')
    # One fixed0--1 scale in all fields; a compact shared scale avoids hiding
    # donor-cell diffusion by automatically rescaling its smaller maximum.
    cax = fig.add_axes([.36, .49, .28, .012])
    fig.colorbar(mesh, cax=cax, orientation='horizontal', label='Cell-mean tracer $q$')

    colors = {'donor-cell': '#247dac', 'muscl-minmod': '#c45034'}
    ax = axes[1, 0]
    for method, label in [('donor-cell', 'Donor-cell'), ('muscl-minmod', 'Minmod MUSCL')]:
        sequence = sorted([row for row in rows if row['family'] == 'refinement' and row['method'] == method], key=lambda row:row['n'])
        ax.loglog([row['n'] for row in sequence], [row['relative_l1'] for row in sequence],
                  'o-', color=colors[method], label=label)
    ax.set(title='Full-turn shape error', xlabel='Cells per side $N$',
           ylabel='Whole-domain relative $L^1$', xticks=[32, 64, 128], xticklabels=['32', '64', '128'])
    ax.minorticks_off();ax.grid(alpha=.15);ax.legend(fontsize=8, frameon=False)

    ax = axes[1, 1]
    ids = ['base-muscl-minmod-n64', 'half-cell-shift', 'oblique-start']
    ax.bar(np.arange(3), [by_id[key]['relative_l1'] for key in ids],
            color=['#c45034', '#537a72', '#7d6592'], width=.55)
    ax.set(title='Center / grid-angle probes', ylabel='Whole-domain relative $L^1$',
           xticks=np.arange(3), xticklabels=['Baseline\nN=64', 'Both centers\nshifted $h/2$', 'Start angle\n$\\pi/4$'])
    ax.grid(axis='y', alpha=.15);ax.set_axisbelow(True)

    ax = axes[1, 2]
    with np.load(saved/limited['history'], allow_pickle=False) as data:
        stage = {str(name): data['values'][:, i].copy() for i, name in enumerate(data['columns'])}
    index = np.arange(1, len(stage['step'])+1)
    low = np.minimum.reduce([stage[key] for key in ['face_min', 'fe_min', 'rk_min']])
    high = np.maximum.reduce([stage[key] for key in ['face_max', 'fe_max', 'rk_max']])
    ax.plot(index, low, color='#247dac', lw=.9, label='Minimum across face / FE / SSP')
    ax.plot(index, high, color='#c45034', lw=.9, label='Maximum across face / FE / SSP')
    ax.axhline(0, color='#173348', ls=':', lw=.7);ax.axhline(1, color='#173348', ls=':', lw=.7)
    ax.set(title='Every stage: bounded means and faces', xlabel='Forward-Euler substep', ylabel='Raw tracer value', ylim=(-.045, 1.045))
    ax.legend(fontsize=7.5, frameon=False, loc='center left')
    ax.text(.03, .08, 'Maximum SSP mass defect\n'+f'{limited["maximum_rk_mass_defect"]:.2e}'+'; no clipping / retries',
             transform=ax.transAxes, fontsize=8, va='bottom')
    ax.grid(alpha=.15)
    fig.text(.07, .02,
             'Periodic scalar-FV variant, not Zalesak FCT or Firedrake DG. Bounds do not imply exact slot preservation or multidimensional TVD.',
             fontsize=9, color='#526476')
    save(fig, CASE)
    provenance = {'case': CASE, 'source_result_sha256': sha(args.results),
                  'source_fields_sha256': result['files_sha256'], 'figures': figures,
                  'scope': 'Actual saved 2D scalar cell means; preview is a labeled crop, main fields show the full unit square; error metrics cover the whole domain. Shared0–1color scale, with saved reference0.5contour.'}
    (args.output/'figure-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'figures': len(figures), 'source': str(args.results)}))


if __name__ == '__main__':
    main()
