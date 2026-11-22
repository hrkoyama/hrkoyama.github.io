#!/usr/bin/env python3
"""Freeze original Yee-TMz sources, then test and rerun an independent ZIP extraction."""
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
SOURCES = ['solver.py', 'run.py', 'test_fdtd.py', 'README.md', 'LICENSE',
           'requirements.txt', 'inputs/periodic-wave.json', 'inputs/pec-cavity.json',
           'scattering.py', 'run_scattering.py', 'test_scattering.py',
           'inputs/dielectric-interface.json', 'inputs/pml-pulse.json',
           'corner.py', 'run_corner.py', 'test_corner.py', 'inputs/pml-corners.json',
           'oblique.py', 'run_oblique.py', 'test_oblique.py', 'inputs/dielectric-oblique.json']
CASES = ['periodic-wave', 'pec-cavity', 'dielectric-interface', 'pml-pulse', 'pml-corners', 'dielectric-oblique']
LEGACY = ['solver.py', 'run.py', 'test_fdtd.py', 'inputs/periodic-wave.json', 'inputs/pec-cavity.json',
          'scattering.py', 'run_scattering.py', 'test_scattering.py',
          'inputs/dielectric-interface.json', 'inputs/pml-pulse.json',
          'corner.py', 'run_corner.py', 'test_corner.py', 'inputs/pml-corners.json']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def package(edition):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', edition):
        raise ValueError('Use YYYY-MM-DD or YYYY-MM-DD-rN')
    target = ROOT/'code/fdtd'/edition
    if target.exists():
        raise ValueError('Edition exists; choose a new revision. Frozen editions are never overwritten.')
    prefix = 'fdtd-'+edition
    with tempfile.TemporaryDirectory(prefix='atlas-fdtd-package-') as temporary:
        temporary = Path(temporary)
        staged = temporary/prefix
        staged.mkdir()
        for name in SOURCES:
            (staged/name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/'scripts/fdtd'/name, staged/name)
        original = ROOT/'code/fdtd/2026-11-22-r3'
        unchanged = {name: sha(original/name) for name in LEGACY}
        assert all(sha(staged/name) == digest for name, digest in unchanged.items())
        dump(staged/'provenance.json', dict(schema_version=1,
            unchanged_source_release='https://hrkoyama.github.io/code/fdtd/2026-11-22-r3/',
            unchanged_source_sha256=unchanged,
            additions=['Original oblique dielectric-interface Fresnel packet examples.',
                       'Previous vacuum, interface and PML solvers, all five inputs and tests retained byte-for-byte.']))
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'MPLBACKEND': 'Agg',
               'MPLCONFIGDIR': str(temporary/'mpl'), 'OPENBLAS_NUM_THREADS': '1',
               'OMP_NUM_THREADS': '1'}

        def run_case(directory, case, output):
            runner = ('run_oblique.py' if case == 'dielectric-oblique' else
                      'run_corner.py' if case == 'pml-corners' else
                      'run.py' if case in CASES[:2] else 'run_scattering.py')
            proc = subprocess.run([sys.executable, runner, '--input', 'inputs/'+case+'.json',
                                   '--output', str(output)], cwd=directory, env=env,
                                  check=True, capture_output=True, text=True)
            result = json.loads((output/'result.json').read_text())
            assert result['passed'] and result['checks'], (case, proc.stdout)
            assert (output/'summary.png').is_file()
            return result

        for case in CASES:
            print('Generate fixed input: '+case, flush=True)
            run_case(staged, case, staged/'results'/case)
        files = {p.relative_to(staged).as_posix(): sha(p) for p in sorted(staged.rglob('*'))
                 if p.is_file() and '__pycache__' not in p.parts}
        dump(staged/'source-manifest.json', dict(schema_version=1, family='fdtd', edition=edition,
            version=edition, public_base_url='https://hrkoyama.github.io/code/fdtd/'+edition+'/',
            files=files, scope='Original educational Yee TMz scheme: retained vacuum/interface/x-PML cases and four-side/corner-PML and oblique Fresnel checks; see per-input assumptions.'))
        archive = staged/(prefix+'.zip')
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
            for name in sorted([*files, 'source-manifest.json']):
                info = zipfile.ZipInfo(prefix+'/'+name, (*map(int, edition[:10].split('-')), 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zipped.writestr(info, (staged/name).read_bytes())
        extracted = temporary/'extracted'
        with zipfile.ZipFile(archive) as zipped:
            assert set(zipped.namelist()) == {prefix+'/'+n for n in [*files, 'source-manifest.json']}
            for name, expected in files.items():
                assert hashlib.sha256(zipped.read(prefix+'/'+name)).hexdigest() == expected
            zipped.extractall(extracted)
        extracted /= prefix
        proc = subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
            'test_fdtd.py', 'test_scattering.py', 'test_corner.py', 'test_oblique.py', '--junitxml='+str(temporary/'tests.xml')], cwd=extracted,
            env=env, capture_output=True, text=True, check=True)
        print(proc.stdout, flush=True)
        suite = ET.parse(temporary/'tests.xml').getroot().find('testsuite')
        counts = {k: int(suite.attrib[k]) for k in ['tests', 'failures', 'errors', 'skipped']}
        assert counts['tests'] > 0 and counts['failures'] == counts['errors'] == counts['skipped'] == 0
        recipes = []
        for case in CASES:
            print('Reproduce extracted ZIP input: '+case, flush=True)
            output = temporary/('rerun-'+case)
            result = run_case(extracted, case, output)
            original = json.loads((staged/'results'/case/'result.json').read_text())
            assert result['metrics'] == original['metrics'], case
            assert result['checks'] == original['checks'], case
            for path in (staged/'results'/case).glob('*.csv'):
                name = path.name
                assert sha(output/name) == sha(staged/'results'/case/name), (case, name)
            assert result['input_sha256'] == sha(extracted/'inputs'/(case+'.json'))
            recipes.append(dict(id=case, passed=True, input_sha256=result['input_sha256'],
                metrics_identical=True, csv_identical=True))
        archive_info = dict(file=archive.name, sha256=sha(archive), bytes=archive.stat().st_size,
                            archive_directory=prefix)
        dump(staged/'verification.json', dict(schema_version=1, edition=edition,
            verified_on=edition[:10], archive=archive_info, archive_sha256=sha(archive),
            source_manifest_sha256=sha(staged/'source-manifest.json'), returncode=0,
            **counts, passed_tests=counts['tests'], passed=counts['tests'], recipes=recipes,
            environment={n: importlib.metadata.version(n) for n in ['numpy', 'matplotlib', 'pytest']},
            execution='ZIP independently extracted; all tests and all six fixed-input cases rerun without network or private source; numerical metrics and CSVs matched exactly.',
            reference='Continuum vacuum modes, Fresnel interface solution, analytic/spectral packet references and independently evaluated discrete energy/work/flux identities. See corner and oblique inputs for their reference scopes. No independent external FDTD solver comparison claimed.'))
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staged, target)
    print(json.dumps(dict(edition=edition, archive=archive_info, tests=counts, recipes=recipes), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--edition', required=True)
    package(parser.parse_args().edition)
