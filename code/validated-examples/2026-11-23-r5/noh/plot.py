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
    parser.add_argument('--comparison-results', type=Path,
                        help='Optional retained failed arithmetic-stress detailed results.json')
    parser.add_argument('--secondary-comparison-results', type=Path,
                        help='Optional retained failed linear-stress/constant detailed results.json for MUSCL comparison')
    args = parser.parse_args()
    summary = args.results.resolve()
    compact = json.loads(summary.read_text())
    if compact.get('passed') is not True:
        raise ValueError('Use an explicitly passed saved result; retain failed attempts separately')
    detailed = summary if summary.name == 'results.json' else summary.with_name('results.json')
    if not detailed.is_file():
        raise ValueError('Missing neighboring detailed results.json')
    detail = json.loads(detailed.read_text())
    if detail.get('passed') is not True:
        raise ValueError('The neighboring detailed result did not pass; use the diagnostic renderer separately')
    if summary != detailed:
        receipts = detail.get('receipts', {})
        if (not compact.get('input_sha256') or compact['input_sha256'] != receipts.get('input_sha256')
                or compact.get('source_receipts') != receipts):
            raise ValueError('Compact and detailed results have different input/source receipts')
        cases = compact.get('cases', [])
        case_id = detail.get('case_id')
        if (not case_id or {case.get('id') for case in cases} != {case_id}
                or any(case.get('passed') is not True for case in cases)
                or compact.get('checks', {}).get(case_id) is not True):
            raise ValueError('Compact and detailed case identities or pass decisions disagree')
    output = args.output.resolve()
    manifest = render(detailed, output, comparison_results=args.comparison_results,
                      secondary_comparison_results=args.secondary_comparison_results)
    if manifest['validation_passed'] is not True:
        raise ValueError('Refusing to publish-named figures from a failed detailed result')
    rename = {'noh-preview': 'noh-shock-preview', 'noh-profiles': 'noh-shock',
              'noh-errors': 'noh-shock-errors'}
    for record in manifest['figures']:
        old = output / record['path']
        name = rename.get(old.stem, old.stem) + old.suffix
        old.replace(output / name)
        record['path'] = name
    manifest['driver_source_sha256'] = {
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        summary.name: hashlib.sha256(summary.read_bytes()).hexdigest(),
    }
    manifest['primary_detail'] = 'noh-shock.png'
    manifest['gallery_preview'] = 'noh-shock-preview.png'
    manifest['additional_detail'] = 'noh-shock-errors.png'
    manifest['additional_details'] = ['noh-shock-errors.png']
    if manifest['plot_reductions']['spherical_budget']:
        manifest['additional_details'].append('noh-spherical-budget.png')
    (output / 'figure-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'output': str(output), 'figures': [record['path'] for record in manifest['figures']]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
