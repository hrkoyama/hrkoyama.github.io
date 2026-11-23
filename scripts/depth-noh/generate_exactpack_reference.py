"""Reproduce an external analytic-reference check; never import the PDE solver.

Supply an isolated, unmodified source tree at the pinned LANL ExactPack commit.
Routine Atlas tests should compare the saved snapshot, not access the network.
"""
import argparse
import hashlib
import importlib
import json
import platform
from pathlib import Path
import sys

import numpy as np

COMMIT = '9bacc477eb791e959c9621e771fc7a725db755fa'
EXPECTED = {
    'exactpack/__init__.py': 'fac5c9e93253890cff33124da6e7ea5259f5bc171ce45574d43a171fc852d7ff',
    'exactpack/base.py': 'ce8e37ee0ed97dedca174a2ac0d8fa01b8b416bc3b441afab4e3bea9fe4f922e',
    'exactpack/solvers/__init__.py': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'exactpack/solvers/noh/__init__.py': '86315ecac0988d291bd9028276d7d693cc2288e47181330653efb83e72a17d5b',
    'exactpack/solvers/noh/noh1.py': 'bac597f501b021be85ef4956d0e075f1cdbff69aa72a3de788600f8c28e0d5a1',
    'LICENSE.txt': '763767e730623814502f95054919a019f17f5257e0cd8d60aede203d9736dd40',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generate(upstream, destination):
    upstream, destination = Path(upstream).resolve(), Path(destination).resolve()
    hashes = {name: digest(upstream / name) for name in EXPECTED}
    if hashes != EXPECTED:
        raise ValueError('ExactPack source bytes do not match the pinned reference')
    sys.path.insert(0, str(upstream))
    module = importlib.import_module('exactpack.solvers.noh.noh1')
    if Path(module.__file__).resolve() != upstream / 'exactpack/solvers/noh/noh1.py':
        raise ValueError('A different ExactPack installation was imported')
    import exactpack
    from noh_reference import point_values, cell_averages

    gamma, rho0, u0 = 5.0 / 3.0, 1.0, -1.0
    tolerance = 2e-12
    # Frozen positive probes and nonuniform shells exercise hot/cold/straddling
    # states. Quadrature splits at the upstream library's own shock metadata.
    radii = np.array([0.01, 0.025, 0.075, 0.145, 0.225, 0.45, 0.8])
    edges = np.array([0.0, 0.015, 0.055, 0.11, 0.175, 0.195,
                      0.205, 0.245, 0.39, 0.65, 1.0])
    times = [0.0, 0.15, 0.3, 0.6]
    nodes, weights = np.polynomial.legendre.leggauss(16)
    snapshot = {'schema_version': 1, 'reference': 'LANL ExactPack',
                'commit': COMMIT, 'parameters': {'gamma': gamma, 'rho0': rho0, 'u0': u0},
                'point_cases': [], 'cell_average_cases': []}
    errors = {'point_max_scaled': 0.0, 'conservative_cell_average_max_scaled': 0.0,
              'pressure_average_max_scaled': 0.0}

    def error(a, b):
        return float(np.max(np.abs(np.asarray(a) - np.asarray(b)) /
                            np.maximum(1.0, np.abs(np.asarray(b)))))

    for dimension in [1, 2, 3]:
        solver = module.Noh(geometry=dimension, gamma=gamma, rho0=rho0, u0=u0)
        for time in times:
            result = solver(radii, time)
            actual = np.column_stack([result[name] for name in
                                      ['density', 'velocity', 'pressure', 'specific_internal_energy']])
            own = np.column_stack(point_values(radii, time, dimension, gamma, rho0, u0))
            errors['point_max_scaled'] = max(errors['point_max_scaled'], error(own, actual))
            snapshot['point_cases'].append({'geometry': dimension, 'time': time,
                'radius': radii.tolist(), 'density': result['density'].tolist(),
                'radial_velocity': result['velocity'].tolist(), 'pressure': result['pressure'].tolist(),
                'specific_internal_energy': result['specific_internal_energy'].tolist()})
            shock = float(result.jumps[0])
            averages, pressures = [], []
            for left, right in zip(edges[:-1], edges[1:]):
                cuts = [left, right]
                if left < shock < right:
                    cuts.insert(1, shock)
                integrated = np.zeros(3)
                integrated_pressure = 0.0
                for start, end in zip(cuts[:-1], cuts[1:]):
                    r = (start + end) / 2.0 + (end - start) / 2.0 * nodes
                    external = solver(r, time)
                    rho, velocity = external['density'], external['velocity']
                    energy = rho * (external['specific_internal_energy'] + 0.5 * velocity**2)
                    values = np.column_stack((rho, rho * velocity, energy))
                    weighted = weights * r**(dimension - 1) * (end - start) / 2.0
                    integrated += np.sum(weighted[:, None] * values, axis=0)
                    integrated_pressure += float(np.sum(weighted * external['pressure']))
                volume = (right**dimension - left**dimension) / dimension
                averages.append(integrated / volume)
                pressures.append(integrated_pressure / volume)
            averages, pressures = np.asarray(averages), np.asarray(pressures)
            own_q, own_p = cell_averages(edges, time, dimension, gamma, rho0, u0)
            errors['conservative_cell_average_max_scaled'] = max(errors['conservative_cell_average_max_scaled'], error(own_q, averages))
            errors['pressure_average_max_scaled'] = max(errors['pressure_average_max_scaled'], error(own_p, pressures))
            snapshot['cell_average_cases'].append({'geometry': dimension, 'time': time,
                'edges': edges.tolist(), 'measure': 'r^(geometry-1) dr; angular factor omitted',
                'conserved_cell_averages': averages.tolist(), 'pressure_cell_averages': pressures.tolist()})

    # A recorded negative control explains the restriction, rather than
    # silently correcting or broadening the upstream implementation.
    nondefault = module.Noh(geometry=3, gamma=1.4, rho0=1.0, u0=-1.0)(np.array([0.03]), 0.6)
    eos_pressure = (1.4 - 1.0) * float(nondefault['density'][0]) * float(nondefault['specific_internal_energy'][0])
    snapshot['unsupported_gamma_diagnostic'] = {
        'gamma': 1.4, 'geometry': 3, 'reported_pressure': float(nondefault['pressure'][0]),
        'pressure_from_reported_density_and_energy_via_EOS': eos_pressure,
        'meaning': 'Upstream hard-coded pressure is inconsistent outside gamma=5/3; not an accepted general-gamma reference.'}

    destination.mkdir(parents=True, exist_ok=True)
    target = destination / 'exactpack-reference-snapshot.json'
    target.write_text(json.dumps(snapshot, indent=2, sort_keys=True, allow_nan=False) + '\n')
    receipt = {'schema_version': 1, 'reference_commit': COMMIT,
        'source_files_sha256': hashes, 'snapshot_sha256': digest(target),
        'reference_generator_sha256': digest(Path(__file__).resolve()),
        'local_analytic_reference_sha256': digest(Path(__file__).resolve().parent / 'noh_reference.py'),
        'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'exactpack': exactpack.__version__},
        'execution': 'Unmodified hash-checked upstream Noh module plus its package/base dependencies in an isolated source directory; no PDE solver import; no whole ExactPack test-suite claim.',
        'command': 'python generate_exactpack_reference.py --upstream /path/to/pinned-ExactPack --output /path/to/reference-output',
        'point_cases': len(snapshot['point_cases']), 'cell_average_cases': len(snapshot['cell_average_cases']),
        'scaled_error_definition': 'max(abs(local-external)/max(1,abs(external)))',
        'tolerance': tolerance, 'errors': errors,
        'checks': {key: value <= tolerance for key, value in errors.items()},
        'gamma_restriction_negative_control_detected': abs(float(nondefault['pressure'][0]) - eos_pressure) > 1.0,
        'scope': 'Reference implementation cross-check only. Radial geometry3 analytic checks are not a spherical PDE execution.'}
    receipt['passed'] = all(receipt['checks'].values()) and receipt['gamma_restriction_negative_control_detected']
    (destination / 'exactpack-reference-receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False) + '\n')
    print(json.dumps({'passed': receipt['passed'], 'errors': errors, 'commit': COMMIT}))
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--upstream', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    raise SystemExit(0 if generate(args.upstream, args.output)['passed'] else 1)
