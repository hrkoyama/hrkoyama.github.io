#!/usr/bin/env python3
"""Freeze a new periodic-force edition after testing a separately extracted ZIP.

Existing editions are never changed. The payload stays in a temporary staging
folder until all packaged tests and the complete fixed-input runner pass.
"""
import argparse
import datetime
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FAILURE_TEST = 'test_scf_failure_is_not_a_usable_bo_force'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite_tree(value):
    if isinstance(value, dict):
        for item in value.values():
            finite_tree(item)
    elif isinstance(value, list):
        for item in value:
            finite_tree(item)
    elif isinstance(value, float):
        assert math.isfinite(value), 'Non-finite number in scientific result'


def read_json(path):
    value = json.loads(path.read_text())
    finite_tree(value)
    return value


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def compare_states(actual, expected):
    """Compare matched electronic states; never truncate mismatched atom lists."""
    assert len(actual) == len(expected) > 0
    energy_differences = []
    force_differences = []
    for observed, stored in zip(actual, expected):
        assert observed['converged'] and stored['converged']
        for key in ['positions_bohr', 'k_n', 'kpoints_fractional', 'kpoint_weights']:
            assert observed[key] == stored[key], key
        for key in ['ecut_hartree', 'basis', 'fft_mesh']:
            if key in observed or key in stored:
                assert observed[key] == stored[key], key
        energy_differences.append(abs(observed['energy_per_cell'] - stored['energy_per_cell']))
        fa, fb = observed['forces_cartesian'], stored['forces_cartesian']
        assert len(fa) == len(fb) == 2
        for xa, xb in zip(fa, fb):
            assert len(xa) == len(xb) == 3
            force_differences.extend(abs(a - b) for a, b in zip(xa, xb))
    delta, force_delta = max(energy_differences), max(force_differences)
    assert delta < 1e-8 and force_delta < 1e-7
    return delta, force_delta


def reference_states(reference):
    """Return all 8 cutoff and 16 displaced SCFs with their explicit identities."""
    cutoff = reference['cutoff_convergence']['records']
    assert len(cutoff) == 8
    assert [(r['k_n'], r['ecut_hartree']) for r in cutoff] == [
        (n, e) for n in [1, 2] for e in [90, 120, 180, 240]
    ]
    fd = reference['finite_difference']
    assert fd['summary']['target_reached'] and len(fd['records']) == 8
    keys, states = [], list(cutoff)
    for record in fd['records']:
        key = (record['atom_index'], record['component'], record['step_bohr'])
        keys.append(key)
        displaced = record['displaced_records']
        assert len(displaced) == 2
        assert displaced[0]['energy_per_cell'] == record['energy_minus']
        assert displaced[1]['energy_per_cell'] == record['energy_plus']
        states.extend(displaced)
    assert len(set(keys)) == 8 and len(states) == 24
    assert {(i, j) for i, j, h in keys if h == min(k[2] for k in keys)} == {
        (i, j) for i in range(2) for j in range(3)
    }
    return keys, states


def audit_reference(source, reference, regenerated_path):
    for key, name in [
        ('input_sha256', 'inputs.json'), ('script_sha256', 'reference.jl'),
        ('pseudopotential_sha256', 'He.gth'),
        ('project_sha256', 'reference-environment/Project.toml'),
        ('manifest_sha256', 'reference-environment/Manifest.toml'),
    ]:
        assert reference[key] == sha(source / name), key
    assert reference['engine'] == 'DFTK'
    assert reference['energy_unit'] == 'hartree/cell'
    assert reference['force_unit'] == 'hartree/bohr'
    assert reference['energy_offset_applied'] == reference['force_offset_applied'] == 0
    expected_keys, expected_states = reference_states(reference)
    verification = dict(
        file='reference-dftk.json', sha256=sha(source / 'reference-dftk.json'),
        engine='DFTK', engine_version=reference['engine_version'],
        julia_version=reference['julia_version'], package_versions=reference['package_versions'],
        regeneration='Separate pinned Julia workflow; see README-reference.txt',
        regenerated_before_freeze=False,
        cutoff_records=8, displaced_scf_records=16, total_scf_records=24,
        source_hashes={key: reference[key] for key in [
            'input_sha256', 'script_sha256', 'pseudopotential_sha256',
            'project_sha256', 'manifest_sha256',
        ]},
    )
    if regenerated_path:
        assert regenerated_path.resolve() != (source / 'reference-dftk.json').resolve()
        regenerated = read_json(regenerated_path)
        for key in [
            'cell', 'xc', 'input_sha256', 'script_sha256', 'pseudopotential_sha256',
            'project_sha256', 'manifest_sha256', 'engine', 'engine_version',
            'julia_version', 'package_versions', 'energy_unit', 'force_unit',
            'energy_offset_applied', 'force_offset_applied',
        ]:
            assert regenerated[key] == reference[key], key
        actual_keys, actual_states = reference_states(regenerated)
        assert actual_keys == expected_keys
        delta, force_delta = compare_states(actual_states, expected_states)
        verification.update(
            regenerated_before_freeze=True, regenerated_records=len(actual_states),
            regenerated_file_sha256=sha(regenerated_path),
            maximum_regenerated_energy_difference=delta,
            maximum_regenerated_force_difference=force_delta,
        )
    return verification


def test_counts(xml_path):
    cases = ET.parse(xml_path).getroot().findall('.//testcase')
    assert cases and any(c.attrib['name'] == FAILURE_TEST for c in cases)
    counts = dict(
        tests=len(cases),
        failures=sum(c.find('failure') is not None for c in cases),
        errors=sum(c.find('error') is not None for c in cases),
        skipped=sum(c.find('skipped') is not None for c in cases),
    )
    assert counts['failures'] == counts['errors'] == counts['skipped'] == 0
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--edition', required=True)
    parser.add_argument('--reference-regenerated', type=Path,
                        help='Separate regenerated Julia JSON; Julia is not a Python runtime dependency')
    args = parser.parse_args()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', args.edition):
        raise SystemExit('Invalid edition')
    source = ROOT / 'scripts/periodic-forces'
    base = ROOT / 'code/periodic-forces' / args.edition
    if base.exists():
        raise SystemExit('Edition already exists; never overwrite a published edition.')
    config = read_json(source / 'inputs.json')
    stored = read_json(source / 'results/result.json')
    reference = read_json(source / 'reference-dftk.json')
    assert stored['passed'] and stored['checks'] and all(stored['checks'].values())
    assert stored['input_sha256'] == sha(source / 'inputs.json')
    assert stored['reference_sha256'] == sha(source / 'reference-dftk.json')
    assert [r['id'] for r in stored['cases']] == [r['id'] for r in config['cases']]
    assert len({r['id'] for r in stored['cases']}) == len(config['cases'])
    reference_verification = audit_reference(source, reference, args.reference_regenerated)
    with tempfile.TemporaryDirectory(prefix='atlas-periodic-forces-package-') as td:
        temp = Path(td)
        payload = temp / 'payload'
        shutil.copytree(source, payload, ignore=shutil.ignore_patterns('__pycache__', '.pytest_cache'))
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'MPLCONFIGDIR': str(temp / 'mpl'),
               'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1'}
        files = {
            path.relative_to(payload).as_posix(): sha(path) for path in sorted(payload.rglob('*'))
            if path.is_file() and not any(
                s.startswith('.') or s == '__pycache__' for s in path.relative_to(payload).parts
            )
        }
        dump(payload / 'source-manifest.json', dict(
            schema_version=1, family='periodic-forces', edition=args.edition, files=files,
            public_base_url='https://hrkoyama.github.io/code/periodic-forces/' + args.edition + '/',
            terms={'original_driver': 'MIT / LICENSE', 'upstream_software_datasets': 'provenance.json',
                   'text_figures_data': 'https://hrkoyama.github.io/rights/'},
            scope=stored['scope'], implementation=stored['implementation'],
        ))
        archive = payload / ('periodic-forces-' + args.edition + '.zip')
        prefix = 'periodic-forces-' + args.edition + '/'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for name in sorted([*files, 'source-manifest.json']):
                info = zipfile.ZipInfo(prefix + name, date_time=(*map(int, args.edition[:10].split('-')), 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, (payload / name).read_bytes())
        with zipfile.ZipFile(archive) as z:
            assert set(z.namelist()) == {prefix + n for n in [*files, 'source-manifest.json']}
            for name, value in files.items():
                assert hashlib.sha256(z.read(prefix + name)).hexdigest() == value
            z.extractall(temp / 'extracted')
        extracted = temp / 'extracted' / prefix
        started = time.perf_counter()
        tests = subprocess.run(
            [sys.executable, '-m', 'pytest', '-q', '--junitxml=' + str(temp / 'tests.xml')],
            cwd=extracted, env=env, text=True, capture_output=True,
        )
        test_seconds = time.perf_counter() - started
        print(tests.stdout[-2000:], flush=True)
        if tests.returncode:
            print(tests.stderr)
            raise SystemExit(tests.returncode)
        counts = test_counts(temp / 'tests.xml')
        reproduced = temp / 'reproduced'
        started = time.perf_counter()
        subprocess.run([sys.executable, 'run.py', '--input', 'inputs.json', '--output', str(reproduced)],
                       cwd=extracted, env=env, check=True)
        runner_seconds = time.perf_counter() - started
        actual = read_json(reproduced / 'result.json')
        assert actual['passed'] and all(actual['checks'].values())
        assert actual['input_sha256'] == stored['input_sha256']
        assert actual['reference_sha256'] == stored['reference_sha256']
        assert [r['id'] for r in actual['cases']] == [r['id'] for r in stored['cases']]
        delta, force_delta = compare_states(actual['cases'], stored['cases'])
        dump(payload / 'verification.json', dict(
            schema_version=1, family='periodic-forces', edition=args.edition,
            verified_on=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date().isoformat(),
            archive_sha256=sha(archive), source_manifest_sha256=sha(payload / 'source-manifest.json'),
            execution='ZIP independently extracted; all packaged tests and the complete fixed-input Python runner executed without network or private source. Separate independent Julia reference regeneration is recorded below.',
            environment={x: importlib.metadata.version(x) for x in ['numpy', 'scipy', 'pytest', 'matplotlib', 'pyscf']},
            **counts, passed=counts['tests'],
            fixed_input=dict(
                id='periodic-he-forces', unique_cases=len(actual['cases']), passed=actual['passed'],
                metrics=actual['metrics'], maximum_reproduced_energy_difference=delta,
                maximum_reproduced_force_difference=force_delta, runtime_seconds=runner_seconds,
            ),
            independent_reference=reference_verification,
            failure_check=dict(
                test=FAILURE_TEST,
                result='An actual one-cycle SCF is rejected by the BO-force interface; unconverged electronic forces cannot advance nuclei.',
            ),
            test_runtime_seconds=test_seconds, scope=stored['scope'],
        ))
        # A failed test/run leaves no incomplete edition in the public tree.
        if base.exists():
            raise SystemExit('Edition appeared during verification; refusing to overwrite.')
        base.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(payload), str(base))
    print(json.dumps(dict(
        edition=args.edition, files=len(files), archive_bytes=(base / archive.name).stat().st_size,
        passed_tests=counts['tests'], cases=len(actual['cases']), runner_seconds=runner_seconds,
        metrics=actual['metrics'],
    )))


if __name__ == '__main__':
    main()
