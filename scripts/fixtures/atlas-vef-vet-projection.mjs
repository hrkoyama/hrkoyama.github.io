// Dated-test presentation metadata only: exact current extension -> cleanup8c.
// Current UI/science tests use their unprojected full inventories.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const bytes=readFileSync(new URL('./atlas-vef-vet-metadata-delta.json',import.meta.url));
assert.equal(createHash('sha256').update(bytes).digest('hex'),'9a72f9969f76ba4261b445e4c802dae33d97d3fa1893e2566ffcf8930304185c','reviewed VEF/VET metadata stage');
const frozen=JSON.parse(bytes);
assert.equal(frozen.base_commit,'8c268badb3e04a6f0cca03544561877342f5d981');
export const methodIdsAddedInVefVet=Object.freeze(frozen.new_method_ids);
export const groupIdsAddedInVefVet=Object.freeze(frozen.new_group_ids);
function typed(v){
 if(v===null)return Buffer.from('z');
 if(typeof v==='boolean')return Buffer.from(v?'b1':'b0');
 if(typeof v==='number'){assert.ok(Number.isFinite(v));const b=Buffer.alloc(8);b.writeDoubleBE(v);return Buffer.concat([Buffer.from('n'),b]);}
 if(typeof v==='string'){const b=Buffer.from(v);return Buffer.concat([Buffer.from('s'+b.length+':'),b]);}
 if(Array.isArray(v))return Buffer.concat([Buffer.from('a'+v.length+':'),...v.map(typed)]);
 assert.ok(v&&typeof v==='object');const keys=Object.keys(v);return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(k=>[typed(k),typed(v[k])])]);
}
const hash=v=>createHash('sha256').update(typed(v)).digest('hex');
export function projectMethodBeforeVefVet(row){
 assert.ok(row&&typeof row.id==='string','method identity');
 const expected=frozen.baseline_method_hashes[row.id]||frozen.new_method_rows[row.id]?.sha256;
 assert.ok(expected,row.id+'/known cleanup or exact VEF/VET method');
 assert.equal(hash(row),expected,row.id+'/complete exact metadata');
 return structuredClone(row); // New IDs are explicitly excluded only by dated callers.
}
export function projectCatalogBeforeVefVet(path,value){
 path=String(path).replace(/^https:\/\/hrkoyama\.github\.io\//,'').replace(/^\//,'');
 const record=frozen.catalogs[path];if(!record)return value;
 const actual=hash(value);if(actual===record.before)return structuredClone(value);
 assert.equal(actual,record.after,path+'/exact VEF/VET extension');
 const copy=structuredClone(value);
 for(const operation of [...record.operations].reverse()){
  let parent=copy;for(const key of operation.parts.slice(0,-1))parent=parent[key];
  const key=operation.parts.at(-1);assert.ok(Object.hasOwn(parent,key));
  if(operation.kind==='added-key'){
   assert.equal(hash(parent[key]),hash(operation.after));delete parent[key];
  }else if(operation.kind==='append'){
   const rows=parent[key];assert.ok(Array.isArray(rows));
   assert.equal(rows.length,operation.before_length+operation.appended.length);
   assert.equal(hash(rows.slice(operation.before_length)),hash(operation.appended));
   parent[key]=rows.slice(0,operation.before_length);
  }else{
   assert.equal(operation.kind,'value');assert.equal(hash(parent[key]),hash(operation.after));
   parent[key]=structuredClone(operation.before);
  }
 }
 assert.equal(hash(copy),record.before,path+'/complete exact cleanup8c restoration');
 return copy;
}
