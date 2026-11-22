"""Matched Lie/Strang splitting for one bounded 1D Schnakenberg FD problem.

The local midpoint/Newton formulas are adapted from the atlas's older biology
supplement; that immutable release is retained. See source-provenance.json.
"""
import math
import time
import numpy as np
import reference

CASE_ID = 'reaction-diffusion-splitting'
METHODS = ('lie-trotter', 'strang')


class Budget:
    def __init__(self, seconds=60):
        if not math.isfinite(seconds) or not 0 < seconds <= 60:
            raise ValueError('Require a positive budget of at most 60 seconds')
        self.deadline = time.perf_counter() + seconds

    def check(self):
        if time.perf_counter() > self.deadline:
            raise RuntimeError('Fixed calculation budget exhausted')


def validate(config):
    def finite(value):
        if type(value) not in (float, int) or not math.isfinite(value):
            raise ValueError('Finite real parameter required')
    for key in ['length', 'a', 'b', 'time', 'newton_tolerance', 'reference_rtol',
                'reference_atol', 'tight_rtol', 'tight_atol', 'dop853_rtol', 'dop853_atol']:
        finite(config[key])
        if config[key] <= 0:
            raise ValueError('Positive parameter required: ' + key)
    if not math.isclose(config['length'], 2*math.pi) or config['time'] > 2:
        raise ValueError('This bounded example uses a 2pi cell and T<=2')
    n = config['grid']
    if type(n) is not int or n % 2 or not 16 <= n <= 64:
        raise ValueError('Require an even grid between 16 and 64')
    steps = config['step_counts']
    if len(steps) != 4 or any(type(v) is not int or not 8 <= v <= 512 for v in steps) or any(b != 2*a for a, b in zip(steps, steps[1:])):
        raise ValueError('Require four bounded dyadic step counts')
    times = config['snapshot_times']
    if len(times) != 5 or times != sorted(set(times)) or times[0] != 0 or times[-1] != config['time']:
        raise ValueError('Require five ordered observations including both endpoints')
    for value in times:
        finite(value)
        if any(not math.isclose(value/config['time']*count, round(value/config['time']*count), abs_tol=1e-12) for count in steps):
            raise ValueError('Every observation must lie on every fixed time grid')
    if type(config['newton_iterations']) is not int or not 1 <= config['newton_iterations'] <= 12:
        raise ValueError('Invalid Newton iteration cap')
    d = np.asarray(config['diffusion'], dtype=float)
    coefficients = np.asarray(config['initial_cosine_coefficients'], dtype=float)
    if d.shape != (2,) or not np.isfinite(d).all() or np.any(d <= 0) or coefficients.shape != (2, 5) or not np.isfinite(coefficients).all():
        raise ValueError('Invalid diffusivities or initial coefficients')
    if config['tight_rtol'] >= config['reference_rtol'] or config['tight_atol'] >= config['reference_atol']:
        raise ValueError('The refined reference must use tighter tolerances')
    for value in config['acceptance'].values():
        finite(value)
        if value < 0:
            raise ValueError('Acceptance bounds must be nonnegative')


def initial_field(config):
    x = np.arange(config['grid']) * config['length'] / config['grid']
    basis = np.cos(2*math.pi*np.arange(5)[:, None]*x[None, :]/config['length'])
    return np.einsum('sk,kj->sj', np.asarray(config['initial_cosine_coefficients']), basis, optimize=False)


def kinetics(field, a, b):
    u, v = field
    rate = u*u*v
    return np.array([a-u+rate, b-rate])


def diffuse(field, h, config):
    """Exact periodic FD2 heat semigroup, NOT continuum spectral diffusion."""
    n = config['grid']
    eigenvalues = -4*np.sin(math.pi*np.arange(n//2+1)/n)**2/(config['length']/n)**2
    multiplier = np.exp(h*np.asarray(config['diffusion'])[:, None]*eigenvalues)
    return np.fft.irfft(np.fft.rfft(field)*multiplier, n=n)


def midpoint(field, h, config):
    new = field.copy()
    for iteration in range(config['newton_iterations']):
        mid = (field+new)/2
        residual = new-field-h*kinetics(mid, config['a'], config['b'])
        error = float(np.max(np.abs(residual)))
        if not np.isfinite(new).all() or np.max(np.abs(new)) > 1e6:
            raise RuntimeError('Nonfinite or unbounded reaction iterate')
        if error <= config['newton_tolerance']:
            return new, mid, error, iteration
        u, v = mid
        aa, bb = 1+h/2-h*u*v, -h*u*u/2
        cc, dd = h*u*v, 1+h*u*u/2
        det = aa*dd-bb*cc
        if np.any(np.abs(det) < 1e-12):
            raise RuntimeError('Singular reaction Newton matrix')
        new -= np.array([(dd*residual[0]-bb*residual[1])/det,
                         (aa*residual[1]-cc*residual[0])/det])
    raise RuntimeError('Reaction Newton did not converge within its fixed cap')


def compose(field, h, diffusion, reaction, method):
    """Apply subflows to UPDATED states; the original problem advances by h."""
    if method == 'lie-trotter':
        return reaction(diffusion(field, h), h)
    if method == 'strang':
        return diffusion(reaction(diffusion(field, h/2), h), h/2)
    if method == 'lie-reversed':
        return diffusion(reaction(field, h), h)
    raise ValueError('Unknown composition')


def integrate(config, steps, method, budget):
    h = config['time']/steps
    field = initial_field(config)
    initial_total = float(np.mean(field.sum(axis=0)))
    source_integral = 0.0
    info = {'minimum_concentration': float(field.min()), 'maximum_midpoint_residual': 0.0,
            'maximum_reaction_balance_error': 0.0, 'reaction_calls': 0,
            'diffusion_calls': 0, 'newton_updates': 0}

    def observe(value):
        if not np.isfinite(value).all():
            raise RuntimeError('Nonfinite substep')
        info['minimum_concentration'] = min(info['minimum_concentration'], float(value.min()))
        return value

    def diffusion(value, step):
        info['diffusion_calls'] += 1
        return observe(diffuse(value, step, config))

    def reaction(value, step):
        nonlocal source_integral
        new, mid, residual, updates = midpoint(value, step, config)
        source_integral += step*(config['a']+config['b']-float(mid[0].mean()))
        info['reaction_calls'] += 1
        info['newton_updates'] += updates
        info['maximum_midpoint_residual'] = max(info['maximum_midpoint_residual'], residual)
        return observe(new)

    snapshots = [field.copy()]
    wanted = {round(t/h) for t in config['snapshot_times'][1:]}
    for index in range(1, steps+1):
        if index % 8 == 1:
            budget.check()
        field = compose(field, h, diffusion, reaction, method)
        balance = abs(float(np.mean(field.sum(axis=0)))-initial_total-source_integral)
        info['maximum_reaction_balance_error'] = max(info['maximum_reaction_balance_error'], balance)
        if index in wanted:
            snapshots.append(field.copy())
    return np.asarray(snapshots), info


def norms(error):
    # Same definition as the earlier biology release: worst species.
    return {'l1': float(np.mean(np.abs(error), axis=-1).max()),
            'l2': float(np.sqrt(np.mean(error**2, axis=-1)).max()),
            'linf': float(np.abs(error).max())}


def run_case(config, budget):
    validate(config)
    primary, primary_info = reference.solve(config, budget, 'Radau', config['reference_rtol'], config['reference_atol'])
    tighter, tighter_info = reference.solve(config, budget, 'Radau', config['tight_rtol'], config['tight_atol'])
    dop853, dop_info = reference.solve(config, budget, 'DOP853', config['dop853_rtol'], config['dop853_atol'])
    reference_tolerance = norms(primary-tighter)['linf']
    reference_algorithm = norms(primary-dop853)['linf']
    rows, time_rows, profiles = [], [], {}
    previous = {}
    for method in METHODS:
        profiles[method] = {}
        for count in config['step_counts']:
            states, info = integrate(config, count, method, budget)
            errors = [norms(state-ref) for state, ref in zip(states, primary)]
            row = {'method': method, 'steps': count, 'dt': config['time']/count,
                   **{'max_'+name: max(error[name] for error in errors[1:]) for name in ['l1', 'l2', 'linf']}, **info}
            if method in previous:
                row['observed_order_l2'] = math.log2(previous[method]/row['max_l2'])
            previous[method] = row['max_l2']
            rows.append(row)
            time_rows.extend({'method': method, 'steps': count, 'time': t, **error}
                             for t, error in zip(config['snapshot_times'], errors))
            profiles[method][str(count)] = states[-1].tolist()
    by_method = {method: [r for r in rows if r['method'] == method] for method in METHODS}
    lie, strang = by_method['lie-trotter'], by_method['strang']
    smallest = config['step_counts'][-1]
    refined_config = {**config, 'newton_tolerance': config['newton_tolerance']/10}
    refined, _ = integrate(refined_config, smallest, 'strang', budget)
    normal, _ = integrate(config, smallest, 'strang', budget)
    newton_sensitivity = norms(refined-normal)['linf']
    reverse, _ = integrate(config, config['step_counts'][0], 'lie-reversed', budget)
    forward, _ = integrate(config, config['step_counts'][0], 'lie-trotter', budget)
    reverse_gap = norms(forward-reverse)['l2']
    bound = config['acceptance']
    finest_lie, finest_strang = lie[-1]['max_l2'], strang[-1]['max_l2']
    checks = {
        'lie_error_decreases': all(b['max_l2'] < a['max_l2'] for a, b in zip(lie, lie[1:])),
        'strang_error_decreases': all(b['max_l2'] < a['max_l2'] for a, b in zip(strang, strang[1:])),
        'lie_first_order': all(bound['lie_order_min'] <= r['observed_order_l2'] <= bound['lie_order_max'] for r in lie[1:]),
        'strang_second_order': all(bound['strang_order_min'] <= r['observed_order_l2'] <= bound['strang_order_max'] for r in strang[1:]),
        'lie_finest_error': finest_lie <= bound['lie_finest_l2_max'],
        'strang_finest_error': finest_strang <= bound['strang_finest_l2_max'],
        'strang_improves_this_input': finest_strang/finest_lie <= bound['strang_to_lie_error_ratio_max'],
        'reference_tolerance': reference_tolerance <= bound['reference_difference_max'],
        'reference_independent_time_algorithm': reference_algorithm <= bound['reference_difference_max'],
        'reference_error_separated': max(reference_tolerance, reference_algorithm)/finest_strang <= bound['reference_to_strang_error_ratio_max'],
        'newton_error_separated': newton_sensitivity/finest_strang <= bound['newton_sensitivity_to_error_ratio_max'],
        'reaction_converged': max(r['maximum_midpoint_residual'] for r in rows) <= bound['midpoint_residual_max'],
        'reaction_source_balance': max(r['maximum_reaction_balance_error'] for r in rows) <= bound['reaction_balance_max'],
        'positive_on_tested_substeps': min(r['minimum_concentration'] for r in rows) > bound['concentration_min'],
        'noncommuting_order_control': reverse_gap >= bound['reverse_order_difference_min'],
    }
    metrics = {'grid': config['grid'], 'final_time': config['time'],
               'lie_finest_l2': finest_lie, 'strang_finest_l2': finest_strang,
               'lie_last_observed_order': lie[-1]['observed_order_l2'],
               'strang_last_observed_order': strang[-1]['observed_order_l2'],
               'reference_tolerance_linf': reference_tolerance,
               'reference_algorithm_linf': reference_algorithm,
               'reference_to_strang_error_ratio': max(reference_tolerance, reference_algorithm)/finest_strang,
               'newton_sensitivity_linf': newton_sensitivity, 'reverse_order_l2_difference': reverse_gap,
               'minimum_concentration': min(r['minimum_concentration'] for r in rows),
               'maximum_reaction_balance_error': max(r['maximum_reaction_balance_error'] for r in rows)}
    reference_rows = [{**info, 'difference_from_primary_linf': difference}
                      for info, difference in [(primary_info, 0.0), (tighter_info, reference_tolerance), (dop_info, reference_algorithm)]]
    return {'id': CASE_ID, 'passed': all(checks.values()), 'metrics': metrics,
            'checks': checks, 'records': rows, 'time_records': time_rows,
            'reference_records': reference_rows,
            'reference_scope': 'Unsplit Radau and DOP853 integration of the SAME centered-FD semidiscrete equations. No continuum-PDE or spatial convergence validation.',
            'profiles': {'x': (np.arange(config['grid'])*config['length']/config['grid']).tolist(),
                         'initial': initial_field(config).tolist(), 'reference_final': primary[-1].tolist(),
                         'computed_final': profiles}}
