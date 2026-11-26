"""Periodic formal angular transport coupled to an independent FD moment solve.

No analytic-reference import is permitted in this module. Spatial values are
POINT samples at i/N. A face is at (i+1/2)/N, with one shared owner per face.
"""
from __future__ import annotations

import math
import numpy as np


class SolverFailure(RuntimeError):
    def __init__(self, message, state):
        super().__init__(message)
        self.state = state


def _tick(deadline, state, phase, **fields):
    state.update(fields)
    state['phase'] = phase
    if deadline is not None:
        deadline(state)


def _require(condition, message, state):
    if not condition:
        raise SolverFailure(message, dict(state))


def quadrature(dimension, mu_order, phi_order=None):
    """Normalized full-S2 measure, with analytic azimuthal averaging in 1D."""
    if dimension not in (1, 2) or type(mu_order) is not int or mu_order < 2:
        raise ValueError('Invalid angular quadrature')
    mu, weight = np.polynomial.legendre.leggauss(mu_order)
    if dimension == 1:
        if phi_order is not None:
            raise ValueError('The slab quadrature integrates azimuth analytically')
        omega = np.zeros((mu_order, 3))
        omega[:, 0] = mu
        return {'omega': omega, 'weights': weight/2, 'axisymmetric': True}
    if type(phi_order) is not int or phi_order < 4 or phi_order % 4:
        raise ValueError('Use a full uniformly sampled azimuth')
    phi = 2*np.pi*np.arange(phi_order)/phi_order
    radius = np.sqrt(1-mu*mu)
    omega = np.stack([np.broadcast_to(radius[:, None]*np.cos(phi), (mu_order, phi_order)),
                      np.broadcast_to(radius[:, None]*np.sin(phi), (mu_order, phi_order)),
                      np.broadcast_to(mu[:, None], (mu_order, phi_order))], axis=-1).reshape(-1, 3)
    weights = np.broadcast_to(weight[:, None]/(2*phi_order), (mu_order, phi_order)).ravel().copy()
    return {'omega': omega, 'weights': weights, 'axisymmetric': False}


def coordinates(shape):
    if len(shape) not in (1, 2) or any(type(n) is not int or n < 5 or n % 2 == 0 for n in shape):
        raise ValueError('Odd periodic point grids are required')
    if len(set(shape)) != 1:
        raise ValueError('This fixed protocol uses equal spacing in every axis')
    return tuple(np.meshgrid(*(np.arange(n)/n for n in shape), indexing='ij'))


def source_values(case, shape):
    points = coordinates(shape)
    q = np.full(shape, float(case['source']['mean']))
    for mode in case['source']['modes']:
        waves = mode['wave_numbers']
        if len(waves) != len(shape) or any(type(k) is not int for k in waves):
            raise ValueError('Fourier source modes require integer wave numbers')
        phase = sum(2*np.pi*k*x for k, x in zip(waves, points))
        b = mode['amplitude']
        q += float(b['real'])*np.cos(phase)-float(b['imag'])*np.sin(phase)
    if not np.all(np.isfinite(q)) or not np.all(q > 0):
        raise ValueError('The prescribed fixed source must be strictly positive')
    return q


def face_fluxes(E, D, st):
    """Conservative face fluxes including both mixed-derivative contributions."""
    h = 1/E.shape[0]
    pxx = D[..., 0, 0]*E
    fx = -(np.roll(pxx, -1, axis=0)-pxx)/(h*st)
    if E.ndim == 1:
        return (fx,)
    pyy, pxy = D[..., 1, 1]*E, D[..., 0, 1]*E
    dy = (np.roll(pxy, -1, axis=1)-np.roll(pxy, 1, axis=1))/(2*h)
    dx = (np.roll(pxy, -1, axis=0)-np.roll(pxy, 1, axis=0))/(2*h)
    fx -= (np.roll(dy, -1, axis=0)+dy)/(2*st)
    fy = -(np.roll(pyy, -1, axis=1)-pyy)/(h*st)
    fy -= (np.roll(dx, -1, axis=1)+dx)/(2*st)
    return fx, fy


def face_divergence(faces):
    n = faces[0].shape[0]
    return sum(n*(face-np.roll(face, 1, axis=axis)) for axis, face in enumerate(faces))


def centered_flux(faces):
    out = np.zeros(faces[0].shape+(3,))
    for axis, face in enumerate(faces):
        out[..., axis] = (face+np.roll(face, 1, axis=axis))/2
    return out


def moment_operator(E, D, st, sa):
    return st*(sa*E+face_divergence(face_fluxes(E, D, st)))


def _preconditioner(shape, st, sa):
    symbol = np.full(shape, st*sa)
    for axis, n in enumerate(shape):
        modes = np.fft.fftfreq(n)*n
        view = [1]*len(shape)
        view[axis] = n
        symbol += (4*n*n*np.sin(np.pi*modes/n)**2/3).reshape(view)
    return symbol


def _real_ifft(values, axes, state, settings):
    complex_field = np.fft.ifftn(values, axes=axes)
    imag = float(np.max(np.abs(complex_field.imag)))
    scale = max(float(np.max(np.abs(complex_field.real))), np.finfo(float).tiny)
    residue = imag/scale
    state['ifft_complex_candidate'] = complex_field
    state['imaginary_residue'] = residue
    _require(math.isfinite(residue) and residue <= settings['imaginary_ifft_residue_max'],
             'Non-negligible imaginary inverse-FFT residue', state)
    return complex_field.real.copy(), residue


def formal_transport(q, E_LO, angular, settings, deadline=None, state=None, feedback='coupled'):
    """Formal FFT solve using the actual supplied LO state, never a reference."""
    state = {} if state is None else state
    st, ss = settings['st'], settings['ss']
    if feedback not in ('coupled', 'frozen-initial'):
        raise ValueError('Unknown explicit feedback variant')
    scatter = E_LO if feedback == 'coupled' else np.full_like(E_LO, settings['qmean']/(st-ss))
    source = q+ss*scatter
    source_hat = np.fft.fftn(source)
    shape, dimension = E_LO.shape, E_LO.ndim
    waves = np.meshgrid(*(2*np.pi*np.fft.fftfreq(n, d=1/n) for n in shape), indexing='ij')
    omega, weights = angular['omega'], angular['weights']
    I = np.full((len(weights),)+shape, np.nan)
    E, H, K = np.zeros(shape), np.zeros(shape+(3,)), np.zeros(shape+(3, 3))
    imag_max, residual_max = 0., 0.
    scale = max(float(np.max(np.abs(source_hat))), np.finfo(float).tiny)
    state.update(E_LO=E_LO, source=source, source_hat=source_hat, I=I, I_valid_directions=0)
    for first in range(0, len(weights), settings['angular_chunk']):
        last = min(first+settings['angular_chunk'], len(weights))
        _tick(deadline, state, 'formal-transfer', angular_first=first, angular_last=last)
        view = (last-first,)+(1,)*dimension
        streaming = sum(omega[first:last, axis].reshape(view)*waves[axis] for axis in range(dimension))
        denominator = st+1j*streaming
        candidate = source_hat[None, ...]/denominator
        state['I_hat_candidate'] = candidate
        residual_max = max(residual_max, float(np.max(np.abs(denominator*candidate-source_hat[None, ...])))/scale)
        values, imaginary = _real_ifft(candidate, tuple(range(1, dimension+1)), state, settings)
        I[first:last] = values
        state['I_valid_directions'] = last
        _require(np.all(np.isfinite(values)) and np.all(values > 0), 'Angular intensity is not strictly positive and finite', state)
        imag_max = max(imag_max, imaginary)
        weighted = weights[first:last].reshape(view)*values
        E += np.sum(weighted, axis=0)
        for i in range(3 if dimension == 2 else 1):
            H[..., i] += np.sum(weighted*omega[first:last, i].reshape(view), axis=0)
        if dimension == 1:
            K[..., 0, 0] += np.sum(weighted*omega[first:last, 0].reshape(view)**2, axis=0)
        else:
            for i in range(3):
                for j in range(i, 3):
                    K[..., i, j] += np.sum(weighted*(omega[first:last, i]*omega[first:last, j]).reshape(view), axis=0)
    if dimension == 1:
        K[..., 1, 1] = (E-K[..., 0, 0])/2
        K[..., 2, 2] = K[..., 1, 1]
    else:
        for i in range(3):
            for j in range(i):
                K[..., i, j] = K[..., j, i]
    state.update(HO_E=E, HO_H=H, HO_K=K)
    _require(np.all(np.isfinite(E)) and np.all(E > 0), 'Formal energy is not strictly positive and finite', state)
    D = K/E[..., None, None]
    state['D_candidate'] = D
    _require(np.all(np.isfinite(D)), 'Nonfinite angular closure', state)
    _require(residual_max <= settings['HO_formal_relative_residual_max'], 'Formal transfer residual exceeds its cap', state)
    return {'I': I, 'E': E, 'H': H, 'K': K, 'D': D, 'source': source,
            'omega': omega, 'weights': weights, 'imaginary_residue': imag_max,
            'formal_residual': residual_max}


def solve_inner(q, D, initial, settings, deadline=None, state=None):
    state = {} if state is None else state
    st, sa = settings['st'], settings['st']-settings['ss']
    rhs = st*q
    scale = max(float(np.max(np.abs(rhs))), np.finfo(float).tiny)
    symbol = _preconditioner(q.shape, st, sa)
    E = initial.copy()
    imaginary = 0.
    for iteration in range(settings['inner_maximum']+1):
        residual = rhs-moment_operator(E, D, st, sa)
        rel = float(np.max(np.abs(residual)))/scale
        _tick(deadline, state, 'inner-moment', inner_iteration=iteration,
              E_accepted=E, residual=residual, inner_true_relative_residual=rel, D=D)
        _require(math.isfinite(rel), 'Nonfinite inner true residual', state)
        if rel <= settings['LO_true_relative_inf_residual_max']:
            return E, {'iterations': iteration, 'relative_residual': rel, 'imaginary_residue': imaginary}
        _require(iteration < settings['inner_maximum'], 'Fixed Richardson iteration cap reached', state)
        step, im = _real_ifft(np.fft.fftn(residual)/symbol, None, state, settings)
        candidate = E+step
        state['E_failed_candidate'] = candidate
        _tick(deadline, state, 'inner-candidate', E_failed_candidate=candidate)
        _require(np.all(np.isfinite(candidate)) and np.all(candidate > 0), 'LO candidate is not strictly positive and finite', state)
        E = candidate
        imaginary = max(imaginary, im)
    raise AssertionError('unreachable')


def solve(case, row, settings, deadline=None, closure='transport', feedback='coupled'):
    """Solve one frozen row; explicit variants are reserved for negative controls."""
    shape = tuple(row['shape'])
    if case['dimension'] != len(shape) or closure not in ('transport', 'isotropic'):
        raise ValueError('Invalid fixed-case shape/closure')
    if not (settings['st'] > settings['ss'] >= 0 and settings['qmean'] > 0):
        raise ValueError('Positive extinction and absorption are required')
    q = source_values(case, shape)
    angular = quadrature(case['dimension'], row['mu_order'], row.get('phi_order'))
    E = np.full(shape, settings['qmean']/(settings['st']-settings['ss']))
    state = {'case_id': case['id'], 'row_id': row['id'], 'E_accepted': E, 'q': q, 'history': []}
    _tick(deadline, state, 'initial-state')
    ho = formal_transport(q, E, angular, settings, deadline, state, feedback)
    history, inner_work, formal_work = [], 0, 1
    for outer in range(1, settings['outer_maximum']+1):
        D = ho['D'] if closure == 'transport' else np.broadcast_to(np.eye(3)/3, shape+(3, 3)).copy()
        state.update(outer_iteration=outer, E_previous=E, D_previous=D, HO_E=ho['E'], I=ho['I'])
        _tick(deadline, state, 'outer-moment', history=history)
        candidate, inner = solve_inner(q, D, E, settings, deadline, state)
        inner_work += inner['iterations']
        next_ho = formal_transport(q, candidate, angular, settings, deadline, state, feedback)
        formal_work += 1
        next_D = next_ho['D'] if closure == 'transport' else D
        delta_E = float(np.max(np.abs(candidate-E)))/float(np.max(np.abs(candidate)))
        delta_D = float(np.max(np.abs(next_D-D)))
        residual = moment_operator(candidate, next_D, settings['st'], settings['st']-settings['ss'])-settings['st']*q
        true_residual = float(np.max(np.abs(residual)))/float(np.max(np.abs(settings['st']*q)))
        faces = face_fluxes(candidate, next_D, settings['st'])
        budget = face_divergence(faces)+(settings['st']-settings['ss'])*candidate-q
        hho = next_ho['H']/next_ho['E'][..., None]
        eig = np.linalg.eigvalsh(next_D)
        covariance = next_D-hho[..., :, None]*hho[..., None, :]
        trace_error = float(np.max(np.abs(np.trace(next_D, axis1=-2, axis2=-1)-1)))
        record = {'outer': outer, 'LOE_relative_update': delta_E, 'D_max_update': delta_D,
                  'true_LO_relative_residual': true_residual,
                  'formal_transport_residual': next_ho['formal_residual'],
                  'HOE_minus_LOE_rms': float(np.sqrt(np.mean((next_ho['E']-candidate)**2))),
                  'minimum_I': float(np.min(next_ho['I'])), 'minimum_LOE': float(np.min(candidate)),
                  'tensor_min_eigenvalue': float(np.min(eig)), 'tensor_max_eigenvalue': float(np.max(eig)),
                  'HO_covariance_min_eigenvalue': float(np.min(np.linalg.eigvalsh(covariance))),
                  'tensor_trace_error': trace_error,
                  'discrete_global_balance': abs(float(np.mean(budget))),
                  'inner_iterations': inner['iterations'], 'imaginary_residue': max(inner['imaginary_residue'], next_ho['imaginary_residue'])}
        history.append(record)
        state.update(E_failed_candidate=candidate, D_candidate=next_D, final_faces=faces, history=history, HO_E=next_ho['E'], I=next_ho['I'])
        _tick(deadline, state, 'outer-assessment')
        E, ho = candidate, next_ho
        if (delta_E <= settings['outer_LOE_relative_update_max'] and delta_D <= settings['outer_D_absolute_update_max']
                and true_residual <= settings['LO_true_relative_inf_residual_max']):
            result = {**ho, 'E_LO': E, 'D': next_D, 'q': q, 'faces': faces,
                      'H_LO_center': centered_flux(faces), 'history': history, 'converged': True,
                      'work': {'outer_iterations': outer, 'inner_iterations': inner_work,
                               'formal_solves': formal_work, 'directional_solves': formal_work*len(angular['weights'])},
                      'variant': {'closure': closure, 'feedback': feedback}}
            _tick(deadline, state, 'completed-row')
            return result
    raise SolverFailure('Fixed outer iteration cap reached', state)
