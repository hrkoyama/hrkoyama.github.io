import {groupsAddedAfterBatch37,supplementCaseCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const text = path => readFileSync(join(root, path), 'utf8');
const json = path => JSON.parse(text(path));
const sha = path => createHash('sha256').update(readFileSync(join(root, path))).digest('hex');
const workflow = text('.github/workflows/atlas-depth-linux.yml');
assert.ok(workflow.includes('\n  public-supplements:'), 'the public scientific job must remain explicit');
const scienceWorkflow = workflow.slice(workflow.indexOf('\n  public-supplements:'));
const registryPath = 'numerical-methods-atlas/validation/releases.json';
const prelude = String.raw`
import copy, hashlib, importlib.util, io, json, os, shutil, stat, sys, tempfile, warnings, zipfile
from pathlib import Path
ROOT = Path(os.environ['ATLAS_TEST_ROOT'])
sys.path.insert(0, str(ROOT/'scripts'))
def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value
v = module('verifier', 'scripts/verify-depth-public.py')
u = module('updater', 'scripts/update-depth-ci-pins.py')
registry_bytes = (ROOT/u.REGISTRY_PATH).read_bytes()
registry = v.strict_json(registry_bytes)
def brief_report(report):
    return {'phase': report.get('phase'), 'error': str(report.get('error'))[:1200],
            'active_group': report.get('active_group')}
def rejects(call):
    try:
        call()
    except (ValueError, TypeError, KeyError, RuntimeError, AssertionError):
        return
    raise AssertionError('Unsafe or invalid input was accepted')
def fixture(group='foundations'):
    release = copy.deepcopy(next(r for r in registry['releases'] if r['group']==group))
    directory = ROOT/'code/validated-examples'/release['edition']/group
    manifest = v.strict_json((directory/'source-manifest.json').read_bytes())
    receipt = v.strict_json((directory/'verification.json').read_bytes())
    return release, manifest, receipt, (directory/release['archive']).read_bytes(), (directory/'requirements.txt').read_bytes()
`;
function python(source, timeout = 30_000) {
  return execFileSync('python3', ['-B', '-c', prelude + '\n' + source], {
    cwd: root, encoding: 'utf8', timeout,
    env: {...process.env, ATLAS_TEST_ROOT: root, PYTHONDONTWRITEBYTECODE: '1'},
  });
}
function shellBlocks() {
  const lines = scienceWorkflow.split('\n'), blocks = [];
  for (let i = 0; i < lines.length; i++) {
    if (lines[i] !== '        run: |') continue;
    const body = [];
    while (++i < lines.length && (!lines[i].trim() || lines[i].startsWith('          '))) body.push(lines[i].slice(10));
    i--;
    blocks.push(body.join('\n'));
  }
  return blocks;
}
const pythonBlocks = shellBlocks().flatMap(block => [...block.matchAll(/python(?:3)? - <<'PY'\n([\s\S]*?)\nPY/g)].map(match => match[1]));

test('registry preserves eleven frozen releases and adds the separately dated Noh release with two workflow pins', () => {
  const registry = json(registryPath);
  assert.equal(registry.case_count, supplementCaseCount);
  const previous = registry.releases.filter(x => !['noh','noh-cartesian','sedov','double-mach','forward-step','low-mach','guderley','euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(x.group));
  assert.equal(createHash('sha256').update(JSON.stringify(previous)).digest('hex'), 'b2e03aeb8798240a38d00bbe2491a5fc50109f2020078decf419f7276eb3241f', 'old eleven release metadata and hashes are immutable');
  assert.ok(previous.every(x => x.edition === '2026-11-22'));
  const noh = registry.releases.find(x => x.group === 'noh');
  assert.equal(noh.edition, '2026-11-23-r5');
  assert.deepEqual(noh.case_ids, ['noh-shock']);
  assert.equal(noh.tests,28);
  assert.equal(registry.releases.filter(row=>!['euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(row.group)).reduce((sum,row)=>sum+row.tests,0),571);
  assert.deepEqual(registry.releases.map(x => x.group), ["foundations","models","particles","mhd","thermostats","biology","mcmc","mhd-convergence","foundations-conditioning","particle-transport","splitting","noh","noh-cartesian","sedov","double-mach","forward-step","low-mach","guderley","euler-positivity","zalesak","weno-critical","shallow-water","wall-flow","level-set","sem-fr","instability-growth","mhd-transport","mesh-boundary","moving-waves","relativistic","coefficient-diffusion","slab-ewald","fmm3d","gravity-dynamics","warm-pic","pic-spatial","dsmc-wall","dsmc-shock",...groupsAddedAfterBatch37]);
  assert.deepEqual(registry.releases.slice(0,4).map(x => x.tests), [29, 26, 27, 11]);
  assert.equal(registry.releases[4].tests,42);
  assert.equal(registry.releases[5].tests,28);
  assert.equal(registry.releases[6].tests,39);
  assert.equal(registry.releases[7].tests,46);
  assert.equal(registry.releases[8].tests,49);
  assert.equal(registry.releases[9].tests,75);
  assert.equal(registry.releases[10].tests,16);
  assert.equal(previous.reduce((sum,release)=>sum+release.tests,0),388);
  assert.deepEqual(previous.map(x => x.case_ids.length), [4, 5, 6, 4, 3, 2, 2, 3, 4, 6, 1]);
  assert.equal(new Set(registry.releases.flatMap(x => x.case_ids)).size, supplementCaseCount);
  for (const release of registry.releases) {
    const base = `code/validated-examples/${release.edition}/${release.group}/`;
    assert.equal(release.base, 'https://hrkoyama.github.io/' + base);
    for (const [file, key] of [[release.archive, 'archive_sha256'], ['source-manifest.json', 'manifest_sha256'], ['verification.json', 'verification_sha256'], ['requirements.txt', 'requirements_sha256']])
      assert.equal(sha(base + file), release[key]);
  }
  assert.ok(workflow.includes(`ATLAS_DEPTH_BOOTSTRAP_SHA256: '${sha('scripts/verify-depth-public.py')}'`));
  assert.ok(workflow.includes(`ATLAS_DEPTH_REGISTRY_SHA256: '${sha(registryPath)}'`));
  python(`assert u.render_registry(u.build_registry(ROOT)) == registry_bytes`);
});

test('workflow uses a fresh guarded public-only Linux environment, exact wheels and retained failure evidence', () => {
  assert.doesNotMatch(scienceWorkflow, /actions\/checkout|persist-credentials|secrets\.|write-all|contents: write|pip cache|cache: ['"]?pip/i);
  assert.doesNotMatch(workflow, /secrets\.|write-all|contents: write/i);
  assert.match(workflow, /github\.repository == 'hrkoyama\/hrkoyama\.github\.io'/);
  assert.match(workflow, /head_repository\.full_name == github\.repository/);
  const jobEnvironment=scienceWorkflow.match(/^    env:\n([\s\S]*?)^    steps:/m)?.[1];
  assert.ok(jobEnvironment);assert.doesNotMatch(jobEnvironment, /runner\./, 'runner context is only available to the steps');
  assert.equal((scienceWorkflow.match(/^          REPORT_DIR: \$\{\{ runner\.temp \}\}/gm)||[]).length,4);
  assert.match(workflow, /workflow_dispatch:/);
  assert.match(workflow, /schedule:/);
  assert.match(workflow, /workflows: \['Public site checks'\]/);
  assert.match(workflow, /conclusion == 'success'/);
  assert.match(workflow, /runs-on: ubuntu-24\.04/);
  assert.match(workflow, /python-version: '3\.12'/);
  assert.match(scienceWorkflow, /timeout-minutes: 45/);
  assert.match(workflow, /python -m venv "\$ATLAS_VENV"/);
  assert.match(workflow, /--only-binary=:all: --no-cache-dir/);
  assert.match(workflow, /numpy==2\.0\.2 scipy==1\.14\.1 pytest==8\.3\.5/);
  assert.doesNotMatch(workflow, /pyscf|matplotlib|quantum-periodic|examples\.json/i);
  assert.equal((scienceWorkflow.match(/if: always\(\)/g) || []).length, 2);
  assert.match(workflow, /retention-days: 90/);
  assert.match(workflow, /publication-attempts\.json/);
  assert.match(workflow, /pip-install\.json/);
  assert.match(workflow, /workflow-context\.json/);
  assert.equal(shellBlocks().length, 4);
  assert.equal(pythonBlocks.length, 4);
  for (const block of shellBlocks()) execFileSync('bash', ['-n'], {input: block});
  for (const block of pythonBlocks) python(`compile(${JSON.stringify(block)}, '<workflow-python>', 'exec')`);
});

test('small verifier rebuild binds both hashes without scanning or changing scientific releases', () => {
  python(String.raw`
with tempfile.TemporaryDirectory() as temporary:
    root = Path(temporary)
    verifier = root/u.VERIFIER_PATH
    verifier.parent.mkdir(parents=True)
    verifier.write_bytes(b'# isolated rendered verifier\n')
    workflow = root/u.WORKFLOW_PATH
    workflow.parent.mkdir(parents=True)
    template = "# preserve the workflow\nenv:\n  ATLAS_DEPTH_BOOTSTRAP_SHA256: '"+'0'*64+"'\n  ATLAS_DEPTH_REGISTRY_SHA256: '"+'1'*64+"'\n"
    workflow.write_text(template)
    registry = b'{"frozen":"registry fixture"}\n'
    pins = u.bind_workflow(root, registry)
    assert pins == {'ATLAS_DEPTH_BOOTSTRAP_SHA256':v.digest(verifier.read_bytes()),
                    'ATLAS_DEPTH_REGISTRY_SHA256':v.digest(registry)}
    expected = template.replace('0'*64, pins['ATLAS_DEPTH_BOOTSTRAP_SHA256']).replace('1'*64, pins['ATLAS_DEPTH_REGISTRY_SHA256'])
    assert workflow.read_text() == expected
    u.bind_workflow(root, registry)
    assert workflow.read_text() == expected
    for bad in [template.replace('  ATLAS_DEPTH_REGISTRY_SHA256:', '  WRONG_PIN:'), template+template]:
        workflow.write_text(bad)
        rejects(lambda: u.bind_workflow(root, registry))
        assert workflow.read_text() == bad
    assert not (root/'code').exists() and not (root/u.REGISTRY_PATH).exists()
`);
});

test('canonical registry URLs, group prefixes and all JSON numeric decisions reject unsafe variants', () => {
  python(String.raw`
v.validate_registry(registry)
for url in ['http://hrkoyama.github.io/x', 'https://evil.example/x', 'https://user@hrkoyama.github.io/x',
            'https://hrkoyama.github.io:443/x', 'https://hrkoyama.github.io//x',
            'https://hrkoyama.github.io/a/../x', 'https://hrkoyama.github.io/%2e%2e/x',
            'https://hrkoyama.github.io/x?token=1', 'https://hrkoyama.github.io/x#anchor']:
    rejects(lambda: v.validate_url(url))
rejects(lambda: v.validate_registry_url('https://hrkoyama.github.io/other/registry.json'))
for patch in [('schema_version', True), ('case_count', 18), ('edition', '../2026-11-22')]:
    value = copy.deepcopy(registry); value[patch[0]] = patch[1]
    rejects(lambda: v.validate_registry(value))
for key, value in [('edition', '../2026-11-23'), ('edition', True), ('edition', '2026-11-23'), ('base', 'https://hrkoyama.github.io/code/validated-examples/other/'),
                   ('archive', '../evil.zip'), ('tests', True), ('archive_sha256', 'a'*63)]:
    altered = copy.deepcopy(registry); altered['releases'][0][key] = value
    rejects(lambda: v.validate_registry(altered))
for value in [b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1e999}', b'{"x":Infinity}']:
    rejects(lambda: v.strict_json(value))
for data in [b'numpy==2.0.2\nscipy==1.14.1\npytest==8.3.5\npyscf==2.8.0\n', b'numpy>=2\n']:
    rejects(lambda: v.validate_requirements(data))
`);
});

test('every packaged ZIP validates independently without importing or executing scientific sources', () => {
  python(String.raw`
with tempfile.TemporaryDirectory() as temporary:
    for release in registry['releases']:
        release, manifest, receipt, payload, requirements = fixture(release['group'])
        target = v.verify_archive(payload, manifest, receipt, requirements, release, Path(temporary)/release['group'])
        assert (target/'run.py').is_file()
        assert {p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file()} == set(manifest['files']) | {'source-manifest.json'}
        result = v.strict_json((target/'results/result.json').read_bytes())
        v.validate_result(result, release['case_ids'], manifest['files']['inputs.json'], result['termination'])
assert not any(name in sys.modules for name in ['numpy', 'scipy', 'pytest', 'pyscf'])
`);
});

test('changed hashes, duplicate paths, symlinks, oversized and traversal archives fail before extraction', () => {
  python(String.raw`
release, manifest, receipt, payload, requirements = fixture()
prefix = receipt['archive']['archive_directory']
with zipfile.ZipFile(io.BytesIO(payload)) as original:
    members = [(copy.copy(info), original.read(info)) for info in original.infolist()]
def repack(mutator):
    records = copy.deepcopy(members); mutator(records)
    stream = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED) as output:
            for info, data in records: output.writestr(info, data)
    return stream.getvalue()
def altered_case(changed, changed_manifest=None):
    local_release, local_receipt = copy.deepcopy(release), copy.deepcopy(receipt)
    local_release['archive_sha256'] = v.digest(changed)
    local_receipt['archive'].update(sha256=v.digest(changed), bytes=len(changed))
    local_receipt['archive_sha256'] = v.digest(changed)
    with tempfile.TemporaryDirectory() as temporary:
        destination = Path(temporary)/'unwritten'
        rejects(lambda: v.verify_archive(changed, changed_manifest or manifest, local_receipt, requirements, local_release, destination))
        assert not destination.exists(), 'Validation must finish before writing any member'
altered_case(repack(lambda records: records.append(records[0])))
altered_case(repack(lambda records: records.append((zipfile.ZipInfo(prefix+'/../escape.py'), b'evil'))))
def symlink(records):
    records[0][0].external_attr = (stat.S_IFLNK | 0o777) << 16
altered_case(repack(symlink))
def changed_member(records):
    info, data = records[0]; records[0] = info, data+b'changed'
altered_case(repack(changed_member))
bad_manifest = copy.deepcopy(manifest); bad_manifest['files']['../evil.py'] = 'a'*64
altered_case(payload, bad_manifest)
old_limit = v.MAX_UNCOMPRESSED_BYTES; v.MAX_UNCOMPRESSED_BYTES = 1
try: altered_case(payload)
finally: v.MAX_UNCOMPRESSED_BYTES = old_limit
with tempfile.TemporaryDirectory() as temporary:
    rejects(lambda: v.verify_archive(payload+b'corrupt', manifest, receipt, requirements, release, Path(temporary)/'bad'))
    existing = Path(temporary)/'exists'; existing.mkdir()
    rejects(lambda: v.verify_archive(payload, manifest, receipt, requirements, release, existing))
`);
});

test('download failures retain both expected and observed hashes and redirects never follow', () => {
  python(String.raw`
class Response:
    status = 200
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, count): return b'changed-public-file'
class Opener:
    def open(self, request, timeout):
        assert request.full_url.startswith(v.ORIGIN+'/')
        return Response()
v.urllib.request.build_opener = lambda *handlers: Opener()
acquisitions = []
rejects(lambda: v.download(v.REGISTRY_URL, '0'*64, acquisitions, 'registry'))
assert acquisitions[0]['passed'] is False
assert acquisitions[0]['sha256'] == v.digest(b'changed-public-file')
assert acquisitions[0]['expected_sha256'] == '0'*64
assert acquisitions[0]['error']['type'] == 'ValueError'
rejects(lambda: v.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://evil.example/'))
`);
});

test('numerical result validation requires literal booleans, finite values, original input and completion', () => {
  python(String.raw`
release, manifest, receipt, payload, requirements = fixture()
source = ROOT/'code/validated-examples'/release['edition']/'foundations/results/result.json'
stored = v.strict_json(source.read_bytes())
def check(value): return v.validate_result(value, release['case_ids'], manifest['files']['inputs.json'], stored['termination'])
for key, value in [('passed', 1), ('schema_version', True), ('input_sha256', '0'*64), ('termination', 'interrupted')]:
    result = copy.deepcopy(stored); result[key] = value; rejects(lambda: check(result))
for value in [False, 1, None]:
    result = copy.deepcopy(stored); result['cases'][0]['checks'][next(iter(result['cases'][0]['checks']))] = value
    rejects(lambda: check(result))
result = copy.deepcopy(stored); result['cases'][0]['metrics']['bad'] = float('inf'); rejects(lambda: check(result))
result = copy.deepcopy(stored); result['cases'].pop(); rejects(lambda: check(result))
result = copy.deepcopy(stored); result['checks'].pop(next(iter(result['checks']))); rejects(lambda: check(result))
`);
});

test('JUnit tests/skips/failures and generated CSV finite-column guards are independently enforced', () => {
  python(String.raw`
with tempfile.TemporaryDirectory() as temporary:
    path = Path(temporary)/'pytest.xml'
    path.write_text('<testsuites><testsuite tests="2"><testcase name="a"/><testcase name="b"/></testsuite></testsuites>')
    assert v.check_junit(path, 2)['tests'] == 2
    rejects(lambda: v.check_junit(path, 3))
    for tag in ['failure', 'error', 'skipped']:
        path.write_text('<testsuites><testsuite><testcase><'+tag+'/></testcase></testsuite></testsuites>')
        rejects(lambda: v.check_junit(path, 1))
    path.write_text('<testsuites><testsuite skipped="1"><testcase/></testsuite></testsuites>')
    rejects(lambda: v.check_junit(path, 1))
    data = Path(temporary)/'series.csv'; data.write_text('step,error\n1,0.1\n2,0.01\n')
    assert len(v.check_generated_csv(temporary)) == 1
    for content in ['x,x\n1,2\n', 'x,y\n1\n', 'x,error\n1,nan\n', 'x,error\n1,inf\n']:
        data.write_text(content); rejects(lambda: v.check_generated_csv(temporary))
`);
});

test('real standard-library subprocess logging and timeout handling retain their evidence', () => {
  python(String.raw`
with tempfile.TemporaryDirectory() as temporary:
    directory = Path(temporary)
    environment = v.clean_environment(directory/'temporary')
    result = v.run_process([sys.executable, '-c', 'print("unit-process-ok")'], directory,
                           directory, 'success', environment, 5)
    assert result['completed'] and result['exit_code']==0 and not result['timed_out']
    assert result['timeout_seconds']==5 and result['termination']=='process_exit'
    assert result['child_cpu_seconds']>=0 and v.math.isfinite(result['child_cpu_seconds'])
    assert v.datetime.datetime.fromisoformat(result['started_at_utc']).tzinfo is not None
    assert v.datetime.datetime.fromisoformat(result['finished_at_utc']).tzinfo is not None
    assert (directory/'success.stdout.log').read_text().strip()=='unit-process-ok'
    result = v.run_process([sys.executable, '-c', 'import time; print("started", flush=True); time.sleep(5)'],
                           directory, directory, 'timeout', environment, 0.2)
    assert result['timed_out'] and not result['completed'] and result['exit_code'] is None
    assert result['timeout_seconds']==0.2 and result['termination']=='wall_timeout'
    assert result['duration_seconds'] < 3
    assert (directory/'timeout.stdout.log').is_file() and (directory/'timeout.stderr.log').is_file()
    for invalid in [0, -1, float('nan'), float('inf'), True]:
        rejects(lambda: v.run_process([sys.executable, '-c', 'raise RuntimeError("must not launch")'],
                                      directory, directory, 'invalid', environment, invalid))
    host = v.inspect_environment()
    for key in ['cpu_count', 'cpu_affinity_count']:
        assert host[key] is None or (type(host[key]) is int and host[key]>0)
`);
});

const mockedPipeline = String.raw`
original_download = v.download
def public_fixture(url, expected, acquisitions, kind):
    v.validate_url(url)
    path = ROOT/url.removeprefix(v.ORIGIN+'/')
    data = registry_bytes if url == v.REGISTRY_URL else path.read_bytes()
    record = {'kind': kind, 'url': url, 'expected_sha256': expected, 'sha256': v.digest(data), 'passed': v.digest(data)==expected}
    acquisitions.append(record)
    v.require(record['passed'], 'Mock public hash mismatch')
    return data
v.download = public_fixture
v.inspect_environment = lambda: {'python': '3.12.0', 'operating_system': 'Linux', 'machine': 'x86_64', 'dependencies': dict(v.DIRECT_PINS), 'source_checkout_required': False, 'plot_regeneration': False}
mode = 'success'
def fake_process(command, cwd, log_directory, name, environment, timeout):
    global mode
    assert 0 < timeout <= v.GROUP_TIMEOUT_SECONDS
    assert not any(key in environment for key in ['GITHUB_TOKEN', 'AWS_SECRET_ACCESS_KEY', 'PYTHONPATH'])
    directory = Path(log_directory)
    for stream in ['stdout', 'stderr']: (directory/(name+'.'+stream+'.log')).write_text('mock '+name+' '+stream+'\n')
    group = v.strict_json((Path(cwd)/'source-manifest.json').read_bytes())['group']
    tests = next(r['tests'] for r in registry['releases'] if r['group']==group)
    record = {'completed': True, 'timed_out': False, 'exit_code': 0, 'duration_seconds': 0.001,
              'stdout': name+'.stdout.log', 'stderr': name+'.stderr.log', 'command': command}
    if name == 'pytest':
        junit = Path(next(arg.split('=', 1)[1] for arg in command if arg.startswith('--junitxml=')))
        marker = '<skipped/>' if mode=='skip' and group=='foundations' else ''
        junit.write_text('<testsuites><testsuite>'+''.join('<testcase name="t'+str(i)+'">'+(marker if i==0 else '')+'</testcase>' for i in range(tests))+'</testsuite></testsuites>')
        if mode=='mutate-input' and group=='foundations': (Path(cwd)/'inputs.json').write_text('{}')
    else:
        generated = Path(command[-1]); generated.mkdir()
        source = Path(cwd)/'results'
        for path in source.glob('*.csv'): shutil.copyfile(path, generated/path.name)
        result = v.strict_json((source/'result.json').read_bytes())
        if group=='models':
            if mode=='run-failed': record['exit_code'] = 1
            if mode=='timeout': record.update(completed=False, timed_out=True, exit_code=None)
            if mode=='numerical-failed': result['cases'][0]['checks'][next(iter(result['cases'][0]['checks']))] = False
            if mode=='omitted-check': result['cases'][0]['checks'].pop(next(iter(result['cases'][0]['checks'])))
        v.write_json(generated/'result.json', result)
    return record
v.run_process = fake_process
os.environ['GITHUB_TOKEN'] = 'do-not-inherit'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'do-not-inherit'
`;

test('operational wall guard admits a slow fixed driver and retains one shared bounded group deadline', () => {
  python(mockedPipeline + String.raw`
# Use the same immutable fixture bytes and numerical decisions as the existing
# state-machine tests. Virtual elapsed time exercises the resource guard only.
registry['releases'] = registry['releases'][:2]
registry['case_count'] = sum(len(r['case_ids']) for r in registry['releases'])
v.GROUPS = tuple(r['group'] for r in registry['releases'])
registry_bytes = json.dumps(registry).encode('utf-8')
assert v.GROUP_TIMEOUT_SECONDS == 240
original_process, original_clock = v.run_process, v.time.monotonic
clock, calls = [0.0], []
charges = {'pytest': 8.0, 'run': 150.0}
v.time.monotonic = lambda: clock[0]
def elapsed_process(command, cwd, log_directory, name, environment, timeout):
    calls.append((name, timeout))
    record = original_process(command, cwd, log_directory, name, environment, timeout)
    elapsed = min(charges[name], timeout)
    clock[0] += elapsed
    record['duration_seconds'] = elapsed
    if charges[name] > timeout:
        record.update(completed=False, timed_out=True, exit_code=None)
    return record
v.run_process = elapsed_process
try:
    with tempfile.TemporaryDirectory() as temporary:
        report = v.verify(v.REGISTRY_URL, v.digest(registry_bytes), Path(temporary)/'slow')
        assert report['passed'] is True, brief_report(report)
        assert report['execution_limits'] == {'group_wall_seconds': 240, 'scope': 'outer_orchestration_only'}
        assert calls == [('pytest', 240.0), ('run', 232.0)] * 2
        assert all(g['run_process']['duration_seconds'] == 150 for g in report['groups'])
        assert report['tests'] == sum(r['tests'] for r in registry['releases'])
    # Tests and driver each fit individually, but their combined250seconds do
    # not fit. Resetting the deadline before the driver would wrongly pass.
    charges['pytest'] = 100.0
    calls.clear()
    with tempfile.TemporaryDirectory() as temporary:
        report = v.verify(v.REGISTRY_URL, v.digest(registry_bytes), Path(temporary)/'over-budget')
        assert report['passed'] is False and report['error']['phase'] == 'execution'
        assert calls == [('pytest', 240.0), ('run', 140.0)]
        assert report['groups'][0]['run_process']['timed_out'] is True
        assert report['groups'][0]['passed'] is False
finally:
    v.run_process, v.time.monotonic = original_process, original_clock
`, 60_000);
});

test('full verifier state machine accepts every mixed-edition saved fixture case without scientific execution', () => {
  python(mockedPipeline + String.raw`
# This positive metadata fixture validates every real archive/result, but does not
# need to rewrite the same growing running report hundreds of times. Keep all
# checkpoint emissions as immutable state projections; persist every terminal
# report and all non-report JSON through the unchanged real atomic writer.
original_write_json = v.write_json
checkpoint_rows, terminal_reports = [], []
verifier_source = ROOT/'scripts/verify-depth-public.py'
verifier_before = v.digest(verifier_source.read_bytes())
def fixture_write_json(path, value):
    if Path(path).name == 'report.json' and value.get('status') == 'running':
        checkpoint_rows.append((value['phase'], value.get('active_group'),
                                len(value['groups']), len(value['acquisitions'])))
        return
    original_write_json(path, value)
    if Path(path).name == 'report.json':
        terminal_reports.append(copy.deepcopy({key: value.get(key) for key in ['status', 'phase', 'passed']}))
v.write_json = fixture_write_json
try:
    # A failed terminal report must never be coalesced into an apparent success.
    with tempfile.TemporaryDirectory() as probe:
        failed = {'status': 'failed', 'phase': 'sentinel', 'passed': False}
        probe_report = Path(probe)/'report.json'
        fixture_write_json(probe_report, failed)
        assert v.strict_json(probe_report.read_bytes()) == failed
    with tempfile.TemporaryDirectory() as temporary:
        report = v.verify(v.REGISTRY_URL, v.digest(registry_bytes), Path(temporary)/'run')
        assert report['passed'] is True, brief_report(report)
        assert report['phase']=='complete' and report['case_count']==registry['case_count'] and report['tests']==sum(g['tests'] for g in registry['releases'])
        assert len(report['acquisitions'])==1+4*len(registry['releases']) and all(r['passed'] for r in report['acquisitions'])
        assert all(g['pytest']['skipped']==0 and g['passed'] and g['generated_csv'] for g in report['groups'])
        assert v.strict_json((Path(temporary)/'run/report.json').read_bytes())['passed'] is True
        for group in v.GROUPS:
            directory = Path(temporary)/'run/groups'/group
            assert (directory/'pytest.stdout.log').is_file() and (directory/'run.stderr.log').is_file()
            assert (directory/'generated/result.json').is_file()
    assert not any(name in sys.modules for name in ['numpy', 'scipy', 'pytest', 'pyscf'])
finally:
    v.write_json = original_write_json
assert v.write_json is original_write_json
assert v.digest(verifier_source.read_bytes()) == verifier_before
expected_checkpoints = [('registry', None, 0, 0)]
groups = [release['group'] for release in registry['releases']]
for index, group in enumerate(groups):
    expected_checkpoints.append(('downloads', group, index+1, 1+4*index))
    expected_checkpoints.extend(('downloads', group, index+1, 1+4*index+item) for item in range(1, 5))
    expected_checkpoints.extend([('archive-validation', group, index+1, 1+4*(index+1))]*2)
expected_checkpoints.extend([('environment', groups[-1], len(groups), 1+4*len(groups))]*2)
for group in groups:
    expected_checkpoints.extend((phase, group, len(groups), 1+4*len(groups)) for phase in
        ['pytest', 'pytest', 'pytest-validation', 'fixed-input-integrity',
         'execution', 'execution', 'numerical-validation', 'numerical-validation'])
assert checkpoint_rows == expected_checkpoints
assert len(checkpoint_rows) == 3+15*len(groups)
assert terminal_reports == [
    {'status': 'failed', 'phase': 'sentinel', 'passed': False},
    {'status': 'complete', 'phase': 'complete', 'passed': True},
]
`, 120_000);
});

test('runner failures, timeout, skips, altered inputs and omitted decisions preserve explicit failed reports', () => {
  python(mockedPipeline + String.raw`
# These failure modes only reach the first two groups. Keep the full-inventory
# positive test above, but avoid extracting unrelated archives six more times.
registry['releases'] = [release for release in registry['releases'] if release['group'] in ['foundations', 'models']]
registry['case_count'] = sum(len(release['case_ids']) for release in registry['releases'])
v.GROUPS = ('foundations', 'models')
registry_bytes = json.dumps(registry).encode('utf-8')
v.validate_registry(registry)
for mode, phase in [('run-failed', 'execution'), ('timeout', 'execution'), ('numerical-failed', 'numerical-validation'),
                    ('omitted-check', 'numerical-validation'), ('skip', 'pytest-validation'), ('mutate-input', 'fixed-input-integrity')]:
    with tempfile.TemporaryDirectory() as temporary:
        output = Path(temporary)/'run'
        report = v.verify(v.REGISTRY_URL, v.digest(registry_bytes), output)
        assert report['passed'] is False and report['status']=='failed', (mode, brief_report(report))
        assert [group['group'] for group in report['groups']]==list(v.GROUPS)
        assert len(report['acquisitions'])==1+4*len(v.GROUPS)
        assert report['error']['phase']==phase, (mode, brief_report(report))
        assert report['environment']['dependencies']==v.DIRECT_PINS
        assert (output/'report.json').is_file() and (output/'groups/foundations/pytest.stdout.log').is_file()
        if mode in ['run-failed', 'timeout', 'numerical-failed', 'omitted-check']:
            assert report['groups'][0]['passed'] is True
            assert (output/'groups/models/generated/result.json').is_file()
            assert (output/'groups/models/run.stderr.log').is_file()
            assert report['groups'][1]['passed'] is False
`);
});

test('registry/setup failures are recorded with environment diagnostics before any scientific execution', () => {
  python(mockedPipeline + String.raw`
with tempfile.TemporaryDirectory() as temporary:
    output = Path(temporary)/'bad-registry'
    report = v.verify(v.REGISTRY_URL, '0'*64, output)
    assert report['passed'] is False and report['error']['phase']=='registry'
    assert (output/'report.json').is_file() and report['acquisitions'][0]['passed'] is False
    output = Path(temporary)/'bad-environment'
    v.inspect_environment = lambda: {'python': '3.12.0', 'operating_system': 'Linux', 'dependencies': {'numpy': 'wrong'}}
    report = v.verify(v.REGISTRY_URL, v.digest(registry_bytes), output)
    assert report['passed'] is False and report['error']['phase']=='environment'
    assert report['environment']['dependencies']=={'numpy': 'wrong'}
    assert not list(output.glob('groups/*/pytest.stdout.log'))
`);
});

test('publication wait verifies both current hashes before saving executable bootstrap and preserves mismatch attempts', () => {
  const block = pythonBlocks.find(value => value.includes('class NoRedirect'));
  assert.ok(block);
  python(String.raw`
import time, urllib.request
bootstrap = b'# reviewed verifier\n'
registry_content = b'{"reviewed":true}\n'
class Response:
    def __init__(self, data): self.data = data
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, count): return self.data
for never_match in [False, True]:
    with tempfile.TemporaryDirectory() as temporary:
        report = Path(temporary)/'report'; report.mkdir()
        os.environ.update(REPORT_DIR=str(report), RUNNER_TEMP=temporary,
            ATLAS_DEPTH_BOOTSTRAP_SHA256=v.digest(bootstrap), ATLAS_DEPTH_REGISTRY_SHA256=v.digest(registry_content))
        counter, clock = [0], [0.0]
        class Opener:
            def open(self, request, timeout):
                assert 0 < timeout <= 30
                assert not (Path(temporary)/'atlas-depth-bootstrap.py').exists()
                counter[0] += 1
                if request.full_url.endswith('.py'): return Response(bootstrap)
                return Response(b'stale' if never_match or counter[0] <= 2 else registry_content)
        urllib.request.build_opener = lambda *handlers: Opener()
        time.monotonic = lambda: clock[0]
        time.sleep = lambda seconds: clock.__setitem__(0, clock[0]+seconds)
        try:
            exec(${JSON.stringify(block)})
            assert not never_match
            assert (Path(temporary)/'atlas-depth-bootstrap.py').read_bytes()==bootstrap
            assert len(v.strict_json((report/'publication-checks.json').read_bytes()))==2
        except RuntimeError:
            assert never_match
            assert not (Path(temporary)/'atlas-depth-bootstrap.py').exists()
            assert clock[0] == 240
        attempts = v.strict_json((report/'publication-attempts.json').read_bytes())
        assert attempts[0]['passed'] is False
        assert attempts[0]['downloads'][-1]['sha256'] == v.digest(b'stale')
`);
});
