"""Offline verification of the beginner-course release, using Python 3.12 only."""
import csv
import hashlib
import json
import math
from pathlib import Path
import tempfile
import unittest
import lab

ROOT = Path(__file__).resolve().parent


def compare(a, b, rel, absolute, path=''):
    if isinstance(a, dict):
        assert a.keys() == b.keys(), path
        for key in a:
            compare(a[key], b[key], rel, absolute, path + '/' + key)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, rel, absolute, path + '/' + str(i))
    elif isinstance(a, (float, int)) and not isinstance(a, bool):
        assert math.isfinite(b) and math.isclose(a, b, rel_tol=rel, abs_tol=absolute), (path, a, b)
    else:
        assert a == b, (path, a, b)


def main():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    for name, digest in manifest['files'].items():
        p = ROOT / name
        assert p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(ROOT), name
        assert hashlib.sha256(p.read_bytes()).hexdigest() == digest, name
    suite = unittest.defaultTestLoader.discover(str(ROOT), pattern='test_lab.py')
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    assert result.wasSuccessful() and result.testsRun == 25
    config = json.loads((ROOT / 'inputs.json').read_text())
    tolerance = config['reproduction']
    with tempfile.TemporaryDirectory(prefix='foundations-verify-') as tmp:
        actual = lab.run(ROOT / 'inputs.json', Path(tmp))
        expected = json.loads((ROOT / 'results/result.json').read_text())
        compare(expected, actual, tolerance['relative_tolerance'], tolerance['absolute_tolerance'])
        for source in sorted((ROOT / 'results').glob('*.csv')):
            with source.open() as f, (Path(tmp) / source.name).open() as g:
                a = list(csv.reader(f)); b = list(csv.reader(g))
            assert len(a) == len(b) and a[0] == b[0], source.name
            for i, (left, right) in enumerate(zip(a[1:], b[1:])):
                assert len(left) == len(right)
                for x, y in zip(left, right):
                    try:
                        u, v = float(x), float(y)
                    except ValueError:
                        assert x == y
                    else:
                        compare(u, v, tolerance['relative_tolerance'], tolerance['absolute_tolerance'], source.name + ':' + str(i))
    receipt = {'passed': True, 'unit_tests': result.testsRun, 'acceptance_checks': len(actual['checks']), 'csv_files': 15, 'manifest_files': len(manifest['files']), 'comparison': tolerance}
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == '__main__':
    main()
