import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const base = 'code/bratu-inverse/2026-11-22/';
const bytes = name => readFileSync(new URL(base+name, root));
const read = name => JSON.parse(bytes(name));
const sha = value => createHash('sha256').update(value).digest('hex');
const manifest = read('source-manifest.json');
const receipt = read('verification.json');
const evidence = read('docs/figures/bratu-inverse.json');

test('inverse supplement binds all payload sources, fixed data and retained modules', () => {
  assert.equal(manifest.family, 'bratu-inverse');
  assert.equal(manifest.version, '2026-11-22');
  assert.equal(manifest.edition, manifest.version);
  assert.equal(manifest.public_base_url, 'https://hrkoyama.github.io/'+base);
  for (const [name, expected] of Object.entries(manifest.files)) {
    assert.ok(!name.startsWith('/') && !name.split('/').includes('..'));
    assert.equal(sha(bytes(name)), expected, name);
    if (/\.(?:py|md|json|txt)$/.test(name)) assert.doesNotMatch(bytes(name).toString(), /\/Users\/|\/private\//);
  }
  const previous = new URL('code/bratu-sensitivity/2026-11-22/', root);
  const provenance = read('provenance.json');
  assert.equal(Object.keys(provenance.unchanged_source_sha256).length, 3);
  for (const [name, expected] of Object.entries(provenance.unchanged_source_sha256)) {
    assert.equal(sha(bytes(name)), expected, name);
    assert.equal(sha(readFileSync(new URL(name, previous))), expected, 'unchanged earlier edition: '+name);
  }
  assert.deepEqual(read('inputs/synthetic-observations.json'), evidence.observations);
  for (const [name, expected] of Object.entries(evidence.source_sha256)) assert.equal(sha(bytes(name)), expected, name);
  for (const [name, expected] of Object.entries(evidence.artifact_sha256)) assert.equal(sha(bytes('docs/figures/'+name)), expected, name);
});

test('inverse archive receipt identifies 23 independently extracted passing tests and exact payload', () => {
  assert.equal(receipt.returncode, 0);
  assert.equal(receipt.tests, 23);
  assert.equal(receipt.passed_tests, receipt.tests);
  assert.equal(receipt.failures+receipt.errors+receipt.skipped, 0);
  assert.equal(receipt.archive.file, 'bratu-inverse-2026-11-22.zip');
  assert.equal(sha(bytes(receipt.archive.file)), receipt.archive.sha256);
  assert.equal(receipt.archive.sha256, receipt.archive_sha256);
  assert.equal(bytes(receipt.archive.file).length, receipt.archive.bytes);
  assert.equal(sha(bytes('source-manifest.json')), receipt.source_manifest_sha256);
  assert.ok(Object.values(receipt.rerun_checks).every(value => value === true));
  const output = execFileSync('python3', ['-c', `
import hashlib,json,pathlib,stat,zipfile
base=pathlib.Path('${base}')
m=json.loads((base/'source-manifest.json').read_bytes())
prefix='bratu-inverse-2026-11-22/'
with zipfile.ZipFile(base/'bratu-inverse-2026-11-22.zip') as z:
 assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
 for info in z.infolist():
  assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
  assert not stat.S_ISLNK(info.external_attr >> 16)
 assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
 for name,expected in m['files'].items():
  assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified exact inverse archive payload')
`], {cwd:root, encoding:'utf8'});
  assert.match(output, /verified exact inverse archive payload/);
});

test('inverse saved evidence distinguishes consistency, continuum bias, perturbations and stationarity', () => {
  assert.equal(evidence.settings.truth_alpha, 1.5);
  assert.ok(Math.abs(evidence.settings.truth_lambda-2.6846361372659913) < 1e-15);
  assert.deepEqual(evidence.settings.bounds, [.2, 3.4]);
  assert.deepEqual(evidence.observations.observation_positions, [.125, .25, .5, .75, .875]);
  assert.deepEqual(evidence.multistart.map(row => row.initial), [.5, 1.5, 3.2]);
  assert.deepEqual(evidence.grid_runs.map(row => row.n), [15, 31, 63, 127]);
  const fits = [...evidence.multistart, ...evidence.grid_runs, evidence.noisy_run];
  assert.equal(fits.length, 8);
  for (const row of fits) {
    assert.ok(row.converged);
    assert.match(row.reason, /projected adjoint-gradient tolerance/);
    assert.ok(row.projected_gradient <= evidence.settings.gradient_tolerance);
    assert.ok(row.primal_residual_l2 <= evidence.settings.newton_tolerance_l2);
    assert.ok(row.adjoint_residual_relative_l2 < 1e-10);
    assert.equal(row.accepted_steps+1, row.history.length);
    for (let i=0; i<row.history.length-1; i++) {
      const current = row.history[i], next = row.history[i+1];
      assert.ok(next.objective <= current.objective);
      assert.ok(next.objective <= current.armijo_rhs);
      const projected = Math.max(.2, Math.min(3.4, current.lambda_value-current.accepted_step*current.gradient));
      assert.equal(next.lambda_value, projected);
    }
  }
  for (const row of evidence.multistart) assert.ok(row.absolute_parameter_error < 3e-9);
  for (const row of evidence.grid_runs.slice(1)) assert.ok(row.parameter_order > 1.9 && row.parameter_order < 2.1);
  for (const row of [...evidence.grid_runs, evidence.noisy_run]) {
    assert.ok(row.reference_parameter_difference < 2e-8);
    assert.ok(row.objective_only_reference.interval_width <= 1e-8);
  }
  assert.ok(evidence.noisy_run.data_rms > 5e-4);
  assert.ok(Math.abs(evidence.noisy_run.parameter_shift_from_noiseless_same_grid) > 2e-4);
  assert.equal(evidence.boundary_only_diagnostic.observation_matrix_rank, 0);
  assert.deepEqual(evidence.boundary_only_diagnostic.objectives, [0, 0]);
  assert.deepEqual(evidence.boundary_only_diagnostic.gradients, [0, 0]);
  for (const row of evidence.gradient_checks) {
    assert.ok(Math.abs(row.adjoint_reference) > .02);
    assert.ok(row.gradient_absolute_error < 1e-9);
    assert.ok(row.direct_adjoint_difference < 1e-12);
  }
  const tight = evidence.parameter_sweep.filter(row => row.solve_tolerance === 1e-10);
  const best = Math.min(...tight.map(row => row.gradient_absolute_error));
  assert.equal(tight.length, 17);
  assert.ok(best < 1e-10);
  assert.ok(tight[0].gradient_absolute_error > 100*best);
  assert.ok(tight.at(-1).gradient_absolute_error > 100*best);
  for (const row of evidence.parameter_sweep) {
    assert.ok(row.plus_lambda > row.minus_lambda);
    assert.ok(row.plus_primal_residual_l2 <= row.solve_tolerance);
    assert.ok(row.minus_primal_residual_l2 <= row.solve_tolerance);
  }
  const scan = evidence.objective_scan;
  const minimum = scan.findIndex(row => row.objective === Math.min(...scan.map(row => row.objective)));
  assert.ok(minimum > 0 && minimum < scan.length-1);
  for (let i=1; i<=minimum; i++) assert.ok(scan[i].objective < scan[i-1].objective);
  for (let i=minimum+1; i<scan.length; i++) assert.ok(scan[i].objective > scan[i-1].objective);
});

test('published optimization entry and bilingual inverse chapter use the verified supplement', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/optimization/index.json', root)));
  assert.equal(record.status, 'educational-example');
  const scalar = record.scalar_inverse_release || record;
  assert.equal(scalar.code_base, manifest.public_base_url);
  assert.equal(scalar.code_download, manifest.public_base_url+receipt.archive.file);
  assert.equal(scalar.code_verification, manifest.public_base_url+'verification.json');
  assert.ok(scalar.code_urls.includes(manifest.public_base_url+'numart/bratu_inverse.py'));
  assert.ok(scalar.test_urls.includes(manifest.public_base_url+'tests/test_bratu_inverse.py'));
  for (const extension of ['json', 'png']) {
    assert.deepEqual(readFileSync(new URL('numerical-methods-atlas/assets/bratu-inverse.'+extension, root)),
                     bytes('docs/figures/bratu-inverse.'+extension));
  }
  for (const lang of ['ja', 'en']) {
    const html = readFileSync(new URL(`numerical-methods-atlas/${lang}/read/bratu-inverse/index.html`, root), 'utf8');
    assert.match(html, /Bratu/);
    assert.match(html, /bratu-inverse\.png/);
    assert.ok(html.includes(manifest.public_base_url.slice('https://hrkoyama.github.io'.length)));
  }
});
