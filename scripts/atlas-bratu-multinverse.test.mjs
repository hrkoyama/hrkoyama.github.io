import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const base = 'code/bratu-multinverse/2026-11-22/';
const bytes = name => readFileSync(new URL(base+name, root));
const read = name => JSON.parse(bytes(name));
const sha = value => createHash('sha256').update(value).digest('hex');
const manifest = read('source-manifest.json');
const receipt = read('verification.json');
const evidence = read('docs/figures/bratu-multinverse.json');

test('multi-parameter inverse payload binds sources, fixed observations and unchanged earlier modules', () => {
  assert.equal(manifest.family, 'bratu-multinverse');
  assert.equal(manifest.version, '2026-11-22');
  assert.equal(manifest.public_base_url, 'https://hrkoyama.github.io/'+base);
  for (const [name, expected] of Object.entries(manifest.files)) {
    assert.ok(!name.startsWith('/') && !name.split('/').includes('..'));
    assert.equal(sha(bytes(name)), expected, name);
    if (/\.(?:py|md|json|txt)$/.test(name)) assert.doesNotMatch(bytes(name).toString(), /\/Users\/|\/private\//);
  }
  const previous = new URL('code/bratu-inverse/2026-11-22/', root);
  const provenance = read('provenance.json');
  assert.equal(Object.keys(provenance.unchanged_source_sha256).length, 4);
  for (const [name, expected] of Object.entries(provenance.unchanged_source_sha256)) {
    assert.equal(sha(bytes(name)), expected, name);
    assert.equal(sha(readFileSync(new URL(name, previous))), expected, 'unchanged: '+name);
  }
  const inputs = read('inputs/synthetic-observations.json');
  for (const [key, value] of Object.entries(evidence.observations)) assert.deepEqual(inputs[key], value, key);
  for (const [name, expected] of Object.entries(evidence.source_sha256)) assert.equal(sha(bytes(name)), expected, name);
  for (const [name, expected] of Object.entries(evidence.artifact_sha256)) assert.equal(sha(bytes(name)), expected, name);
});

test('multi-parameter inverse ZIP and independent extraction receipt identify the exact tested payload', () => {
  assert.equal(receipt.returncode, 0);
  assert.ok(receipt.tests > 0 && receipt.checked_fit_records > 0);
  assert.equal(receipt.passed_tests, receipt.tests);
  assert.equal(receipt.failures+receipt.errors+receipt.skipped, 0);
  assert.equal(receipt.archive.file, 'bratu-multinverse-2026-11-22.zip');
  assert.equal(sha(bytes(receipt.archive.file)), receipt.archive.sha256);
  assert.equal(receipt.archive.sha256, receipt.archive_sha256);
  assert.equal(bytes(receipt.archive.file).length, receipt.archive.bytes);
  assert.equal(sha(bytes('source-manifest.json')), receipt.source_manifest_sha256);
  assert.ok(Object.values(receipt.rerun_checks).every(value => value === true));
  const output = execFileSync('python3', ['-B', '-c', `
import hashlib,json,pathlib,stat,zipfile
base=pathlib.Path('${base}')
m=json.loads((base/'source-manifest.json').read_bytes())
prefix='bratu-multinverse-2026-11-22/'
with zipfile.ZipFile(base/'bratu-multinverse-2026-11-22.zip') as z:
 assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
 for info in z.infolist():
  assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
  assert not stat.S_ISLNK(info.external_attr >> 16)
 assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
 for name,expected in m['files'].items():
  assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified exact multi-parameter inverse archive payload')
`], {cwd:root, encoding:'utf8'});
  assert.match(output, /verified exact multi-parameter inverse archive payload/);
});

function* fitRecords(value) {
  if (Array.isArray(value)) {
    for (const child of value) yield* fitRecords(child);
  } else if (value && typeof value === 'object') {
    if (['converged','projected_gradient_inf','primal_residual_l2'].every(key => key in value)) yield value;
    for (const child of Object.values(value)) yield* fitRecords(child);
  }
}

test('saved multi-parameter fits separate data rank, prior curvature and optimization stationarity', () => {
  const fits = [...fitRecords(evidence)];
  assert.equal(fits.length, receipt.checked_fit_records);
  for (const row of fits) {
    assert.equal(row.parameters.length, 2);
    assert.ok(row.converged);
    assert.ok(row.projected_gradient_inf <= evidence.settings.gradient_tolerance);
    assert.ok(row.primal_residual_l2 <= evidence.settings.newton_tolerance_l2);
    for (let i=0; i<row.history.length-1; i++) {
      const current = row.history[i], next = row.history[i+1];
      assert.ok(next.objective <= current.objective);
      assert.ok(next.objective <= current.armijo_rhs);
    }
  }
  const ids = evidence.identifiability;
  assert.deepEqual(['full','center','center_symmetric','boundary'].map(key => ids[key].data_rank), [2,1,1,0]);
  for (const key of ['full','center','center_symmetric','boundary']) {
    assert.equal(ids[key].data_singular_values.length, 2);
    assert.equal(ids[key].right_singular_vectors.length, 2);
  }
  assert.equal(ids.center.data_singular_values[1], 0);
  assert.equal(ids.boundary.data_singular_values[0], 0);
  assert.ok(ids.full.data_singular_values[1] > 0);
  assert.ok(evidence.grid_runs.slice(1).every(row => row.parameter_order > 1.9 && row.parameter_order < 2.1));
  assert.ok(evidence.regularization_runs.some(row => row.gamma === 0));
  assert.ok(evidence.regularization_runs.some(row => row.gamma > 0));
  for (const row of evidence.regularization_runs) {
    assert.ok(row.reference_parameter_difference < 2e-6);
    assert.ok(row.clean.data_objective >= 0 && row.noisy.penalty >= 0);
  }
});

test('public multi-parameter entry links the new edition and retains the independently verified scalar edition', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/optimization/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.equal(record.code_archive_sha256, receipt.archive.sha256);
  assert.equal(record.passed_tests, receipt.passed_tests);
  assert.ok(record.code_urls.includes(manifest.public_base_url+'numart/bratu_multinverse.py'));
  assert.ok(record.test_urls.includes(manifest.public_base_url+'tests/test_bratu_multinverse.py'));
  assert.equal(record.scalar_inverse_release.code_base, 'https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/');
  assert.equal(record.scalar_inverse_release.passed_tests, 23);
  for (const extension of ['json','png']) {
    assert.deepEqual(readFileSync(new URL('numerical-methods-atlas/assets/bratu-multinverse.'+extension, root)), bytes('docs/figures/bratu-multinverse.'+extension));
  }
  for (const lang of ['ja','en']) {
    const html = readFileSync(new URL(`numerical-methods-atlas/${lang}/read/bratu-multi-inverse/index.html`, root), 'utf8');
    assert.ok(html.includes('bratu-multinverse.png'));
    assert.ok(html.includes(manifest.public_base_url.slice('https://hrkoyama.github.io'.length)));
    assert.equal(record.reading[lang], `https://hrkoyama.github.io/numerical-methods-atlas/${lang}/read/bratu-multi-inverse/`);
  }
});
