"""Original small CSVR/local-Langevin implementations and fixed-input experiments.

Unit masses and k_B=1 are used by MD cases. The bath kernel accepts arbitrary
positive masses. Primary algorithms: Bussi et al. 2007 Appendix A and Bussi &
Parrinello 2008 Eqs. 8--9. References are evaluated independently with SciPy.
"""
import math
import numbers
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, solve_discrete_lyapunov
from scipy.special import gammainc, ndtr
from scipy.stats import ncx2


def real(value, name, positive=False, nonnegative=False):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Real) or not math.isfinite(value):
        raise ValueError(name+' must be a finite real number')
    if positive and value <= 0 or nonnegative and value < 0:
        raise ValueError(name+' is outside its allowed range')
    return float(value)


def integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(name+' must be an integer >= '+str(minimum))
    return value


def count_steps(duration, step):
    n = int(round(duration/step))
    if n < 0 or not math.isclose(n*step, duration, rel_tol=0, abs_tol=1e-10):
        raise ValueError('Times must be nonnegative integer multiples of the timestep')
    return n


def real_sequence(value, name, minimum_length=1, maximum_length=20, positive=False):
    if not isinstance(value, list) or not minimum_length <= len(value) <= maximum_length:
        raise ValueError(name+' must be a bounded nonempty list')
    return [real(x, name, positive=positive) for x in value]


def validate_config(config, kind):
    """Reject invalid or excessive educational workloads before allocating states."""
    integer(config['seed'], 'seed', 0)
    real(config['temperature'], 'temperature', positive=True)
    for name, value in config['acceptance'].items():
        real(value, 'acceptance.'+name, positive=True)
    replicas = integer(config['replicas'], 'replicas', 1024) if kind == 'kernel' else None
    if kind == 'kernel':
        h = real(config['step'], 'step', positive=True)
        real(config['tau'], 'tau', positive=True)
        dofs = config['degrees_of_freedom']
        if not isinstance(dofs, list) or not 1 <= len(dofs) <= 8:
            raise ValueError('Bounded degree counts required')
        for dof in dofs:
            integer(dof, 'degrees_of_freedom')
            if dof > 32:
                raise ValueError('At most 32 bath degrees supported in the educational budget')
        ratios = real_sequence(config['initial_energy_ratios'], 'initial_energy_ratios', maximum_length=16, positive=True)
        lags = real_sequence(config['lag_times'], 'lag_times', maximum_length=20)
        probabilities = real_sequence(config['cdf_probabilities'], 'cdf_probabilities', maximum_length=16, positive=True)
        if any(x >= 1 for x in probabilities):
            raise ValueError('CDF probabilities must lie strictly inside (0,1)')
        work = replicas*sum(dofs)*(len(ratios)+1+count_steps(lags[-1], h))
    else:
        a = integer(config['canonical_replicas'], 'canonical_replicas', 1024)
        b = integer(config['heated_replicas'], 'heated_replicas', 1024)
        real(config['heated_scale'], 'heated_scale', positive=True)
        duration = real(config['burn_time'], 'burn_time', positive=True)
        quartic = real(config['quartic'], 'quartic', nonnegative=True)
        if kind == 'harmonic' and quartic != 0 or kind == 'quartic' and quartic <= 0:
            raise ValueError('Potential parameters do not match the named case')
        frequencies = real_sequence(config['frequencies'], 'frequencies', 2, 2, positive=True)
        steps = real_sequence(config['steps'], 'steps', 2, 8, positive=True)
        taus = real_sequence(config['tau_values'], 'tau_values', maximum_length=8, positive=True)
        lags = real_sequence(config['lag_times'], 'lag_times', maximum_length=20)
        q_points = real_sequence(config['position_cdf_points'], 'position_cdf_points', maximum_length=16)
        e_points = real_sequence(config['energy_cdf_points'], 'energy_cdf_points', maximum_length=16, positive=True)
        if any(abs(x) > 50 for x in q_points+e_points) or duration > 100:
            raise ValueError('Reference/time range exceeds the educational budget')
        if len(set(steps)) != len(steps) or steps != sorted(steps, reverse=True):
            raise ValueError('Timestep sequence must be distinct and descending')
        if any(h*max(frequencies) >= 2 for h in steps):
            raise ValueError('Harmonic Verlet stability h*omega<2 required')
        for h in steps:
            count_steps(duration, h)
            for lag in lags:
                count_steps(lag, h)
        if kind == 'harmonic':
            reference_steps = real_sequence(config['reference_steps'], 'reference_steps', 3, 8, positive=True)
            if reference_steps != sorted(set(reference_steps), reverse=True) or any(h*max(frequencies) >= 2 for h in reference_steps):
                raise ValueError('Stable, distinct descending reference timesteps required')
        replicas = a+b
        work = 4*replicas*len(taus)*sum(count_steps(duration+lags[-1], h) for h in steps)
    if replicas > 262144 or work > 200_000_000:
        raise ValueError('Requested workload exceeds the lightweight educational budget')
    if lags[0] != 0 or lags != sorted(set(lags)) or any(x < 0 for x in lags):
        raise ValueError('Lag times must be distinct increasing values beginning at zero')


def csvr_rescale(momentum, step, tau, temperature, normal, chi_square, masses=1.0):
    """Exact signed global radial bath, with a shared scalar normal per replica.

    A replica is one final-axis momentum vector. chi_square is an independent
    chi-square(Nf-1) draw, exactly zero for Nf=1. Stable unit-vector arithmetic
    avoids forming K'/K for tiny nonzero momenta. Zero total K is rejected: a
    global rescaling cannot invent a momentum direction. No COM subtraction or
    constraints are silently applied.
    """
    h = real(step, 'step', nonnegative=True)
    tau = real(tau, 'tau', positive=True)
    temperature = real(temperature, 'temperature', positive=True)
    p = np.asarray(momentum, dtype=float)
    mass = np.asarray(masses, dtype=float)
    if p.ndim < 1 or not p.shape[-1] or not np.all(np.isfinite(p)):
        raise ValueError('Finite momentum vectors with a nonempty final axis required')
    try:
        mass = np.broadcast_to(mass, (p.shape[-1],))
    except ValueError as error:
        raise ValueError('One positive mass per degree of freedom required') from error
    if not np.all(np.isfinite(mass)) or np.any(mass <= 0):
        raise ValueError('Masses must be finite and positive')
    r, s = np.asarray(normal, dtype=float), np.asarray(chi_square, dtype=float)
    try:
        r, s = np.broadcast_to(r, p.shape[:-1]), np.broadcast_to(s, p.shape[:-1])
    except ValueError as error:
        raise ValueError('Independent scalar bath draws must match replica dimensions') from error
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(s)) or np.any(s < 0):
        raise ValueError('Finite normal and nonnegative chi-square draws required')
    if p.shape[-1] == 1 and np.any(s != 0):
        raise ValueError('Nf=1 requires chi-square(0)=0 exactly')
    if h == 0:
        return p.copy()
    x = p/np.sqrt(mass)
    scale = np.max(abs(x), axis=-1)
    if np.any(scale == 0):
        raise ValueError('Zero kinetic energy has no global rescaling direction')
    reduced = x/scale[..., None]
    reduced_norm = np.sqrt(np.sum(reduced*reduced, axis=-1))
    direction = reduced/reduced_norm[..., None]
    sqrt_k = scale*(reduced_norm/math.sqrt(2.))
    one_minus_c = -math.expm1(-h/tau)
    radial = math.exp(-h/(2*tau))*sqrt_k+math.sqrt(temperature*one_minus_c/2)*r
    radius = math.sqrt(2)*np.hypot(radial, np.sqrt(temperature*one_minus_c*s/2))
    signed_radius = np.copysign(radius, radial)
    result = direction*signed_radius[..., None]*np.sqrt(mass)
    if not np.all(np.isfinite(result)):
        raise ArithmeticError('Nonfinite rescaled momentum')
    return result


def csvr_bath(momentum, step, tau, temperature, rng):
    p = np.asarray(momentum)
    if p.ndim < 1 or not p.shape[-1]:
        raise ValueError('Momentum vectors need a nonempty final axis')
    shape, dof = p.shape[:-1], p.shape[-1]
    normal = rng.normal(size=shape)
    chi_square = rng.chisquare(dof-1, size=shape) if dof > 1 else np.zeros(shape)
    return csvr_rescale(p, step, tau, temperature, normal, chi_square)


def langevin_bath(momentum, step, tau, temperature, rng):
    # gamma=1/(2*tau) matches the bath-only kinetic-energy relaxation time.
    a = math.exp(-step/(2*tau))
    return a*momentum+math.sqrt(temperature*(-math.expm1(-step/tau)))*rng.normal(size=momentum.shape)


def potential(q, frequencies, quartic):
    q2 = q*q
    return np.sum(.5*np.asarray(frequencies)**2*q2+.25*quartic*q2*q2, axis=-1)


def force(q, frequencies, quartic):
    return -np.asarray(frequencies)**2*q-quartic*q*q*q


def kinetic(p):
    return .5*np.sum(p*p, axis=-1)


def verlet_step(q, p, step, frequencies, quartic):
    p = p+.5*step*force(q, frequencies, quartic)
    q = q+step*p
    p = p+.5*step*force(q, frequencies, quartic)
    return q, p


def md_step(q, p, step, frequencies, quartic, tau, temperature, rng, method):
    if method not in ('csvr', 'langevin'):
        raise ValueError('Unknown thermostat')
    bath = csvr_bath if method == 'csvr' else langevin_bath
    p = bath(p, step/2, tau, temperature, rng)
    q, p = verlet_step(q, p, step, frequencies, quartic)
    p = bath(p, step/2, tau, temperature, rng)
    return q, p


def canonical_positions(rng, replicas, frequencies, quartic, temperature):
    """Independent canonical draws by Gaussian-envelope rejection, not MD."""
    frequencies = np.asarray(frequencies, dtype=float)
    q = rng.normal(size=(replicas, len(frequencies)))*math.sqrt(temperature)/frequencies
    if quartic == 0:
        return q
    accepted = rng.random(q.shape) < np.exp(-quartic*q*q*q*q/(4*temperature))
    while not np.all(accepted):
        indices = np.where(~accepted)
        candidates = rng.normal(size=len(indices[0]))*math.sqrt(temperature)/frequencies[indices[1]]
        q[indices] = candidates
        accepted[indices] = rng.random(len(candidates)) < np.exp(-quartic*candidates**4/(4*temperature))
    return q


def coordinate_energy(x, omega, quartic):
    return .5*omega*omega*x*x+.25*quartic*x**4


def turning_point(energy, omega, quartic):
    if energy <= 0:
        return 0.
    if quartic == 0:
        return math.sqrt(2*energy)/omega
    a = omega*omega/2
    return math.sqrt(2*energy/(a+math.sqrt(a*a+quartic*energy)))


def canonical_reference(frequencies, quartic, temperature, q_points, e_points, tolerance):
    """Independent 1D Boltzmann integrals and a bounded 2D H-CDF integral.

    Nf=2 gives K~Exp(T). Integrating its CDF over independent canonical
    positions yields the full physical-H CDF, including the quartic potential.
    """
    if len(frequencies) != 2:
        raise ValueError('The full-energy quadrature reference is explicitly two-dimensional')
    z, q_var, u_mean, u_var, position_cdf = [], [], [], [], []
    for omega in frequencies:
        weight = lambda x: math.exp(-coordinate_energy(x, omega, quartic)/temperature)
        integral = lambda fn: quad(lambda x: fn(x)*weight(x), -np.inf, np.inf,
                                  epsabs=tolerance, epsrel=tolerance, limit=200)[0]
        zi = integral(lambda x: 1.)
        mu = integral(lambda x: coordinate_energy(x, omega, quartic))/zi
        second = integral(lambda x: coordinate_energy(x, omega, quartic)**2)/zi
        z.append(zi);q_var.append(integral(lambda x: x*x)/zi)
        u_mean.append(mu);u_var.append(second-mu*mu)
        position_cdf.append([quad(weight, -np.inf, x, epsabs=tolerance, epsrel=tolerance,
                                  limit=200)[0]/zi for x in q_points])
    energy_cdf = []
    for energy in e_points:
        if quartic == 0:
            energy_cdf.append(float(gammainc(2, energy/temperature)))
            continue
        xmax = turning_point(energy, frequencies[0], quartic)
        def outer(x):
            ux = coordinate_energy(x, frequencies[0], quartic)
            ymax = turning_point(max(0., energy-ux), frequencies[1], quartic)
            def inner(y):
                u = ux+coordinate_energy(y, frequencies[1], quartic)
                return math.exp(-u/temperature)*(-math.expm1(-max(0., energy-u)/temperature))
            return quad(inner, 0, ymax, epsabs=tolerance, epsrel=tolerance, limit=150)[0]
        value = 4*quad(outer, 0, xmax, epsabs=tolerance, epsrel=tolerance, limit=150)[0]/(z[0]*z[1])
        energy_cdf.append(value)
    return {'normalizers': z, 'q_variance': q_var, 'u_mean': float(sum(u_mean)),
            'u_variance': float(sum(u_var)), 'k_mean': temperature,
            'k_variance': temperature**2, 'h_mean': temperature+sum(u_mean),
            'h_variance': temperature**2+sum(u_var), 'position_cdf': position_cdf,
            'energy_cdf': energy_cdf}


def harmonic_langevin_reference(step, tau, frequencies, temperature, lag):
    """Independent affine-map Lyapunov covariance and full covariance lag."""
    a = math.exp(-step/(4*tau))
    o = np.diag([1., a]);noise = np.diag([0., temperature*(1-a*a)])
    covariances, lags, continuous = [], [], []
    for omega in frequencies:
        vv = np.array([[1-step*step*omega*omega/2, step],
                       [-step*omega*omega*(1-step*step*omega*omega/4), 1-step*step*omega*omega/2]])
        matrix = o@vv@o
        q = o@vv@noise@vv.T@o+noise
        covariance = solve_discrete_lyapunov(matrix, q)
        covariances.append(covariance)
        lags.append(np.linalg.matrix_power(matrix, count_steps(lag, step))@covariance)
        generator = np.array([[0., 1.], [-omega*omega, -1/(2*tau)]])
        continuous.append(expm(generator*lag)@np.diag([temperature/omega**2, temperature]))
    q_corr = np.mean([c[0, 0]/(temperature/w**2) for c, w in zip(lags, frequencies)])
    p_corr = np.mean([c[1, 1]/temperature for c in lags])
    k_cov = .5*sum(c[1, 1]**2 for c in lags)
    h_cov = .5*sum(np.trace(np.diag([w*w, 1.])@c@np.diag([w*w, 1.])@c.T)
                   for c, w in zip(lags, frequencies))
    mean_h = .5*sum(np.trace(np.diag([w*w, 1.])@c) for c, w in zip(covariances, frequencies))
    h_mean_shift = mean_h-len(frequencies)*temperature
    return {'covariance': np.array(covariances), 'q_acf': float(q_corr), 'p_acf': float(p_corr),
            'k_acf': float(k_cov/(len(frequencies)*temperature**2/2)),
            'h_acf': float((h_cov+h_mean_shift*h_mean_shift)/(len(frequencies)*temperature**2)),
            'q_acf_continuum': float(np.mean([c[0, 0]/(temperature/w**2) for c, w in zip(continuous, frequencies)]))}


def result(ident, checks, metrics, records, **extra):
    return {'id': ident, 'passed': all(checks.values()), 'checks': {k: bool(v) for k, v in checks.items()},
            'metrics': {k: float(v) for k, v in metrics.items()}, 'records': records, **extra}


def kinetic_case(config):
    validate_config(config, 'kernel')
    temperature = real(config['temperature'], 'temperature', positive=True)
    tau = real(config['tau'], 'tau', positive=True);step = real(config['step'], 'step', positive=True)
    replicas = integer(config['replicas'], 'replicas', 1024)
    rng = np.random.default_rng(config['seed']);records = []
    mean_z, var_error, cdf_error = [], [], []
    stationary_mean, stationary_variance, acf_error = [], [], []
    for dof in config['degrees_of_freedom']:
        integer(dof, 'degrees_of_freedom')
        target_mean, target_var = dof*temperature/2, dof*temperature**2/2
        c = math.exp(-step/tau);scale = temperature*(1-c)/2
        for ratio in config['initial_energy_ratios']:
            k0 = real(ratio, 'initial_energy_ratio', positive=True)*target_mean
            p = np.zeros((replicas, dof));p[:, 0] = math.sqrt(2*k0)
            evolved = kinetic(csvr_bath(p, step, tau, temperature, rng))
            exact_mean = c*k0+(1-c)*target_mean
            exact_var = 2*temperature*k0*c*(1-c)+target_var*(1-c)**2
            z = abs(evolved.mean()-exact_mean)/math.sqrt(exact_var/replicas)
            relative_var = abs(evolved.var()-exact_var)/exact_var
            thresholds = scale*ncx2.ppf(config['cdf_probabilities'], dof, c*k0/scale)
            error = float(np.max(abs(np.mean(evolved[:, None] <= thresholds, axis=0)-config['cdf_probabilities'])))
            mean_z.append(z);var_error.append(relative_var);cdf_error.append(error)
            records.append({'series': 'conditional', 'dof': dof, 'initial_energy_ratio': ratio,
                            'sample_mean': float(evolved.mean()), 'exact_mean': exact_mean,
                            'sample_variance': float(evolved.var()), 'exact_variance': exact_var,
                            'mean_z': float(z), 'variance_relative_error': float(relative_var),
                            'noncentral_chi_square_cdf_error': error})
        p = rng.normal(size=(replicas, dof))*math.sqrt(temperature)
        initial = kinetic(p);p0 = p.copy()
        for lag in config['lag_times']:
            if lag:
                previous = config['lag_times'][config['lag_times'].index(lag)-1]
                for _ in range(count_steps(lag-previous, step)):
                    p = csvr_bath(p, step, tau, temperature, rng)
            k = kinetic(p)
            covariance = (initial-target_mean)*(k-target_mean)/target_var
            measured = float(covariance.mean());se = float(covariance.std(ddof=1)/math.sqrt(replicas))
            exact_acf = math.exp(-lag/tau)
            acf_error.append(abs(measured-exact_acf))
            stationary_mean.append(abs(k.mean()-target_mean)/target_mean)
            stationary_variance.append(abs(k.var()-target_var)/target_var)
            thresholds = np.array([.25, 1., 2., 4.])*target_mean
            gamma_error = float(np.max(abs(np.mean(k[:, None] <= thresholds, axis=0)-gammainc(dof/2, thresholds/temperature))))
            cdf_error.append(gamma_error)
            records.append({'series': 'stationary-acf', 'dof': dof, 'lag': lag, 'measured_acf': measured,
                            'acf_standard_error': se, 'exact_acf': exact_acf,
                            'sample_mean': float(k.mean()), 'exact_mean': target_mean,
                            'sample_variance': float(k.var()), 'exact_variance': target_var,
                            'temperature_variance': float((2*k/dof).var()),
                            'exact_temperature_variance': 2*temperature**2/dof,
                            'gamma_cdf_error': gamma_error})
    # A noiseless contraction reaches the correct mean while killing the variance.
    control = target_mean+(kinetic(p0)-target_mean)*math.exp(-10)
    control_ratio = float(control.var()/target_var)
    metrics = {'maximum_conditional_mean_z': max(mean_z), 'maximum_conditional_variance_relative_error': max(var_error),
               'maximum_cdf_error': max(cdf_error), 'maximum_stationary_mean_relative_error': max(stationary_mean),
               'maximum_stationary_variance_relative_error': max(stationary_variance),
               'maximum_kinetic_acf_error': max(acf_error), 'noiseless_variance_fraction': control_ratio}
    a = config['acceptance'];checks = {
        'conditional_mean': metrics['maximum_conditional_mean_z'] <= a['conditional_mean_z'],
        'conditional_variance': metrics['maximum_conditional_variance_relative_error'] <= a['conditional_variance_relative_error'],
        'transition_and_stationary_cdf': metrics['maximum_cdf_error'] <= a['cdf_max_error'],
        'stationary_mean': metrics['maximum_stationary_mean_relative_error'] <= a['stationary_mean_relative_error'],
        'stationary_fluctuations': metrics['maximum_stationary_variance_relative_error'] <= a['stationary_variance_relative_error'],
        'kinetic_correlation': metrics['maximum_kinetic_acf_error'] <= a['kinetic_acf_error'],
        'noiseless_control_loses_fluctuations': control_ratio <= a['noiseless_variance_fraction']}
    return result('csvr-kinetic-kernel', checks, metrics, records)


def ensemble_statistics(q, p, config, reference):
    temperature = config['temperature'];q_points = np.array(config['position_cdf_points'])
    k = kinetic(p);u = potential(q, config['frequencies'], config['quartic']);h = k+u
    q_cdf = np.mean(q[:, :, None] <= q_points, axis=0)
    p_cdf = np.mean(p[:, :, None] <= q_points*math.sqrt(temperature), axis=0)
    k_points = np.array(config['energy_cdf_points'])*temperature
    # Same energy thresholds are used for kinetic and physical total energy.
    k_cdf = np.mean(k[:, None] <= k_points, axis=0)
    h_cdf = np.mean(h[:, None] <= k_points, axis=0)
    errors = {'position_cdf_error': float(np.max(abs(q_cdf-np.array(reference['position_cdf'])))),
              'momentum_cdf_error': float(np.max(abs(p_cdf-ndtr(q_points)))),
              'kinetic_cdf_error': float(np.max(abs(k_cdf-gammainc(1., k_points/temperature)))),
              'total_energy_cdf_error': float(np.max(abs(h_cdf-reference['energy_cdf'])))}
    for name, values in [('k', k), ('u', u), ('h', h)]:
        errors[name+'_mean_relative_error'] = abs(float(values.mean())-reference[name+'_mean'])/reference[name+'_mean']
        errors[name+'_variance_relative_error'] = abs(float(values.var())-reference[name+'_variance'])/reference[name+'_variance']
    return {**errors, 'temperature_mean': float(k.mean()), 'temperature_variance': float(k.var()),
            'exact_temperature_mean': temperature, 'exact_temperature_variance': temperature**2,
            'q_cdf': q_cdf.tolist(), 'p_cdf': p_cdf.tolist(), 'k_cdf': k_cdf.tolist(), 'h_cdf': h_cdf.tolist(),
            'q_variance': (q*q).mean(axis=0).tolist(), 'p_variance': (p*p).mean(axis=0).tolist(),
            'energy_means': {'kinetic': float(k.mean()), 'potential': float(u.mean()), 'total': float(h.mean())},
            'energy_variances': {'kinetic': float(k.var()), 'potential': float(u.var()), 'total': float(h.var())}}


def comparison_case(config):
    validate_config(config, 'harmonic' if config['quartic'] == 0 else 'quartic')
    temp = real(config['temperature'], 'temperature', positive=True)
    quartic = real(config['quartic'], 'quartic', nonnegative=True)
    frequencies = np.array(config['frequencies'], dtype=float)
    if frequencies.shape != (2,) or not np.all(np.isfinite(frequencies)) or np.any(frequencies <= 0):
        raise ValueError('Exactly two finite positive frequencies required')
    canonical_n = integer(config['canonical_replicas'], 'canonical_replicas', 1024)
    heated_n = integer(config['heated_replicas'], 'heated_replicas', 1024)
    points = np.array(config['position_cdf_points']);energies = np.array(config['energy_cdf_points'])*temp
    reference = canonical_reference(frequencies, quartic, temp, points, energies, 2e-10)
    refined = canonical_reference(frequencies, quartic, temp, points, energies, 2e-12)
    ref_error = max(float(np.max(abs(np.array(reference[k])-np.array(refined[k])))) for k in reference)
    reference = refined
    records = [];worst = {'canonical_cdf': 0., 'canonical_mean': 0., 'canonical_variance': 0.,
                          'heated_cdf': 0., 'heated_mean': 0., 'heated_variance': 0.,
                          'acf_standard_error': 0., 'langevin_acf_absolute_error': 0., 'langevin_acf_z': 0.}
    record_index = 0
    for tau in config['tau_values']:
        real(tau, 'tau', positive=True)
        for step in config['steps']:
            real(step, 'step', positive=True)
            if step*frequencies.max() >= 2:
                raise ValueError('Harmonic Verlet stability h*omega<2 required')
            for method in ['csvr', 'langevin']:
                rng = np.random.default_rng(np.random.SeedSequence([config['seed'], record_index]))
                record_index += 1
                n = canonical_n+heated_n
                q = canonical_positions(rng, n, frequencies, quartic, temp)
                p = rng.normal(size=q.shape)*math.sqrt(temp)
                q[canonical_n:] *= config['heated_scale'];p[canonical_n:] *= config['heated_scale']
                for _ in range(count_steps(config['burn_time'], step)):
                    q, p = md_step(q, p, step, frequencies, quartic, tau, temp, rng, method)
                for label, selection in [('canonical', slice(0, canonical_n)), ('heated', slice(canonical_n, None))]:
                    stats = ensemble_statistics(q[selection], p[selection], config, reference)
                    worst[label+'_cdf'] = max(worst[label+'_cdf'], max(stats[k] for k in stats if k.endswith('_cdf_error')))
                    worst[label+'_mean'] = max(worst[label+'_mean'], max(stats[k] for k in stats if k.endswith('_mean_relative_error')))
                    worst[label+'_variance'] = max(worst[label+'_variance'], max(stats[k] for k in stats if k.endswith('_variance_relative_error')))
                    records.append({'series': 'distribution', 'method': method, 'tau': tau, 'gamma_langevin': 1/(2*tau),
                                    'dt': step, 'initial_ensemble': label, 'replicas': len(q[selection]), **stats})
                q = q[:canonical_n].copy();p = p[:canonical_n].copy()
                q0, p0 = q.copy(), p.copy();k0 = kinetic(p0)
                h0 = k0+potential(q0, frequencies, quartic)
                previous = 0.
                for lag in config['lag_times']:
                    for _ in range(count_steps(lag-previous, step)):
                        q, p = md_step(q, p, step, frequencies, quartic, tau, temp, rng, method)
                    previous = lag
                    k = kinetic(p);h = k+potential(q, frequencies, quartic)
                    observables = {
                        'q': np.mean(q*q0/np.array(reference['q_variance']), axis=-1),
                        'p': np.mean(p*p0/temp, axis=-1),
                        'k': (k-reference['k_mean'])*(k0-reference['k_mean'])/reference['k_variance'],
                        'h': (h-reference['h_mean'])*(h0-reference['h_mean'])/reference['h_variance']}
                    row = {'series': 'correlation', 'method': method, 'tau': tau, 'dt': step, 'lag': lag,
                           'replicas': canonical_n}
                    for name, samples in observables.items():
                        value, se = float(samples.mean()), float(samples.std(ddof=1)/math.sqrt(canonical_n))
                        row[name+'_acf'] = value;row[name+'_acf_standard_error'] = se
                        worst['acf_standard_error'] = max(worst['acf_standard_error'], se)
                    if quartic == 0 and method == 'langevin':
                        independent = harmonic_langevin_reference(step, tau, frequencies, temp, lag)
                        for name in ['q', 'p', 'k', 'h']:
                            key = name+'_acf';exact = independent[key]
                            error = abs(row[key]-exact)
                            z = error/max(row[key+'_standard_error'], 1e-15)
                            row[key+'_discrete_reference'] = exact
                            row[key+'_absolute_error'] = error;row[key+'_z'] = z
                            worst['langevin_acf_absolute_error'] = max(worst['langevin_acf_absolute_error'], error)
                            worst['langevin_acf_z'] = max(worst['langevin_acf_z'], z)
                        row['q_acf_continuum_reference'] = independent['q_acf_continuum']
                    records.append(row)
    metrics = {'maximum_'+key: value for key, value in worst.items()}
    metrics['quadrature_refinement_error'] = ref_error
    if quartic > 0:
        # No independent dynamical reference is claimed for the quartic case.
        metrics.pop('maximum_langevin_acf_absolute_error')
        metrics.pop('maximum_langevin_acf_z')
    a = config['acceptance']
    checks = {'canonical_position_momentum_energy_cdfs': worst['canonical_cdf'] <= a['canonical_cdf_error'],
              'canonical_energy_means': worst['canonical_mean'] <= a['canonical_mean_relative_error'],
              'canonical_energy_fluctuations': worst['canonical_variance'] <= a['canonical_variance_relative_error'],
              'heated_start_cdfs': worst['heated_cdf'] <= a['heated_cdf_error'],
              'heated_start_energy_means': worst['heated_mean'] <= a['heated_mean_relative_error'],
              'heated_start_energy_fluctuations': worst['heated_variance'] <= a['heated_variance_relative_error'],
              'quadrature_reference_refined': ref_error <= a['quadrature_refinement_error'],
              'independent_replica_correlation_uncertainty': worst['acf_standard_error'] <= a['maximum_correlation_standard_error']}
    if quartic == 0:
        biases, covariance_error = [], []
        for step in config['reference_steps']:
            analytic = np.array([np.diag([temp/(w*w*(1-step*step*w*w/4)), temp]) for w in frequencies])
            numerical = harmonic_langevin_reference(step, config['tau_values'][0], frequencies, temp, 0.)['covariance']
            covariance_error.append(float(np.max(abs(numerical-analytic))))
            bias = float(np.max(abs(analytic[:, 0, 0]-temp/frequencies**2)))
            biases.append(bias)
            records.append({'series': 'deterministic-shadow-reference', 'dt': step,
                            'maximum_position_variance_bias': bias, 'lyapunov_difference': covariance_error[-1]})
        orders = [math.log(biases[i]/biases[i+1])/math.log(config['reference_steps'][i]/config['reference_steps'][i+1])
                  for i in range(len(biases)-1)]
        metrics.update(minimum_shadow_bias_order=min(orders), maximum_shadow_covariance_error=max(covariance_error),
                       finest_shadow_position_bias=biases[-1])
        checks.update(langevin_independent_discrete_correlation=worst['langevin_acf_absolute_error'] <= a['langevin_reference_acf_absolute_error'] and worst['langevin_acf_z'] <= a['langevin_reference_acf_z'],
                      shadow_covariance_identity=max(covariance_error) <= a['maximum_shadow_covariance_error'],
                      deterministic_second_order_bias=min(orders) >= a['minimum_shadow_bias_order'],
                      finest_shadow_bias=biases[-1] <= a['finest_shadow_position_bias'])
    ident = 'csvr-langevin-harmonic' if quartic == 0 else 'csvr-langevin-quartic'
    return result(ident, checks, metrics, records, canonical_reference=reference,
                  comparison_policy={'splitting': 'O/2 - velocity-Verlet - O/2 (OBABO)',
                                     'coupling_match': 'gamma=1/(2*tau), equal bath-only kinetic relaxation',
                                     'correlation_policy': 'Measure q,p,K,H separately. Global and local full-MD correlations need not agree.',
                                     'canonical_start': 'Tests invariance, not ergodicity.',
                                     'heated_start': 'Finite-time full-support ensemble check, not a general mixing proof.'})


def harmonic_case(config):
    validate_config(config, 'harmonic')
    return comparison_case(config)


def quartic_case(config):
    validate_config(config, 'quartic')
    return comparison_case(config)


RUNNERS = {'csvr-kinetic-kernel': kinetic_case,
           'csvr-langevin-harmonic': harmonic_case,
           'csvr-langevin-quartic': quartic_case}
