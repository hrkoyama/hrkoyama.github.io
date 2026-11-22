"""Reproduce the fixed-data Bratu inverse experiment and its audit evidence."""
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
from numart.autodiff import bratu_jacobian
from numart.bratu_sensitivity import implicit_sensitivity
from numart.bratu_inverse import (TRUTH_LAMBDA, POSITIONS, FIXED_NOISE, BOUNDS,
    observation_matrix, continuous_observations, evaluate, fit_parameter,
    golden_reference)

OUT = ROOT/'docs/figures'
SOURCES = ['numart/autodiff.py', 'numart/krylov.py', 'numart/bratu_sensitivity.py',
    'numart/bratu_inverse.py', 'scripts/build_bratu_inverse.py',
    'tests/test_bratu_inverse.py', 'inputs/synthetic-observations.json']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fit_row(n, data, initial):
    fit = fit_parameter(n, data, initial)
    if not fit['converged']:
        raise RuntimeError(fit['reason'])
    result = fit['result']
    row = dict(n=n, h=1/(n+1), initial=initial,
        converged=fit['converged'], reason=fit['reason'],
        lambda_value=fit['lambda_value'],
        parameter_error=fit['lambda_value']-TRUTH_LAMBDA,
        absolute_parameter_error=abs(fit['lambda_value']-TRUTH_LAMBDA),
        accepted_steps=len(fit['history'])-1, evaluations=fit['evaluations'],
        projected_gradient=fit['history'][-1]['projected_gradient'],
        history=fit['history'])
    for name in ['objective', 'data_rms', 'gradient', 'primal_residual_l2',
                 'adjoint_residual_l2', 'adjoint_residual_relative_l2']:
        row[name] = result[name]
    for name in ['predicted', 'misfit', 'state', 'adjoint', 'primal_residual_history']:
        row[name] = np.asarray(result[name]).tolist()
    row['x'] = (np.arange(1, n+1)/(n+1)).tolist()
    return row


def difference_row(lam, epsilon, tolerance, data, adjoint):
    plus = evaluate(31, lam+epsilon, data, primal_tolerance=tolerance, gradient=False)
    minus = evaluate(31, lam-epsilon, data, primal_tolerance=tolerance, gradient=False)
    finite = (plus['objective']-minus['objective'])/(2*epsilon)
    return dict(n=31, lambda_value=lam, epsilon=float(epsilon),
        solve_tolerance=tolerance, adjoint_reference=adjoint,
        finite_difference_gradient=finite, gradient_absolute_error=abs(finite-adjoint),
        plus_lambda=lam+float(epsilon), minus_lambda=lam-float(epsilon),
        plus_primal_residual_l2=plus['primal_residual_l2'],
        minus_primal_residual_l2=minus['primal_residual_l2'])


def build():
    hashes = {name: digest(ROOT/name) for name in SOURCES}
    inputs = json.loads((ROOT/'inputs/synthetic-observations.json').read_text())
    data = np.array(inputs['continuous_noiseless'])
    perturbed = np.array(inputs['continuous_perturbed'])
    np.testing.assert_allclose(data, continuous_observations(), rtol=0, atol=2e-16)
    np.testing.assert_array_equal(inputs['observation_positions'], POSITIONS)
    np.testing.assert_array_equal(inputs['fixed_perturbations'], FIXED_NOISE)
    np.testing.assert_array_equal(perturbed, data+FIXED_NOISE)
    assert inputs['truth_lambda'] == TRUTH_LAMBDA
    discrete = np.array(inputs['same_discrete']['data'])
    same = [fit_row(31, discrete, initial) for initial in (.5, 1.5, 3.2)]
    grids = [fit_row(n, data, 1.5) for n in (15, 31, 63, 127)]
    for previous, row in zip(grids, grids[1:]):
        row['parameter_order'] = float(np.log2(previous['absolute_parameter_error']/row['absolute_parameter_error']))
    for row in grids:
        row['objective_only_reference'] = golden_reference(row['n'], data)
        row['reference_parameter_difference'] = abs(row['lambda_value']-row['objective_only_reference']['lambda_value'])
    noisy = fit_row(63, perturbed, 1.5)
    noisy['objective_only_reference'] = golden_reference(63, perturbed)
    noisy['reference_parameter_difference'] = abs(noisy['lambda_value']-noisy['objective_only_reference']['lambda_value'])
    noisy['parameter_shift_from_noiseless_same_grid'] = noisy['lambda_value']-grids[2]['lambda_value']

    checks = []
    for lam in (.8, 1.8, 3.):
        result = evaluate(31, lam, data)
        matrix = bratu_jacobian(result['state'], lam)
        # This independent tangent solve is a diagnostic, never an optimizer step.
        sensitivity = implicit_sensitivity(matrix, -np.exp(result['state']))
        direct = float(np.sum(result['objective_state']*sensitivity))
        row = difference_row(lam, 1e-5, 1e-10, data, result['gradient'])
        row.update(direct_implicit_gradient=direct,
            direct_adjoint_difference=abs(direct-result['gradient']),
            adjoint_residual_l2=result['adjoint_residual_l2'],
            adjoint_residual_relative_l2=result['adjoint_residual_relative_l2'])
        checks.append(row)
    steps = np.logspace(-1, -9, 17)
    selected_gradient = checks[-1]['adjoint_reference']
    sweep = [difference_row(3., step, tol, data, selected_gradient)
             for tol in (1e-2, 1e-6, 1e-10) for step in steps]
    scan = []
    for lam in np.linspace(*BOUNDS, 65):
        result = evaluate(63, float(lam), perturbed, gradient=False)
        scan.append(dict(lambda_value=float(lam), objective=result['objective']))
    boundary = [evaluate(15, lam, [0., 0.], [0., 1.]) for lam in (.5, 3.)]
    diagnostic = dict(positions=[0., 1.], lambdas=[.5, 3.],
        objectives=[r['objective'] for r in boundary],
        gradients=[r['gradient'] for r in boundary],
        observation_matrix_rank=int(np.linalg.matrix_rank(observation_matrix(15, [0., 1.]))),
        conclusion='Fixed boundary observations carry no information about lambda; fit_parameter rejects this unregularized experiment.')

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8), layout='constrained')
    colors = ['#416b9b', '#bd6037', '#3c897b']
    for row, color in zip(same, colors):
        axes[0, 0].semilogy([r['iteration'] for r in row['history']],
            [max(abs(r['lambda_value']-TRUTH_LAMBDA), 1e-16) for r in row['history']],
            color=color, label=f"Initial lambda={row['initial']:g}")
    axes[0, 0].set(title='Same discrete data: code consistency only | n=31',
        xlabel='Accepted projected Armijo steps', ylabel='Absolute parameter error')
    for tol, color in zip((1e-2, 1e-6, 1e-10), colors):
        rows = [r for r in sweep if r['solve_tolerance'] == tol]
        axes[0, 1].loglog([r['epsilon'] for r in rows],
            [max(r['gradient_absolute_error'], 1e-18) for r in rows], 'o-', ms=3,
            color=color, label=f'Primal tolerance={tol:g}')
    axes[0, 1].set(title='Re-solved finite difference vs adjoint | lambda=3',
        xlabel='Parameter perturbation epsilon', ylabel='Absolute gradient difference')
    hs = np.array([r['h'] for r in grids])
    errors = np.array([r['absolute_parameter_error'] for r in grids])
    axes[1, 0].loglog(hs, errors, 'o-', color=colors[0], label='Continuous-data parameter bias')
    axes[1, 0].loglog(hs, errors[0]*(hs/hs[0])**2, '--', color=colors[1], label='Reference slope 2')
    axes[1, 0].set(title='Independent analytic observations | n=15,31,63,127',
        xlabel='Inverse grid spacing h', ylabel='Absolute parameter error')
    axes[1, 1].axhline(0, color='#999999', lw=.8)
    axes[1, 1].plot(POSITIONS, 1e3*FIXED_NOISE, 's--', color=colors[1], label='Fixed input perturbation')
    axes[1, 1].plot(POSITIONS, 1e3*np.array(noisy['misfit']), 'o-', color=colors[0], label='Fitted prediction - perturbed datum')
    axes[1, 1].set(title=f"Perturbed fit | n=63, lambda={noisy['lambda_value']:.7f}",
        xlabel='Sensor position x', ylabel='Observation difference x 1000')
    for ax in axes.flat:
        ax.grid(alpha=.2)
        ax.legend(fontsize=7)
    fig.suptitle('Bratu: scalar inverse estimation with a discrete adjoint\nFixed lower branch and bounds; data consistency, discretization bias and perturbations are separate checks')
    OUT.mkdir(parents=True, exist_ok=True)
    figure = OUT/'bratu-inverse.png'
    fig.savefig(figure, dpi=125)
    plt.close(fig)
    assert hashes == {name: digest(ROOT/name) for name in SOURCES}, 'Sources changed during build'
    evidence = dict(schema_version=1,
        settings=dict(truth_alpha=inputs['truth_alpha'], truth_lambda=TRUTH_LAMBDA,
            equation='F(u,lambda)=D*u-lambda*exp(u)=0; D=tridiag(-1,2,-1)/h^2',
            boundary='u(0)=u(1)=0, independent of lambda',
            observation_operator='H samples fixed exact grid nodes; boundary rows are zero; no interpolation',
            objective='L=.5*(H*u-d).T*W*(H*u-d)+.5*gamma*(lambda-prior)^2',
            weights=inputs['weights'], gamma=0., prior=0.,
            adjoint_equation='J.T*p=H.T*W*(H*u-d)',
            reduced_gradient='g=gamma*(lambda-prior)+p.T*exp(u)',
            branch='Zero-start dense Armijo-Newton lower-branch solve, bounds [0.2,3.4]; no fold crossing or branch switching validated',
            newton_tolerance_l2=1e-10, max_newton_updates=40,
            optimizer='Projected gradient with Armijo backtracking; every search direction comes from the discrete adjoint; no state sensitivity in optimization',
            bounds=list(BOUNDS), initial_step=10., backtrack_factor=.5, armijo_c=1e-4,
            armijo_condition='L_trial <= L + c*g*(lambda_trial-lambda), using the actual clipped displacement',
            gradient_tolerance=1e-10, projected_gradient='abs(lambda-clip(lambda-g,bounds))',
            max_optimization_steps=300, same_discrete_initials=[.5, 1.5, 3.2],
            interior_nodes=[15, 31, 63, 127], perturbed_n=63,
            parameter_error='fitted lambda minus generating continuum truth lambda; includes grid bias for independent data',
            residual_norms='Unscaled Euclidean primal residual; absolute and relative Euclidean adjoint residual, relative denominator ||H.T W r||2',
            finite_difference='Central parameter differences; fresh zero-start primal solves at both lambda+epsilon and lambda-epsilon; no state held fixed',
            finite_difference_n=31, finite_difference_lambdas=[.8, 1.8, 3.],
            finite_difference_steps=steps.tolist(), primal_tolerance_sweep=[1e-2, 1e-6, 1e-10],
            reference='Independent objective-only bounded golden section, interval-width tolerance 1e-8; assumes unimodality on the bracket. A sampled landscape is evidence, not a proof.',
            identifiability='Only fixed interior sensors constrain lambda; projected stationarity or a prior alone is not proof of data identifiability or truth recovery.'),
        observations=inputs, multistart=same, grid_runs=grids, noisy_run=noisy,
        gradient_checks=checks, parameter_sweep=sweep, objective_scan=scan,
        boundary_only_diagnostic=diagnostic,
        environment=dict(python=platform.python_version(), numpy=np.__version__,
            float_dtype='float64', float_epsilon=float(np.finfo(float).eps)),
        scope='A bounded one-parameter synthetic inverse problem on the tested smooth Bratu lower branch. Same-discrete recovery is an inverse-crime code-consistency control. Independent analytic observations reveal grid bias. Fixed deterministic perturbations are not a statistical noise distribution; no confidence intervals, universal convergence, global identifiability or performance advantage is claimed.',
        source_sha256=hashes, artifact_sha256={figure.name:digest(figure)})
    (OUT/'bratu-inverse.json').write_text(json.dumps(evidence, separators=(',', ':'), allow_nan=False)+'\n')
    print('Built fixed-data Bratu inverse evidence: 3 consistency fits, 4 mesh fits, 1 perturbed fit, 3 off-optimum gradient checks.')


if __name__ == '__main__':
    build()
