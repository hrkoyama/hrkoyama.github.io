import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const bytes=p=>fs.readFileSync(new URL(p,root));
const read=p=>JSON.parse(bytes(p));
const hash=p=>createHash('sha256').update(bytes(p)).digest('hex');
const registry=read('catalog/atlas-execution-examples.json');
const depth=read('numerical-methods-atlas/depth/index.json');
const methods=read('numerical-methods-atlas/methods/index.json').methods;

test('field depth binds to the current successful public-registry rerun and its actual evidence',()=>{
 const receipt=read(new URL(depth.verification_receipt).pathname.slice(1));
 assert.equal(receipt.registry_source_mode,'public-registry');assert.equal(receipt.passed,true);
 assert.equal(receipt.registry_sha256,hash('numerical-methods-atlas/code-and-data/examples.json'));
 for(const [p,h] of Object.entries(depth.source_sha256))assert.equal(hash(p),h,p);
 for(const field of depth.fields)for(const id of field.examples){
  assert.ok(registry.examples.some(e=>e.id===id));assert.equal(receipt.examples.find(e=>e.id===id)?.passed,true);
 }
});
test('supplements retain their own evidence and do not borrow or expand the common execution registry',()=>{
 assert.equal(registry.examples.length,22);
 assert.equal(hash('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.deepEqual(depth.fields.find(f=>f.id==='temperature').examples,[]);
 assert.deepEqual(depth.fields.find(f=>f.id==='temperature').supplemental_examples,['langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic']);
 assert.deepEqual(depth.fields.find(f=>f.id==='biology').examples,['logistic-growth','sir-epidemic']);
 assert.deepEqual(depth.fields.find(f=>f.id==='probability').examples,['mc-integral','gbm-sde']);
 const supplementIds=depth.fields.flatMap(f=>f.supplemental_examples||[]);
 const expectedCount=Object.keys(read('catalog/atlas-depth-expansion.json').case_problem_ids).length;
 assert.equal(supplementIds.length,expectedCount);assert.equal(new Set(supplementIds).size,expectedCount);
 assert.equal(read('catalog/atlas-depth-expansion.json').case_problem_ids['csvr-kinetic-kernel'],null);
 assert.deepEqual(new Set(supplementIds),new Set(Object.keys(read('catalog/atlas-depth-expansion.json').case_problem_ids)));
 const verified=JSON.parse(execFileSync('python3',['-c',`import sys,json
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_goal_availability import load_supplemental_examples
r=Path('.')
d=json.loads((r/'catalog/atlas-depth.json').read_text())
ids=[i for f in d['fields'] for i in f.get('supplemental_examples',[])]
print(json.dumps([x['id'] for x in load_supplemental_examples(r,ids)]))`],{cwd:root,encoding:'utf8'}));
 assert.deepEqual(verified,supplementIds);
 for(const id of ['mcmc','langevin-thermostat','stochastic-velocity-rescaling','ewald','pme','spme']){
  const method=methods.find(m=>m.id===id);assert.ok(method,id);assert.equal(method.status,'educational-example');assert.ok(method.code_urls.length);assert.ok(method.test_urls.length);
 }
 for(const id of ['nose-hoover','berendsen-thermostat']){
  const method=methods.find(m=>m.id===id);assert.ok(method,id);assert.equal(method.status,'planned');assert.deepEqual(method.code_urls,[]);assert.deepEqual(method.execution_examples,[]);
 }
 const survey=read('numerical-methods-atlas/assets/biological-models.json');
 assert.equal(survey.models.length,22);
 assert.deepEqual(new Set(survey.models.filter(m=>m.status==='scoped-educational-example').map(m=>m.id)),new Set(['logistic','sir','turing','schnakenberg','fitzhugh-nagumo']));
 assert.notEqual(survey.models.find(m=>m.id==='hodgkin-huxley').status,'scoped-educational-example');
 assert.notEqual(survey.models.find(m=>m.id==='gray-scott').status,'scoped-educational-example');
 for(const lang of ['ja','en']){
  const html=bytes(`numerical-methods-atlas/${lang}/read/biological-models/index.html`).toString();
  assert.ok(html.includes('biological-execution-scope'));assert.ok(!html.includes('22項目すべてが文献調査とベンチマーク設計案です。'));assert.ok(!/All 22 entries are literature and proposed/.test(html));
  for(const id of ['reaction-diffusion-fourier','turing-schnakenberg','fitzhugh-nagumo'])assert.ok(html.includes('/numerical-methods-atlas/validation/'+id+'/?lang='+lang));
  const thermo=bytes(`numerical-methods-atlas/${lang}/read/thermostats/index.html`).toString();
  for(const id of ['langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'])assert.ok(thermo.includes('/numerical-methods-atlas/validation/'+id+'/?lang='+lang));
  assert.ok(thermo.includes('OBABO')&&thermo.includes('BAOAB'));
  assert.ok(!thermo.includes('Dedicated code and measured verification results are under construction.'));
 }
});
test('four scoped cases preserve model inputs, independent/analytic references and measured convergence rather than promoting full method families',()=>{
 assert.equal(methods.length,145);
 const base='code/model-benchmarks/2026-11-22/';const verification=read(base+'verification.json');
 assert.equal(verification.passed,11);assert.equal(verification.recipes.length,4);
 for(const id of ['logistic-growth','sir-epidemic','mc-integral','gbm-sde']){
  const e=registry.examples.find(e=>e.id===id);const input=read(base+e.inputs.path);const result=read(base+'results/'+id+'/result.json');
  assert.equal(result.input_sha256,hash(base+e.inputs.path));assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');assert.ok(Object.values(result.checks).every(v=>v===true));
  assert.ok(input.acceptance);assert.ok(e.scope.ja&&e.scope.en);
 }
 const sir=read(base+'references/sir.json');assert.ok(sir.tolerance_refinement_max_difference<1e-9);
 const refCode=bytes(base+'reference_sir.py').toString();assert.ok(!/from (models|run) import/.test(refCode));assert.ok(refCode.includes("method='DOP853'"));
 assert.ok(read(base+'results/sir-epidemic/result.json').metrics.mass_balance_max<2e-13);
 const gbm=read(base+'results/gbm-sde/result.json');assert.ok(gbm.metrics.observed_orders.every(p=>p>=.35&&p<=.7));
});
