"""Small original sampling, Langevin and reaction/excitation experiments.

References provide algorithms and context; all acceptance conditions live in inputs.json.
SciPy is used only for separate analytic/linear-algebra/ODE references.
"""
import math
import numpy as np
from scipy.linalg import expm, solve_discrete_lyapunov
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import ndtr


def finite_number(value, name, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not np.isfinite(value):
        raise ValueError(name + ' must be finite')
    if positive and value <= 0:
        raise ValueError(name + ' must be positive')
    return float(value)


def integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(name + ' must be an integer >= ' + str(minimum))
    return value


def rk4_step(rhs, y, h):
    a = rhs(y)
    b = rhs(y + h*a/2)
    c = rhs(y + h*b/2)
    d = rhs(y + h*c)
    return y + h*(a + 2*b + 2*c + d)/6


def integrate_fixed(rhs, initial, end, step):
    n = int(round(end/step))
    if n < 1 or not np.isclose(n*step, end, rtol=0, atol=1e-11):
        raise ValueError('end/step must be a positive integer')
    y = np.array(initial, dtype=float, copy=True)
    for _ in range(n):
        y = rk4_step(rhs, y, step)
        if not np.all(np.isfinite(y)):
            raise ArithmeticError('nonfinite state')
    return y


def periodic_laplacian(y, dx):
    return (np.roll(y, 1, axis=-1)-2*y+np.roll(y, -1, axis=-1))/dx**2


def initial_positive_tau(acf):
    """Geyer initial-positive paired autocovariances, normalized by gamma_0.

    Pairs start with rho_0+rho_1. Thus tau = -1 + 2 sum(pairs).
    The conservative floor tau>=1 omits super-efficient anticorrelated estimates.
    """
    acf = np.asarray(acf, dtype=float)
    if acf.ndim != 1 or len(acf) < 2 or not np.all(np.isfinite(acf)):
        raise ValueError('finite one-dimensional acf required')
    pairs = acf[:2*(len(acf)//2)].reshape(-1, 2).sum(axis=1)
    stop = np.flatnonzero(pairs <= 0)
    positive = pairs[:int(stop[0])] if len(stop) else pairs
    return float(max(1.0, -1 + 2*positive.sum()))


def chain_diagnostics(samples):
    """Classical split-Rhat plus pooled within-chain initial-positive ESS.

    This is not modern rank-normalized Rhat, nor a convergence certificate.
    ESS is for the scalar mean observable only.
    """
    x = np.asarray(samples, dtype=float)
    if x.ndim != 2 or min(x.shape) < 4 or not np.all(np.isfinite(x)):
        raise ValueError('finite chains x samples array required')
    m, n = x.shape
    nfft = 1 << (2*n-1).bit_length()
    centered = x-x.mean(axis=1, keepdims=True)
    fourier = np.fft.rfft(centered, n=nfft, axis=1)
    cov = np.fft.irfft(fourier*fourier.conj(), n=nfft, axis=1)[:, :n].mean(axis=0)/n
    if cov[0] <= 1e-24:
        raise ValueError('zero within-chain variance')
    acf = cov/cov[0]
    tau = initial_positive_tau(acf)
    half = n//2
    split = np.concatenate([x[:, :half], x[:, -half:]], axis=0)
    within = split.var(axis=1, ddof=1).mean()
    between = half*split.mean(axis=1).var(ddof=1)
    rhat = math.sqrt(((half-1)*within/half+between/half)/within)
    return {'tau': tau, 'ess': float(m*n/tau), 'split_rhat': float(rhat),
            'acf_lag1': float(acf[1])}


def gaussian_metropolis(seed, chains, samples, burn, proposal):
    integer(chains, 'chains', 4)
    integer(samples, 'samples', 8)
    integer(burn, 'burn', 0)
    finite_number(proposal, 'proposal', True)
    streams = [np.random.default_rng(s) for s in np.random.SeedSequence(seed).spawn(chains)]
    normals = np.array([rng.normal(size=samples+burn) for rng in streams])
    uniforms = np.array([rng.random(samples+burn) for rng in streams])
    state = np.linspace(-4., 4., chains)
    output = np.empty((chains, samples))
    accepted = 0
    for i in range(samples+burn):
        candidate = state+proposal*normals[:, i]
        take = np.log(uniforms[:, i]) < -.5*(candidate*candidate-state*state)
        state = np.where(take, candidate, state)
        if i >= burn:
            output[:, i-burn] = state
            accepted += int(take.sum())
    return output, accepted/(chains*samples)


def mcmc_case(config):
    x, acceptance = gaussian_metropolis(**config['sampler'])
    thresholds = np.array(config['cdf_points'], dtype=float)
    cdf = np.mean(x[..., None] <= thresholds, axis=(0, 1))
    target = ndtr(thresholds)
    diag = chain_diagnostics(x)
    records = []
    for n in config['sample_budgets']:
        integer(n, 'sample_budget', 8)
        if n > x.shape[1]:
            raise ValueError('sample_budget exceeds fixed run')
        means = x[:, :n].mean(axis=1)
        records.append({'samples_per_chain': n, 'mean_rmse_across_chains': float(np.sqrt(np.mean(means**2))),
                        **chain_diagnostics(x[:, :n])})
    rho = finite_number(config['ar1_rho'], 'ar1_rho')
    if not 0 < rho < 1:
        raise ValueError('AR(1) diagnostic reference needs 0<rho<1')
    exact_tau = (1+rho)/(1-rho)
    series_tau = initial_positive_tau(rho**np.arange(2048))
    rng = np.random.default_rng(config['sampler']['seed']+1000)
    ar = np.empty_like(x)
    ar[:, 0] = rng.normal(size=x.shape[0])
    for i in range(1, x.shape[1]):
        ar[:, i] = rho*ar[:, i-1]+math.sqrt(1-rho*rho)*rng.normal(size=x.shape[0])
    ar_tau = chain_diagnostics(ar)['tau']
    metrics = {'mean_error': float(abs(x.mean())), 'variance_error': float(abs(x.var()-1)),
               'cdf_max_error': float(np.max(abs(cdf-target))), 'acceptance': acceptance,
               **diag, 'ar1_exact_tau': exact_tau, 'ar1_series_tau_error': abs(series_tau-exact_tau),
               'ar1_empirical_tau_relative_error': abs(ar_tau/exact_tau-1),
               'budget_mean_rmse_ratio': records[0]['mean_rmse_across_chains']/records[-1]['mean_rmse_across_chains']}
    a = config['acceptance']
    checks = {'finite': bool(np.all(np.isfinite(x))),
              'mean': metrics['mean_error'] <= a['mean_error'],
              'variance': metrics['variance_error'] <= a['variance_error'],
              'cdf': metrics['cdf_max_error'] <= a['cdf_max_error'],
              'split_rhat': diag['split_rhat'] <= a['split_rhat'],
              'ess': diag['ess'] >= a['minimum_ess'],
              'acceptance': a['acceptance_min'] <= acceptance <= a['acceptance_max'],
              'ar1_exact_sequence': metrics['ar1_series_tau_error'] <= a['ar1_series_error'],
              'ar1_sampling_diagnostic': metrics['ar1_empirical_tau_relative_error'] <= a['ar1_tau_relative_error'],
              'sample_budget': metrics['budget_mean_rmse_ratio'] >= a['budget_rmse_ratio']}
    records += [{'cdf_point': float(z), 'empirical_cdf': float(p), 'normal_cdf': float(q)} for z, p, q in zip(thresholds, cdf, target)]
    return result('gaussian-mcmc', checks, metrics, records)


def baoab_step(q, p, h, omega, gamma, temperature, noise):
    p = p-h*omega**2*q/2
    q = q+h*p/2
    c = math.exp(-gamma*h)
    p = c*p+math.sqrt(temperature*(-math.expm1(-2*gamma*h)))*noise
    q = q+h*p/2
    p = p-h*omega**2*q/2
    return q, p


def baoab_linear_map(h, omega, gamma, temperature):
    for name, value in [('h', h), ('omega', omega), ('gamma', gamma), ('temperature', temperature)]:
        finite_number(value, name, True)
    if h*omega >= 2:
        raise ValueError('harmonic BAOAB requires h*omega < 2')
    B = np.array([[1., 0.], [-h*omega**2/2, 1.]])
    A = np.array([[1., h/2], [0., 1.]])
    O = np.diag([1., math.exp(-gamma*h)])
    matrix = B@A@O@A@B
    noise = B@A@np.array([0., math.sqrt(temperature*(-math.expm1(-2*gamma*h)))])
    return matrix, np.outer(noise, noise)


def ecdf_error(values, cdf):
    ordered = np.sort(np.asarray(values, dtype=float))
    n = len(ordered)
    target = cdf(ordered)
    return float(max(np.max(np.arange(1, n+1)/n-target), np.max(target-np.arange(n)/n)))


def langevin_case(config):
    omega, gamma, temp = [finite_number(config[n], n, True) for n in ['omega', 'gamma', 'temperature']]
    replicas = integer(config['replicas'], 'replicas', 1024)
    canonical = np.diag([temp/omega**2, temp])
    generator = np.array([[0., 1.], [-omega**2, -gamma]])
    records = []
    all_samples = []
    for j, h in enumerate(config['steps']):
        matrix, noise_cov = baoab_linear_map(h, omega, gamma, temp)
        stationary = solve_discrete_lyapunov(matrix, noise_cov)
        residual = np.max(abs(stationary-matrix@stationary@matrix.T-noise_cov))
        rng = np.random.default_rng(config['seed']+j)
        q = np.zeros(replicas)
        p = np.zeros(replicas)
        burn_steps = int(math.ceil(config['burn_time']/h))
        burn_propagator = np.linalg.matrix_power(matrix, burn_steps)
        transient_covariance_error = float(np.max(abs(burn_propagator@stationary@burn_propagator.T)))
        for _ in range(burn_steps):
            q, p = baoab_step(q, p, h, omega, gamma, temp, rng.normal(size=replicas))
        sample = np.column_stack([q, p])
        covariance = sample.T@sample/replicas
        energy = (p*p+omega**2*q*q)/2
        q0 = q.copy()
        lag_steps = int(round(config['lag_time']/h))
        if not np.isclose(lag_steps*h, config['lag_time']):
            raise ValueError('lag_time must align with each step')
        for _ in range(lag_steps):
            q, p = baoab_step(q, p, h, omega, gamma, temp, rng.normal(size=replicas))
        empirical_corr = float(np.mean(q*q0)/canonical[0, 0])
        discrete_corr = float((np.linalg.matrix_power(matrix, lag_steps)@stationary)[0, 0]/canonical[0, 0])
        continuum_corr = float((expm(generator*config['lag_time'])@canonical)[0, 0]/canonical[0, 0])
        records.append({'dt': h, 'burn_steps': burn_steps, 'replicas': replicas,
            'discrete_covariance': stationary.tolist(), 'sample_covariance': covariance.tolist(),
            'discrete_covariance_bias': float(np.max(abs(stationary-canonical))),
            'covariance_sampling_error': float(np.max(abs(covariance-stationary))),
            'stationary_lyapunov_residual': float(residual),
            'burn_transient_covariance_error': transient_covariance_error,
            'q_correlation_sample': empirical_corr, 'q_correlation_discrete': discrete_corr,
            'q_correlation_continuum': continuum_corr,
            'correlation_sampling_error': abs(empirical_corr-discrete_corr),
            'energy_cdf_error': ecdf_error(energy, lambda e: -np.expm1(-e/temp)),
            'position_cdf_error': ecdf_error(sample[:, 0], lambda x: ndtr(x*omega/math.sqrt(temp))),
            'momentum_cdf_error': ecdf_error(sample[:, 1], lambda p: ndtr(p/math.sqrt(temp))),
            'energy_mean_error': abs(float(energy.mean())-temp),
            'energy_variance_error': abs(float(energy.var())-temp**2)})
        all_samples.append(sample)
    bias = [r['discrete_covariance_bias'] for r in records]
    orders = [math.log(bias[i]/bias[i+1])/math.log(config['steps'][i]/config['steps'][i+1]) for i in range(len(bias)-1)]
    metrics = {'maximum_covariance_sampling_error': max(r['covariance_sampling_error'] for r in records),
               'maximum_correlation_sampling_error': max(r['correlation_sampling_error'] for r in records),
               'maximum_lyapunov_residual': max(r['stationary_lyapunov_residual'] for r in records),
               'maximum_burn_transient_covariance_error': max(r['burn_transient_covariance_error'] for r in records),
               'minimum_covariance_bias_order': min(orders),
               'finest_covariance_bias': bias[-1],
               **{k: records[-1][k] for k in ['energy_cdf_error', 'position_cdf_error', 'momentum_cdf_error', 'energy_mean_error', 'energy_variance_error']}}
    a = config['acceptance']
    checks = {'finite': all(np.all(np.isfinite(s)) for s in all_samples),
              'stationary_reference': metrics['maximum_lyapunov_residual'] <= a['lyapunov_residual'],
              'burn_transient': metrics['maximum_burn_transient_covariance_error'] <= a['burn_covariance_error'],
              'covariance_sampling': metrics['maximum_covariance_sampling_error'] <= a['covariance_sampling_error'],
              'correlation_sampling': metrics['maximum_correlation_sampling_error'] <= a['correlation_sampling_error'],
              'bias_refinement': min(orders) >= a['minimum_bias_order'],
              'finest_bias': bias[-1] <= a['finest_covariance_bias'],
              'canonical_energy_cdf': metrics['energy_cdf_error'] <= a['cdf_error'],
              'canonical_position_cdf': metrics['position_cdf_error'] <= a['cdf_error'],
              'canonical_momentum_cdf': metrics['momentum_cdf_error'] <= a['cdf_error'],
              'canonical_energy_mean': metrics['energy_mean_error'] <= a['energy_mean_error'],
              'canonical_energy_variance': metrics['energy_variance_error'] <= a['energy_variance_error']}
    return result('langevin-harmonic', checks, metrics, records)


def observed_orders(records, error='max_error', scale='n'):
    return [math.log(records[i][error]/records[i+1][error])/math.log(records[i+1][scale]/records[i][scale])
            for i in range(len(records)-1)]


def reaction_diffusion_case(config):
    D, r, T = [finite_number(config[n], n, n != 'reaction') for n in ['diffusion', 'reaction', 'time']]
    mode = integer(config['mode'], 'mode')
    spatial = []
    for n in config['grids']:
        dx = 2*math.pi/n
        x = np.arange(n)*dx
        rhs = lambda y: D*periodic_laplacian(y, dx)+r*y
        y = integrate_fixed(rhs, np.cos(mode*x), T, config['space_dt'])
        exact = math.exp((r-D*mode**2)*T)*np.cos(mode*x)
        spatial.append({'sequence': 'space', 'n': n, 'dt': config['space_dt'], 'max_error': float(np.max(abs(y-exact)))})
    n = config['temporal_grid']
    dx = 2*math.pi/n
    x = np.arange(n)*dx
    lam_h = r-D*4*math.sin(mode*dx/2)**2/dx**2
    temporal = []
    for h in config['time_steps']:
        rhs = lambda y: D*periodic_laplacian(y, dx)+r*y
        y = integrate_fixed(rhs, np.cos(mode*x), T, h)
        exact_h = math.exp(lam_h*T)*np.cos(mode*x)
        temporal.append({'sequence': 'time', 'n': n, 'dt': h, 'inverse_dt': 1/h,
                         'max_error': float(np.max(abs(y-exact_h)))})
    metrics = {'spatial_finest_error': spatial[-1]['max_error'], 'spatial_minimum_order': min(observed_orders(spatial)),
               'temporal_finest_error': temporal[-1]['max_error'], 'temporal_minimum_order': min(observed_orders(temporal, scale='inverse_dt'))}
    a = config['acceptance']
    checks = {'space_error': metrics['spatial_finest_error'] <= a['space_error'],
              'space_order': metrics['spatial_minimum_order'] >= a['space_order'],
              'time_error': metrics['temporal_finest_error'] <= a['time_error'],
              'time_order': metrics['temporal_minimum_order'] >= a['time_order']}
    return result('reaction-diffusion-fourier', checks, metrics, spatial+temporal)


def turing_case(config):
    a, b = config['a'], config['b']
    if a <= 0 or b <= 0:
        raise ValueError('positive Schnakenberg rates required')
    steady = np.array([a+b, b/(a+b)**2])
    u, v = steady
    jac = np.array([[-1+2*u*v, u*u], [-2*u*v, -u*u]])
    diffusion = np.array(config['diffusion'], dtype=float)
    mode = integer(config['mode'], 'mode')
    continuous = jac-np.diag(diffusion*mode**2)
    eigenvalues, eigenvectors = np.linalg.eig(continuous)
    index = np.argmax(eigenvalues.real)
    eigenvector = eigenvectors[:, index].real
    eigenvector /= np.max(abs(eigenvector))
    growth = float(eigenvalues[index].real)
    spatial = []
    for n in config['grids']:
        dx = 2*math.pi/n
        x = np.arange(n)*dx
        perturb = config['amplitude']*eigenvector[:, None]*np.cos(mode*x)
        steps = int(math.ceil(config['linear_time']/(.2*dx*dx/diffusion.max())))
        h = config['linear_time']/steps
        rhs = lambda y: jac@y+diffusion[:, None]*periodic_laplacian(y, dx)
        y = integrate_fixed(rhs, perturb, config['linear_time'], h)
        exact = expm(continuous*config['linear_time'])@perturb
        projected = 2*(y@np.cos(mode*x))/n
        measured_growth = math.log(np.linalg.norm(projected)/(config['amplitude']*np.linalg.norm(eigenvector)))/config['linear_time']
        spatial.append({'sequence': 'linear-space', 'n': n, 'dt': h,
            'max_error': float(np.max(abs(y-exact))/config['amplitude']),
            'growth_rate': measured_growth, 'growth_rate_error': abs(measured_growth-growth)})
    n = config['nonlinear_grid']
    dx = 2*math.pi/n
    x = np.arange(n)*dx
    perturb = config['amplitude']*eigenvector[:, None]*np.cos(mode*x)
    def nonlinear(y):
        u, v = y
        reaction = np.array([a-u+u*u*v, b-u*u*v])
        return reaction+diffusion[:, None]*periodic_laplacian(y, dx)
    y = integrate_fixed(nonlinear, steady[:, None]+perturb, config['nonlinear_time'], config['nonlinear_dt'])
    kappa_h = 4*math.sin(mode*dx/2)**2/dx**2
    linear_h = expm((jac-np.diag(diffusion*kappa_h))*config['nonlinear_time'])@perturb
    deviation = y-steady[:, None]
    metrics = {'homogeneous_max_real_eigenvalue': float(np.max(np.linalg.eigvals(jac).real)),
               'continuum_mode_growth_rate': growth, 'linear_finest_relative_error': spatial[-1]['max_error'],
               'linear_minimum_spatial_order': min(observed_orders(spatial)),
               'linear_finest_growth_rate_error': spatial[-1]['growth_rate_error'],
               'nonlinear_minimum_concentration': float(y.min()),
               'nonlinear_early_linear_relative_error': float(np.max(abs(deviation-linear_h))/np.max(abs(linear_h))),
               'pattern_amplitude_growth': float(np.max(abs(deviation))/np.max(abs(perturb)))}
    accept = config['acceptance']
    checks = {'homogeneous_stable': metrics['homogeneous_max_real_eigenvalue'] < 0,
              'diffusion_mode_unstable': growth > 0,
              'linear_space_error': metrics['linear_finest_relative_error'] <= accept['linear_error'],
              'linear_space_order': metrics['linear_minimum_spatial_order'] >= accept['space_order'],
              'growth_rate': metrics['linear_finest_growth_rate_error'] <= accept['growth_rate_error'],
              'nonlinear_finite_positive': bool(np.all(np.isfinite(y)) and y.min()>0),
              'early_linear_agreement': metrics['nonlinear_early_linear_relative_error'] <= accept['early_linear_relative_error'],
              'growing_spatial_pattern': metrics['pattern_amplitude_growth'] >= accept['minimum_growth']}
    records = spatial+[{'sequence': 'nonlinear-profile', 'x': float(xi), 'u': float(ui), 'v': float(vi)} for xi, ui, vi in zip(x, *y)]
    return result('turing-schnakenberg', checks, metrics, records)


def fhn_rhs(y, current, a, b, tau):
    v, w = y
    return np.array([v-v**3/3-w+current, (v+a-b*w)/tau])


def fhn_case(config):
    a, b, tau = config['a'], config['b'], config['tau']
    rest_v = brentq(lambda v: v-v**3/3-(v+a)/b, -3, 0, xtol=1e-14)
    initial = np.array([rest_v, (rest_v+a)/b])
    segments = [(0., config['pulse_start'], 0.), (config['pulse_start'], config['pulse_end'], config['pulse_current']),
                (config['pulse_end'], config['time'], 0.)]
    times = np.arange(int(round(config['time']/config['output_dt']))+1)*config['output_dt']
    def reference(tolerance):
        y = initial.copy()
        output = np.empty((len(times), 2))
        for start, end, current in segments:
            sol = solve_ivp(lambda t, z: fhn_rhs(z, current, a, b, tau), (start, end), y,
                            method='DOP853', rtol=tolerance, atol=tolerance/20, dense_output=True)
            if not sol.success:
                raise RuntimeError(sol.message)
            take = (times >= start-1e-10)&(times <= end+1e-10)
            output[take] = sol.sol(times[take]).T
            y = sol.y[:, -1]
        return output
    reference_coarse, exact = reference(1e-11), reference(1e-13)
    records, trajectories = [], []
    for h in config['steps']:
        y = initial.copy()
        output = [y.copy()]
        output_stride = int(round(config['output_dt']/h))
        if not np.isclose(output_stride*h, config['output_dt']):
            raise ValueError('output_dt must be divisible by integration step')
        for start, end, current in segments:
            count = int(round((end-start)/h))
            if not np.isclose(count*h, end-start):
                raise ValueError('pulse boundaries must align with time steps')
            for step in range(count):
                y = rk4_step(lambda z: fhn_rhs(z, current, a, b, tau), y, h)
                if (step+1) % output_stride == 0:
                    output.append(y.copy())
        output = np.array(output)
        if output.shape != exact.shape or not np.all(np.isfinite(output)):
            raise ArithmeticError('invalid FHN output')
        error = float(np.max(abs(output-exact)))
        records.append({'sequence': 'time', 'dt': h, 'inverse_dt': 1/h, 'max_error': error,
                        'peak_v': float(output[:, 0].max()), 'peak_time': float(times[np.argmax(output[:, 0])]),
                        'recovery_distance': float(np.max(abs(output[-1]-initial)))})
        trajectories.append(output)
    metrics = {'reference_tolerance_difference': float(np.max(abs(reference_coarse-exact))),
               'finest_max_error': records[-1]['max_error'], 'minimum_temporal_order': min(observed_orders(records, scale='inverse_dt')),
               'peak_v': records[-1]['peak_v'], 'peak_v_error': abs(records[-1]['peak_v']-float(exact[:, 0].max())),
               'peak_time_error': abs(records[-1]['peak_time']-float(times[np.argmax(exact[:, 0])])),
               'recovery_distance': records[-1]['recovery_distance']}
    accept = config['acceptance']
    checks = {'reference_tolerance': metrics['reference_tolerance_difference'] <= accept['reference_difference'],
              'solution_error': metrics['finest_max_error'] <= accept['solution_error'],
              'time_order': metrics['minimum_temporal_order'] >= accept['time_order'],
              'excitation': metrics['peak_v'] >= accept['minimum_peak'],
              'peak_voltage': metrics['peak_v_error'] <= accept['peak_error'],
              'peak_time': metrics['peak_time_error'] <= accept['peak_time_error'],
              'recovery': metrics['recovery_distance'] <= accept['recovery_distance']}
    records += [{'sequence': 'trajectory', 't': float(t), 'v': float(y[0]), 'w': float(y[1]),
                 'reference_v': float(z[0]), 'reference_w': float(z[1])} for t, y, z in zip(times, trajectories[-1], exact)]
    return result('fitzhugh-nagumo', checks, metrics, records)


def result(name, checks, metrics, records):
    checks = {k: bool(v) for k, v in checks.items()}
    return {'id': name, 'passed': all(checks.values()), 'termination': 'fixed_budget_completed',
            'checks': checks, 'metrics': metrics, 'records': records}


RUNNERS = {'gaussian-mcmc': mcmc_case, 'langevin-harmonic': langevin_case,
           'reaction-diffusion-fourier': reaction_diffusion_case, 'turing-schnakenberg': turing_case,
           'fitzhugh-nagumo': fhn_case}
