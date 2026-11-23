import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const cases=['schnakenberg-nonlinear','schnakenberg-pattern'];
const methods=json('numerical-methods-atlas/methods/index.json').methods;

test('time refinement preserves the initially declared numerical acceptance criteria and physical model',()=>{
 const base='code/validated-examples/2026-11-22/biology/';
 const initial=json(base+'inputs-initial.json'),current=json(base+'inputs.json');
 assert.equal(sha(base+'inputs-initial.json'),'aa97550f4d965505da9841d2e565b066a02e7af1d7585585e001bea0eb52accb');
 assert.equal(sha(base+'inputs.json'),'375d70f40187400bf812dcd09d4beb0a8f7f3a79baf6a67c818b940bf82bbb84');
 for(const id of cases){
  for(const key of ['acceptance','a','b','diffusion','initial_cosine_coefficients','time','grids','reference_modes','reference_rtol','tight_rtol'])assert.deepEqual(current.cases[id][key],initial.cases[id][key],id+'/'+key);
  assert.ok(current.cases[id].space_step<initial.cases[id].space_step);
  assert.ok(current.cases[id].time_steps.every((h,i)=>h<initial.cases[id].time_steps[i]));
 }
});

test('nonlinear biological comparisons reuse one physical problem and preserve the earlier linear-onset release',()=>{
 const index=json('numerical-methods-atlas/validation/index.json');
 assert.equal(index.case_count,54);
 assert.equal(index.groups.length,23);
 for(const id of cases)assert.equal(index.case_problem_ids[id],'turing-schnakenberg');
 const inventory=json('numerical-methods-atlas/test-cases/index.json').problems;
 assert.equal(inventory.length,91);
 assert.equal(inventory.filter(x=>x.id==='turing-schnakenberg').length,1);
 const problem=inventory.find(x=>x.id==='turing-schnakenberg');
 assert.deepEqual(new Set(problem.supplemental_examples.map(x=>x.id)),new Set(['turing-schnakenberg',...cases,'reaction-diffusion-splitting']));
 const centered=methods.find(x=>x.id==='centered-difference');
 assert.equal(centered.depth_release.group,'models');
 assert.deepEqual(centered.depth_release.case_ids,['reaction-diffusion-fourier','turing-schnakenberg']);
 assert.deepEqual(centered.depth_additional_releases.find(x=>x.group==='biology').case_ids,cases);
 const midpoint=methods.find(x=>x.id==='implicit-midpoint');
 assert.equal(midpoint.depth_release.group,'biology');
 assert.deepEqual(midpoint.depth_release.case_ids,cases);
 const rk4=methods.find(x=>x.id==='rk4');
 assert.ok(!rk4.execution_examples.some(x=>cases.includes(x.id)),'new midpoint/Strang cases cannot be borrowed by RK4');
});

test('five earlier supplement archives, the common registry and unrelated availability stay unchanged',()=>{
 const hashes={foundations:'1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2',models:'18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c',particles:'8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6',mhd:'2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16',thermostats:'38142da988bf0c790eab7e7f10f8d1e209d074c3627f73a207f5223a24e18d65'};
 for(const [group,hash] of Object.entries(hashes))assert.equal(sha(`code/validated-examples/2026-11-22/${group}/atlas-${group}-2026-11-22.zip`),hash);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.equal(methods.length,147);
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),{'educational-example':117,'reading-only':14,'planned':16});
 const bio=json('numerical-methods-atlas/assets/biological-models.json').models;
 assert.deepEqual(new Set(bio.filter(x=>x.status==='scoped-educational-example').map(x=>x.id)),new Set(['logistic','sir','turing','schnakenberg','fitzhugh-nagumo']));
 const detailed=read('.github/workflows/atlas-public-linux.yml').toString();
 assert.doesNotMatch(detailed,/workflow_run:|schedule:/);
 assert.doesNotMatch(read('.github/workflows/atlas-depth-linux.yml').toString(),/pyscf|quantum-periodic|matplotlib/i);
});

test('both languages expose nonlinear examples and actual independently rerun evidence',()=>{
 for(const id of cases){
  const record=json(`numerical-methods-atlas/validation/${id}/index.json`);
  assert.equal(record.measured.passed,true);
  assert.ok(record.references.some(x=>x.doi==='10.1016/0022-5193(79)90042-0'));
  for(const lang of ['ja','en']){
   const chapter=read(`numerical-methods-atlas/${lang}/read/validation-biology/index.html`).toString();
   const survey=read(`numerical-methods-atlas/${lang}/read/biological-models/index.html`).toString();
   assert.ok(chapter.includes(`id="${id}"`));
   assert.ok(chapter.includes('/biology/protocol-history.json'));
   assert.ok(chapter.includes('/biology/inputs-initial.json'));
   assert.ok(survey.includes(`/validation/${id}/?lang=${lang}`));
   assert.ok(record.assumptions[lang]&&record.validation[lang]&&record.limits[lang]);
  }
  for(const [path,hash] of Object.entries(record.source_sha256))assert.equal(sha(path),hash,path);
 }
});
