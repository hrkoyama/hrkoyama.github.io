export {methodIdsAddedInFinal23,methodIdsPromotedInFinal23,groupIdsAddedInFinal23,projectMethodBeforeFinal23,projectCatalogBeforeFinal23} from './atlas-final23-projection.mjs';
import {projectMethodBeforeBatch68 as projectMethodBeforeBatch68Only,methodIdsAddedInBatch68} from './atlas-batch68-method-projection.mjs';
import {projectMethodBeforeBatch78,methodIdsAddedInBatch78,methodIdsPromotedInBatch78} from './atlas-batch78-projection.mjs';
export {methodIdsAddedInBatch68,methodIdsAddedInBatch78,methodIdsPromotedInBatch78};
export function projectMethodBeforeBatch68(row){return projectMethodBeforeBatch68Only(projectMethodBeforeBatch78(row));}
// Current registration expectations come from canonical inputs. Immutable
// release counts, hashes and numerical golden values stay in their own tests.
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
const root=new URL('../../',import.meta.url),read=path=>JSON.parse(readFileSync(new URL(path,root)));
const registration=read('catalog/atlas-registration.json');
const methods=read(registration.methods_catalog).methods;
const supplements=read(registration.supplements_catalog);
export const methodIds=methods.map(row=>row.id);
export const methodCount=methodIds.length;
export const methodStatusCounts=Object.fromEntries(['educational-example','reading-only','planned'].map(status=>[status,methods.filter(row=>row.status===status).length]));
export const supplementGroupIds=supplements.groups.map(row=>row.id);
export const supplementCaseIds=supplements.groups.flatMap(row=>{
 const value=read('code/validated-examples/'+(row.edition||supplements.edition)+'/'+row.id+'/cases.json');return (Array.isArray(value)?value:value.cases).map(x=>x.id);
});

// General inventory sizes are canonical. Historical preservation tests below
// exclude later additions while retaining every original hash/golden value.
export const supplementCaseCount=supplementCaseIds.length;
export const supplementGroupCount=supplementGroupIds.length;
const problemRows=read('catalog/atlas-test-problems.json').problems;
export const problemCount=problemRows.length;
export const equationCount=read('catalog/atlas-equations.json').equations.length;
const mapped=Object.values(supplements.case_problem_ids).filter(x=>x!==null);
export const supplementalMappedCaseCount=mapped.length;
export const supplementalProblemCount=new Set(mapped).size;
export const runnableProblemCount=new Set([...read('catalog/atlas-execution-examples.json').examples.map(x=>x.problem_id),...mapped]).size;
const batch37=read('scripts/fixtures/atlas-batch38-47-baseline.json');
const oldGroups=new Set(batch37.release_registry.releases.map(x=>x.group));
const oldProblems=new Set(batch37.gallery_items.map(x=>x.id));
export const groupsAddedAfterBatch37=supplementGroupIds.filter(x=>!oldGroups.has(x));
const oldCases=new Set(batch37.release_registry.releases.flatMap(x=>x.case_ids));
export const examplesAddedAfterBatch37=[...new Set([...problemRows.map(x=>x.id).filter(x=>!oldProblems.has(x)),...supplementCaseIds.filter(x=>!oldCases.has(x))])];

export const equationsAddedAfterBatch37=read('catalog/atlas-equations.json').equations.map(x=>x.id).filter(x=>!Object.hasOwn(batch37.equation_formulas,x));

// Explicit metadata projection only for historical goldens. Current science
// fields remain in each golden and the batch38 preservation test below.
export function projectMethodBeforeBatch38(row){
 const previous=batch37.method_append_fields_before_batch38[row.id];
 if(!previous)return row;
 const copy={...row};
 for(const key of ['summary','limitations','depth_release','depth_additional_releases','supplemental_scope_profiles','metadata_review','depth_scope']){
  if(Object.hasOwn(previous,key))copy[key]=previous[key];else delete copy[key];
 }
 return copy;
}

export const problemGroupCounts=Object.fromEntries([...new Set(problemRows.map(x=>x.group))].map(g=>[g,problemRows.filter(x=>x.group===g).length]));

// Batch48 historical projections are deliberately narrow: old immutable files
// remain hash-checked, and the current MHD edition has separate equivalence
// and real-ZIP tests. Never project other current science or new candidates.
const batch47=read('scripts/fixtures/atlas-batch48-57-baseline.json');
const before48Groups=new Set(batch47.release_order);
export const groupsAddedAfterBatch47=supplementGroupIds.filter(id=>!before48Groups.has(id));
export const problemsAddedAfterBatch47=problemRows.map(row=>row.id).filter(id=>!Object.hasOwn(batch47.gallery_records_sha256,id));
export const equationsAddedAfterBatch47=read('catalog/atlas-equations.json').equations.map(row=>row.id).filter(id=>!Object.hasOwn(batch47.equations,id));
export function projectPointerBeforeBatch48(row){
 const exception=batch47.current_edition_exception;
 if(row?.group===exception.group&&row.edition===exception.new_edition){
  if(!row.case_ids.every(id=>exception.case_ids.includes(id)))throw new Error('Unexpected MHD case association');
  return {...row,edition:exception.old_edition};
 }
 return row;
}
export function projectReleaseBeforeBatch48(row){
 const exception=batch47.current_edition_exception;
 if(row?.group===exception.group&&row.edition===exception.new_edition){
  const old=batch47.releases.find(value=>value.release.group===exception.group).release;
  if(row.tests!==old.tests||JSON.stringify(row.case_ids)!==JSON.stringify(old.case_ids))throw new Error('Changed MHD science inventory');
  return old;
 }
 return row;
}

// Invert only the exact reviewed batch58–67 append for the two older whole-record
// goldens. All prior scientific fields, UTF-8 prefixes, reference/release prefixes
// and review values are checked first; neither historical golden is replaced.
const batch57Bytes=readFileSync(new URL('scripts/fixtures/atlas-batch58-67-baseline.json',root));
assert.equal(createHash('sha256').update(batch57Bytes).digest('hex'),'815c6672fdd93c526e510c5620c765453ca5b1a82af44afbbab261b6bddc7327','frozen batch57 method baseline');
const batch57=JSON.parse(batch57Bytes);
export const methodIdsAddedInBatch58=Object.freeze(['dogleg-trust-region']);
assert.deepEqual(batch57.expected_new_method_ids,[...methodIdsAddedInBatch58]);
const batch58AppendSHA={"centered-difference":"90703248b950640fbb685e52114f4f49224784d39515dc00733229f66778c804","backward-euler":"02142648a15f6e52da5ec250bcbdd431fe6e9941035f63173cb5e56601d5bb27","thomas":"47101d6ed9c241854910565d67388291a3b32bfe93abaf7af8ab6e0c88b48052","gmres":"90703248b950640fbb685e52114f4f49224784d39515dc00733229f66778c804","newton":"c62457826427d25eb1e46296391bcaa81027e64f14c02446dd6a92ba8063909a","optimization":"06136160d5ed622239df6cc4c2377052988d6c453c10883fbff2a79897681dce","adjoint":"d7043312c46735aae9dfef7ae5e2a149a00eb1d85aed3f35e6df286d183a0e88","automatic-differentiation":"818e13c73b0ed9bad475a7514807397ed08b1ecbdf2953d82dfe225b74136876"};
const batch58PriorOptionalKeys={"centered-difference":["references","depth_additional_releases","supplemental_scope_profiles"],"backward-euler":["references","supplemental_scope_profiles"],"thomas":["references","supplemental_scope_profiles"],"gmres":["references","depth_additional_releases","supplemental_scope_profiles"],"newton":["references","supplemental_scope_profiles"],"optimization":["references"],"adjoint":["references"],"automatic-differentiation":["references","supplemental_scope_profiles"]};
const batch58PriorReviewExtras={"centered-difference":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"upwind":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"rusanov":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"backward-euler":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"heun":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"implicit-midpoint":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"leapfrog":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"verlet":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"thomas":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"cg":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"multigrid":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"gmres":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"newton":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"d2q9-bgk":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"cic":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"barnes-hut":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"fmm":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"ewald":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"slab-ewald":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"fdtd":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"pic":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"amg":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"eigensolvers":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"monte-carlo":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"mcmc":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"sde":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"radiation-transport":{"keys":["supplemental_review"],"sha256":"adbbf10368ddebd7fc3b86fbfd4567af953aa6171f475c7de43213294ed31765"},"dsmc":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"automatic-differentiation":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"q1-fem":{"keys":["supplemental_review"],"sha256":"75e623f56a6c74eb29c77f66b63e66e6d9a4027b0b329abcf7146172bb577ec4"},"lu-partial-pivoting":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"cholesky":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"minres":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"lobpcg":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"pseudo-arclength-continuation":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"},"jacobian-free-newton-krylov":{"keys":["supplemental_review"],"sha256":"536e5914d0083a0537291615747ca05ba6d64bac7ec4085f2315827b55eff56f"}};
const batch58ReviewReplacements={"backward-euler":{"supplemental_review":{"before":{"on":"2026-11-24","level":"Frozen fixed-input source,independent review,actual pytest/main and independently extracted ZIP; see each new release for exact reference independence and failed-attempt history."},"after_sha256":"dc360ac702a489b4988512bf1c4ec10c330556cf095f04c8baf5ea29c696aadc"}}};
function batch58Typed(value){
 if(value===null)return Buffer.from('z');
 if(typeof value==='boolean')return Buffer.from(value?'b1':'b0');
 if(typeof value==='number'){
  assert.ok(Number.isFinite(value));const n=Buffer.alloc(8);n.writeDoubleBE(value);
  return Buffer.from('n'+n.toString('hex'));
 }
 if(typeof value==='string'){
  const text=Buffer.from(value);return Buffer.concat([Buffer.from('s'+text.length+':'),text]);
 }
 if(Array.isArray(value))return Buffer.concat([Buffer.from('a'+value.length+':'),...value.map(batch58Typed)]);
 assert.ok(value&&typeof value==='object','finite metadata value');
 const keys=Object.keys(value).sort((a,b)=>Buffer.compare(Buffer.from(a),Buffer.from(b)));
 return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(key=>[batch58Typed(key),batch58Typed(value[key])])]);
}
const batch58Hash=value=>createHash('sha256').update(batch58Typed(value)).digest('hex');
const batch58Pick=(row,keys)=>Object.fromEntries(keys.map(key=>[key,row[key]]));
export function projectMethodBeforeBatch58(row){
 row=projectMethodBeforeBatch68(row);
 const before=batch57.methods[row.id];
 if(!before)return row;
 assert.equal(row.status,before.status,row.id+'/old-status');
 assert.equal(batch58Hash(batch58Pick(row,before.stable_keys)),before.stable_sha256,row.id+'/old-scientific-fields');
 assert.equal(batch58Hash(batch58Pick(row.metadata_review||{},before.review_keys)),before.review_sha256,row.id+'/old-review');
 const variable=['summary','limitations','references','depth_release','depth_additional_releases','supplemental_scope_profiles','metadata_review'];
 assert.deepEqual(Object.keys(row).filter(key=>!before.stable_keys.includes(key)&&!variable.includes(key)),[],row.id+'/no-unreviewed-field');
 const copy={...row},added={};
 for(const field of ['summary','limitations']){
  assert.deepEqual(Object.keys(row[field]).sort(),Object.keys(before.text_prefixes[field]).sort(),row.id+'/'+field+'/languages');
  copy[field]={};added[field]={};
  for(const [language,prefix]of Object.entries(before.text_prefixes[field])){
   const bytes=Buffer.from(row[field][language]),head=bytes.subarray(0,prefix.utf8_bytes);
   assert.equal(createHash('sha256').update(head).digest('hex'),prefix.sha256,row.id+'/'+field+'/'+language+'/old-prefix');
   copy[field][language]=head.toString('utf8');added[field][language]=bytes.subarray(prefix.utf8_bytes).toString('utf8');
   assert.ok(Buffer.from(copy[field][language]).equals(head),row.id+'/complete-UTF8-prefix');
  }
 }
 for(const [field,prefix]of [['references',before.reference_prefix_sha256],['depth_additional_releases',before.additional_release_prefix_sha256],['supplemental_scope_profiles',before.scope_profile_prefix_sha256]]){
  const values=row[field]||[];assert.ok(values.length>=prefix.length,row.id+'/'+field+'/old-length');
  assert.deepEqual(values.slice(0,prefix.length).map(batch58Hash),prefix,row.id+'/'+field+'/old-prefix');
  added[field]=values.slice(prefix.length);
  const priorKeys=batch58PriorOptionalKeys[row.id];
  if(priorKeys){if(priorKeys.includes(field))copy[field]=values.slice(0,prefix.length);else delete copy[field];}
 }
 const oldExtra=batch58PriorReviewExtras[row.id];
 const oldReviewKeys=[...before.review_keys,...(oldExtra?.keys||[])];
 added.metadata_review=Object.fromEntries(Object.entries(row.metadata_review||{}).filter(([key])=>!oldReviewKeys.includes(key)));
 copy.metadata_review=batch58Pick(row.metadata_review,oldReviewKeys);
 const replacements=batch58ReviewReplacements[row.id];
 if(replacements){
  added.metadata_review.$replaced={};
  for(const [key,replacement]of Object.entries(replacements)){
   assert.equal(batch58Hash(row.metadata_review[key]),replacement.after_sha256,row.id+'/'+key+'/exact-reviewed-replacement');
   added.metadata_review.$replaced[key]=row.metadata_review[key];
   copy.metadata_review[key]=replacement.before;
  }
 }
 if(oldExtra)assert.equal(batch58Hash(batch58Pick(copy.metadata_review,oldExtra.keys)),oldExtra.sha256,row.id+'/old-supplemental-review');
 added.depth_release=before.primary_release?null:(row.depth_release||null);
 if(before.primary_release)assert.deepEqual(row.depth_release,before.primary_release,row.id+'/old-primary-release');
 else delete copy.depth_release;
 if(Object.hasOwn(batch58AppendSHA,row.id)){
  assert.equal(batch58Hash(added),batch58AppendSHA[row.id],row.id+'/exact-reviewed-batch58-append');
  return copy;
 }
 assert.deepEqual(added,{summary:{ja:'',en:''},limitations:{ja:'',en:''},references:[],depth_additional_releases:[],supplemental_scope_profiles:[],metadata_review:{},depth_release:null},row.id+'/no-batch58-change');
 return row;
}
