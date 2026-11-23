"""Independent continuous Fourier--Galerkin linear initial-value reference.

No primary finite-difference routine is imported. Derivatives of base profiles
come from Fourier coefficients, independently of the primary analytic formulas.
The linearization is a scoped reference for small perturbations, not a second
nonlinear PDE code and not the infinite-domain sharp-interface growth formula.
"""
import numpy as np
from scipy.linalg import eigvals
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply


def operator(case, kmax, controls, quadrature=1024):
    modes = np.arange(-kmax, kmax+1)
    total = len(modes)
    y = 2*np.pi*np.arange(quadrature)/quadrature
    base = np.tanh(np.sin(y)/controls['width'])
    coefficients = np.fft.fft(base)/quadrature
    difference = modes[:, None]-modes[None, :]
    multiply = coefficients[difference % quadrature]
    minus_laplacian = 1.+modes*modes
    diffusion = -np.diag(minus_laplacian)
    if case == 'kh-initial-growth':
        second = -(difference**2)*multiply
        matrix = -1j*(multiply+second/minus_laplacian[None, :])+controls['viscosity']*diffusion
    elif case == 'rt-initial-growth':
        gradient = controls['buoyancy']*1j*difference*multiply
        matrix = np.block([[controls['viscosity']*diffusion, 1j*np.eye(total)],
                           [1j*gradient/minus_laplacian[None, :], controls['diffusivity']*diffusion]])
    else:
        raise ValueError('Unknown reference case')
    return modes, matrix


def initial_coefficients(case, modes, epsilon):
    if case == 'kh-initial-growth':
        psi = np.where(modes == 0, 1., np.where(abs(modes) == 2, .125, 0.))*epsilon
        return (1.+modes*modes)*psi
    theta = np.where(modes == 0, 1., np.where(abs(modes) == 1, -.5, 0.))*epsilon
    return np.concatenate([np.zeros_like(theta), theta])


def trajectory(case, kmax, controls, epsilon, times):
    modes, matrix = operator(case, kmax, controls)
    start = initial_coefficients(case, modes, epsilon)
    times = np.asarray(times)
    if len(times) < 2 or not np.allclose(times, np.linspace(times[0], times[-1], len(times)), rtol=0, atol=1e-14):
        raise ValueError('Reference requires evenly spaced output times')
    states = expm_multiply(csr_matrix(matrix), start, start=float(times[0]),
                           stop=float(times[-1]), num=len(times), endpoint=True, traceA=np.trace(matrix))
    return modes, states, float(np.max(eigvals(matrix).real))


def fields(case, modes, state, n):
    size = len(modes)
    omega = state[:size]
    theta = state[size:] if case == 'rt-initial-growth' else np.zeros_like(omega)
    psi = omega/(1.+modes*modes)
    x = 2*np.pi*np.arange(n)/n
    phase_y = np.exp(1j*modes[:, None]*x[None, :])
    phase_x = np.exp(1j*x[:, None])
    def evaluate(coefficients):
        return (phase_x*(np.einsum('i,ij->j', coefficients, phase_y, optimize=False))[None, :]).real
    return dict(omega=evaluate(omega), theta=evaluate(theta),
                u=evaluate(1j*modes*psi), v=evaluate(-1j*psi))


def modal_amplitude(case, modes, state):
    size = len(modes)
    if case == 'rt-initial-growth':
        return float(np.sqrt(.5*np.sum(abs(state[size:])**2)))
    return float(np.sqrt(.5*np.sum(abs(state[:size])**2/(1.+modes*modes))))
