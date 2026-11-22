"""Small kinetic solvers and explicitly scoped independent references.

The CIC, collision and upwind kernels adapt scripts/depth-particles/transport.py.
Copyright (c) 2026 Hiroshi Koyama. MIT License:
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from math import pi

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import betainc, expn
from scipy.stats import beta


def _integer(value, lower, upper, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not lower <= value <= upper:
        raise ValueError(f'{name} must be an integer in [{lower}, {upper}]')


def _positive(value, name):
    if not np.isscalar(value) or not np.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be positive and finite')


def cic_state(position, grid, length=2*pi):
    """Periodic neutral electron PIC; matched CIC gather and skew spectral E.

    rho=1-n_e, -phi_xx=rho, E=-phi_x, electron acceleration=-E.
    Nyquist is a null mode of the real skew first derivative, separately exposed.
    """
    _integer(grid, 4, 512, 'grid')
    _positive(length, 'length')
    x = np.asarray(position, dtype=float)
    if x.ndim != 1 or len(x) < 2 or not np.isfinite(x).all():
        raise ValueError('Finite one-dimensional particle coordinates required')
    u = (x % length)*grid/length
    left = np.floor(u).astype(int)
    fraction = u-left
    density = (np.bincount(left, weights=1-fraction, minlength=grid)
               + np.bincount((left+1) % grid, weights=fraction, minlength=grid))*grid/len(x)
    rho = 1-density
    modes = 2*pi*np.fft.fftfreq(grid, d=length/grid)
    charge_hat = np.fft.fft(rho)
    electric_hat = np.zeros(grid, complex)
    resolved = modes != 0
    if grid % 2 == 0:
        resolved[grid//2] = False
    electric_hat[resolved] = charge_hat[resolved]/(1j*modes[resolved])
    electric = np.fft.ifft(electric_hat).real
    acceleration = -((1-fraction)*electric[left]+fraction*electric[(left+1) % grid])
    gauss_hat = 1j*modes*electric_hat-charge_hat
    gauss = float(np.max(np.abs(gauss_hat[resolved]))/grid)
    nyquist = float(abs(charge_hat[grid//2])/grid) if grid % 2 == 0 else 0.
    return acceleration, {
        'charge_error': float(abs(np.sum(rho))*length/grid),
        'resolved_gauss_error': gauss,
        'nyquist_charge': nyquist,
        'field_energy': float(.5*length/grid*np.dot(electric, electric)),
        'grid_field_rms': float(np.sqrt(np.mean(electric**2))),
        'grid_charge_mode_power': float(abs(charge_hat[1]/grid)**2),
    }


def quiet_start(particles, amplitude):
    _integer(particles, 16, 8192, 'particles')
    if not np.isfinite(amplitude) or not 0 < amplitude < .01:
        raise ValueError('Small positive amplitude < .01 required')
    base = (np.arange(particles)+.5)*2*pi/particles
    return base, base+amplitude*np.sin(base), np.zeros(particles)


def plasma_verlet(grid, particles, dt, end_time, amplitude):
    _positive(dt, 'dt')
    _positive(end_time, 'end_time')
    if end_time > 8 or dt > .5:
        raise ValueError('Short-time educational PIC budget exceeded')
    base, x, v = quiet_start(particles, amplitude)
    shape = np.sin(base)
    normalization = amplitude*np.dot(shape, shape)
    steps = int(np.ceil(end_time/dt))
    if steps > 4000:
        raise ValueError('PIC step budget exceeded')
    step = end_time/steps
    acceleration, state = cic_state(x, grid)
    initial_energy = state['field_energy']
    history = []
    extrema = dict(charge_error=0., momentum_error=0., resolved_gauss_error=0.,
                   nyquist_charge=0., relative_energy_drift=0.)
    for index in range(steps+1):
        time = index*step
        mode = float(np.dot(x-base, shape)/normalization)
        energy = float(pi/particles*np.dot(v, v)+state['field_energy'])
        momentum = float(abs(2*pi/particles*np.sum(v)))
        drift = float(abs(energy-initial_energy)/initial_energy)
        extrema['momentum_error'] = max(extrema['momentum_error'], momentum)
        extrema['relative_energy_drift'] = max(extrema['relative_energy_drift'], drift)
        for name in ('charge_error', 'resolved_gauss_error', 'nyquist_charge'):
            extrema[name] = max(extrema[name], state[name])
        history.append(dict(time=float(time), mode=mode, continuum_mode=float(np.cos(time)),
                            energy=energy, relative_energy_drift=drift,
                            momentum_error=momentum, **state))
        if index < steps:
            v += .5*step*acceleration
            x += step*v
            acceleration, state = cic_state(x, grid)
            v += .5*step*acceleration
    return dict(dt=float(step), particles=particles, grid=grid,
                particles_per_cell=float(particles/grid), final_position=x,
                final_velocity=v, records=history,
                max_mode_error=float(max(abs(r['mode']-r['continuum_mode']) for r in history)),
                **extrema)


def plasma_dop853(grid, particles, end_time, amplitude, rtol, atol, max_step):
    """Independent *time integrator* of the shared CIC particle-grid RHS."""
    base, x, v = quiet_start(particles, amplitude)
    _positive(end_time, 'end_time')
    _positive(max_step, 'max_step')
    if not 1e-14 <= rtol <= 1e-6 or not 1e-15 <= atol <= 1e-7:
        raise ValueError('Reference tolerances outside the educational budget')
    def rhs(_time, y):
        a, _ = cic_state(y[:particles], grid)
        return np.concatenate((y[particles:], a))
    solution = solve_ivp(rhs, (0., end_time), np.concatenate((x, v)), method='DOP853',
                         rtol=rtol, atol=atol, max_step=max_step)
    if not solution.success or not np.isfinite(solution.y).all():
        raise RuntimeError('DOP853 particle-grid reference failed')
    final = solution.y[:, -1]
    return dict(final_position=final[:particles], final_velocity=final[particles:],
                mode=float(np.dot(final[:particles]-base, np.sin(base))
                           /(amplitude*np.dot(np.sin(base), np.sin(base)))),
                evaluations=int(solution.nfev))


def elastic_round(velocity, rng):
    """One isotropic random matching, with no physical-time calibration."""
    v = np.asarray(velocity)
    if v.ndim != 2 or v.shape[1] != 3 or len(v) < 4 or len(v) % 2 or not np.isfinite(v).all() or v.dtype.kind != 'f':
        raise ValueError('Finite, even, floating N by 3 velocity array required')
    first, second = rng.permutation(len(v)).reshape(-1, 2).T
    center = .5*(v[first]+v[second])
    half_speed = .5*np.linalg.norm(v[first]-v[second], axis=1)
    cosine = rng.uniform(-1., 1., len(first))
    azimuth = rng.uniform(0., 2*pi, len(first))
    sine = np.sqrt(1-cosine*cosine)
    direction = np.column_stack((sine*np.cos(azimuth), sine*np.sin(azimuth), cosine))
    relative = half_speed[:, None]*direction
    v[first] = center+relative
    v[second] = center-relative


def microcanonical_sample(particles, rng):
    """Uniform sphere in zero-momentum subspace, independent of collisions."""
    _integer(particles, 4, 8192, 'particles')
    v = rng.standard_normal((particles, 3))
    v -= v.mean(axis=0)
    v *= np.sqrt(3*particles/np.sum(v*v))
    return v


def microcanonical_energy_cdf(energy, particles):
    _integer(particles, 4, 8192, 'particles')
    energy = np.asarray(energy, dtype=float)
    if not np.isfinite(energy).all():
        raise ValueError('Finite energies required')
    return betainc(1.5, 1.5*(particles-2), np.clip(energy/(1.5*(particles-1)), 0., 1.))


def microcanonical_fourth(particles):
    _integer(particles, 4, 8192, 'particles')
    return 9*(particles-1)/(3*particles-1)


def absorption_slab(cells, ordinates, optical_depth, scheme='upwind'):
    _integer(cells, 1, 1024, 'cells')
    _integer(ordinates, 2, 128, 'ordinates')
    _positive(optical_depth, 'optical_depth')
    if optical_depth > 20 or scheme not in ('upwind', 'characteristic'):
        raise ValueError('Unsupported slab depth or marching scheme')
    mu, weight = np.polynomial.legendre.leggauss(ordinates)
    mu, weight = .5*(mu+1), .5*weight
    increment = optical_depth/(cells*mu)
    attenuation = np.log1p(increment) if scheme == 'upwind' else increment
    intensity = np.exp(-np.arange(cells+1)[:, None]*attenuation)
    exact = np.exp(-np.arange(cells+1)[:, None]*increment)
    incoming = 2*pi*float(np.dot(weight, mu))
    outgoing = 2*pi*float(np.dot(weight*mu, intensity[-1]))
    characteristic = 2*pi*float(np.dot(weight*mu, exact[-1]))
    if scheme == 'upwind':
        absorbed = 2*pi*optical_depth/cells*float(np.sum(intensity[1:]*weight))
    else:
        # Exact per-cell characteristic loss, summed rather than 1-Fout.
        absorbed = 2*pi*float(np.sum((intensity[:-1]-intensity[1:])*(weight*mu)))
    return dict(flux=outgoing, characteristic_flux=characteristic, absorbed_flux=absorbed,
                spatial_flux_error=abs(outgoing-characteristic),
                ray_max_error=float(np.max(abs(intensity-exact))),
                balance_error=abs(incoming-outgoing-absorbed),
                minimum_intensity=float(intensity.min()), maximum_intensity=float(intensity.max()))


def slab_references(optical_depth, epsabs=1e-12, epsrel=1e-12):
    _positive(optical_depth, 'optical_depth')
    value, error = quad(lambda mu: mu*np.exp(-optical_depth/mu), 0., 1.,
                        epsabs=epsabs, epsrel=epsrel)
    return dict(quad_flux=float(2*pi*value), quad_error=float(2*pi*error),
                expn_flux=float(2*pi*expn(3, optical_depth)))


def photon_survival(histories, optical_depth, rng, confidence=.95):
    """Analog flux photons: mu=sqrt(U), exponential path, Bernoulli exit."""
    _integer(histories, 16, 1000000, 'histories')
    _positive(optical_depth, 'optical_depth')
    if not 0 < confidence < 1:
        raise ValueError('Confidence must lie strictly between zero and one')
    cosine = np.sqrt(rng.random(histories))
    optical_path = rng.exponential(size=histories)
    escaped = int(np.count_nonzero(cosine*optical_path > optical_depth))
    alpha = 1-confidence
    lower = 0. if escaped == 0 else float(beta.ppf(alpha/2, escaped, histories-escaped+1))
    upper = 1. if escaped == histories else float(beta.ppf(1-alpha/2, escaped+1, histories-escaped))
    return dict(escaped=escaped, absorbed=histories-escaped, survival=escaped/histories,
                lower=lower, upper=upper, flux=float(pi*escaped/histories),
                count_balance=escaped+(histories-escaped)-histories)
