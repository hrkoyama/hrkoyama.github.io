"""Plot only the eight saved rows; never import a solver or analytic evaluator."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'atlas-vef-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

CASE_IDS = ('vef-fourier-scattering1d', 'vet-fourier-source2d')
ROLES = {'coarse', 'fine', 'angle-probe', 'constant'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows(result_path):
    data = json.loads(result_path.read_text())
    if data.get('passed') is not True or set(data.get('checks', {})) != set(CASE_IDS):
        raise ValueError('Expected a successful fixed two-case result')
    cases = data.get('cases')
    if not isinstance(cases, list) or [row['id'] for row in cases] != list(CASE_IDS):
        raise ValueError('Unexpected case order or identity')
    loaded = {}
    for case in cases:
        records = case['records']
        if len(records) != 4 or {row['role'] for row in records} != ROLES:
            raise ValueError('Expected three variable-source rows and one constant control')
        rows = {}
        for row in records:
            filename = row['arrays']
            expected = case['id']+'--'+row['row_id']+'.npz'
            path = result_path.parent/filename
            if (not isinstance(filename, str)
                    or re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*\.npz', filename) is None
                    or filename != expected or path.is_symlink() or not path.is_file()
                    or path.resolve().parent != result_path.parent):
                raise ValueError('Unsafe or missing saved array member')
            checksum = row.get('arrays_sha256')
            if (not isinstance(checksum, str) or re.fullmatch(r'[0-9a-f]{64}', checksum) is None
                    or sha(path) != checksum):
                raise ValueError('Missing, invalid or changed saved array digest')
            with np.load(path, allow_pickle=False) as archive:
                arrays = {key: archive[key].copy() for key in archive.files}
            required = {'x', 'q', 'E_LO', 'E_HO', 'H_HO', 'K_HO', 'D', 'I',
                        'omega', 'weights', 'Fx_face', 'H_LO_center', 'E_reference',
                        'H_reference', 'K_reference', 'D_reference', 'Hx_reference_face'}
            if case['id'] == CASE_IDS[1]:
                required |= {'y', 'Fy_face', 'Hy_reference_face'}
            if not required.issubset(arrays):
                raise ValueError('Missing saved field: '+str(sorted(required-set(arrays))))
            if any(not np.issubdtype(value.dtype, np.number) or np.iscomplexobj(value)
                   or not np.all(np.isfinite(value)) for value in arrays.values()):
                raise ValueError('Plots require finite real saved numerical arrays')
            shape = arrays['E_LO'].shape
            if arrays['D'].shape != shape+(3, 3) or arrays['H_LO_center'].shape != shape+(3,):
                raise ValueError('Unexpected moment or tensor layout')
            if arrays['I'].shape != (len(arrays['weights']),)+shape:
                raise ValueError('Intensity must have a leading angular axis')
            rows[row['role']] = (row, arrays)
        loaded[case['id']] = rows
    return data, loaded


def periodic_line(x, values):
    """Repeat the saved first point at the periodic endpoint for display only."""
    return np.append(x, 1.0), np.concatenate((values, values[..., :1]), axis=-1)


def field(ax, arrays, values, label, symmetric=False):
    """Periodic endpoint repetition, without recomputing an interior field."""
    n = values.shape[0]
    coord = np.arange(n+1)/n
    wrapped = np.pad(values, ((0, 1), (0, 1)), mode='wrap')
    options = {'cmap': 'viridis'}
    if symmetric:
        scale = float(np.max(np.abs(values)))
        if scale == 0:
            # A display range only: all stored values remain exactly zero.
            scale = 1.0
            label += ' (all values zero)'
        options = {'cmap': 'coolwarm', 'vmin': -scale, 'vmax': scale}
    image = ax.pcolormesh(coord, coord, wrapped.T, shading='gouraud', **options)
    ax.figure.colorbar(image, ax=ax, label=label, shrink=0.88)
    ax.set(xlabel='x / L', ylabel='y / L', xlim=(0, 1), ylim=(0, 1), aspect='equal')
    return image


def main_vef(arrays, path):
    x, mu = arrays['x'], arrays['omega'][:, 0]
    order = np.argsort(mu)
    xp, intensity = periodic_line(x, arrays['I'][order])
    fig, axes = plt.subplots(2, 1, figsize=(10.5, 7.3),
                             gridspec_kw={'height_ratios': [3, 1.35]}, layout='constrained')
    image = axes[0].pcolormesh(xp, mu[order], intensity, shading='auto', cmap='magma')
    fig.colorbar(image, ax=axes[0], label='Normalized intensity I')
    axes[0].set(xlabel='Position x / L', ylabel='Angular cosine mu', xlim=(0, 1), ylim=(-1, 1),
                title='1D space x angular cosine: saved formal-transport intensity')
    xx, f = periodic_line(x, arrays['D'][:, 0, 0])
    _, reference = periodic_line(x, arrays['D_reference'][:, 0, 0])
    axes[1].plot(xx, f, label='Computed f = Kxx / E_HO', lw=2)
    axes[1].plot(xx, reference, '--', label='Continuum reference', lw=1.4)
    axes[1].axhline(1/3, color='0.5', lw=0.8, label='Isotropic 1/3')
    axes[1].set(xlabel='Position x / L', ylabel='Eddington factor f', xlim=(0, 1))
    axes[1].legend(fontsize=8, ncols=3)
    fig.suptitle('Variable Eddington factor | fixed fine grid, separate angular probe')
    fig.savefig(path, dpi=135)
    plt.close(fig)


def main_vet(arrays, path):
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6), layout='constrained')
    field(axes[0], arrays, arrays['E_LO'], 'Normalized moment energy E_LO')
    n = arrays['E_LO'].shape[0]
    stride = max(1, n//8)
    selection = (slice(None, None, stride),)*2
    flow = arrays['H_LO_center']
    arrows = axes[0].quiver(arrays['x'][selection], arrays['y'][selection],
                            flow[..., 0][selection], flow[..., 1][selection],
                            angles='xy', scale_units='xy', scale=1.0, color='white', width=0.004)
    axes[0].quiverkey(arrows, 0.45, 1.035, 0.05, 'H = 0.05 (scale=1)', labelpos='E',
                      coordinates='axes', color='black', fontproperties={'size': 8})
    axes[0].set_title('Saved E_LO and colocated face-averaged H', pad=30)
    field(axes[1], arrays, arrays['D'][..., 0, 1], 'Dxy (symmetric actual range)', symmetric=True)
    axes[1].set_title('Transport-derived off-diagonal tensor component')
    fig.suptitle('Variable Eddington tensor | periodic source, spatial 2D / angular S2')
    fig.savefig(path, dpi=135)
    plt.close(fig)


def errors(arrays):
    e = float(np.sqrt(np.mean((arrays['E_LO']-arrays['E_reference'])**2)) /
              np.sqrt(np.mean(arrays['E_reference']**2)))
    actual = [arrays['Fx_face']]
    ref = [arrays['Hx_reference_face']]
    if arrays['E_LO'].ndim == 2:
        actual.append(arrays['Fy_face'])
        ref.append(arrays['Hy_reference_face'])
    numerator = sum(float(np.sum((a-b)**2)) for a, b in zip(actual, ref))
    denominator = sum(float(np.sum(b*b)) for b in ref)
    if denominator <= 0:
        raise ValueError('Variable-source flux reference must be nonzero')
    return e, float(np.sqrt(numerator/denominator))


def convergence(ax, rows):
    selected = [rows[role] for role in ('coarse', 'fine', 'angle-probe')]
    values = [errors(arrays) for _, arrays in selected]
    ax.plot([0, 1], [values[i][0] for i in (0, 1)], 'o-', label='E: same angular rule')
    ax.plot([0, 1], [values[i][1] for i in (0, 1)], 's-', label='Face H: same angular rule')
    ax.plot(2, values[2][0], 'o', label='E: angular probe')
    ax.plot(2, values[2][1], 's', label='Face H: angular probe')
    ns = [arrays['E_LO'].shape[0] for _, arrays in selected]
    ax.set_xticks([0, 1, 2], ['coarse N='+str(ns[0]), 'fine N='+str(ns[1]), 'angle N='+str(ns[2])])
    ax.set_yscale('log')
    ax.set(ylabel='Relative RMS error', title='Spatial comparison and separate angular probe')
    ax.legend(fontsize=7)


def history(ax, record):
    rows = record['history']
    if not rows:
        raise ValueError('Missing saved fixed-point history')
    for name, label in [('LOE_relative_update', 'E update'), ('D_max_update', 'D update'),
                        ('true_LO_relative_residual', 'True LO residual'),
                        ('HOE_minus_LOE_rms', 'HO-LO gap (study)')]:
        ax.plot([row['outer'] for row in rows], [row[name] for row in rows], '.-', label=label)
    ax.set_yscale('symlog', linthresh=1e-14)
    modes = record['metrics']['source_modes']
    if not modes:
        raise ValueError('Fine variable-source row must retain mode diagnostics')
    mode_label = '\n'.join('k='+str(tuple(mode['wave_numbers']))+
                           ': rel='+format(mode['complex_relative_error'], '.2g')+
                           ', phase='+format(mode['phase_error_radians'], '.2g')+' rad'
                           for mode in modes)
    ax.set(xlabel='Outer iteration', ylabel='Saved norm',
           title='Fine-row history | source-mode errors\n'+mode_label)
    ax.title.set_fontsize(9)
    ax.legend(fontsize=7)


def diagnostics(case_id, rows, path):
    record, arrays = rows['fine']
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout='constrained')
    if arrays['E_LO'].ndim == 1:
        axes[0, 0].plot(arrays['x'], arrays['E_LO']-arrays['E_reference'], 'o-', ms=2,
                        label='E_LO - continuum E')
        axes[0, 0].plot(arrays['x'], arrays['E_HO']-arrays['E_LO'], '--', label='HO - LO')
        axes[0, 0].set(xlabel='x / L', ylabel='Absolute difference', title='Point-sampled energy errors')
        axes[0, 0].legend(fontsize=8)
        faces = (np.arange(len(arrays['x']))+0.5)/len(arrays['x'])
        axes[0, 1].plot(faces, arrays['Fx_face'], 'o', ms=3, label='Shared face Hx')
        axes[0, 1].plot(faces, arrays['Hx_reference_face'], '--', label='Reference at same face')
        axes[0, 1].set(xlabel='Face x / L', ylabel='Normalized Hx', title='Conservative face flux')
        axes[0, 1].legend(fontsize=8)
    else:
        field(axes[0, 0], arrays, arrays['E_LO']-arrays['E_reference'], 'E_LO - E_reference', symmetric=True)
        axes[0, 0].set_title('Saved point-value error')
        field(axes[0, 1], arrays, arrays['D'][..., 2, 2], 'Dzz')
        axes[0, 1].set_title('Retained third angular dimension')
    convergence(axes[1, 0], rows)
    history(axes[1, 1], record)
    fig.suptitle(case_id+' | saved diagnostics; no additional solves')
    fig.savefig(path, dpi=135)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result_path = args.results.resolve()
    _, cases = load_rows(result_path)
    args.output.mkdir(parents=True, exist_ok=True)
    written = []
    for case_id in CASE_IDS:
        primary = args.output/(case_id+'.png')
        extra = args.output/(case_id+'-diagnostics.png')
        if primary.exists() or extra.exists():
            raise ValueError('Refusing to replace an existing figure')
        arrays = cases[case_id]['fine'][1]
        (main_vef if case_id == CASE_IDS[0] else main_vet)(arrays, primary)
        diagnostics(case_id, cases[case_id], extra)
        written += [primary, extra]
    manifest = {'schema_version': 1, 'source_result_sha256': sha(result_path),
                'source_npz': {row['arrays']: sha(result_path.parent/row['arrays'])
                               for rows in cases.values() for row, _ in rows.values()},
                'files': {path.name: sha(path) for path in written},
                'scope': 'Saved fine-row fields and fixed-row diagnostics only; no numerical solver/reference call.'}
    destination = args.output/'plot-manifest.json'
    if destination.exists():
        raise ValueError('Refusing to replace an existing plot manifest')
    destination.write_text(json.dumps(manifest, indent=2)+'\n')


if __name__ == '__main__':
    main()
