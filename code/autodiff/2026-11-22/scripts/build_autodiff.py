"""Build deterministic derivative/Bratu evidence; no timing ranking is made."""
from pathlib import Path
import hashlib
import json
import platform
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from numart.autodiff import (BRATU_LAMBDA, Dual, bratu_residual,
    bratu_jacobian, bratu_reference, finite_difference_jacobian, jacobian, jvp)
from numart.krylov import newton

OUT = ROOT / 'docs/figures'
SOURCES = ['numart/autodiff.py', 'numart/krylov.py',
           'tests/test_autodiff.py', 'scripts/build_autodiff.py']


def digest(relative):
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def build():
    sources = {name: digest(name) for name in SOURCES}
    n = 31
    x, exact = bratu_reference(n)
    state = exact + .05*np.sin(3*np.pi*x)
    direction = np.sin(2*np.pi*x) + .3*np.cos(5*np.pi*x)
    direction /= np.linalg.norm(direction)
    analytic = bratu_jacobian(state)
    automatic = jacobian(bratu_residual, state)
    analytic_product = analytic @ direction
    value, automatic_product = jvp(bratu_residual, state, direction)
    relative = lambda error, reference: float(np.linalg.norm(error) / np.linalg.norm(reference))
    derivative = dict(n=n, x=x.tolist(), state=state.tolist(), direction=direction.tolist(),
        state_definition='u_exact(x) + 0.05 sin(3 pi x)',
        direction_definition='[sin(2 pi x) + 0.3 cos(5 pi x)] / Euclidean norm',
        jacobian_relative_frobenius_error=relative(automatic-analytic, analytic),
        jvp_relative_l2_error=relative(automatic_product-analytic_product, analytic_product),
        primal_maximum_difference=float(np.max(abs(value-bratu_residual(state)))),
        analytic_jvp=analytic_product.tolist(), autodiff_jvp=automatic_product.tolist())
    sweep = []
    for step in np.logspace(0, -14, 29):
        row = dict(step=float(step))
        for scheme in ('forward', 'central'):
            estimated = finite_difference_jacobian(bratu_residual, state, step, scheme)
            plus = bratu_residual(state+step*direction)
            estimated_product = ((plus-bratu_residual(state))/step if scheme == 'forward'
                else (plus-bratu_residual(state-step*direction))/(2*step))
            row[scheme+'_jacobian_relative_frobenius_error'] = relative(estimated-analytic, analytic)
            row[scheme+'_jvp_relative_l2_error'] = relative(estimated_product-analytic_product, analytic_product)
        sweep.append(row)

    tolerance, fd_step = 1e-10, 1e-5
    runs = []
    for n in (15, 31, 63):
        x, exact = bratu_reference(n)
        reference_root = None
        for method in ('analytic', 'finite_difference', 'autodiff'):
            counts = dict(primal_residual_calls=0, dual_residual_calls=0, jacobian_calls=0)

            def residual(u):
                counts['dual_residual_calls' if isinstance(u, Dual) else 'primal_residual_calls'] += 1
                return bratu_residual(u)

            def derivative_at(u):
                counts['jacobian_calls'] += 1
                if method == 'analytic':
                    return bratu_jacobian(u)
                if method == 'finite_difference':
                    return finite_difference_jacobian(residual, u, fd_step)
                return jacobian(residual, u)

            result = newton(residual, derivative_at, np.zeros(n), tolerance=tolerance,
                            maxiter=30, linear_solver='dense')
            if not result.converged:
                raise RuntimeError(f'{method} n={n}: {result.reason}')
            if method == 'analytic':
                reference_root = result.x.copy()
            runs.append(dict(method=method, n=n, h=1/(n+1),
                converged=result.converged, reason=result.reason,
                iterations=len(result.step_lengths), residuals=result.residuals.tolist(),
                step_lengths=result.step_lengths.tolist(),
                final_residual_l2=float(np.linalg.norm(bratu_residual(result.x))),
                continuous_error_linf=float(np.max(abs(result.x-exact))),
                difference_from_analytic_root_linf=float(np.max(abs(result.x-reference_root))),
                solution=result.x.tolist(), **counts))
    for method in ('analytic', 'finite_difference', 'autodiff'):
        selected = [run for run in runs if run['method'] == method]
        for previous, current in zip(selected, selected[1:]):
            current['continuous_error_order'] = float(np.log2(previous['continuous_error_linf'] / current['continuous_error_linf']))

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8), layout='constrained')
    colors = {'analytic': '#23392f', 'finite_difference': '#bf5b35', 'autodiff': '#476b9c'}
    for ax, metric, baseline, title in (
        (axes[0, 0], 'jacobian_relative_frobenius_error', derivative['jacobian_relative_frobenius_error'], 'Jacobian: relative Frobenius error'),
        (axes[0, 1], 'jvp_relative_l2_error', derivative['jvp_relative_l2_error'], 'Directional derivative: relative 2-norm error')):
        for scheme, marker in (('forward', 's'), ('central', 'o')):
            ax.loglog([r['step'] for r in sweep], [r[scheme+'_'+metric] for r in sweep], marker+'-', ms=3, label=scheme+' differences')
        ax.axhline(max(baseline, np.finfo(float).eps), color=colors['autodiff'], ls='--', label='AD (floor shown at machine epsilon)')
        ax.set(title=title+' | n=31', xlabel='Absolute perturbation epsilon', ylabel='Error against analytic derivative')
        ax.legend(fontsize=7)
    for method, label in (('analytic', 'Analytic'), ('finite_difference', 'Central FD / epsilon=1e-5'), ('autodiff', 'Forward AD')):
        selected = [r for r in runs if r['method'] == method]
        fine = selected[-1]
        axes[1, 0].semilogy(range(len(fine['residuals'])), fine['residuals'], 'o-', ms=4, color=colors[method], label=label)
        axes[1, 1].loglog([r['h'] for r in selected], [r['continuous_error_linf'] for r in selected], 'o-', ms=4, color=colors[method], label=label)
    axes[1, 0].axhline(tolerance, color='black', ls=':', lw=1)
    axes[1, 0].set(title='Same damped Newton solve | n=63', xlabel='Completed Newton updates', ylabel='Recomputed residual 2-norm')
    axes[1, 1].set(title='Spatial refinement | n=15,31,63', xlabel='Mesh spacing h=1/(n+1)', ylabel='Maximum nodal error vs continuous solution')
    for ax in axes.flat:
        ax.grid(alpha=.2)
    for ax in axes[1]:
        ax.legend(fontsize=7)
    fig.suptitle('Bratu: one residual, three ways to supply its derivative\nOverlapping Newton/error curves are expected; no solver speed ranking')
    OUT.mkdir(parents=True, exist_ok=True)
    figure = OUT / 'autodiff-bratu.png'
    fig.savefig(figure, dpi=125)
    plt.close(fig)
    assert sources == {name: digest(name) for name in SOURCES}, 'Sources changed during build'
    manifest = dict(schema_version=1,
        settings=dict(lambda_value=BRATU_LAMBDA, interior_nodes=[15, 31, 63],
            boundary='u(0)=u(1)=0', equation='-u_xx-lambda exp(u)=0',
            mesh='x_i=i/(n+1), i=1,...,n; centered second differences',
            initial_guess='zero vector for every method and grid',
            newton_tolerance_l2=tolerance, max_newton_updates=30,
            linear_solver='existing numart.krylov.newton, dense numpy.linalg.solve, Armijo backtracking',
            finite_difference_scheme='central', finite_difference_absolute_step=fd_step,
            continuous_reference='-2 log(cosh(x-1/2)/cosh(1/2))',
            jacobian_error_norm='Frobenius norm of error / Frobenius norm of analytic Jacobian',
            jvp_error_norm='Euclidean norm of error / Euclidean norm of analytic Jv'),
        derivative_checks=derivative, difference_sweep=sweep, newton_runs=runs,
        environment=dict(python=platform.python_version(), numpy=np.__version__, float_dtype='float64',
                         float_epsilon=float(np.finfo(float).eps)),
        scope='Educational real forward AD with one seed per Jacobian column; no reverse-mode implementation. The Bratu discretization and parameter match the original sparse/Newton verification; dense Newton isolates derivative construction. Counts include residual monitoring and line search; a dual call costs more than a primal call, and analytic Jacobian work is not a residual call. No timings or universal performance ranking. Discrete root error and continuous spatial error are separate. No near-fold, nonsmooth, adaptive-time or implicit-sensitivity claims.',
        source_sha256=sources, artifact_sha256={figure.name: hashlib.sha256(figure.read_bytes()).hexdigest()})
    (OUT / 'autodiff-bratu.json').write_text(json.dumps(manifest, separators=(',', ':'), allow_nan=False)+'\n')
    print('AD derivative checks:', json.dumps({k: v for k, v in derivative.items() if k.endswith('error') or k.endswith('difference')}))
    for run in runs:
        print(run['method'], run['n'], 'updates', run['iterations'], 'residual', run['final_residual_l2'], 'continuous error', run['continuous_error_linf'])
    print('Built docs/figures/autodiff-bratu.json and .png')


if __name__ == '__main__':
    build()
