import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
import {makeSearch} from '../search/engine.mjs';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const base='code/validated-examples/2026-11-22/splitting/';
const id='reaction-diffusion-splitting';
const inputs=json(base+'inputs.json'),config=inputs.cases[id];
const result=json(base+'results/result.json'),measured=result.cases[0];
const receipt=json(base+'verification.json');

test('one predeclared short-time comparison keeps the old nonlinear input and every original acceptance criterion',()=>{
 const old=json('code/validated-examples/2026-11-22/biology/inputs.json').cases['schnakenberg-nonlinear'];
 for(const key of ['a','b','diffusion','initial_cosine_coefficients'])assert.deepEqual(config[key],old[key],key);
 assert.equal(config.grid,32);assert.equal(config.time,1);
 assert.deepEqual(config.step_counts,[16,32,64,128]);
 assert.deepEqual(config.snapshot_times,[0,.25,.5,.75,1]);
 assert.equal(sha(base+'inputs.json'),sha(base+'inputs-initial.json'));
 const history=json(base+'protocol-history.json');
 assert.equal(history.first_fixed_protocol_passed,true);
 assert.equal(history.acceptance_modified_after_first_execution,false);
 assert.equal(history.input_sha256_before_first_execution,sha(base+'inputs.json'));
 assert.equal(result.input_sha256,sha(base+'inputs.json'));
 assert.equal(receipt.passed_tests,16);assert.equal(receipt.all_cases_rerun,true);
 for(const key of ['failures','errors','skipped','returncode'])assert.equal(receipt[key],0);
 execFileSync('python3',['-B','-c',"import pathlib,sys;sys.path.insert(0,'scripts');from atlas_depth_release import load_depth_group;assert load_depth_group(pathlib.Path.cwd(),'splitting','2026-11-22')['verification']['passed']"],{cwd:fileURLToPath(root)});
});

test('stored observed orders follow shared-time errors and the actual subsolver work, with resolved references',()=>{
 assert.ok(result.passed&&measured.passed&&Object.values(measured.checks).every(Boolean));
 assert.deepEqual(measured.reference_records.map(row=>row.method),['Radau','Radau','DOP853']);
 assert.ok(measured.metrics.reference_to_strang_error_ratio<config.acceptance.reference_to_strang_error_ratio_max);
 assert.match(measured.reference_scope,/SAME.*FD/);assert.match(measured.reference_scope,/No continuum/);
 for(const [method,order] of [['lie-trotter',1],['strang',2]]){
  const rows=measured.records.filter(row=>row.method===method);
  assert.deepEqual(rows.map(row=>row.steps),config.step_counts);
  rows.forEach((row,index)=>{
   const observed=measured.time_records.filter(x=>x.method===method&&x.steps===row.steps);
   assert.deepEqual(observed.map(x=>x.time),config.snapshot_times);
   assert.equal(row.max_l2,Math.max(...observed.slice(1).map(x=>x.l2)));
   assert.equal(row.reaction_calls,row.steps);
   assert.equal(row.diffusion_calls,row.steps*(method==='strang'?2:1));
   if(index){assert.ok(Math.abs(row.observed_order_l2-Math.log2(rows[index-1].max_l2/row.max_l2))<1e-12);assert.ok(Math.abs(row.observed_order_l2-order)<.2);}
  });
 }
 assert.ok(measured.metrics.minimum_concentration>0);
 assert.ok(measured.metrics.maximum_reaction_balance_error<config.acceptance.reaction_balance_max);
 const referenceSource=read(base+'reference.py');
 assert.doesNotMatch(referenceSource,/^(?:from splitting import|import splitting)/m);
 assert.ok(referenceSource.includes('solve_ivp')&&referenceSource.includes('bmat'));
});

test('the two methods acquire only the verified dedicated release and the physical/common problem inventories stay fixed',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 assert.equal(methods.length,149);
 for(const methodId of ['lie-trotter','strang-splitting']){
  const method=methods.find(x=>x.id===methodId);
  assert.equal(method.status,'educational-example');
  assert.equal(method.depth_previous_status,'reading-only');
  assert.equal(method.depth_release.group,'splitting');
  assert.deepEqual(method.depth_release.case_ids,[id]);
  assert.deepEqual(method.execution_examples.map(x=>x.id),[id]);
  assert.ok(method.code_urls.every(url=>url.includes('/splitting/')));
 }
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.releases.length,21);assert.equal(registry.case_count,51);
 assert.equal(registry.releases.filter(row=>!['noh','noh-cartesian','sedov','double-mach','forward-step','low-mach','guderley','euler-positivity','zalesak','level-set'].includes(row.group)).reduce((sum,row)=>sum+row.tests,0),388);
 assert.equal(registry.releases.find(row=>row.group==='noh').tests,28);
 assert.equal(registry.releases.filter(row=>!['euler-positivity','zalesak','level-set'].includes(row.group)).reduce((sum,row)=>sum+row.tests,0),571);
 const problems=json('numerical-methods-atlas/test-cases/index.json').problems;
 assert.equal(problems.length,88);
 assert.deepEqual(problems.filter(p=>(p.supplemental_examples||[]).some(x=>x.id===id)).map(x=>x.id),['turing-schnakenberg']);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 const oldArchive='code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip';
 assert.equal(sha(oldArchive),'d7608d121ad2c5a2b5fb8db8c87bc648f372bb666c3079e6b4835b276d3b5979');
});

test('bilingual reading, numerical entries and both searches lead to the published input/ZIP/figure instead of borrowing another example',()=>{
 const route=`numerical-methods-atlas/validation/${id}/`;
 const entry=json(route+'index.json'),html=read(route+'index.html');
 assert.equal(entry.problem_id,'turing-schnakenberg');assert.deepEqual(entry.measured,measured);
 for(const lang of ['ja','en']){
  const chapter=json(`numerical-methods-atlas/${lang}/read/operator-splitting/index.json`);
  assert.ok(chapter.html.includes(`/validation/${id}/?lang=${lang}`));
  assert.deepEqual(chapter.scoped_supplements.map(x=>x.id),[id]);
  assert.ok(read(`numerical-methods-atlas/${lang}/read/validation-splitting/index.html`).includes(`id="${id}"`));
  assert.ok(json(`numerical-methods-atlas/${lang}/read/index.json`).groups.some(g=>g.chapters.some(c=>c.id==='validation-splitting')));
  for(const field of ['assumptions','algorithm','validation','limits'])assert.ok(entry[field][lang]);
 }
 for(const name of ['inputs.json','source-manifest.json','verification.json','results/result.json',`results/${id}.png`,'atlas-splitting-2026-11-22.zip']){
  assert.ok(existsSync(new URL(base+name,root)));
  assert.ok(html.includes('/'+base+name),name);
 }
 const inline=json('numerical-methods-atlas/home-search-index.json');
 const global=makeSearch(json('search/index.json').documents);
 for(const [query,lang] of [['Lie-Trotter 実行','ja'],['Strang 反応拡散 実行','ja'],['Lie Trotter reaction diffusion run','en']]){
  const found=searchChapters(inline,query,lang)[0];
  assert.equal(found.kind,'execution-example',query);assert.ok(found.url.includes(`/validation/${id}/`),query);
  const all=global(query,lang,'atlas')[0];
  assert.equal(all.kind,'execution-example',query);assert.ok(all.url.includes(`/validation/${id}/`),query);
 }
});
