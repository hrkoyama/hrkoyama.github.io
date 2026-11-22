"""Implicit state derivatives and discrete adjoints on the Bratu lower branch.

The converged residual is differentiated, not the finite Newton iteration.
General helpers accept several parameter columns. A nonsymmetric manufactured
example tests the transpose/sign convention independently of symmetric Bratu.
"""
import numpy as np
from .autodiff import bratu_matrix, bratu_residual, bratu_jacobian, jacobian
from .krylov import newton


OBJECTIVE_BETA = .05


def _linearization(matrix, parameter_derivative):
    matrix = np.asarray(matrix, dtype=float)
    parameter_derivative = np.asarray(parameter_derivative, dtype=float)
    if (matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]
            or not len(matrix) or not np.all(np.isfinite(matrix))):
        raise ValueError('A finite nonempty square state Jacobian is required')
    if (parameter_derivative.ndim not in (1, 2)
            or parameter_derivative.shape[0] != len(matrix)
            or not np.all(np.isfinite(parameter_derivative))):
        raise ValueError('F_theta must have shape (states,) or (states, parameters)')
    return matrix, parameter_derivative


def implicit_sensitivity(matrix, parameter_derivative):
    """Solve J U_theta = -F_theta; singular systems raise LinAlgError."""
    matrix, parameter_derivative = _linearization(matrix, parameter_derivative)
    return np.linalg.solve(matrix, -parameter_derivative)


def adjoint_gradient(matrix, parameter_derivative, objective_state, objective_parameter=0.):
    """Return (dL/dtheta,p) from J.T p=L_u and L_theta-p.T F_theta.

    L_u is the column-vector representation of the scalar objective's state
    gradient. No symmetry of J is assumed.
    """
    matrix, parameter_derivative = _linearization(matrix, parameter_derivative)
    objective_state = np.asarray(objective_state, dtype=float)
    if objective_state.shape != (len(matrix),) or not np.all(np.isfinite(objective_state)):
        raise ValueError('L_u must be a finite state-gradient vector')
    objective_parameter = np.asarray(objective_parameter, dtype=float)
    shape = () if parameter_derivative.ndim == 1 else (parameter_derivative.shape[1],)
    if objective_parameter.shape not in ((), shape) or not np.all(np.isfinite(objective_parameter)):
        raise ValueError('L_theta must be scalar or have one entry per parameter')
    adjoint = np.linalg.solve(matrix.T, objective_state)
    contraction = (np.sum(adjoint*parameter_derivative) if parameter_derivative.ndim == 1
                   else np.einsum('i,ij->j', adjoint, parameter_derivative))
    gradient = objective_parameter-contraction
    return (float(gradient) if gradient.ndim == 0 else gradient), adjoint


def family_reference(n, alpha=1.):
    """Exact continuous Bratu family and du/dlambda at the same alpha.

    alpha=1 and 2 are lower-branch settings. At the fold lambda'(alpha)=0,
    hence lambda is no longer a regular local family coordinate.
    """
    bratu_matrix(n)
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError('alpha must be positive and finite')
    x = np.arange(1, n+1)/(n+1)
    lam = float(2*alpha**2/np.cosh(alpha/2)**2)
    lam_alpha = lam*(2/alpha-np.tanh(alpha/2))
    if abs(lam_alpha) < 1e-12:
        raise ValueError('lambda is a singular family coordinate near the fold')
    u = -2*np.log(np.cosh(alpha*(x-.5))/np.cosh(alpha/2))
    u_alpha = np.tanh(alpha/2)-2*(x-.5)*np.tanh(alpha*(x-.5))
    return x, u, u_alpha/lam_alpha, lam


def solve_bratu(n, lam, tolerance=1e-10):
    """Zero-start Armijo-Newton solve using the original unscaled residual.

    Return all diagnostics; callers must reject failed solves. The exhibit
    only uses smooth lower-branch settings away from the fold.
    """
    bratu_matrix(n)
    if not np.isfinite(lam) or lam <= 0:
        raise ValueError('lambda must be positive and finite')
    return newton(lambda u: bratu_residual(u, lam),
                  lambda u: bratu_jacobian(u, lam), np.zeros(n),
                  tolerance=tolerance, maxiter=40, linear_solver='dense')


def bratu_derivatives(u, lam):
    """Differentiate the shared residual in augmented coordinates (u,lambda)."""
    augmented = np.r_[np.asarray(u, dtype=float), float(lam)]
    derivative = jacobian(lambda z: bratu_residual(z[:-1], z[-1]), augmented)
    return derivative[:, :-1], derivative[:, -1]


def objective(u, lam, beta=OBJECTIVE_BETA):
    """Discrete L=(h/2)sum(u_i^2)+(beta/2)lambda^2, h=1/(n+1).

    Fixed zero endpoints give zero trapezoidal boundary contributions. This
    is a discrete objective; continuum quadrature error remains.
    """
    u = np.asarray(u, dtype=float)
    if u.ndim != 1 or not len(u):
        raise ValueError('A nonempty state vector is required')
    return float(.5*np.sum(u*u)/(len(u)+1)+.5*beta*lam**2)


def objective_partials(u, lam, beta=OBJECTIVE_BETA):
    """Return L_u=h*u and the explicit partial L_lambda=beta*lambda."""
    u = np.asarray(u, dtype=float)
    return u/(len(u)+1), float(beta*lam)
