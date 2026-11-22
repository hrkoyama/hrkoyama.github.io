#!/usr/bin/env python3
"""Verify public code examples with an existing Python; never install packages.

The optional artifact directory retains logs and partial outputs, including failed
groups. A local --registry remains supported for pre-publication checks; all
scientific source, inputs and references still come from public immutable ZIPs.
"""
from pathlib import Path
import argparse
import csv
import datetime
import hashlib
import importlib.util
import io
import json
import math
import os
import platform
import re
import stat
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import zipfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('execution_registry', HERE / 'build-atlas-execution-examples.py')
registry_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registry_module)
REGISTRY_URL = registry_module.ORIGIN + registry_module.ROUTE
sha = registry_module.digest


def validate_download_url(url):
    path = registry_module.public_path(url)
    if not (str(path).startswith('code/') or url == REGISTRY_URL):
        raise ValueError('Only the public registry and immutable code artifacts may be downloaded')
    return url


class PublicRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urllib.parse.urljoin(req.full_url, newurl)
        validate_download_url(target)  # Before urllib issues the redirected request.
        return super().redirect_request(req, fp, code, msg, headers, target)


PUBLIC_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}), PublicRedirectHandler())


def checked_download(url, expected=None, limit=20_000_000):
    validate_download_url(url)
    if expected is not None:
        registry_module.hash_field(expected)
    request = urllib.request.Request(url, headers={'User-Agent':'Atlas-example-verification/2.0'})
    with PUBLIC_OPENER.open(request, timeout=60) as response:
        validate_download_url(response.geturl())
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError('Artifact exceeds download budget')
    if expected is not None and sha(data) != expected:
        raise ValueError('Downloaded artifact SHA-256 mismatch')
    return data


def strict_json(raw):
    def reject(value):
        raise ValueError('Nonfinite JSON constant: '+value)
    value = json.loads(raw, parse_constant=reject)
    def finite(item):
        if isinstance(item, float) and not math.isfinite(item):
            raise ValueError('Nonfinite JSON number')
        if isinstance(item, dict):
            for child in item.values():finite(child)
        elif isinstance(item, list):
            for child in item:finite(child)
    finite(value)
    return value


def json_safe(value):
    # An overflowing failed-check diagnostic must not prevent a failure report.
    if isinstance(value, float) and not math.isfinite(value):return None
    if isinstance(value, dict):return {key:json_safe(child) for key,child in value.items()}
    if isinstance(value, (list, tuple)):return [json_safe(child) for child in value]
    return value


def write_json(path, value):
    path = Path(path);path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.writing')
    temporary.write_bytes(registry_module.encode(json_safe(value)))
    temporary.replace(path)


def child_environment(temporary, parent=None):
    parent = os.environ if parent is None else parent
    allowed = ['PATH','LANG','LC_ALL','LC_CTYPE','SYSTEMROOT','WINDIR','COMSPEC','PATHEXT']
    env = {key:parent[key] for key in allowed if key in parent}
    temporary = Path(temporary)
    home = temporary/'home';home.mkdir(parents=True, exist_ok=True)
    scratch = temporary/'tmp';scratch.mkdir(parents=True, exist_ok=True)
    env.update(PATH=env.get('PATH', os.defpath), HOME=str(home), USERPROFILE=str(home),
               TMPDIR=str(scratch), TMP=str(scratch), TEMP=str(scratch),
               PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1',
               MPLCONFIGDIR=str(temporary/'plot-cache'), MPLBACKEND='Agg',
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    return env


def _bytes(value):
    if value is None:return b''
    return value if isinstance(value, bytes) else str(value).encode('utf-8', errors='replace')


def execute_logged(argv, cwd, env, timeout, stdout_path, stderr_path):
    """Keep normal and timeout partial output; return a serializable process state."""
    stdout_path, stderr_path = Path(stdout_path), Path(stderr_path)
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stdout_path.write_bytes(b'');stderr_path.write_bytes(b'')
    started = time.monotonic();out = err = b''
    result = {'started':False, 'exit_code':None, 'timed_out':False}
    try:
        completed = subprocess.run(argv, cwd=cwd, env=env, text=True,
                                   encoding='utf-8', errors='replace', capture_output=True, timeout=timeout)
        result.update(started=True, exit_code=completed.returncode)
        out, err = _bytes(completed.stdout), _bytes(completed.stderr)
    except subprocess.TimeoutExpired as exc:
        result.update(started=True, timed_out=True, error='runner_timeout')
        out, err = _bytes(exc.stdout), _bytes(exc.stderr)
    except (OSError, subprocess.SubprocessError) as exc:
        result['error'] = type(exc).__name__+': '+str(exc)
        err = _bytes(result['error'])
    finally:
        stdout_path.write_bytes(out);stderr_path.write_bytes(err)
    result['duration_seconds'] = round(time.monotonic()-started, 6)
    return result


def safe_extract(data, manifest, release, destination):
    """Extract exactly the verified edition, rejecting traversal, links and bombs."""
    prefix = release['archive_directory'] + '/'
    allowed = {prefix + str(registry_module.safe_path(p)) for p in manifest['files']}
    allowed.add(prefix + 'source-manifest.json')
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = archive.infolist()
        if len(infos) != len(allowed) or {x.filename for x in infos} != allowed:
            raise ValueError('Archive entries do not match the source manifest')
        if sum(x.file_size for x in infos) > 50_000_000:
            raise ValueError('Archive exceeds expanded-size budget')
        for entry in infos:
            registry_module.safe_path(entry.filename)
            if stat.S_IFMT(entry.external_attr >> 16) == stat.S_IFLNK:
                raise ValueError('Symbolic links are not permitted in code archives')
            payload = archive.read(entry)
            relative = entry.filename[len(prefix):]
            expected = release['manifest_sha256'] if relative == 'source-manifest.json' else manifest['files'][relative]
            if sha(payload) != expected:
                raise ValueError('Archived file SHA-256 mismatch')
            target = Path(destination) / entry.filename
            target.parent.mkdir(parents=True, exist_ok=True);target.write_bytes(payload)
    return Path(destination) / release['archive_directory']


def _output_path(output, relative):
    path = Path(output) / registry_module.safe_path(relative)
    path.resolve().relative_to(Path(output).resolve())
    if path.is_symlink():raise ValueError('Output symlinks are not accepted')
    return path


def check_case(example, output):
    result_file = next(x['generated_path'] for x in example['outputs'] if x['id'] == 'results')
    try:
        document = strict_json(_output_path(output, result_file).read_bytes())
    except (OSError, ValueError):
        return {'passed':False, 'checks':[], 'expected_failures':[], 'error':'missing_invalid_or_nonfinite_result_json'}
    checks = [registry_module.evaluate_check(document, c) for c in example['checks']]
    failures = [registry_module.evaluate_check(document, c) for c in example.get('expected_failures', [])]
    for artifact in example['outputs']:
        check = {'id':'output-'+artifact['id'], 'passed':False,
                 'generated_path':artifact['generated_path'], 'comparison':'nonempty_artifact'}
        try:
            path = _output_path(output, artifact['generated_path'])
            payload = path.read_bytes()
            good = bool(payload)
            if artifact['format'] == 'json':strict_json(payload)
            if artifact['format'] == 'csv':
                rows = list(csv.reader(io.StringIO(payload.decode('utf-8'))))
                good = len(rows) > 1 and bool(rows[0]) and all(cell.strip() for cell in rows[0])
                good = good and all(len(row)==len(rows[0]) and all(cell.strip() and math.isfinite(float(cell)) for cell in row) for row in rows[1:])
            check.update(passed=bool(good), sha256=sha(payload), bytes=len(payload))
        except (OSError, ValueError, UnicodeError):
            check['error'] = 'missing_invalid_or_nonfinite_artifact'
        checks.append(check)
    return json_safe({'passed':all(x['passed'] for x in checks+failures), 'checks':checks, 'expected_failures':failures})


def _group_label(group):
    return group if isinstance(group,str) and re.fullmatch('[a-z0-9-]+',group) else 'group-'+sha(str(group).encode())[:16]


def _not_run(case, execution, phase, error):
    return {'id':case['id'], 'problem_id':case['problem_id'], 'execution':execution,
            'validation':{'passed':False, 'checks':[], 'expected_failures':[], 'phase':phase, 'error':error},
            'residuals':{}, 'passed':False}


def run_registry(registry, python, timeout=300, artifacts_dir=None, checkpoint=None):
    """Keep the historical (environment, releases, examples) return value."""
    registry_module.validate_registry(registry)
    if timeout <= 0:raise ValueError('Runner timeout must be positive')
    groups = {}
    for case in registry['examples']:groups.setdefault(case['execution_group'], []).append(case)
    receipts, examples = [], []
    with tempfile.TemporaryDirectory(prefix='atlas-public-verification-') as temporary:
        temporary = Path(temporary)
        artifacts = Path(artifacts_dir) if artifacts_dir is not None else temporary/'artifacts'
        artifacts.mkdir(parents=True, exist_ok=True)
        if (artifacts/'groups').exists() or (artifacts/'environment.stdout.log').exists() or (artifacts/'environment.stderr.log').exists():
            raise ValueError('Run artifacts already exist; choose a new artifact directory')
        env = child_environment(temporary)
        probe = 'import json,platform,importlib.metadata as m;print(json.dumps({"python":platform.python_version(),"numpy":m.version("numpy"),"scipy":m.version("scipy"),"matplotlib":m.version("matplotlib")}))'
        process = execute_logged([str(python),'-c',probe], temporary, env, 30,
                                 artifacts/'environment.stdout.log', artifacts/'environment.stderr.log')
        environment = {'operating_system':platform.system(), 'machine':platform.machine(),
                       'thread_limits':{'OPENBLAS_NUM_THREADS':1,'OMP_NUM_THREADS':1,'MKL_NUM_THREADS':1}}
        env_error = None
        try:
            if process['exit_code'] != 0:raise ValueError('Selected Python requires NumPy, SciPy and Matplotlib; no installation was attempted')
            versions = strict_json((artifacts/'environment.stdout.log').read_bytes())
            if not isinstance(versions, dict) or any(not isinstance(versions.get(k),str) for k in ['python','numpy','scipy','matplotlib']):raise ValueError('Invalid environment probe output')
            environment.update({key:versions[key] for key in ['python','numpy','scipy','matplotlib']})
        except (ValueError, OSError) as exc:
            env_error = str(exc);environment['error'] = env_error
        write_json(artifacts/'environment.json', environment)
        if checkpoint:checkpoint(environment, receipts, examples)
        for group, cases in groups.items():
            first, phase = cases[0], 'environment' if env_error else 'download'
            release = first['release'];label = _group_label(group)
            group_artifacts = artifacts/'groups'/label
            group_artifacts.mkdir(parents=True, exist_ok=False)
            execution = {'group':group, 'started':False, 'completed':False, 'exit_code':None,
                         'timed_out':False, 'duration_seconds':0.,
                         'shared_runner_cases':[x['id'] for x in cases], 'command':first['commands']['run']}
            if artifacts_dir is not None:
                execution['artifacts'] = {key:'groups/'+label+'/'+name for key,name in [('stdout','stdout.log'),('stderr','stderr.log'),('output','output')]}
            receipt = {'family':release['family'], 'version':release['version'], 'download':release['download'],
                       'sha256':release['sha256'], 'archive_bytes':0, 'manifest':release['manifest'],
                       'manifest_sha256':release['manifest_sha256'], 'archived_files_verified':0,
                       'downloaded_artifacts':[], 'execution':execution, 'setup':{'passed':False}}
            try:
                if env_error:raise ValueError(env_error)
                manifest_bytes = checked_download(release['manifest'], release['manifest_sha256'])
                manifest = strict_json(manifest_bytes)
                if manifest['edition'] != release['version']:raise ValueError('Downloaded source edition mismatch')
                archive = checked_download(release['download'], release['sha256'])
                receipt['archive_bytes'] = len(archive)
                verification = strict_json(checked_download(release['verification']))
                if verification['archive_sha256'] != release['sha256'] or verification['failures'] or verification['errors']:raise ValueError('Existing release verification is incompatible')
                phase = 'archive-validation'
                folder = safe_extract(archive, manifest, release, temporary/label)
                receipt['archived_files_verified'] = len(manifest['files'])
                phase = 'artifact-validation';seen = set()
                for case in cases:
                    assets = [case['inputs'], *case['outputs'], *[x for x in case['references'] if 'sha256' in x]]
                    for artifact in assets:
                        if artifact['url'] in seen:continue
                        seen.add(artifact['url'])
                        if manifest['files'].get(artifact['path']) != artifact['sha256']:raise ValueError('Artifact is not covered by the source manifest')
                        payload = checked_download(artifact['url'], artifact['sha256'])
                        if payload != (folder/registry_module.safe_path(artifact['path'])).read_bytes():raise ValueError('Standalone artifact differs from archived copy')
                        receipt['downloaded_artifacts'].append({'url':artifact['url'],'sha256':artifact['sha256'],'bytes':len(payload)})
                receipt['setup'] = {'passed':True, 'phase':'complete'}
                output = group_artifacts/'output'
                argv = [str(python) if i==0 else str(output) if arg=='{output}' else arg for i,arg in enumerate(first['commands']['run_argv'])]
                phase = 'run'
                execution.update(execute_logged(argv, folder, env, timeout, group_artifacts/'stdout.log', group_artifacts/'stderr.log'))
                execution['completed'] = execution['exit_code'] == 0
                phase = 'validation'
                for case in cases:
                    validation = check_case(case, output)
                    residuals = {c['id']:c['maximum_residual'] for c in validation['checks'] if 'maximum_residual' in c}
                    examples.append({'id':case['id'],'problem_id':case['problem_id'],'execution':execution,
                                     'validation':validation,'residuals':residuals,
                                     'passed':execution['completed'] and validation['passed']})
            except Exception as exc:
                error = type(exc).__name__+': '+str(exc)
                receipt['setup'] = {'passed':False, 'phase':phase, 'error':error}
                for name in ['stdout.log','stderr.log']:
                    path = group_artifacts/name
                    if not path.exists() or (name=='stderr.log' and path.stat().st_size==0):
                        path.write_bytes(_bytes(error if name=='stderr.log' else ''))
                examples.extend(_not_run(case, execution, phase, error) for case in cases if not any(x['id']==case['id'] for x in examples))
            receipts.append(receipt)
            write_json(group_artifacts/'group.json', {'release':receipt,'examples':[x for x in examples if x['id'] in execution['shared_runner_cases']]})
            if checkpoint:checkpoint(environment, receipts, examples)
    return environment, receipts, examples


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', default=REGISTRY_URL)
    parser.add_argument('--python', default=sys.executable)
    parser.add_argument('--output', type=Path, required=True, help='New report JSON; existing receipts are never overwritten')
    parser.add_argument('--timeout', type=int, default=300)
    parser.add_argument('--artifacts-dir', type=Path, help='Retain group logs and partial JSON/CSV outputs')
    parser.add_argument('--expected-registry-sha256', help='Pin remote or local registry bytes')
    args = parser.parse_args(argv)
    report = {'schema_version':1,'verified_on':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'registry_url':REGISTRY_URL,'registry_sha256':None,'registry_source_mode':'unavailable',
              'expected_registry_sha256':args.expected_registry_sha256,
              'verification_tool':{'verifier_url':registry_module.ORIGIN+'/scripts/verify-atlas-execution-examples.py',
                  'verifier_sha256':sha(Path(__file__).read_bytes()),
                  'registry_builder_url':registry_module.ORIGIN+'/scripts/build-atlas-execution-examples.py',
                  'registry_builder_sha256':sha((HERE/'build-atlas-execution-examples.py').read_bytes())},
              'environment':{},'scope':'Only curated public execution recipes; not a general solver certification.',
              'releases':[],'examples':[],'unique_runner_executions':0,'passed':False,'status':'running'}
    registry = None;phase = 'preflight'
    if args.output.exists():
        print('Existing report is preserved; choose a new --output path', file=sys.stderr)
        return 2
    def checkpoint(environment, releases, records):
        report.update(environment=environment, releases=releases)
        indexed = {x['id']:x for x in records};rows = []
        for case in registry['examples']:
            execution = {'group':case['execution_group'],'started':False,'completed':False,'exit_code':None,
                         'timed_out':False,'duration_seconds':0.,'shared_runner_cases':case['shared_runner_cases'],'command':case['commands']['run']}
            rows.append(indexed.get(case['id']) or _not_run(case,execution,'pending','not_yet_attempted'))
        report['examples'] = rows
        report['unique_runner_executions'] = sum(x['execution'].get('started',False) for x in releases)
        write_json(args.output, report)
    try:
        write_json(args.output, report)
        if args.timeout <= 0:raise ValueError('--timeout must be positive')
        if args.expected_registry_sha256 is not None:registry_module.hash_field(args.expected_registry_sha256)
        phase = 'registry-download'
        if args.registry.startswith('https://'):
            raw = checked_download(args.registry, args.expected_registry_sha256)
            registry = strict_json(raw)
            if registry.get('url') != REGISTRY_URL or 'catalog_source' not in registry:raise ValueError('Remote registry is missing canonical metadata')
            source_mode = 'public-registry'
        else:
            raw_catalog = Path(args.registry).read_bytes();data = strict_json(raw_catalog)
            if args.expected_registry_sha256 is not None and sha(raw_catalog) != args.expected_registry_sha256:raise ValueError('Registry SHA-256 mismatch')
            if 'catalog_source' in data:
                registry, raw, source_mode = data, raw_catalog, 'local-public-registry-before-publication'
            else:
                registry = registry_module.build_registry(data, source_bytes=raw_catalog)
                raw, source_mode = registry_module.encode(registry), 'local-catalog-before-publication'
        phase = 'registry-validation';registry_module.validate_registry(registry)
        report.update(registry_sha256=sha(raw), registry_source_mode=source_mode,
                      scope=f'Only the {len(registry["examples"])} curated public execution examples. Atomic cases share one runner. Separate from packaged pytest checks, PySCF reference regeneration, the full atlas problem inventory and general solver certification.')
        checkpoint({}, [], [])
        phase = 'execution'
        environment,releases,examples = run_registry(registry,args.python,args.timeout,args.artifacts_dir,checkpoint)
        checkpoint(environment,releases,examples)
        report.update(passed=bool(examples) and all(x['passed'] for x in examples),status='complete')
    except Exception as exc:
        report.update(passed=False,status='failed',error={'phase':phase,'type':type(exc).__name__,'message':str(exc)})
    try:write_json(args.output, report)
    except OSError as exc:
        print('Could not save verification report: '+str(exc),file=sys.stderr);return 2
    print(json.dumps({'examples':len(report['examples']),'unique_runner_executions':report['unique_runner_executions'],'passed':report['passed']}))
    return 0 if report['passed'] else 1


if __name__ == '__main__':raise SystemExit(main())
