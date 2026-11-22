import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const base = 'code/fdtd/2026-11-22/';
const bytes = name => readFileSync(new URL(base+name, root));
const json = name => JSON.parse(bytes(name));
const hash = value => createHash('sha256').update(value).digest('hex');
const manifest = json('source-manifest.json');
const receipt = json('verification.json');
const cases = ['periodic-wave', 'pec-cavity'];

test('FDTD archive and independent-extraction receipt bind the exact fixed inputs, source and measurements', () => {
  assert.equal(manifest.family, 'fdtd');
  assert.equal(manifest.public_base_url, 'https://hrkoyama.github.io/'+base);
  for (const [name, expected] of Object.entries(manifest.files)) {
    assert.ok(!name.startsWith('/') && !name.split('/').includes('..'));
    assert.equal(hash(bytes(name)), expected, name);
  }
  assert.equal(receipt.returncode, 0);
  assert.ok(receipt.passed_tests > 0);
  assert.equal(receipt.tests, receipt.passed_tests);
  assert.equal(receipt.failures+receipt.errors+receipt.skipped, 0);
  assert.equal(hash(bytes(receipt.archive.file)), receipt.archive.sha256);
  assert.equal(receipt.archive.sha256, receipt.archive_sha256);
  assert.equal(receipt.archive.bytes, bytes(receipt.archive.file).length);
  assert.equal(hash(bytes('source-manifest.json')), receipt.source_manifest_sha256);
  const output = execFileSync('python3', ['-B', '-c', `
import hashlib,json,pathlib,stat,zipfile
base=pathlib.Path('${base}')
m=json.loads((base/'source-manifest.json').read_bytes())
prefix='fdtd-2026-11-22/'
with zipfile.ZipFile(base/'fdtd-2026-11-22.zip') as z:
 assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
 for info in z.infolist():
  assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
  assert not stat.S_ISLNK(info.external_attr >> 16)
 assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
 for name,expected in m['files'].items():
  assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified exact FDTD archive payload')
`], {cwd: root, encoding: 'utf8'});
  assert.match(output, /verified exact FDTD archive payload/);
});

test('both 2D TMz cases retain analytic accuracy, dispersion, grid refinement and distinct energy checks', () => {
  for (const name of cases) {
    const result = json(`results/${name}/result.json`);
    assert.equal(result.case, name);
    assert.equal(result.input_sha256, hash(bytes(`inputs/${name}.json`)));
    assert.equal(result.termination, 'fixed_budget_completed');
    assert.equal(result.passed, true);
    for (const check of ['field_accuracy', 'field_refinement', 'frequency_accuracy', 'frequency_refinement',
      'dispersion_identity', 'modified_energy', 'synchronized_energy_accuracy', 'synchronized_energy_refinement',
      'pec_boundary', 'magnetic_divergence_preserved']) assert.equal(result.checks[check], true, name+' '+check);
    const rows = result.metrics.meshes;
    assert.ok(rows.length >= 3);
    assert.ok(rows.every(row => row.nx !== row.ny && row.electric_relative_l2 > 0 && row.magnetic_relative_l2 > 0));
    assert.ok(rows.at(-1).field_relative_l2 < rows[0].field_relative_l2/10);
    assert.ok(rows.at(-1).relative_frequency_error < rows[0].relative_frequency_error/10);
    assert.ok(result.metrics.observed_orders.every(order => order > 1.8));
    assert.ok(result.metrics.physical_energy_error_orders.every(order => order > 1.8));
    assert.ok(result.metrics.finest_synchronized_energy_error > 0, 'Physical energy error differs from conserved modified energy drift');
    assert.ok(result.metrics.max_modified_energy_drift < 1e-10);
    assert.ok(result.metrics.max_dispersion_identity_error < 1e-10);
    if (name === 'pec-cavity') assert.equal(result.metrics.max_boundary_e, 0);
  }
});

test('FDTD method, search and bilingual reading expose only the verified dedicated supplement', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.deepEqual(record.code_urls, ['solver.py', 'run.py'].map(name => manifest.public_base_url+name));
  assert.deepEqual(record.test_urls, [manifest.public_base_url+'test_fdtd.py']);
  assert.deepEqual(record.execution_examples, [], 'Supplement has a separate extraction receipt, not a borrowed common execution');
  for (const extension of ['html', 'md']) {
    const text = readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.'+extension, root), 'utf8');
    assert.ok(text.includes(record.code_download));
    for (const name of cases) assert.ok(text.includes(record.result_urls[name]));
  }
  for (const language of ['ja', 'en']) {
    const doc = JSON.parse(readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.json`, root)));
    assert.equal(doc.implementation_status.fdtd, 'educational-example');
    for (const name of cases) assert.ok(doc.html.includes(base+`results/${name}/result.json`));
    const html = readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.html`, root), 'utf8');
    assert.ok(html.includes('katex-mathml') && !html.includes('math-placeholder'));
  }
});
