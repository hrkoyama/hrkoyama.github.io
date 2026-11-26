import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {projectCatalogBeforeVefVet,projectMethodBeforeVefVet,methodIdsAddedInVefVet} from './fixtures/atlas-vef-vet-projection.mjs';
const root=new URL('../',import.meta.url),read=path=>readFileSync(new URL(path,root));
const frozen=JSON.parse(read('scripts/fixtures/atlas-vef-vet-metadata-delta.json'));
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
test('the VEF/VET metadata stage preserves every cleanup catalog and rejects unknown additions',()=>{
 for(const [path,record]of Object.entries(frozen.catalogs)){
  const raw=read(path);assert.equal(sha(raw),record.source_after_sha256,path+'/current source bytes');
  const current=JSON.parse(raw),copy=structuredClone(current),old=projectCatalogBeforeVefVet(path,current);
  assert.deepEqual(current,copy);assert.deepEqual(projectCatalogBeforeVefVet(path,old),old);
  const changed=structuredClone(current);changed.unknown_metadata=true;
  assert.throws(()=>projectCatalogBeforeVefVet(path,changed),path+'/unknown field');
 }
});
test('the two VEF/VET methods are a separate exact cohort and do not change final23 membership',()=>{
 assert.deepEqual([...methodIdsAddedInVefVet],['variable-eddington-factor','variable-eddington-tensor']);
 const methods=JSON.parse(read('catalog/atlas-methods.json')).methods;
 assert.equal(methods.length,171);
 for(const row of methods)assert.deepEqual(projectMethodBeforeVefVet(row),row);
 for(const id of methodIdsAddedInVefVet){
  const row=methods.find(r=>r.id===id),copy=structuredClone(row);copy.name.en+=' extra';
  assert.throws(()=>projectMethodBeforeVefVet(copy));
 }
 assert.throws(()=>projectMethodBeforeVefVet({id:'unreviewed-third-method'}));
 const previous=JSON.parse(read('scripts/fixtures/atlas-final23-metadata-delta.json'));
 assert.deepEqual(previous.new_method_ids,['gillespie-ssa','semi-lagrangian']);
});
