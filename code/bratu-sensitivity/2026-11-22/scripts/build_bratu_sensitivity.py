"""Reproduce implicit Bratu sensitivities and discrete-adjoint checks offline."""
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
from numart.autodiff import bratu_jacobian, bratu_residual
from numart.bratu_sensitivity import (OBJECTIVE_BETA, adjoint_gradient,
    bratu_derivatives, family_reference, implicit_sensitivity, objective,
    objective_partials, solve_bratu)

OUT = ROOT/'docs/figures'
SOURCES = ['numart/autodiff.py', 'numart/krylov.py', 'numart/bratu_sensitivity.py',
           'tests/test_bratu_sensitivity.py', 'scripts/build_bratu_sensitivity.py']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def continuous_gradient(alpha, order):
    """Independent continuum reference from exact family and Gauss quadrature."""
    nodes, weights = np.polynomial.legendre.leggauss(order)
    x, weights = (nodes+1)/2, weights/2
    lam = 2*alpha**2/np.cosh(alpha/2)**2
    lam_alpha = lam*(2/alpha-np.tanh(alpha/2))
    u = -2*np.log(np.cosh(alpha*(x-.5))/np.cosh(alpha/2))
    sensitivity = (np.tanh(alpha/2)-2*(x-.5)*np.tanh(alpha*(x-.5)))/lam_alpha
    return float(np.sum(weights*u*sensitivity)+OBJECTIVE_BETA*lam)


def root_at(n, lam, tolerance):
    root = solve_bratu(n, lam, tolerance)
    if not root.converged:
        raise RuntimeError(f'n={n}, lambda={lam}, tolerance={tolerance}: {root.reason}')
    residual = float(np.linalg.norm(bratu_residual(root.x, lam)))
    if residual > tolerance:
        raise RuntimeError('Converged flag failed true unscaled-residual check')
    return root, residual


def build():
    hashes = {name: digest(ROOT/name) for name in SOURCES}
    tolerance = 1e-10
    runs, continuum = [], []
    for alpha in (1., 2.):
        reference96, reference192 = continuous_gradient(alpha, 96), continuous_gradient(alpha, 192)
        continuum.append(dict(alpha=alpha, quadrature_orders=[96, 192],
            gradient=reference192, quadrature_difference=abs(reference96-reference192),
            definition='beta*lambda + integral_0^1 u_alpha(x)*(du_alpha/dlambda)(x) dx; exact continuous family'))
        for n in (15, 31, 63):
            x, exact, exact_sensitivity, lam = family_reference(n, alpha)
            root, primal_residual = root_at(n, lam, tolerance)
            matrix, parameter = bratu_derivatives(root.x, lam)
            sensitivity = implicit_sensitivity(matrix, parameter)
            lu, ll = objective_partials(root.x, lam)
            gradient, adjoint = adjoint_gradient(matrix, parameter, lu, ll)
            direct = float(np.sum(lu*sensitivity)+ll)
            tangent_residual = np.einsum('ij,j->i', matrix, sensitivity)+parameter
            adjoint_residual = np.einsum('ji,j->i', matrix, adjoint)-lu
            runs.append(dict(alpha=alpha, lambda_value=lam, n=n, h=1/(n+1),
                converged=root.converged, reason=root.reason,
                newton_updates=len(root.step_lengths), primal_residual_history=root.residuals.tolist(),
                primal_residual_l2=primal_residual,
                sensitivity_residual_l2=float(np.linalg.norm(tangent_residual)),
                sensitivity_residual_relative_l2=float(np.linalg.norm(tangent_residual)/np.linalg.norm(parameter)),
                adjoint_residual_l2=float(np.linalg.norm(adjoint_residual)),
                adjoint_residual_relative_l2=float(np.linalg.norm(adjoint_residual)/np.linalg.norm(lu)),
                jacobian_condition_2=float(np.linalg.cond(matrix)),
                ad_jacobian_maximum_difference=float(np.max(abs(matrix-bratu_jacobian(root.x, lam)))),
                ad_parameter_maximum_difference=float(np.max(abs(parameter+np.exp(root.x)))),
                state_error_linf=float(np.max(abs(root.x-exact))),
                sensitivity_error_linf=float(np.max(abs(sensitivity-exact_sensitivity))),
                objective=objective(root.x, lam), direct_gradient=direct, adjoint_gradient=gradient,
                direct_adjoint_difference=abs(direct-gradient), explicit_gradient=ll,
                continuum_gradient_error=abs(gradient-reference192),
                x=x.tolist(), state=root.x.tolist(), sensitivity=sensitivity.tolist(),
                exact_sensitivity=exact_sensitivity.tolist(), adjoint=adjoint.tolist()))
        selected = [r for r in runs if r['alpha'] == alpha]
        for previous, current in zip(selected, selected[1:]):
            current['sensitivity_order'] = float(np.log2(previous['sensitivity_error_linf']/current['sensitivity_error_linf']))
            current['gradient_order'] = float(np.log2(previous['continuum_gradient_error']/current['continuum_gradient_error']))

    steps = np.logspace(-1, -9, 17)
    sweep, tolerance_sweep = [], []

    def difference_row(alpha, step, solve_tolerance):
        baseline = next(r for r in runs if r['alpha'] == alpha and r['n'] == 31)
        lam = baseline['lambda_value']
        plus, rp = root_at(31, lam+step, solve_tolerance)
        minus, rm = root_at(31, lam-step, solve_tolerance)
        lp, lm = objective(plus.x, lam+step), objective(minus.x, lam-step)
        finite = (lp-lm)/(2*step)
        state_finite = (plus.x-minus.x)/(2*step)
        exact_discrete_s = np.array(baseline['sensitivity'])
        return dict(alpha=alpha, n=31, epsilon=float(step), solve_tolerance=solve_tolerance,
            finite_difference_gradient=finite,
            adjoint_reference=baseline['adjoint_gradient'],
            gradient_absolute_error=abs(finite-baseline['adjoint_gradient']),
            state_sensitivity_relative_l2_error=float(np.linalg.norm(state_finite-exact_discrete_s)/np.linalg.norm(exact_discrete_s)),
            plus_primal_residual_l2=rp, minus_primal_residual_l2=rm,
            plus_newton_updates=len(plus.step_lengths), minus_newton_updates=len(minus.step_lengths),
            plus_root_linf=float(np.max(abs(plus.x))), minus_root_linf=float(np.max(abs(minus.x))),
            plus_lambda=lam+float(step), minus_lambda=lam-float(step),
            first_order_taylor_remainder_abs=abs(lp-baseline['objective']-step*baseline['adjoint_gradient']))

    for alpha in (1., 2.):
        for step in steps:
            sweep.append(difference_row(alpha, step, tolerance))
    for tol in (1e-2, 1e-6, 1e-10):
        for step in steps:
            tolerance_sweep.append(difference_row(2., step, tol))

    a = np.array([[3., 2., -1.], [0., 4., .5], [1., -2., 5.]])
    b = np.array([[1., -.3], [2., .4], [-.2, 1.3]])
    w = np.array([.4, -1.2, .7])
    theta = np.array([.2, -.6])
    r = np.array([[2., .3], [.3, 1.5]])
    s = implicit_sensitivity(a, -b)
    g, p = adjoint_gradient(a, -b, w, r@theta)
    independent = w@np.linalg.solve(a, b)+r@theta
    nonsymmetric = dict(matrix=a.tolist(), parameter_rhs=b.tolist(), objective_state=w.tolist(),
        parameters=theta.tolist(), explicit_quadratic=r.tolist(),
        residual='A*u-B*theta-c=0; c=[1,-0.3,0.2]',
        objective='w dot u + .5 theta.T R theta',
        sensitivity=s.tolist(), adjoint=p.tolist(), gradient=g.tolist(),
        independent_gradient=independent.tolist(),
        maximum_gradient_difference=float(np.max(abs(g-independent))),
        reason='Bratu Jacobian is symmetric; this independent three-state/two-parameter system detects wrong transpose and sign conventions.')

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8), layout='constrained')
    colors = {1.: '#476b9c', 2.: '#bf5b35'}
    for alpha in (1., 2.):
        selected = [r for r in runs if r['alpha'] == alpha]
        fine = selected[-1]
        axes[0, 0].plot(fine['x'], fine['sensitivity'], color=colors[alpha], label=f'Implicit / alpha={alpha:g}')
        axes[0, 0].plot(fine['x'][::4], fine['exact_sensitivity'][::4], 'o', fillstyle='none', color=colors[alpha], ms=4, label=f'Continuous exact / alpha={alpha:g}')
        rows = [r for r in sweep if r['alpha'] == alpha]
        axes[0, 1].loglog([r['epsilon'] for r in rows], [r['gradient_absolute_error'] for r in rows], 'o-', ms=3, color=colors[alpha], label=f'alpha={alpha:g}')
        axes[1, 0].loglog([r['h'] for r in selected], [r['sensitivity_error_linf'] for r in selected], 'o-', color=colors[alpha], label=f'State sensitivity / alpha={alpha:g}')
        axes[1, 0].loglog([r['h'] for r in selected], [r['continuum_gradient_error'] for r in selected], 's--', color=colors[alpha], label=f'Objective derivative / alpha={alpha:g}')
    for tol in (1e-2, 1e-6, 1e-10):
        rows = [r for r in tolerance_sweep if r['solve_tolerance'] == tol]
        axes[1, 1].loglog([r['epsilon'] for r in rows], [r['gradient_absolute_error'] for r in rows], 'o-', ms=3, label=f'Primal tolerance {tol:g}')
    axes[0, 0].set(title='State sensitivity du/dlambda | n=63', xlabel='x', ylabel='Sensitivity (zero boundary derivatives)')
    axes[0, 1].set(title='Re-solved central difference vs adjoint | n=31', xlabel='Parameter perturbation epsilon', ylabel='Absolute discrete-gradient difference')
    axes[1, 0].set(title='Independent continuous references | n=15,31,63', xlabel='Grid spacing h', ylabel='Maximum state-sensitivity / scalar-gradient error')
    axes[1, 1].set(title='Loose nonlinear solves can bias gradient checks | alpha=2', xlabel='Parameter perturbation epsilon', ylabel='Absolute gradient difference vs tight adjoint')
    for ax in axes.flat:
        ax.grid(alpha=.2)
        ax.legend(fontsize=7)
    fig.suptitle('Bratu: implicit differentiation and a discrete adjoint\nOne parameter / one objective; no performance advantage or inverse fit is claimed')
    OUT.mkdir(parents=True, exist_ok=True)
    figure = OUT/'bratu-sensitivity.png'
    fig.savefig(figure, dpi=125)
    plt.close(fig)
    assert hashes == {name: digest(ROOT/name) for name in SOURCES}, 'Sources changed during build'
    manifest = dict(schema_version=1,
        settings=dict(alphas=[1., 2.], interior_nodes=[15, 31, 63],
            equation='F(u,lambda)=D*u-lambda*exp(u)=0; D=tridiag(-1,2,-1)/h^2',
            domain='[0,1]', boundary='u(0)=u(1)=0 fixed independently of lambda',
            initial_guess='zero vector in every independent parameter solve',
            branch='smooth lower branch, alpha=1 and alpha=2; no folds or branch switching validated',
            newton_tolerance_l2=tolerance, max_newton_updates=40,
            primal_jacobian='analytic; existing Armijo-damped dense Newton',
            derivative_construction='Forward AD of shared residual in augmented coordinates (u,lambda); no Newton iteration unrolling',
            implicit_equation='J*s=-F_lambda=exp(u)',
            objective='L_h=(h/2)*sum(u_i^2)+(beta/2)*lambda^2; h=1/(n+1)',
            beta=OBJECTIVE_BETA, objective_partials='L_u=h*u; L_lambda=beta*lambda',
            adjoint_equation='J.T*p=L_u; gradient=L_lambda-p.T*F_lambda',
            adjoint_convention='Euclidean discrete gradient; p contains h weighting and is not directly a continuum adjoint nodal value',
            state_error_norm='absolute maximum over interior nodes',
            gradient_error_norm='absolute scalar difference',
            residual_norms='unscaled residual Euclidean norms; relative sensitivity denominator ||F_lambda||2, adjoint denominator ||L_u||2',
            finite_difference='central parameter difference with separate zero-start nonlinear solves at lambda +/- epsilon',
            finite_difference_steps=steps.tolist(), finite_difference_n=31,
            tolerance_sweep=[1e-2, 1e-6, 1e-10], tolerance_sweep_alpha=2.,
            continuous_reference='Differentiate exact alpha-family; independent 96/192-point Gauss integral for continuum objective derivative'),
        grid_runs=runs, continuous_references=continuum, parameter_sweep=sweep,
        tolerance_sweep=tolerance_sweep, nonsymmetric_check=nonsymmetric,
        environment=dict(python=platform.python_version(), numpy=np.__version__, float_dtype='float64', float_epsilon=float(np.finfo(float).eps)),
        scope='Real, finite-dimensional implicit differentiation and discrete adjoints for smooth lower-branch Bratu. Original AD/Newton code retained. Dense linear solves, one physical parameter and one scalar objective. An independent nonsymmetric multiparameter manufactured system tests the transpose and sign. No reverse-mode AD engine, nonlinear-iteration differentiation, PDE-constrained inverse fit, time-dependent/continuous-adjoint solver, singular fold continuation, or performance ranking. Primal, derivative and continuum errors are distinct.',
        source_sha256=hashes, artifact_sha256={figure.name: digest(figure)})
    (OUT/'bratu-sensitivity.json').write_text(json.dumps(manifest, separators=(',', ':'), allow_nan=False)+'\n')
    for run in runs:
        print('alpha', run['alpha'], 'n', run['n'], 'sensitivity Linf', run['sensitivity_error_linf'], 'gradient', run['adjoint_gradient'], 'direct-adjoint', run['direct_adjoint_difference'], 'condition', run['jacobian_condition_2'])
    print('Built docs/figures/bratu-sensitivity.json and .png')


if __name__ == '__main__':
    build()
