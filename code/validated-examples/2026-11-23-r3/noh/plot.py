#!/usr/bin/env python3
"""Standard plot driver: render saved Noh data, never execute a solver.

python plot.py --results results/result.json --output results

The compact verification result and its neighboring results.json describe the
same saved computation. See plot_noh.py --describe-input for profile semantics.
"""
import argparse
import hashlib
import json
from pathlib import Path

from plot_noh import render


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    summary = args.results.resolve()
    compact = json.loads(summary.read_text())
    if compact.get('passed') is not True:
        raise ValueError('Use an explicitly passed saved result; retain failed attempts separately')
    detailed = summary if summary.name == 'results.json' else summary.with_name('results.json')
    if not detailed.is_file():
        raise ValueError('Missing neighboring detailed results.json')
    output = args.output.resolve()
    manifest = render(detailed, output, geometry='cylindrical')
    rename = {'noh-preview': 'noh-shock-preview', 'noh-profiles': 'noh-shock',
              'noh-errors': 'noh-shock-errors'}
    for record in manifest['figures']:
        old = output / record['path']
        name = rename[old.stem] + old.suffix
        old.replace(output / name)
        record['path'] = name
    manifest['driver_source_sha256'] = {
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        summary.name: hashlib.sha256(summary.read_bytes()).hexdigest(),
    }
    manifest['primary_detail'] = 'noh-shock.png'
    manifest['gallery_preview'] = 'noh-shock-preview.png'
    manifest['additional_detail'] = 'noh-shock-errors.png'
    (output / 'figure-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'output': str(output), 'figures': [record['path'] for record in manifest['figures']]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
