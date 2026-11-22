"""Independent mpmath reference for supplied actual binary64 matrix/RHS payload.

No atlas source is imported. Run using a separate environment containing only
mpmath==1.3.0. The actual floats are reconstructed by integer ratios, not by
rounding their decimal renderings. SVD uses mpmath's bidiagonalization/QR;
least squares uses its separate high precision Householder implementation.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import inspect
import json
import math
from pathlib import Path
import platform
import struct
import sys

import mpmath as mp
from mpmath.matrices import eigen_symmetric, linalg


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_float(text):
    value = float.fromhex(text)
    if not math.isfinite(value):
        raise ValueError('nonfinite reference input')
    numerator, denominator = value.as_integer_ratio()
    return mp.mpf(numerator) / denominator


def read_array(payload):
    if math.prod(payload['shape']) != len(payload['hex']):
        raise ValueError('reference input shape does not match element count')
    raw = b''.join(struct.pack('<d', float.fromhex(x)) for x in payload['hex'])
    if hashlib.sha256(raw).hexdigest() != payload['sha256']:
        raise ValueError('reference input array SHA mismatch')
    flat = [exact_float(x) for x in payload['hex']]
    if len(payload['shape']) == 1:
        return mp.matrix(flat)
    rows, columns = payload['shape']
    return mp.matrix([flat[k*columns:(k+1)*columns] for k in range(rows)])


def strings(values, digits):
    return [mp.nstr(x, n=digits, strip_zeros=False) for x in values]


def solve_case(case, digits):
    with mp.workdps(digits):
        a, b, bp = (read_array(case['arrays'][key]) for key in ('matrix', 'rhs', 'perturbed_rhs'))
        singular = mp.svd(a, compute_uv=False)
        x, residual = mp.qr_solve(a, b)
        xp, residualp = mp.qr_solve(a, bp)
        return {'dps': digits, 'singular_values': strings(singular, digits), 'condition_2': mp.nstr(singular[0]/singular[len(singular)-1], digits), 'solution': strings(x, digits), 'perturbed_solution': strings(xp, digits), 'residual_norm': mp.nstr(residual, digits), 'perturbed_residual_norm': mp.nstr(residualp, digits)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--recipe', type=Path, required=True)
    parser.add_argument('--protocol', type=Path, required=True)
    parser.add_argument('--install-report', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    if sha(args.recipe) != payload['recipe_sha256'] or sha(args.protocol) != payload['input_sha256']:
        raise ValueError('recipe/protocol SHA mismatch')
    install = json.loads(args.install_report.read_text())['install']
    package = next(x for x in install if x['metadata']['name'] == 'mpmath')
    if mp.__version__ != '1.3.0' or package['metadata']['version'] != '1.3.0':
        raise ValueError('reference mpmath version must be 1.3.0')
    results = []
    with mp.workdps(140):
        for case in payload['datasets']:
            runs = [solve_case(case, digits) for digits in (80, 120)]
            max_difference = max(abs(mp.mpf(x)-mp.mpf(y)) for key in ('singular_values', 'solution', 'perturbed_solution') for x, y in zip(runs[0][key], runs[1][key]))
            sigma_ideal = [mp.mpf(2)**(-case['exponent']*k) for k in range(4)]
            sigma_error = max(abs(mp.mpf(x)-y)/y for x,y in zip(runs[-1]['singular_values'],sigma_ideal))
            assert max_difference < mp.mpf('1e-65'), (case['id'], max_difference)
            assert sigma_error < mp.mpf('1e-100'), (case['id'], sigma_error)
            # Independent Sylvester Hadamard construction, using exact fractions.
            h = [[1]]
            while len(h) < 16:
                h = [row+row for row in h] + [row+[-x for x in row] for row in h]
            h4 = [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]
            expected_matrix = [sum((Fraction(h[i][k],4)*Fraction(1,2**(case['exponent']*k))*Fraction(h4[j][k],2) for k in range(4)), Fraction(0)) for i in range(16) for j in range(4)]
            actual_matrix = [Fraction.from_float(float.fromhex(z)) for z in case['arrays']['matrix']['hex']]
            assert actual_matrix == expected_matrix, case['id']
            expected_base = [mp.mpf('0.5')]*4
            expected_perturbed = [mp.mpf('0.5') + mp.mpf(h4[i][-1])/2 * mp.mpf(2)**(3*case['exponent']-40) for i in range(4)]
            solution_error = max(abs(mp.mpf(x)-y) for key, expected in (('solution',expected_base),('perturbed_solution',expected_perturbed)) for x,y in zip(runs[-1][key],expected))
            assert solution_error < mp.mpf('1e-100'), (case['id'], solution_error)
            results.append({'exact_fraction_matrix_recipe_matches_actual_input': True, 'actual_input_vs_analytic_solution_max_absolute': mp.nstr(solution_error,30), 'id': case['id'], 'exponent': case['exponent'], 'array_sha256': {k: v['sha256'] for k,v in case['arrays'].items()}, 'runs': runs, 'precision_agreement_max_absolute': mp.nstr(max_difference, 30), 'actual_input_vs_ideal_sigma_max_relative': mp.nstr(sigma_error, 30)})
    result = {'schema_version': 1, 'generated_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'Actually executed independent mpmath 1.3.0 at 80/120 decimal digits on supplied actual binary64 matrix and RHS, four fixed full-rank 16x4 cases only. No atlas solver imported; no A.T@A used. High precision is generation-only, not a runtime dependency.', 'algorithms': {'svd': 'mpmath svd: Householder bidiagonalization and QR variant, separate from atlas cyclic one-sided Jacobi and LAPACK gesdd', 'least_squares': 'mpmath qr_solve: separate arbitrary precision Householder implementation; same mathematical QR family as atlas, not claimed a distinct QR family', 'conversion': 'float.fromhex -> as_integer_ratio -> arbitrary precision numerator/denominator'}, 'generator_sha256': sha(__file__), 'reference_input_sha256': sha(args.input), 'protocol_sha256': sha(args.protocol), 'fixture_recipe_sha256': sha(args.recipe), 'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation(), 'mpmath': mp.__version__, 'precision_dps': [80,120], 'wheel_url': package['download_info']['url'], 'wheel_archive_info': package['download_info']['archive_info'], 'implementation_source_sha256': {'mpmath/matrices/eigen_symmetric.py': sha(inspect.getfile(eigen_symmetric)), 'mpmath/matrices/linalg.py': sha(inspect.getfile(linalg))}}, 'results': results, 'all_reference_checks_passed': True}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'output': str(args.output), 'sha256': sha(args.output), 'cases': len(results), 'all_reference_checks_passed': True}))


if __name__ == '__main__':
    main()
