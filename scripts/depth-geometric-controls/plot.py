"""Figures from saved arrays only; no reference or primary solver import."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def packet(directory, name):
    with np.load(directory/name, allow_pickle=False) as arrays:
        return {key: arrays[key].copy() for key in arrays.files}


def save(figure, output, name):
    figure.tight_layout()
    for extension in ['png', 'svg', 'pdf']:
        figure.savefig(output/(name+'.'+extension), dpi=150, facecolor='white')
    plt.close(figure)


def pendulum(directory, output, case):
    tight = [r for r in case['records'] if r['role'] == 'primary' and r['target'] == 1e-13]
    finest = {method: next(r for r in tight if r['method'] == method and r['steps'] == 10000)
              for method in ['rattle', 'shake']}
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for method, row in finest.items():
        raw = packet(directory, row['raw_file']); diag = packet(directory, row['diagnostic_file'])
        axes[0, 0].plot(diag['q'][:, 0], diag['q'][:, 1], lw=1., label=method.upper())
        axes[0, 1].plot(raw['times'], abs(diag['constraint']), lw=.7, label=method.upper())
        axes[1, 0].plot(diag['times'], diag['energy_error'], lw=.8, label=method.upper())
        points = [r for r in tight if r['method'] == method]
        axes[1, 1].loglog([r['h'] for r in points], [r['max_state_error'] for r in points], 'o-', label=method.upper())
    axes[0, 0].set(xlabel='x / L', ylabel='y / L', title='Saved constrained orbit, h = 0.01')
    axes[0, 0].set_aspect('equal', adjustable='box')
    axes[0, 1].set(xlabel='Time', ylabel='|C(q)|', title='Position constraint: measured residual')
    axes[0, 1].set_yscale('symlog', linthresh=1e-16)
    axes[1, 0].set(xlabel='Time', ylabel='|H − H(0)|', title='SHAKE energy uses interior centered momentum')
    axes[1, 1].set(xlabel='Step size', ylabel='Maximum same-time state error', title='Three fixed step sizes, T = 100')
    for axis in axes.flat:axis.grid(alpha=.2);axis.legend(fontsize=8)
    fig.suptitle('SHAKE and RATTLE: position constraints and momentum ownership', fontsize=13)
    save(fig, output, case['id'])
    fig, axis = plt.subplots(figsize=(7.8, 5.8))
    for method, row in finest.items():
        data = packet(directory, row['diagnostic_file'])
        theta = np.arctan2(data['q'][:, 0], -data['q'][:, 1])
        angular_p = data['q'][:, 0]*data['p'][:, 1]-data['q'][:, 1]*data['p'][:, 0]
        axis.plot(theta, angular_p, lw=.8, label=method.upper(), rasterized=True)
    reference = packet(directory, finest['rattle']['diagnostic_file'])
    theta = np.arctan2(reference['reference_q'][:, 0], -reference['reference_q'][:, 1])
    momentum = reference['reference_q'][:, 0]*reference['reference_p'][:, 1]-reference['reference_q'][:, 1]*reference['reference_p'][:, 0]
    axis.plot(theta, momentum, '--', color='black', lw=1., label='Qualified Jacobi reference')
    axis.set(xlabel='Angle θ', ylabel='Angular momentum pθ', title='Actual reduced phase portraits, h = 0.01')
    axis.grid(alpha=.2);axis.legend();save(fig, output, case['id']+'-preview')


def kepler(directory, output, case):
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for e, axis in zip([.1, .7], axes[0]):
        row = next(r for r in case['records'] if r['role'] == 'primary' and r['eccentricity'] == e and r['periods'] == 1 and r['steps'] == 2048)
        raw, data = packet(directory, row['raw_file']), packet(directory, row['diagnostic_file'])
        axis.plot(data['reference_q'][:, 0], data['reference_q'][:, 1], '--', color='black', label='Kepler equation')
        axis.plot(raw['q'][:, 0], raw['q'][:, 1], label='KDK, 2048 steps')
        axis.scatter([0], [0], marker='*', color='orange', s=80)
        axis.set(xlabel='Relative x / a', ylabel='Relative y / a', title=f'One period, eccentricity e = {e}')
        axis.set_aspect('equal', adjustable='box');axis.legend(fontsize=8)
    for control in ['fixed', 'variable']:
        row = next(r for r in case['records'] if r['role'] == 'primary' and r['eccentricity'] == .7 and r['periods'] == 10 and r['control'] == control)
        raw, data = packet(directory, row['raw_file']), packet(directory, row['diagnostic_file'])
        axes[1, 0].plot(raw['times'], data['state_error'], lw=.8, label=control)
        events = packet(directory, row['id']+'-periapses.npz')
        axes[1, 1].plot(np.arange(1, len(events['times'])+1), events['times']-2*np.pi*np.arange(1, len(events['times'])+1), 'o-', label=control)
    axes[1, 0].set(xlabel='Time', ylabel='Same-time full-state error', title='Ten periods, e = 0.7: phase error matters')
    axes[1, 1].set(xlabel='Periapsis number', ylabel='tperi − 2πk', title='Hermite-localized physical periapses')
    for axis in axes.flat:axis.grid(alpha=.2)
    axes[1, 0].legend();axes[1, 1].legend()
    save(fig, output, case['id'])
    fig, axis = plt.subplots(figsize=(8, 5.8))
    for control in ['fixed', 'variable']:
        row = next(r for r in case['records'] if r['role'] == 'primary' and r['eccentricity'] == .7 and r['periods'] == 10 and r['control'] == control)
        raw = packet(directory, row['raw_file']);axis.plot(raw['q'][:, 0], raw['q'][:, 1], lw=.8, label=control, rasterized=True)
    axis.scatter([0], [0], marker='*', color='orange', s=110, label='Unsoftened focus')
    axis.set(xlabel='Relative x / a', ylabel='Relative y / a', title='Actual ten-period Kepler orbits, e = 0.7')
    axis.set_aspect('equal', adjustable='box');axis.grid(alpha=.2);axis.legend()
    save(fig, output, case['id']+'-preview')


def coupled(directory, output, case):
    row = next(r for r in case['records'] if r['role'] == 'accuracy' and r['method'] == 'impulse' and r['steps'] == 2000)
    raw, data = packet(directory, row['raw_file']), packet(directory, row['diagnostic_file'])
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    axes[0, 0].plot(raw['times'], data['coordinate_energy'][:, 0], label='Coordinate energy 1')
    axes[0, 0].plot(raw['times'], data['coordinate_energy'][:, 1], label='Coordinate energy 2')
    axes[0, 0].set(xlabel='Time', ylabel='Coordinate energies', title='Exchange is not modal energy drift')
    for j in range(2):axes[0, 1].plot(raw['times'], data['modal_energy'][:, j]-data['modal_energy'][0, j], label=f'Normal mode {j+1}')
    axes[0, 1].set(xlabel='Time', ylabel='Modal energy − initial value', title='Coupled normal modes, ω = 10')
    for method in ['verlet', 'impulse']:
        selected = [r for r in case['records'] if r['role'] == 'accuracy' and r['method'] == method]
        axes[1, 0].loglog([r['h'] for r in selected], [r['max_scaled_state_error'] for r in selected], 'o-', label=method)
        probes = [r for r in case['records'] if r['role'] == 'probe' and r['method'] == method and r['omega'] == 10]
        axes[1, 1].semilogy([r['h']*10 for r in probes], [r['finite_horizon_amplification'] for r in probes], 'o-', label=method)
    axes[1, 0].set(xlabel='Step size', ylabel='Maximum scaled state error', title='Actual three-level accuracy experiment')
    axes[1, 1].set(xlabel='Evaluated hω', ylabel='Maximum scaled norm over 64 steps', title='Finite probes; central float map is unresolved')
    for axis in axes.flat:axis.grid(alpha=.2);axis.legend(fontsize=8)
    save(fig, output, case['id'])
    fig, axis = plt.subplots(figsize=(7.8, 5.8))
    points = axis.scatter(raw['states'][:, 0], raw['states'][:, 1], c=raw['times'], cmap='viridis', s=4, rasterized=True)
    axis.plot(data['continuum'][:, 0], data['continuum'][:, 1], color='black', lw=.55, alpha=.5, label='Exact coupled continuum')
    axis.set(xlabel='Slow coordinate q1', ylabel='Fast coordinate q2', title='Actual coupled trajectory: impulse h = 0.005')
    axis.grid(alpha=.2);axis.legend();fig.colorbar(points, ax=axis, label='Physical time')
    save(fig, output, case['id']+'-preview')


def main():
    parser = argparse.ArgumentParser();parser.add_argument('--results', required=True, type=Path);parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(); result_path = args.results/'result.json' if args.results.is_dir() else args.results
    result = json.loads(result_path.read_text())
    if result['passed'] is not True:raise ValueError('Plot qualified saved main only')
    output = args.output;output.mkdir(parents=True, exist_ok=True)
    for function, case in zip([pendulum, kepler, coupled], result['cases']):function(result_path.parent, output, case)


if __name__ == '__main__':main()
