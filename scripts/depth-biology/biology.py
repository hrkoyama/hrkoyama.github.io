"""Finite-amplitude Schnakenberg tests: FD splitting and independent Galerkin/Radau.

The reference is deliberately a different spatial and temporal discretization.
Its real cosine representation is valid only for the declared reflection-even IC.
"""
import math
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.sparse import bmat, diags


def product(left, right):
    # Non-BLAS contraction avoids a NumPy 2.0/macOS matmul FP-status artifact.
    # No floating-point warning is suppressed; all results remain checked normally.
    return np.einsum('ik,kj->ij', left, right, optimize=False)


class Budget:
    def __init__(self, seconds=120.):
        if not math.isfinite(seconds) or not 0 < seconds <= 120:
            raise ValueError('Budget must be positive and at most 120 seconds')
        self.deadline = time.perf_counter()+seconds

    def check(self):
        if time.perf_counter() > self.deadline:
            raise RuntimeError('Fixed 120-second-or-less calculation budget exhausted')


def validate(config):
    def real(value, name, positive=True):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or (positive and value <= 0):
            raise ValueError('Invalid '+name)
    for key in ['a', 'b', 'time', 'space_step', 'reference_rtol', 'reference_atol', 'tight_rtol', 'tight_atol', 'newton_tolerance']:
        real(config[key], key)
    if config['time'] > 100 or config['tight_rtol'] >= config['reference_rtol'] or config['tight_atol'] >= config['reference_atol']:
        raise ValueError('Invalid fixed reference budget or tolerance ordering')
    for key, maximum in [('grids', 256), ('reference_modes', 128)]:
        values = config[key]
        if len(values) != 3 or values != sorted(set(values)) or any(type(v) is not int or not 8 <= v <= maximum for v in values):
            raise ValueError('Invalid bounded '+key)
    if type(config['temporal_grid']) is not int or not 16 <= config['temporal_grid'] <= 256:
        raise ValueError('Invalid temporal grid')
    if type(config['diagnostic_grid']) is not int or not 64 <= config['diagnostic_grid'] <= 2048:
        raise ValueError('Invalid diagnostic grid')
    if type(config['newton_iterations']) is not int or not 2 <= config['newton_iterations'] <= 20:
        raise ValueError('Invalid Newton iteration budget')
    if len(config['time_steps']) != 3 or config['time_steps'] != sorted(set(config['time_steps']), reverse=True):
        raise ValueError('Require three descending time steps')
    for step in [config['space_step']]+config['time_steps']:
        real(step, 'step')
        count = round(config['time']/step)
        if count > 100000 or not math.isclose(count*step, config['time'], abs_tol=1e-11):
            raise ValueError('Time step must divide final time within the fixed step budget')
        if any(not math.isclose(round(t/step)*step, t, abs_tol=1e-11) for t in config['snapshot_times']):
            raise ValueError('All snapshot times must lie on each fixed time grid')
    for value in config['diffusion']:
        real(value, 'diffusion')
    if len(config['diffusion']) != 2:
        raise ValueError('Two diffusivities required')
    coefficients = np.asarray(config['initial_cosine_coefficients'], float)
    if coefficients.shape != (2, 5) or not np.isfinite(coefficients).all():
        raise ValueError('Two five-term cosine coefficient rows required')
    if config['snapshot_times'][0] != 0 or config['snapshot_times'][-1] != config['time'] or config['snapshot_times'] != sorted(set(config['snapshot_times'])):
        raise ValueError('Invalid snapshot ordering')
    for value in config['acceptance'].values():
        real(value, 'acceptance', positive=False)
        if value < 0:
            raise ValueError('Negative acceptance criterion')


def initial_field(config, x):
    return product(np.asarray(config['initial_cosine_coefficients']), np.cos(np.arange(5)[:, None]*np.asarray(x)[None, :]))


def kinetics(y, a, b):
    u, v = y
    rate = u*u*v
    return np.array([a-u+rate, b-rate])


def periodic_laplacian(y, dx):
    return (np.roll(y, -1, axis=-1)-2*y+np.roll(y, 1, axis=-1))/(dx*dx)


def midpoint_reaction(y, step, a, b, tolerance=2e-13, iterations=12):
    """Local coupled implicit midpoint; never clip, fall back, or change the step."""
    new = y.copy()
    minimum_iterate = float(new.min())
    for iteration in range(iterations):
        mid = (y+new)/2
        u, v = mid
        residual = new-y-step*kinetics(mid, a, b)
        error = float(np.max(np.abs(residual)))
        if not np.isfinite(new).all() or np.max(np.abs(new)) > 1e6:
            raise RuntimeError('Unbounded midpoint Newton state')
        if error <= tolerance:
            return new, mid, {'residual': error, 'iterations': iteration,
                              'minimum_newton_iterate': minimum_iterate}
        aa = 1+step/2-step*u*v
        bb = -step*u*u/2
        cc = step*u*v
        dd = 1+step*u*u/2
        det = aa*dd-bb*cc
        if np.any(np.abs(det) < 1e-12):
            raise RuntimeError('Singular midpoint Newton matrix')
        correction = np.array([(dd*residual[0]-bb*residual[1])/det,
                               (aa*residual[1]-cc*residual[0])/det])
        new -= correction
        minimum_iterate = min(minimum_iterate, float(new.min()))
    raise RuntimeError('Midpoint Newton failed within the declared iteration budget')


def fd_split(config, n, step, budget=None):
    """FD2 exact diffusion half-steps / implicit-midpoint reaction (Strang)."""
    budget = budget or Budget()
    x = np.arange(n)*2*math.pi/n
    y = initial_field(config, x)
    modes = np.arange(n//2+1)
    # These are FD eigenvalues, not continuum Fourier eigenvalues.
    eigenvalues = -4*np.sin(math.pi*modes/n)**2/(2*math.pi/n)**2
    multiplier = np.exp(np.asarray(config['diffusion'])[:, None]*eigenvalues*step/2)
    diffuse = lambda field: np.fft.irfft(np.fft.rfft(field)*multiplier, n=n)
    snapshots = {0.: y.copy()}
    wanted = {round(t/step): t for t in config['snapshot_times']}
    initial_total = float(y.sum(axis=0).mean())
    source_integral = 0.
    diagnostic = {'minimum_concentration': float(y.min()), 'minimum_newton_iterate': float(y.min()),
                  'maximum_midpoint_residual': 0., 'maximum_newton_iterations': 0,
                  'maximum_reaction_balance_error': 0.}
    for index in range(1, round(config['time']/step)+1):
        if index % 64 == 1:
            budget.check()
        y, mid, info = midpoint_reaction(diffuse(y), step, config['a'], config['b'],
                                         config['newton_tolerance'], config['newton_iterations'])
        source_integral += step*(config['a']+config['b']-float(mid[0].mean()))
        diagnostic['minimum_concentration'] = min(diagnostic['minimum_concentration'], float(y.min()))
        y = diffuse(y)
        diagnostic['minimum_concentration'] = min(diagnostic['minimum_concentration'], float(y.min()))
        diagnostic['minimum_newton_iterate'] = min(diagnostic['minimum_newton_iterate'], info['minimum_newton_iterate'])
        diagnostic['maximum_midpoint_residual'] = max(diagnostic['maximum_midpoint_residual'], info['residual'])
        diagnostic['maximum_newton_iterations'] = max(diagnostic['maximum_newton_iterations'], info['iterations'])
        balance = abs(float(y.sum(axis=0).mean())-initial_total-source_integral)
        diagnostic['maximum_reaction_balance_error'] = max(diagnostic['maximum_reaction_balance_error'], balance)
        if index in wanted:
            snapshots[wanted[index]] = y.copy()
    return snapshots, diagnostic


class CosineGalerkin:
    """Independent cosine Galerkin RHS; M>4K integrates all retained cubic modes."""
    def __init__(self, modes, config, budget):
        self.k = np.arange(modes+1)
        self.m = 4*(modes+1)
        self.basis = np.cos(np.arange(self.m)[:, None]*2*math.pi/self.m*self.k)
        self.project = self.basis.T*(2/self.m)
        self.project[0] /= 2
        self.diffusion = np.asarray(config['diffusion'])
        self.a, self.b, self.budget = config['a'], config['b'], budget

    def rhs(self, t, vector):
        self.budget.check()
        coefficients = vector.reshape(2, -1)
        u, v = product(coefficients, self.basis.T)
        cubic = u*u*v
        reaction = product(np.array([self.a-u+cubic, self.b-cubic]), self.project.T)
        return (reaction-self.diffusion[:, None]*self.k**2*coefficients).ravel()

    def jac(self, t, vector):
        self.budget.check()
        u, v = product(vector.reshape(2, -1), self.basis.T)
        uv = self.project*(2*u*v)
        uu = self.project*(u*u)
        j00 = product(uv, self.basis)-np.eye(len(self.k))-np.diag(self.diffusion[0]*self.k**2)
        j01 = product(uu, self.basis)
        j10 = -product(uv, self.basis)
        j11 = -j01-np.diag(self.diffusion[1]*self.k**2)
        return np.block([[j00, j01], [j10, j11]])


def galerkin_reference(config, modes, rtol, atol, budget):
    system = CosineGalerkin(modes, config, budget)
    initial = np.zeros((2, modes+1))
    initial[:, :5] = config['initial_cosine_coefficients']
    sol = solve_ivp(system.rhs, [0, config['time']], initial.ravel(), method='Radau',
                    jac=system.jac, t_eval=config['snapshot_times'], rtol=rtol, atol=atol)
    if not sol.success or sol.t[-1] != config['time']:
        raise RuntimeError('Galerkin Radau reference failed: '+sol.message)
    snapshots = {float(t): y.reshape(2, modes+1) for t, y in zip(sol.t, sol.y.T)}
    return snapshots, {'nfev': sol.nfev, 'njev': sol.njev, 'nlu': sol.nlu,
                       'modes': modes, 'product_points': system.m, 'rtol': rtol, 'atol': atol}


def evaluate_cosine(coefficients, x):
    return product(coefficients, np.cos(np.arange(coefficients.shape[1])[:, None]*np.asarray(x)[None, :]))


def fd_radau_reference(config, n, budget):
    """Independent time integrator for the SAME FD semidiscretization only."""
    dx = 2*math.pi/n
    lap = diags([np.ones(n-1), -2*np.ones(n), np.ones(n-1)], [-1, 0, 1], format='lil')
    lap[0, -1] = lap[-1, 0] = 1
    lap = lap.tocsc()/(dx*dx)
    d0, d1 = config['diffusion']
    a, b = config['a'], config['b']
    def rhs(t, vector):
        budget.check()
        u, v = vector[:n], vector[n:]
        rate = u*u*v
        return np.concatenate([d0*(lap@u)+a-u+rate, d1*(lap@v)+b-rate])
    def jac(t, vector):
        budget.check()
        u, v = vector[:n], vector[n:]
        return bmat([[d0*lap+diags(-1+2*u*v), diags(u*u)],
                     [diags(-2*u*v), d1*lap-diags(u*u)]], format='csc')
    initial = initial_field(config, np.arange(n)*dx)
    sol = solve_ivp(rhs, [0, config['time']], initial.ravel(), method='Radau', jac=jac,
                    t_eval=config['snapshot_times'], rtol=config['tight_rtol'], atol=config['tight_atol'])
    if not sol.success or sol.t[-1] != config['time']:
        raise RuntimeError('FD Radau time reference failed: '+sol.message)
    return {float(t): y.reshape(2, n) for t, y in zip(sol.t, sol.y.T)}


def norms(error):
    # Per-component normalized periodic Lp; worst component is the scalar summary.
    return {'l1': float(np.max(np.mean(np.abs(error), axis=-1))),
            'l2': float(np.max(np.sqrt(np.mean(error*error, axis=-1)))) ,
            'linf': float(np.max(np.abs(error)))}


def orders(rows, scale):
    return {name: [math.log(rows[i][name]/rows[i+1][name])/math.log(rows[i+1][scale]/rows[i][scale])
                   for i in range(len(rows)-1)] for name in ['l1', 'l2', 'linf']}


def observables(field):
    spectrum = 2*np.abs(np.fft.rfft(field[0]))/field.shape[1]
    spectrum[0] = 0
    # k=4 is already seeded; only initially absent k>=5 count as generated modes.
    higher = math.sqrt(float(np.sum(spectrum[5:]**2)))
    return {'mean_u': float(field[0].mean()), 'mean_v': float(field[1].mean()),
            'amplitude_u': float(np.ptp(field[0])/2), 'dominant_mode_u': int(np.argmax(spectrum)),
            'mode2_amplitude_u': float(spectrum[2]),
            'higher_harmonic_ratio': higher/max(float(spectrum[2]), 1e-300)}


def linearized_field(config, x, time):
    fixed = np.array([config['a']+config['b'], config['b']/(config['a']+config['b'])**2])
    u, v = fixed
    jac = np.array([[-1+2*u*v, u*u], [-2*u*v, -u*u]])
    coefficients = np.array(config['initial_cosine_coefficients'], float)
    coefficients[:, 0] -= fixed
    for k in range(5):
        coefficients[:, k] = np.einsum('ij,j->i', expm((jac-np.diag(np.asarray(config['diffusion'])*k*k))*time), coefficients[:, k])
    return fixed[:, None]+evaluate_cosine(coefficients, x)


def run_case(name, config, budget=None):
    validate(config)
    budget = budget or Budget()
    started = time.perf_counter()
    final = config['time']
    x = np.arange(config['diagnostic_grid'])*2*math.pi/config['diagnostic_grid']
    records, references = [], []
    reference_fields = []
    for modes in config['reference_modes']:
        snapshots, info = galerkin_reference(config, modes, config['reference_rtol'], config['reference_atol'], budget)
        references.append((snapshots, info))
        reference_fields.append(evaluate_cosine(snapshots[final], x))
    tight, tight_info = galerkin_reference(config, config['reference_modes'][-1], config['tight_rtol'], config['tight_atol'], budget)
    finest = evaluate_cosine(tight[final], x)
    spatial_sensitivity = norms(reference_fields[-1]-reference_fields[-2])
    tolerance_sensitivity = norms(finest-reference_fields[-1])
    for index, (_, info) in enumerate(references):
        records.append({'series': 'reference-refinement', **info,
                        **{'error_'+k: v for k, v in norms(reference_fields[index]-finest).items()}})
    records.append({'series': 'reference-tolerance', **tight_info,
                    **{'error_'+k: v for k, v in tolerance_sensitivity.items()}})
    # The FD/Radau result isolates temporal error, and is not a spatial reference.
    fd_references = {n: fd_radau_reference(config, n, budget) for n in sorted(set(config['grids']+[config['temporal_grid']]))}
    space_rows, time_rows, primary_solutions, diagnostics = [], [], [], []
    for n in config['grids']:
        snapshots, diagnostic = fd_split(config, n, config['space_step'], budget)
        local_x = np.arange(n)*2*math.pi/n
        exact = evaluate_cosine(tight[final], local_x)
        errors = norms(snapshots[final]-exact)
        temporal = norms(snapshots[final]-fd_references[n][final])
        spatial = norms(fd_references[n][final]-exact)
        row = {'series': 'space', 'n': n, 'dt': config['space_step'], **errors,
               **{'temporal_'+k: v for k, v in temporal.items()},
               **{'semidiscrete_spatial_'+k: v for k, v in spatial.items()}}
        space_rows.append(row);records.append(row)
        primary_solutions.append(snapshots);diagnostics.append(diagnostic)
    n = config['temporal_grid']
    for step in config['time_steps']:
        snapshots, diagnostic = fd_split(config, n, step, budget)
        row = {'series': 'time', 'n': n, 'dt': step, 'inverse_dt': 1/step,
               **norms(snapshots[final]-fd_references[n][final])}
        time_rows.append(row);records.append(row);diagnostics.append(diagnostic)
    spatial_orders, temporal_orders = orders(space_rows, 'n'), orders(time_rows, 'inverse_dt')
    best = primary_solutions[-1]
    finest_n = config['grids'][-1]
    best_x = np.arange(finest_n)*2*math.pi/finest_n
    stored_snapshots = []
    for t in config['snapshot_times']:
        ref_field = evaluate_cosine(tight[t], best_x)
        obs = observables(best[t])
        records.append({'series': 'evolution', 'time': t, **obs,
                        **{'reference_'+k: v for k, v in observables(ref_field).items()},
                        **{'error_'+k: v for k, v in norms(best[t]-ref_field).items()}})
        stored_snapshots.append({'time': t, 'x': best_x.tolist(), 'u': best[t][0].tolist(), 'v': best[t][1].tolist(),
                                 'reference_u': ref_field[0].tolist(), 'reference_v': ref_field[1].tolist()})
        if t == final:
            stride = max(1, finest_n//64)
            for xi, ui, vi, ru, rv in zip(best_x[::stride], *best[t][:, ::stride], *ref_field[:, ::stride]):
                records.append({'series': 'profile', 'time': t, 'x': float(xi), 'u': float(ui), 'v': float(vi),
                                'reference_u': float(ru), 'reference_v': float(rv)})
    obs = observables(finest)
    fixed = np.array([config['a']+config['b'], config['b']/(config['a']+config['b'])**2])
    nonlinear_delta = norms(finest-linearized_field(config, x, final))['l2']
    nonlinear_scale = norms(finest-fixed[:, None])['l2']
    metrics = {'spatial_finest_linf': space_rows[-1]['linf'],
               'temporal_finest_linf': time_rows[-1]['linf'],
               'minimum_spatial_order': min(min(v) for v in spatial_orders.values()),
               'minimum_temporal_order': min(min(v) for v in temporal_orders.values()),
               'reference_spatial_linf': spatial_sensitivity['linf'],
               'reference_tolerance_linf': tolerance_sensitivity['linf'],
               'reference_to_primary_error_ratio': (spatial_sensitivity['linf']+tolerance_sensitivity['linf'])/space_rows[-1]['linf'],
               'temporal_contamination_ratio': max(r['temporal_linf']/r['semidiscrete_spatial_linf'] for r in space_rows),
               'minimum_concentration': min(d['minimum_concentration'] for d in diagnostics),
               'minimum_newton_iterate': min(d['minimum_newton_iterate'] for d in diagnostics),
               'maximum_midpoint_residual': max(d['maximum_midpoint_residual'] for d in diagnostics),
               'maximum_reaction_balance_error': max(d['maximum_reaction_balance_error'] for d in diagnostics),
               'maximum_newton_iterations': max(d['maximum_newton_iterations'] for d in diagnostics),
               'nonlinear_relative_difference': nonlinear_delta/max(nonlinear_scale, 1e-300),
               'pattern_amplitude': obs['amplitude_u'], 'higher_harmonic_ratio': obs['higher_harmonic_ratio'],
               'dominant_mode_u': obs['dominant_mode_u'], 'mean_u': obs['mean_u'], 'mean_v': obs['mean_v']}
    accept = config['acceptance']
    checks = {key: metrics[key] <= accept[key] for key in [
        'spatial_finest_linf', 'temporal_finest_linf', 'reference_spatial_linf', 'reference_tolerance_linf',
        'reference_to_primary_error_ratio', 'temporal_contamination_ratio', 'maximum_midpoint_residual', 'maximum_reaction_balance_error']}
    for key in ['minimum_spatial_order', 'minimum_temporal_order']:
        checks[key] = metrics[key] >= accept[key]
    checks['positive_without_clipping'] = metrics['minimum_concentration'] > accept['minimum_concentration']
    for key in ['nonlinear_relative_difference', 'pattern_amplitude', 'higher_harmonic_ratio']:
        checks[key] = metrics[key] >= accept['minimum_'+key]
    if name == 'schnakenberg-pattern':
        start = accept['saturation_start_time']
        before = evaluate_cosine(tight[start], x)
        system = CosineGalerkin(config['reference_modes'][-1], config, budget)
        rhs_coeff = system.rhs(final, tight[final].ravel()).reshape(tight[final].shape)
        metrics['saturation_change'] = norms(finest-before)['linf']
        second_derivative = evaluate_cosine(-np.arange(tight[final].shape[1])**2*tight[final], x)
        full_rhs = np.asarray(config['diffusion'])[:, None]*second_derivative+kinetics(finest, config['a'], config['b'])
        metrics['saturation_rhs'] = float(np.max(np.abs(full_rhs)))
        metrics['saturation_projected_rhs'] = float(np.max(np.abs(evaluate_cosine(rhs_coeff, x))))
        metrics['saturation_fd_rhs'] = float(np.max(np.abs(np.asarray(config['diffusion'])[:, None]*
            periodic_laplacian(best[final], 2*math.pi/finest_n)+kinetics(best[final], config['a'], config['b']))))
        metrics['saturation_amplitude_change'] = abs(obs['amplitude_u']-observables(before)['amplitude_u'])
        for key in ['saturation_change', 'saturation_rhs', 'saturation_amplitude_change']:
            checks[key] = metrics[key] <= accept['maximum_'+key]
    budget.check()
    return {'id': name, 'passed': all(checks.values()), 'checks': checks, 'metrics': metrics,
            'spatial_orders': spatial_orders, 'temporal_orders': temporal_orders,
            'reference': {'method': 'real cosine Fourier-Galerkin / SciPy Radau, analytic Jacobian',
                          'product_rule': 'M=4(K+1)>4K, exact retained cubic projection',
                          'scope': 'Reflection-even, pi-periodic IC; fixed-origin raw-field comparison; no phase alignment.',
                          'tight': tight_info},
            'snapshots': stored_snapshots, 'records': records, 'duration_seconds': time.perf_counter()-started}


RUNNERS = {name: (lambda config, budget=None, name=name: run_case(name, config, budget))
           for name in ['schnakenberg-nonlinear', 'schnakenberg-pattern']}
