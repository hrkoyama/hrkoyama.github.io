import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const originalEdition = '2026-11-22';
const secondEdition = '2026-11-22-r2';
const edition = '2026-11-22-r3';
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
const cornerCases = ['pml-corners'];
const retainedCases = [...legacyCases, ...scatteringCases];
const cases = [...retainedCases, ...cornerCases];

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

test('both previous FDTD editions remain byte-identical and all three ZIP payloads match their manifests', () => {
  const original = checkEdition(originalEdition);
  const second = checkEdition(secondEdition);
  checkEdition(edition);
  assert.equal(second.verification.archive.sha256, '50f8dad211f0b5fa54c538c9f272ec2509bc8740063f6b4e4c3ec907d8f7adcc');
  assert.equal(original.verification.archive.sha256, '482404475f935e8df487580ed48b8f98ada580fd61a79dd705fef9d5cf620d4d');
  for (const name of ['solver.py','run.py','test_fdtd.py', ...legacyCases.map(name=>`inputs/${name}.json`)]) {
    assert.deepEqual(bytes(name), originalBytes(name), 'Retained vacuum source/input: '+name);
  }
  const output = execFileSync('python3', ['-B', '-c', `
import hashlib,json,pathlib,stat,zipfile
for edition in ['${originalEdition}','${secondEdition}','${edition}']:
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
print('verified all three exact FDTD archive payloads')
`], {cwd: root, encoding: 'utf8'});
  assert.match(output, /verified all three exact FDTD archive payloads/);
});

test('the new dedicated edition independently reran all five inputs and binds its code to measured results', () => {
  assert.ok(receipt.passed_tests > 43);
  assert.deepEqual(receipt.recipes.map(row=>row.id).sort(), cases.slice().sort());
  for (const recipe of receipt.recipes) {
    assert.equal(recipe.passed, true);
    assert.equal(recipe.metrics_identical, true);
    assert.equal(recipe.csv_identical, true);
    assert.equal(recipe.input_sha256, hash(bytes(`inputs/${recipe.id}.json`)));
  }
  for (const name of ['scattering.py','run_scattering.py','test_scattering.py','corner.py','run_corner.py','test_corner.py']) assert.ok(manifest.files[name]);
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

test('r3 retains all r2 numerical source, fixed inputs and saved measurement values', () => {
  const previous = name => readFileSync(new URL(`code/fdtd/${secondEdition}/${name}`, root));
  for (const name of ['solver.py','run.py','test_fdtd.py','scattering.py','run_scattering.py','test_scattering.py',
      ...retainedCases.map(name=>`inputs/${name}.json`)]) assert.deepEqual(bytes(name), previous(name), name);
  for (const name of retainedCases) {
    const before=JSON.parse(previous(`results/${name}/result.json`));
    assert.deepEqual(json(`results/${name}/result.json`).metrics,before.metrics,name+' retains measured values');
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

test('four-side and corner packets exercise both damping pairs, every side and actual corner overlaps', () => {
  const input=json('inputs/pml-corners.json');
  const result=json('results/pml-corners/result.json');
  const a=input.acceptance;
  const rows=result.metrics.meshes;
  const sides=['bottom','left','right','top'];
  const corners=['NE','NW','SE','SW'];
  const directions=['electric_x','electric_y','magnetic_x','magnetic_y'];
  const finite=value=>typeof value==='number'&&Number.isFinite(value);
  assert.deepEqual(input.families,['axis','diagonal']);
  assert.equal(rows.length,input.families.length*input.meshes.length);
  assert.deepEqual(result.metrics.series.map(row=>row.family),input.families);
  assert.match(result.reflection_scope,/initial PML\/auxiliary tails/);
  assert.match(result.reflection_scope,/not pure ideal-PML reflection/);
  assert.ok(manifest.files['results/pml-corners/waveforms.csv']);
  for(const check of ['continuum_accuracy','continuum_refinement','reflection_amplitude',
    'reflected_waveform_refinement','independent_work_balance','physical_flux_balance',
    'physical_flux_refinement','late_energy','reference_period_control',
    'reference_below_return_signal','initial_layer_tail','initial_layer_sensitivity_below_return','gate_contains_global_peak',
    'all_four_sides','all_four_corners'])assert.equal(result.checks[check],true,check);
  for(const family of input.families){
    const values=rows.filter(row=>row.family===family);
    const series=result.metrics.series.find(row=>row.family===family);
    assert.deepEqual(values.map(row=>[row.nx,row.ny]),input.meshes.map(n=>[n,n]));
    assert.deepEqual(values.map(row=>row.steps),[1,2,4].map(factor=>values[0].steps*factor));
    for(const row of values){
      assert.ok(Math.abs(row.dx-input.length/row.nx)<1e-14);
      assert.ok(Math.abs(row.dt*row.steps-input.end_time)<1e-12);
      assert.equal(row.pml_thickness,input.pml_thickness);
      assert.equal(row.pml_strength,input.pml_strength);
      assert.ok(Math.abs(row.pml_cells*row.dx-input.pml_thickness)<1e-12);
      assert.equal(row.reference_period,input.reference_period);
      assert.ok(Number.isInteger(row.spectrum_mode_count)&&row.spectrum_mode_count>1);
      assert.ok(finite(row.spectrum_dk)&&row.spectrum_dk>0);
      assert.ok(finite(row.spectrum_kmax)&&Math.abs(row.spectrum_kmax-input.spectral_cutoff)<=row.spectrum_dk/2+1e-12);
      assert.ok(row.spectrum_kmax<Math.PI*input.meshes[0]/input.length,'Actual finite modes stay below every grid Nyquist');
      assert.ok(row.modified_energy_budget_relative_residual<=a.max_work_residual);
      assert.ok(row.initial_layer_energy_fraction>=0&&row.initial_layer_energy_fraction<=a.max_initial_layer_energy_fraction);
      for(const key of ['initial_layer_electric_field_max','initial_layer_split_electric_field_max',
        'initial_layer_magnetic_field_max','initial_unclipped_cap_electric_field_max',
        'global_return_amplitude_ratio','excluded_early_return_peak_ratio'])assert.ok(finite(row[key])&&row[key]>=0,key);
      assert.deepEqual(Object.keys(row.directional_work_fractions).sort(),directions);
      assert.ok(Object.values(row.directional_work_fractions).every(finite));
      const work=Object.values(row.directional_work_fractions).reduce((sum,value)=>sum+value,0);
      assert.ok(Math.abs(work-row.total_pml_work_fraction)<1e-11,'Both electric and magnetic damping directions enter the budget');
      assert.deepEqual(Object.keys(row.side_flux_fractions).sort(),sides);
      assert.deepEqual(Object.keys(row.corner_work_fractions).sort(),corners);
      assert.deepEqual(Object.keys(row.corner_abs_work_fractions).sort(),corners);
      assert.deepEqual(Object.keys(row.corner_max_electric_fields).sort(),corners);
      for(const corner of corners){
        assert.ok(finite(row.corner_work_fractions[corner]));
        assert.ok(finite(row.corner_abs_work_fractions[corner])&&row.corner_abs_work_fractions[corner]>=0);
        assert.ok(row.corner_abs_work_fractions[corner]+1e-13>=Math.abs(row.corner_work_fractions[corner]));
        assert.ok(finite(row.corner_max_electric_fields[corner])&&row.corner_max_electric_fields[corner]>0);
      }
    }
    const finest=values.at(-1);
    assert.ok(finest.early_field_relative_l2<=a.max_field_error);
    assert.ok(finest.reflection_amplitude_ratio>0&&finest.reflection_amplitude_ratio<=a.max_reflection_amplitude);
    assert.ok(finest.physical_flux_budget_relative_residual<=a.max_flux_residual);
    assert.ok(finest.remaining_physical_energy_fraction<=a.max_final_energy_fraction);
    assert.ok(finest.total_pml_work_fraction>0);
    assert.ok(Object.values(finest.directional_work_fractions).every(value=>Math.abs(value)>0),'Each damping direction is exercised');
    assert.ok(Object.values(finest.side_flux_fractions).every(value=>finite(value)&&value>=a.min_side_flux_fraction),'All four sides carry outgoing energy');
    assert.ok(finest.global_return_peak_time>=input.gate_start&&finest.global_return_peak_time<=input.end_time);
    assert.ok(finest.return_peak_time>=input.gate_start&&finest.return_peak_time<=input.end_time);
    assert.ok(Math.abs(finest.global_return_amplitude_ratio-finest.reflection_amplitude_ratio)<1e-12,'The gate contains the global peak');
    assert.ok(finest.excluded_early_return_peak_ratio<=finest.global_return_amplitude_ratio);
    assert.ok(series.field_orders.every(order=>finite(order)&&order>=a.min_field_order));
    assert.ok(series.flux_orders.every(order=>finite(order)&&order>=a.min_flux_order));
    assert.equal(series.return_waveform_differences.length,2);
    assert.ok(series.return_waveform_differences.every(value=>finite(value)&&value>0));
    assert.ok(finite(series.return_order)&&series.return_order>=a.min_return_order);
    assert.ok(series.reference_period_doubling_error_ratio>=0&&series.reference_period_doubling_error_ratio<=a.max_reference_period_error);
    assert.ok(series.reference_period_doubling_error_ratio<=a.max_reference_to_return_fraction*finest.reflection_amplitude_ratio);
    assert.ok(finite(series.initial_layer_zeroing_sensitivity_ratio)&&series.initial_layer_zeroing_sensitivity_ratio>=0,
      'Initial-layer zeroing is retained as a measured sensitivity diagnostic');
    const tailFraction=series.initial_layer_zeroing_sensitivity_ratio/finest.reflection_amplitude_ratio;
    assert.ok(Math.abs(tailFraction-series.initial_layer_sensitivity_to_return_fraction)<1e-12);
    assert.ok(series.initial_layer_sensitivity_to_return_fraction<=a.max_initial_layer_sensitivity_to_return_fraction,
      'The declared boundary-return signal is not dominated by initial auxiliary-layer tails');
    if(family==='diagonal')assert.ok(Object.values(finest.corner_abs_work_fractions).every(value=>value>=a.min_corner_abs_work_fraction),
      'All four corner overlaps have measured work, beyond merely configuring damping profiles');
  }
});

test('saved corner return waveforms reproduce the reported Cauchy differences on common clocks', () => {
  const input=json('inputs/pml-corners.json');
  const result=json('results/pml-corners/result.json');
  const lines=bytes('results/pml-corners/waveforms.csv').toString().trim().split(/\r?\n/);
  assert.deepEqual(lines.shift().split(',').slice(0,3),['family','nx','time']);
  const groups=new Map();
  for(const line of lines){
    const [family,nx,...fields]=line.split(',');
    const values=fields.map(Number);
    assert.ok(input.families.includes(family)&&input.meshes.includes(Number(nx)));
    assert.equal(values.length,5,'Time plus four returned probe fields');
    assert.ok(values.every(Number.isFinite));
    const key=family+'/'+nx;
    if(!groups.has(key))groups.set(key,[]);
    groups.get(key).push(values);
  }
  assert.equal(groups.size,input.families.length*input.meshes.length);
  for(const series of result.metrics.series){
    const traces=input.meshes.map(nx=>groups.get(series.family+'/'+nx));
    for(let k=0;k<traces.length;k++){
      const row=result.metrics.meshes.find(row=>row.family===series.family&&row.nx===input.meshes[k]);
      assert.equal(traces[k].length,row.steps+1);
      assert.equal(traces[k][0][0],0);
      assert.ok(Math.abs(traces[k].at(-1)[0]-input.end_time)<1e-12);
    }
    const differences=[];
    for(let k=0;k<2;k++){
      const coarse=traces[k],fine=traces[k+1];
      let maximum=0;
      for(let n=0;n<coarse.length;n++){
        assert.ok(Math.abs(coarse[n][0]-fine[2*n][0])<1e-12);
        if(coarse[n][0]<input.gate_start)continue;
        const squared=coarse[n].slice(1).reduce((sum,value,j)=>sum+(value-fine[2*n][j+1])**2,0);
        maximum=Math.max(maximum,Math.sqrt(squared/4));
      }
      differences.push(maximum);
      assert.ok(Math.abs(maximum-series.return_waveform_differences[k])<=1e-12*Math.max(1,maximum));
    }
    assert.ok(Math.abs(Math.log2(differences[0]/differences[1])-series.return_order)<1e-10);
  }
});

test('FDTD method and bilingual reading expose the new supplement and retain the original release', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.deepEqual(record.code_urls, ['solver.py', 'run.py','scattering.py','run_scattering.py','corner.py','run_corner.py'].map(name => manifest.public_base_url+name));
  assert.deepEqual(record.test_urls, ['test_fdtd.py','test_scattering.py','test_corner.py'].map(name=>manifest.public_base_url+name));
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
    for (const name of cornerCases) assert.ok(doc.html.includes(base+`results/${name}/result.json`));
    for (const name of scatteringCases) assert.ok(doc.html.includes(`code/fdtd/${secondEdition}/results/${name}/result.json`));
    assert.ok(doc.html.includes(originalBase+`fdtd-${originalEdition}.zip`));
    assert.ok(doc.html.includes(`code/fdtd/${secondEdition}/fdtd-${secondEdition}.zip`));
    assert.ok(doc.html.includes('id="pml-corners"'));
    assert.ok(doc.html.includes(base+`fdtd-${edition}.zip`));
    for (const name of cases) {
      assert.deepEqual(readFileSync(new URL(`numerical-methods-atlas/assets/fdtd-${name}.png`,root)), bytes(`results/${name}/summary.png`));
    }
    const html = readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.html`, root), 'utf8');
    assert.ok(html.includes('katex-mathml') && !html.includes('math-placeholder'));
  }
});
