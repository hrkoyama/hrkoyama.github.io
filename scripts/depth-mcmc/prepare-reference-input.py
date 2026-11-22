#!/usr/bin/env python3
"""Prepare fixed actual chains for an independently installed reference library.

Only sampler.py and fixtures.py are imported; no local diagnostics implementation.
The compressed archive is temporary; per-array hashes bind the public reference.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from sampler import Budget, array_sha256, sample_chains
from fixtures import edge_fixtures

HERE = Path(__file__).resolve().parent


def prepare(output):
    output = Path(output)
    if output.exists() and any(output.iterdir()):
        raise ValueError('Use a new or empty reference-input directory')
    payload = (HERE/'inputs.json').read_bytes()
    config = json.loads(payload)
    c = config['cases']['mcmc-multimodal-mixing']['sampler']
    arrays, entries = {}, []
    budget = Budget(config['maximum_total_seconds'])
    for scenario in c['scenarios']:
        for seed in c['seeds']:
            key = f'{scenario}__{seed}'
            x = sample_chains(c, scenario, seed, budget)[0]
            arrays[key] = x
            for n in c['budgets']:
                for observable in ['x', 'positive_indicator']:
                    values = x[:, :n] if observable == 'x' else (x[:, :n] > 0).astype(float)
                    entries.append({'id': f'{key}__{n}__{observable}', 'key': key, 'prefix': n,
                                    'observable': observable, 'sha256': array_sha256(values), 'shape': list(values.shape)})
    for name, x in edge_fixtures().items():
        key = 'edge__'+name;arrays[key] = x
        entries.append({'id': key, 'key': key, 'prefix': x.shape[1], 'observable': 'x',
                        'sha256': array_sha256(x), 'shape': list(x.shape)})
    manifest = {'schema_version': 1,
                'chain_encoding': 'little-endian float64 C-order bytes; SHA256 excludes NPZ headers',
                'input_sha256': hashlib.sha256(payload).hexdigest(),
                'source_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ['sampler.py','fixtures.py']},
                'datasets': entries,
                'metrics': ['rhat_rank','rhat_z','rhat_folded','rhat_split','ess_bulk','ess_tail','ess_mean'],
                'tail_probabilities': [.05,.95],
                'edge_policy': 'Record raw ArviZ constant/nonfinite values with status, never nonfinite JSON. Atlas reports undefined zero-global-variance diagnostics rather than using the ArviZ constant-ESS raw-count convention as evidence of mixing.'}
    output.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(output/'chains.npz', **arrays)
    (output/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'arrays': len(arrays), 'datasets': len(entries), 'input_directory': str(output.resolve())}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument('--output', required=True)
    prepare(parser.parse_args().output)
