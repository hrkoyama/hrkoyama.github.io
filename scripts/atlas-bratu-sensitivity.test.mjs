import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const base = 'code/bratu-sensitivity/2026-11-22/';
const bytes = name => readFileSync(new URL(base+name, root));
const read = name => JSON.parse(bytes(name));
const sha = value => createHash('sha256').update(value).digest('hex');
const manifest = read('source-manifest.json');
const receipt = read('verification.json');
const evidence = read('docs/figures/bratu-sensitivity.json');

test('implicit-adjoint supplement binds its public sources, original AD code and numerical evidence', () => {
  assert.equal(manifest.family, 'bratu-sensitivity');
  assert.equal(manifest.version, '2026-11-22');
  assert.equal(manifest.public_base_url, 'https://hrkoyama.github.io/'+base);
  for (const [name, expected] of Object.entries(manifest.files)) {
    assert.ok(!name.startsWith('/') && !name.split('/').includes('..'));
    assert.equal(sha(bytes(name)), expected, name);
  }
  const previous = new URL('code/autodiff/2026-11-22/', root);
  const provenance = read('provenance.json');
  for (const [name, expected] of Object.entries(provenance.unchanged_source_sha256)) {
    assert.equal(sha(bytes(name)), expected, name);
    assert.equal(sha(readFileSync(new URL(name, previous))), expected, 'unchanged older edition: '+name);
  }
  for (const [name, expected] of Object.entries(evidence.source_sha256)) assert.equal(sha(bytes(name)), expected, name);
  for (const [name, expected] of Object.entries(evidence.artifact_sha256)) assert.equal(sha(bytes('docs/figures/'+name)), expected, name);
  assert.doesNotMatch(bytes('README.md').toString(), /koyamarium|\/Users\/|\/private\//);
});

test('independent nine-test extraction and rebuilt evidence describe the exact published ZIP', () => {
  assert.equal(receipt.returncode, 0);
  assert.equal(receipt.tests, 9);
  assert.equal(receipt.passed_tests, 9);
  assert.equal(receipt.failures+receipt.errors+receipt.skipped, 0);
  assert.equal(receipt.archive.file, 'bratu-sensitivity-2026-11-22.zip');
  assert.equal(sha(bytes(receipt.archive.file)), receipt.archive.sha256);
  assert.equal(receipt.archive.sha256, receipt.archive_sha256);
  assert.equal(bytes(receipt.archive.file).length, receipt.archive.bytes);
  assert.equal(sha(bytes('source-manifest.json')), receipt.source_manifest_sha256);
  assert.ok(Object.values(receipt.rerun_checks).every(value => value === true));
  const output = execFileSync('python3', ['-c', `
import hashlib,json,pathlib,stat,zipfile
base=pathlib.Path('${base}')
m=json.loads((base/'source-manifest.json').read_bytes())
prefix='bratu-sensitivity-2026-11-22/'
with zipfile.ZipFile(base/'bratu-sensitivity-2026-11-22.zip') as z:
 assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
 for info in z.infolist():
  assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
  assert not stat.S_ISLNK(info.external_attr >> 16)
 assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
 for name,expected in m['files'].items():
  assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified exact sensitivity archive payload')
`], {cwd:root, encoding:'utf8'});
  assert.match(output, /verified exact sensitivity archive payload/);
});

test('saved implicit and adjoint checks keep primal, linear and continuum errors separate', () => {
  assert.equal(evidence.settings.beta, .05);
  assert.deepEqual(evidence.settings.interior_nodes, [15, 31, 63]);
  assert.deepEqual(evidence.settings.alphas, [1, 2]);
  assert.equal(evidence.grid_runs.length, 6);
  for (const alpha of [1, 2]) {
    const runs = evidence.grid_runs.filter(run => run.alpha === alpha);
    assert.deepEqual(runs.map(run => run.n), [15, 31, 63]);
    for (const run of runs) {
      assert.ok(run.converged);
      assert.ok(run.primal_residual_l2 <= evidence.settings.newton_tolerance_l2);
      assert.ok(run.sensitivity_residual_relative_l2 < 1e-11);
      assert.ok(run.adjoint_residual_relative_l2 < 1e-11);
      assert.ok(run.direct_adjoint_difference < 1e-12);
      assert.ok(run.ad_parameter_maximum_difference < 1e-13);
      assert.ok(run.sensitivity_error_linf > 1e-7, 'Spatial error is not the tangent residual');
      assert.ok(Math.abs(run.adjoint_gradient-run.explicit_gradient) > .01);
    }
    for (const run of runs.slice(1)) {
      assert.ok(run.sensitivity_order > 1.9 && run.sensitivity_order < 2.1);
      assert.ok(run.gradient_order > 1.9 && run.gradient_order < 2.1);
    }
    const rows = evidence.parameter_sweep.filter(row => row.alpha === alpha);
    assert.equal(rows.length, 17);
    const best = Math.min(...rows.map(row => row.gradient_absolute_error));
    assert.ok(best < 1e-8);
    assert.ok(rows[0].gradient_absolute_error > 100*best);
    assert.ok(rows.at(-1).gradient_absolute_error > 100*best);
    for (const row of rows) {
      assert.ok(row.plus_primal_residual_l2 <= row.solve_tolerance);
      assert.ok(row.minus_primal_residual_l2 <= row.solve_tolerance);
      assert.ok(row.plus_lambda > row.minus_lambda);
    }
  }
  const nonsymmetric = evidence.nonsymmetric_check;
  assert.ok(nonsymmetric.matrix.some((row, i) => row.some((value, j) => value !== nonsymmetric.matrix[j][i])));
  assert.equal(nonsymmetric.parameter_rhs[0].length, 2);
  assert.ok(nonsymmetric.maximum_gradient_difference < 1e-12);
  for (const row of evidence.continuous_references) assert.ok(row.quadrature_difference < 1e-12);
});

test('published adjoint entry and both reading editions point to the same verified sensitivity supplement', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/adjoint/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.equal(record.code_verification, manifest.public_base_url+'verification.json');
  assert.ok(record.code_urls.includes(manifest.public_base_url+'numart/bratu_sensitivity.py'));
  assert.ok(record.test_urls.includes(manifest.public_base_url+'tests/test_bratu_sensitivity.py'));
  for (const extension of ['json', 'png']) {
    assert.deepEqual(readFileSync(new URL('numerical-methods-atlas/assets/bratu-sensitivity.'+extension, root)),
                     bytes('docs/figures/bratu-sensitivity.'+extension));
  }
  for (const lang of ['ja', 'en']) {
    const html = readFileSync(new URL(`numerical-methods-atlas/${lang}/read/adjoint/index.html`, root), 'utf8');
    assert.match(html, /Bratu/);
    assert.match(html, /bratu-sensitivity\.png/);
    assert.ok(html.includes(manifest.public_base_url.slice('https://hrkoyama.github.io'.length)));
  }
});
