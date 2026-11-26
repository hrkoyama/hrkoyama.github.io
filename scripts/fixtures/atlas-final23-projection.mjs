// Use only for dated historical tests. Current UI/registry tests retain the full
// cohort. Exact source metadata is checked before its reviewed inverse is used;
// no scientific packet, old fixture, result or tolerance is projected.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const bytes=readFileSync(new URL('./atlas-final23-metadata-delta.json',import.meta.url));
assert.equal(createHash('sha256').update(bytes).digest('hex'),'da065045339f0266faabda492a0a32a9728626b1c49bee0fb634c9e71be33dff','frozen final23 metadata inverse');
const frozen=JSON.parse(bytes);
assert.equal(frozen.base_commit,'812f0e1a295f1491d12c50db9df5b6147bb41744');
export const methodIdsAddedInFinal23=Object.freeze(frozen.new_method_ids);
export const methodIdsPromotedInFinal23=Object.freeze(frozen.promoted_method_ids);
export const groupIdsAddedInFinal23=Object.freeze(frozen.new_group_ids);
function typed(v){
 if(v===null)return Buffer.from('z');
 if(typeof v==='boolean')return Buffer.from(v?'b1':'b0');
 if(typeof v==='number'){assert.ok(Number.isFinite(v));const b=Buffer.alloc(8);b.writeDoubleBE(v);return Buffer.concat([Buffer.from('n'),b]);}
 if(typeof v==='string'){const b=Buffer.from(v);return Buffer.concat([Buffer.from('s'+b.length+':'),b]);}
 if(Array.isArray(v))return Buffer.concat([Buffer.from('a'+v.length+':'),...v.map(typed)]);
 assert.ok(v&&typeof v==='object');const keys=Object.keys(v);return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(k=>[typed(k),typed(v[k])])]);
}
const hash=v=>createHash('sha256').update(typed(v)).digest('hex');
function inverse(value,delta,label){
 if(!delta)return structuredClone(value);
 const actual=hash(value);
 if(actual===delta.before)return structuredClone(value);
 assert.equal(actual,delta.after,label+'/exact-reviewed-current-metadata');
 let result;
 if(delta.kind==='value')result=structuredClone(delta.value);
 else if(delta.kind==='object')result=Object.fromEntries(delta.keys.map(key=>[key,Object.hasOwn(delta.restore,key)?structuredClone(delta.restore[key]):Object.hasOwn(delta.changes,key)?inverse(value[key],delta.changes[key],label+'/'+key):structuredClone(value[key])]));
 else {
  assert.equal(delta.kind,'rows');
  const rows=new Map(value.map(row=>[row.id,row]));assert.equal(rows.size,value.length,label+'/unique-ids');
  result=delta.ids.map(id=>Object.hasOwn(delta.changes,id)?inverse(rows.get(id),delta.changes[id],label+'/'+id):structuredClone(rows.get(id)));
 }
 assert.equal(hash(result),delta.before,label+'/complete-exact-812-restoration');return result;
}
export function projectMethodBeforeFinal23(row){
 const record=frozen.methods[row?.id];assert.ok(record,row?.id+'/known-final23-or-baseline-method');
 const actual=hash(row);
 if(actual===record.before)return structuredClone(row);
 assert.equal(actual,record.after,row.id+'/exact-reviewed-current-method');
 return record.delta?inverse(row,record.delta,row.id):structuredClone(row);
}
export function projectCatalogBeforeFinal23(path,value){
 path=String(path).replace(/^https:\/\/hrkoyama\.github\.io\//,'').replace(/^\//,'');
 const record=frozen.catalogs[path];if(!record)return value;
 const actual=hash(value);
 if(actual===record.before)return structuredClone(value);
 assert.equal(actual,record.after,path+'/exact-reviewed-current-catalog');
 return inverse(value,record.delta,path);
}
