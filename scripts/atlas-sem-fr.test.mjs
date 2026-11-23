import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root=new URL('../',import.meta.url),base='code/validated-examples/2026-11-23/sem-fr/';
const text=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const hash=x=>createHash('sha256').update(JSON.stringify(canonical(x))).digest('hex');
const ids=['sem-poisson-2d','fr-periodic-advection'],methods=['spectral-element','flux-reconstruction'];
const baseline=json('scripts/sem-fr-baseline.json'),result=json(base+'results/result.json');

test('SEM/FR preserve the previous149 method records,24 releases,92 primary pictures and common executions',()=>{
 const rows=json('catalog/atlas-methods.json').methods;
 assert.equal(rows.length,151);
 const original=rows.filter(m=>!methods.includes(m.id)).map(m=>Object.fromEntries(Object.entries(m).filter(([k])=>!(['p1-fem','dg'].includes(m.id)&&['depth_release','depth_scope','depth_previous_status'].includes(k)))));
 assert.equal(hash(original),baseline.method_records_sha256);
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.releases.length,25);assert.equal(registry.case_count,58);assert.equal(registry.releases.reduce((n,r)=>n+r.tests,0),760);
 assert.equal(hash(registry.releases.filter(r=>r.group!=='sem-fr')),baseline.release_records_sha256);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 assert.equal(pictures.length,92);assert.equal(hash(pictures),baseline.primary_records_sha256);
 for(const p of pictures)assert.equal(sha(p.image.replace(/^\//,'')),p.image_sha256);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),baseline.common_registry_sha256);
});

test('the independent25-test ZIP retains original acceptance, both actual failed protocols and exact legacy baselines',()=>{
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,25);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);
 for(const [p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(sha(base+p),h,p);
 for(const [p,h]of Object.entries(json(base+'pre-run-contract.json').files_sha256))assert.equal(sha(base+p),h,p);
 assert.equal(sha(base+'inputs.json'),sha(base+'inputs-initial.json'));
 assert.equal(sha(base+'inputs.json'),sha(base+'attempts/01-dense-exponential/source/inputs.json'));
 const history=json(base+'protocol-history.json');assert.equal(history.acceptance_modified_after_first_execution,false);assert.equal(history.input_modified_after_first_execution,false);assert.equal(history.original_pytest.passed,23);assert.equal(history.original_pytest.failed,1);
 const provenance=json(base+'baseline-provenance.json');assert.equal(Object.keys(provenance.files).length,7);
 for(const [p,r]of Object.entries(provenance.files)){
  assert.equal(sha(base+p),r.sha256);assert.equal(sha(new URL(r.source_url).pathname.slice(1)),r.sha256);
 }
});

test('SEM has independently integrated errors, matched free unknowns and separate h/p refinement',()=>{
 const c=result.cases.find(c=>c.id===ids[0]);assert.ok(c.passed&&Object.values(c.checks).every(Boolean));
 const h=c.records.filter(r=>r.method==='GLL-SEM'&&r.series==='h'),p=c.records.filter(r=>r.series==='p'),fem=c.records.filter(r=>r.method==='published-P1-FEM');
 assert.deepEqual(h.map(r=>r.elements_per_axis),[2,4,8]);assert.deepEqual(h.map(r=>r.free_dofs),[9,49,225]);assert.deepEqual(fem.map(r=>r.free_dofs),[9,49,225]);assert.deepEqual(p.map(r=>r.degree),[1,2,3,4,5,6]);
 assert.ok(Math.abs(c.metrics.sem_h_l2_order-Math.log2(h[1].l2_error/h[2].l2_error))<1e-12);
 assert.ok(c.metrics.sem_h_l2_order>3&&c.metrics.p1_h_l2_order>1.9);
 assert.ok(c.metrics.p_refinement_l2_reduction>1e5);
 assert.ok(text(base+'sem.py').includes('leggauss(quadrature or p+4)'));
 assert.ok(text(base+'README.md').includes('not a runtime or universal superiority'));
});

test('FR compares the actual published DG, records every timestep mass and separates temporal error',()=>{
 const c=result.cases.find(c=>c.id===ids[1]);assert.ok(c.passed&&Object.values(c.checks).every(Boolean));assert.equal(c.records.length,6);
 assert.ok(c.metrics.maximum_fr_vs_published_dg<2e-10);assert.ok(c.metrics.maximum_stage_mass_drift<2e-12);
 for(const h of c.mass_energy_histories){
  const row=c.records.find(r=>r.degree===h.degree&&r.cells===h.cells);
  assert.equal(h.samples.length,row.steps+1);assert.equal(h.samples.at(-1).time,.25);
  for(const sample of h.samples)assert.ok(Math.abs(sample.mass-h.samples[0].mass)<=c.metrics.maximum_stage_mass_drift+1e-16);
 }
 assert.ok(c.metrics.time_error_halving_ratio>.1&&c.metrics.time_error_halving_ratio<.15);
 assert.ok(c.metrics.actual_transport_l2_change>.9);
 assert.ok(text(base+'experiments.py').includes('dg_advection(n, p,'));assert.ok(text(base+'fr.py').includes('expm_multiply(csr_matrix(time*matrix)'));
});

test('two new methods and two saved-data previews connect to existing physical problems without duplicating them',()=>{
 const rows=json('numerical-methods-atlas/methods/index.json').methods;
 for(let i=0;i<2;i++){
  const m=rows.find(m=>m.id===methods[i]);assert.equal(m.status,'educational-example');assert.deepEqual(m.execution_examples.map(e=>e.id),[ids[i]]);
  const c=json('numerical-methods-atlas/validation/'+ids[i]+'/index.json');assert.equal(c.problem_id,['poisson-2d-sine','advection-sine'][i]);
  assert.deepEqual(c.execution_navigation.equations.map(e=>e.id),[['poisson-laplace'],['linear-advection']][i]);
 }
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,92);
 const gallery=json('numerical-methods-atlas/gallery/index.json').items;
 for(let i=0;i<2;i++){
  const p=gallery.find(p=>p.id===['poisson-2d-sine','advection-sine'][i]);const e=p.supplemental_execution_entries.find(e=>e.id===ids[i]);
  assert.ok(e.preview.url.endsWith('/'+ids[i]+'-preview.png'));
 }
});

test('bilingual theory, software context and both searches expose the appropriate methods and executions',()=>{
 for(const lang of ['ja','en'])for(let i=0;i<2;i++){
  const c=json(`numerical-methods-atlas/${lang}/read/${methods[i]}/index.json`);
  assert.ok(c.html.includes('katex-mathml')&&!c.html.includes('math-placeholder'));
  assert.ok(c.html.includes('id="'+['fem-comparison','dg-comparison'][i]+'"'));
  assert.deepEqual(c.scoped_supplements.map(c=>c.id),[ids[i]]);
  assert.ok(text(`numerical-methods-atlas/${lang}/read/${methods[i]}/index.md`).includes('| --- |'));
  assert.ok(c.html.includes(['https://github.com/Nek5000/nekRS','https://www.pyfr.org/'][i]));
 }
 const global=makeSearch(json('search/index.json').documents),inline=json('numerical-methods-atlas/home-search-index.json');
 for(const [q,lang,id]of [['SEM Poisson 実行','ja',ids[0]],['FR periodic advection run','en',ids[1]]])for(const rows of [global(q,lang,'atlas'),searchChapters(inline,q,lang)])assert.ok(rows.some(r=>r.kind==='execution-example'&&r.url.includes('/validation/'+id+'/')),q);
 for(const [q,id]of [['SEM',methods[0]],['FR',methods[1]]])for(const rows of [global(q,'ja','atlas'),searchChapters(inline,q,'ja')])assert.ok(rows.some(r=>r.kind==='method'&&r.id===id),q);
 for(const [q,id]of [['Nek5000',methods[0]],['nekRS',methods[0]],['PyFR',methods[1]]])assert.ok(global(q,'en','atlas').some(r=>r.url.includes('/read/'+id+'/')),q);
});
