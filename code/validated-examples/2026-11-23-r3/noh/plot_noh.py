#!/usr/bin/env python3
"""Publication figures from saved Noh finite-volume data; never run a solver.

Usage (numpy/matplotlib/Pillow are the only plotting dependencies)::

    python plot_noh.py --describe-input
    python plot_noh.py --results results/results.json --output figures

The JSON contains metadata and a flat runs list. Each run supplies geometry
('planar' or 'cylindrical'), n, time, and profile (relative CSV path). Metadata
supplies gamma, rho0, u0 and p0, directly or under 'parameters'. See INPUT_SCHEMA.

CSV exact_rho/momentum/total_energy are exact *volume cell means*. The other
exact_* columns are primitive variables recovered from those exact means;
exact_pressure_average is the independently averaged physical pressure.
These two pressures are deliberately shown as different curves.

The cylindrical picture rotates a piecewise-constant 1D radial density profile
for display. It neither solves 2D Euler nor measures angular symmetry errors.
No synthetic numerical data, numerical smoothing, or vertical error clipping
is introduced. Plot reductions use the saved volume weights and are described
in figure-manifest.json. Existing results and solver sources remain untouched.

This script deliberately supports Python 3.7 / matplotlib 3.1 as available on
the workstation, as well as current scientific Python environments.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


INPUT_SCHEMA = {
    'schema_version': 1,
    'metadata': {
        'gamma': 'finite > 1; first verified edition uses 5/3',
        'rho0': 'positive upstream density',
        'u0': 'negative incident radial velocity',
        'p0': '0 for the cold Noh exact reference',
        'units': 'dimensionless normalized benchmark units',
    },
    'runs': [{
        'geometry': 'planar | cylindrical; one-dimensional FV in either case',
        'n': 'number of cells', 'time': 'actual final time > 0',
        'profile': 'profiles/cylindrical-n512.csv (relative to results JSON)',
        'metrics': 'optional saved validation diagnostics; not overwritten',
    }],
    'csv_columns': [
        'r_left', 'r_right', 'r_center', 'volume',
        'rho', 'momentum', 'total_energy', 'velocity', 'pressure',
        'specific_internal_energy', 'exact_rho', 'exact_momentum',
        'exact_total_energy', 'exact_velocity', 'exact_pressure',
        'exact_specific_internal_energy', 'exact_pressure_average',
        'mask_center', 'mask_shock', 'mask_plateau',
    ],
    'representation': {
        'conserved': 'numerical and exact volume cell averages',
        'pressure': 'p(q_bar), not the exact volume average of pressure',
        'exact_pressure_average': 'independently integrated pressure mean',
        'cylindrical_display': '1D radial cell means rotated for display; not 2D Euler',
    },
}

INK = '#173747'
MUTED = '#586d78'
ACCENT = '#b45335'
GRID = '#dce5e8'
COLORS = ('#8baebf', '#4b899c', '#277181', '#b45335', '#754b6e')
GEOMETRY_LABEL = {'planar': 'Planar', 'cylindrical': 'Cylindrical'}


def scalar(metadata, name):
    value = metadata.get(name, metadata.get('parameters', {}).get(name))
    if value is None or isinstance(value, bool):
        raise ValueError('Missing physical metadata: ' + name)
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('Nonfinite physical metadata: ' + name)
    return value


def load_results(path):
    import numpy as np
    path = Path(path).resolve()
    payload = json.loads(path.read_text())
    metadata = payload['metadata']
    parameters = {name: scalar(metadata, name) for name in ('gamma', 'rho0', 'u0', 'p0')}
    if not (parameters['gamma'] > 1 and parameters['rho0'] > 0 and parameters['u0'] < 0):
        raise ValueError('Expected gamma>1, rho0>0 and u0<0')
    if parameters['p0'] != 0:
        raise ValueError('Cold Noh reference requires declared p0=0; no hidden pressure floor')
    groups = {}
    seen = set()
    receipts = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()}
    required = [name for name in INPUT_SCHEMA['csv_columns'] if not name.startswith('mask_')]
    for record in payload['runs']:
        geometry = record['geometry']
        if geometry not in GEOMETRY_LABEL:
            raise ValueError('Unsupported geometry: ' + str(geometry))
        n, time = int(record['n']), float(record['time'])
        if n <= 0 or time <= 0 or not math.isfinite(time):
            raise ValueError('Invalid cell count or actual final time')
        key = (geometry, n, time)
        if key in seen:
            raise ValueError('Ambiguous duplicate geometry/grid/time: ' + str(key))
        seen.add(key)
        profile = (path.parent / record['profile']).resolve()
        if path.parent not in profile.parents:
            raise ValueError('Profile must remain inside the results package')
        data = np.atleast_1d(np.genfromtxt(str(profile), delimiter=',', names=True,
                                         dtype=None, encoding='utf-8'))
        missing = set(required) - set(data.dtype.names or [])
        if missing or data.shape != (n,):
            raise ValueError('Invalid profile columns/row count: {} {}'.format(profile, sorted(missing)))
        columns = {name: np.asarray(data[name], dtype=float) for name in required}
        if not all(np.isfinite(value).all() for value in columns.values()):
            raise ValueError('Profile contains nonfinite values; do not silently mask them')
        left, right = columns['r_left'], columns['r_right']
        if not (np.all(right > left) and np.all(columns['volume'] > 0)
                and np.all(columns['rho'] > 0) and np.all(columns['exact_rho'] > 0)):
            raise ValueError('Invalid cell geometry, weights or density')
        if left[0] != 0 or not np.allclose(left[1:], right[:-1], rtol=0, atol=1e-13):
            raise ValueError('Expected contiguous radial cells beginning at the origin')
        if not np.allclose(columns['r_center'], .5 * (left + right), rtol=0, atol=1e-13):
            raise ValueError('Cell centers do not match saved edges')
        shock = abs(parameters['u0']) * time * (parameters['gamma'] - 1) / 2
        if not 0 < shock < right[-1]:
            raise ValueError('Analytic shock must remain inside the saved domain')
        # This is the same formula used in the saved exact reference, used only
        # as a locator. No point-sampled curve replaces exact CSV cell means.
        row = dict(record=record, geometry=geometry, n=n, time=time, data=columns,
                   edges=np.r_[left, right[-1]], shock=shock, length=float(right[-1]))
        groups.setdefault(geometry, []).append(row)
        receipts[profile.relative_to(path.parent).as_posix()] = hashlib.sha256(profile.read_bytes()).hexdigest()
    if not groups:
        raise ValueError('No saved runs to plot')
    for geometry, rows in groups.items():
        rows.sort(key=lambda row: row['n'])
        if len({row['time'] for row in rows}) != 1 or len({row['length'] for row in rows}) != 1:
            raise ValueError('A grid-convergence family must share final time and domain: ' + geometry)
    return payload, parameters, groups, receipts


def configure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 10,
        'axes.titlesize': 11, 'axes.titleweight': 'semibold',
        'axes.labelsize': 10, 'axes.labelcolor': INK, 'axes.edgecolor': '#9bafb8',
        'axes.spines.top': False, 'axes.spines.right': False,
        'xtick.color': MUTED, 'ytick.color': MUTED,
        'text.color': INK, 'figure.facecolor': 'white', 'savefig.facecolor': 'white',
        'axes.facecolor': 'white', 'grid.color': GRID, 'grid.alpha': .75,
        'grid.linewidth': .6, 'legend.frameon': False,
        'legend.fontsize': 8, 'pdf.fonttype': 42, 'ps.fonttype': 42,
        'svg.fonttype': 'none', 'svg.hashsalt': 'noh-fv-figures-v1',
    })
    return plt


def staircase(ax, run, key, scale=1., **style):
    import numpy as np
    values = run['data'][key] / scale
    return ax.step(run['edges'] / run['length'], np.r_[values, values[-1]],
                   where='post', **style)[0]


def clean_axes(ax, title=None):
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    ax.tick_params(length=3, width=.6)
    if title:
        ax.set_title(title, loc='left', pad=9)


def conditions(parameters, groups):
    times = sorted({run['time'] for rows in groups.values() for run in rows})
    return (r'$\gamma={:.6g}$   $\rho_0={:g}$   $u_0={:g}$   $p_0=0$   $t={:g}$'
            '   |   dimensionless benchmark units').format(
                parameters['gamma'], parameters['rho0'], parameters['u0'], times[0])


def save_figure(fig, output, name, dpi, plt):
    from PIL import Image
    files = []
    for extension in ('png', 'svg', 'pdf'):
        target = output / (name + '.' + extension)
        options = {'metadata': {'Creator': 'Noh finite-volume figure script',
                                'CreationDate': None, 'ModDate': None}} if extension == 'pdf' else {}
        fig.savefig(str(target), dpi=dpi, format=extension, facecolor='white', **options)
        if extension == 'svg':
            target.write_text('\n'.join(line.rstrip() for line in target.read_text().splitlines()) + '\n')
        record = {'path': target.name, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}
        if extension == 'png':
            with Image.open(str(target)) as im:
                record['width'], record['height'] = im.size
        files.append(record)
    plt.close(fig)
    return files


def thumbnail(groups, parameters, output, geometry, plt):
    import numpy as np
    from matplotlib.patches import Circle
    run = groups[geometry][-1]
    fig = plt.figure(figsize=(6.4, 3.8), dpi=130)
    fig.text(.07, .945, 'NOH  /  CONVERGING FLOW', fontsize=15, weight='semibold')
    method = '1D cylindrical radial FV' if geometry == 'cylindrical' else '1D planar FV'
    fig.text(.07, .89, method + '  ·  N = ' + str(run['n']) + '  ·  t = {:g}'.format(run['time']),
             fontsize=9.3, color=MUTED)
    field = fig.add_axes([.075, .28, .405, .55])
    profile = fig.add_axes([.655, .25, .295, .58])
    half = min(run['length'] / math.sqrt(2), max(2 * run['shock'], .32 * run['length']))
    side = 420
    coordinates = (np.arange(side) + .5) * (2 * half / side) - half
    xx, yy = np.meshgrid(coordinates, coordinates)
    radius = np.sqrt(xx * xx + yy * yy) if geometry == 'cylindrical' else np.abs(xx)
    index = np.searchsorted(run['edges'], radius, side='right') - 1
    valid = (index >= 0) & (index < run['n'])
    display = np.full(radius.shape, np.nan)
    display[valid] = run['data']['rho'][index[valid]] / parameters['rho0']
    im = field.imshow(display, origin='lower', extent=[-half, half, -half, half],
                      interpolation='nearest', cmap='viridis', aspect='equal',
                      vmin=min(1., float(np.nanmin(display))), vmax=float(np.nanmax(display)))
    if geometry == 'cylindrical':
        field.add_patch(Circle((0, 0), run['shock'], fill=False, ec='white', lw=1, ls='--'))
    else:
        for x in (-run['shock'], run['shock']):
            field.axvline(x, color='white', ls='--', lw=1)
    field.set(xlabel='Display x / L', ylabel='Display y / L')
    field.set_title('Rotated 1D density' if geometry == 'cylindrical' else 'Mirrored / extruded 1D density',
                    fontsize=9, loc='left', pad=9)
    tick = round(half / run['length'], 2)
    field.set_xticks([-half, 0, half]); field.set_xticklabels(['-' + str(tick), '0', str(tick)])
    field.set_yticks([-half, 0, half]); field.set_yticklabels(['-' + str(tick), '0', str(tick)])
    barax = fig.add_axes([.505, .31, .014, .45])
    bar = fig.colorbar(im, cax=barax)
    bar.ax.set_title(r'$\bar\rho/\rho_0$', fontsize=9, pad=8)
    bar.ax.tick_params(labelsize=8, length=2)
    staircase(profile, run, 'exact_rho', parameters['rho0'], color=INK, ls='--', lw=1.4,
              label='Noh exact cell means', zorder=4)
    staircase(profile, run, 'rho', parameters['rho0'], color=ACCENT, lw=1.65,
              label='Finite volume', zorder=3)
    profile.axvline(run['shock'] / run['length'], color='#93a6ac', ls=':', lw=.8)
    profile.set(xlabel='r / L', ylabel=r'$\bar\rho/\rho_0$', xlim=(0, 1))
    clean_axes(profile, 'Radial cell means' if geometry == 'cylindrical' else 'Planar cell means')
    profile.set_ylim(bottom=0)
    profile.legend(loc='upper right', fontsize=7.1, handlelength=2)
    note = ('Rotated 1D radial data, not a 2D Euler calculation.' if geometry == 'cylindrical'
            else 'Mirrored / extruded 1D data, not a 2D Euler calculation.')
    fig.text(.07, .09, note, fontsize=8, color=MUTED)
    fig.text(.07, .047, r'Cold ideal gas  ·  $\gamma=5/3$, $\rho_0=1$, $u_0=-1$, $p_0=0$'
             if abs(parameters['gamma'] - 5 / 3) < 1e-12 and parameters['rho0'] == 1 and parameters['u0'] == -1
             else conditions(parameters, groups), fontsize=8, color=MUTED)
    return save_figure(fig, output, 'noh-preview', 130, plt)


def profiles(groups, parameters, output, plt):
    geometries = [g for g in ('planar', 'cylindrical') if g in groups]
    fig, axes = plt.subplots(len(geometries), 3, figsize=(12.8, 3.1 * len(geometries) + 1.35), squeeze=False)
    fig.suptitle('Noh shock  |  conserved cell averages and recovered primitives',
                 x=.065, y=.97, ha='left', fontsize=16, weight='semibold')
    fig.text(.065, .917, conditions(parameters, groups), fontsize=9, color=MUTED)
    handles, labels = [], []
    definitions = [('rho', parameters['rho0'], r'$\bar\rho/\rho_0$', 'Density'),
                   ('velocity', abs(parameters['u0']), r'$(\bar m/\bar\rho)/|u_0|$', 'Velocity from means'),
                   ('pressure', parameters['rho0'] * parameters['u0'] ** 2,
                    r'$p(\bar q)/(\rho_0 u_0^2)$', 'Pressure from means')]
    for row_index, geometry in enumerate(geometries):
        rows = groups[geometry]
        for column, (key, scale, ylabel, title) in enumerate(definitions):
            ax = axes[row_index, column]
            for i, run in enumerate(rows):
                color = COLORS[i % len(COLORS)]
                line = staircase(ax, run, key, scale, color=color,
                                 lw=1.6 if i == len(rows) - 1 else .95,
                                 alpha=1 if i == len(rows) - 1 else .9,
                                 label='N = ' + str(run['n']))
                if row_index == column == 0:
                    handles.append(line); labels.append(line.get_label())
            finest = rows[-1]
            reference = staircase(ax, finest, 'exact_' + key, scale, color=INK, ls='--', lw=1.35,
                                  label='Noh: exact conserved means', zorder=5)
            if row_index == column == 0:
                handles.append(reference); labels.append(reference.get_label())
            if key == 'pressure':
                average = staircase(ax, finest, 'exact_pressure_average', scale, color='#62666a', ls=':', lw=1.8,
                                    label='Exact volume mean of pressure', zorder=6)
                if row_index == 0:
                    handles.append(average); labels.append(average.get_label())
            ax.axvline(finest['shock'] / finest['length'], color='#aebdc4', lw=.7, zorder=0)
            ax.set(xlabel='r / L', ylabel=ylabel, xlim=(0, 1))
            clean_axes(ax, GEOMETRY_LABEL[geometry] + ' · ' + title)
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.52, .89), ncol=3,
               columnspacing=2.2, handlelength=2.7, fontsize=8)
    fig.text(.065, .057, 'References use the same cells and volume weights. Velocity and solid/dashed pressure are recovered from conserved means.',
             fontsize=8, color=MUTED)
    fig.text(.065, .029, 'The dotted pressure curve is the separate volume average of physical pressure; it differs inside the shock cell. No pressure floor is inserted.',
             fontsize=8, color=MUTED)
    fig.subplots_adjust(left=.065, right=.975, bottom=.16, top=.75, hspace=.64, wspace=.36)
    return save_figure(fig, output, 'noh-profiles', 160, plt)


def reductions(groups, parameters):
    import numpy as np
    out = {}
    for geometry, rows in groups.items():
        values = []
        for run in rows:
            data = run['data']; error = (data['rho'] - data['exact_rho']) / parameters['rho0']
            weights = data['volume'] / np.sum(data['volume'])
            exact = data['exact_rho'] / parameters['rho0']
            l1 = float(np.sum(weights * np.abs(error)) / np.sum(weights * np.abs(exact)))
            l2 = float(np.sqrt(np.sum(weights * error ** 2) / np.sum(weights * exact ** 2)))
            linf = float(np.max(np.abs(error)) / np.max(np.abs(exact)))
            for name, value in [('density_l1', l1), ('density_l2', l2), ('density_linf', linf)]:
                saved = run['record'].get('metrics', {}).get(name)
                if saved is not None and not np.isclose(float(saved), value, rtol=2e-12, atol=2e-14):
                    raise ValueError('Saved and plotted error definitions disagree: ' + name)
            values.append({'n': run['n'], 'density_relative_l1': l1,
                           'density_relative_l2': l2,
                           'density_relative_linf': linf,
                           'center_specific_internal_energy_ratio': float(data['specific_internal_energy'][0] / data['exact_specific_internal_energy'][0])})
        out[geometry] = values
    return out


def errors(groups, parameters, diagnostics, output, plt):
    import numpy as np
    from matplotlib.ticker import NullLocator
    geometries = [g for g in ('planar', 'cylindrical') if g in groups]
    fig, axes = plt.subplots(len(geometries), 3, figsize=(12.8, 3.15 * len(geometries) + 1.35), squeeze=False)
    fig.suptitle('Noh verification  |  origin heating, local errors and grid refinement',
                 x=.065, y=.97, ha='left', fontsize=15, weight='semibold')
    fig.text(.065, .918, conditions(parameters, groups), fontsize=9, color=MUTED)
    handles, labels = [], []
    for index, geometry in enumerate(geometries):
        rows = groups[geometry]; finest = rows[-1]
        a, b, c = axes[index]
        reference_energy = .5 * parameters['u0'] ** 2
        for i, run in enumerate(rows):
            color = COLORS[i % len(COLORS)]; data = run['data']
            central = data['r_center'] <= .45 * run['shock']
            # The r-axis window is explicitly stated; every central value is
            # shown without an upper y limit, including the origin-heating peak.
            if not central.any():
                raise ValueError('Grid too coarse to display the declared origin window')
            line = a.plot(data['r_center'][central] / run['shock'],
                          data['specific_internal_energy'][central] / reference_energy,
                          '-o', color=color, lw=1.35 if i == len(rows) - 1 else .95,
                          ms=3 if run['n'] <= 128 else 1.8, label='N = ' + str(run['n']))[0]
            if index == 0:
                handles.append(line); labels.append(line.get_label())
            error = (data['rho'] - data['exact_rho']) / parameters['rho0']
            b.plot(data['r_center'] / run['length'], error, color=color,
                   lw=1.15 if i == len(rows) - 1 else .8, label='N = ' + str(run['n']))
        a.axhline(1, ls='--', color=INK, lw=1.3, label='Exact shocked value')
        a.set(xlabel=r'$r/r_s$ (central window)', ylabel=r'$e(\bar q)/(u_0^2/2)$', xlim=(0, .45))
        a.text(.97, .96, 'First-cell ratio: {:.3f}'.format(diagnostics[geometry][-1]['center_specific_internal_energy_ratio']),
               transform=a.transAxes, ha='right', va='top', fontsize=8, color=ACCENT)
        b.axhline(0, color=INK, lw=.7)
        b.axvline(finest['shock'] / finest['length'], color='#a9bac0', lw=.8, ls=':')
        b.set(xlabel='r / L', ylabel=r'$(\bar\rho-\bar\rho_{exact})/\rho_0$', xlim=(0, 1))
        ns = [record['n'] for record in diagnostics[geometry]]
        for metric, label, style, color in [('density_relative_l1', 'Weighted mean L1', 'o-', '#277181'),
                                             ('density_relative_l2', 'Weighted RMS L2', 's-', ACCENT),
                                             ('density_relative_linf', 'Cell-mean Linf', '^--', '#7b6b8c')]:
            values = np.asarray([record[metric] for record in diagnostics[geometry]])
            if np.any(values <= 0):
                raise ValueError('Zero/nonpositive error cannot be placed on a log axis without a declared display convention')
            c.loglog(ns, values, style, color=color, ms=4, lw=1.4, label=label)
        c.set(xlabel='Radial cells N', ylabel='Relative density norm error')
        c.set_xticks(ns); c.set_xticklabels([str(n) for n in ns]); c.xaxis.set_minor_locator(NullLocator())
        c.grid(True, which='major', alpha=.7)
        c.legend(loc='best', fontsize=7.7)
        clean_axes(a, GEOMETRY_LABEL[geometry] + ' · origin heating')
        clean_axes(b, GEOMETRY_LABEL[geometry] + ' · signed density error')
        clean_axes(c, GEOMETRY_LABEL[geometry] + ' · whole-domain error')
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.46, .888), ncol=min(4, len(labels)),
               handlelength=2.6, columnspacing=2.5, fontsize=8)
    fig.text(.065, .063, 'Origin panels retain every saved value within r <= 0.45 rs; no vertical clipping. Signed error and norms retain the whole domain, including the origin and shock.',
             fontsize=8, color=MUTED)
    fig.text(.065, .036, 'Relative norms divide each volume-weighted density error norm by the matching exact-density norm. Cylindrical weights use radial cell volumes.',
             fontsize=8, color=MUTED)
    fig.text(.065, .009, 'A shock/center layer can keep Linf large while integrated errors decrease; no universal convergence order is inferred.',
             fontsize=8, color=MUTED)
    fig.subplots_adjust(left=.065, right=.975, bottom=.17, top=.77, hspace=.64, wspace=.37)
    return save_figure(fig, output, 'noh-errors', 160, plt)


def render(results, output, geometry='cylindrical'):
    source = Path(results).resolve()
    payload, parameters, groups, receipts = load_results(source)
    if geometry not in groups:
        raise ValueError('Thumbnail geometry is not present in saved results: ' + geometry)
    output = Path(output).resolve(); output.mkdir(parents=True, exist_ok=True)
    plt = configure()
    diagnostics = reductions(groups, parameters)
    files = thumbnail(groups, parameters, output, geometry, plt)
    files += profiles(groups, parameters, output, plt)
    files += errors(groups, parameters, diagnostics, output, plt)
    manifest = {
        'schema_version': 1,
        'calculation_kind': 'one-dimensional finite volume; planar and cylindrical radial equations',
        'picture_kind': 'piecewise-constant radial density rotated for display' if geometry == 'cylindrical'
                        else 'piecewise-constant planar density mirrored and extruded for display',
        'not_a_two_dimensional_euler_calculation': True,
        'gallery_caption': {
            'ja': '円筒対称1次元Noh計算の密度セル平均を回転表示。右は同じセルでの厳密平均との比較。2次元Euler計算ではありません。'
                  if geometry == 'cylindrical' else '平面1次元Noh計算の密度セル平均を鏡映・延長表示。2次元Euler計算ではありません。',
            'en': 'Density cell means from a cylindrical 1D Noh run, rotated for display; the profile compares exact means on the same cells. Not a 2D Euler calculation.'
                  if geometry == 'cylindrical' else 'Planar 1D Noh density cell means, mirrored and extruded for display. Not a 2D Euler calculation.',
        },
        'source_sha256': receipts,
        'plot_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'reference': {'citation': 'Noh (1987), J. Comput. Phys. 72, 78-120',
                      'doi': '10.1016/0021-9991(87)90074-X',
                      'representation': INPUT_SCHEMA['representation']},
        'plot_reductions': {'definition': 'L1=sum(V*abs(error))/sum(V*abs(exact)); L2=sqrt(sum(V*error^2)/sum(V*exact^2)); Linf=max(abs(error))/max(abs(exact)). Compared with the saved run metrics. No solver execution.',
                            'records': diagnostics},
        'figures': files,
    }
    (output / 'figure-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--results', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--thumbnail-geometry', choices=sorted(GEOMETRY_LABEL), default='cylindrical')
    parser.add_argument('--describe-input', action='store_true')
    args = parser.parse_args()
    if args.describe_input:
        print(json.dumps(INPUT_SCHEMA, ensure_ascii=False, indent=2)); return
    if args.results is None or args.output is None:
        parser.error('--results and --output are required unless --describe-input is used')
    manifest = render(args.results, args.output, args.thumbnail_geometry)
    print(json.dumps({'figures': manifest['figures'], 'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
