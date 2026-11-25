// Exact inverse of the reviewed batch78 metadata changes for historical tests.
// Current scientific values are checked before the named metadata is restored.
import {projectCatalogBeforeFinal23,projectMethodBeforeFinal23,methodIdsAddedInFinal23} from './atlas-final23-projection.mjs';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const root=new URL('../../',import.meta.url),sorted=xs=>[...xs].sort();
function load(path,hash){const b=readFileSync(new URL(path,root));assert.equal(createHash('sha256').update(b).digest('hex'),hash,path+'/frozen');return JSON.parse(b);}
const baseline=load('scripts/fixtures/atlas-batch78-87-baseline.json','af74ae58975c6b978bec5a425927ce05c0d894ed5c325443dc452ee7ec6df653');
const freeze=load('scripts/fixtures/atlas-batch78-87-freeze.json','b5ea04031e443f0ec3c2e20e610034bcbbbc326f5884350d454df2fbad85b7ad');
assert.equal(freeze.status,'ROOT_REVIEWED_ACTUAL_CANONICAL_FREEZE');
assert.equal(freeze.source_base_commit,baseline.base_commit);
export const methodIdsAddedInBatch78=Object.freeze(['gauss-kronrod','tanh-sinh','smolyak-sparse-grid','pchip']);
export const methodIdsPromotedInBatch78=Object.freeze(['splines','chebyshev','wavelets','pinn-operators']);
assert.deepEqual(freeze.new_method_ids,[...methodIdsAddedInBatch78]);
assert.deepEqual(freeze.promotions,[...methodIdsPromotedInBatch78]);
function typed(v){
 if(v===null)return Buffer.from('z');
 if(typeof v==='boolean')return Buffer.from(v?'b1':'b0');
 if(typeof v==='number'){assert.ok(Number.isFinite(v));const b=Buffer.alloc(8);b.writeDoubleBE(v);return Buffer.concat([Buffer.from('n'),b]);}
 if(typeof v==='string'){const b=Buffer.from(v);return Buffer.concat([Buffer.from('s'+b.length+':'),b]);}
 if(Array.isArray(v))return Buffer.concat([Buffer.from('a'+v.length+':'),...v.map(typed)]);
 assert.ok(v&&typeof v==='object');const keys=Object.keys(v);return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(k=>[typed(k),typed(v[k])])]);
}
const hash=v=>createHash('sha256').update(typed(v)).digest('hex');
const same=(a,b,label)=>assert.ok(typed(a).equals(typed(b)),label);
const append=['summary','limitations','references','metadata_review','depth_release','depth_additional_releases','supplemental_scope_profiles','depth_scope'];
const promotion=[...append,'status','depth_previous_status','next_deliverable','assumptions','assumptions_ja','units','units_ja','boundary_conditions','boundary_conditions_ja','code_mapping_scope','code_mapping_scope_ja'];
function inverse(row,record,change,allowed){
 assert.ok(row&&record);
 if(!change){assert.equal(hash(row),record.typed_sha256,row.id+'/unchanged');return row;}
 assert.deepEqual(sorted(Object.keys(row)),change.after_keys,row.id+'/after-keys');
 assert.deepEqual(sorted(record.keys),change.before_keys,row.id+'/before-keys');
 const changed=sorted(new Set([...Object.keys(change.before),...Object.keys(change.after),...change.before_absent,...change.after_absent]));
 for(const key of changed){
  assert.ok(allowed.includes(key),row.id+'/'+key+'/authorized');
  assert.notEqual(Object.hasOwn(change.before,key),change.before_absent.includes(key));
  assert.notEqual(Object.hasOwn(change.after,key),change.after_absent.includes(key));
  if(Object.hasOwn(change.after,key)){assert.ok(Object.hasOwn(row,key));same(row[key],change.after[key],row.id+'/'+key+'/exact-after');}
  else assert.ok(!Object.hasOwn(row,key),row.id+'/'+key+'/absent-after');
 }
 const copy={...row};for(const key of changed){if(Object.hasOwn(change.before,key))copy[key]=structuredClone(change.before[key]);else delete copy[key];}
 assert.deepEqual(sorted(Object.keys(copy)),change.before_keys);
 const ordered=Object.fromEntries(record.keys.map(k=>[k,copy[k]]));
 assert.equal(hash(ordered),record.typed_sha256,row.id+'/all-old-values');return ordered;
}
export function projectMethodBeforeBatch78(row){
 row=projectMethodBeforeFinal23(row);
 if(methodIdsAddedInFinal23.includes(row.id))return row;
 const record=baseline.method_records[row.id];
 if(!record){assert.ok(methodIdsAddedInBatch78.includes(row.id),row.id+'/known-new-method');assert.equal(hash(row),freeze.new_method_records_typed_sha256[row.id]);return row;}
 return inverse(row,record,freeze.method_transitions[row.id],methodIdsPromotedInBatch78.includes(row.id)?promotion:append);
}
export function projectEquationBeforeBatch78(row){
 const before=baseline.models[row.id];
 if(!before){assert.ok(freeze.new_model_ids.includes(row.id),row.id+'/known-new-model');return row;}
 const allowed=['supplemental_examples',...(['bio-enzyme','bio-lotka-volterra'].includes(row.id)?['status','note','execution_scope','coverage_scope']:[])];
 return inverse(row,{keys:Object.keys(before),typed_sha256:hash(before)},freeze.model_transitions[row.id],allowed);
}
function projectProblem(row){
 const record=baseline.problem_records[row.id];
 if(!record)return row;
 return inverse(row,record,freeze.problem_transitions[row.id],['method_ids','equation_ids','supplemental_examples','references']);
}
function exactIDs(rows,oldIDs,newIDs,label){
 const ids=rows.map(r=>r.id);assert.equal(new Set(ids).size,ids.length,label+'/no-duplicate');
 assert.deepEqual(sorted(ids),sorted([...oldIDs,...newIDs]),label+'/exact-cohort');
}
const newProblems=[...new Set(Object.values(freeze.case_problem_ids))].filter(id=>!Object.hasOwn(baseline.problem_records,id));
function registryBefore78(value){
 const rows=value.releases,ids=rows.map(r=>r.group),groups=Object.keys(freeze.expected_new_groups);
 assert.equal(new Set(ids).size,ids.length);assert.deepEqual(sorted(ids),sorted([...baseline.release_order,...groups]));
 assert.equal(value.case_count,138);
 const old=rows.filter(r=>baseline.release_order.includes(r.group));same(old,baseline.releases,'all-old-release-values');
 for(const group of groups){const row=rows.find(r=>r.group===group),f=freeze.canonical_packets[group];
  assert.equal(row.edition,f.edition);same(row.case_ids,sorted(freeze.expected_new_groups[group]),group+'/sorted-registry-cases');assert.equal(row.tests,f.tests);
  for(const key of ['archive_sha256','manifest_sha256','verification_sha256'])assert.equal(row[key],f[key]);
  assert.equal(row.archive,f.archive_file);assert.equal(row.base,'https://hrkoyama.github.io/'+f.base);
 }
 return {...value,releases:old,case_count:127};
}
// Use only in a dated historical-cohort test. Current registration checks keep
// the complete new cohort and validate its actual canonical packets separately.
export function projectCatalogBeforeBatch78(path,value){
 value=projectCatalogBeforeFinal23(path,value);
 if(path==='catalog/atlas-methods.json'){
  exactIDs(value.methods,baseline.method_order,methodIdsAddedInBatch78,'methods');
  for(const row of value.methods)if(methodIdsAddedInBatch78.includes(row.id))projectMethodBeforeBatch78(row);
  return {...value,methods:value.methods.filter(r=>!methodIdsAddedInBatch78.includes(r.id))};
 }
 if(path==='catalog/atlas-equations.json'){
  exactIDs(value.equations,Object.keys(baseline.models),freeze.new_model_ids,'models');
  return {...value,equations:value.equations.filter(r=>Object.hasOwn(baseline.models,r.id)).map(projectEquationBeforeBatch78)};
 }
 if(path==='catalog/atlas-test-problems.json'){
  exactIDs(value.problems,baseline.problem_order,newProblems,'problems');
  return {...value,problems:value.problems.filter(r=>Object.hasOwn(baseline.problem_records,r.id)).map(projectProblem)};
 }
 if(path==='catalog/atlas-gallery.json'){
  exactIDs(value.items,baseline.gallery_order,newProblems,'gallery');
  const old=value.items.filter(r=>Object.hasOwn(baseline.gallery_records,r.id));
  for(const row of old)assert.equal(hash(row),baseline.gallery_records[row.id].typed_sha256,row.id+'/old-primary');
  return {...value,items:old};
 }
 if(path==='numerical-methods-atlas/validation/releases.json')return registryBefore78(value);
 return value;
}
