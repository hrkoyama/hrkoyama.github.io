// Frozen canonical cohort checks; no scientific calculation is executed here.
// Metadata and byte checks only: no numerical imports, archive extraction,
// reference regeneration, training, image rendering or network access.
import {projectCatalogBeforeFinal23} from './fixtures/atlas-final23-projection.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {createReadStream,readFileSync,statSync} from 'node:fs';
const root=new URL('../',import.meta.url);
const local=p=>String(p).replace(/^https:\/\/hrkoyama\.github\.io\//,'').replace(/^\//,'');
const bytes=p=>readFileSync(new URL(local(p),root));
// This dated batch keeps its exact old cohort; the strict final23 inverse validates later changes first.
const json=p=>projectCatalogBeforeFinal23(local(p),JSON.parse(bytes(p)));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const sorted=xs=>[...xs].sort();
const baselinePath='scripts/fixtures/atlas-batch78-87-baseline.json';
assert.equal(sha(baselinePath),'af74ae58975c6b978bec5a425927ce05c0d894ed5c325443dc452ee7ec6df653');
const baseline=json(baselinePath),freeze=json('scripts/fixtures/atlas-batch78-87-freeze.json');
assert.equal(sha('scripts/fixtures/atlas-batch78-87-freeze.json'),'b5ea04031e443f0ec3c2e20e610034bcbbbc326f5884350d454df2fbad85b7ad');
// An accidentally installed unfilled template fails closed, never skips tests.
assert.equal(freeze.status,'ROOT_REVIEWED_ACTUAL_CANONICAL_FREEZE');
assert.equal(freeze.source_base_commit,baseline.base_commit);
assert.equal(freeze.baseline_sha256,sha(baselinePath));
const EXPECTED={
 'quadrature-controls':['quadpack-domain-selection','gk15-double-exponential','tensor-smolyak-dimensions'],
 'approximation-controls':['runge-barycentric-clenshaw','spline-shape-controls','haar-mallat-boundary-threshold'],
 'small-models':['pinn-poisson','fno-periodic-heat','enzyme-qssa','lotka-volterra','seir-linearization'],
};
const NEW_METHODS=['gauss-kronrod','tanh-sinh','smolyak-sparse-grid','pchip'];
const PROMOTIONS=['splines','chebyshev','wavelets','pinn-operators'];
const ids=Object.values(EXPECTED).flat(),groups=Object.keys(EXPECTED);
const registry=()=>json('numerical-methods-atlas/validation/releases.json');
const releaseBase=r=>`code/validated-examples/${r.edition}/${r.group}/`;
async function streamSHA(path){const h=createHash('sha256');for await(const b of createReadStream(new URL(local(path),root)))h.update(b);return h.digest('hex');}
function typed(value){
 if(value===null)return Buffer.from('z');
 if(typeof value==='boolean')return Buffer.from(value?'b1':'b0');
 if(typeof value==='number'){assert.ok(Number.isFinite(value));const b=Buffer.alloc(8);b.writeDoubleBE(value);return Buffer.concat([Buffer.from('n'),b]);}
 if(typeof value==='string'){const b=Buffer.from(value,'utf8');return Buffer.concat([Buffer.from('s'+b.length+':'),b]);}
 if(Array.isArray(value))return Buffer.concat([Buffer.from('a'+value.length+':'),...value.map(typed)]);
 assert.ok(value&&typeof value==='object');const keys=Object.keys(value);
 return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(k=>[typed(k),typed(value[k])])]);
}
const fingerprint=v=>createHash('sha256').update(typed(v)).digest('hex');
const appendFields=['summary','limitations','references','metadata_review','depth_release','depth_additional_releases','supplemental_scope_profiles','depth_scope'];
const promotionFields=[...appendFields,'status','depth_previous_status','next_deliverable','assumptions','assumptions_ja','units','units_ja','boundary_conditions','boundary_conditions_ja','code_mapping_scope','code_mapping_scope_ja'];
function inverse(row,record,transition,allow){
 assert.ok(row&&record);if(!transition){assert.equal(fingerprint(row),record.typed_sha256,row.id+'/unchanged');return row;}
 assert.deepEqual(sorted(Object.keys(row)),transition.after_keys);
 assert.deepEqual(sorted(record.keys),transition.before_keys);
 const changed=sorted(new Set([...Object.keys(transition.before),...Object.keys(transition.after),...transition.before_absent,...transition.after_absent]));
 for(const key of changed){
  assert.ok(allow.includes(key),row.id+'/'+key+'/authorized-field');
  if(Object.hasOwn(transition.after,key)){assert.ok(Object.hasOwn(row,key));assert.ok(typed(row[key]).equals(typed(transition.after[key])));}
  else assert.ok(!Object.hasOwn(row,key)&&transition.after_absent.includes(key));
  assert.notEqual(Object.hasOwn(transition.after,key),transition.after_absent.includes(key));
  assert.notEqual(Object.hasOwn(transition.before,key),transition.before_absent.includes(key));
 }
 const copy={...row};for(const key of changed){if(Object.hasOwn(transition.before,key))copy[key]=structuredClone(transition.before[key]);else delete copy[key];}
 assert.deepEqual(sorted(Object.keys(copy)),transition.before_keys);
 const ordered=Object.fromEntries(record.keys.map(key=>[key,copy[key]]));
 assert.equal(fingerprint(ordered),record.typed_sha256,row.id+'/exact-old-record');return ordered;
}
function finite(v){if(typeof v==='number')assert.ok(Number.isFinite(v));else if(Array.isArray(v))v.forEach(finite);else if(v&&typeof v==='object')Object.values(v).forEach(finite);}
function studyOutcomes(c,acceptance){
 if(Object.hasOwn(freeze.original_study_goals,c.id)){
  const fixed=freeze.original_study_goals[c.id];
  for(const key of ['original_target_results','original_target_summary','original_study_goal_measurements'])assert.deepEqual(c[key],fixed[key],c.id+'/'+key+'/actual-canonical');
  const values=Object.values(c.original_target_results);assert.ok(values.every(v=>typeof v==='boolean'));
  assert.deepEqual(c.original_target_summary,{met:values.filter(Boolean).length,total:values.length,all_met:values.every(Boolean),acceptance_sha256:acceptance});
  for(const [key,goal] of Object.entries(c.original_study_goal_measurements)){
   assert.equal(goal.met,c.original_target_results[key]);
   assert.ok(['<=','=='].includes(goal.comparison));
   assert.equal(goal.met,goal.comparison==='<='?goal.measured<=goal.limit:goal.measured===goal.limit);
  }
 }
 if(Object.hasOwn(freeze.quadrature_row_accuracy_studies,c.id)){
  const fixed=freeze.quadrature_row_accuracy_studies[c.id],map=Object.fromEntries(c.records.map(r=>[r.row_id,r.accuracy_goal_met]));
  assert.equal(Object.keys(map).length,c.records.length);assert.deepEqual(map,fixed.accuracy_goal_met_by_row_id);
  const values=Object.values(map);assert.ok(values.every(v=>v===true||v===false||v===null));
  assert.deepEqual({met:values.filter(v=>v===true).length,unmet:values.filter(v=>v===false).length,not_computable:values.filter(v=>v===null).length,total:values.length},fixed.summary);
 }
}
function png(path,hash){const b=bytes(path);assert.equal(sha(path),hash);assert.ok(b.subarray(0,8).equals(Buffer.from('89504e470d0a1a0a','hex')));assert.equal(b.toString('ascii',12,16),'IHDR');assert.ok(b.readUInt32BE(16)>0&&b.readUInt32BE(20)>0);}
function csv(text){
 const out=[];let row=[],cell='',quoted=false;
 for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quoted&&text[i+1]==='"'){cell+='"';i++;}else quoted=!quoted;}else if(!quoted&&c===','){row.push(cell);cell='';}else if(!quoted&&(c==='\n'||c==='\r')){if(c==='\r'&&text[i+1]==='\n')i++;row.push(cell);out.push(row);row=[];cell='';}else cell+=c;}
 assert.equal(quoted,false);if(cell||row.length){row.push(cell);out.push(row);}return out;
}

test('batch78 baseline and dated metadata inverse preserve all old cohorts and scientific fields',async()=>{
 assert.equal(baseline.base_commit,'35e34ae130d47cc43445765b88e99c0c556c38bb');
 assert.deepEqual(baseline.baseline_counts,{groups:60,cases:127,pytest:1572,methods:163,problems:149,models:80,gallery_items:149,preview_records:149});
 assert.deepEqual(baseline.expected_new_groups,EXPECTED);assert.deepEqual(freeze.expected_new_groups,EXPECTED);
 assert.deepEqual(baseline.expected_new_method_ids,NEW_METHODS);assert.deepEqual(baseline.expected_promotions,PROMOTIONS);
 assert.deepEqual(registry().releases.filter(r=>baseline.release_order.includes(r.group)),baseline.releases);
 for(const [path,hash] of Object.entries(baseline.immutable_anchor_files))assert.equal(await streamSHA(path),hash,path);
 const methods=json('catalog/atlas-methods.json').methods;
 assert.deepEqual(sorted(methods.filter(m=>!Object.hasOwn(baseline.method_records,m.id)).map(m=>m.id)),sorted(NEW_METHODS));
 for(const [id,before] of Object.entries(baseline.method_records)){
  const row=methods.find(m=>m.id===id);inverse(row,before,freeze.method_transitions[id],PROMOTIONS.includes(id)?promotionFields:appendFields);
  assert.equal(row.status,PROMOTIONS.includes(id)?'educational-example':before.status,id+'/status');
 }
 assert.ok(Object.keys(freeze.method_transitions).every(id=>Object.hasOwn(baseline.method_records,id)));
 const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const before of baseline.preview_manifest_items){assert.deepEqual(previews.find(x=>x.id===before.id),before);assert.equal(await streamSHA(before.image),before.image_sha256);}
 for(const [file,records,changes,allow] of [
  ['catalog/atlas-test-problems.json',baseline.problem_records,freeze.problem_transitions,['method_ids','equation_ids','supplemental_examples','references']],
  ['catalog/atlas-gallery.json',baseline.gallery_records,freeze.gallery_transitions,['supplemental_examples','supplemental_execution_entries']],
 ]){const data=json(file),rows=data.problems||data.items;for(const [id,record] of Object.entries(records))inverse(rows.find(x=>x.id===id),record,changes[id],allow);assert.ok(Object.keys(changes).every(id=>Object.hasOwn(records,id)));}
});

test('three exact groups expose actual canonical proofs, eleven cases and finite saved CSV records',async()=>{
 const r=registry();assert.equal(r.releases.length,63);assert.equal(r.case_count,138);
 assert.deepEqual(sorted(r.releases.filter(x=>!baseline.release_order.includes(x.group)).map(x=>x.group)),sorted(groups));
 assert.deepEqual(sorted(Object.keys(freeze.canonical_packets)),sorted(groups));
 let actualNewTests=0;
 for(const [group,caseIDs] of Object.entries(EXPECTED)){
  const release=r.releases.find(x=>x.group===group),fixed=freeze.canonical_packets[group];assert.ok(release&&fixed);
  const base=releaseBase(release),v=json(base+'verification.json'),manifest=json(base+'source-manifest.json'),result=json(base+'results/result.json');
  assert.deepEqual(sorted(release.case_ids),sorted(caseIDs));assert.equal(release.base,'https://hrkoyama.github.io/'+base);
  assert.equal(release.edition,fixed.edition);assert.equal(release.tests,fixed.tests);actualNewTests+=release.tests;
  for(const key of ['archive_sha256','manifest_sha256','verification_sha256'])assert.equal(release[key],fixed[key]);
  assert.equal(release.archive,fixed.archive_file);assert.equal(await streamSHA(base+release.archive),release.archive_sha256);assert.equal(statSync(new URL(base+release.archive,root)).size,fixed.archive_bytes);
  assert.equal(sha(base+'source-manifest.json'),release.manifest_sha256);assert.equal(sha(base+'verification.json'),release.verification_sha256);
  assert.equal(v.passed,true);assert.equal(v.all_cases_rerun,true);assert.equal(v.tests,release.tests);assert.equal(v.passed_tests,release.tests);for(const key of ['returncode','failures','errors','skipped'])assert.equal(v[key],0);
  assert.equal(v.source_manifest_sha256,release.manifest_sha256);assert.equal(v.archive.sha256,release.archive_sha256);
  assert.deepEqual(Object.fromEntries(['numpy','scipy','pytest'].map(k=>[k,v.environment[k]])),{numpy:'2.0.2',scipy:'1.14.1',pytest:'8.3.5'});
  assert.equal(manifest.group,group);assert.equal(manifest.version,release.edition);assert.deepEqual(sorted(manifest.case_ids),sorted(caseIDs));
  for(const [name,hash] of Object.entries(manifest.files))assert.equal(await streamSHA(base+name),hash,group+'/'+name);
  assert.equal(result.passed,true);assert.equal(result.termination,'completed_fixed_protocol');assert.equal(result.input_sha256,sha(base+'inputs.json'));assert.equal(result.input_sha256,fixed.input_sha256);finite(result);
  assert.deepEqual(sorted(result.cases.map(c=>c.id)),sorted(caseIDs));assert.deepEqual(sorted(Object.keys(result.checks)),sorted(caseIDs));assert.ok(Object.values(result.checks).every(v=>v===true));
  for(const c of result.cases){assert.equal(c.passed,true);assert.ok(Object.keys(c.metrics).length);assert.ok(c.records.length);assert.equal(c.records.length,fixed.case_records[c.id]);assert.equal(Object.keys(c.checks).length,freeze.new_check_counts[c.id]);assert.ok(Object.values(c.checks).every(v=>v===true));studyOutcomes(c,sha(base+'acceptance.json'));}
  const names=Object.keys(manifest.files).filter(n=>/^results\/[^/]+\.csv$/.test(n));assert.ok(names.length);
  for(const name of names){const rows=csv(bytes(base+name).toString());assert.ok(rows.length>1);assert.equal(new Set(rows[0]).size,rows[0].length);for(const row of rows.slice(1)){assert.equal(row.length,rows[0].length);assert.ok(row.some(v=>v.trim()!==''&&Number.isFinite(Number(v))));assert.ok(row.every(v=>!/^[+-]?(nan|inf|infinity)$/i.test(v.trim())));}}
 }
 assert.equal(actualNewTests,freeze.new_pytest_total);assert.equal(r.releases.reduce((n,x)=>n+x.tests,0),1572+actualNewTests);
});

test('all eleven cases bind equations, reference inputs, scoped methods, own figures and readable routes',()=>{
 const exp=json('catalog/atlas-depth-expansion.json'),links=json('catalog/atlas-problem-links.json').problems,refs=json('catalog/atlas-reference-supplements.json').cases;
 const methods=json('catalog/atlas-methods.json').methods,models=json('catalog/atlas-equations.json').equations,gallery=json('numerical-methods-atlas/gallery/index.json').items,chapters=json('catalog/atlas-chapter-links.json').chapters;
 assert.deepEqual(sorted(Object.keys(freeze.case_problem_ids)),sorted(ids));assert.deepEqual(sorted(Object.keys(freeze.case_models)),sorted(ids));
 for(const [id,pid] of Object.entries(baseline.case_problem_ids))assert.equal(exp.case_problem_ids[id],pid,id+'/old-physical-alias');
 for(const [id,before] of Object.entries(baseline.case_equations))assert.deepEqual(exp.case_equations[id],before,id+'/old-model-map');
 for(const [group,caseIDs] of Object.entries(EXPECTED)){
  const release=registry().releases.find(x=>x.group===group),base=releaseBase(release),metadata=json(base+'cases.json'),manifest=json(base+'source-manifest.json'),saved=json(base+'results/result.json');
  for(const id of caseIDs){
   const c=(Array.isArray(metadata)?metadata:metadata.cases).find(x=>x.id===id),pid=freeze.case_problem_ids[id],modelIDs=freeze.case_models[id],ref=refs.find(x=>x.id===id),link=links.find(x=>x.id===pid);
   assert.ok(c&&pid&&modelIDs.length&&ref&&link);assert.equal(exp.case_problem_ids[id],pid);assert.deepEqual(exp.case_equations[id].ids,modelIDs);assert.equal(ref.model,modelIDs[0]);
   for(const field of ['title','summary','assumptions','algorithm','validation','limits'])for(const lang of ['ja','en'])assert.ok(c[field][lang].trim());
   for(const method of c.method_ids){assert.ok(link.method_ids.includes(method));const m=methods.find(x=>x.id===method);assert.ok(m);assert.ok([m.depth_release,...(m.depth_additional_releases||[])].filter(Boolean).some(x=>x.group===group&&x.edition===release.edition&&x.case_ids.includes(id)),id+'/'+method+'/own-run-scope');}
   for(const model of modelIDs){assert.ok(link.equation_ids.includes(model));assert.ok(models.find(x=>x.id===model).supplemental_examples.includes(id));}
   const inputs=ref.parameters.public_inputs;assert.equal(inputs.registry_group,group);assert.equal(inputs.edition,release.edition);assert.equal(inputs.url,release.base+'inputs.json');assert.equal(inputs.sha256,sha(base+'inputs.json'));assert.equal(ref.parameters.inputs_sha256,inputs.sha256);
   let target=json(base+'inputs.json');assert.equal(typeof inputs.json_pointer,'string');assert.ok(inputs.json_pointer===''||inputs.json_pointer.startsWith('/'));for(const encoded of inputs.json_pointer===''?[]:inputs.json_pointer.slice(1).split('/')){assert.ok(!/~(?![01])/.test(encoded));const key=encoded.replaceAll('~1','/').replaceAll('~0','~');assert.ok(Object.hasOwn(target,key));target=target[key];}assert.ok(target&&typeof target==='object');
   assert.deepEqual({dimension:ref.dimension,domain_kind:ref.domain_kind??null,bounds:ref.bounds},freeze.reference_geometry[id]);
   assert.equal(c.gallery_figure,id+'-preview.png');assert.equal(c.additional_figures.filter(x=>x.file===c.gallery_figure).length,1);
   png(base+'results/'+id+'.png',manifest.files['results/'+id+'.png']);png(base+'results/'+c.gallery_figure,manifest.files['results/'+c.gallery_figure]);
   const item=gallery.find(x=>x.id===pid),entry=item.supplemental_execution_entries.find(x=>x.id===id);assert.equal(entry.preview.url,'/'+base+'results/'+c.gallery_figure);assert.equal(entry.preview.sha256,manifest.files['results/'+c.gallery_figure]);
   const page=json(`numerical-methods-atlas/validation/${id}/index.json`),html=bytes(`numerical-methods-atlas/validation/${id}/index.html`).toString();assert.equal(page.problem_id,pid);assert.equal(page.release.base,release.base);assert.ok(page.release.code_urls.includes(release.base+'run.py'));assert.ok(page.release.test_urls.length);
   const measured=saved.cases.find(x=>x.id===id);assert.deepEqual(page.measured,measured);studyOutcomes(page.measured,sha(base+'acceptance.json'));
   if(measured.original_target_summary){assert.ok(html.includes('data-original-target-status="'+(measured.original_target_summary.all_met?'all-met':'unmet')+'"'));assert.ok(html.includes('Passing the separate reproduction/reporting checks does not mean that every original accuracy goal was met.'));}
   if(Object.hasOwn(freeze.quadrature_row_accuracy_studies,id)){
    assert.deepEqual(page.editorial_note,exp.case_notes[id]);assert.ok(html.includes('validation-editorial-note'));
    const counts=freeze.quadrature_row_accuracy_studies[id].summary;
    assert.ok(page.editorial_note.en.includes(`${counts.met} met, ${counts.unmet} unmet and ${counts.not_computable} not computable`));
    assert.ok(html.includes('Passing reproduction checks does not mean that every accuracy goal was met.'));
   }
   assert.ok(c.code_files.every(file=>file.endsWith('.py')));for(const file of c.code_files)assert.ok(page.release.code_urls.includes(release.base+file));
   for(const lang of ['ja','en']){assert.ok(html.includes(`id="${id}-${lang}-measurements"`));assert.equal(ref.view[lang],`/numerical-methods-atlas/validation/${id}/?lang=${lang}#${id}-${lang}-measurements`);assert.ok(page.reading[lang].includes('/'+lang+'/read/'));}
   const chapter=chapters.find(x=>x.id==='validation-'+group);for(const [key,value] of [['problem_ids',pid],['execution_ids',id],['reference_ids',id]])assert.ok(chapter[key].includes(value));
  }
 }
 for(const [id,before] of Object.entries(baseline.models)){
  const now=models.find(x=>x.id===id),prior=before.supplemental_examples||[],tail=(now.supplemental_examples||[]).slice(prior.length);assert.deepEqual((now.supplemental_examples||[]).slice(0,prior.length),prior);
  assert.deepEqual(sorted(tail),sorted(ids.filter(cid=>freeze.case_models[cid].includes(id))));
  const bio={'bio-enzyme':'enzyme-qssa','bio-lotka-volterra':'lotka-volterra'},allowed=['supplemental_examples',...(Object.hasOwn(bio,id)?['status','note','execution_scope','coverage_scope']:[])];
  inverse(now,{keys:Object.keys(before),typed_sha256:fingerprint(before)},freeze.model_transitions[id],allowed);
  if(Object.hasOwn(bio,id)){
   const r=registry().releases.find(r=>r.group==='small-models'),m=json(releaseBase(r)+'cases.json'),c=(Array.isArray(m)?m:m.cases).find(c=>c.id===bio[id]);
   assert.equal(now.status,'local-example');assert.deepEqual(now.execution_scope,c.limits);assert.equal(now.coverage_scope,c.limits.en);
   assert.deepEqual(now.note,{ja:before.note.ja.replace(/ 文献解説のみ。$/,'')+' 限定した実行例：'+c.limits.ja,en:before.note.en.replace(/Literature-only\.$/,'').trimEnd()+' Scoped executed example: '+c.limits.en});
   assert.deepEqual(now.formula,before.formula);assert.deepEqual(now.formula_source,before.formula_source);
  }
 }
 assert.deepEqual(sorted(models.filter(x=>!Object.hasOwn(baseline.models,x.id)).map(x=>x.id)),sorted(freeze.new_model_ids));
});

test('four new methods and four promotions preserve legacy bilingual METHOD shapes and reading scope',()=>{
 const methods=json('catalog/atlas-methods.json').methods;assert.equal(methods.length,167);
 for(const id of [...NEW_METHODS,...PROMOTIONS]){
  const m=methods.find(x=>x.id===id);assert.equal(m.status,'educational-example');assert.ok(Array.isArray(m.assumptions)&&Array.isArray(m.assumptions_ja));
  for(const key of ['units','units_ja','boundary_conditions','boundary_conditions_ja','code_mapping_scope','code_mapping_scope_ja'])assert.ok(typeof m[key]==='string'&&m[key].trim());
  assert.ok(m.depth_scope.en.trim()&&m.depth_scope.ja.trim());assert.ok(m.references.every(r=>r.url&&r.label&&r.scope));
  if(NEW_METHODS.includes(id))assert.equal(fingerprint(m),freeze.new_method_records_typed_sha256[id]);
 }
 const curated=freeze.reference_curation;assert.equal(curated.sequence,86);assert.equal(curated.numerical_cases,0);assert.ok(curated.citations.length&&curated.public_reading_paths.length);
 for(const path of curated.public_reading_paths){const text=bytes(path).toString();assert.ok(!text.includes('/Users/')&&!text.includes('/private/tmp/'));}
 assert.ok(!ids.includes('mallat-original-reference')&&!ids.some(id=>/^sequence86/.test(id)));
 for(const cite of curated.citations){assert.ok(cite.url&&cite.read_scope&&cite.accessed_on);if(cite.publication_year===null)assert.notEqual(cite.year_role,'publication');}
});

test('the reviewed inverse rejects an unapproved method field, changed after-value and unrelated science',()=>{
 const methods=json('catalog/atlas-methods.json').methods;
 const id=PROMOTIONS[0],row=methods.find(x=>x.id===id),before=baseline.method_records[id],change=freeze.method_transitions[id];assert.ok(change);
 for(const mutate of [m=>{m.status='planned';},m=>{m.unreviewed_field=true;},m=>{m.aliases.push('unreviewed');}]){const bad=structuredClone(row);mutate(bad);assert.throws(()=>inverse(bad,before,change,promotionFields));}
 const old=methods.find(x=>Object.hasOwn(baseline.method_records,x.id)&&!Object.hasOwn(freeze.method_transitions,x.id));assert.ok(old);const bad=structuredClone(old);bad.units='unreviewed';assert.throws(()=>inverse(bad,baseline.method_records[old.id],null,appendFields));
 const model=json('catalog/atlas-equations.json').equations.find(x=>x.id==='bio-enzyme'),beforeModel=baseline.models[model.id],record={keys:Object.keys(beforeModel),typed_sha256:fingerprint(beforeModel)},changeModel=freeze.model_transitions[model.id],allowed=['supplemental_examples','status','note','execution_scope','coverage_scope'];
 for(const mutate of [m=>{m.execution_scope.en+=' unreviewed scope';},m=>{m.formula='unreviewed equation';},m=>{m.unreviewed_field=true;}]){const altered=structuredClone(model);mutate(altered);assert.throws(()=>inverse(altered,record,changeModel,allowed));}
});
