#!/usr/bin/env python3
"""Download the reviewed public RKDG kit and execute lightweight checks.

No full scientific campaign, MPI execution or quantum calculation is started.
The local expected manifest pins the public bytes before any code is executed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import stat
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zipfile

ORIGIN = 'https://hrkoyama.github.io'
MANIFEST_URL = ORIGIN+'/numerical-methods-atlas/agent-kits/rkdg2d/manifest.json'
ARCHIVE_URL = ORIGIN+'/code/rkdg2d/2026-11-23-r1/atlas-rkdg-agent-kit.zip'
ROOT_NAME = 'atlas-rkdg-agent-kit'


def digest(data):
    return hashlib.sha256(data).hexdigest()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise ValueError('Public downloads must not redirect')


def fetch(url, limit):
    if not url.startswith(ORIGIN+'/'):
        raise ValueError('Unexpected public origin')
    request = urllib.request.Request(url, headers={'User-Agent': 'Atlas-RKDG-public-verifier/1.0'})
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=40) as response:
        data = response.read(limit+1)
    if len(data) > limit:
        raise ValueError('Download size exceeds limit')
    return data


def run(output, expected_manifest, wait_seconds):
    output.mkdir(parents=True, exist_ok=False)
    report = {'passed': False, 'phase': 'download', 'downloads': [], 'commands': [],
              'environment': {'python': sys.version, 'platform': platform.platform()},
              'full48_fresh_pde_rerun': False, 'mpi_pde_executed': False,
              'quantum_runs': 0}
    try:
        expected = expected_manifest.read_bytes()
        deadline = time.monotonic()+wait_seconds
        while True:
            try:
                manifest_bytes = fetch(MANIFEST_URL, 1_000_000)
                if manifest_bytes != expected:
                    raise ValueError('Public manifest has not reached the reviewed version')
                break
            except (OSError, ValueError, urllib.error.URLError):
                if time.monotonic() >= deadline:
                    raise
                time.sleep(min(10, max(0, deadline-time.monotonic())))
        manifest = json.loads(manifest_bytes)
        report['downloads'].append({'url': MANIFEST_URL, 'sha256': digest(manifest_bytes)})
        (output/'manifest.json').write_bytes(manifest_bytes)
        archive = manifest['archive']
        if archive['url'] != ARCHIVE_URL:
            raise ValueError('Unexpected archive URL')
        raw = fetch(ARCHIVE_URL, 64*1024*1024)
        if digest(raw) != archive['sha256'] or len(raw) != archive['bytes']:
            raise ValueError('Public archive differs from pinned manifest')
        archive_path = output/'atlas-rkdg-agent-kit.zip'
        archive_path.write_bytes(raw)
        report['downloads'].append({'url': ARCHIVE_URL, 'sha256': digest(raw), 'bytes': len(raw)})
        for lang in ('ja', 'en'):
            guide = manifest['guides'][lang]
            data = fetch(guide['url'], 1_000_000)
            if digest(data) != guide['sha256']:
                raise ValueError('Public guide differs from pinned manifest: '+lang)
            (output/('TESTSET-'+lang+'.md')).write_bytes(data)
            report['downloads'].append({'url': guide['url'], 'sha256': digest(data)})
        checksum = fetch(ARCHIVE_URL+'.sha256', 1000).decode().split()
        if checksum != [archive['sha256'], 'atlas-rkdg-agent-kit.zip']:
            raise ValueError('Archive checksum sidecar mismatch')
        report['phase'] = 'extract-and-hash'
        extracted = output/'extracted'
        with zipfile.ZipFile(archive_path) as z:
            members = z.infolist()
            if len(members) > 2000 or sum(m.file_size for m in members) > 256*1024*1024:
                raise ValueError('Archive exceeds extraction limits')
            names = set()
            for entry in members:
                path = PurePosixPath(entry.filename)
                if (path.is_absolute() or '..' in path.parts or '\\' in entry.filename
                        or not path.parts or path.parts[0] != ROOT_NAME
                        or entry.filename.rstrip('/') != path.as_posix()
                        or entry.filename in names or stat.S_ISLNK(entry.external_attr >> 16)):
                    raise ValueError('Unsafe/duplicate ZIP member')
                names.add(entry.filename)
            z.extractall(extracted)
        kit = extracted/ROOT_NAME
        hashed = set()
        for line in (kit/'SHA256SUMS.txt').read_text().splitlines():
            sha, name = line.split('  ', 1)
            path = PurePosixPath(name)
            if path.is_absolute() or '..' in path.parts or name in hashed:
                raise ValueError('Unsafe/duplicate checksum entry')
            if digest((kit/name).read_bytes()) != sha:
                raise ValueError('Extracted member hash mismatch: '+name)
            hashed.add(name)
        actual = {p.relative_to(kit).as_posix() for p in kit.rglob('*') if p.is_file()}
        if actual != hashed | {'SHA256SUMS.txt'}:
            raise ValueError('Unlisted archive member or incomplete checksum list')
        report['member_hashes_checked'] = len(hashed)
        checks = kit/'outputs/public-verification'
        checks.mkdir()
        commands = [
            [sys.executable, 'scripts/run_rkdg_smoke.py', '--output', str(checks/'smoke.json')],
            [sys.executable, 'scripts/package_rkdg_agent_release.py', '--verify-only'],
            [sys.executable, '-m', 'pytest', '-q']+
            [p.relative_to(kit).as_posix() for p in sorted((kit/'tests').glob('test_rkdg*.py'))],
        ]
        env = dict(os.environ, PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1',
                   OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
        env.pop('PYTHONPATH', None)
        for i, command in enumerate(commands):
            report['phase'] = ['fresh-smoke', 'saved-evidence', 'regression-tests'][i]
            stamp = time.monotonic()
            result = subprocess.run(command, cwd=kit, env=env, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, timeout=240)
            log = output/('check-'+str(i)+'.log')
            log.write_text(result.stdout)
            report['commands'].append({'command': command[1:], 'exit_code': result.returncode,
                                       'seconds': time.monotonic()-stamp, 'log': log.name})
            if result.returncode:
                raise ValueError('Check failed: '+report['phase']+'; see '+log.name)
            if i == 1:
                saved = json.loads(result.stdout)
                reflection = saved['reflection_supplement']
                if (saved.get('integrity_passed') is not True or saved.get('new_pde_runs') != 0
                        or saved['original48_and_waveform4'].get('scientific_saved_result_recheck_passed') is not True
                        or reflection.get('integrity_passed') is not True
                        or reflection.get('qualification_passed') is not False
                        or reflection.get('passed_cases') != 5 or reflection.get('total_cases') != 6):
                    raise ValueError('Saved-evidence scope/result mismatch')
                report['saved_evidence'] = saved
        smoke = json.loads((checks/'smoke.json').read_text())
        if not smoke['passed'] or smoke['fresh_pde_runs'] != 6:
            raise ValueError('Fresh smoke result is incomplete')
        report['smoke'] = smoke
        report['known_reflection_qualification'] = '5/6 saved cases pass; not an overall qualification PASS'
        report['passed'] = True
        report['phase'] = 'complete'
    except Exception as error:
        report['error'] = {'type': type(error).__name__, 'message': str(error)}
    (output/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'passed': report['passed'], 'phase': report['phase'], 'report': str(output/'report.json')}))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-manifest-file', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--wait-seconds', type=int, default=0)
    args = parser.parse_args()
    raise SystemExit(run(args.output_dir.resolve(), args.expected_manifest_file.resolve(), args.wait_seconds))
