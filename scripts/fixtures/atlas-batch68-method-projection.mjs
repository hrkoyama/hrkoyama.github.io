// Strict, dated inverse of the reviewed batch68–77 method metadata changes.
// Unchanged values come from the current row, never from a baseline substitute.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const root=new URL('../../',import.meta.url);
const load=(name,expected)=>{
 const bytes=readFileSync(new URL(name,root));
 assert.equal(createHash('sha256').update(bytes).digest('hex'),expected,name+'/frozen-bytes');
 return JSON.parse(bytes);
};
const baseline=load('scripts/fixtures/atlas-batch68-77-baseline.json','d499b7ed43875a18a71a66dbf02114bd981bec8b8cb4e2f0326a419d9b82b506');
const transition=load('scripts/fixtures/atlas-batch68-77-method-transition.json','af06addc47ad365783697edf89da2bdc476105f91eac213bb5fc205eec03429e');
export const methodIdsAddedInBatch68=Object.freeze(['rk45','jameson-steady-rk','shake','rattle']);
assert.deepEqual(baseline.expected_new_method_ids,[...methodIdsAddedInBatch68]);
assert.deepEqual(transition.new_method_ids,[...methodIdsAddedInBatch68]);
assert.equal(transition.status,'EXACT_REVIEWED_BATCH68_METADATA_TRANSITIONS');
assert.equal(transition.source_base_commit,baseline.base_commit);

// Unlike a JSON stringify hash, this also retains negative-zero and exact
// nested object-key order. Strings are compared through their UTF-8 bytes.
function typed(value){
 if(value===null)return Buffer.from('z');
 if(typeof value==='boolean')return Buffer.from(value?'b1':'b0');
 if(typeof value==='number'){
  assert.ok(Number.isFinite(value));const b=Buffer.alloc(8);b.writeDoubleBE(value);
  return Buffer.concat([Buffer.from('n'),b]);
 }
 if(typeof value==='string'){
  const b=Buffer.from(value,'utf8');return Buffer.concat([Buffer.from('s'+b.length+':'),b]);
 }
 if(Array.isArray(value))return Buffer.concat([Buffer.from('a'+value.length+':'),...value.map(typed)]);
 assert.ok(value&&typeof value==='object');
 const keys=Object.keys(value);
 return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(k=>[typed(k),typed(value[k])])]);
}
function same(actual,expected,label){assert.ok(typed(actual).equals(typed(expected)),label);}
const keys=row=>Object.keys(row).sort();
const allowedAppend=new Set(['summary','limitations','depth_release','depth_additional_releases','supplemental_scope_profiles','metadata_review']);
const allowedDAE=new Set(['status','depth_previous_status','summary','assumptions','assumptions_ja','units','units_ja','boundary_conditions','boundary_conditions_ja','code_mapping_scope','code_mapping_scope_ja','limitations','next_deliverable','references','metadata_review','depth_release','depth_additional_releases','supplemental_scope_profiles']);

export function projectMethodBeforeBatch68(row){
 const before=baseline.methods[row.id];
 if(!before)return row; // Later IDs are explicitly excluded by their cohort tests.
 const change=transition.transitions[row.id];
 if(!change){same(row,before,row.id+'/no-batch68-change');return row;}
 assert.deepEqual(keys(row),change.after_all_keys,row.id+'/exact-after-key-set');
 assert.deepEqual(keys(before),change.before_all_keys,row.id+'/exact-before-key-set');
 const changed=[...new Set([...Object.keys(change.before),...Object.keys(change.after),...change.before_absent,...change.after_absent])];
 const allow=row.id==='dae'?allowedDAE:allowedAppend;
 for(const key of changed){
  assert.ok(allow.has(key),row.id+'/'+key+'/named-authorized-field');
  if(Object.hasOwn(change.before,key))same(change.before[key],before[key],row.id+'/'+key+'/exact-before');
  else assert.ok(!Object.hasOwn(before,key)&&change.before_absent.includes(key),row.id+'/'+key+'/previously-absent');
  if(Object.hasOwn(change.after,key)){
   assert.ok(Object.hasOwn(row,key),row.id+'/'+key+'/required-after');
   same(row[key],change.after[key],row.id+'/'+key+'/exact-reviewed-after');
  }else assert.ok(!Object.hasOwn(row,key)&&change.after_absent.includes(key),row.id+'/'+key+'/exact-after-absence');
 }
 // No other current value is hidden by this projection.
 for(const key of Object.keys(before))if(!changed.includes(key)){
  assert.ok(Object.hasOwn(row,key),row.id+'/'+key+'/preserved-key');
  same(row[key],before[key],row.id+'/'+key+'/preserved-current-value');
 }
 const copy={...row};
 for(const key of changed){
  if(Object.hasOwn(change.before,key))copy[key]=structuredClone(change.before[key]);
  else delete copy[key];
 }
 assert.deepEqual(keys(copy),change.before_all_keys,row.id+'/restored-key-set');
 // Restore only top-level key ordering for older JSON-byte goldens. Values
 // outside the named change remain those just verified in the current row.
 return Object.fromEntries(Object.keys(before).map(key=>[key,copy[key]]));
}
