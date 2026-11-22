#!/usr/bin/env python3
"""Small linear spatial/RK4 analyses for the KEEP teaching chapter.

Copyright (c) 2026 Hiroshi Koyama. Original analysis script: MIT (see LICENSE).
Existing site terms apply separately to figures
and data. This is not a nonlinear Euler convergence or stability certificate.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import sys
import tempfile

import numpy as np


PUBLIC_BASE = 'https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/'
KEEP_SHA256 = '0819e2c3de3e4ab9ffe763f247a471a21966fde88da6ed13621ae334afc71f91'
SCOPE = ('Uniform-state linearization / linear scalar characteristic mode only; '
         'not the modified wavenumber of nonlinear split products or a nonlinear Euler verification.')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rk4_polynomial(z):
    return 1 + z + z*z/2 + z*z*z/6 + z*z*z*z/24


def rk4_stages(z):
    k1 = z
    k2 = z * (1 + k1/2)
    k3 = z * (1 + k2/2)
    k4 = z * (1 + k3)
    return 1 + (k1 + 2*k2 + 2*k3 + k4)/6


def write_csv(path: Path, columns: list[str], rows):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)


def plot_style(plt):
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 12,
        'axes.titlesize': 13, 'axes.labelsize': 12,
        'legend.fontsize': 10.5, 'xtick.labelsize': 10.5,
        'ytick.labelsize': 10.5, 'figure.facecolor': 'white',
        'axes.facecolor': 'white', 'axes.spines.top': False,
        'axes.spines.right': False, 'savefig.facecolor': 'white',
        'lines.linewidth': 2.2,
    })


def spatial_analysis(output: Path, plt):
    theta = np.linspace(0, np.pi, 513)
    modified = np.sin(theta)
    phase = np.sinc(theta/np.pi)
    group = np.cos(theta)
    write_csv(output/'spatial-dispersion.csv',
              ['theta_kh', 'modified_wavenumber_times_h', 'phase_speed_over_a',
               'group_speed_over_a', 'semidiscrete_modal_gain'],
              zip(theta, modified, phase, group, np.ones_like(theta)))

    blue, orange, gray = '#0072B2', '#D55E00', '#666666'
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.6), dpi=120)
    fig.subplots_adjust(left=.075, right=.98, bottom=.235, top=.82, wspace=.31)
    fig.suptitle('Second-order centered difference: no damping, but phase error', y=.955, fontsize=16)
    axes[0].plot(theta, theta, '--', color=gray, label='Exact: $kh$')
    axes[0].plot(theta, modified, color=blue, label=r'Centered: $\widetilde{k}h=\sin(kh)$')
    axes[0].set(xlabel=r'Dimensionless wavenumber $\theta=kh$',
                ylabel=r'Dimensionless wavenumber', xlim=(0, np.pi), ylim=(-.05, 3.3))
    axes[1].axhline(1, linestyle='--', color=gray, label='Exact speed / $a$')
    axes[1].plot(theta, phase, color=blue, label=r'Phase: $\sin\theta/\theta$')
    axes[1].plot(theta, group, color=orange, label=r'Group: $\cos\theta$')
    axes[1].set(xlabel=r'Dimensionless wavenumber $\theta=kh$',
                ylabel='Speed / characteristic speed $a$', xlim=(0, np.pi), ylim=(-1.1, 1.18))
    for ax in axes:
        ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
                      ['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])
        ax.grid(alpha=.2)
        ax.legend(loc='upper left')
    axes[1].legend(loc='lower left')
    fig.text(.075, .115, 'Scope: uniform-state linearization / linear scalar characteristic mode; semidiscrete in time.', fontsize=10)
    fig.text(.075, .07, 'Each Fourier-mode amplitude is constant here. Short waves have phase error; Nyquist has zero derivative.', fontsize=10)
    fig.text(.075, .025, 'This is not a nonlinear split-product modified-wavenumber curve or a nonlinear Euler verification.', fontsize=9.6)
    fig.savefig(output/'spatial-dispersion.png', dpi=120)
    plt.close(fig)

    # Independently apply the periodic stencil to resolved Fourier vectors.
    n, length, a = 64, 1.0, .4
    h = length/n
    checks = []
    for m in [1, 4, 8, 16, 24, 31, 32]:
        angle = 2*np.pi*m/n
        wave = np.exp(1j*angle*np.arange(n))
        observed = -a*(np.roll(wave, -1)-np.roll(wave, 1))/(2*h)
        expected_lambda = -1j*a*np.sin(angle)/h
        projected_lambda = np.vdot(wave, observed)/np.vdot(wave, wave)
        checks.append({'mode': m, 'theta': float(angle),
                       'expected_lambda_real': 0., 'expected_lambda_imag': float(expected_lambda.imag),
                       'observed_lambda_real': float(projected_lambda.real),
                       'observed_lambda_imag': float(projected_lambda.imag),
                       'projection_residual': float(abs(projected_lambda-expected_lambda)),
                       'maximum_vector_residual': float(np.max(abs(observed-expected_lambda*wave)))})
    max_projection = max(x['projection_residual'] for x in checks)
    max_vector = max(x['maximum_vector_residual'] for x in checks)
    assert max_projection < 2e-12 and max_vector < 5e-12
    return {'scope': SCOPE, 'samples': len(theta),
            'stencil_probe': {'n': n, 'length': length, 'a': a, 'cases': checks,
                              'max_projection_residual': max_projection,
                              'max_vector_residual': max_vector,
                              'acceptance': {'projection_max': 2e-12, 'vector_max': 5e-12}, 'passed': True},
            'nyquist': {'theta': float(np.pi), 'sine_observed': float(modified[-1]),
                        'theoretical_modified_wavenumber': 0., 'phase_speed_ratio_limit': 0.,
                        'meaning': 'Alternating grid values lie in the nullspace of the centered derivative.'}}


def rk4_analysis(output: Path, plt):
    boundary = 2*np.sqrt(2.)
    xi = np.unique(np.r_[np.linspace(0, 3.1, 801), boundary])
    z = -1j*xi
    r = rk4_polynomial(z)
    gain = abs(r)
    phase = -np.unwrap(np.angle(r))
    phase_error = phase-xi
    poly_gain_squared = 1-xi**6/72+xi**8/576
    stage_residual = float(np.max(abs(r-rk4_stages(z))))
    identity_residual = float(np.max(abs(gain**2-poly_gain_squared)))
    assert stage_residual < 2e-14 and identity_residual < 2e-14
    assert abs(abs(rk4_polynomial(-1j*boundary))-1) < 2e-14
    assert abs(rk4_polynomial(-1j*3.)) > 1
    write_csv(output/'rk4-response.csv',
              ['xi_omega_h_dt', 'gain_abs_R', 'gain_squared', 'gain_squared_polynomial',
               'continuous_phase_omega_dt', 'phase_error_omega_dt_minus_xi', 'stable_on_imaginary_axis'],
              zip(xi, gain, gain**2, poly_gain_squared, phase, phase_error, (xi <= boundary).astype(int)))
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.6), dpi=120)
    fig.subplots_adjust(left=.075, right=.98, bottom=.235, top=.82, wspace=.31)
    fig.suptitle('Classical RK4 changes both amplitude and phase', y=.955, fontsize=16)
    blue, orange, gray = '#0072B2', '#D55E00', '#666666'
    axes[0].axhline(1, linestyle='--', color=gray, label='Exact modal gain = 1')
    axes[0].plot(xi, gain, color=blue, label=r'RK4: $|R(-i\xi)|$')
    axes[0].set(ylabel='Amplitude multiplier per step', ylim=(.4, 2.03))
    axes[1].axhline(0, linestyle='--', color=gray, label='Exact phase error = 0')
    axes[1].plot(xi, phase_error, color=orange, label=r'RK4: $\Omega\Delta t-\xi$')
    axes[1].set(ylabel='Phase error per step (radians)', ylim=(-.1, 1.85))
    for ax in axes:
        ax.axvspan(boundary, 3.1, color='#888888', alpha=.13)
        ax.axvline(boundary, color=gray, linewidth=1.2, linestyle=':')
        ax.set(xlabel=r'$\xi=\omega_h\Delta t$ (dimensionless)', xlim=(0, 3.1))
        ax.grid(alpha=.2)
        ax.legend(loc='upper left')
    axes[0].text(boundary-.04, 1.82, r'$2\sqrt{2}$', ha='right', fontsize=11)
    fig.text(.075, .115, 'Scope: one linear mode with a purely imaginary semidiscrete eigenvalue; no nonlinear CFL guarantee.', fontsize=10)
    fig.text(.075, .07, 'Phase follows the branch continuous from zero; RK4 can lag or lead. Gray: imaginary-axis instability.', fontsize=10)
    fig.text(.075, .025, 'Spatial phase error and temporal phase/amplitude error are separate; stability does not imply accuracy.', fontsize=9.6)
    fig.savefig(output/'rk4-response.png', dpi=120)
    plt.close(fig)

    theta, nu = np.pi/2, .5
    fixed_xi = nu*np.sin(theta)
    fixed_r = complex(rk4_polynomial(-1j*fixed_xi))
    phase_step = float(-np.angle(fixed_r))
    return {'scope': SCOPE, 'samples': len(xi), 'phase_branch': 'continuous from xi=0, via numpy.unwrap',
            'imaginary_axis_stability_bound': float(boundary),
            'checks': {'stage_vs_polynomial_maximum_residual': stage_residual,
                       'gain_squared_identity_maximum_residual': identity_residual,
                       'absolute_residual_acceptance': 2e-14, 'passed': True},
            'fixed_example': {'theta': float(theta), 'cfl_a_dt_over_h': nu, 'xi': float(fixed_xi),
                              'exact_continuum_phase_per_step': float(nu*theta),
                              'exact_semidiscrete_gain_per_step': 1.,
                              'exact_semidiscrete_phase_per_step': float(fixed_xi),
                              'rk4_gain_per_step': float(abs(fixed_r)),
                              'rk4_phase_per_step': phase_step,
                              'spatial_phase_speed_over_a': float(np.sin(theta)/theta),
                              'fully_discrete_phase_speed_over_a': float(phase_step/(nu*theta)),
                              'rk4_amplitude_after_100_steps': float(abs(fixed_r)**100),
                              'note': 'A scalar Fourier mode, not a finite-amplitude Euler/KEEP solution.'}}


def frozen_keep_probe(folder: Path):
    """Read-only optional check against the unchanged public package."""
    file = folder/'numart/keep.py'
    if digest(file) != KEEP_SHA256:
        raise ValueError('Expected the unchanged public 2026-11-21 KEEP source SHA-256')
    # Import the already-inspected versioned public package, never edit it.
    sys.path.insert(0, str(folder.resolve()))
    keep = importlib.import_module('numart.keep')
    euler = importlib.import_module('numart.euler2d')
    if Path(keep.__file__).resolve() != file.resolve():
        raise ValueError('Imported KEEP module does not belong to the selected public edition')
    n, m, length = 32, 3, 1.
    rho, u, v, pressure = 1., .4, .2, 1.
    h, angle = length/n, 2*np.pi*m/n
    x = np.arange(n)
    mode = np.broadcast_to(np.exp(1j*angle*x)[:, None], (n, n))
    cosine, sine = mode.real, mode.imag
    base = np.broadcast_to(euler.conserved([rho, u, v, pressure]), (n, n, 4)).copy()
    vector = np.array([1., u, v, .5*(u*u+v*v)])
    perturbation = cosine[..., None]*vector
    omega = u*np.sin(angle)/h
    expected = omega*sine[..., None]*vector
    denominator = np.vdot(mode, cosine)
    cases = []
    for epsilon in [1e-3, 1e-4, 1e-5, 1e-6]:
        derivative = (keep.rhs(base+epsilon*perturbation, length)-
                      keep.rhs(base-epsilon*perturbation, length))/(2*epsilon)
        projected = np.vdot(mode, derivative[..., 0])/denominator
        relative = float(np.linalg.norm(derivative-expected)/np.linalg.norm(expected))
        cases.append({'epsilon': epsilon, 'relative_directional_derivative_residual': relative,
                      'density_mode_lambda_real': float(projected.real),
                      'density_mode_lambda_imag': float(projected.imag),
                      'expected_lambda_imag': float(-omega)})
    best = min(x['relative_directional_derivative_residual'] for x in cases)
    max_real = max(abs(x['density_mode_lambda_real']) for x in cases)
    assert best < 2e-8 and max_real < 2e-9
    return {'scope': 'Centered finite-epsilon directional derivative about a uniform Euler state; entropy characteristic, x direction only.',
            'source': {'url': PUBLIC_BASE+'numart/keep.py', 'sha256': digest(file), 'edition': '2026-11-21'},
            'n': n, 'mode': m, 'length': length, 'theta': float(angle),
            'uniform_primitive_state': {'rho': rho, 'u': u, 'v': v, 'p': pressure},
            'perturbation_conserved_vector': vector.tolist(), 'epsilon_cases': cases,
            'best_relative_directional_derivative_residual': best,
            'maximum_in_phase_lambda_real': max_real,
            'acceptance': {'best_relative_residual_max': 2e-8, 'in_phase_lambda_real_max': 2e-9},
            'passed': True,
            'limitation': 'Does not establish finite-amplitude modal nondissipation, nonlinear split-product dispersion, entropy equality, or shock behavior.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='New or empty output directory')
    parser.add_argument('--keep-code', type=Path, help='Optional extracted unchanged 2026-11-21 public ZIP folder')
    args = parser.parse_args()
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Choose a new or empty output directory; existing results are not overwritten')
    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='keep-analysis-mpl-') as cache:
        os.environ['MPLCONFIGDIR'] = cache
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        plot_style(plt)
        result = {
            'schema_version': 1, 'scope': SCOPE,
            'source_script_sha256': digest(Path(__file__)),
            'environment': {'python': platform.python_version(), 'system': platform.system(),
                            'machine': platform.machine(), 'numpy': np.__version__,
                            'matplotlib': importlib.metadata.version('matplotlib')},
            'inputs': {'spatial_theta_interval': [0., float(np.pi)], 'spatial_samples': 513,
                       'rk4_xi_interval': [0., 3.1], 'rk4_uniform_samples': 801,
                       'rk4_stability_boundary_included': True},
            'formulas': {'spatial': 'lambda_h=-i*a*sin(theta)/h; cp/a=sin(theta)/theta; cg/a=cos(theta)',
                         'rk4': 'R(z)=1+z+z^2/2+z^3/6+z^4/24; z=-i*xi',
                         'gain_squared': 'abs(R(-i*xi))^2=1-xi^6/72+xi^8/576'},
            'spatial': spatial_analysis(args.output, plt),
            'rk4': rk4_analysis(args.output, plt),
        }
        if args.keep_code is not None:
            result['frozen_public_keep_linearization'] = frozen_keep_probe(args.keep_code)
        result['passed'] = True
        result['outputs'] = [{'path': p.name, 'bytes': p.stat().st_size, 'sha256': digest(p)}
                             for p in sorted(args.output.iterdir()) if p.is_file()]
        (args.output/'result.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': True, 'spatial_probe': result['spatial']['stencil_probe']['passed'],
                      'rk4_checks': result['rk4']['checks']['passed'],
                      'optional_keep_probe': result.get('frozen_public_keep_linearization', {}).get('passed'),
                      'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
