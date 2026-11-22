import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const originalEdition = '2026-11-22';
const secondEdition = '2026-11-22-r2';
const thirdEdition = '2026-11-22-r3';
const fourthEdition = '2026-11-22-r4';
const edition = '2026-11-22-r5';
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
const obliqueCases = ['dielectric-oblique'];
const polarizationCases = ['p-polarization'];
const secondCases = [...legacyCases, ...scatteringCases];
const thirdCases = [...secondCases, ...cornerCases];
const retainedCases = [...thirdCases, ...obliqueCases];
const cases = [...retainedCases, ...polarizationCases];

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

test('all four previous FDTD editions remain byte-identical and all five ZIP payloads match their manifests', () => {
  const original = checkEdition(originalEdition);
  const second = checkEdition(secondEdition);
  const third = checkEdition(thirdEdition);
  const fourth = checkEdition(fourthEdition);
  checkEdition(edition);
  assert.equal(fourth.verification.archive.sha256, 'd34e3cb1bdf1daef35b008ac1495e4980f86fcb2dc0e8398f0df0e30dd576de1');
  assert.equal(third.verification.archive.sha256, '367fa305bc35f89c85217cecb5f6c383c86ae8a6b14b8a1b040889b75d690199');
  assert.equal(second.verification.archive.sha256, '50f8dad211f0b5fa54c538c9f272ec2509bc8740063f6b4e4c3ec907d8f7adcc');
  assert.equal(original.verification.archive.sha256, '482404475f935e8df487580ed48b8f98ada580fd61a79dd705fef9d5cf620d4d');
  for (const name of ['solver.py','run.py','test_fdtd.py', ...legacyCases.map(name=>`inputs/${name}.json`)]) {
    assert.deepEqual(bytes(name), originalBytes(name), 'Retained vacuum source/input: '+name);
  }
  const output = execFileSync('python3', ['-B', '-c', `
import hashlib,json,pathlib,stat,zipfile
for edition in ['${originalEdition}','${secondEdition}','${thirdEdition}','${fourthEdition}','${edition}']:
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
print('verified all five exact FDTD archive payloads')
`], {cwd: root, encoding: 'utf8'});
  assert.match(output, /verified all five exact FDTD archive payloads/);
});

test('the new dedicated edition independently reran all seven inputs and binds its code to measured results', () => {
  assert.ok(receipt.passed_tests > 71);
  assert.deepEqual(receipt.recipes.map(row=>row.id).sort(), cases.slice().sort());
  for (const recipe of receipt.recipes) {
    assert.equal(recipe.passed, true);
    assert.equal(recipe.metrics_identical, true);
    assert.equal(recipe.csv_identical, true);
    assert.equal(recipe.input_sha256, hash(bytes(`inputs/${recipe.id}.json`)));
  }
  for (const name of ['scattering.py','run_scattering.py','test_scattering.py','corner.py','run_corner.py','test_corner.py',
    'oblique.py','run_oblique.py','test_oblique.py',
    'polarization.py','run_polarization.py','test_polarization.py']) assert.ok(manifest.files[name]);
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

test('the current edition retains all r2 numerical source, fixed inputs and saved measurement values', () => {
  const previous = name => readFileSync(new URL(`code/fdtd/${secondEdition}/${name}`, root));
  for (const name of ['solver.py','run.py','test_fdtd.py','scattering.py','run_scattering.py','test_scattering.py',
      ...secondCases.map(name=>`inputs/${name}.json`)]) assert.deepEqual(bytes(name), previous(name), name);
  for (const name of secondCases) {
    const before=JSON.parse(previous(`results/${name}/result.json`));
    assert.deepEqual(json(`results/${name}/result.json`).metrics,before.metrics,name+' retains measured values');
  }
});

test('the current edition retains all five r3 numerical cases, sources, tests and fixed inputs', () => {
  const previous = name => readFileSync(new URL(`code/fdtd/${thirdEdition}/${name}`, root));
  for (const name of ['solver.py','run.py','test_fdtd.py','scattering.py','run_scattering.py','test_scattering.py',
      'corner.py','run_corner.py','test_corner.py',...thirdCases.map(name=>`inputs/${name}.json`)]) {
    assert.deepEqual(bytes(name), previous(name), name);
  }
  for (const name of thirdCases) {
    const before=JSON.parse(previous(`results/${name}/result.json`));
    assert.deepEqual(json(`results/${name}/result.json`).metrics,before.metrics,name+' retains measured values');
  }
});

test('r5 retains all six r4 numerical cases, sources, tests and fixed inputs', () => {
  const previous = name => readFileSync(new URL(`code/fdtd/${fourthEdition}/${name}`, root));
  for (const name of ['solver.py','run.py','test_fdtd.py','scattering.py','run_scattering.py','test_scattering.py',
      'corner.py','run_corner.py','test_corner.py','oblique.py','run_oblique.py','test_oblique.py',
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

test('oblique-interface packets use s-polarized spectral Fresnel energies and distinct carrier coefficients', () => {
  const input=json('inputs/dielectric-oblique.json');
  const result=json('results/dielectric-oblique/result.json');
  const a=input.acceptance,rows=result.metrics.meshes;
  const close=(actual,expected,label)=>assert.ok(Number.isFinite(actual)&&Math.abs(actual-expected)<=1e-11*Math.max(1,Math.abs(expected)),label);
  assert.ok(input.transverse_wave_numbers.includes(0)&&input.transverse_wave_numbers.some(ky=>ky>0));
  assert.ok(input.epsilon_right>input.epsilon_left);
  assert.match(result.polarization,/optical s\/TE/);
  assert.match(result.amplitude_scope,/expected gain 1/);
  assert.match(result.amplitude_scope,/not a measured monochromatic carrier/);
  assert.match(result.reference_scope,/underlying continuous spectrum/);
  assert.match(result.reference_scope,/No independent external solver or PML comparison/);
  assert.match(result.initial_secondary_scope,/staggered initial clocks/);
  assert.match(result.initial_secondary_scope,/distinct from same-time physical energy/);
  for(const check of ['field_accuracy','field_refinement','reflected_field_refinement','transmitted_field_refinement',
    'spectral_template_amplitudes','fresnel_energy_fractions','reflected_energy_refinement','transmitted_energy_refinement',
    'energy_fraction_closure','modified_energy','independent_flux_balance','flux_refinement','reference_period_control',
    'finite_window_reference','reference_initial_energy_norm','initial_secondary_fields','distant_pec_caps'])assert.equal(result.checks[check],true,check);
  assert.equal(rows.length,input.transverse_wave_numbers.length*input.meshes.length);
  assert.deepEqual(result.metrics.series.map(row=>row.ky),input.transverse_wave_numbers);
  assert.ok(manifest.files['results/dielectric-oblique/spectrum.csv']);
  const lines=bytes('results/dielectric-oblique/spectrum.csv').toString().trim().split(/\r?\n/);
  assert.deepEqual(lines.shift().split(','),['ky','kx','amplitude','energy_weight','omega','kx_transmitted','r_s','t_s','R_s','T_s','dkx2_dkx']);
  const modes=new Map(input.transverse_wave_numbers.map(ky=>[ky,[]]));
  const dk=2*Math.PI/input.reference_period;
  for(const line of lines){
    const values=line.split(',').map(Number);
    assert.equal(values.length,11);
    assert.ok(values.every(Number.isFinite));
    const [ky,k,amplitude,weight,omega,q,r,t,R,T,qprime]=values;
    assert.ok(modes.has(ky)&&k>0&&amplitude>0&&weight>0);
    close(omega**2,(k*k+ky*ky)/input.epsilon_left,'Incident dispersion');
    close(q*q+ky*ky,input.epsilon_right*omega**2,'Transmitted dispersion and conserved tangential wave number');
    close(r,(k-q)/(k+q),'Signed electric reflection coefficient');
    close(t,2*k/(k+q),'Electric transmission coefficient');
    close(1+r,t,'Tangential electric-field continuity');
    close(k*(1-r),q*t,'Tangential magnetic-field continuity');
    close(R,r*r,'Reflectance differs from signed amplitude');
    close(T,q/k*t*t,'Normal Poynting-flux factor');
    close(R+T,1,'Lossless modal energy closure');
    close(qprime,input.epsilon_right/input.epsilon_left*k/q,'Refraction packet Jacobian');
    close(input.epsilon_right/(input.epsilon_left*qprime)*t*t,T,'Spatial transmitted-packet energy includes the Jacobian');
    const expected=input.width/Math.sqrt(2*Math.PI)*Math.exp(-.5*(input.width*(k-input.carrier_kx))**2)*dk;
    assert.ok(Math.abs(amplitude-expected)<=1e-11*expected,'Fixed input determines every spectral amplitude');
    assert.ok(Math.abs(weight-amplitude*amplitude)<=1e-11*weight,'Parseval weights are squared modal amplitudes');
    modes.get(ky).push({k,weight,R,T});
  }
  for(const ky of input.transverse_wave_numbers){
    const spectrum=modes.get(ky),values=rows.filter(row=>row.ky===ky);
    assert.equal(spectrum.length,Math.round(input.spectral_cutoff/dk));
    spectrum.forEach((mode,i)=>close(mode.k,(i+1)*dk,'Positive-k quadrature grid'));
    const weight=spectrum.reduce((sum,z)=>sum+z.weight,0);
    const R=spectrum.reduce((sum,z)=>sum+z.weight*z.R,0)/weight;
    const T=spectrum.reduce((sum,z)=>sum+z.weight*z.T,0)/weight;
    const incident=.5*input.epsilon_left*input.lengths[1]*input.reference_period*weight;
    const k=input.carrier_kx,omega=Math.sqrt((k*k+ky*ky)/input.epsilon_left);
    const q=Math.sqrt(input.epsilon_right*omega**2-ky*ky),r=(k-q)/(k+q),t=2*k/(k+q);
    const theta1=Math.atan2(ky,k),theta2=Math.atan2(ky,q);
    assert.deepEqual(values.map(row=>[row.nx,row.ny]),input.meshes);
    for(const row of values){
      for(const [key,expected] of Object.entries({analytic_R:R,analytic_T:T,analytic_incident_energy:incident,
        carrier_r:r,carrier_t:t,carrier_R:r*r,carrier_T:q/k*t*t,
        incident_angle_degrees:theta1*180/Math.PI,transmitted_angle_degrees:theta2*180/Math.PI}))close(row[key],expected,key);
      close(Math.sqrt(input.epsilon_left)*Math.sin(row.incident_angle_degrees*Math.PI/180),
        Math.sqrt(input.epsilon_right)*Math.sin(row.transmitted_angle_degrees*Math.PI/180),'Carrier Snell law');
      if(ky>0)assert.ok(row.incident_angle_degrees>row.transmitted_angle_degrees&&row.transmitted_angle_degrees>0);
      close(row.dx,input.lengths[0]/row.nx,'dx');close(row.dy,input.lengths[1]/row.ny,'dy');
      close(row.dt*row.steps,input.end_time,'Common physical end time');
      assert.ok(row.dt*Math.hypot(1/row.dx,1/row.dy)/Math.sqrt(input.epsilon_left)<1,'Strict multidimensional CFL');
      close(row.spectrum_dk,dk,'Spectral spacing');
      close(row.spectrum_kmax,spectrum.at(-1).k,'Actual rounded spectral cutoff');
      close(row.reference_period,input.reference_period,'Reference period');
      close(row.reflection_gain_error,Math.abs(row.reflected_template_gain-1),'Broadband reflection-template gain');
      close(row.transmission_gain_error,Math.abs(row.transmitted_template_gain-1),'Broadband transmission-template gain');
      close(row.reflected_energy_error,Math.abs(row.reflected_energy_fraction-R),'Reflected packet energy error');
      close(row.transmitted_energy_error,Math.abs(row.transmitted_energy_fraction-T),'Transmitted packet energy error');
      close(row.energy_fraction_closure,Math.abs(row.reflected_energy_fraction+row.transmitted_energy_fraction-1),'Measured R + T closure');
      assert.ok(row.modified_energy_max_relative_drift<=a.max_modified_energy_drift);
      assert.ok(row.reference_period_doubling_relative_l2<=a.max_reference_period_error);
      assert.ok(row.reference_window_energy_error<=a.max_reference_window_error);
      assert.ok(Math.abs(row.reference_initial_energy_ratio-1)<=a.max_reference_window_error);
      assert.ok(row.initial_secondary_field_energy_fraction<=a.max_initial_secondary_energy_fraction);
      assert.ok(row.initial_pec_clipping_field_norm_fraction<=a.max_initial_secondary_energy_fraction);
      assert.ok(Number.isFinite(row.reference_final_interface_electric_max)&&row.reference_final_interface_electric_max>=0);
      assert.ok(row.analytic_cap_electric_max<=a.max_analytic_cap_field);
    }
    const finest=values.at(-1),series=result.metrics.series.find(s=>s.ky===ky);
    assert.ok(finest.field_relative_l2<=a.max_field_error);
    assert.ok(Math.max(finest.reflection_gain_error,finest.transmission_gain_error)<=a.max_template_gain_error);
    assert.ok(Math.max(finest.reflected_energy_error,finest.transmitted_energy_error)<=a.max_energy_fraction_error);
    assert.ok(finest.energy_fraction_closure<=a.max_energy_closure);
    assert.ok(finest.physical_flux_budget_max_relative_residual<=a.max_flux_residual);
    assert.ok(series.reference_energy_period_doubling_error<=a.max_reference_period_error);
    for(const name of ['field_orders','reflection_field_orders','transmission_field_orders'])assert.ok(series[name].every(p=>p>=a.min_field_order));
    for(const name of ['reflection_energy_orders','transmission_energy_orders'])assert.ok(series[name].every(p=>p>=a.min_energy_order));
    assert.ok(series.flux_orders.every(p=>p>=a.min_flux_order));
  }
});

test('saved oblique energy histories and convergence CSV independently reproduce the reported budgets and orders', () => {
  const input=json('inputs/dielectric-oblique.json');
  const result=json('results/dielectric-oblique/result.json');
  const close=(actual,expected,label)=>assert.ok(Number.isFinite(actual)&&Math.abs(actual-expected)<=1e-11*Math.max(1,Math.abs(expected)),label);
  function csv(name){
    const lines=bytes(`results/dielectric-oblique/${name}.csv`).toString().trim().split(/\r?\n/),header=lines.shift().split(',');
    return lines.map(line=>{
      const values=line.split(',').map(Number);assert.equal(values.length,header.length);assert.ok(values.every(Number.isFinite));
      return Object.fromEntries(header.map((key,i)=>[key,values[i]]));
    });
  }
  const convergence=csv('convergence'),history=csv('energy');
  assert.equal(convergence.length,result.metrics.meshes.length);
  for(const row of result.metrics.meshes){
    const saved=convergence.find(z=>z.nx===row.nx&&z.ny===row.ny&&z.ky===row.ky);assert.ok(saved);
    for(const [key,value] of Object.entries(row))close(saved[key],value,'Saved convergence '+key);
    const trace=history.filter(z=>z.nx===row.nx&&z.ny===row.ny&&z.ky===row.ky);
    assert.equal(trace.length,row.steps+1);assert.equal(trace[0].time,0);close(trace.at(-1).time,input.end_time,'Energy end time');
    close(trace[0].physical_energy/row.analytic_incident_energy,row.initial_physical_energy_ratio,'Initial numerical physical energy normalization');
    close(trace[0].interface_region_energy,row.flux_region_initial_energy,'Initial interface-region energy');
    const u0=trace[0].modified_energy,region0=trace[0].interface_region_energy;
    let drift=0,residual=0;
    for(let n=0;n<trace.length;n++){
      const z=trace[n];close(z.time,n*row.dt,'Saved energy clock');
      drift=Math.max(drift,Math.abs(z.modified_energy/u0-1));
      residual=Math.max(residual,Math.abs(z.interface_region_energy-region0+z.flux_right_integral-z.flux_left_integral)/row.analytic_incident_energy);
    }
    close(drift,row.modified_energy_max_relative_drift,'Independently recomputed global modified-energy drift');
    close(residual,row.physical_flux_budget_max_relative_residual,'Independently recomputed local Poynting-flux balance');
    const final=trace.at(-1);
    close(final.interface_region_energy,row.flux_region_final_energy,'Final local energy');
    close(final.flux_left_integral,row.flux_left_integral,'Left face integrated flux');
    close(final.flux_right_integral,row.flux_right_integral,'Right face integrated flux');
  }
  const orderFields={field_orders:'field_relative_l2',reflection_field_orders:'reflected_field_relative_l2',
    transmission_field_orders:'transmitted_field_relative_l2',reflection_energy_orders:'reflected_energy_error',
    transmission_energy_orders:'transmitted_energy_error',closure_orders:'energy_fraction_closure',
    flux_orders:'physical_flux_budget_max_relative_residual'};
  for(const series of result.metrics.series){
    const values=input.meshes.map(([nx,ny])=>convergence.find(z=>z.nx===nx&&z.ny===ny&&z.ky===series.ky));
    for(const [name,field] of Object.entries(orderFields)){
      assert.equal(series[name].length,2);
      for(let n=0;n<2;n++)close(Math.log2(values[n][field]/values[n+1][field]),series[name][n],'Recomputed '+name);
    }
  }
});

function polarizationCsv(name,visit){
  const lines=bytes('results/p-polarization/'+name+'.csv').toString().trim().split(/\r?\n/);
  const header=lines.shift().split(',');
  for(const line of lines){
    const fields=line.split(',');assert.equal(fields.length,header.length,name+' column count');
    const row=Object.fromEntries(header.map((key,i)=>[key,key==='subcase'?fields[i]:Number(fields[i])]));
    assert.ok(Object.entries(row).every(([key,value])=>key==='subcase'||Number.isFinite(value)),name+' finite values');
    visit(row);
  }
  return header;
}

function pFresnel(k,ky,eps1,eps2){
  const omega=Math.sqrt((k*k+ky*ky)/eps1),delta=eps2*omega*omega-ky*ky;
  const qr=delta>=0?Math.sqrt(delta):0,qi=delta<0?Math.sqrt(-delta):0;
  const y1=k/eps1,yr=qr/eps2,yi=qi/eps2,den=(y1+yr)**2+yi*yi;
  const rr=((y1-yr)*(y1+yr)-yi*yi)/den,ri=-2*y1*yi/den;
  const tr=1+rr,ti=ri,R=rr*rr+ri*ri,T=eps1/eps2*qr/k*(tr*tr+ti*ti);
  return {omega,qr,qi,rr,ri,tr,ti,R,T};
}

test('p-polarized spectral evidence distinguishes Brewster packets from an evanescent TIR branch', () => {
  const input=json('inputs/p-polarization.json'),result=json('results/p-polarization/result.json');
  const close=(actual,expected,label)=>assert.ok(Number.isFinite(actual)&&Math.abs(actual-expected)<=2e-11*Math.max(1,Math.abs(expected)),label);
  const definitions=new Map(input.subcases.map(c=>[c.id,c])),groups=new Map(input.subcases.map(c=>[c.id,[]]));
  assert.deepEqual([...definitions.keys()],['propagating','brewster','tir']);
  assert.match(result.polarization,/TEz Hz,Ex,Ey.*optical p/);
  assert.match(result.backend,/single-positive-ky reduction/);
  assert.match(result.backend,/full 2D equivalence/);
  assert.match(result.amplitude_scope,/rH\/tH are Hz amplitudes/);
  assert.match(result.energy_scope,/Evanescent stored energy is not T/);
  assert.match(result.field_scope,/Late field error.*separate diagnostic/);
  for(const name of ['field_accuracy','pre_interface_accuracy','field_refinement','fresnel_packet_flux',
    'packet_reflection_refinement','packet_transmission_refinement','energy_fraction_closure',
    'complex_fresnel_amplitudes','complex_reflection_refinement','modified_energy','independent_physical_flux',
    'flux_refinement','reference_period_control','finite_window_fluence_control','finite_window_dft_control',
    'initial_secondary_fields','distant_pec_caps','incident_fluence_normalization','brewster_carrier_null',
    'brewster_finite_band_residual','tir_flux','tir_nonzero_reactive_storage','tir_decay_accuracy',
    'tir_decay_refinement','tir_stored_energy_reference','tir_transient_flux_waveform_accuracy',
    'tir_transient_flux_waveform_refinement'])assert.equal(result.checks[name],true,name);
  assert.ok(manifest.files['results/p-polarization/spectrum.csv']);
  const header=polarizationCsv('spectrum',row=>{
    const c=definitions.get(row.subcase);assert.ok(c,'Known polarization subcase');
    const k=row.kx,z=pFresnel(k,c.ky,c.epsilon_left,c.epsilon_right),dk=2*Math.PI/input.reference_period;
    assert.ok(k>c.band[0]&&k<c.band[1]&&k>0,'Every mode lies strictly inside the prescribed compact band');
    close(row.ky,c.ky,'Fixed tangential wave number');close(row.epsilon_left,c.epsilon_left,'Left permittivity');
    close(row.epsilon_right,c.epsilon_right,'Right permittivity');close(row.dk,dk,'Quadrature spacing');
    close(row.omega,z.omega,'Incident dispersion');close(row.q_real,z.qr,'Outgoing transmitted branch real part');
    close(row.q_imag,z.qi,'Decaying transmitted branch imaginary part');
    assert.ok(row.q_real>=0&&row.q_imag>=0,'Outgoing or decaying branch, never a growing evanescent field');
    close(row.rH_real,z.rr,'Signed p/Hz reflection real part');close(row.rH_imag,z.ri,'Reflection phase');
    close(row.tH_real,z.tr,'Hz transmission real part');close(row.tH_imag,z.ti,'Hz transmission imaginary part');
    close(1+row.rH_real,row.tH_real,'Tangential Hz continuity real part');
    close(row.rH_imag,row.tH_imag,'Tangential Hz continuity imaginary part');
    close(k/c.epsilon_left*(1-row.rH_real),(row.q_real*row.tH_real-row.q_imag*row.tH_imag)/c.epsilon_right,'Tangential Ey continuity real part');
    close(-k/c.epsilon_left*row.rH_imag,(row.q_real*row.tH_imag+row.q_imag*row.tH_real)/c.epsilon_right,'Tangential Ey continuity imaginary part');
    close(row.R,z.R,'Modal reflected energy fraction');close(row.T,z.T,'Re(q), not abs(q), sets normal transmitted power');
    close(row.R+row.T,1,'Lossless modal flux closure');
    const u=(k-c.carrier_kx)/c.band_half_width;
    const amplitude=Math.exp(-.5*(c.width*(k-c.carrier_kx))**2-u**8/(1-u*u))*dk;
    assert.ok(Math.abs(row.amplitude-amplitude)<=1e-10*Math.max(amplitude,1e-250),'Fixed smooth compact spectral amplitude');
    assert.ok(row.amplitude>=0&&row.energy_weight>=0);
    close(row.energy_weight,row.amplitude*row.amplitude,'Squared Hz amplitudes supply Parseval weights');
    if(c.id==='tir')assert.ok(row.q_real===0&&row.q_imag>0,'All TIR spectral components are evanescent');
    else assert.ok(row.q_real>0&&row.q_imag===0,'Propagating controls have real transmitted wave numbers');
    groups.get(c.id).push(row);
  });
  for(const key of ['subcase','kx','ky','epsilon_left','epsilon_right','dk','amplitude','energy_weight','omega','q_real','q_imag','rH_real','rH_imag','tH_real','tH_imag','R','T'])assert.ok(header.includes(key),key);
  for(const c of input.subcases){
    const modes=groups.get(c.id),rows=result.metrics.meshes.filter(row=>row.subcase===c.id);
    assert.ok(modes.length>1&&modes.some(z=>z.energy_weight>0));
    const weight=modes.reduce((sum,z)=>sum+z.energy_weight,0);
    const R=modes.reduce((sum,z)=>sum+z.energy_weight*z.R,0)/weight;
    const T=modes.reduce((sum,z)=>sum+z.energy_weight*z.T,0)/weight;
    const incident=.5*c.lengths[1]*input.reference_period*weight;
    const carrier=pFresnel(c.carrier_kx,c.ky,c.epsilon_left,c.epsilon_right);
    assert.deepEqual(rows.map(row=>[row.nx,row.ny]),c.meshes);
    assert.deepEqual(rows.map(row=>row.steps),[1,2,4].map(factor=>rows[0].steps*factor),'Nested clocks share each physical time under grid refinement');
    for(const row of rows){
      close(row.analytic_R,R,'Spectral packet R');close(row.analytic_T,T,'Spectral packet T');
      close(row.analytic_incident_energy,incident,'Hz-normalized Parseval energy has no epsilon1 factor');
      for(const [name,expected] of Object.entries({carrier_rH_real:carrier.rr,carrier_rH_imag:carrier.ri,
        carrier_tH_real:carrier.tr,carrier_tH_imag:carrier.ti,carrier_q_real:carrier.qr,carrier_q_imag:carrier.qi,
        carrier_incident_angle_degrees:Math.atan2(c.ky,c.carrier_kx)*180/Math.PI}))close(row[name],expected,name);
      close(row.dx,c.lengths[0]/row.nx,'dx');close(row.dy,c.lengths[1]/row.ny,'dy');
      close(row.dt*row.steps,c.end_time,'Common physical end time');
      assert.ok(Math.abs(row.accuracy_time-c.accuracy_time)<=row.dt/2+1e-12,'Interaction field comparison uses its declared clock');
      assert.ok(Number.isFinite(row.late_field_relative_l2)&&row.late_field_relative_l2>=0,'Longer fluence-window field error remains separately visible');
      assert.ok(row.dt*Math.hypot(1/row.dx,1/row.dy)/Math.sqrt(Math.min(c.epsilon_left,c.epsilon_right))<1,'Strict two-dimensional CFL');
      assert.ok(row.modified_energy_max_relative_drift<=input.acceptance.max_modified_energy_drift);
      close(row.reflection_error,Math.abs(row.reflection_flux_fraction-row.analytic_window_R),'Windowed reflected-fluence error');
      close(row.transmission_error,Math.abs(row.transmission_flux_fraction-row.analytic_window_T),'Windowed transmitted-fluence error');
      close(row.energy_fraction_closure,Math.abs(row.reflection_flux_fraction+row.transmission_flux_fraction-1),'Finite-window flux closure');
      assert.ok(row.reference_window_energy_gap<=input.acceptance.max_reference_window_energy_gap);
      assert.ok(row.reference_period_doubling_relative_l2<=input.acceptance.max_reference_period_error);
      assert.ok(Math.max(row.reference_dft_r_error,row.reference_dft_t_error)<=input.acceptance.max_reference_dft_error);
      assert.ok(row.initial_secondary_field_norm_fraction<=input.acceptance.max_initial_secondary_norm_fraction);
      assert.ok(row.initial_pec_clipping_field_norm_fraction>=0&&row.initial_pec_clipping_field_norm_fraction<=input.acceptance.max_initial_secondary_norm_fraction);
      assert.ok(row.analytic_cap_tangential_electric_max<=input.acceptance.max_analytic_cap_field);
      close(row.complex_r_error,Math.hypot(row.numerical_rH_real-row.reference_rH_real,row.numerical_rH_imag-row.reference_rH_imag),'Complex reflection error uses its finite-window reference');
      close(row.complex_t_error,Math.hypot(row.numerical_tH_real-row.reference_tH_real,row.numerical_tH_imag-row.reference_tH_imag),'Complex transmission error uses its finite-window reference');
      close(row.carrier_complex_r_error,Math.hypot(row.numerical_rH_real-carrier.rr,row.numerical_rH_imag-carrier.ri),'Ideal-carrier reflection error is distinct');
      close(row.carrier_complex_t_error,Math.hypot(row.numerical_tH_real-carrier.tr,row.numerical_tH_imag-carrier.ti),'Ideal-carrier transmission error is distinct');
      close(row.reference_dft_r_error,Math.hypot(row.reference_rH_real-carrier.rr,row.reference_rH_imag-carrier.ri),'Finite-window reflection-reference error');
      close(row.reference_dft_t_error,Math.hypot(row.reference_tH_real-carrier.tr,row.reference_tH_imag-carrier.ti),'Finite-window transmission-reference error');
    }
    const fine=rows.at(-1);
    assert.ok(fine.field_relative_l2<=input.acceptance.max_field_error);
    assert.ok(fine.pre_interface_field_relative_l2<=input.acceptance.max_early_field_error);
    assert.ok(fine.physical_flux_budget_max_relative_residual<=input.acceptance.max_flux_residual);
    assert.ok(fine.reflection_error<=input.acceptance.max_energy_fraction_error&&fine.transmission_error<=input.acceptance.max_energy_fraction_error);
    assert.ok(fine.energy_fraction_closure<=input.acceptance.max_energy_closure);
    assert.ok(fine.carrier_complex_r_error<=input.acceptance.max_complex_r_error&&fine.carrier_complex_t_error<=input.acceptance.max_complex_t_error);
    assert.ok(fine.incident_fluence_energy_relative_error<=input.acceptance.max_incident_fluence_error);
    if(c.id==='brewster'){
      close(c.ky/c.carrier_kx,Math.sqrt(c.epsilon_right/c.epsilon_left),'Carrier tangent equals the Brewster index ratio');
      close(carrier.R,0,'Only the monochromatic carrier has zero Brewster reflectance');
      assert.ok(R>0&&R<=input.acceptance.max_brewster_packet_reflection,'Finite-band Brewster packet retains physical reflection');
      assert.ok(Math.hypot(fine.numerical_rH_real,fine.numerical_rH_imag)<=input.acceptance.max_brewster_carrier_reflection,'Numerical carrier null is an amplitude criterion');
    }
    if(c.id==='tir'){
      close(R,1,'All compact-spectrum TIR modes reflect unit normal power');close(T,0,'All compact-spectrum TIR modes have zero normal transmittance');
      assert.ok(Math.atan2(c.ky,c.carrier_kx)>Math.asin(Math.sqrt(c.epsilon_right/c.epsilon_left)),'Carrier lies above the critical angle');
      assert.ok(fine.max_right_stored_energy_fraction>=input.acceptance.min_tir_peak_stored_energy,'Evanescent energy storage is actually exercised');
      assert.ok(fine.max_right_stored_energy_fraction>=fine.final_right_stored_energy_fraction&&fine.final_right_stored_energy_fraction>=0);
      assert.ok(fine.min_transmitted_instantaneous_flux<0&&fine.max_transmitted_instantaneous_flux>0,'TIR exchanges energy transiently in both normal directions');
      assert.ok(Math.abs(fine.transmission_flux_fraction)<=input.acceptance.max_tir_transmission,'Finite-window net transmission is distinct from stored right-side energy');
      assert.ok(fine.carrier_decay_rate_error<=input.acceptance.max_decay_error&&fine.reference_decay_rate_error<=input.acceptance.max_reference_decay_error);
      assert.ok(fine.peak_right_stored_energy_relative_error<=input.acceptance.max_stored_energy_error);
      assert.ok(fine.transmitted_flux_waveform_relative_l2<=input.acceptance.max_tir_flux_waveform_error,'A noncancelling transient-flux norm verifies TIR refinement');
    }
  }
});

test('saved p-polarization histories reproduce fluxes, complex Fresnel ratios, evanescent decay and refinement', () => {
  const input=json('inputs/p-polarization.json'),result=json('results/p-polarization/result.json');
  const close=(actual,expected,label)=>assert.ok(Number.isFinite(actual)&&Math.abs(actual-expected)<=2e-9*Math.max(1,Math.abs(expected)),label);
  const key=row=>row.subcase+'/'+row.nx+'/'+row.ny;
  const definitions=new Map(input.subcases.map(c=>[c.id,c])),measurements=new Map(result.metrics.meshes.map(row=>[key(row),row]));
  const convergence=[];polarizationCsv('convergence',row=>convergence.push(row));
  assert.equal(convergence.length,result.metrics.meshes.length);
  for(const row of result.metrics.meshes){
    const saved=convergence.find(z=>key(z)===key(row));assert.ok(saved);
    for(const [name,value] of Object.entries(row)){
      if(typeof value==='string')assert.equal(saved[name],value);
      else close(saved[name],value,'Saved convergence '+name);
    }
  }
  const energy=new Map();
  const energyHeader=polarizationCsv('energy',z=>{
    const id=key(z),row=measurements.get(id);assert.ok(row);
    if(!energy.has(id))energy.set(id,{count:0,u0:z.modified_energy,region0:z.region_energy,drift:0,budget:0,peak:0,peakTime:0,final:0});
    const s=energy.get(id);close(z.time,s.count*row.dt,'Energy saved clock');s.count++;
    s.drift=Math.max(s.drift,Math.abs(z.modified_energy/s.u0-1));
    s.budget=Math.max(s.budget,Math.abs(z.region_energy-s.region0+z.flux_right_integral-z.flux_left_integral)/row.analytic_incident_energy);
    const stored=z.right_stored_energy/row.analytic_incident_energy;
    if(stored>s.peak){s.peak=stored;s.peakTime=z.time;}
    s.final=stored;
  });
  assert.deepEqual(energyHeader,['subcase','nx','ny','time','modified_energy','physical_energy','region_energy','flux_left_integral','flux_right_integral','right_stored_energy']);
  for(const row of result.metrics.meshes){
    const s=energy.get(key(row));assert.ok(s);assert.equal(s.count,row.steps+1);
    close(s.drift,row.modified_energy_max_relative_drift,'Recomputed modified-energy drift');
    assert.ok(s.drift<=input.acceptance.max_modified_energy_drift);
    close(s.budget,row.physical_flux_budget_max_relative_residual,'Recomputed independent local energy/flux budget');
    close(s.peak,row.max_right_stored_energy_fraction,'Peak stored right energy, not transmittance');
    close(s.peakTime,row.peak_right_stored_time,'Stored-energy peak clock');
    close(s.final,row.final_right_stored_energy_fraction,'Final stored right energy');
    close(Math.abs(s.peak-row.reference_right_energy_at_numerical_peak)/Math.max(Math.abs(row.reference_right_energy_at_numerical_peak),1e-30),
      row.peak_right_stored_energy_relative_error,'Stored energy uses its continuum reference at the numerical peak time');
  }
  const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],scale=(a,b)=>[a[0]*b,a[1]*b];
  const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
  const div=(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];assert.ok(d>0);return[(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d];};
  const absolute=a=>Math.hypot(...a),minusI=(a,d)=>scale([Math.cos(a[0]*d),-Math.sin(a[0]*d)],Math.exp(a[1]*d));
  const cosine=a=>[Math.cos(a[0])*Math.cosh(a[1]),-Math.sin(a[0])*Math.sinh(a[1])];
  const discreteK=(omega,epsilon,row,c)=>{
    const K=2*Math.sin(c.ky*row.dy/2)/row.dy;
    const z=epsilon*(2*Math.sin(omega*row.dt/2)/row.dt)**2-K*K,argument=Math.sqrt(Math.abs(z))*row.dx/2;
    if(z>=0){assert.ok(argument<1,'Resolved propagating carrier');return[2*Math.asin(argument)/row.dx,0];}
    return[0,2*Math.asinh(argument)/row.dx];
  };
  const complex=(z,name)=>[z[name+'_real'],z[name+'_imag']];
  const signalNames=['incident_H','incident_Ey','reflected_H','reflected_Ey','transmitted_H','transmitted_Ey','second_transmitted_H'];
  const fluxNames=['incident_flux','reflected_flux','transmitted_flux'];
  const waves=new Map();
  for(const c of input.subcases){
    const name='waveforms-'+c.id;assert.ok(manifest.files['results/p-polarization/'+name+'.csv']);
    const header=polarizationCsv(name,z=>{
      assert.equal(z.subcase,c.id);const id=key(z),row=measurements.get(id);assert.ok(row);
      if(!waves.has(id))waves.set(id,{count:0,last:null,fluence:Array(6).fill(0),fourier:Array.from({length:8},()=>[0,0]),fluxErrorSquared:0,referenceFluxSquared:0,min:Infinity,max:-Infinity});
      const s=waves.get(id),carrier=pFresnel(c.carrier_kx,c.ky,c.epsilon_left,c.epsilon_right);
      close(z.time,s.count*row.dt,'Waveform saved clock');s.count++;
      const phase=[Math.cos(carrier.omega*z.time),Math.sin(carrier.omega*z.time)],fluxes=[],transformed=[];
      for(const prefix of ['', 'analytic_']){
        for(let i=0;i<3;i++){
          const H=complex(z,prefix+signalNames[2*i]),E=complex(z,prefix+signalNames[2*i+1]);
          const flux=.5*c.lengths[1]*(E[0]*H[0]+E[1]*H[1]);
          close(z[prefix+fluxNames[i]],flux,'Normal Poynting flux from saved complex H and Ey');fluxes.push(flux);
        }
        for(const name of ['incident_H','reflected_H','transmitted_H','second_transmitted_H'])transformed.push(mul(complex(z,prefix+name),phase));
      }
      if(s.last){
        const dt=z.time-s.last.time;assert.ok(dt>0);
        for(let i=0;i<6;i++)s.fluence[i]+=.5*dt*(s.last.fluxes[i]+fluxes[i]);
        for(let i=0;i<8;i++)s.fourier[i]=add(s.fourier[i],scale(add(s.last.transformed[i],transformed[i]),.5*dt));
        s.fluxErrorSquared+=.5*dt*((s.last.fluxes[2]-s.last.fluxes[5])**2+(fluxes[2]-fluxes[5])**2);
        s.referenceFluxSquared+=.5*dt*(s.last.fluxes[5]**2+fluxes[5]**2);
      }
      s.min=Math.min(s.min,fluxes[2]/row.analytic_incident_energy);s.max=Math.max(s.max,fluxes[2]/row.analytic_incident_energy);
      s.last={time:z.time,fluxes,transformed};
    });
    const expected=['subcase','nx','ny','time'];
    for(const prefix of ['', 'analytic_'])for(const name of signalNames)for(const part of ['real','imag'])expected.push(prefix+name+'_'+part);
    expected.push(...fluxNames,...fluxNames.map(name=>'analytic_'+name));assert.deepEqual(header,expected);
  }
  for(const row of result.metrics.meshes){
    const c=definitions.get(row.subcase),s=waves.get(key(row)),d=c.monitor_offset;assert.ok(s);
    assert.equal(s.count,row.steps+1);close(s.last.time,c.end_time,'Waveform fluence end time');
    const [Fi,Fr,Ft,Ai,Ar,At]=s.fluence;
    assert.ok(Fi>0&&Ai>0,'Both incident fluence normalizations are positive');
    close(Fi,row.incident_fluence,'Homogeneous same-Yee incident fluence');close(Ai,row.analytic_incident_fluence,'Continuum incident fluence');
    close(-Fr/Fi,row.reflection_flux_fraction,'Reflected time-integrated normal fluence');close(Ft/Fi,row.transmission_flux_fraction,'Transmitted time-integrated normal fluence');
    close(-Ar/Ai,row.analytic_window_R,'Continuum finite-window R');close(At/Ai,row.analytic_window_T,'Continuum finite-window T');
    close(Math.abs(Fi/row.analytic_incident_energy-1),row.incident_fluence_energy_relative_error,'Numerical incident energy normalization');
    close(Math.abs(Ai/row.analytic_incident_energy-1),row.reference_incident_fluence_energy_error,'Reference incident window coverage');
    close(s.min,row.min_transmitted_instantaneous_flux,'Most negative transient transmitted normal flux');
    close(s.max,row.max_transmitted_instantaneous_flux,'Most positive transient transmitted normal flux');
    assert.ok(s.referenceFluxSquared>0,'The transmitted transient flux waveform is exercised even when its signed time integral cancels');
    close(Math.sqrt(s.fluxErrorSquared/s.referenceFluxSquared),row.transmitted_flux_waveform_relative_l2,'Independent noncancelling transmitted-flux waveform norm');
    const [hi,hr,ht,h2,ai,ar,at,a2]=s.fourier,carrier=pFresnel(c.carrier_kx,c.ky,c.epsilon_left,c.epsilon_right);
    const kn=discreteK(carrier.omega,c.epsilon_left,row,c),qn=discreteK(carrier.omega,c.epsilon_right,row,c);
    const rn=mul(div(hr,hi),minusI(kn,2*d));
    const tn=mul(mul(div(ht,hi),minusI(add(kn,qn),d)),div(cosine(scale(kn,row.dx/2)),cosine(scale(qn,row.dx/2))));
    const ra=mul(div(ar,ai),minusI([c.carrier_kx,0],2*d));
    const ta=mul(div(at,ai),minusI([c.carrier_kx+carrier.qr,carrier.qi],d));
    for(const [name,value] of Object.entries({numerical_rH:rn,numerical_tH:tn,reference_rH:ra,reference_tH:ta})){
      close(value[0],row[name+'_real'],'DFT '+name+' real part');close(value[1],row[name+'_imag'],'DFT '+name+' imaginary part');
    }
    close(-Math.log(absolute(div(h2,ht)))/d,row.numerical_decay_rate,'Yee evanescent decay extracted from two saved planes');
    close(-Math.log(absolute(div(a2,at)))/d,row.reference_window_decay_rate,'Continuum finite-window decay extracted from two planes');
    close(Math.abs(row.numerical_decay_rate-row.reference_window_decay_rate),row.decay_rate_error,'Finite-window decay error');
    close(Math.abs(row.numerical_decay_rate-carrier.qi),row.carrier_decay_rate_error,'Ideal carrier decay error');
    close(Math.abs(row.reference_window_decay_rate-carrier.qi),row.reference_decay_rate_error,'Reference finite-window decay offset');
  }
  const orderFields={field_orders:'field_relative_l2',reflection_orders:'reflection_error',transmission_fluence_orders:'transmission_error',
    complex_r_orders:'complex_r_error',complex_t_orders:'complex_t_error',flux_orders:'physical_flux_budget_max_relative_residual',
    transmitted_flux_waveform_orders:'transmitted_flux_waveform_relative_l2',decay_orders:'decay_rate_error'};
  for(const series of result.metrics.series){
    const c=definitions.get(series.subcase),rows=c.meshes.map(([nx,ny])=>convergence.find(z=>z.subcase===c.id&&z.nx===nx&&z.ny===ny));
    for(const [name,field] of Object.entries(orderFields)){
      if(name==='decay_orders'&&c.id!=='tir'){assert.deepEqual(series[name],[]);continue;}
      assert.equal(series[name].length,2);
      for(let n=0;n<2;n++)close(Math.log2(rows[n][field]/rows[n+1][field]),series[name][n],'Recomputed '+c.id+' '+name);
    }
    assert.ok(series.field_orders.every(p=>p>=input.acceptance.min_field_order));
    assert.ok(series.reflection_orders.every(p=>p>=input.acceptance.min_energy_order));
    if(c.id!=='tir')assert.ok(series.transmission_fluence_orders.every(p=>p>=input.acceptance.min_energy_order));
    assert.ok(series.complex_r_orders.every(p=>p>=input.acceptance.min_complex_r_order));
    assert.ok(series.flux_orders.every(p=>p>=input.acceptance.min_flux_order));
    assert.ok(series.reference_energy_period_doubling_error<=input.acceptance.max_reference_period_error);
    if(c.id==='tir'){
      assert.ok(series.decay_orders.every(p=>p>=input.acceptance.min_decay_order));
      assert.ok(series.transmitted_flux_waveform_orders.every(p=>p>=input.acceptance.min_energy_order));
    }
  }
});

test('FDTD method and bilingual reading expose the new supplement and retain the original release', () => {
  const record = JSON.parse(readFileSync(new URL('numerical-methods-atlas/methods/fdtd/index.json', root)));
  assert.equal(record.status, 'educational-example');
  assert.equal(record.code_base, manifest.public_base_url);
  assert.equal(record.code_download, manifest.public_base_url+receipt.archive.file);
  assert.match(record.run_from,/TMz\/TEz/);
  assert.equal(record.run_commands[0], 'python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py');
  assert.ok(record.run_commands.includes('python run_polarization.py --input inputs/p-polarization.json --output rerun-p-polarization'));
  assert.deepEqual(record.code_urls, ['solver.py', 'run.py','scattering.py','run_scattering.py','corner.py','run_corner.py','oblique.py','run_oblique.py','polarization.py','run_polarization.py'].map(name => manifest.public_base_url+name));
  assert.deepEqual(record.test_urls, ['test_fdtd.py','test_scattering.py','test_corner.py','test_oblique.py','test_polarization.py'].map(name=>manifest.public_base_url+name));
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
    for (const name of cornerCases) assert.ok(doc.html.includes(`code/fdtd/${thirdEdition}/results/${name}/result.json`));
    for (const name of obliqueCases) assert.ok(doc.html.includes(`code/fdtd/${fourthEdition}/results/${name}/result.json`));
    for (const name of polarizationCases) assert.ok(doc.html.includes(base+`results/${name}/result.json`));
    for (const name of scatteringCases) assert.ok(doc.html.includes(`code/fdtd/${secondEdition}/results/${name}/result.json`));
    assert.ok(doc.html.includes(originalBase+`fdtd-${originalEdition}.zip`));
    assert.ok(doc.html.includes(`code/fdtd/${secondEdition}/fdtd-${secondEdition}.zip`));
    assert.ok(doc.html.includes(`code/fdtd/${thirdEdition}/fdtd-${thirdEdition}.zip`));
    assert.ok(doc.html.includes(`code/fdtd/${fourthEdition}/fdtd-${fourthEdition}.zip`));
    assert.ok(doc.html.includes('id="pml-corners"'));
    assert.ok(doc.html.includes('id="interface-oblique"'));
    assert.ok(doc.html.includes('id="interface-p-polarization"'));
    assert.ok(doc.html.includes(base+`fdtd-${edition}.zip`));
    for (const name of cases) {
      assert.deepEqual(readFileSync(new URL(`numerical-methods-atlas/assets/fdtd-${name}.png`,root)), bytes(`results/${name}/summary.png`));
    }
    const html = readFileSync(new URL(`numerical-methods-atlas/${language}/read/fdtd/index.html`, root), 'utf8');
    assert.ok(html.includes('katex-mathml') && !html.includes('math-placeholder'));
  }
});
