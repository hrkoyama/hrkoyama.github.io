#!/usr/bin/env python3
"""Publication figures from saved Noh finite-volume data; never run a solver.

Usage (numpy/matplotlib/Pillow are the only plotting dependencies)::

    python plot_noh.py --describe-input
    python plot_noh.py --results results/results.json --output figures

The JSON contains metadata and a flat runs list. Each run supplies geometry
('planar', 'cylindrical' or 'spherical'), n, time, and profile (relative CSV path). Metadata
supplies gamma, rho0, u0 and p0, directly or under 'parameters'. See INPUT_SCHEMA.

CSV exact_rho/momentum/total_energy are exact *volume cell means*. The other
exact_* columns are primitive variables recovered from those exact means;
exact_pressure_average is the independently averaged physical pressure.
These two pressures are deliberately shown as different curves.

The cylindrical picture rotates a piecewise-constant 1D radial density profile
for display. The spherical picture is its z=0 radial section, with
r=sqrt(x*x+y*y). Neither is a Cartesian multi-dimensional Euler calculation
or a measurement of angular symmetry errors.
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
        'geometry': 'planar | cylindrical | spherical; one-dimensional FV in every case',
        'n': 'number of cells', 'time': 'actual final time > 0',
        'profile': 'profiles/cylindrical-n512.csv (relative to results JSON)',
        'metrics': 'optional for planar/cylindrical; spherical budgets require saved integral, dt_cubed_sum and boundary-bias diagnostics; never overwritten',
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
        'spherical_display': 'z=0 section of 1D spherical-radial cell means, r=sqrt(x^2+y^2); not Cartesian 3D Euler',
    },
}

INK = '#173747'
MUTED = '#586d78'
ACCENT = '#b45335'
GRID = '#dce5e8'
COLORS = ('#8baebf', '#4b899c', '#277181', '#b45335', '#754b6e')
GEOMETRY_ORDER = ('planar', 'cylindrical', 'spherical')
GEOMETRY_LABEL = {'planar': 'Planar', 'cylindrical': 'Cylindrical',
                  'spherical': 'Spherical-radial'}
GEOMETRY_DIMENSION = {'planar': 1, 'cylindrical': 2, 'spherical': 3}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


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
    receipts = {path.name: digest(path)}
    required = [name for name in INPUT_SCHEMA['csv_columns'] if not name.startswith('mask_')]
    for record in payload['runs']:
        geometry = record['geometry']
        if geometry not in GEOMETRY_LABEL:
            raise ValueError('Unsupported geometry: ' + str(geometry))
        dimension = GEOMETRY_DIMENSION[geometry]
        if record.get('dimension', dimension) != dimension:
            raise ValueError('Saved geometry and dimension disagree')
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
        if not np.allclose(columns['volume'], (right**dimension - left**dimension) / dimension,
                           rtol=2e-12, atol=1e-16):
            raise ValueError('Saved weights do not match the declared radial geometry')
        shock = abs(parameters['u0']) * time * (parameters['gamma'] - 1) / 2
        if not 0 < shock < right[-1]:
            raise ValueError('Analytic shock must remain inside the saved domain')
        # This is the same formula used in the saved exact reference, used only
        # as a locator. No point-sampled curve replaces exact CSV cell means.
        row = dict(record=record, geometry=geometry, n=n, time=time, data=columns,
                   edges=np.r_[left, right[-1]], shock=shock, length=float(right[-1]),
                   reconstruction=reconstruction_mode(payload, record),
                   stress_quadrature=stress_mode(payload, record))
        groups.setdefault(geometry, []).append(row)
        profile_hash = digest(profile)
        if record.get('profile_sha256', profile_hash) != profile_hash:
            raise ValueError('Profile does not match its numerical-result receipt: ' + profile.name)
        receipts[profile.relative_to(path.parent).as_posix()] = profile_hash
        if record.get('history'):
            history = (path.parent / record['history']).resolve()
            if path.parent not in history.parents:
                raise ValueError('History must remain inside the results package')
            history_hash = digest(history)
            if record.get('history_sha256', history_hash) != history_hash:
                raise ValueError('History does not match its numerical-result receipt: ' + history.name)
            receipts[history.relative_to(path.parent).as_posix()] = history_hash
    if not groups:
        raise ValueError('No saved runs to plot')
    for geometry, rows in groups.items():
        rows.sort(key=lambda row: row['n'])
        if len({row['time'] for row in rows}) != 1 or len({row['length'] for row in rows}) != 1:
            raise ValueError('A grid-convergence family must share final time and domain: ' + geometry)
    return payload, parameters, groups, receipts


def supporting_provenance(source, payload):
    """Record saved execution/source receipts without a post-render hash cycle."""
    execution = payload.get('receipts', {})
    expected = dict(execution.get('source_sha256', {}))
    expected.update({name: execution[key] for name, key in
                     [('inputs.json', 'input_sha256'), ('acceptance.json', 'acceptance_sha256'),
                      ('spherical-acceptance.json', 'spherical_acceptance_sha256')]
                     if execution.get(key)})
    if execution.get('spherical_pre_run_contract_sha256'):
        active = execution.get('spherical_pre_run_contract_filename', 'pre-run-contract-spherical.json')
        if not isinstance(active, str) or Path(active).name != active:
            raise ValueError('Expected a local pre-run receipt filename')
        expected[active] = execution['spherical_pre_run_contract_sha256']
    if execution.get('spherical_original_pre_run_contract_sha256'):
        expected['pre-run-contract-spherical.json'] = execution['spherical_original_pre_run_contract_sha256']
    candidates = [source.parent.parent, source.parent.parent / 'source',
                  Path(__file__).resolve().parent]
    verified = {}
    support = {}
    for directory in candidates:
        matched = {}
        for name, expected_hash in expected.items():
            target = directory / name
            if target.is_file() and digest(target) == expected_hash:
                matched[name] = expected_hash
        # Packaging QA is a consumer of the finished figures, not a figure
        # input; hashing it here would create a circular artifact dependency.
        names = ['exactpack-reference-snapshot.json', 'exactpack-reference-receipt.json',
                 'unit-tests-receipt.json']
        names += [item.name for item in directory.glob('pre-run-contract*.json')]
        if matched and all(name in matched for name in expected):
            if not verified:
                verified = matched
            for name in names:
                target = directory / name
                if target.is_file() and name not in support:
                    support[name] = digest(target)
    for name in ['execution-receipt.json', 'execution-start.json', 'pre-run-review.json',
                 'r3-preservation-comparison.json', 'spherical-attempt-summary.json']:
        target = source.parent.parent / name
        if target.is_file():
            support['attempt/' + name] = digest(target)
    return {'saved_execution_receipts': execution,
            'verified_source_and_input_sha256': verified,
            'supporting_receipt_sha256': support,
            'plot_script_sha256': {Path(__file__).name: digest(__file__)},
            'receipt_scope': 'Execution receipts and numerical/reference pre-render evidence only; post-render packaging QA is excluded to avoid a hash cycle.'}


def stress_mode(payload, record):
    metadata = payload['metadata']
    declared = record.get('stress_quadrature') or metadata.get(
        'stress_quadrature_by_geometry', {}).get(record['geometry']) or metadata.get('stress_quadrature')
    if declared:
        return declared
    # The retained first spherical attempt predates the option field and
    # explicitly describes its arithmetic-face rule in physical metadata.
    if metadata.get('geometric_source', '').startswith('arithmetic face quadrature'):
        return 'arithmetic-face'
    return None


def reconstruction_mode(payload, record):
    metadata = payload['metadata']
    return record.get('reconstruction') or metadata.get(
        'reconstruction_by_geometry', {}).get(record['geometry']) or metadata.get('reconstruction')


def load_spherical_comparison(source, payload, parameters, groups, comparison_results=None,
                              secondary_comparison_results=None):
    import numpy as np
    if 'spherical' not in groups:
        if comparison_results is not None or secondary_comparison_results is not None:
            raise ValueError('A spherical baseline requires spherical current results')
        return None
    current = groups['spherical'][-1]
    reconstruction = reconstruction_mode(payload, current['record'])
    if (stress_mode(payload, current['record']) != 'linear-radial-stress'
            or reconstruction not in ('piecewise-constant', 'muscl-minmod')):
        if comparison_results is not None or secondary_comparison_results is not None:
            raise ValueError('The source-comparison panel requires a declared linear-radial-stress current run')
        return None
    specifications = [('spherical-01', 'arithmetic-face', comparison_results,
                       'arithmetic stress (failed)')]
    if reconstruction == 'muscl-minmod':
        specifications.append(('spherical-02', 'linear-radial-stress', secondary_comparison_results,
                               'linear stress / constant (failed)'))
    elif secondary_comparison_results is not None:
        raise ValueError('The second baseline is reserved for a declared MUSCL/minmod current run')
    baselines, manifests = [], []
    for attempt, expected_mode, explicit, label in specifications:
        relative = Path('attempts') / attempt / 'results/results.json'
        candidates = [Path(explicit).resolve()] if explicit is not None else [
            source.parent.parent / relative, Path(__file__).resolve().parent / relative]
        target = next((candidate for candidate in candidates if candidate.is_file()), None)
        if target is None:
            if explicit is not None:
                raise ValueError('Missing explicitly requested saved spherical baseline')
            continue
        target = target.resolve()
        if target == source:
            raise ValueError('A source comparison cannot compare a result with itself')
        baseline, physical, families, receipts = load_results(target)
        if baseline.get('passed') is not False or 'spherical' not in families:
            raise ValueError('Use a retained failed spherical baseline, not a successful or unclassified result')
        rows = [row for row in families['spherical'] if row['n'] == current['n']]
        if len(rows) != 1:
            raise ValueError('Baseline must contain the same finest spherical mesh')
        previous = rows[0]
        if (stress_mode(baseline, previous['record']) != expected_mode
                or reconstruction_mode(baseline, previous['record']) != 'piecewise-constant'):
            raise ValueError('Baseline does not declare its expected stress and constant-reconstruction options')
        if physical != parameters or previous['time'] != current['time']:
            raise ValueError('Source comparison requires identical physical parameters and final time')
        for name in ['flux', 'time_integrator', 'cfl', 'state_floor']:
            if baseline['metadata'].get(name) != payload['metadata'].get(name):
                raise ValueError('Source comparison changes another declared algorithm option: ' + name)
        for name in ['edges', 'length']:
            if not np.array_equal(previous[name], current[name]):
                raise ValueError('Source comparison requires identical cell edges and domain')
        for name in ['volume'] + [key for key in current['data'] if key.startswith('exact_')]:
            if not np.array_equal(previous['data'][name], current['data'][name]):
                raise ValueError('Source comparison changes saved weights or exact cell means: ' + name)
        for key in ['acceptance_sha256', 'spherical_acceptance_sha256']:
            value = payload.get('receipts', {}).get(key)
            if not value or baseline.get('receipts', {}).get(key) != value:
                raise ValueError('Source comparison requires unchanged pre-run acceptance receipts: ' + key)
        baselines.append({'run': previous, 'label': label})
        manifests.append({
            'attempt': attempt, 'kind': 'retained failed constant-reconstruction spherical baseline',
            'validation_passed': False, 'n': previous['n'], 'time': previous['time'],
            'stress_quadrature': expected_mode, 'reconstruction': 'piecewise-constant',
            'center_max_sie_relative_excess': previous['record']['metrics']['center_max_sie_relative_excess'],
            'failed_checks': [check['name'] for check in baseline.get('checks', []) if check.get('passed') is False],
            'source_sha256': receipts, 'provenance': supporting_provenance(target, baseline)})
    if not baselines:
        return None
    return {'baselines': baselines, 'manifest': {
        'kind': 'same-mesh source/reconstruction comparison with retained failed baselines',
        'current_source': 'linear-radial-stress', 'current_reconstruction': reconstruction,
        'current_center_max_sie_relative_excess': current['record']['metrics']['center_max_sie_relative_excess'],
        'current_face_limiter': ('one common theta for all conserved components and both faces; cell means unchanged'
                                 if reconstruction == 'muscl-minmod' else None),
        'current_validation_passed': payload.get('passed') is True,
        'same_mesh_and_physical_parameters': True, 'acceptance_unchanged': True,
        'acceptance_sha256': {key: payload['receipts'][key] for key in
                              ['acceptance_sha256', 'spherical_acceptance_sha256']},
        'baselines': manifests}}


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


def symmetric_log_y(ax, threshold):
    import matplotlib
    version = tuple(int(part) for part in matplotlib.__version__.split('.')[:2])
    keyword = 'linthreshy' if version < (3, 3) else 'linthresh'
    ax.set_yscale('symlog', **{keyword: threshold})


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


def validation_stamp(fig, note, thumbnail=False):
    if note:
        fig.text(.95 if thumbnail else .975, .985, note, ha='right', va='top',
                 fontsize=6.7 if thumbnail else 8, color=ACCENT, weight='semibold')


def thumbnail(groups, parameters, output, geometry, plt, status_note=None):
    import numpy as np
    from matplotlib.patches import Circle
    run = groups[geometry][-1]
    fig = plt.figure(figsize=(6.4, 3.8), dpi=130)
    validation_stamp(fig, status_note, thumbnail=True)
    fig.text(.07, .945, 'NOH  /  CONVERGING FLOW', fontsize=15, weight='semibold')
    method = {'planar': '1D planar FV', 'cylindrical': '1D cylindrical-radial FV',
              'spherical': '1D spherical-radial FV; radial section'}[geometry]
    if run['reconstruction'] == 'muscl-minmod':
        method = method.replace('; radial section', '')
        method += r'  ·  MUSCL + common $\theta$'
    fig.text(.07, .89, method + '  ·  N = ' + str(run['n']) + '  ·  t = {:g}'.format(run['time']),
             fontsize=8.8, color=MUTED)
    field = fig.add_axes([.075, .30, .405, .53])
    profile = fig.add_axes([.655, .28, .295, .55])
    half = min(run['length'] / math.sqrt(2), max(2 * run['shock'], .32 * run['length']))
    side = 420
    coordinates = (np.arange(side) + .5) * (2 * half / side) - half
    xx, yy = np.meshgrid(coordinates, coordinates)
    radius = np.sqrt(xx * xx + yy * yy) if geometry != 'planar' else np.abs(xx)
    index = np.searchsorted(run['edges'], radius, side='right') - 1
    valid = (index >= 0) & (index < run['n'])
    display = np.full(radius.shape, np.nan)
    display[valid] = run['data']['rho'][index[valid]] / parameters['rho0']
    im = field.imshow(display, origin='lower', extent=[-half, half, -half, half],
                      interpolation='nearest', cmap='viridis', aspect='equal',
                      vmin=min(1., float(np.nanmin(display))), vmax=float(np.nanmax(display)))
    if geometry != 'planar':
        field.add_patch(Circle((0, 0), run['shock'], fill=False, ec='white', lw=1, ls='--'))
    else:
        for x in (-run['shock'], run['shock']):
            field.axvline(x, color='white', ls='--', lw=1)
    field.set(xlabel='Display x / L', ylabel='Display y / L')
    field_title = {'planar': 'Mirrored / extruded 1D density',
                   'cylindrical': 'Rotated 1D density',
                   'spherical': r'$z=0$ section of saved 1D $\rho(r)$'}[geometry]
    field.set_title(field_title,
                    fontsize=9, loc='left', pad=9)
    tick = round(half / run['length'], 2)
    field.set_xticks([-half, 0, half]); field.set_xticklabels(['-' + str(tick), '0', str(tick)])
    field.set_yticks([-half, 0, half]); field.set_yticklabels(['-' + str(tick), '0', str(tick)])
    barax = fig.add_axes([.505, .33, .014, .43])
    bar = fig.colorbar(im, cax=barax)
    bar.ax.set_title(r'$\bar\rho/\rho_0$', fontsize=9, pad=8)
    bar.ax.tick_params(labelsize=8, length=2)
    staircase(profile, run, 'exact_rho', parameters['rho0'], color=INK, ls='--', lw=1.4,
              label='Noh exact cell means', zorder=4)
    staircase(profile, run, 'rho', parameters['rho0'], color=ACCENT, lw=1.65,
              label='Finite volume', zorder=3)
    profile.axvline(run['shock'] / run['length'], color='#93a6ac', ls=':', lw=.8)
    profile.set(xlabel='r / L', ylabel=r'$\bar\rho/\rho_0$', xlim=(0, 1))
    clean_axes(profile, 'Radial cell means' if geometry != 'planar' else 'Planar cell means')
    profile.set_ylim(bottom=0)
    profile.legend(loc='upper right', fontsize=7.1, handlelength=2)
    notes = {
        'planar': ('Mirrored / extruded 1D data; not a 2D Euler calculation.',
                   'The cold flow moves inward; the shock moves outward.'),
        'cylindrical': ('Rotated 1D radial data; not a 2D Euler calculation.',
                       'The cold flow moves inward; the shock moves outward.'),
        'spherical': (r'$z=0$ display of 1D radial data, $r=\sqrt{x^2+y^2}$.',
                      'Not a Cartesian 3D calculation; no angular-symmetry test.'),
    }[geometry]
    fig.text(.07, .12, notes[0], fontsize=7.8, color=MUTED)
    fig.text(.07, .079, notes[1], fontsize=7.8, color=MUTED)
    fig.text(.07, .035, r'Cold ideal gas  ·  $\gamma=5/3$, $\rho_0=1$, $u_0=-1$, $p_0=0$'
             if abs(parameters['gamma'] - 5 / 3) < 1e-12 and parameters['rho0'] == 1 and parameters['u0'] == -1
             else conditions(parameters, groups), fontsize=8, color=MUTED)
    return save_figure(fig, output, 'noh-preview', 130, plt)


def profiles(groups, parameters, output, plt, status_note=None):
    geometries = [g for g in GEOMETRY_ORDER if g in groups]
    height = 3.3 * len(geometries) + 1.75
    fig, axes = plt.subplots(len(geometries), 3, figsize=(12.8, height), squeeze=False)
    validation_stamp(fig, status_note)
    fig.suptitle('Noh shock  |  conserved cell averages and recovered primitives',
                 x=.065, y=1-.22/height, ha='left', fontsize=16, weight='semibold')
    fig.text(.065, 1-.64/height, conditions(parameters, groups), fontsize=9, color=MUTED)
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
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.52, 1-.92/height), ncol=3,
               columnspacing=2.2, handlelength=2.7, fontsize=8)
    fig.text(.065, .50/height, 'References use the same cells and volume weights. Velocity and solid/dashed pressure are recovered from conserved means.',
             fontsize=8, color=MUTED)
    fig.text(.065, .25/height, 'The dotted pressure curve is the separate volume average of physical pressure; it differs inside the shock cell. No pressure floor is inserted.',
             fontsize=8, color=MUTED)
    fig.subplots_adjust(left=.065, right=.975, bottom=1.35/height, top=1-1.8/height,
                        hspace=.64, wspace=.36)
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
            reduced = {'n': run['n'], 'density_relative_l1': l1,
                       'density_relative_l2': l2,
                       'density_relative_linf': linf,
                       'center_specific_internal_energy_ratio': float(data['specific_internal_energy'][0] / data['exact_specific_internal_energy'][0])}
            if geometry == 'spherical':
                core = data['r_right'] <= .70 * run['shock']
                if not np.any(core):
                    raise ValueError('No cells in the declared spherical core')
                core_l1 = float(np.sum(data['volume'][core] * np.abs(error[core])) /
                                np.sum(data['volume'][core] * np.abs(exact[core])))
                saved = run['record'].get('metrics', {}).get('core_density_l1')
                if saved is not None and not np.isclose(float(saved), core_l1, rtol=2e-12, atol=2e-14):
                    raise ValueError('Saved and plotted core error definitions disagree')
                reduced['core_density_relative_l1'] = core_l1
                reduced['core_cells'] = int(np.count_nonzero(core))
            values.append(reduced)
        out[geometry] = values
    return out


def errors(groups, parameters, diagnostics, output, plt, status_note=None):
    import numpy as np
    from matplotlib.ticker import NullLocator
    geometries = [g for g in GEOMETRY_ORDER if g in groups]
    height = 3.35 * len(geometries) + 1.85
    fig, axes = plt.subplots(len(geometries), 3, figsize=(12.8, height), squeeze=False)
    validation_stamp(fig, status_note)
    fig.suptitle('Noh verification  |  origin heating, local errors and grid refinement',
                 x=.065, y=1-.22/height, ha='left', fontsize=15, weight='semibold')
    fig.text(.065, 1-.64/height, conditions(parameters, groups), fontsize=9, color=MUTED)
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
               transform=a.transAxes, ha='right', va='top', fontsize=8, color=ACCENT,
               bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .8, 'pad': 2})
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
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.46, 1-.92/height), ncol=min(4, len(labels)),
               handlelength=2.6, columnspacing=2.5, fontsize=8)
    fig.text(.065, .73/height, 'Origin panels retain every saved value within r <= 0.45 rs; no vertical clipping. Signed error and norms retain the whole domain, including the origin and shock.',
             fontsize=8, color=MUTED)
    fig.text(.065, .47/height, 'Relative norms use matching exact-density norms. Volume measures: planar dr; cylindrical r dr; spherical r^2 dr. No center/shock exclusion.',
             fontsize=8, color=MUTED)
    fig.text(.065, .21/height, 'A shock/center layer can keep Linf large while integrated errors decrease; no universal convergence order is inferred.',
             fontsize=8, color=MUTED)
    fig.subplots_adjust(left=.065, right=.975, bottom=1.55/height, top=1-1.65/height,
                        hspace=.64, wspace=.37)
    return save_figure(fig, output, 'noh-errors', 160, plt)


def spherical_budget_records(groups, parameters, diagnostics):
    """Reduce saved sphere receipts; never infer a numerical time history."""
    import numpy as np
    records = []
    for run, reduced in zip(groups['spherical'], diagnostics['spherical']):
        metrics = run['record'].get('metrics', {})

        def saved(name):
            value = metrics.get(name)
            if value is None or isinstance(value, bool) or not math.isfinite(float(value)):
                raise ValueError('Spherical budget requires a finite saved metric: ' + name)
            return float(value)

        dt_cubed = saved('dt_cubed_sum')
        if dt_cubed <= 0:
            raise ValueError('A completed spherical run must record a positive sum(dt^3)')
        record = {'n': run['n'], 'dt_cubed_sum': dt_cubed,
                  'core_density_relative_l1': reduced['core_density_relative_l1'],
                  'density_relative_l1': reduced['density_relative_l1']}
        final = np.asarray(metrics['final_integral'], dtype=float)
        closure = np.asarray(metrics['conservation_residual'], dtype=float)
        if final.shape != (3,) or closure.shape != (3,) or not np.isfinite([final, closure]).all():
            raise ValueError('Spherical budget requires finite three-component saved integrals')
        for kind, component in [('mass', 0), ('energy', 2)]:
            analytic = saved('analytic_total_' + kind)
            actual = saved(kind + '_vs_analytic_signed')
            expected = saved(kind + '_temporal_bias_expected')
            corrected = saved(kind + '_temporal_bias_residual_signed_relative')
            formula = parameters['rho0'] * abs(parameters['u0'])**3 * dt_cubed / 6
            if kind == 'energy':
                formula *= .5 * parameters['u0']**2
            if not (np.isclose(actual, final[component] - analytic, rtol=2e-12, atol=2e-14)
                    and np.isclose(expected, formula, rtol=2e-12, atol=2e-14)
                    and np.isclose(corrected, (actual - expected) / abs(analytic),
                                   rtol=2e-12, atol=2e-14)):
                raise ValueError('Saved spherical budget metrics disagree with their stated reduction: ' + kind)
            record[kind + '_closure_absolute_relative'] = float(abs(closure[component]) / abs(final[component]))
            record[kind + '_analytic_signed_difference'] = actual
            record[kind + '_bias_formula'] = expected
            record[kind + '_bias_residual_signed_relative'] = corrected
        records.append(record)
    return records


def spherical_budget(groups, parameters, diagnostics, records, output, plt, status_note=None,
                     comparison=None):
    import numpy as np
    from matplotlib.ticker import NullLocator
    rows = groups['spherical']
    ns = [record['n'] for record in records]
    fig, axes = plt.subplots(2, 3, figsize=(12.8, 8.9), squeeze=False)
    validation_stamp(fig, status_note)
    fig.suptitle('Spherical Noh  |  boundary budgets and the unresolved origin',
                 x=.065, y=.972, ha='left', fontsize=15, weight='semibold')
    fig.text(.065, .925, conditions(parameters, groups), fontsize=9, color=MUTED)
    if comparison is not None:
        summary = comparison['manifest']
        old_excess = [float(item['center_max_sie_relative_excess']) for item in summary['baselines']]
        current_excess = float(summary['current_center_max_sie_relative_excess'])
        if not all(math.isfinite(value) for value in old_excess + [current_excess]):
            raise ValueError('Center-heating comparison requires finite saved excess metrics')
        old_text = ', '.join('failed {:02d} {:+.1f}%'.format(i+1, 100*value)
                             for i, value in enumerate(old_excess))
        method = 'MUSCL' if summary['current_reconstruction'] == 'muscl-minmod' else 'constant'
        note = ('N={} center max internal-energy excess: {}; current {} {:+.1f}%'.format(
            rows[-1]['n'], old_text, method, 100*current_excess))
        if current_excess > max(old_excess):
            note += ' (higher).'
        else:
            note += '.'
        fig.text(.065, .885, note, fontsize=8.5, color=ACCENT)
    a, b, c = axes[0]
    d, e, f = axes[1]
    for kind, name, color, marker in [('mass', 'Mass', '#277181', 'o'),
                                      ('energy', 'Energy', ACCENT, 's')]:
        a.plot(ns, [r[kind + '_closure_absolute_relative'] for r in records],
               marker + '-', color=color, ms=4, lw=1.35, label=name)
        b.plot(ns, [r[kind + '_analytic_signed_difference'] for r in records],
               marker, color=color, ms=5, markerfacecolor='white', label=name + ': saved excess')
        b.plot(ns, [r[kind + '_bias_formula'] for r in records],
               '--' if kind == 'mass' else ':', color=color, lw=1.5, label=name + ': RK2 formula')
        c.plot(ns, [r[kind + '_bias_residual_signed_relative'] for r in records],
               marker + '-', color=color, ms=4, lw=1.35, label=name)
    symmetric_log_y(a, 1e-16)
    a.set_ylabel('Absolute closure / final integral')
    symmetric_log_y(b, 1e-15)
    b.set_ylabel('Signed integral excess\n(numerical - exact)')
    symmetric_log_y(c, 1e-16)
    c.set_ylabel('Bias-corrected excess\n/ exact integral')
    for ax in (a, b, c):
        ax.axhline(0, color=INK, lw=.65, zorder=0)
        ax.set_xlabel('Radial cells N')
        ax.legend(loc='best', fontsize=7.3, handlelength=2)
    for key, name, style, color in [
            ('density_relative_l1', 'Whole domain, including shock', 'o-', '#277181'),
            ('core_density_relative_l1', 'Core, including origin', 's-', ACCENT)]:
        values = np.asarray([r[key] for r in records])
        if np.any(values <= 0):
            raise ValueError('Positive saved core and whole-domain L1 errors required for log display')
        d.loglog(ns, values, style, color=color, lw=1.4, ms=4, label=name)
    d.set(xlabel='Radial cells N', ylabel='Relative density L1\n(volume weighted)')
    d.legend(loc='best', fontsize=7.1)
    reference_energy = .5 * parameters['u0']**2
    reference_density = parameters['rho0'] * ((parameters['gamma'] + 1) /
                                               (parameters['gamma'] - 1))**3
    for i, run in enumerate(rows):
        data = run['data']; color = COLORS[i % len(COLORS)]
        center = data['r_center'] <= .25 * run['shock']
        core = data['r_right'] <= .70 * run['shock']
        if not np.any(center) or not np.any(core):
            raise ValueError('No saved cells in a declared spherical origin/core display window')
        e.plot(data['r_center'][center] / run['shock'],
               data['specific_internal_energy'][center] / reference_energy,
               '-o', color=color, lw=1.3 if i == len(rows)-1 else .9,
               ms=3 if run['n'] <= 128 else 1.8, label='N = ' + str(run['n']))
        if comparison is None:
            f.plot(data['r_center'][core] / run['shock'],
                   (data['rho'][core] - data['exact_rho'][core]) / reference_density,
                   '-o', color=color, lw=1.3 if i == len(rows)-1 else .9,
                   ms=3 if run['n'] <= 128 else 1.8, label='N = ' + str(run['n']))
    e.axhline(1, color=INK, ls='--', lw=1.2)
    e.set(xlabel=r'$r/r_s$ (origin window)', ylabel=r'$e(\bar q)/(u_0^2/2)$', xlim=(0, .25))
    e.legend(loc='best', fontsize=7.1, ncol=2)
    if comparison is None:
        f.axhline(0, color=INK, lw=.7)
        f.set(xlabel=r'$r/r_s$ (core, including origin)',
              ylabel=r'$(\bar\rho-\bar\rho_{exact})/\rho_{post}$', xlim=(0, .70))
        comparison_title = 'Signed core density error'
    else:
        current = rows[-1]
        for baseline, color, style in zip(comparison['baselines'], ['#7b6b8c', '#4b899c'], ['-.', ':']):
            staircase(f, baseline['run'], 'rho', parameters['rho0'], color=color,
                      lw=1.4, ls=style, label=baseline['label'])
        method = r'MUSCL + $\theta$' if comparison['manifest']['current_reconstruction'] == 'muscl-minmod' else 'constant'
        label = 'linear / ' + method + ' (' + ('passed' if comparison['manifest']['current_validation_passed'] else 'failed') + ')'
        staircase(f, current, 'rho', parameters['rho0'], color=ACCENT, lw=1.5, label=label)
        staircase(f, current, 'exact_rho', parameters['rho0'], color=INK, lw=1.2,
                  ls='--', label='Noh exact cell means')
        f.axvline(current['shock'] / current['length'], color='#a9bac0', lw=.8, ls=':')
        f.set(xlabel='r / L (origin and shock)', ylabel=r'$\bar\rho/\rho_0$',
              xlim=(0, min(1., 1.6 * current['shock'] / current['length'])))
        f.legend(loc='lower left', fontsize=6.9, handlelength=2.2)
        comparison_title = 'Source comparison · N = ' + str(current['n'])
    for ax in (a, b, c, d):
        ax.set_xscale('log')
        ax.set_xticks(ns); ax.set_xticklabels([str(n) for n in ns])
        ax.xaxis.set_minor_locator(NullLocator())
    for ax, title in zip(axes.flat, [
            'Discrete mass / energy closure', 'Analytic excess and RK2 prediction',
            'Bias-corrected closure', 'Whole-domain / core density errors',
            'Origin heating (unclipped)', comparison_title]):
        clean_axes(ax, title)
    fig.text(.065, .103, r'Sphere: $V=(r_R^3-r_L^3)/3$; angular factor omitted. $M_{exact}=\rho_0(R+|u_0|t)^3/3$, $E_{exact}=u_0^2 M_{exact}/2$.',
             fontsize=8, color=MUTED)
    fig.text(.065, .073, r'RK2 boundary quadrature: $\Delta M=\rho_0|u_0|^3\sum\Delta t^3/6$, $\Delta E=u_0^2\Delta M/2$. Symmetric-log budget axes retain zero and either sign.',
             fontsize=8, color=MUTED)
    fig.text(.065, .043, 'Core L1 uses cells with right edge <= 0.70 rs and includes the origin. Each L1 has its own exact mass denominator; it does not replace the full-domain check.',
             fontsize=8, color=MUTED)
    footer = ('Same frozen gates, physical parameters and mesh. All displayed constant baselines failed; MUSCL uses one common theta per cell, preserving its mean.'
              if comparison is not None and comparison['manifest']['current_reconstruction'] == 'muscl-minmod' else
              'Same pre-run gates, physical parameters and mesh. The constant-reconstruction arithmetic-stress baseline failed; current options are named in the legend.'
              if comparison is not None else
              'Saved 1D spherical-radial FV only. Origin/core windows keep every value in their stated windows; no Cartesian 3D or angular-symmetry calculation is shown.')
    fig.text(.065, .013, footer,
             fontsize=8, color=MUTED)
    fig.subplots_adjust(left=.065, right=.975, bottom=.20, top=.835, hspace=.61, wspace=.39)
    return save_figure(fig, output, 'noh-spherical-budget', 160, plt)


def render(results, output, geometry=None, comparison_results=None, secondary_comparison_results=None):
    source = Path(results).resolve()
    payload, parameters, groups, receipts = load_results(source)
    if geometry is None or geometry == 'auto':
        geometry = next(g for g in reversed(GEOMETRY_ORDER) if g in groups)
    if geometry not in groups:
        raise ValueError('Thumbnail geometry is not present in saved results: ' + geometry)
    comparison = load_spherical_comparison(source, payload, parameters, groups, comparison_results,
                                           secondary_comparison_results)
    output = Path(output).resolve(); output.mkdir(parents=True, exist_ok=True)
    plt = configure()
    diagnostics = reductions(groups, parameters)
    status_note = 'DIAGNOSTIC / FAILED ACCEPTANCE' if payload.get('passed') is False else None
    files = thumbnail(groups, parameters, output, geometry, plt, status_note)
    files += profiles(groups, parameters, output, plt, status_note)
    files += errors(groups, parameters, diagnostics, output, plt, status_note)
    budget = []
    if 'spherical' in groups:
        budget = spherical_budget_records(groups, parameters, diagnostics)
        files += spherical_budget(groups, parameters, diagnostics, budget, output, plt, status_note,
                                  comparison=comparison)
    captions = {
        'planar': {
            'ja': '平面1次元Noh計算の密度セル平均を鏡映・延長表示。2次元Euler計算ではありません。',
            'en': 'Planar 1D Noh density cell means, mirrored and extruded for display. Not a 2D Euler calculation.'},
        'cylindrical': {
            'ja': '円筒対称1次元Noh計算の密度セル平均を回転表示。右は同じセルでの厳密平均との比較。2次元Euler計算ではありません。',
            'en': 'Density cell means from a cylindrical 1D Noh run, rotated for display; the profile compares exact means on the same cells. Not a 2D Euler calculation.'},
        'spherical': {
            'ja': '球対称1次元の半径方向Noh計算から密度セル平均をz=0断面として表示（r=√(x²+y²)）。右は同じセルの厳密平均との比較。Cartesian 3次元計算・角方向の対称性検証ではありません。',
            'en': 'A z=0 radial section of density cell means from a 1D spherical-radial Noh run (r=sqrt(x^2+y^2)); the profile compares exact means on the same cells. Not a Cartesian 3D calculation or an angular-symmetry test.'},
    }
    manifest = {
        'schema_version': 1,
        'validation_passed': payload.get('passed') is True,
        'failed_checks': [check['name'] for check in payload.get('checks', []) if check.get('passed') is False],
        'calculation_kind': 'one-dimensional finite volume; ' + ', '.join(g for g in GEOMETRY_ORDER if g in groups),
        'algorithms_by_geometry': {g: {
            'stress_quadrature': stress_mode(payload, groups[g][-1]['record']),
            'reconstruction': reconstruction_mode(payload, groups[g][-1]['record'])}
            for g in GEOMETRY_ORDER if g in groups},
        'reconstruction_scope': 'Saved cell means are displayed piecewise constantly. Face admissibility checks do not establish a general positivity or convergence theorem for radial cold flows.',
        'thumbnail_geometry': geometry,
        'picture_kind': {'planar': 'piecewise-constant planar density mirrored and extruded for display',
                         'cylindrical': 'piecewise-constant radial density rotated for display',
                         'spherical': 'z=0 radial section of piecewise-constant 1D spherical density; r=sqrt(x^2+y^2)'}[geometry],
        'not_a_two_dimensional_euler_calculation': True,
        'not_a_cartesian_three_dimensional_calculation': True,
        'no_angular_symmetry_test': True,
        'gallery_caption': captions[geometry],
        'source_sha256': receipts,
        'provenance': supporting_provenance(source, payload),
        'source_comparison': comparison['manifest'] if comparison is not None else None,
        'plot_script_sha256': digest(__file__),
        'reference': {'citation': 'Noh (1987), J. Comput. Phys. 72, 78-120',
                      'doi': '10.1016/0021-9991(87)90074-X',
                      'representation': INPUT_SCHEMA['representation']},
        'plot_reductions': {'definition': 'L1=sum(V*abs(error))/sum(V*abs(exact)); L2=sqrt(sum(V*error^2)/sum(V*exact^2)); Linf=max(abs(error))/max(abs(exact)). Compared with the saved run metrics. No solver execution.',
                            'records': diagnostics,
                            'spherical_budget': budget,
                            'core_definition': 'Cells with r_right <= 0.70*exact shock radius; the origin is never excluded. Core and whole-domain L1 have separate exact-mass denominators.'},
        'figures': files,
    }
    (output / 'figure-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--results', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--thumbnail-geometry', choices=['auto'] + list(GEOMETRY_ORDER), default='auto')
    parser.add_argument('--comparison-results', type=Path,
                        help='Optional retained failed arithmetic-stress detailed results.json; auto-detected when packaged')
    parser.add_argument('--secondary-comparison-results', type=Path,
                        help='Optional retained failed linear-stress/constant detailed results.json for MUSCL comparison')
    parser.add_argument('--describe-input', action='store_true')
    args = parser.parse_args()
    if args.describe_input:
        print(json.dumps(INPUT_SCHEMA, ensure_ascii=False, indent=2)); return
    if args.results is None or args.output is None:
        parser.error('--results and --output are required unless --describe-input is used')
    manifest = render(args.results, args.output, args.thumbnail_geometry,
                      comparison_results=args.comparison_results,
                      secondary_comparison_results=args.secondary_comparison_results)
    print(json.dumps({'figures': manifest['figures'], 'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
