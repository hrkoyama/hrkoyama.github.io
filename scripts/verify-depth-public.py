#!/usr/bin/env python3
# Generated from scripts/templates/verify-depth-public.py.tmpl; edit that template.
"""Verify reviewed lightweight public ZIPs without a source checkout.

Only the Python standard library is used by this verifier. The current Python
must already contain the three pinned scientific/test dependencies. No quantum
code, plot regeneration, automatic installation or Git operation is performed.
"""
import argparse
import csv
import datetime
import hashlib
import importlib.metadata
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import platform
import re
import signal
import stat
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

ORIGIN = 'https://hrkoyama.github.io'
REGISTRY_URL = ORIGIN + '/numerical-methods-atlas/validation/releases.json'
GROUPS = ('foundations', 'models', 'particles', 'mhd', 'thermostats', 'biology', 'mcmc', 'mhd-convergence', 'foundations-conditioning', 'particle-transport', 'splitting', 'noh', 'noh-cartesian', 'sedov', 'double-mach', 'forward-step', 'low-mach', 'guderley', 'euler-positivity', 'zalesak', 'weno-critical', 'shallow-water', 'wall-flow', 'level-set', 'sem-fr', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'coefficient-diffusion', 'slab-ewald', 'fmm3d', 'gravity-dynamics', 'warm-pic', 'pic-spatial', 'dsmc-wall', 'dsmc-shock', 'lbm-cavity', 'lbm-taylor-green', 'lbm-annulus', 'lbm-curved-boundary', 'radiation-scattering', 'radiation-matter', 'radiation-geometry', 'stochastic-accuracy', 'stochastic-estimation', 'maxwell-cylinder', 'maxwell-lorentz', 'maxwell-grazing', 'linear-algebra-spectral', 'bratu-continuation-jfnk', 'globalization-controls', 'reverse-higher-ad', 'adjoint', 'inverse-optimization', 'ode-adaptivity', 'steady-rk', 'dae-controls', 'geometric-controls')
DIRECT_PINS = {'numpy': '2.0.2', 'scipy': '1.14.1', 'pytest': '8.3.5'}
GROUP_TIMEOUT_SECONDS = 120
MAX_DOWNLOAD_BYTES = 64 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 128 * 1024 * 1024
MAX_ARCHIVE_MEMBERS = 1000
SHA_PATTERN = r'[0-9a-f]{64}'
EDITION_PATTERN = r'\d{4}-\d{2}-\d{2}(?:-r\d+)?'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def strict_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'Duplicate JSON key')
            result[key] = value
        return result
    def invalid(value):
        raise ValueError('Nonfinite JSON constant')
    result = json.loads(data, object_pairs_hook=pairs, parse_constant=invalid)
    check_finite(result)
    return result


def check_finite(value):
    if isinstance(value, float):
        require(math.isfinite(value), 'Nonfinite numeric value')
    elif isinstance(value, dict):
        for child in value.values():
            check_finite(child)
    elif isinstance(value, list):
        for child in value:
            check_finite(child)


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def safe_relative(name):
    require(isinstance(name, str) and name and len(name) <= 240, 'Invalid archive relative path')
    require(re.fullmatch(r'[A-Za-z0-9_./-]+', name) is not None, 'Unsafe archive path characters')
    path = PurePosixPath(name)
    require(not path.is_absolute() and '..' not in path.parts and path.as_posix() == name,
            'Unsafe or noncanonical archive path')
    return name


def validate_url(url):
    require(isinstance(url, str), 'Public URL must be a string')
    parsed = urllib.parse.urlsplit(url)
    require(parsed.scheme == 'https' and parsed.netloc == 'hrkoyama.github.io', 'Unsupported public origin')
    require(not parsed.query and not parsed.fragment and '%' not in parsed.path and '\\' not in parsed.path,
            'Noncanonical public URL')
    require(parsed.path.startswith('/') and '//' not in parsed.path and
            '..' not in PurePosixPath(parsed.path).parts and
            PurePosixPath(parsed.path).as_posix() + ('/' if parsed.path.endswith('/') and parsed.path != '/' else '') == parsed.path,
            'Unsafe public URL path')
    return url


def validate_registry_url(url):
    validate_url(url)
    require(url == REGISTRY_URL, 'Unexpected lightweight registry URL')
    return url


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        raise ValueError('Public downloads must not redirect')


def download(url, expected_sha256, acquisitions, kind):
    validate_url(url)
    require(re.fullmatch(SHA_PATTERN, expected_sha256 or '') is not None, 'Invalid expected SHA-256')
    record = {'kind': kind, 'url': url, 'expected_sha256': expected_sha256, 'passed': False}
    acquisitions.append(record)
    try:
        opener = urllib.request.build_opener(NoRedirect())
        request = urllib.request.Request(url, headers={'User-Agent': 'Atlas-lightweight-public-verifier/1.0'})
        with opener.open(request, timeout=60) as response:
            require(getattr(response, 'status', 200) == 200, 'Public download did not return HTTP 200')
            data = response.read(MAX_DOWNLOAD_BYTES + 1)
        require(len(data) <= MAX_DOWNLOAD_BYTES, 'Public download exceeds size limit')
        record.update(bytes=len(data), sha256=digest(data))
        require(record['sha256'] == expected_sha256, 'Public SHA-256 mismatch: ' + kind)
        record['passed'] = True
        return data
    except Exception as error:
        record['error'] = {'type': type(error).__name__, 'message': str(error)}
        raise


def validate_registry(registry):
    require(isinstance(registry, dict) and type(registry.get('schema_version')) is int and
            registry['schema_version'] == 1, 'Unsupported registry schema')
    edition = registry.get('edition')
    require(isinstance(edition, str) and re.fullmatch(EDITION_PATTERN, edition), 'Invalid edition')
    releases = registry.get('releases')
    require(isinstance(releases, list) and len(releases) == len(GROUPS), 'Exactly the reviewed release groups are required')
    require([r.get('group') for r in releases] == list(GROUPS), 'Unexpected or duplicate release group/order')
    all_cases = []
    for release in releases:
        group = release['group']
        release_edition = release.get('edition')
        require(isinstance(release_edition, str) and re.fullmatch(EDITION_PATTERN, release_edition),
                'Invalid release edition')
        base = ORIGIN + '/code/validated-examples/' + release_edition + '/' + group + '/'
        require(release.get('base') == base, 'Release base is outside its reviewed prefix')
        validate_url(base)
        require(release.get('archive') == 'atlas-' + group + '-' + release_edition + '.zip', 'Unexpected archive name')
        for key in ['archive_sha256', 'manifest_sha256', 'verification_sha256', 'requirements_sha256']:
            require(re.fullmatch(SHA_PATTERN, release.get(key, '')) is not None, 'Invalid release SHA-256: ' + key)
        ids = release.get('case_ids')
        require(isinstance(ids, list) and ids and len(ids) == len(set(ids)) and
                all(isinstance(i, str) and re.fullmatch(r'[a-z][a-z0-9-]+', i) for i in ids), 'Invalid case IDs')
        require(type(release.get('tests')) is int and release['tests'] > 0, 'Invalid expected pytest count')
        all_cases.extend(ids)
    require(len(all_cases) == len(set(all_cases)), 'Case IDs repeated across release groups')
    require(type(registry.get('case_count')) is int and registry['case_count'] == len(all_cases) and len(all_cases) > 0,
            'Registry case count differs from its pinned release inventory')
    return releases


def validate_requirements(data):
    expected = {name + '==' + version for name, version in DIRECT_PINS.items()}
    lines = [line.strip() for line in data.decode('utf-8').splitlines() if line.strip()]
    require(len(lines) == len(expected) and set(lines) == expected,
            'Release requirements must contain only the three reviewed direct pins')


def validate_result(result, expected_ids, input_sha256, termination):
    check_finite(result)
    require(isinstance(result, dict) and type(result.get('schema_version')) is int and
            result['schema_version'] == 1, 'Unsupported result schema')
    require(result.get('passed') is True, 'Scientific result did not pass')
    require(result.get('input_sha256') == input_sha256, 'Executed input SHA-256 mismatch')
    require(isinstance(termination, str) and termination and result.get('termination') == termination,
            'Missing or changed completion reason')
    checks = result.get('checks')
    require(isinstance(checks, dict) and set(checks) == set(expected_ids) and all(v is True for v in checks.values()),
            'Top-level case decisions are incomplete or failed')
    cases = result.get('cases')
    require(isinstance(cases, list) and len(cases) == len(expected_ids) and
            {c.get('id') for c in cases} == set(expected_ids), 'Executed case IDs differ from registry')
    for case in cases:
        require(case.get('passed') is True and isinstance(case.get('checks'), dict) and case['checks'] and
                all(v is True for v in case['checks'].values()), 'Case numerical checks did not pass')
        require(isinstance(case.get('metrics'), dict) and case['metrics'], 'Missing case metrics')
        require(isinstance(case.get('records'), (list, dict)) and case['records'], 'Missing refinement records')
    return cases


def verify_archive(payload, manifest, receipt, requirements, release, destination):
    """Check exact members and hashes before writing any file to the extraction tree."""
    group, edition = release['group'], release['edition']
    require(manifest.get('family') == 'depth-' + group and manifest.get('group') == group and
            manifest.get('version') == edition and manifest.get('public_base_url') == release['base'],
            'Manifest identity differs from registry')
    require(set(manifest.get('case_ids', [])) == set(release['case_ids']) and
            len(manifest['case_ids']) == len(release['case_ids']), 'Manifest case IDs differ')
    files = manifest.get('files')
    require(isinstance(files, dict) and files, 'Missing manifest file map')
    required = {'run.py', 'inputs.json', 'cases.json', 'requirements.txt', 'README.md', 'LICENSE', 'results/result.json'}
    require(required <= set(files), 'Missing required manifest files')
    for name, checksum in files.items():
        safe_relative(name)
        require(re.fullmatch(SHA_PATTERN, checksum or '') is not None, 'Invalid member SHA-256')
    require('source-manifest.json' not in files and 'verification.json' not in files and release['archive'] not in files,
            'Manifest must not recursively include itself, receipt or archive')
    require(any(PurePosixPath(name).name.startswith('test_') and name.endswith('.py') for name in files),
            'No packaged scientific tests')
    require(receipt.get('group') == group and receipt.get('edition') == edition and receipt.get('passed') is True and
            receipt.get('all_cases_rerun') is True, 'Release receipt did not pass')
    require(receipt.get('source_manifest_sha256') == release['manifest_sha256'], 'Receipt manifest SHA differs')
    require(type(receipt.get('tests')) is int and type(receipt.get('passed_tests')) is int and
            receipt['tests'] == receipt['passed_tests'] == release['tests'],
            'Receipt pytest count differs from registry')
    require(all(type(receipt.get(key)) is int and receipt[key] == 0
                for key in ['returncode', 'failures', 'errors', 'skipped']),
            'Stored scientific tests failed or skipped')
    require(set(receipt.get('case_ids', [])) == set(release['case_ids']) and
            len(receipt['case_ids']) == len(release['case_ids']), 'Receipt case IDs differ')
    prefix = 'atlas-' + group + '-' + edition
    archive = receipt.get('archive', {})
    require(archive.get('file') == release['archive'] and archive.get('archive_directory') == prefix and
            archive.get('bytes') == len(payload) and archive.get('sha256') == release['archive_sha256'] == digest(payload),
            'Archive receipt identity/size/hash differs')
    if 'archive_sha256' in receipt:
        require(receipt['archive_sha256'] == digest(payload), 'Changed receipt archive SHA')
    require(files['requirements.txt'] == release['requirements_sha256'] == digest(requirements),
            'Requirements file differs between registry/manifest/download')
    validate_requirements(requirements)
    destination = Path(destination)
    require(not destination.exists(), 'Extraction directory must be new')
    expected_names = {prefix + '/' + name for name in [*files, 'source-manifest.json']}
    with zipfile.ZipFile(io.BytesIO(payload)) as zipped:
        members = zipped.infolist()
        require(len(members) <= MAX_ARCHIVE_MEMBERS and len(members) == len({m.filename for m in members}),
                'Too many or duplicate ZIP members')
        require({m.filename for m in members} == expected_names, 'ZIP member set differs from manifest')
        require(sum(m.file_size for m in members) <= MAX_UNCOMPRESSED_BYTES, 'Expanded ZIP exceeds size limit')
        for member in members:
            safe_relative(member.filename)
            require(not member.is_dir() and not member.flag_bits & 1, 'Directory/encrypted ZIP member rejected')
            require(stat.S_IFMT(member.external_attr >> 16) in (0, stat.S_IFREG), 'Symlink/special ZIP member rejected')
            require(member.file_size <= MAX_DOWNLOAD_BYTES, 'ZIP member exceeds size limit')
            data = zipped.read(member)
            relative = member.filename[len(prefix) + 1:]
            expected = release['manifest_sha256'] if relative == 'source-manifest.json' else files[relative]
            require(digest(data) == expected, 'ZIP member SHA-256 mismatch: ' + relative)
        # Reopening members is intentional: all safety and integrity checks finish first.
        for member in members:
            target = destination / member.filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(zipped.read(member))
    return destination / prefix


def inspect_environment():
    versions = {}
    for name in DIRECT_PINS:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return {'python': platform.python_version(), 'operating_system': platform.system(),
            'machine': platform.machine(), 'dependencies': versions,
            'source_checkout_required': False, 'plot_regeneration': False}


def clean_environment(temporary):
    Path(temporary).mkdir(parents=True, exist_ok=True)
    environment = {'PATH': str(Path(sys.executable).parent) + os.pathsep + os.defpath,
                   'PYTHONNOUSERSITE': '1', 'PYTHONDONTWRITEBYTECODE': '1',
                   'PYTEST_DISABLE_PLUGIN_AUTOLOAD': '1', 'OPENBLAS_NUM_THREADS': '1',
                   'OMP_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1', 'TMPDIR': str(temporary)}
    for name in ['LANG', 'LC_ALL', 'SYSTEMROOT']:
        if name in os.environ:
            environment[name] = os.environ[name]
    return environment


def run_process(command, cwd, log_directory, name, environment, timeout):
    """Preserve streaming logs and kill the whole POSIX process group on timeout."""
    require(timeout > 0, 'Group execution budget exhausted')
    logs = Path(log_directory)
    logs.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    record = {'command': command, 'started': True, 'completed': False, 'timed_out': False,
              'exit_code': None, 'stdout': name + '.stdout.log', 'stderr': name + '.stderr.log'}
    with (logs / record['stdout']).open('wb') as stdout, (logs / record['stderr']).open('wb') as stderr:
        process = subprocess.Popen(command, cwd=cwd, env=environment, stdout=stdout, stderr=stderr,
                                   start_new_session=os.name == 'posix')
        try:
            record['exit_code'] = process.wait(timeout=timeout)
            record['completed'] = True
        except subprocess.TimeoutExpired:
            record['timed_out'] = True
            if os.name == 'posix':
                os.killpg(process.pid, signal.SIGKILL)
            else:
                process.kill()
            process.wait()
    record['duration_seconds'] = time.monotonic() - started
    return record


def check_junit(path, expected_tests):
    tree = ET.parse(path).getroot()
    cases = list(tree.iter('testcase'))
    require(len(cases) == expected_tests, 'Executed pytest count differs from registry')
    for node in tree.iter():
        require(node.tag not in ('failure', 'error', 'skipped'), 'Executed pytest failed or skipped')
        for key in ('failures', 'errors', 'skipped'):
            if key in node.attrib:
                require(int(node.attrib[key]) == 0, 'JUnit reports failures/errors/skips')
    return {'tests': len(cases), 'failures': 0, 'errors': 0, 'skipped': 0}


def check_generated_csv(directory):
    files = sorted(Path(directory).glob('*.csv'))
    require(files, 'No generated CSV outputs')
    records = []
    for path in files:
        with path.open(newline='') as handle:
            rows = list(csv.reader(handle))
        require(len(rows) >= 2 and rows[0] and len(rows[0]) == len(set(rows[0])), 'Empty or ambiguous generated CSV')
        for row in rows[1:]:
            require(len(row) == len(rows[0]), 'Ragged generated CSV')
            for value in row:
                try:
                    number = float(value)
                except ValueError:
                    continue
                require(math.isfinite(number), 'Nonfinite generated CSV value')
        records.append({'file': path.name, 'bytes': path.stat().st_size, 'sha256': digest(path.read_bytes())})
    return records


def verify(registry_url, expected_registry_sha256, output_dir):
    output = Path(output_dir).resolve()
    require(not output.exists() or (output.is_dir() and not any(output.iterdir())), 'Choose a new or empty output directory')
    output.mkdir(parents=True, exist_ok=True)
    report = {'schema_version': 1, 'started_at_utc': utc_now(), 'registry_url': registry_url,
              'expected_registry_sha256': expected_registry_sha256, 'registry_sha256': None,
              'status': 'running', 'phase': 'registry', 'passed': False,
              'source_checkout': False, 'environment': {}, 'acquisitions': [], 'groups': []}
    active = None
    def save():
        write_json(output / 'report.json', report)
    save()
    try:
        validate_registry_url(registry_url)
        registry_bytes = download(registry_url, expected_registry_sha256, report['acquisitions'], 'registry')
        report['registry_sha256'] = digest(registry_bytes)
        registry = strict_json(registry_bytes)
        releases = validate_registry(registry)
        write_json(output / 'registry.json', registry)
        prepared = []
        for release in releases:
            group = release['group']
            active = {'group': group, 'passed': False, 'status': 'preparing', 'case_ids': release['case_ids'],
                      'expected_tests': release['tests']}
            report['groups'].append(active)
            report['active_group'] = group
            report['phase'] = 'downloads'
            save()
            directory = output / 'groups' / group
            directory.mkdir(parents=True, exist_ok=True)
            payloads = {}
            for name, key in [('source-manifest.json', 'manifest_sha256'), ('verification.json', 'verification_sha256'),
                              ('requirements.txt', 'requirements_sha256'), (release['archive'], 'archive_sha256')]:
                payloads[name] = download(release['base'] + name, release[key], report['acquisitions'], group + ':' + name)
                (directory / name).write_bytes(payloads[name])
                save()
            manifest = strict_json(payloads['source-manifest.json'])
            receipt = strict_json(payloads['verification.json'])
            report['phase'] = 'archive-validation'
            save()
            extracted = verify_archive(payloads[release['archive']], manifest, receipt, payloads['requirements.txt'],
                                       release, directory / 'extracted')
            stored = strict_json((extracted / 'results/result.json').read_bytes())
            validate_result(stored, release['case_ids'], manifest['files']['inputs.json'], stored.get('termination'))
            metadata = strict_json((extracted / 'cases.json').read_bytes())
            metadata = metadata['cases'] if isinstance(metadata, dict) else metadata
            require(isinstance(metadata, list) and len(metadata) == len(release['case_ids']) and
                    {case.get('id') for case in metadata} == set(release['case_ids']), 'Metadata case IDs differ')
            active['status'] = 'prepared'
            active['archive_sha256'] = release['archive_sha256']
            active['manifest_sha256'] = release['manifest_sha256']
            prepared.append((release, extracted, stored, directory, manifest))
            save()
        report['phase'] = 'environment'
        save()
        report['environment'] = inspect_environment()
        save()
        require(report['environment']['dependencies'] == DIRECT_PINS,
                'Current environment differs from the three reviewed pins')
        for release, extracted, stored, directory, manifest in prepared:
            active = next(g for g in report['groups'] if g['group'] == release['group'])
            report['active_group'] = release['group']
            active['status'] = 'testing'
            deadline = time.monotonic() + GROUP_TIMEOUT_SECONDS
            environment = clean_environment(directory / 'temporary')
            report['phase'] = 'pytest'
            save()
            junit = directory / 'pytest.xml'
            command = [sys.executable, '-W', 'error', '-m', 'pytest', '-q', '-p', 'no:cacheprovider',
                       '--junitxml=' + str(junit.resolve())]
            active['pytest_process'] = run_process(command, extracted, directory, 'pytest', environment,
                                                  deadline - time.monotonic())
            save()
            p = active['pytest_process']
            require(p['completed'] and not p['timed_out'] and p['exit_code'] == 0, 'Packaged pytest did not complete successfully')
            report['phase'] = 'pytest-validation'
            save()
            active['pytest'] = check_junit(junit, release['tests'])
            report['phase'] = 'fixed-input-integrity'
            save()
            for name, expected in manifest['files'].items():
                require(digest((extracted / name).read_bytes()) == expected,
                        'Packaged tests changed a fixed release member: ' + name)
            report['phase'] = 'execution'
            active['status'] = 'executing'
            save()
            generated = directory / 'generated'
            command = [sys.executable, '-W', 'error', 'run.py', '--input', 'inputs.json', '--output', str(generated.resolve())]
            active['run_process'] = run_process(command, extracted, directory, 'run', environment,
                                               deadline - time.monotonic())
            save()
            p = active['run_process']
            require(p['completed'] and not p['timed_out'] and p['exit_code'] == 0, 'Fixed-input runner did not complete successfully')
            report['phase'] = 'numerical-validation'
            save()
            result = strict_json((generated / 'result.json').read_bytes())
            require(digest((extracted / 'inputs.json').read_bytes()) == manifest['files']['inputs.json'],
                    'Runner changed its reviewed fixed input')
            cases = validate_result(result, release['case_ids'], manifest['files']['inputs.json'], stored['termination'])
            expected_checks = {case['id']: set(case['checks']) for case in stored['cases']}
            require(all(set(case['checks']) == expected_checks[case['id']] for case in cases),
                    'Executed numerical checks differ from the frozen decisions')
            active['generated_csv'] = check_generated_csv(generated)
            active['cases'] = cases
            active['result_sha256'] = digest((generated / 'result.json').read_bytes())
            active['passed'] = True
            active['status'] = 'passed'
            save()
        report.update(status='complete', phase='complete', passed=True,
                      case_count=sum(len(g['cases']) for g in report['groups']),
                      tests=sum(g['pytest']['tests'] for g in report['groups']))
        report.pop('active_group', None)
    except Exception as error:
        report.update(status='failed', passed=False, error={'phase': report['phase'],
                      'type': type(error).__name__, 'message': str(error)})
        if active is not None:
            active.update(status='failed', passed=False)
    report['finished_at_utc'] = utc_now()
    save()
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', required=True)
    parser.add_argument('--expected-registry-sha256', required=True)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    try:
        report = verify(args.registry, args.expected_registry_sha256, args.output_dir)
    except Exception as error:
        print(json.dumps({'passed': False, 'phase': 'output-preflight', 'error': type(error).__name__, 'message': str(error)}), file=sys.stderr)
        return 2
    print(json.dumps({key: report[key] for key in ['passed', 'status', 'phase']}))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
