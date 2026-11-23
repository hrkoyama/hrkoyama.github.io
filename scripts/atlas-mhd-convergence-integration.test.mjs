import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const cases=['ct-glm-smooth-convergence','ct-glm-ot-convergence','ct-glm-constraint-control'];
const methods=json('numerical-methods-atlas/methods/index.json').methods;

test('matched CT and GLM examples retain their earlier primary releases and resolve dedicated evidence',()=>{
 for(const id of ['ct','glm']){
  const method=methods.find(m=>m.id===id);
  assert.equal(method.status,'educational-example');
  assert.equal(method.depth_release.group,'mhd');
  assert.deepEqual(method.depth_release.case_ids,id==='ct'?['ct-glm-independent']:['ct-glm-independent','glm-fourier-mode']);
  const added=method.depth_additional_releases.find(x=>x.group==='mhd-convergence');
  assert.deepEqual([...added.case_ids].sort(),[...cases].sort());
  for(const caseId of cases)assert.ok(method.execution_examples.some(x=>x.id===caseId));
  assert.ok(added.code_urls.some(x=>x.endsWith('/mhd-convergence/run.py')));
  assert.ok(added.test_urls.length>0);
 }
 for(const id of cases){
  const entry=json(`numerical-methods-atlas/validation/${id}/index.json`);
  assert.equal(entry.measured.passed,true);
  assert.deepEqual([...entry.method_ids].sort(),['ct','glm']);
  for(const [path,hash] of Object.entries(entry.source_sha256))assert.equal(sha(path),hash,path);
  for(const lang of ['ja','en']){
   assert.ok(entry.assumptions[lang]&&entry.validation[lang]&&entry.limits[lang]);
   const chapter=read(`numerical-methods-atlas/${lang}/read/validation-mhd-convergence/index.html`).toString();
   assert.ok(chapter.includes(lang==='ja'?'入力・検証手順の履歴':'Input and validation protocol history'));
   assert.ok(!chapter.includes('初回の不合格と刻み細分化の記録')&&!chapter.includes('Initial failure and step-refinement record'));
  }
 }
});

test('same-target OT refinements add no problem while the constructed equilibrium adds exactly one',()=>{
 const index=json('numerical-methods-atlas/validation/index.json');
 assert.equal(index.case_count,83);assert.equal(index.groups.length,38);
 assert.equal(index.case_problem_ids[cases[0]],'advected-magnetostatic-equilibrium');
 assert.equal(index.case_problem_ids[cases[1]],'orszag-tang');
 assert.equal(index.case_problem_ids[cases[2]],null);
 assert.equal(Object.values(index.case_problem_ids).filter(x=>x===null).length,5);
 const problems=json('numerical-methods-atlas/test-cases/index.json').problems;
 assert.equal(problems.length,113);
 assert.equal(problems.filter(p=>p.id==='advected-magnetostatic-equilibrium').length,1);
 const ot=problems.find(p=>p.id==='orszag-tang');
 const otExecutions=ot.supplemental_examples.map(x=>x.id);
 assert.deepEqual(otExecutions.filter(id=>id!=='postshock-orszag-tang').sort(),['ct-glm-independent','ct-glm-ot-convergence']);
 assert.deepEqual(otExecutions.filter(id=>id==='postshock-orszag-tang'),['postshock-orszag-tang']);
 assert.equal(methods.length,152);
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),{'educational-example':122,'reading-only':15,'planned':15});
});

test('seven immutable earlier archives, common examples and pre-pilot controls stay fixed',()=>{
 const archives={"biology": "d7608d121ad2c5a2b5fb8db8c87bc648f372bb666c3079e6b4835b276d3b5979", "foundations": "1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2", "mcmc": "7fb1cde233b79e2b2d56edac89c6e1bdbe8239c1b7f5e166054f8e3e2cdaac11", "mhd": "2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16", "models": "18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c", "particles": "8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6", "thermostats": "38142da988bf0c790eab7e7f10f8d1e209d074c3627f73a207f5223a24e18d65"};
 for(const [group,hash] of Object.entries(archives))assert.equal(sha(`code/validated-examples/2026-11-22/${group}/atlas-${group}-2026-11-22.zip`),hash);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.equal(sha('code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json'),'274e3e30d1abfb15efaef12e1e53cdd8176d3bc7229a3a89bcd5fa9e3b67d67d');
 assert.equal(sha('code/validated-examples/2026-11-22/mhd-convergence/inputs.json'),'ef1066846f52a270af0ee89282843ef6ea39279bedac758a1e13a0970c639734');
 const protocol=json('code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json');
 assert.equal(protocol.numerical_pilot_before_revision,false);assert.equal(protocol.physical_case_inputs_and_acceptance_changed,false);
 const workflow=read('.github/workflows/atlas-public-linux.yml').toString();
 assert.doesNotMatch(workflow,/workflow_run:|schedule:/);
 assert.doesNotMatch(read('.github/workflows/atlas-depth-linux.yml').toString(),/pyscf|arviz|xarray|pandas|matplotlib/i);
});
