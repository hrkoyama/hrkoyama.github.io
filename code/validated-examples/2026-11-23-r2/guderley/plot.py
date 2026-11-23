#!/usr/bin/env python3
"""Plot only hash-qualified saved radial fields; no solver or ODE is run."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import NullLocator


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def primitive(q):
    rho, velocity = q[:, 0], q[:, 1]/q[:, 0]
    return rho, velocity, .4*(q[:, 2]-.5*q[:, 1]*velocity)


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
            raise ValueError('Changed frozen numerical source: '+name)
    for name, digest in result['files_sha256'].items():
        if Path(name).name != name or sha(saved/name) != digest:
            raise ValueError('Changed saved state/history: '+name)
    rows = case['records']
    fields = {}
    for row in rows:
        with np.load(saved/row['field'], allow_pickle=False) as data:
            fields[row['n']] = {name: data[name].copy() for name in data.files}
    finest = rows[-1]
    n = finest['n']
    data = fields[n]
    edges, radius = data['edges'], finest['reference_shock_radius']
    outer = float(edges[-1])
    rho, velocity, pressure = primitive(data['q'])
    reference_rho, reference_velocity, reference_pressure = primitive(data['q_reference'])
    centers = .5*(edges[:-1]+edges[1:])
    xy = np.linspace(-outer, outer, 401)
    xx, yy = np.meshgrid(xy, xy)
    radii = np.hypot(xx, yy)
    indices = np.clip(np.searchsorted(edges, radii, side='right')-1, 0, n-1)
    vmin = min(float(rho.min()), float(reference_rho.min()))
    vmax = max(float(rho.max()), float(reference_rho.max()))
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'text.color': '#173348',
                         'axes.labelcolor': '#173348', 'axes.titlecolor': '#173348',
                         'savefig.facecolor': 'white'})
    figures = []
    args.output.mkdir(parents=True, exist_ok=True)

    def save(fig, name):
        for extension in ['png', 'svg', 'pdf']:
            path = args.output/(name+'.'+extension)
            if path.exists():
                raise ValueError('Use a fresh figure output directory')
            metadata = ({'Date': None} if extension == 'svg' else
                        {'CreationDate': None, 'ModDate': None} if extension == 'pdf' else {})
            fig.savefig(path, dpi=160, facecolor='white', metadata=metadata)
            if extension == 'svg':
                path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
            figures.append({'path': path.name, 'sha256': sha(path)})
        plt.close(fig)

    def meridional(ax, density, speed, title):
        image = np.ma.masked_where(radii > outer, density[indices])
        cmap = plt.get_cmap('magma').copy()
        cmap.set_bad('#f5f4ef')
        im = ax.imshow(image, origin='lower', extent=[-outer, outer, -outer, outer],
                       interpolation='nearest', cmap=cmap, vmin=vmin, vmax=vmax)
        ax.add_patch(Circle((0, 0), radius, fill=False, ec='white', ls='--', lw=.85))
        theta = np.arange(4)*np.pi/2 + np.pi/4
        rr = outer*.9
        speeds = speed[min(int(np.searchsorted(edges, rr))-1, n-1)]
        ax.quiver(rr*np.cos(theta), rr*np.sin(theta), speeds*np.cos(theta), speeds*np.sin(theta),
                  color='white', scale_units='xy', angles='xy', scale=2.2,
                  width=.007, headwidth=4)
        ax.set(xlabel='$x$ (meridional display)', ylabel='$z$',
               xticks=[-outer, 0, outer], yticks=[-outer, 0, outer], title=title)
        return im

    fig = plt.figure(figsize=(8.6, 5.5))
    fig.text(.07, .94, 'GUDERLEY / CONVERGING SHOCK', fontsize=20, fontweight='bold')
    fig.text(.07, .865, f'1D SPHERICAL RADIAL EULER  |  {n} shells  |  gamma=1.4  |  t=-0.85', fontsize=10)
    im = meridional(fig.add_axes([.07, .265, .34, .525]), reference_rho, reference_velocity,
                    'Similarity shell means')
    meridional(fig.add_axes([.51, .265, .34, .525]), rho, velocity, 'HLL + Heun shell means')
    fig.colorbar(im, cax=fig.add_axes([.91, .29, .018, .46]), label='Spherical shell-mean density')
    fig.text(.07, .15, 'Saved radial states mapped onto a meridional plane; this is NOT a Cartesian 2D evolution.', fontsize=8.8)
    fig.text(.07, .09, 'Dashed circle: similarity shock. Arrows: inward radial velocity. Inner gas is cold and at rest.', fontsize=8.6)
    fig.text(.07, .035, 'Short pre-collapse window only; collapse singularity, reflected branch and nonradial stability are untested.', fontsize=8.1)
    save(fig, 'guderley-implosion-preview')

    fig, axes = plt.subplots(2, 3, figsize=(12.6, 9.4))
    fig.subplots_adjust(left=.065, right=.97, top=.85, bottom=.165,
                        hspace=.49, wspace=.38)
    fig.text(.065, .95, 'Guderley implosion / pre-collapse radial Euler verification', fontsize=19, fontweight='bold')
    fig.text(.065, .902, '128 / 256 / 512 spherical shells; t=-1 to -0.85; cold upstream; fixed HLL + Heun, CFL=0.4.', fontsize=10)
    im = meridional(axes[0, 0], rho, velocity, '512-shell density / meridional display')
    fig.colorbar(im, ax=axes[0, 0], fraction=.045, pad=.025)
    colors = ['#8a9aa6', '#3b8d9a', '#c24c2d']
    for axis, variable, reference_values, ylabel, title in [
        (axes[0, 1], 0, reference_rho, r'$\rho$', 'Density: whole radial domain'),
        (axes[0, 2], 2, reference_pressure, '$p$', 'Pressure from conserved shell means'),
        (axes[1, 2], 1, reference_velocity, '$u_r$', 'Radial velocity: inward flow')]:
        for row, color in zip(rows, colors):
            current = fields[row['n']]
            x = .5*(current['edges'][:-1]+current['edges'][1:])
            axis.plot(x, primitive(current['q'])[variable], c=color, lw=1.2,
                      label=str(row['n'])+' shells')
        axis.plot(centers, reference_values, '--', c='#173348', lw=1.15, label='Similarity means')
        axis.axvline(radius, color='#173348', ls=':', lw=.9)
        axis.set(xlim=(0, outer), xlabel='Radius r', ylabel=ylabel, title=title)
        axis.grid(alpha=.2)
        axis.legend(fontsize=7.1)
    for row, color in zip(rows, colors):
        trajectory = row['shock_trajectory']
        axes[1, 0].plot([p['time'] for p in trajectory], [p['shock_radius'] for p in trajectory],
                        'o-', ms=2, lw=1, color=color, label=str(row['n'])+' shells')
    trajectory = finest['shock_trajectory']
    axes[1, 0].plot([p['time'] for p in trajectory], [p['reference_shock_radius'] for p in trajectory],
                    '--', color='#173348', label='Similarity radius')
    axes[1, 0].set(xlabel='Physical similarity time t < 0', ylabel='Shock radius',
                   title='Saved shock trajectory', xticks=[-1., -.95, -.9, -.85],
                   xticklabels=['-1.00', '-0.95', '-0.90', '-0.85'])
    axes[1, 0].grid(alpha=.2)
    axes[1, 0].legend(fontsize=7.1)
    for metric, style, color, label in [
        ('density_l1', 'o--', '#c24c2d', 'Density / full volume'),
        ('active_density_l1', 'o-', '#c24c2d', 'Density / r >= 0.8 Rs'),
        ('pressure_l1', 's--', '#3b8d9a', 'Pressure / full volume'),
        ('active_pressure_l1', 's-', '#3b8d9a', 'Pressure / r >= 0.8 Rs')]:
        axes[1, 1].loglog([row['n'] for row in rows], [row[metric] for row in rows],
                          style, color=color, label=label)
    axes[1, 1].set(xlabel='Radial shells N', ylabel='Volume-weighted relative L1',
                   title='Full and predetermined active-region errors',
                   xticks=[row['n'] for row in rows], xticklabels=[str(row['n']) for row in rows])
    axes[1, 1].xaxis.set_minor_locator(NullLocator())
    axes[1, 1].grid(alpha=.2)
    axes[1, 1].legend(fontsize=7)
    balance = max(value for row in rows for value in row['conservation_relative'])
    guards = sum(row['sound_speed_roundoff_guard_evaluations'] for row in rows)
    fig.text(.065, .108, f"All {len(case['checks'])} fixed gates passed; max scaled mass/momentum/energy balance={balance:.2e}; sound-only guard evaluations={guards}.", fontsize=9)
    fig.text(.065, .068, 'Momentum includes its spherical pressure source; all three budgets use the actual stage-weighted outer boundary flux.', fontsize=8.7)
    fig.text(.065, .029, 'Pinned ExactPack eigenvalue + ODE, split Gauss shell means; radial meridional picture only. No collapse/reflection or nonradial-stability claim.', fontsize=8.3)
    save(fig, 'guderley-implosion')
    manifest = {'schema_version': 1, 'validation_passed': True,
                'result_sha256': sha(args.results), 'plot_sha256': sha(Path(__file__)),
                'files_sha256': result['files_sha256'], 'actual_cartesian_field': False,
                'actual_radial_field': True, 'n': n,
                'geometry': '1D spherical shell means mapped onto a meridional plane; not a 2D Cartesian computation',
                'display_grid_pixels': [401, 401], 'radial_mapping': 'nearest saved shell; no synthetic 2D PDE',
                'figures': figures}
    (args.output/'figure-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'passed': True, 'figures': len(figures), 'n': n,
                      'actual_cartesian_field': False, 'actual_radial_field': True}))


if __name__ == '__main__':
    main()
