import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const json=path=>JSON.parse(readFileSync(new URL(path,root),'utf8'));
const oldIds=['langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'];
const ids=[...oldIds,'two-state-bo-cp-ou','deterministic-thermostat-contrasts','projected-canonical-dof'];
const depth=json('catalog/atlas-depth.json');
const goal=json('catalog/atlas-goals.json').goals.find(item=>item.id==='temperature-control');
const route=json('catalog/atlas-crossovers.json').routes.find(item=>item.id==='dft-md');
const stage=route.stages.find(item=>item.id==='thermostat');

test('field and goal retain the old four thermal components plus separate fixed cases; crossover keeps its four-component scope',()=>{
 const field=depth.fields.find(item=>item.id==='temperature');
 assert.deepEqual(field.supplemental_examples,ids);
 assert.deepEqual(goal.supplemental_examples,ids);
 assert.deepEqual(stage.supplemental_ids,oldIds);
 assert.deepEqual(field.examples,[]);assert.deepEqual(goal.examples,[]);assert.deepEqual(stage.example_ids,[]);
 for(const item of [field])for(const lang of ['ja','en']){
  assert.ok(item.scope[lang].includes('CSVR')&&item.scope[lang].includes('Langevin'));
  assert.ok(item.scope[lang].includes('OBABO')&&item.scope[lang].includes('BAOAB'));
 }
 assert.match(field.scope.ja,/2手法/);assert.match(field.scope.ja,/残る6手法/);
 assert.match(field.scope.en,/remaining six methods/);
 for(const lang of ['ja','en'])assert.match(goal.scope[lang],lang==='ja'?/未達・未解決/:/unmet\/unresolved/);
 assert.match(field.reference.en,/Gamma/);assert.match(field.reference.en,/CIR/);
 assert.match(field.reference.en,/shadow Gaussian/);assert.match(field.reference.en,/independent quadrature/);
 assert.match(field.refinement.en,/correlations need not agree/);
 assert.match(stage.supplemental_scope.en,/same OBABO/);
 assert.match(stage.supplemental_scope.en,/quartic lambda=0.2/);
 assert.equal(stage.supplemental_role,'scoped-component');
 assert.ok(stage.reading.some(item=>item.url.en==='/numerical-methods-atlas/en/read/validation-thermostats/'));
});

test('new classical thermostat evidence does not enter first-principles stages or certify quantum coupling',()=>{
 const md=route.stages.find(item=>item.id==='first-principles-md');
 assert.deepEqual(md.example_ids,[]);assert.deepEqual(md.supplemental_ids||[],[]);
 for(const item of [route,route.connections.find(item=>item.id==='md-to-thermostat')]){
  assert.equal(item.coupled_validation.status,'not-executed');
  assert.deepEqual(item.coupled_validation.example_ids,[]);
  assert.deepEqual(item.coupled_validation.supplemental_ids||[],[]);
 }
 assert.match(stage.supplemental_scope.en,/consume neither BOMD\/CPMD nuclear geometries nor interatomic forces/);
 assert.match(stage.gap.en,/separate fixed-input examples of other algorithms are not evidence of coupling/);
 const reference=json('catalog/atlas-crossovers.json').references.find(item=>item.id==='bussi2007csvr');
 assert.equal(reference.year,2007);assert.ok(reference.review_level&&reference.review.ja&&reference.review.en);
 assert.ok(route.connections.find(item=>item.id==='md-to-thermostat').reference_ids.includes(reference.id));
 for(const field of depth.fields.filter(item=>item.id.startsWith('quantum-'))){
  assert.match(field.next.en,/only on explicit need/);
 }
 const program=String.raw`
import ast,pathlib,sys
sys.path.insert(0,'scripts')
from atlas_crossovers import SUPPLEMENT_STAGE_CASES
expected={'langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'}
assert SUPPLEMENT_STAGE_CASES['thermostat']==expected
assert 'first-principles-md' not in SUPPLEMENT_STAGE_CASES
for path in ['scripts/atlas_crossovers.py','scripts/atlas_depth.py','scripts/build-atlas-depth.py']:
 ast.parse(pathlib.Path(path).read_text())
print('scoped thermal allowlist and generators valid')
`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/allowlist and generators valid/);
});
