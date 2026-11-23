import {methodCount,methodStatusCounts} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const cases=['mcmc-multimodal-mixing','mcmc-diagnostic-reference'];
const methods=json('numerical-methods-atlas/methods/index.json').methods;

 test('modern multimodal diagnostics supplement the earlier Gaussian example without borrowing its evidence',()=>{
 const method=methods.find(x=>x.id==='mcmc');
 assert.equal(method.status,'educational-example');
 assert.equal(method.depth_release.group,'models');
 assert.deepEqual(method.depth_release.case_ids,['gaussian-mcmc']);
 const added=method.depth_additional_releases.find(x=>x.group==='mcmc');
 assert.deepEqual(added.case_ids,cases);
 for(const id of ['gaussian-mcmc',...cases])assert.ok(method.execution_examples.some(x=>x.id===id));
 assert.ok(added.code_urls.some(x=>x.endsWith('/mcmc/run.py')));
 assert.ok(added.test_urls.length>0);
 for(const id of cases){
  const entry=json(`numerical-methods-atlas/validation/${id}/index.json`);
  assert.equal(entry.measured.passed,true);
  assert.deepEqual(entry.method_ids,['mcmc']);
  for(const [path,h] of Object.entries(entry.source_sha256))assert.equal(sha(path),h,path);
  for(const lang of ['ja','en']){
   assert.ok(entry.assumptions[lang]&&entry.validation[lang]&&entry.limits[lang]);
   const chapter=read(`numerical-methods-atlas/${lang}/read/mcmc/index.html`).toString();
   assert.ok(chapter.includes(`/validation/${id}/?lang=${lang}`));
  }
 }
});

 test('three sampler scenarios add one target and the calibration diagnostic adds no physical problem',()=>{
 const d=json('numerical-methods-atlas/validation/index.json');
 assert.equal(d.case_count,71);assert.equal(d.groups.length,30);
 assert.equal(d.case_problem_ids[cases[0]],'mcmc-bimodal-mixture');
 assert.equal(d.case_problem_ids[cases[1]],null);
 const problems=json('numerical-methods-atlas/test-cases/index.json').problems;
 assert.equal(problems.length,102);
 assert.equal(problems.filter(p=>p.id==='mcmc-bimodal-mixture').length,1);
 assert.ok(!problems.some(p=>p.id===cases[1]));
 assert.equal(problems.find(p=>p.id==='mcmc-bimodal-mixture').supplemental_examples.length,1);
 assert.equal(methods.length,methodCount);
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),methodStatusCounts);
});

 test('the six earlier archives, common registry and pre-run MCMC input remain fixed',()=>{
 const archives={"biology": "d7608d121ad2c5a2b5fb8db8c87bc648f372bb666c3079e6b4835b276d3b5979", "foundations": "1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2", "mhd": "2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16", "models": "18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c", "particles": "8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6", "thermostats": "38142da988bf0c790eab7e7f10f8d1e209d074c3627f73a207f5223a24e18d65"};
 for(const [group,h] of Object.entries(archives))assert.equal(sha(`code/validated-examples/2026-11-22/${group}/atlas-${group}-2026-11-22.zip`),h);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.equal(sha('code/validated-examples/2026-11-22/mcmc/inputs.json'),'b20b594ab2d001426fbc58d1fe86fe4719bd42455f6a10f502966f85fb6eb49a');
 const workflow=read('.github/workflows/atlas-public-linux.yml').toString();
 assert.doesNotMatch(workflow,/workflow_run:|schedule:/);
 assert.doesNotMatch(read('.github/workflows/atlas-depth-linux.yml').toString(),/pyscf|arviz|xarray|pandas|matplotlib/i);
});
