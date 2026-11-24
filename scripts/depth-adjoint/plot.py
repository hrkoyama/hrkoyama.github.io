"""Saved-data figures only; imports no forward solver or reference generator."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

IDS = ['diffusion-discrete-adjoint', 'bratu-fold-sensitivity', 'bratu-distributed-vjp']


def save(fig, output, name):
    fig.tight_layout()
    for extension in ['png', 'svg', 'pdf']:
        fig.savefig(output/(name+'.'+extension), dpi=155, bbox_inches='tight')
    plt.close(fig)


def positive(values):
    # Exact zeros are omitted from logarithmic axes, never replaced by a floor.
    return np.ma.masked_less_equal(np.asarray(values), 0)


def diffusion(results, output, case):
    root = results/case['id']; data = np.load(root/'n15-N256.npz')
    x = np.arange(17)/16; states = np.pad(data['states'], ((0, 0), (1, 1)))
    fig, axes = plt.subplots(2, 2, figsize=(10.2, 7))
    image = axes[0, 0].pcolormesh(x, np.linspace(0, .1, 257), states, shading='nearest')
    fig.colorbar(image, ax=axes[0, 0], label='u(x,t)')
    axes[0, 0].set(xlabel='x', ylabel='physical time t', title='Backward Euler, 15 interior nodes')
    axes[0, 1].plot(x[1:-1], data['states'][-1], 'o', label='Thomas / backward Euler')
    axes[0, 1].plot(x[1:-1], data['reference_terminal'], '-', label='Decimal modal / same time steps')
    axes[0, 1].set(xlabel='x', ylabel='u(x,T)', title='Terminal state'); axes[0, 1].legend(fontsize=8)
    for n in [7, 15]:
        rows = [r for r in case['records'] if r['n'] == n]
        axes[1, 0].loglog([r['steps'] for r in rows], positive([r['metrics']['time_error'] for r in rows]), 'o-', label=f'n={n}')
    axes[1, 0].set(xlabel='time steps N', ylabel='weighted L2 error', title='Time error vs semidiscrete exact modes'); axes[1, 0].legend()
    rows = [r for r in case['records'] if r['n'] == 15]
    axes[1, 1].plot([r['steps'] for r in rows], [r['metrics']['full_ledger']['peak_total_bytes'] for r in rows], 'o-', label='full storage')
    axes[1, 1].plot([r['steps'] for r in rows], [r['metrics']['checkpoint_ledger']['peak_total_bytes'] for r in rows], 's-', label='checkpoint + block replay')
    axes[1, 1].set(xlabel='time steps N', ylabel='owned numeric bytes', title='Separate ownership windows; not process RSS'); axes[1, 1].legend(fontsize=8)
    fig.suptitle('Discrete adjoint: time stepping, replay and memory', y=1.02)
    save(fig, output, case['id'])
    preview, ax = plt.subplots(figsize=(7, 4.3))
    im = ax.pcolormesh(x, np.linspace(0, .1, 257), states, shading='nearest')
    preview.colorbar(im, ax=ax, label='u(x,t)')
    ax.set(xlabel='x', ylabel='time t', title='1D diffusion: discrete adjoint and checkpoint replay')
    save(preview, output, case['id']+'-preview')


def fold(results, output, case):
    root = results/case['id']; fig, axes = plt.subplots(2, 2, figsize=(10.2, 7))
    for i in range(3):
        d = np.load(root/f'n63-point{i}.npz'); x = np.arange(65)/64
        axes[0, 0].plot(x, np.pad(d['state_strict'], (1, 1)), label=f'delta={case["records"][3+i]["metrics"]["delta"]:g}')
    axes[0, 0].set(xlabel='x', ylabel='u', title='Lower branch near the discrete fold, n=63'); axes[0, 0].legend()
    for n in [31, 63]:
        rows = [r for r in case['records'] if r['n'] == n]
        delta = [r['metrics']['delta'] for r in rows]
        axes[0, 1].loglog(delta, [r['metrics']['sigma_estimate'] for r in rows], 'o-', label=f'n={n}')
        axes[1, 0].loglog(delta, positive([r['metrics']['gradient_error'] for r in rows]), 'o-', label=f'n={n}')
    axes[0, 1].set(xlabel='discrete-anchor gap delta', ylabel='smallest |eigenvalue(J)|', title='Floating condition diagnostic'); axes[0, 1].legend()
    axes[1, 0].set(xlabel='delta', ylabel='absolute gradient error', title='Strict returned adjoint vs Decimal shooting'); axes[1, 0].legend()
    last = case['records'][-1]['metrics']; statuses = last['linear_statuses']
    for kind in ['tangent', 'adjoint']:
        axes[1, 1].loglog([s['requested_rtol'] for s in statuses], [s[kind]['actual_true_residual'] for s in statuses], 'o-', label=kind)
    axes[1, 1].loglog([s['requested_rtol'] for s in statuses], [s['adjoint']['requested_absolute_target'] for s in statuses], '--', label='adjoint requested target')
    axes[1, 1].set(xlabel='requested relative tolerance', ylabel='true residual norm', title='Tight target is observational; status in CSV'); axes[1, 1].legend(fontsize=8)
    fig.suptitle('Bratu: sensitivity near a discrete fold', y=1.02); save(fig, output, case['id'])
    preview, ax = plt.subplots(figsize=(7, 4.3))
    for n in [31, 63]:
        rows = [r for r in case['records'] if r['n'] == n]
        ax.loglog([r['metrics']['delta'] for r in rows], [abs(r['metrics']['reference_gradient']) for r in rows], 'o-', label=f'n={n}: independent shooting')
    ax.set(xlabel='gap to discrete fold anchor', ylabel='|d objective / d lambda|', title='Near-fold sensitivity; continuum fold is separate')
    ax.legend(fontsize=8); save(preview, output, case['id']+'-preview')


def parameters(results, output, case):
    root = results/case['id']; data = np.load(root/'m32.npz'); x = np.arange(1, 64)/64
    fig, axes = plt.subplots(2, 2, figsize=(10.2, 7))
    axes[0, 0].plot(x, data['coefficient'], label='a = 2 + B theta'); axes[0, 0].plot(x, data['u'], label='state u')
    axes[0, 0].set(xlabel='x', title='Distributed coefficient and 1D Dirichlet state'); axes[0, 0].legend()
    names = ['integral(u)', 'midpoint u', '0.5 integral(u^2)']
    for j, name in enumerate(names):
        axes[0, 1].plot(np.arange(32)/31, data['gradients'][j], label=name)
        axes[0, 1].plot(np.arange(32)/31, data['reference_gradients'][j], '.', color=axes[0, 1].lines[-1].get_color())
    axes[0, 1].set(xlabel='control node xi', ylabel='coordinate gradient', title='Adjoint lines; full-sensitivity reference dots'); axes[0, 1].legend(fontsize=8)
    for j, name in enumerate(names):
        axes[1, 0].semilogy([r['m'] for r in case['records']], positive([r['metrics']['gradient_errors'][j] for r in case['records']]), 'o-', label=name)
    axes[1, 0].set(xlabel='number of controls m', ylabel='gradient L2 error', title='Same discrete state, separate dense reference'); axes[1, 0].legend(fontsize=8)
    axes[1, 1].plot([8, 16, 32], [r['metrics']['one_RHS'] for r in case['records']], 'o-', label='one objective')
    axes[1, 1].plot([8, 16, 32], [r['metrics']['three_RHS'] for r in case['records']], 's-', label='three objectives')
    axes[1, 1].plot([8, 16, 32], [r['metrics']['reference_RHS'] for r in case['records']], '^-', label='full-sensitivity reference')
    axes[1, 1].set(xlabel='m', ylabel='derivative RHS solves', title='Shared primary Poisson factor; not timing'); axes[1, 1].legend(fontsize=8)
    fig.suptitle('Bratu: matrix-free VJP with local coefficient hats', y=1.02); save(fig, output, case['id'])
    preview, ax = plt.subplots(figsize=(7, 4.3))
    for j, name in enumerate(names): ax.plot(np.arange(32)/31, data['gradients'][j], 'o-', ms=3, label=name)
    ax.set(xlabel='coefficient control xi', ylabel='coordinate gradient', title='32 spatial controls: one adjoint RHS per objective')
    ax.legend(fontsize=8); save(preview, output, case['id']+'-preview')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--results', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    a = p.parse_args(); a.output.mkdir(parents=True, exist_ok=True)
    if a.results.is_file():
        report_path = a.results; a.results = a.results.parent
    else:
        report_path = a.results/'result.json'
    report = json.loads(report_path.read_text())
    if report['passed'] is not True: raise ValueError('Plot only a completed passing result; failures remain data')
    for case, function in zip(report['cases'], [diffusion, fold, parameters]): function(a.results, a.output, case)


if __name__ == '__main__': main()
