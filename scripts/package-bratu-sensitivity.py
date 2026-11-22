#!/usr/bin/env python3
"""Freeze an explicitly supplied implicit/adjoint source into an immutable ZIP.

Pass an authored supplement directory as --source-root. An existing unfrozen
directory may be completed; an edition with a manifest/archive/receipt is never
overwritten. No private source path is recorded in the public release.
"""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FAMILY = 'bratu-sensitivity'
AUTHORED = ['README.md', 'LICENSE', 'LICENSING.md', 'requirements.txt',
    'numart/__init__.py', 'numart/autodiff.py', 'numart/krylov.py',
    'numart/bratu_sensitivity.py', 'scripts/build_bratu_sensitivity.py',
    'tests/test_bratu_sensitivity.py']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def package(source, edition):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', edition):
        raise ValueError('Use a dated edition, optionally followed by -rN')
    source = source.resolve()
    base = ROOT/'code'/FAMILY/edition
    archive_directory = FAMILY+'-'+edition
    if any((base/name).exists() for name in ['source-manifest.json', 'verification.json', archive_directory+'.zip']):
        raise ValueError('Edition is already frozen; choose a new revision')
    previous = ROOT/'code/autodiff/2026-11-22'
    unchanged = ['numart/autodiff.py', 'numart/krylov.py']
    original = {name: sha(previous/name) for name in unchanged}
    assert all(sha(source/name) == original[name] for name in unchanged)
    with tempfile.TemporaryDirectory(prefix='atlas-bratu-package-') as temporary:
        temporary = Path(temporary)
        staged = temporary/archive_directory
        staged.mkdir()
        for name in AUTHORED:
            (staged/name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source/name, staged/name)
        dump(staged/'provenance.json', dict(schema_version=1,
            unchanged_source_release='https://hrkoyama.github.io/code/autodiff/2026-11-22/',
            unchanged_source_sha256=original,
            adaptations=['Original AD and Armijo-Newton modules retained byte-for-byte.',
                'New implicit/discrete-adjoint helpers, exact-family references, tests and evidence builder.',
                'Minimal package initializer avoids unrelated solver imports.']))
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE':'1', 'MPLCONFIGDIR':str(temporary/'mpl')}
        built = subprocess.run([sys.executable, 'scripts/build_bratu_sensitivity.py'],
            cwd=staged, env=env, check=True, capture_output=True, text=True)
        print(built.stdout)
        files = {p.relative_to(staged).as_posix(): sha(p) for p in sorted(staged.rglob('*')) if p.is_file()}
        dump(staged/'source-manifest.json', dict(schema_version=1, family=FAMILY,
            edition=edition, version=edition,
            public_base_url='https://hrkoyama.github.io/code/'+FAMILY+'/'+edition+'/',
            files=files,
            scope='Smooth lower-branch Bratu implicit sensitivities and discrete adjoints; independent nonsymmetric multiparameter check.'))
        archive = staged/(archive_directory+'.zip')
        prefix = archive_directory+'/'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
            for name in sorted([*files, 'source-manifest.json']):
                info = zipfile.ZipInfo(prefix+name, (*map(int, edition[:10].split('-')), 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zipped.writestr(info, (staged/name).read_bytes())
        extracted = temporary/'extracted'
        with zipfile.ZipFile(archive) as zipped:
            assert set(zipped.namelist()) == {prefix+name for name in [*files, 'source-manifest.json']}
            for name, expected in files.items():
                assert hashlib.sha256(zipped.read(prefix+name)).hexdigest() == expected
            zipped.extractall(extracted)
        extracted /= archive_directory
        tested = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
            'tests/test_bratu_sensitivity.py', '--junitxml='+str(temporary/'tests.xml')],
            cwd=extracted, env=env, check=True, capture_output=True, text=True)
        print(tested.stdout)
        suite = ET.parse(temporary/'tests.xml').getroot().find('testsuite')
        counts = {name:int(suite.attrib[name]) for name in ['tests', 'failures', 'errors', 'skipped']}
        assert counts == dict(tests=9, failures=0, errors=0, skipped=0)
        subprocess.run([sys.executable, 'scripts/build_bratu_sensitivity.py'],
            cwd=extracted, env=env, check=True, capture_output=True, text=True)
        evidence_name = 'docs/figures/bratu-sensitivity.json'
        evidence = json.loads((staged/evidence_name).read_text())
        rebuilt = json.loads((extracted/evidence_name).read_text())
        assert evidence == rebuilt, 'Extracted package rebuilt different evidence'
        for name, expected in evidence['source_sha256'].items():
            assert sha(extracted/name) == expected
        archive_info = dict(file=archive.name, sha256=sha(archive),
            bytes=archive.stat().st_size, archive_directory=archive_directory)
        dump(staged/'verification.json', dict(schema_version=1, edition=edition,
            verified_on=edition[:10], archive_sha256=sha(archive), archive=archive_info,
            source_manifest_sha256=sha(staged/'source-manifest.json'),
            command='python -m pytest -q tests/test_bratu_sensitivity.py', returncode=0,
            summary='9 passed; independently extracted package rebuilt identical saved numerical evidence.',
            **counts, passed=9, passed_tests=9,
            environment={name:importlib.metadata.version(name) for name in ['numpy', 'matplotlib', 'pytest']},
            execution='ZIP independently extracted; dedicated tests and builder executed without source checkout or network.',
            rerun_checks=dict(all_source_hashes_match=True, numerical_evidence_identical=True,
                all_six_newton_roots_converged=all(r['converged'] for r in evidence['grid_runs']),
                primal_residuals_within_tolerance=all(r['primal_residual_l2'] <= evidence['settings']['newton_tolerance_l2'] for r in evidence['grid_runs']),
                nonsymmetric_gradient_check=evidence['nonsymmetric_check']['maximum_gradient_difference'] < 1e-12)))
        base.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staged, base, dirs_exist_ok=True)
    print(json.dumps(dict(edition=edition, base_url='https://hrkoyama.github.io/code/'+FAMILY+'/'+edition+'/', archive=archive_info, tests=counts), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--edition', default='2026-11-22')
    args = parser.parse_args()
    package(args.source_root, args.edition)
