#!/usr/bin/env python3
"""Run public ArviZ APIs on independently supplied arrays; import no atlas diagnostics."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata as metadata
import json
from pathlib import Path
import platform
import time
import warnings

import arviz as az
import numpy as np


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scalar(value):
    value = float(value)
    if np.isnan(value):
        return {'value': None, 'nonfinite_kind': 'nan'}
    if np.isposinf(value):
        return {'value': None, 'nonfinite_kind': 'positive_infinity'}
    if np.isneginf(value):
        return {'value': None, 'nonfinite_kind': 'negative_infinity'}
    return {'value': value, 'nonfinite_kind': None}


def generate(input_directory, source_directory, evidence_directory, output_path, install_report=None):
    assert az.__version__ == '0.20.0'
    assert not output_path.exists(), 'Do not overwrite an independently generated reference'
    manifest_path = input_directory/'manifest.json'
    archive_path = input_directory/'chains.npz'
    manifest = json.loads(manifest_path.read_text())
    assert manifest['schema_version'] == 1
    assert manifest['tail_probabilities'] == [.05, .95]
    assert digest(source_directory/'inputs.json') == manifest['input_sha256']
    for name, expected in manifest['source_sha256'].items():
        assert digest(source_directory/name) == expected, name
    public_calls = {
        'rhat_rank': lambda a: az.rhat(a, method='rank'),
        'rhat_z': lambda a: az.rhat(a, method='z_scale'),
        'rhat_folded': lambda a: az.rhat(a, method='folded'),
        'rhat_split': lambda a: az.rhat(a, method='split'),
        'ess_bulk': lambda a: az.ess(a, method='bulk'),
        'ess_tail': lambda a: az.ess(a, method='tail', prob=(.05, .95)),
        'ess_mean': lambda a: az.ess(a, method='mean'),
    }
    assert set(public_calls) == set(manifest['metrics'])
    lags = [0, 1, 2, 4, 8, 16, 32, 64]
    records = []
    started = time.perf_counter()
    with np.load(archive_path, allow_pickle=False) as arrays:
        for entry in manifest['datasets']:
            assert entry['observable'] in ['x', 'positive_indicator']
            values = arrays[entry['key']][:, :entry['prefix']]
            if entry['observable'] == 'positive_indicator':
                values = (values > 0).astype(float)
            values = np.array(values, dtype='<f8', order='C')
            assert list(values.shape) == entry['shape']
            assert np.isfinite(values).all()
            assert hashlib.sha256(values.tobytes(order='C')).hexdigest() == entry['sha256']
            assert values.shape[1] > max(lags)
            row = {**entry, 'metrics': {}, 'warnings': []}
            for name, call in public_calls.items():
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter('always')
                    row['metrics'][name] = scalar(call(values))
                row['warnings'].extend({'operation': name, 'category': w.category.__name__,
                                        'message': str(w.message)} for w in caught)
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter('always')
                autocorrelation = az.autocorr(values, axis=1)[:, lags]
            encoded = [[scalar(value) for value in chain] for chain in autocorrelation]
            row['acf'] = {'lags': lags,
                          'values': [[v['value'] for v in chain] for chain in encoded],
                          'nonfinite_kind': [[v['nonfinite_kind'] for v in chain] for chain in encoded]}
            row['warnings'].extend({'operation': 'autocorr', 'category': w.category.__name__,
                                    'message': str(w.message)} for w in caught)
            records.append(row)
    upstream = json.loads((evidence_directory/'arviz-upstream-source.json').read_text())
    package_root = Path(az.__file__).resolve().parent
    library_hashes = {name: digest(package_root/name) for name in upstream['files']}
    for name, actual in library_hashes.items():
        assert actual == upstream['files'][name]['upstream_sha256'], name
    package_names = ['arviz', 'numpy', 'scipy', 'matplotlib', 'pandas', 'xarray', 'h5netcdf',
                     'h5py', 'xarray-einstats', 'typing_extensions', 'pytz', 'tzdata',
                     'packaging', 'setuptools', 'python-dateutil']
    environment = {'arviz_version': az.__version__, 'platform': platform.platform(),
                   'python': platform.python_version(),
                   'dependencies': {name: metadata.version(name) for name in package_names},
                   'source_sha256': library_hashes}
    installs = json.loads(install_report.read_text()) if install_report else {'install': []}
    for item in installs['install']:
        assert metadata.version(item['metadata']['name']) == item['metadata']['version']
    result = {
        'schema_version': 1, 'reference': 'ArviZ', 'version': az.__version__,
        'provenance': {
            'generated_on': datetime.now(timezone.utc).date().isoformat(),
            'generated_at_utc': datetime.now(timezone.utc).isoformat(),
            'actually_executed': True,
            'generator_sha256': digest(Path(__file__)),
            'chain_encoding': manifest['chain_encoding'],
            'input_sha256': manifest['input_sha256'],
            'source_sha256': manifest['source_sha256'],
            'chain_manifest_sha256': digest(manifest_path),
            'chains_npz_sha256': digest(archive_path),
            'upstream': upstream,
            'environment': {k: environment[k] for k in
                            ['arviz_version', 'platform', 'python', 'dependencies', 'source_sha256']},
            'wheel_sources': [{'name': item['metadata']['name'],
                               'version': item['metadata']['version'],
                               'url': item['download_info']['url'],
                               'archive_info': item['download_info']['archive_info']}
                              for item in installs['install']],
            'wheel_report_provided_for_current_environment': install_report is not None,
            'numba_enabled': bool(az.Numba.numba_flag),
            'duration_seconds': time.perf_counter()-started,
            'independence': 'Only supplied array bytes and public ArviZ APIs are used. No atlas sampler or diagnostic code is imported.',
            'edge_policy': manifest['edge_policy'],
        },
        'datasets': records,
    }
    output_path.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'actually_executed': True, 'datasets': len(records),
                      'finite_metric_values': sum(m['nonfinite_kind'] is None for row in records
                                                 for m in row['metrics'].values()),
                      'nonfinite_metric_values': sum(m['nonfinite_kind'] is not None for row in records
                                                    for m in row['metrics'].values()),
                      'seconds': result['provenance']['duration_seconds'],
                      'reference_sha256': digest(output_path)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--install-report', type=Path,
                        help='Optional pip --report for this actual environment; never reuse another platform report')
    args = parser.parse_args()
    generate(args.input, args.sources, args.evidence, args.output, args.install_report)
