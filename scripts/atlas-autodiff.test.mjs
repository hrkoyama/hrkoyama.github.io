import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const release = 'code/autodiff/2026-11-22/';
const bytes = name => readFileSync(new URL(release+name, root));
const read = name => JSON.parse(bytes(name));
const sha = data => createHash('sha256').update(data).digest('hex');
const manifest = read('source-manifest.json');
const verified = read('verification.json');
const evidence = read('docs/figures/autodiff-bratu.json');

test('minimal AD release inventories exact public payload hashes and original code provenance', () => {
  assert.equal(manifest.schema_version, 1);
  assert.equal(manifest.family, 'autodiff');
  assert.equal(manifest.edition, '2026-11-22');
  assert.equal(manifest.public_base_url, 'https://hrkoyama.github.io/'+release);
  assert.deepEqual(Object.keys(manifest.files).sort(), [
    'LICENSE', 'LICENSING.md', 'README.md',
    'docs/figures/autodiff-bratu.json', 'docs/figures/autodiff-bratu.png',
    'numart/__init__.py', 'numart/autodiff.py', 'numart/krylov.py',
    'provenance.json', 'requirements.txt', 'scripts/build_autodiff.py',
    'tests/test_autodiff.py'
  ].sort());
  for (const [path, expected] of Object.entries(manifest.files)) {
    assert.ok(!path.startsWith('/') && !path.split('/').includes('..'));
    assert.equal(sha(bytes(path)), expected, path);
  }
  const provenance = read('provenance.json');
  for (const path of provenance.unchanged_code) {
    assert.equal(sha(bytes(path)), provenance.original_source_sha256[path], path);
  }
  for (const [path, expected] of Object.entries(evidence.source_sha256)) {
    assert.equal(sha(bytes(path)), expected, path);
  }
  for (const [path, expected] of Object.entries(evidence.artifact_sha256)) {
    assert.equal(sha(bytes('docs/figures/'+path)), expected, path);
  }
  assert.match(bytes('README.md').toString(), /\/ja\/read\/automatic-differentiation\//);
  assert.match(bytes('README.md').toString(), /\/en\/read\/automatic-differentiation\//);
  assert.doesNotMatch(bytes('README.md').toString(), /koyamarium|\/Users\/|\/private\//);
});

test('independently extracted eight-test verification binds the exact published ZIP', () => {
  assert.equal(verified.returncode, 0);
  assert.equal(verified.tests, 8);
  assert.equal(verified.passed_tests, 8);
  assert.equal(verified.passed, 8);
  assert.equal(verified.failures+verified.errors+verified.skipped, 0);
  assert.equal(verified.archive.file, 'autodiff-2026-11-22.zip');
  assert.equal(verified.archive.archive_directory, 'autodiff-2026-11-22');
  assert.equal(sha(bytes(verified.archive.file)), verified.archive_sha256);
  assert.equal(verified.archive.sha256, verified.archive_sha256);
  assert.equal(bytes(verified.archive.file).length, verified.archive.bytes);
  assert.equal(sha(bytes('source-manifest.json')), verified.source_manifest_sha256);
  assert.ok(Object.values(verified.rerun_checks).every(value => value === true));
  const output = execFileSync('python3', ['-c', `
import hashlib,json,pathlib,stat,zipfile
base=pathlib.Path('${release}')
m=json.loads((base/'source-manifest.json').read_bytes())
prefix='autodiff-2026-11-22/'
with zipfile.ZipFile(base/'autodiff-2026-11-22.zip') as z:
 assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
 for info in z.infolist():
  assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
  assert not stat.S_ISLNK(info.external_attr >> 16)
 assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
 for name,expected in m['files'].items():
  assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified exact archive payload')
`], {cwd:root, encoding:'utf8'});
  assert.match(output, /verified exact archive payload/);
});

test('saved Bratu evidence separates derivative agreement, common root and spatial refinement', () => {
  assert.equal(evidence.derivative_checks.n, 31);
  assert.equal(evidence.derivative_checks.primal_maximum_difference, 0);
  assert.ok(evidence.derivative_checks.jacobian_relative_frobenius_error <= 1e-13);
  assert.ok(evidence.derivative_checks.jvp_relative_l2_error <= 1e-12);
  assert.equal(evidence.settings.newton_tolerance_l2, 1e-10);
  assert.equal(evidence.settings.finite_difference_absolute_step, 1e-5);
  assert.equal(evidence.newton_runs.length, 9);
  for (const method of ['analytic', 'finite_difference', 'autodiff']) {
    const runs = evidence.newton_runs.filter(run => run.method === method);
    assert.deepEqual(runs.map(run => run.n), [15,31,63]);
    for (const run of runs) {
      assert.equal(run.converged, true);
      assert.equal(run.iterations, 3);
      assert.ok(run.final_residual_l2 <= evidence.settings.newton_tolerance_l2);
      assert.ok(run.difference_from_analytic_root_linf < 1e-12);
      assert.equal(run.solution.length, run.n);
      assert.ok(run.continuous_error_linf > 1e-6);
    }
    for (const run of runs.slice(1)) assert.ok(run.continuous_error_order > 1.9 && run.continuous_error_order < 2.1);
  }
  assert.equal(evidence.difference_sweep.length, 29);
  for (const scheme of ['forward', 'central']) {
    const errors = evidence.difference_sweep.map(row => row[scheme+'_jvp_relative_l2_error']);
    const best = Math.min(...errors);
    assert.ok(errors[0] > 100*best, 'large-step truncation error');
    assert.ok(errors.at(-1) > 100*best, 'small-step cancellation/roundoff');
  }
});
