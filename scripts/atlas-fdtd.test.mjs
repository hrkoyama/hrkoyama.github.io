import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const originalEdition = '2026-11-22';
const edition = '2026-11-22-r2';
const base = `code/fdtd/${edition}/`;
const originalBase = `code/fdtd/${originalEdition}/`;
const bytes = name => readFileSync(new URL(base+name, root));
const originalBytes = name => readFileSync(new URL(originalBase+name, root));
const json = name => JSON.parse(bytes(name));
const hash = value => createHash('sha256').update(value).digest('hex');
const manifest = json('source-manifest.json');
const receipt = json('verification.json');
const legacyCases = ['periodic-wave', 'pec-cavity'];
const scatteringCases = ['dielectric-interface', 'pml-pulse'];
const cases = [...legacyCases, ...scatteringCases];

function checkEdition(version) {
  const prefix = `code/fdtd/${version}/`;
  const get = name => readFileSync(new URL(prefix+name, root));
  const metadata = JSON.parse(get('source-manifest.json'));
  const verification = JSON.parse(get('verification.json'));
  assert.equal(metadata.family, 'fdtd');
  assert.equal(metadata.public_base_url, 'https://hrkoyama.github.io/'+prefix);
  for (const [name, expected] of Object.entries(metadata.files)) {
    assert.ok(!name.startsWith('/') && !name.split('/').includes('..'));
    assert.equal(hash(get(name)), expected, name);
  }
  assert.equal(verification.returncode, 0);
  assert.ok(verification.passed_tests > 0);
  assert.equal(verification.tests, verification.passed_tests);
  assert.equal(verification.failures+verification.errors+verification.skipped, 0);
  assert.equal(hash(get(verification.archive.file)), verification.archive.sha256);
  assert.equal(verification.archive.sha256, verification.archive_sha256);
  assert.equal(verification.archive.bytes, get(verification.archive.file).length);
  assert.equal(hash(get('source-manifest.json')), verification.source_manifest_sha256);
  return {get, metadata, verification};
}

test('the original vacuum FDTD edition remains byte-identical and both ZIP payloads match their manifests', () => {
  const original = checkEdition(originalEdition);
  checkEdition(edition);
  assert.equal(original.verification.archive.sha256, '482404475f935e8df487580ed48b8f98ada580fd61a79dd705fef9d5cf620d4d');
  for (const name of ['solver.py','run.py','test_fdtd.py', ...legacyCases.map(name=>`inputs/${name}.json`)]) {
    assert.deepEqual(bytes(name), originalBytes(name), 'Retained vacuum source/input: '+name);
  }
  const output = execFileSync('python3', ['-B', '-c', `
import hashlib,json,pathlib,stat,zipfile
for edition in ['${originalEdition}','${edition}']:
 base=pathlib.Path('code/fdtd')/edition
 m=json.loads((base/'source-manifest.json').read_bytes())
 prefix='fdtd-'+edition+'/'
 with zipfile.ZipFile(base/('fdtd-'+edition+'.zip')) as z:
  assert set(z.namelist())=={prefix+n for n in [*m['files'],'source-manifest.json']}
  for info in z.infolist():
   assert not info.filename.startswith('/') and '..' not in info.filename.split('/')
   assert not stat.S_ISLNK(info.external_attr >> 16)
  assert z.read(prefix+'source-manifest.json')==(base/'source-manifest.json').read_bytes()
  for name,expected in m['files'].items():
   assert hashlib.sha256(z.read(prefix+name)).hexdigest()==expected,name
print('verified both exact FDTD archive payloads')
`], {cwd: root, encoding: 'utf8'});
  assert.match(output, /verified both exact FDTD archive payloads/);
});

test('the new dedicated edition independently reran all four inputs and binds the scattering code to its results', () => {
  assert.ok(receipt.passed_tests > 24);
  assert.deepEqual(receipt.recipes.map(row=>row.id).sort(), cases.slice().sort());
  for (const recipe of receipt.recipes) {
    assert.equal(recipe.passed, true);
    assert.equal(recipe.metrics_identical, true);
    assert.equal(recipe.csv_identical, true);
    assert.equal(recipe.input_sha256, hash(bytes(`inputs/${recipe.id}.json`)));
  }
  for (const name of ['scattering.py','run_scattering.py','test_scattering.py']) assert.ok(manifest.files[name]);
  for (const name of cases) {
    const result = json(`results/${name}/result.json`);
    assert.equal(result.case, name);
    assert.equal(result.input_sha256, hash(bytes(`inputs/${name}.json`)));
    assert.equal(result.termination, 'fixed_budget_completed');
    assert.equal(result.passed, true);
    assert.ok(Object.keys(result.checks).length > 0);
    assert.ok(Object.values(result.checks).every(value=>value===true));
    for (const output of ['result.json','summary.png','convergence.csv','energy.csv','solution.csv']) assert.ok(manifest.files[`results/${name}/${output}`]);
    assert.ok(result.metrics.meshes.length >= 3);
  }
});

test('the retained vacuum examples still meet independent continuum, dispersion and energy criteria', () => {
  for (const name of legacyCases) {
    const result = json(`results/${name}/result.json`);
    const original = JSON.parse(originalBytes(`results/${name}/result.json`));
    assert.deepEqual(result.metrics, original.metrics);
    for (const check of ['field_accuracy', 'field_refinement', 'frequency_accuracy', 'frequency_refinement',
      'dispersion_identity', 'modified_energy', 'synchronized_energy_accuracy', 'synchronized_energy_refinement',
      'pec_boundary', 'magnetic_divergence_preserved']) assert.equal(result.checks[check], true, name+' '+check);
    const rows = result.metrics.meshes;
    assert.ok(rows.every(row => row.nx !== row.ny && row.electric_relative_l2 > 0 && row.magnetic_relative_l2 > 0));
    assert.ok(rows.at(-1).field_relative_l2 < rows[0].field_relative_l2/10);
    assert.ok(rows.at(-1).relative_frequency_error < rows[0].relative_frequency_error/10);
    assert.ok(result.metrics.observed_orders.every(order => order > 1.8));
    assert.ok(result.metrics.physical_energy_error_orders.every(order => order > 1.8));
    assert.ok(result.metrics.finest_synchronized_energy_error > 0);
    assert.ok(result.metrics.max_modified_energy_drift < 1e-10);
    assert.ok(result.metrics.max_dispersion_identity_error < 1e-10);
    if (name === 'pec-cavity') assert.equal(result.metrics.max_boundary_e, 0);
  }
});

test('the dielectric pulse is compared with lossless Fresnel amplitudes and energy fractions under refinement', () => {
  const input=json('inputs/dielectric-interface.json');
  const result=json('results/dielectric-interface/result.json');
  const rows=result.metrics.meshes;
  const a=input.acceptance;
  const n1=Math.sqrt(input.epsilon_left),n2=Math.sqrt(input.epsilon_right);
  const r=(n1-n2)/(n1+n2),t=2*n1/(n1+n2),R=r*r,T=n2/n1*t*t;
  assert.ok(Math.abs(R+T-1)<1e-14);
  assert.deepEqual(rows.map(row=>row.nx),input.meshes);
  assert.ok(rows.every(row=>row.ny===input.transverse_cells));
  for(const row of rows){
    for(const [name,expected] of Object.entries({analytic_r:r,analytic_t:t,analytic_R:R,analytic_T:T}))assert.ok(Math.abs(row[name]-expected)<1e-14,name);
    assert.ok(Math.abs(row.energy_fraction_closure-Math.abs(row.reflected_energy_fraction+row.transmitted_energy_fraction-1))<1e-14);
    assert.ok(row.modified_energy_max_relative_drift<=a.max_modified_energy_drift);
  }
  const last=rows.at(-1);
  assert.ok(last.field_relative_l2<=a.max_field_error);
  assert.ok(Math.abs(last.reflection_amplitude-r)<=a.max_amplitude_error);
  assert.ok(Math.abs(last.transmission_amplitude-t)<=a.max_amplitude_error);
  assert.ok(Math.abs(last.reflected_energy_fraction-R)<=a.max_energy_fraction_error);
  assert.ok(Math.abs(last.transmitted_energy_fraction-T)<=a.max_energy_fraction_error);
  assert.ok(last.energy_fraction_closure<=a.max_energy_closure);
  assert.ok(result.metrics.field_orders.every(order=>order>=a.min_refinement_order));
});

test('normal and oblique PML pulses retain fixed physical thickness, return-wave and two energy-budget checks', () => {
  const input=json('inputs/pml-pulse.json');
  const result=json('results/pml-pulse/result.json');
  const a=input.acceptance;
  assert.ok(input.transverse_wave_numbers.includes(0));
  assert.ok(input.transverse_wave_numbers.some(ky=>ky>0));
  assert.deepEqual(result.metrics.series.map(row=>row.ky),input.transverse_wave_numbers);
  for(const series of result.metrics.series){
    const rows=result.metrics.meshes.filter(row=>row.ky===series.ky);
    assert.deepEqual(rows.map(row=>[row.nx,row.ny]),input.meshes);
    for(const row of rows){
      assert.equal(row.pml_thickness,input.pml_thickness);
      assert.equal(row.pml_strength,input.pml_strength);
      assert.ok(Math.abs(row.pml_cells*row.dx-input.pml_thickness)<1e-12);
      assert.ok(row.reference_domain_length>input.lengths[0]);
      assert.ok(Math.abs(row.reflected_peak_intensity_ratio-row.reflection_amplitude_ratio**2)<1e-14);
      assert.ok(row.modified_energy_budget_relative_residual<=a.max_work_budget_residual);
      assert.ok(Math.abs(row.total_pml_work_fraction-row.electric_pml_work_fraction-row.magnetic_pml_work_fraction)<1e-12);
    }
    const last=rows.at(-1);
    assert.ok(last.field_relative_l2<=a.max_field_error);
    assert.ok(last.reflection_amplitude_ratio<=a.max_reflection_amplitude);
    assert.ok(last.physical_region_flux_budget_max_relative_residual<=a.max_flux_budget_residual);
    assert.ok(last.total_pml_work_fraction>.99);
    assert.ok(last.remaining_physical_energy_fraction<=a.max_remaining_energy_fraction);
    assert.ok(series.field_orders.every(order=>order>=a.min_field_refinement_order));
    assert.ok(series.reflection_orders.every(order=>order>=a.min_reflection_refinement_order));
    assert.ok(series.flux_budget_orders.every(order=>order>=a.min_flux_refinement_order));
  }
});

test('FDTD method and bilingual reading expose the new supplement and retain the original release', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.deepEqual(record.code_urls, ['solver.py', 'run.py','scattering.py','run_scattering.py'].map(name => manifest.public_base_url+name));
  assert.deepEqual(record.test_urls, ['test_fdtd.py','test_scattering.py'].map(name=>manifest.public_base_url+name));
  assert.deepEqual(record.execution_examples, [], 'Supplement has its own extraction receipt; common registry remains separately verified');
  assert.deepEqual(Object.keys(record.result_urls).sort(), cases.slice().sort());
  for (const extension of ['html', 'md']) {
    const text = readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.'+extension, root), 'utf8');
    assert.ok(text.includes(record.code_download));
    for (const name of cases) assert.ok(text.includes(record.result_urls[name]));
  }
  for (const language of ['ja', 'en']) {
    const doc = JSON.parse(readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.json`, root)));
    assert.equal(doc.implementation_status.fdtd, 'educational-example');
    for (const name of scatteringCases) assert.ok(doc.html.includes(base+`results/${name}/result.json`));
    assert.ok(doc.html.includes(originalBase+`fdtd-${originalEdition}.zip`));
    assert.ok(doc.html.includes(base+`fdtd-${edition}.zip`));
    for (const name of cases) {
      assert.deepEqual(readFileSync(new URL(`numerical-methods-atlas/assets/fdtd-${name}.png`,root)), bytes(`results/${name}/summary.png`));
    }
    const html = readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.html`, root), 'utf8');
    assert.ok(html.includes('katex-mathml') && !html.includes('math-placeholder'));
  }
});
