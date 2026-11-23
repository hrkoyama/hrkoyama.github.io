import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const cases={amg:['sa-amg','amg-conditioning',null],'qr-svd':['qr-svd-factorization','qr-svd-conditioning','matrix-factorization'],eigensolvers:['krylov-eigenvalues','krylov-eigen-conditioning','krylov-spectrum'],quadrature:['gauss-adaptive-quadrature','quadrature-conditioning','quadrature-moments']};

test('four conditioning examples extend their own methods while retaining the original primary releases',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const [methodId,[primary,caseId]] of Object.entries(cases)){
  const method=methods.find(m=>m.id===methodId);
  assert.equal(method.status,'educational-example');
  assert.equal(method.depth_release.group,'foundations');
  assert.deepEqual(method.depth_release.case_ids,[primary]);
  const added=method.depth_additional_releases.filter(x=>x.group==='foundations-conditioning');
  assert.equal(added.length,1);assert.deepEqual(added[0].case_ids,[caseId]);
  assert.ok(added[0].code_urls.some(x=>x.endsWith('/foundations-conditioning/run.py')));
  assert.ok(added[0].test_urls.length>0);
  assert.ok(method.execution_examples.some(x=>x.id===caseId));
  const entry=json(`numerical-methods-atlas/validation/${caseId}/index.json`);
  assert.equal(entry.measured.passed,true);assert.deepEqual(entry.method_ids,[methodId]);
  for(const [path,hash] of Object.entries(entry.source_sha256))assert.equal(sha(path),hash,path);
  for(const lang of ['ja','en'])assert.ok(entry.assumptions[lang]&&entry.validation[lang]&&entry.limits[lang]);
 }
 assert.equal(methods.length,147);
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),{'educational-example':117,'reading-only':14,'planned':16});
});

test('algebraic AMG controls borrow no Poisson validation and the remaining refinements add no problem families',()=>{
 const index=json('numerical-methods-atlas/validation/index.json');
 assert.equal(index.case_count,54);assert.equal(index.groups.length,23);
 assert.equal(Object.values(index.case_problem_ids).filter(x=>x===null).length,5);
 const problems=json('numerical-methods-atlas/test-cases/index.json').problems;
 assert.equal(problems.length,91);
 for(const [,caseId,problemId] of Object.values(cases)){
  assert.equal(index.case_problem_ids[caseId],problemId);
  const linked=problems.filter(p=>(p.supplemental_examples||[]).some(x=>x.id===caseId));
  assert.deepEqual(linked.map(x=>x.id),problemId?[problemId]:[]);
 }
 const poisson=problems.filter(p=>(p.supplemental_examples||[]).some(x=>x.id==='sa-amg'));
 assert.equal(poisson.length,1);
 assert.ok(poisson.every(p=>!(p.supplemental_examples||[]).some(x=>x.id==='amg-conditioning')));
});

test('pre-pilot criteria, all eight earlier archives and the shared lightweight boundary remain fixed',()=>{
 const archives={biology:'d7608d121ad2c5a2b5fb8db8c87bc648f372bb666c3079e6b4835b276d3b5979',foundations:'1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2',mcmc:'7fb1cde233b79e2b2d56edac89c6e1bdbe8239c1b7f5e166054f8e3e2cdaac11',mhd:'2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16',models:'18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c',particles:'8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6',thermostats:'38142da988bf0c790eab7e7f10f8d1e209d074c3627f73a207f5223a24e18d65'};
 for(const [group,hash] of Object.entries(archives))assert.equal(sha(`code/validated-examples/2026-11-22/${group}/atlas-${group}-2026-11-22.zip`),hash);
 assert.equal(sha('code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip'),'5db2fc202014a576145e98c84e1802540df7d8e26353d469fbd55c8e393fd866');
 assert.equal(sha('code/validated-examples/2026-11-22/foundations-conditioning/inputs.json'),'142f7fdeb264f130c64d402f417eb34e0a64e269431137eba5b821e85484306f');
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.doesNotMatch(read('.github/workflows/atlas-public-linux.yml').toString(),/workflow_run:|schedule:/);
 assert.doesNotMatch(read('.github/workflows/atlas-depth-linux.yml').toString(),/pyscf|arviz|xarray|pandas|mpmath|matplotlib/i);
});
