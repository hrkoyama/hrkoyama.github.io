"""Independent continuum-angle response to positive periodic Fourier sources.

This oracle does not import the primary solver or use its FFT/quadrature/closure.
Moments use <g>=(4*pi)^-1 integral_S2 g dOmega and c=1. Thus E=<I>,
H=<Omega I>, K=<Omega Omega I>; physical quantities share a factor 4*pi.
The source is prescribed first, not manufactured from a chosen moment field.
"""
from __future__ import annotations

import math
import numpy as np


def mode_response(wave_numbers, amplitude, st=4., ss=3.):
    """Return exact complex Fourier coefficients in the Re(b*exp(i*k.x)) convention."""
    if (len(wave_numbers) not in (1, 2) or any(type(n) is not int for n in wave_numbers)
            or not any(wave_numbers)):
        raise ValueError('A nonzero integer spatial mode in one or two dimensions is required')
    st, ss = float(st), float(ss)
    if not (math.isfinite(st) and math.isfinite(ss) and st > ss >= 0):
        raise ValueError('Positive absorption and extinction are required')
    if not isinstance(amplitude, dict) or set(amplitude) != {'real', 'imag'}:
        raise ValueError('An explicit real/imaginary source amplitude is required')
    b = complex(amplitude['real'], amplitude['imag'])
    if not (math.isfinite(b.real) and math.isfinite(b.imag)):
        raise ValueError('Nonfinite source amplitude')
    vector = np.zeros(3)
    vector[:len(wave_numbers)] = [2*math.pi*n for n in wave_numbers]
    k = math.sqrt(math.fsum(float(x)*float(x) for x in vector))
    direction = vector/k
    R = math.atan(k/st)/k
    B = (1-st*R)/k
    C = st*(1-st*R)/(k*k)
    T = (R-C)/2
    scattering = b/(1-ss*R)
    tensor = np.eye(3)*T+(C-T)*direction[:, None]*direction[None, :]
    return {'wave_vector': vector, 'wave_number': k, 'source_amplitude': b,
            'scattering_amplitude': scattering, 'R': R, 'B': B, 'C': C, 'T': T,
            'E': scattering*R, 'H': -1j*scattering*B*direction,
            'K': scattering*tensor}


def reference_fields(case, coordinates, st=4., ss=3., omega=None):
    """Evaluate exact E,H,K,D and optional angle intensities at supplied point arrays.

    Coordinates are an ij-mesh tuple at any real positions, including shifted
    faces. E has spatial shape; H adds (3,), K/D add (3,3), I prepends (ndir,).
    A one-dimensional omega array may encode only mu_x: azimuth is irrelevant
    to I in a slab. The analytic K still contains both transverse components.
    """
    dimension = case.get('dimension')
    if dimension not in (1, 2) or not isinstance(coordinates, (tuple, list)) or len(coordinates) != dimension:
        raise ValueError('Coordinates must match the declared spatial dimension')
    points = tuple(np.asarray(x, dtype=float) for x in coordinates)
    shape = points[0].shape
    if not shape or any(x.shape != shape or not np.all(np.isfinite(x)) for x in points):
        raise ValueError('Finite, equally shaped point arrays are required')
    st, ss = float(st), float(ss)
    if not (math.isfinite(st) and math.isfinite(ss) and st > ss >= 0):
        raise ValueError('Positive absorption and extinction are required')
    source = case['source']
    mean = float(source['mean'])
    modes = source['modes']
    if not math.isfinite(mean) or not isinstance(modes, list):
        raise ValueError('Invalid mean source or mode list')
    # This sufficient positive-source bound is part of the two fixed examples.
    amplitudes = [complex(m['amplitude']['real'], m['amplitude']['imag']) for m in modes]
    if not (mean > math.fsum(abs(x) for x in amplitudes)):
        raise ValueError('The fixed source must remain strictly positive everywhere')
    responses = []
    wave_keys = []
    for mode in modes:
        waves = mode['wave_numbers']
        if len(waves) != dimension:
            raise ValueError('Source mode dimension differs')
        response = mode_response(waves, mode['amplitude'], st=st, ss=ss)
        key = tuple(waves)
        if key in wave_keys or tuple(-n for n in key) in wave_keys:
            raise ValueError('Repeated/conjugate source modes must be combined explicitly')
        wave_keys.append(key)
        responses.append((mode, response))
    E0 = mean/(st-ss)
    E = np.full(shape, E0)
    H = np.zeros(shape+(3,))
    K = np.broadcast_to(E0*np.eye(3)/3, shape+(3, 3)).copy()
    directions, I = None, None
    if omega is not None:
        directions = np.asarray(omega, dtype=float)
        if (directions.ndim != 2 or directions.shape[1] != 3 or not len(directions)
                or not np.all(np.isfinite(directions))):
            raise ValueError('Finite angular directions with shape(ndir,3) are required')
        norms = np.sum(directions*directions, axis=1)
        if (np.any(norms > 1+1e-13) or
                (dimension == 2 and np.any(np.abs(norms-1) > 1e-13))):
            raise ValueError('Directions must represent S2 or the slab mu_x reduction')
        I = np.full((len(directions),)+shape, E0)
    for mode, response in responses:
        phase = sum(2*math.pi*n*x for n, x in zip(mode['wave_numbers'], points))
        oscillation = np.exp(1j*phase)
        E += np.real(response['E']*oscillation)
        H += np.real(oscillation[..., None]*response['H'])
        K += np.real(oscillation[..., None, None]*response['K'])
        if I is not None:
            projection = sum(directions[:, j]*response['wave_vector'][j] for j in range(3))
            coefficient = response['scattering_amplitude']/(st+1j*projection)
            I += np.real(coefficient.reshape((len(directions),)+(1,)*len(shape))*oscillation[None, ...])
    if not (np.all(np.isfinite(E)) and np.all(E > 0) and np.all(np.isfinite(H)) and np.all(np.isfinite(K))):
        raise ValueError('Nonpositive/nonfinite analytic field')
    result = {'E': E, 'H': H, 'K': K, 'D': K/E[..., None, None]}
    if I is not None:
        if not (np.all(np.isfinite(I)) and np.all(I > 0)):
            raise ValueError('Nonpositive/nonfinite analytic intensity')
        result['I'] = I
    return result


def m1_tensor(E, H):
    """Pointwise dimensionless M1 tensor diagnostic; this is not an M1 PDE solver."""
    E, H = np.asarray(E, dtype=float), np.asarray(H, dtype=float)
    if H.shape != E.shape+(3,) or not (np.all(np.isfinite(E)) and np.all(E > 0) and np.all(np.isfinite(H))):
        raise ValueError('Positive finite energy and matching three-component flux required')
    magnitude = np.sqrt(np.sum(H*H, axis=-1))
    reduced = magnitude/E
    if np.any(reduced > 1):
        raise ValueError('M1 diagnostic input is not realizable; no clipping is used')
    direction = np.zeros_like(H)
    np.divide(H, magnitude[..., None], out=direction, where=magnitude[..., None] > 0)
    chi = (3+4*reduced*reduced)/(5+2*np.sqrt(4-3*reduced*reduced))
    return ((1-chi)[..., None, None]*np.eye(3)/2
            +(3*chi-1)[..., None, None]*direction[..., :, None]*direction[..., None, :]/2)
