#!/usr/bin/env python3
"""Freeze and independently verify a minimal forward-AD/Bratu supplement.

This command only creates a new immutable release. The private source root is
an explicit input and is never recorded as an absolute path in public files.
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


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def package(source, edition):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', edition):
        raise ValueError('Use a dated edition, optionally followed by -rN')
    base = ROOT / 'code/autodiff' / edition
    if base.exists():
        raise ValueError('Edition already exists; use a new revision. No overwriting.')
    source = source.resolve()
    archive_directory = 'autodiff-'+edition
    original_files = ['numart/autodiff.py', 'numart/krylov.py',
                      'scripts/build_autodiff.py', 'tests/test_autodiff.py', 'LICENSE']
    original_hashes = {name: sha(source/name) for name in original_files}
    base.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='atlas-ad-package-') as temp:
        temp = Path(temp)
        staged = temp / archive_directory
        staged.mkdir()
        for name in original_files:
            (staged/name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source/name, staged/name)
        (staged/'numart/__init__.py').write_text('"""Minimal numerical methods atlas AD/Bratu supplement."""\n')
        builder = staged/'scripts/build_autodiff.py'
        text = builder.read_text()
        if text.count("'tests/test_sparse_fem.py'") != 1:
            raise ValueError('Unexpected original builder source-list format')
        text = text.replace("'tests/test_sparse_fem.py'", "'tests/test_autodiff.py'")
        text = text.replace('The Bratu discretization and parameter match tests/test_sparse_fem.py;',
            'The Bratu discretization and parameter match the original sparse/Newton verification;')
        builder.write_text(text)
        (staged/'requirements.txt').write_text('numpy>=1.24\nmatplotlib>=3.7\npytest>=7\n')
        (staged/'LICENSING.md').write_text('''# License scope

Original implementation code in numart/, scripts/ and tests/ is MIT licensed;
retain LICENSE when redistributing it. The code was extracted from the numerical
methods atlas with its original copyright notice.

Explanatory text, plots and saved datasets have separate terms. A software
license does not automatically license its generated output. See
https://hrkoyama.github.io/rights/ for the public content policy. This notice
claims no exclusive rights over unprotected facts, mathematics or ideas.

NumPy, Matplotlib, pytest and Python are external dependencies with their own
licenses. They are not redistributed in this archive.
''')
        (staged/'README.md').write_text('''# Forward automatic differentiation and Bratu verification

Supplemental source edition: '''+edition+'''. Public chapter:
Japanese: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/
English: https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/

This self-contained NumPy example compares an analytic Jacobian, finite
differences and genuine forward automatic differentiation on the same Bratu
residual. It includes the existing damped Newton solver and a minimal package
initializer. The only builder adaptation replaces the original broad-suite test
hash with the packaged dedicated test hash. provenance.json records the original
input hashes. No source checkout or network is needed after dependencies exist.

## Reproduce

Requires Python 3.9 or later. From the extracted directory:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q tests/test_autodiff.py
MPLCONFIGDIR=.mplconfig python scripts/build_autodiff.py
```

Outputs: docs/figures/autodiff-bratu.json and autodiff-bratu.png. The JSON records
all source hashes, derivative checks, finite-difference sweeps and nine Newton
runs. The residual is -u_xx-lambda exp(u)=0 on [0,1], with zero Dirichlet boundary
data, lambda=2/cosh(1/2)^2 and 15/31/63 interior nodes. Each method starts at zero,
uses the same dense Armijo-Newton solver and stops at absolute residual 2-norm
1e-10. Central differences in Newton use absolute perturbation 1e-5. Separate
forward/central sweeps run from 1 down to 1e-14.

This implements one-direction forward AD, with one seed per Jacobian column.
Reverse mode, implicit sensitivity, adaptive integrator differentiation and
nonsmooth shock sensitivities are outside this package. No performance ranking
is claimed. Discrete-root agreement and second-order spatial error are checked
separately. Last-bit rounding can depend on NumPy and the host platform.

source-manifest.json hashes every payload file and is also inside the ZIP.
verification.json is published beside the archive and records its SHA-256,
independent extracted-package test results and the numerical rebuild check.
Code and content have distinct terms; see LICENSE and LICENSING.md.
''')
        dump(staged/'provenance.json', dict(schema_version=1,
            source_label='Numerical methods atlas local AD supplement',
            original_source_sha256=original_hashes,
            adaptations=['Minimal numart/__init__.py avoids unrelated solver imports.',
                'Builder source hash list uses tests/test_autodiff.py instead of the omitted broad-suite tests/test_sparse_fem.py.',
                'Builder scope describes that original validation without an unavailable package path.'],
            unchanged_code=['numart/autodiff.py', 'numart/krylov.py', 'tests/test_autodiff.py']))
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE':'1', 'MPLCONFIGDIR':str(temp/'mpl')}
        build = subprocess.run([sys.executable, 'scripts/build_autodiff.py'], cwd=staged,
            env=env, check=True, capture_output=True, text=True)
        print(build.stdout)
        files = {p.relative_to(staged).as_posix(): sha(p) for p in sorted(staged.rglob('*')) if p.is_file()}
        dump(staged/'source-manifest.json', dict(schema_version=1, family='autodiff',
            edition=edition, version=edition,
            public_base_url='https://hrkoyama.github.io/code/autodiff/'+edition+'/',
            files=files, scope='Minimal forward AD and three-derivative Bratu verification; no general reverse-mode or sensitivity solver.'))
        archive = staged/(archive_directory+'.zip')
        prefix = archive_directory+'/'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for name in sorted([*files, 'source-manifest.json']):
                info = zipfile.ZipInfo(prefix+name, (*map(int, edition[:10].split('-')), 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, (staged/name).read_bytes())
        extracted = temp/'extracted'
        with zipfile.ZipFile(archive) as z:
            assert set(z.namelist()) == {prefix+name for name in [*files, 'source-manifest.json']}
            for name, expected in files.items():
                assert hashlib.sha256(z.read(prefix+name)).hexdigest() == expected
            z.extractall(extracted)
        extracted /= archive_directory
        test_command = [sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
                        'tests/test_autodiff.py', '--junitxml='+str(temp/'tests.xml')]
        tested = subprocess.run(test_command, cwd=extracted, env=env, check=True,
                                capture_output=True, text=True)
        print(tested.stdout)
        suite = ET.parse(temp/'tests.xml').getroot().find('testsuite')
        counts = {name:int(suite.attrib[name]) for name in ['tests','failures','errors','skipped']}
        assert counts == dict(tests=8, failures=0, errors=0, skipped=0)
        subprocess.run([sys.executable, 'scripts/build_autodiff.py'], cwd=extracted,
                        env=env, check=True, capture_output=True, text=True)
        evidence_path = 'docs/figures/autodiff-bratu.json'
        evidence = json.loads((staged/evidence_path).read_text())
        rebuilt = json.loads((extracted/evidence_path).read_text())
        assert evidence == rebuilt, 'Rebuilt numerical evidence differs from saved result'
        for name, expected in evidence['source_sha256'].items():
            assert sha(extracted/name) == expected
        archive_info = dict(file=archive.name, sha256=sha(archive),
            bytes=archive.stat().st_size, archive_directory=archive_directory)
        dump(staged/'verification.json', dict(schema_version=1, edition=edition,
            verified_on=edition[:10], archive_sha256=sha(archive),
            source_manifest_sha256=sha(staged/'source-manifest.json'), archive=archive_info,
            command='python -m pytest -q tests/test_autodiff.py', returncode=0,
            summary='8 passed; independently extracted package rebuilt identical saved numerical evidence.',
            **counts, passed=8, passed_tests=8,
            environment={name:importlib.metadata.version(name) for name in ['numpy','matplotlib','pytest']},
            execution='ZIP independently extracted; dedicated tests and builder executed without private source or network.',
            rerun_checks=dict(all_source_hashes_match=True, numerical_evidence_identical=True,
                all_nine_newton_runs_converged=all(r['converged'] for r in evidence['newton_runs']),
                all_residuals_within_tolerance=all(r['final_residual_l2'] <= evidence['settings']['newton_tolerance_l2'] for r in evidence['newton_runs']))))
        shutil.copytree(staged, base)
    print(json.dumps(dict(edition=edition, base_url='https://hrkoyama.github.io/code/autodiff/'+edition+'/',
                          archive=archive_info, tests=counts), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--edition', default='2026-11-22')
    args = parser.parse_args()
    package(args.source_root, args.edition)
