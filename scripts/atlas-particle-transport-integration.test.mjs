import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const mapping={ewald:['ewald','ewald-convergence','neutral-periodic-charges'],pme:['spme','spme-convergence','neutral-periodic-charges'],spme:['spme','spme-convergence','neutral-periodic-charges'],fmm:['fmm','fmm-convergence','logarithmic-particles'],pic:['pic','pic-conservation','cold-plasma-pic'],dsmc:['dsmc','dsmc-statistics','maxwell-collisions'],'radiation-transport':['radiation-transport','radiation-convergence','absorbing-slab']};

test('seven methods retain original particle releases and expose precisely their new measured cases',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const [id,[previous,added]] of Object.entries(mapping)){
  const method=methods.find(m=>m.id===id);
  assert.equal(method.status,'educational-example');assert.equal(method.depth_release.group,'particles');assert.deepEqual(method.depth_release.case_ids,[previous]);
  const release=method.depth_additional_releases.filter(x=>x.group==='particle-transport');
  assert.equal(release.length,1);assert.deepEqual(release[0].case_ids,[added]);assert.ok(release[0].code_urls.some(u=>u.endsWith('/particle-transport/run.py')));assert.ok(release[0].test_urls.length);
  assert.ok(method.execution_examples.some(x=>x.id===added));
 }
 for(const id of new Set(Object.values(mapping).map(x=>x[1]))){
  const entry=json(`numerical-methods-atlas/validation/${id}/index.json`);assert.equal(entry.measured.passed,true);
  for(const [path,hash] of Object.entries(entry.source_sha256))assert.equal(sha(path),hash,path);
  for(const lang of ['ja','en'])assert.ok(entry.assumptions[lang]&&entry.validation[lang]&&entry.limits[lang]);
 }
 assert.equal(methods.length,147);assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(x=>x.status===s).length])),{'educational-example':116,'reading-only':15,'planned':16});
});

test('six refinements reuse five physical families without changing diagnostic or problem totals',()=>{
 const index=json('numerical-methods-atlas/validation/index.json');assert.equal(index.case_count,42);assert.equal(index.groups.length,13);assert.equal(Object.values(index.case_problem_ids).filter(x=>x===null).length,5);
 const problems=json('numerical-methods-atlas/test-cases/index.json').problems;assert.equal(problems.length,84);
 for(const [,caseId,problemId] of Object.values(mapping)){
  assert.equal(index.case_problem_ids[caseId],problemId);
  assert.deepEqual(problems.filter(p=>(p.supplemental_examples||[]).some(x=>x.id===caseId)).map(x=>x.id),[problemId]);
 }
 const entry=json('numerical-methods-atlas/problems/neutral-periodic-charges/index.json');
 assert.deepEqual(entry.executions.filter(x=>['ewald-convergence','spme-convergence'].includes(x.id)).map(x=>x.id).sort(),['ewald-convergence','spme-convergence']);
});

test('nine immutable earlier archives, pre-pilot criteria and quantum-light separation remain fixed',()=>{
 const archives={"code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip":"d7608d121ad2c5a2b5fb8db8c87bc648f372bb666c3079e6b4835b276d3b5979","code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip":"1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2","code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip":"71d8f0d3b0bed4a6a97f976aabfd02cc0baf08a30c1655f6b1ea42ea16df3c9d","code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip":"7fb1cde233b79e2b2d56edac89c6e1bdbe8239c1b7f5e166054f8e3e2cdaac11","code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip":"2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16","code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip":"5db2fc202014a576145e98c84e1802540df7d8e26353d469fbd55c8e393fd866","code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip":"18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c","code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip":"8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6","code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip":"38142da988bf0c790eab7e7f10f8d1e209d074c3627f73a207f5223a24e18d65"};
 for(const [path,hash] of Object.entries(archives))assert.equal(sha(path),hash,path);
 assert.equal(Object.keys(archives).length,9);
 assert.equal(sha('code/validated-examples/2026-11-22/particle-transport/inputs.json'),'c90c95405e1622affc84c3feaffc50a7f5599fc868741823e26c7840eeda288b');
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 const receipt=json('code/validated-examples/2026-11-22/particle-transport/verification.json');assert.equal(receipt.tests,75);assert.equal(receipt.all_cases_rerun,true);
 const protocol=json('code/validated-examples/2026-11-22/particle-transport/protocol-history.json');assert.equal(protocol.locked_before_primary_pilot_and_reference,true);assert.equal(protocol.post_pilot_criteria_changes,false);
 assert.doesNotMatch(read('.github/workflows/atlas-public-linux.yml').toString(),/workflow_run:|schedule:/);
 assert.doesNotMatch(read('.github/workflows/atlas-depth-linux.yml').toString(),/pyscf|arviz|matplotlib|mpmath/i);
});
