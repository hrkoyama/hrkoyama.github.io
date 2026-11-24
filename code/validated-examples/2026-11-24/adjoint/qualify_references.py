"""Reference-only fixed67checks; no primary state/time/VJP solver import."""
import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import json
from pathlib import Path
import signal
import time
import numpy as np
from references.modal_decimal import modes, pi, pi_remainder, strings, sine
from references.shooting_decimal import fold, lower_state, independent_newton, discrete_residual, positive_pivots, thomas
from references.linear_oracle import solve
from io_contract import fresh_directory, save_json, digest


def close_decimal(a, b, tolerance=D('1e-35')):
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(close_decimal(x, y, tolerance) for x, y in zip(a, b))
    return abs(a-b) <= tolerance*max(D(1), abs(b))


def nonsymmetric_fraction():
    M = [[F(3, 4), F(1, 8)], [F(-1, 4), F(1, 2)]]
    b, u, theta, d = [F(1, 4), F(1)], [F(1), F(-1, 2)], F(1, 2), [F(1, 8), F(-1, 4)]
    tangent = [F(0), F(0)]
    def mv(A, x):
        return [sum(a*y for a, y in zip(row, x)) for row in A]
    for _ in range(4):
        u = [x+theta*y for x, y in zip(mv(M, u), b)]
        tangent = [x+y for x, y in zip(mv(M, tangent), b)]
    p = [x-y for x, y in zip(u, d)]
    forward = sum(x*y for x, y in zip(p, tangent))
    adjoint = F(0)
    MT = [list(row) for row in zip(*M)]
    for _ in range(4):
        adjoint += sum(x*y for x, y in zip(p, b))
        p = mv(MT, p)
    wrong_p = [x-y for x, y in zip(u, d)]
    wrong = F(0)
    for _ in range(4):
        wrong += sum(x*y for x, y in zip(wrong_p, b))
        wrong_p = mv(M, wrong_p)
    # Independently composed affine map: derivative sum_{j=0}^3 M^j*b.
    power, total = b[:], [F(0), F(0)]
    for _ in range(4):
        total = [x+y for x, y in zip(total, power)]
        power = mv(M, power)
    return forward == adjoint and tangent == total and wrong != forward


def qualify(source, output):
    source, output = Path(source), fresh_directory(output)
    started = time.monotonic()
    config = json.loads((source/'inputs.json').read_text())
    plan = json.loads((source/'reference-qualification-plan.json').read_text())
    expected = [row['id'] for row in plan['checks']]
    checks, audit, time_cache, fold_cache = {}, {}, {}, {'folds': {}, 'points': {}}
    report = {'schema_version': 1, 'passed': False, 'checks': checks,
              'input_sha256': digest(source/'inputs.json'),
              'acceptance_sha256': digest(source/'acceptance.json'),
              'source_sha256': {name: digest(source/name) for name in
                 ['references/modal_decimal.py', 'references/shooting_decimal.py',
                  'references/linear_oracle.py', 'qualify_references.py',
                  'reference-qualification-plan.json', 'io_contract.py']},
              'cache_sha256': {}, 'failure': None}

    def save():
        save_json(output/'qualification.json', report)

    def add(name, value):
        if name not in expected or name in checks:
            raise ValueError('Unknown/duplicate reference check: '+name)
        checks[name] = bool(value)
        save()

    def raw(name, value):
        save_json(output/name, strings(value))

    def stop(_signal, _frame):
        raise TimeoutError('Reference qualification terminated')

    old_handler = signal.signal(signal.SIGTERM, stop)
    save()
    try:
        with localcontext() as context:
            context.prec = 110
            p50, p80 = pi(50), pi(80)
            raw('pi.json', {'50': p50, '80': p80, 'analytic_alternating_remainder_bound': pi_remainder(),
                            'bound_formula': '16/(401*5^401)+4/(401*239^401); truncation only,not total rounding enclosure'})
            add('62-pi-precision', abs(p50-p80) <= D('1e-40'))
            c = config['cases']['diffusion-discrete-adjoint']
            for n in c['n']:
                first = None
                for N in c['steps']:
                    audit.update(stage='modal', n=n, steps=N)
                    raw('current-reference.json', audit)
                    low = modes(n, N, c['kappa'], c['theta'], c['T'], 50)
                    raw(f'modal-n{n}-N{N}-50.json', low)
                    high = modes(n, N, c['kappa'], c['theta'], c['T'], 80)
                    raw(f'modal-n{n}-N{N}-80.json', high)
                    time_cache[f'n{n}-N{N}'] = strings(high)
                    if first is None:
                        first = high
                        h = D(1)/(n+1)
                        B = high['basis']
                        orthogonal = all(abs(h*sum(row[j]*row[k] for row in B)-(D('.5') if j == k else 0)) <= D('1e-35')
                                         for j in range(3) for k in range(3))
                        eigen = True
                        for j in range(3):
                            column = [row[j] for row in B]
                            for k, value in enumerate(column):
                                lap = (2*value-(column[k-1] if k else 0)-(column[k+1] if k+1 < n else 0))/(h*h)
                                eigen &= abs(lap-high['eigenvalues'][j]*value) <= D('1e-35')
                        add(f'62-n{n}-sine-orthogonality', orthogonal and all(r['next_term_bound'] <= D('1e-90') for r in high['sine_tails']))
                        add(f'62-n{n}-discrete-eigenrelation', eigen)
                    add(f'62-n{n}-N{N}-precision-state-objective-gradient',
                        close_decimal(low['field'], high['field']) and close_decimal(low['gradient'], high['gradient']) and close_decimal(low['objective'], high['objective']))
                    add(f'62-n{n}-N{N}-closed-vs-recurrence-state', close_decimal(high['coefficients'][-1], high['closed']))
                    add(f'62-n{n}-N{N}-closed-vs-recurrence-gradient', close_decimal(high['gradient'], high['closed_gradient']))
                add(f'62-n{n}-semidiscrete-exact', close_decimal(low['time_exact_field'], high['time_exact_field']) and close_decimal(high['time_exact_coefficients'], high['time_exact_series_coefficients']) and all(r['remainder_bound'] <= D('1e-90') for r in high['expm1_series_tails']))
            add('62-nonsymmetric-Fraction', nonsymmetric_fraction())
            c = config['cases']['bratu-fold-sensitivity']
            for n in c['n']:
                audit.update(stage='fold', n=n)
                raw('current-reference.json', audit)
                low_fold = fold(n, 50, audit)
                raw(f'fold-n{n}-50.json', low_fold)
                high_fold = fold(n, 80, audit)
                raw(f'fold-n{n}-80.json', high_fold)
                fold_cache['folds'][str(n)] = strings(high_fold)
                add(f'63-n{n}-fold-precision', close_decimal(low_fold['lambda'], high_fold['lambda']) and close_decimal(low_fold['a'], high_fold['a']))
                add(f'63-n{n}-fold-anchor', abs(high_fold['lambda']-D(c['stored_discrete_anchor_decimal'][str(n)])) <= D('1e-10'))
                add(f'63-n{n}-fold-fold-residuals', max(abs(high_fold['R']), abs(high_fold['Ra'])) <= D('1e-40'))
                add(f'63-n{n}-fold-nondegenerate', high_fold['determinant'] != 0)
                profile = high_fold['profile'][1:-1]
                add(f'63-n{n}-fold-positive-symmetric-profile', min(profile) > 0 and close_decimal(profile, profile[::-1]))
                for i, decimal_lambda in enumerate(c['lambda_decimal'][str(n)]):
                    value = float(decimal_lambda)
                    lam = D.from_float(value)
                    audit.update(stage='lower-state', n=n, index=i, lam=lam)
                    raw('current-reference.json', audit)
                    low = lower_state(n, lam, low_fold['a'], 50, audit)
                    raw(f'lower-n{n}-i{i}-50.json', low)
                    high = lower_state(n, lam, high_fold['a'], 80, audit)
                    raw(f'lower-n{n}-i{i}-80.json', high)
                    secondary = independent_newton(n, lam, 80, audit)
                    raw(f'Thomas-n{n}-i{i}-80.json', {'u': secondary})
                    fold_cache['points'][f'n{n}-point{i}'] = {**strings(high), 'lambda_hex': value.hex()}
                    add(f'63-n{n}-point{i}-precision-state-gradient', close_decimal(low['u'], high['u']) and close_decimal(low['gradient'], high['gradient']))
                    add(f'63-n{n}-point{i}-shooting-vs-Thomas', close_decimal(high['u'], secondary))
                    add(f'63-n{n}-point{i}-stencil-residual', max(abs(x) for x in discrete_residual(high['u'], lam)) <= D('1e-40'))
                    add(f'63-n{n}-point{i}-positive-lower-branch', min(high['u']) > 0 and close_decimal(high['u'], high['u'][::-1]) and positive_pivots(high['u'], lam))
            one = fold(1, 80, audit)
            raw('fold-n1-exact-control.json', one)
            add('63-exact-discrete-n1-fold', close_decimal(one['a'], D(1)) and close_decimal(one['lambda'], D(8)/D(1).exp()))
            for label, n, diagonal_value, lower_value, upper_value in [
                    ('n7-SPD-dyadic', 7, D(4), D(-1), D(-1)),
                    ('n7-nonsymmetric-dyadic', 7, D(4), D(-1), D(-2)),
                    ('n31-shifted-Poisson', 31, D(2)+D(1)/32, D(-1), D(-1))]:
                diagonal, lower, upper = [diagonal_value]*n, [lower_value]*(n-1), [upper_value]*(n-1)
                rhs = [D(i+1)/(n+1) for i in range(n)]
                for transpose, tag in [(False, 'tangent'), (True, 'adjoint')]:
                    exact = thomas(upper if transpose else lower, diagonal,
                                   lower if transpose else upper, rhs)
                    raw_name = 'linear-'+label+'-'+tag+'.json'
                    raw(raw_name, {'reference': exact})
                    candidate = solve(np.array(diagonal, dtype=float), np.array(lower, dtype=float),
                                      np.array(upper, dtype=float), np.array(rhs, dtype=float), transpose)
                    raw(raw_name, {'reference': exact, 'candidate': candidate.tolist()})
                    values = [D.from_float(float(x)) for x in candidate]
                    left, right = (upper, lower) if transpose else (lower, upper)
                    residual = [diagonal[k]*values[k]+(left[k-1]*values[k-1] if k else 0)+(right[k]*values[k+1] if k+1 < n else 0)-rhs[k] for k in range(n)]
                    raw(raw_name, {'reference': exact, 'candidate': candidate.tolist(), 'actual_residual_components': residual,
                                   'actual_residual_max_abs': max(abs(x) for x in residual),
                                   'residual_arithmetic': 'Independent Decimal evaluation at the actual float candidate; dyadic matrix/RHS exact.'})
                    error = max(abs(D.from_float(float(x))-y) for x, y in zip(candidate, exact))
                    add('linear-'+label+'-'+tag, error <= D('2e-11')*max(D(1), max(abs(x) for x in exact)) and max(abs(x) for x in residual) <= D('2e-11')*max(D(1), max(abs(x) for x in rhs)))
        if list(sorted(checks)) != list(sorted(expected)) or len(checks) != 67:
            raise AssertionError('Actual reference inventory must be exactly67')
        raw('cache-time.json', {'format': 1, 'records': time_cache})
        raw('cache-fold.json', {'format': 1, **fold_cache})
        report['cache_sha256'] = {name: digest(output/name) for name in ['cache-time.json', 'cache-fold.json']}
        report['passed'] = all(checks.values())
    except BaseException as error:
        raw('failed-current-reference.json', audit)
        report['failure'] = {'type': type(error).__name__, 'message': str(error)}
    finally:
        report['duration_seconds'] = time.monotonic()-started
        save()
        signal.signal(signal.SIGTERM, old_handler)
    return report


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source', type=Path, default=Path(__file__).resolve().parent)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = qualify(a.source, a.output)
    print(json.dumps({'passed': result['passed'], 'checks': len(result['checks']), 'duration': result['duration_seconds']}))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
