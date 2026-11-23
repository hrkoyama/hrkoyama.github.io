"""Small, original standard-library numerical experiments for the beginner course.
No plotting dependency, network, random input or external numerical solver.
"""
import cmath, csv, hashlib, json, math
from decimal import Decimal, localcontext
from pathlib import Path

def norm(v, h=1.0):
    return math.sqrt(h * sum((abs(x) ** 2 for x in v)))

def orders(errors):
    return [math.log(a / b, 2) for (a, b) in zip(errors, errors[1:])]

def maxabs(v):
    return max(map(abs, v), default=0.0)

def tridiagonal(lo, di, up, b):
    """Thomas elimination for the nonsingular tridiagonal examples used here."""
    n = len(di)
    if not (n and len(lo) == len(up) == n - 1 and (len(b) == n)):
        raise ValueError('array lengths')
    c = list(up)
    a = list(di)
    x = list(b)
    for i in range(1, n):
        if abs(a[i - 1]) < 1e-30:
            raise ValueError('zero pivot')
        z = lo[i - 1] / a[i - 1]
        a[i] -= z * c[i - 1]
        x[i] -= z * x[i - 1]
    if abs(a[-1]) < 1e-30:
        raise ValueError('singular system')
    x[-1] /= a[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (x[i] - c[i] * x[i + 1]) / a[i]
    return x

def symbol(method, theta, nu):
    if method == 'upwind':
        return 1 - nu + nu * cmath.exp(-1j * theta)
    if method == 'lax-wendroff':
        return 1 - 1j * nu * math.sin(theta) + nu * nu * (math.cos(theta) - 1)
    if method == 'ftcs':
        return 1 - 1j * nu * math.sin(theta)
    raise ValueError(method)

def advect(u, nu, method):
    if method == 'upwind':
        return [u[j] - nu * (u[j] - u[j - 1]) for j in range(len(u))]
    if method == 'lax-wendroff':
        return [u[j] - 0.5 * nu * (u[(j + 1) % len(u)] - u[j - 1]) + 0.5 * nu * nu * (u[(j + 1) % len(u)] - 2 * u[j] + u[j - 1]) for j in range(len(u))]
    if method == 'ftcs':
        return [u[j] - 0.5 * nu * (u[(j + 1) % len(u)] - u[j - 1]) for j in range(len(u))]
    raise ValueError(method)

def heat_step(u, r):
    return [0.0] + [u[i] + r * (u[i - 1] - 2 * u[i] + u[i + 1]) for i in range(1, len(u) - 1)] + [0.0]

def R(method, z):
    if method == 'forward':
        return 1 + z
    if method == 'backward':
        return 1 / (1 - z)
    if method == 'trapezoidal':
        return (1 + z / 2) / (1 - z / 2)
    raise ValueError(method)

def oscillator_step(q, p, h, method):
    if method == 'forward':
        return (q + h * p, p - h * q)
    if method == 'backward':
        return ((q + h * p) / (1 + h * h), (p - h * q) / (1 + h * h))
    if method == 'symplectic':
        pn = p - h * q
        return (q + h * pn, pn)
    if method == 'verlet':
        ph = p - h * q / 2
        qn = q + h * ph
        return (qn, ph - h * qn / 2)
    raise ValueError(method)

def modified_energy(q, p, h, method):
    if method == 'symplectic':
        return (q * q + p * p - h * q * p) / 2
    if method == 'verlet':
        return ((1 - h * h / 4) * q * q + p * p) / 2
    return (q * q + p * p) / 2

def neumann_compatibility(f, h, gleft=0.0, gright=0.0, tolerance=1e-10):
    defect = h * (sum(f) - 0.5 * (f[0] + f[-1])) + gleft + gright
    if abs(defect) > tolerance:
        raise ValueError('incompatible Neumann source and outward derivatives')
    return defect

def poisson(n, kind, alpha=2.0, beta=1.0):
    h = 1 / n
    x = [i * h for i in range(n + 1)]
    if kind == 'dirichlet':
        exact = [math.sin(math.pi * z) + 0.3 * z + 1 for z in x]
        f = [math.pi ** 2 * math.sin(math.pi * z) for z in x]
    elif kind == 'neumann':
        exact = [math.cos(2 * math.pi * z) for z in x]
        f = [4 * math.pi ** 2 * math.cos(2 * math.pi * z) for z in x]
    else:
        exact = [math.exp(z) for z in x]
        f = [-math.exp(z) for z in x]
    lo = [-1.0] * n
    di = [2.0] * (n + 1)
    up = [-1.0] * n
    b = [h * h * z for z in f]
    if kind == 'dirichlet':
        di[0] = di[-1] = 1
        up[0] = lo[-1] = 0
        b[0] = exact[0]
        b[-1] = exact[-1]
    elif kind == 'neumann':
        neumann_compatibility(f, h)
        di[0] = di[-1] = 1
        b[0] /= 2
        b[-1] /= 2
        up[0] = 0
        b[0] = 0
    elif kind == 'robin':
        if alpha <= 0 or beta <= 0:
            raise ValueError('this Robin example requires positive alpha,beta')
        di[0] = di[-1] = 1 + h * alpha / beta
        b[0] = h * h * f[0] / 2 + h * (alpha - beta) / beta
        b[-1] = h * h * f[-1] / 2 + h * (alpha + beta) * math.e / beta
    elif kind in ['mixed-good', 'mixed-naive']:
        di[0] = 1
        b[0] = -h + (h * h * f[0] / 2 if kind == 'mixed-good' else 0)
        di[-1] = 1
        lo[-1] = 0
        b[-1] = math.e
    else:
        raise ValueError(kind)
    u = tridiagonal(lo, di, up, b)
    if kind == 'neumann':
        mean = h * (sum(u) - 0.5 * (u[0] + u[-1]))
        u = [z - mean for z in u]
    res = []
    for i in range(1, n):
        res.append(-u[i - 1] + 2 * u[i] - u[i + 1] - h * h * f[i])
    if kind == 'neumann':
        res += [u[0] - u[1] - h * h * f[0] / 2, u[-1] - u[-2] - h * h * f[-1] / 2]
    else:
        res += [di[0]*u[0] + up[0]*u[1] - b[0],
                lo[-1]*u[-2] + di[-1]*u[-1] - b[-1]]
    return (x, u, exact, maxabs(res))

def experiment(config):
    rows = {}
    metrics = {}
    checks = {}
    c = config['derivative']
    x = c['x']
    errs = []
    a = []
    for h in c['hs']:
        v = (math.sin(x + h) - math.sin(x - h)) / (2 * h)
        e = abs(v - math.cos(x))
        errs.append(e)
        a.append([h, v, e])
    checks['derivative_order'] = min(orders(errs)) >= c['min_order']
    decade = []
    for i in range(1, c['decades'] + 1):
        h = 10.0 ** (-i)
        v = (math.sin(x + h) - math.sin(x - h)) / (2 * h)
        decade.append([h, v, abs(v - math.cos(x))])
    checks['roundoff_floor_visible'] = decade[-1][2] > c['min_roundoff_to_best_ratio'] * min((z[2] for z in decade))
    rows['derivative'] = (['h', 'approximation', 'error'], decade)
    metrics['derivative'] = {'orders': orders(errs), 'best_h': min(decade, key=lambda z: z[2])[0]}
    a = []
    for n in config['norms']['meshes']:
        h = config['norms']['length'] / n
        e = [0.0] * n
        e[n // 2] = 1
        a.append([n, h, h, math.sqrt(h), 1.0])
    rows['norms'] = (['n', 'h', 'l1', 'l2', 'linf'], a)
    checks['norms_match_cell_integrals'] = all((abs(z[2] - 1 / z[0]) < 1e-15 and abs(z[3] - 1 / math.sqrt(z[0])) < 1e-15 and (z[4] == 1) for z in a))
    c = config['conditioning']
    eps = c['epsilon']
    delta = c['rhs_perturbation']
    xh = [1 - delta / eps, 1 + delta / eps]
    A = [[1.0, 1.0], [1.0, 1 + eps]]
    b = [2.0, 2 + eps]
    res = [sum((ai * xj for (ai, xj) in zip(row, xh))) - bi for (row, bi) in zip(A, b)]
    forward = maxabs([z - 1 for z in xh])
    relative = maxabs(res) / maxabs(b)
    cond = (2 + eps) ** 2 / eps
    with localcontext() as ctx:
        ctx.prec = 50
        ed = Decimal(str(eps))
        dd = Decimal(str(delta))
        xd = [Decimal(1) - dd / ed, Decimal(1) + dd / ed]
    checks['conditioned_solution_matches_decimal'] = max((abs(x - float(y)) for (x, y) in zip(xh, xd))) <= c['max_decimal_difference']
    checks['small_residual_large_error'] = forward / relative >= c['min_amplification']
    checks['condition_bound'] = forward <= cond * relative * (1 + 1e-06)
    metrics['conditioning'] = {'condition_inf': cond, 'forward_relative_inf': forward, 'residual_relative_inf': relative, 'amplification': forward / relative, 'backward_error': maxabs(res) / ((2 + eps) * maxabs(xh) + maxabs(b))}
    rows['conditioning'] = (['component', 'exact', 'perturbed_solution', 'residual'], [[i, 1.0, xh[i], res[i]] for i in range(2)])
    c = config['ode']
    a = []
    trace = []
    om = {}
    for method in ['forward', 'backward', 'trapezoidal']:
        errs = []
        for n in c['steps']:
            dt = c['end'] / n
            y = R(method, c['lambda'] * dt) ** n
            e = abs(y - math.exp(c['lambda'] * c['end']))
            errs.append(e)
            a.append([method, n, dt, y, e])
        om[method] = {'orders': orders(errs), 'fine_error': errs[-1]}
        minimum = c['min_trapezoidal_order'] if method == 'trapezoidal' else c['min_euler_order']
        maximum = c['max_trapezoidal_fine_error'] if method == 'trapezoidal' else c['max_euler_fine_error']
        checks['ode_' + method] = min(orders(errs)) >= minimum and errs[-1] <= maximum
        for n in range(c['stiff_steps'] + 1):
            trace.append([method, n * c['stiff_dt'], R(method, c['stiff_lambda'] * c['stiff_dt']) ** n])
    checks['stiff_expected_behavior'] = abs(R('trapezoidal', c['stiff_lambda'] * c['stiff_dt'])) < 1 and R('trapezoidal', c['stiff_lambda'] * c['stiff_dt']) < 0 and (abs(R('backward', c['stiff_lambda'] * c['stiff_dt'])) < abs(R('trapezoidal', c['stiff_lambda'] * c['stiff_dt']))) and (abs(R('forward', c['stiff_lambda'] * c['stiff_dt'])) > 1)
    metrics['ode'] = om
    rows['ode'] = (['method', 'steps', 'dt', 'value', 'error'], a)
    rows['stiff'] = (['method', 'time', 'value'], trace)
    c = config['advection']
    a = []
    fields = []
    am = {}
    spectral = []
    exact = lambda x, t: sum((v * math.sin(2 * math.pi * k * (x - c['speed'] * t) / c['length']) for (k, v) in c['modes']))
    for method in ['upwind', 'lax-wendroff']:
        errs = []
        for n in c['meshes']:
            h = c['length'] / n
            steps = round(c['end'] * c['speed'] / (c['courant'] * h))
            dt = c['end'] / steps
            nu = c['speed'] * dt / h
            u = [exact(j * h, 0) for j in range(n)]
            for _ in range(steps):
                u = advect(u, nu, method)
            ref = [exact(j * h, c['end']) for j in range(n)]
            error = norm([x - y for (x, y) in zip(u, ref)], h)
            errs.append(error)
            a.append([method, n, h, dt, steps, error, h * sum(u), norm(u, h)])
            if n == c['meshes'][-1]:
                fields += [[method, j * h, u[j], ref[j]] for j in range(n)]
        am[method] = {'orders': orders(errs), 'fine_l2': errs[-1]}
        checks['advection_' + method] = min(orders(errs)) >= (c['min_upwind_order'] if method == 'upwind' else c['min_lw_order']) and errs[-1] <= (c['max_upwind_fine_l2'] if method == 'upwind' else c['max_lw_fine_l2'])
        checks['advection_mass_' + method] = max((abs(z[6]) for z in a if z[0] == method)) < 1e-12
        for j in range(1, 64):
            theta = math.pi * j / 64
            g = symbol(method, theta, c['courant'])
            gp = -1j * c['courant'] * cmath.exp(-1j * theta) if method == 'upwind' else -1j * c['courant'] * math.cos(theta) - c['courant'] ** 2 * math.sin(theta)
            spectral.append([method, theta / math.pi, abs(g), -cmath.phase(g) / (c['courant'] * theta), -(gp / g).imag / c['courant']])
    symerr = 0.0
    for method in ['upwind', 'lax-wendroff', 'ftcs']:
        n = 40
        theta = 2 * math.pi * 3 / n
        v = [cmath.exp(1j * theta * j) for j in range(n)]
        vn = advect(v, c['courant'], method)
        symerr = max(symerr, maxabs([a - symbol(method, theta, c['courant']) * b for (a, b) in zip(vn, v)]))
    checks['measured_fourier_symbol'] = symerr <= c['max_symbol_error']
    bad = []
    for (method, nu, label) in [('upwind', 1.2, 'upwind-CFL-1.2'), ('ftcs', 0.6, 'FTCS-CFL-0.6')]:
        v = [math.cos(math.pi * j / 2) for j in range(40)]
        n0 = norm(v)
        for n in range(c['diagnostic_steps'] + 1):
            bad.append([label, n, norm(v) / n0])
            v = advect(v, nu, method)
    checks['intentional_unstable_examples_grow'] = all((next((z[2] for z in reversed(bad) if z[0] == name)) > 50 for name in ['upwind-CFL-1.2', 'FTCS-CFL-0.6']))
    metrics['advection'] = am
    rows['advection'] = (['method', 'n', 'h', 'dt', 'steps', 'l2_error', 'mass', 'l2_norm'], a)
    rows['advection-field'] = (['method', 'x', 'numerical', 'reference'], fields)
    rows['symbols'] = (['method', 'theta_over_pi', 'amplitude', 'phase_speed_ratio', 'group_speed_ratio'], spectral)
    rows['unstable'] = (['method', 'step', 'norm_ratio'], bad)
    c = config['heat']
    a = []
    hm = {}

    def evolve(n, steps):
        h = 1 / n
        dt = c['end'] / steps
        r = c['diffusivity'] * dt / (h * h)
        if r > 0.50000000001:
            raise ValueError('explicit heat stability bound')
        u = [math.sin(math.pi * j * h) for j in range(n + 1)]
        u[0] = u[-1] = 0
        for _ in range(steps):
            u = heat_step(u, r)
        return (h, dt, u)
    for n in c['meshes']:
        h = 1 / n
        steps = round(c['end'] * c['diffusivity'] / (c['r'] * h * h))
        (h, dt, u) = evolve(n, steps)
        ref = [math.exp(-c['diffusivity'] * math.pi ** 2 * c['end']) * math.sin(math.pi * j * h) for j in range(n + 1)]
        a.append([n, h, dt, steps, norm([x - y for (x, y) in zip(u, ref)], h)])
    es = [z[-1] for z in a]
    checks['heat_joint_order'] = min(orders(es)) >= c['min_joint_order'] and es[-1] <= c['max_joint_fine_l2']
    hm['joint_orders'] = orders(es)
    rows['heat'] = (['n', 'h', 'dt', 'steps', 'continuum_l2_error'], a)
    a = []
    n = c['time_n']
    h = 1 / n
    rate = -4 * c['diffusivity'] * math.sin(math.pi / (2 * n)) ** 2 / (h * h)
    for steps in c['time_steps']:
        (h, dt, u) = evolve(n, steps)
        semi = [math.exp(rate * c['end']) * math.sin(math.pi * j * h) for j in range(n + 1)]
        cont = [math.exp(-c['diffusivity'] * math.pi ** 2 * c['end']) * math.sin(math.pi * j * h) for j in range(n + 1)]
        a.append([steps, dt, norm([x - y for (x, y) in zip(u, semi)], h), norm([x - y for (x, y) in zip(u, cont)], h)])
    es = [z[2] for z in a]
    checks['heat_time_order'] = min(orders(es)) >= c['min_time_order']
    hm['time_orders'] = orders(es)
    metrics['heat'] = hm
    rows['heat-time'] = (['steps', 'dt', 'semidiscrete_l2_error', 'continuum_l2_error'], a)
    c = config['boundary']
    a = []
    bf = []
    bm = {}
    maxres = 0.0
    for kind in ['dirichlet', 'neumann', 'robin', 'mixed-good', 'mixed-naive']:
        errs = []
        for n in c['meshes']:
            (x, u, ref, res) = poisson(n, kind, c['robin_alpha'], c['robin_beta'])
            maxres = max(maxres, res)
            e = maxabs([v - w for (v, w) in zip(u, ref)])
            errs.append(e)
            a.append([kind, n, 1 / n, e, res])
            if n == c['meshes'][-1]:
                bf += [[kind, t, v, w] for (t, v, w) in zip(x, u, ref)]
        oo = orders(errs)
        bm[kind] = {'orders': oo, 'fine_error': errs[-1]}
        checks['boundary_' + kind] = errs[-1] <= c['max_fine_errors'][kind] and (min(oo) >= c['min_good_order'] if kind != 'mixed-naive' else min(oo) >= c['naive_order_range'][0] and max(oo) <= c['naive_order_range'][1])
    checks['boundary_equation_residual'] = maxres <= c['max_equation_residual']
    checks['neumann_compatibility'] = all((abs(neumann_compatibility([4 * math.pi ** 2 * math.cos(2 * math.pi * j / n) for j in range(n + 1)], 1 / n, tolerance=c['max_compatibility_residual'])) <= c['max_compatibility_residual'] for n in c['meshes']))
    metrics['boundary'] = bm
    rows['boundary'] = (['kind', 'n', 'h', 'linf_error', 'equation_residual'], a)
    rows['boundary-field'] = (['kind', 'x', 'numerical', 'reference'], bf)
    c = config['splitting']
    a = []
    sm = {}
    for (method, label) in [('symplectic', 'lie'), ('verlet', 'strang')]:
        es = []
        for n in c['steps']:
            h = c['end'] / n
            (q, p) = (1.0, 0.0)
            for _ in range(n):
                (q, p) = oscillator_step(q, p, h, method)
            e = math.hypot(q - math.cos(c['end']), p + math.sin(c['end']))
            es.append(e)
            a.append([label, n, h, q, p, e])
        sm[label] = {'orders': orders(es), 'fine_error': es[-1]}
        checks['splitting_' + label] = min(orders(es)) >= (c['min_lie_order'] if label == 'lie' else c['min_strang_order']) and es[-1] <= (c['max_lie_fine_error'] if label == 'lie' else c['max_strang_fine_error'])
    commute = max((abs((math.exp(-h) * math.exp(-0.5 * h)) ** n - math.exp(-1.5 * c['end'])) for n in c['steps'] for h in [c['end'] / n]))
    checks['commuting_control'] = commute <= c['max_commuting_error']
    sm['commuting_error'] = commute
    metrics['splitting'] = sm
    rows['splitting'] = (['method', 'steps', 'dt', 'q', 'p', 'state_error'], a)
    c = config['oscillator']
    a = []
    om = {}
    h = c['dt']
    q0 = c['initial_q']
    p0 = c['initial_p']
    H0 = (q0 * q0 + p0 * p0) / 2
    for method in ['forward', 'backward', 'symplectic', 'verlet']:
        (q, p) = (q0, p0)
        M0 = modified_energy(q, p, h, method)
        maxE = maxM = 0.0
        phase = 0.0
        prev = math.atan2(-p, q)
        for n in range(c['steps'] + 1):
            H = (q * q + p * p) / 2
            M = modified_energy(q, p, h, method)
            maxE = max(maxE, abs(H / H0 - 1))
            maxM = max(maxM, abs(M / M0 - 1))
            angle = math.atan2(-p, q)
            z = (angle - prev + math.pi) % (2 * math.pi) - math.pi
            phase += z
            prev = angle
            a.append([method, n * h, q, p, H / H0, M / M0, phase - n * h])
            if n < c['steps']:
                (q, p) = oscillator_step(q, p, h, method)
        om[method] = {'max_energy_relative_error': maxE, 'max_modified_energy_drift': maxM, 'final_energy_fraction': H / H0, 'final_phase_error': phase - c['steps'] * h}
    checks['oscillator_forward_expected_growth'] = om['forward']['final_energy_fraction'] >= c['min_forward_energy_growth']
    checks['oscillator_backward_expected_decay'] = om['backward']['final_energy_fraction'] <= c['max_backward_energy_fraction']
    checks['symplectic_energy_band'] = om['symplectic']['max_energy_relative_error'] <= c['max_symplectic_energy_relative_error']
    checks['verlet_energy_band'] = om['verlet']['max_energy_relative_error'] <= c['max_verlet_energy_relative_error']
    checks['modified_oscillator_invariants'] = max((om[k]['max_modified_energy_drift'] for k in ['symplectic', 'verlet'])) <= c['max_modified_energy_relative_drift']
    defect = 0.0
    for method in ['symplectic', 'verlet']:
        x = oscillator_step(1.0, 0.0, h, method)
        y = oscillator_step(0.0, 1.0, h, method)
        defect = max(defect, abs(x[0] * y[1] - y[0] * x[1] - 1))
    checks['one_dof_symplectic_defect'] = defect <= c['max_symplectic_defect']
    metrics['oscillator'] = om
    rows['oscillator'] = (['method', 'time', 'q', 'p', 'energy_fraction', 'modified_energy_fraction', 'phase_error'], a)
    return (metrics, checks, rows)

def run(input_path, output):
    source = Path(input_path)
    config = json.loads(source.read_text())
    out = Path(output)
    if out.exists() and any(out.iterdir()):
        raise ValueError('new or empty output directory required')
    (m, c, rows) = experiment(config)
    out.mkdir(parents=True, exist_ok=True)
    for (name, (header, values)) in rows.items():
        with (out / (name + '.csv')).open('w', newline='') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(values)
    result = {'schema_version': 1, 'edition': config['edition'], 'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'metrics': m, 'checks': c, 'passed': all(c.values()), 'scope': 'Fixed small educational exercises; intentional unstable/low-order controls are checked as diagnostics, not accepted as accurate algorithms.'}
    (out / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    return result
if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', default='inputs.json')
    p.add_argument('--output', required=True)
    a = p.parse_args()
    r = run(a.input, a.output)
    print(json.dumps({'passed': r['passed'], 'checks': r['checks']}))
    raise SystemExit(0 if r['passed'] else 1)
