import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const text=p=>bytes(p).toString();
const json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const base='code/periodic-forces/2026-11-22/';
const input=json(base+'inputs.json'),result=json(base+'results/result.json'),reference=json(base+'reference-dftk.json');
const close=(x,y,t=1e-12)=>assert.ok(Math.abs(x-y)<=t,`${x} != ${y}`);
const forceDiff=(a,b)=>Math.max(...a.flatMap((v,i)=>v.map((x,j)=>Math.abs(x-b[i][j]))));

test('multiatom forces are nonzero and all Cartesian energy differences reproduce the saved forces',()=>{
  assert.equal(result.case,'periodic-he-forces');assert.equal(result.passed,true);
  assert.equal(result.input_sha256,sha(base+'inputs.json'));assert.equal(result.reference_sha256,sha(base+'reference-dftk.json'));
  assert.equal(result.force_unit,'hartree/bohr');assert.equal(result.energy_unit,'hartree/cell');
  assert.deepEqual(input.cell.positions_bohr,[[.37,.61,.83],[2.13,2.27,2.41]]);
  assert.equal(input.cell.positions_bohr.length,2);
  assert.ok(result.cases.every(c=>c.converged&&c.electron_count_error<1e-8));
  const fd=result.finite_difference;
  assert.equal(fd.components.length,6);assert.equal(new Set(fd.components.map(r=>`${r.atom}/${r.axis}`)).size,6);
  for(const r of fd.components){
    assert.ok(Math.abs(r.force_analytic)>1e-3);
    close(r.force_finite_difference,-(r.energy_plus-r.energy_minus)/(2*r.step_bohr));
    close(r.absolute_error,Math.abs(r.force_analytic-r.force_finite_difference));
    assert.ok(r.absolute_error<=input.acceptance.finite_difference_max_error);
  }
  assert.ok(fd.steps.length>=3);assert.ok(new Set(fd.steps.map(r=>r.step_bohr)).size>=3);
  for(const r of fd.steps)close(r.absolute_error,Math.abs(-(r.energy_plus-r.energy_minus)/(2*r.step_bohr)-r.force_analytic));
  assert.ok(Object.values(result.checks).every(v=>v===true));
});

test('force convergence separates k meshes, both Gaussian-basis scans, auxiliary grids and SCF',()=>{
  const indexed=new Map(result.cases.map(c=>[c.id,c]));
  assert.deepEqual(Object.keys(result.convergence).sort(),['auxiliary','basis','basis-k2','kpoint','scf']);
  for(const [axis,c] of Object.entries(result.convergence)){
    assert.deepEqual(c.case_ids,input.convergence_groups[axis]);const rows=c.case_ids.map(id=>indexed.get(id));
    for(let i=1;i<rows.length;i++)close(c.adjacent_changes[i-1],forceDiff(rows[i].forces_cartesian,rows[i-1].forces_cartesian));
    close(c.last_change,c.adjacent_changes.at(-1));assert.equal(c.target_reached,true);assert.ok(c.last_change<=input.acceptance[axis+'_last_change']);
    if(axis!=='kpoint')assert.equal(new Set(rows.map(r=>r.k_n)).size,1);
    if(!axis.startsWith('basis'))assert.equal(new Set(rows.map(r=>r.basis)).size,1);
    if(axis!=='auxiliary')assert.equal(new Set(rows.map(r=>JSON.stringify(r.fft_mesh))).size,1);
    if(axis!=='scf')assert.equal(new Set(rows.map(r=>JSON.stringify(r.scf_options))).size,1);
  }
  const k=result.convergence.kpoint;assert.ok(k.adjacent_changes[1]>k.target,'the initially insufficient 2-to-3 increment remains visible');
  assert.equal(indexed.get(k.case_ids.at(-1)).k_n,4);
});

test('independent plane-wave analytic forces have their own cutoff and energy-derivative checks',()=>{
  assert.equal(reference.engine,'DFTK');assert.equal(reference.engine_version,'0.7.19');
  assert.deepEqual(reference.cell,input.cell);assert.deepEqual(reference.xc,input.xc.libxc);
  assert.equal(reference.input_sha256,sha(base+'inputs.json'));assert.equal(reference.script_sha256,sha(base+'reference.jl'));
  assert.equal(reference.pseudopotential_sha256,sha(base+'He.gth'));
  assert.equal(reference.project_sha256,sha(base+'reference-environment/Project.toml'));
  assert.equal(reference.manifest_sha256,sha(base+'reference-environment/Manifest.toml'));
  assert.equal(reference.energy_offset_applied,0);
  for(const c of result.independent_comparison.cases){
    close(c.max_absolute_force_difference,forceDiff(c.pyscf_forces_cartesian,c.dftk_forces_cartesian));
    assert.ok(c.max_absolute_force_difference<=input.acceptance.reference_force_difference);assert.equal(c.passed,true);
    const rows=reference.cutoff_convergence.records.filter(r=>r.k_n===c.k_n);
    assert.deepEqual(rows.map(r=>r.ecut_hartree),input.reference.ecut_hartree);
    assert.ok(forceDiff(rows.at(-1).forces_cartesian,rows.at(-2).forces_cartesian)<=input.reference.force_cutoff_tolerance);
    assert.ok(rows.every(r=>r.converged));
  }
  const fd=reference.finite_difference.records;
  const fine=fd.filter(r=>r.step_bohr===Math.min(...fd.map(r=>r.step_bohr)));
  assert.equal(fine.length,6);assert.equal(new Set(fine.map(r=>`${r.atom_index}/${r.component}`)).size,6);
  for(const r of fd){
    close(r.central_difference_force,-(r.energy_plus-r.energy_minus)/(2*r.step_bohr));
    assert.ok(Math.abs(r.central_difference_force-r.analytic_force)<=input.reference.finite_difference_tolerance);
  }
});

test('BOMD evidence is an actually reconverged local interface rather than a long-trajectory claim',()=>{
  const b=result.bomd;assert.equal(b.electronic_force_evaluations.length,3);
  assert.ok(b.electronic_force_evaluations.every(r=>r.converged&&r.scf_commutator_norm<1e-6));
  assert.ok(b.position_max_difference<=input.acceptance.bomd_position_step_difference);
  assert.ok(b.full_step_energy_defect<=input.acceptance.bomd_energy_defect);
  assert.ok(b.two_half_steps_energy_defect<=input.acceptance.bomd_energy_defect);
  assert.notDeepEqual(b.full_step.positions_bohr,input.cell.positions_bohr);
  const methods=json('numerical-methods-atlas/methods/index.json').methods;
  for(const id of ['born-oppenheimer-md','car-parrinello-md']){
    const m=methods.find(m=>m.id===id);assert.equal(m.status,'reading-only');assert.deepEqual(m.execution_examples,[]);
  }
  const route=json('numerical-methods-atlas/connections/index.json').routes.find(r=>r.id==='dft-md');
  assert.equal(route.coupled_validation.status,'not-executed');
  assert.equal(route.connections.find(c=>c.id==='dft-to-forces').coupled_validation.status,'fixed-input');
  assert.equal(route.connections.find(c=>c.id==='forces-to-md').coupled_validation.status,'interface-only');
  assert.equal(route.connections.find(c=>c.id==='md-to-thermostat').coupled_validation.status,'not-executed');
});

test('bilingual force reading connects measured evidence, runnable code, sources and purpose discovery',()=>{
  for(const lang of ['ja','en']){
    const route=`numerical-methods-atlas/${lang}/read/periodic-forces/`;
    const doc=json(route+'index.json'),html=text(route+'index.html');
    assert.equal(doc.locale,lang);assert.equal(doc.execution_example,'periodic-he-forces');assert.deepEqual(doc.measurements,result.metrics);
    for(const [path,hash] of Object.entries(doc.source_sha256))assert.equal(sha(path),hash,path);
    assert.ok(html.includes('katex-mathml')&&!html.includes('katex-error'));
    assert.ok(html.includes('/examples/periodic-he-forces/'));assert.ok(html.includes(base+'periodic_forces.py'));
    for(const id of ['feynman1939','pulay1969','herbert-head-gordon2005'])assert.ok(doc.references.some(r=>r.id===id&&r.review[lang]));
  }
  const goal=json('catalog/atlas-goals.json').goals.find(g=>g.id==='periodic-forces');assert.deepEqual(goal.examples,['periodic-he-forces']);
  const index=json('numerical-methods-atlas/home-search-index.json');
  for(const q of ['DFT forces','原子間力','Pulay'])assert.ok(searchChapters(index,q).some(r=>['execution-periodic-he-forces','reading-periodic-forces'].includes(r.id)),q);
  const registry=json('numerical-methods-atlas/code-and-data/examples.json');const entry=registry.examples.find(e=>e.id==='periodic-he-forces');
  assert.equal(entry.release.family,'periodic-forces');assert.equal(entry.inputs.sha256,sha(base+'inputs.json'));
  const old='code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip';assert.equal(sha(old),'f331515e3ad419b5435dbf851553c6b853b28b2432801fc13c84109faa362df8');
});

test('the staged public registry and final registry have identical verified bytes',()=>{
  const registryPath='numerical-methods-atlas/code-and-data/examples.json';
  const registry=json(registryPath);
  const receipt=json(new URL(registry.verification_receipt).pathname.slice(1));
  assert.equal(receipt.registry_source_mode,'public-registry');
  assert.equal(receipt.registry_sha256,sha(registryPath));
  assert.equal(receipt.registry_acquisition_url,'https://hrkoyama.github.io/code/periodic-forces/verification-candidates/2026-11-22.json');
  assert.equal(sha(new URL(receipt.registry_acquisition_url).pathname.slice(1)),sha(registryPath));
  assert.equal(receipt.unique_runner_executions,21);assert.equal(receipt.examples.length,22);
  assert.ok(receipt.examples.every(r=>r.execution.completed&&r.validation.passed));
});
