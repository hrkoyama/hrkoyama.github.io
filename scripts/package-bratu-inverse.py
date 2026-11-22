#!/usr/bin/env python3
"""Freeze the Bratu inverse supplement and independently verify its exact ZIP.

Existing frozen editions are never overwritten. Source paths and temporary
workspace paths are not recorded in the public release.
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
FAMILY = 'bratu-inverse'
AUTHORED = ['README.md', 'LICENSE', 'LICENSING.md', 'requirements.txt',
    'numart/__init__.py', 'numart/autodiff.py', 'numart/krylov.py',
    'numart/bratu_sensitivity.py', 'numart/bratu_inverse.py',
    'scripts/build_bratu_inverse.py', 'tests/test_bratu_inverse.py',
    'inputs/synthetic-observations.json']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def package(source, edition, temporary_root=None):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', edition):
        raise ValueError('Use a dated edition, optionally followed by -rN')
    source = source.resolve()
    base = ROOT/'code'/FAMILY/edition
    archive_directory = FAMILY+'-'+edition
    if any((base/name).exists() for name in ['source-manifest.json', 'verification.json', archive_directory+'.zip']):
        raise ValueError('Edition is already frozen; choose a new revision')
    previous = ROOT/'code/bratu-sensitivity/2026-11-22'
    unchanged = ['numart/autodiff.py', 'numart/krylov.py', 'numart/bratu_sensitivity.py']
    original = {name:sha(previous/name) for name in unchanged}
    assert all(sha(source/name) == original[name] for name in unchanged)
    if temporary_root is not None:
        temporary_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='atlas-inverse-package-', dir=temporary_root) as temporary:
        temporary = Path(temporary)
        staged = temporary/archive_directory
        staged.mkdir()
        for name in AUTHORED:
            (staged/name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source/name, staged/name)
        dump(staged/'provenance.json', dict(schema_version=1,
            unchanged_source_release='https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/',
            unchanged_source_sha256=original,
            adaptations=['Original AD, Armijo-Newton and implicit/adjoint modules retained byte-for-byte.',
                'New fixed-node observation operator, weighted least-squares objective and bounded adjoint-gradient optimizer.',
                'New fixed synthetic inputs, independent continuous-data refinement, objective-only reference, tests and evidence builder.',
                'Minimal initializer avoids unrelated solver imports.']))
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE':'1', 'MPLCONFIGDIR':str(temporary/'mpl')}
        built = subprocess.run([sys.executable, 'scripts/build_bratu_inverse.py'],
            cwd=staged, env=env, check=True, capture_output=True, text=True)
        print(built.stdout, end='')
        files = {p.relative_to(staged).as_posix():sha(p) for p in sorted(staged.rglob('*')) if p.is_file()}
        dump(staged/'source-manifest.json', dict(schema_version=1, family=FAMILY,
            edition=edition, version=edition,
            public_base_url='https://hrkoyama.github.io/code/'+FAMILY+'/'+edition+'/',
            files=files,
            scope='Bounded scalar lower-branch Bratu inverse estimation with discrete-adjoint projected Armijo optimization, fixed synthetic observations, independent continuous-data refinement and deterministic perturbations.'))
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
            'tests/test_bratu_inverse.py', '--junitxml='+str(temporary/'tests.xml')],
            cwd=extracted, env=env, check=True, capture_output=True, text=True)
        print(tested.stdout)
        suite = ET.parse(temporary/'tests.xml').getroot().find('testsuite')
        counts = {name:int(suite.attrib[name]) for name in ['tests', 'failures', 'errors', 'skipped']}
        passed = counts['tests']-counts['failures']-counts['errors']-counts['skipped']
        assert passed > 0 and counts['failures'] == counts['errors'] == counts['skipped'] == 0
        subprocess.run([sys.executable, 'scripts/build_bratu_inverse.py'],
            cwd=extracted, env=env, check=True, capture_output=True, text=True)
        evidence_name = 'docs/figures/bratu-inverse.json'
        evidence = json.loads((staged/evidence_name).read_text())
        rebuilt = json.loads((extracted/evidence_name).read_text())
        assert evidence == rebuilt, 'Extracted package rebuilt different numerical evidence'
        assert sha(staged/'docs/figures/bratu-inverse.png') == sha(extracted/'docs/figures/bratu-inverse.png'), 'Rebuilt figure differs'
        for name, expected in evidence['source_sha256'].items():
            assert sha(extracted/name) == expected
        fits = [*evidence['multistart'], *evidence['grid_runs'], evidence['noisy_run']]
        archive_info = dict(file=archive.name, sha256=sha(archive),
            bytes=archive.stat().st_size, archive_directory=archive_directory)
        dump(staged/'verification.json', dict(schema_version=1, edition=edition,
            verified_on=edition[:10], archive_sha256=sha(archive), archive=archive_info,
            source_manifest_sha256=sha(staged/'source-manifest.json'),
            command='python -m pytest -q tests/test_bratu_inverse.py', returncode=0,
            summary=f'{passed} passed; independently extracted package rebuilt identical numerical evidence and figure.',
            **counts, passed=passed, passed_tests=passed,
            environment={name:importlib.metadata.version(name) for name in ['numpy', 'matplotlib', 'pytest']},
            execution='ZIP independently extracted; dedicated tests and builder executed without source checkout or network.',
            rerun_checks=dict(all_source_hashes_match=True, numerical_evidence_identical=True,
                figure_identical=True,
                all_eight_adjoint_fits_converged=all(r['converged'] for r in fits),
                primal_residuals_within_tolerance=all(r['primal_residual_l2'] <= evidence['settings']['newton_tolerance_l2'] for r in fits),
                projected_gradients_within_tolerance=all(r['projected_gradient'] <= evidence['settings']['gradient_tolerance'] for r in fits),
                independent_parameter_refinement=all(1.9 < r['parameter_order'] < 2.1 for r in evidence['grid_runs'][1:]),
                objective_only_reference_agrees=all(r['reference_parameter_difference'] < 2e-8 for r in [*evidence['grid_runs'],evidence['noisy_run']]),
                boundary_only_zero_information=evidence['boundary_only_diagnostic']['observation_matrix_rank'] == 0)))
        base.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staged, base, dirs_exist_ok=True)
    print(json.dumps(dict(edition=edition, base_url='https://hrkoyama.github.io/code/'+FAMILY+'/'+edition+'/', archive=archive_info, tests=counts), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--edition', default='2026-11-22')
    parser.add_argument('--temporary-root', type=Path,
        help='Optional directory for all extraction, rebuild and test scratch data')
    args = parser.parse_args()
    package(args.source_root, args.edition, args.temporary_root)
