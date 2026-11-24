// Frozen scientific cohort and public data/graph checks only. No science,
// rendering, reference generation, archive extraction or network request.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {createReadStream,readFileSync,statSync} from 'node:fs';
import {projectMethodBeforeBatch68} from './fixtures/atlas-inventory.mjs';
const root=new URL('../',import.meta.url);
const local=p=>String(p).replace(/^https:\/\/hrkoyama\.github\.io\//,'').replace(/^\//,'');
const bytes=p=>readFileSync(new URL(local(p),root));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const sorted=xs=>[...xs].sort();
const rows=value=>Array.isArray(value)?value:Object.values(value);
async function streamSHA(path){const h=createHash('sha256');for await(const b of createReadStream(new URL(local(path),root)))h.update(b);return h.digest('hex');}
const baseline=json('scripts/fixtures/atlas-batch68-77-baseline.json');
const EXPECTED={
 'ode-adaptivity':['robertson-stiff-kinetics','van-der-pol-stiff-transition','rk45-dense-events','strang-boundary-order-reduction'],
 'steady-rk':['jameson-steady-linear-modes'],
 'dae-controls':['index1-dae-consistent-initialization','robertson-conservation-dae','high-index-pendulum'],
 'geometric-controls':['shake-rattle-pendulum','kepler-eccentricity','multifrequency-resonance'],
};
const MODELS={
 'robertson-stiff-kinetics':['robertson-kinetics'],
 'van-der-pol-stiff-transition':['van-der-pol'],
 'rk45-dense-events':['linear-evolution-system'],
 'strang-boundary-order-reduction':['inhomogeneous-reaction-diffusion','heat'],
 'jameson-steady-linear-modes':['linear-evolution-system','finite-dimensional-linear-system'],
 'index1-dae-consistent-initialization':['index-one-dae'],
 'robertson-conservation-dae':['robertson-kinetics','index-one-dae'],
 'high-index-pendulum':['constrained-pendulum','hamiltonian'],
 'shake-rattle-pendulum':['constrained-pendulum','hamiltonian'],
 'kepler-eccentricity':['kepler-two-body','particle-gravity','hamiltonian'],
 'multifrequency-resonance':['coupled-harmonic-oscillators','hamiltonian'],
};
const PROBLEMS=Object.fromEntries(Object.keys(MODELS).map(id=>[id,({'robertson-conservation-dae':'robertson-stiff-kinetics','shake-rattle-pendulum':'high-index-pendulum','kepler-eccentricity':'gravity-kepler'})[id]||id]));
const NEW_METHODS=['rk45','jameson-steady-rk','shake','rattle'];
const NEW_MODELS=['robertson-kinetics','van-der-pol','linear-evolution-system','inhomogeneous-reaction-diffusion','index-one-dae','constrained-pendulum','kepler-two-body','coupled-harmonic-oscillators'];
const ids=Object.values(EXPECTED).flat(),groups=Object.keys(EXPECTED);
const releaseBase=r=>`code/validated-examples/${r.edition}/${r.group}/`;
const registry=()=>json('numerical-methods-atlas/validation/releases.json');
function finite(value){if(typeof value==='number')assert.ok(Number.isFinite(value));else if(Array.isArray(value))value.forEach(finite);else if(value&&typeof value==='object')Object.values(value).forEach(finite);}
function png(path,hash){const b=bytes(path);assert.equal(sha(path),hash,path);assert.ok(b.subarray(0,8).equals(Buffer.from('89504e470d0a1a0a','hex')));assert.equal(b.toString('ascii',12,16),'IHDR');assert.ok(b.readUInt32BE(16)>0&&b.readUInt32BE(20)>0);}
// CSV parser preserves quoted labels, escaped quotes and embedded line breaks.
function csv(text){
 const out=[];let row=[],cell='',quoted=false;
 for(let i=0;i<text.length;i++){
  const c=text[i];
  if(c==='"'){if(quoted&&text[i+1]==='"'){cell+='"';i++;}else quoted=!quoted;}
  else if(!quoted&&c===','){row.push(cell);cell='';}
  else if(!quoted&&(c==='\n'||c==='\r')){if(c==='\r'&&text[i+1]==='\n')i++;row.push(cell);out.push(row);row=[];cell='';}
  else cell+=c;
 }
 assert.equal(quoted,false,'unclosed CSV quote');if(cell||row.length){row.push(cell);out.push(row);}return out;
}
function originalSummary(targets,acceptance){const values=Object.values(targets);assert.ok(values.length);assert.ok(values.every(v=>typeof v==='boolean'));return {met:values.filter(Boolean).length,total:values.length,all_met:values.every(Boolean),acceptance_sha256:acceptance};}

test('batch68–77 pins its exact baseline and preserves earlier releases, methods, equations and primary pictures',async()=>{
 assert.equal(baseline.base_commit,'c89776f807fc0137d3aa46aba172a784dabc61aa');
 assert.deepEqual(baseline.baseline_counts,{groups:56,cases:116,pytest:1456,methods:159,primary_figures:141,equations:72});
 assert.deepEqual(baseline.expected_new_groups,EXPECTED);assert.deepEqual(sorted(baseline.expected_new_method_ids),sorted(NEW_METHODS));
 assert.deepEqual(sorted(baseline.expected_new_equation_ids),sorted(NEW_MODELS));
 const releases=registry().releases;
 assert.deepEqual(releases.filter(r=>baseline.release_order.includes(r.group)),baseline.releases);
 const methods=json('catalog/atlas-methods.json').methods;
 assert.deepEqual(sorted(methods.filter(m=>!Object.hasOwn(baseline.methods,m.id)).map(m=>m.id)),sorted(NEW_METHODS));
 for(const id of NEW_METHODS){const m=methods.find(m=>m.id===id);assert.equal(m.status,'educational-example');assert.ok(Array.isArray(m.aliases));assert.equal(typeof m.code_mapping_scope,'string');assert.ok(m.references.length&&m.references.every(r=>r.url&&r.label&&r.scope));}
 const dae=methods.find(m=>m.id==='dae');assert.equal(dae.status,'educational-example');assert.equal(dae.depth_release.group,'dae-controls');
 for(const [id,before] of Object.entries(baseline.methods))assert.deepEqual(projectMethodBeforeBatch68(methods.find(m=>m.id===id)),before,id+'/all-old-method-fields');
 const equations=json('catalog/atlas-equations.json').equations;
 for(const [id,before] of Object.entries(baseline.equations)){
  const now=equations.find(e=>e.id===id);assert.ok(now,id);
  const projected=structuredClone(now),prior=before.supplemental_examples||[],tail=(now.supplemental_examples||[]).slice(prior.length);
  assert.deepEqual((now.supplemental_examples||[]).slice(0,prior.length),prior,id+'/old-equation-release-prefix');
  assert.deepEqual(sorted(tail),sorted(ids.filter(caseID=>MODELS[caseID].includes(id))),id+'/exact-new-equation-edges');
  if(Object.hasOwn(before,'supplemental_examples'))projected.supplemental_examples=prior;else delete projected.supplemental_examples;
  assert.deepEqual(projected,before,id+'/all-old-equation-fields');
 }
 const gallery=json('catalog/atlas-gallery.json').items,preview=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const before of rows(baseline.gallery_items))assert.deepEqual(gallery.find(r=>r.id===before.id),before,before.id+'/old-primary-selection');
 for(const before of rows(baseline.preview_manifest_items)){
  assert.deepEqual(preview.find(r=>r.id===before.id),before,before.id+'/old-preview-record');
  assert.equal(await streamSHA(before.image),before.image_sha256,before.id+'/old-primary-image');
 }
});

test('four exact new groups expose eleven cases, canonical ZIP proofs and finite numeric CSV',async()=>{
 const current=registry(),releases=current.releases;
 assert.equal(releases.length,60);assert.equal(current.case_count,127);assert.equal(ids.length,11);
 assert.deepEqual(sorted(releases.filter(r=>!baseline.release_order.includes(r.group)).map(r=>r.group)),sorted(groups));
 assert.equal(json('catalog/atlas-methods.json').methods.length,163);assert.equal(json('catalog/atlas-equations.json').equations.length,80);
 assert.equal(json('catalog/atlas-gallery.json').items.length,149);assert.equal(json('catalog/atlas-test-problems.json').problems.length,149);
 for(const [group,caseIDs] of Object.entries(EXPECTED)){
  const r=releases.find(r=>r.group===group),fixed=baseline.canonical_packets[group];assert.ok(r&&fixed,group);
  const base=releaseBase(r),v=json(base+'verification.json'),manifest=json(base+'source-manifest.json'),result=json(base+'results/result.json');
  assert.deepEqual(sorted(r.case_ids),sorted(caseIDs));assert.deepEqual(sorted(fixed.case_ids),sorted(caseIDs));assert.equal(local(fixed.base),base);assert.equal(r.edition,fixed.edition);
  assert.equal(r.base,'https://hrkoyama.github.io/'+base);assert.equal(r.tests,fixed.tests);
  for(const [key,fixedKey] of [['verification_sha256','verification_sha256'],['manifest_sha256','manifest_sha256'],['archive_sha256','archive_sha256']])assert.equal(r[key],fixed[fixedKey],group+'/'+key);
  assert.equal(r.archive,fixed.archive_file);assert.equal(v.passed,true);assert.equal(v.all_cases_rerun,true);assert.equal(v.tests,r.tests);assert.equal(v.passed_tests,r.tests);
  for(const key of ['failures','errors','skipped','returncode'])assert.equal(v[key],0,group+'/'+key);
  assert.deepEqual(Object.fromEntries(['numpy','scipy','pytest'].map(k=>[k,v.environment[k]])),{numpy:'2.0.2',scipy:'1.14.1',pytest:'8.3.5'});
  assert.equal(sha(base+'requirements.txt'),r.requirements_sha256);assert.equal(manifest.files['requirements.txt'],r.requirements_sha256);
  assert.equal(v.source_manifest_sha256,r.manifest_sha256);assert.equal(v.archive.sha256,r.archive_sha256);assert.equal(v.archive.file,r.archive);
  assert.equal(v.archive.bytes,fixed.archive_bytes);assert.equal(statSync(new URL(base+r.archive,root)).size,fixed.archive_bytes);
  for(const [path,hash] of [[base+'source-manifest.json',r.manifest_sha256],[base+'verification.json',r.verification_sha256],[base+r.archive,r.archive_sha256]])assert.equal(await streamSHA(path),hash,path);
  assert.equal(manifest.group,group);assert.equal(manifest.version,r.edition);assert.deepEqual(sorted(manifest.case_ids),sorted(caseIDs));
  assert.equal(result.passed,true);assert.equal(result.termination,'completed_fixed_protocol');assert.equal(result.input_sha256,sha(base+'inputs.json'));assert.equal(result.input_sha256,fixed.input_sha256);finite(result);
  assert.deepEqual(sorted(Object.keys(result.checks)),sorted(caseIDs));assert.ok(Object.values(result.checks).every(v=>v===true));assert.deepEqual(sorted(result.cases.map(c=>c.id)),sorted(caseIDs));
  for(const c of result.cases){assert.equal(c.passed,true);assert.ok(c.records.length);assert.ok(Object.keys(c.metrics).length);assert.ok(Object.keys(c.checks).length);assert.ok(Object.values(c.checks).every(v=>v===true));}
  for(const name of ['pre-run-contract.json','acceptance.json','inputs.json','cases.json','results/result.json'])assert.equal(sha(base+name),manifest.files[name],group+'/'+name);
  const csvNames=Object.keys(manifest.files).filter(name=>/^results\/[^/]+\.csv$/.test(name));assert.ok(csvNames.length,group+'/numeric-CSV');
  for(const name of csvNames){
   assert.equal(sha(base+name),manifest.files[name]);const parsed=csv(bytes(base+name).toString());assert.ok(parsed.length>=2);const header=parsed[0];assert.equal(new Set(header).size,header.length);
   for(const row of parsed.slice(1)){assert.equal(row.length,header.length);let numeric=0;for(const value of row){assert.ok(!/^[+-]?(?:nan|inf|infinity)$/i.test(value.trim()),name+'/nonfinite');if(value.trim()!==''&&Number.isFinite(Number(value)))numeric++;}assert.ok(numeric,name+'/numeric-row');}
  }
 }
 assert.equal(releases.reduce((n,r)=>n+r.tests,0),1456+Object.values(baseline.canonical_packets).reduce((n,r)=>n+r.tests,0));
});

test('all eleven executions bind exact physical aliases, equations, bilingual pages and their own preview images',()=>{
 const exp=json('catalog/atlas-depth-expansion.json'),links=json('catalog/atlas-problem-links.json').problems,problems=json('catalog/atlas-test-problems.json').problems,refs=json('catalog/atlas-reference-supplements.json').cases;
 const gallery=json('numerical-methods-atlas/gallery/index.json').items,methodRows=json('catalog/atlas-methods.json').methods,methods=new Set(methodRows.map(r=>r.id)),equations=json('catalog/atlas-equations.json').equations,chapters=json('catalog/atlas-chapter-links.json').chapters;
 for(const [group,caseIDs] of Object.entries(EXPECTED)){
  const r=registry().releases.find(r=>r.group===group),base=releaseBase(r),manifest=json(base+'source-manifest.json'),metadata=json(base+'cases.json');
  for(const id of caseIDs){
   const c=(Array.isArray(metadata)?metadata:metadata.cases).find(c=>c.id===id),pid=PROBLEMS[id],link=links.find(p=>p.id===pid),ref=refs.find(p=>p.id===id);assert.ok(c&&link&&ref,id);
   const input=ref.parameters.public_inputs;assert.equal(input.registry_group,group);assert.equal(input.edition,r.edition);assert.equal(input.member,'inputs.json');assert.equal(input.url,r.base+'inputs.json');assert.equal(input.sha256,sha(base+'inputs.json'));assert.equal(ref.parameters.inputs_sha256,input.sha256);
   assert.equal(typeof input.json_pointer,'string');let target=json(base+'inputs.json');if(input.json_pointer!==''){assert.ok(input.json_pointer.startsWith('/'));for(const encoded of input.json_pointer.slice(1).split('/')){assert.ok(!/~(?![01])/.test(encoded));const key=encoded.replaceAll('~1','/').replaceAll('~0','~');assert.ok(Object.hasOwn(target,key));target=target[key];}}assert.ok(target&&typeof target==='object'&&Object.keys(target).length);
   assert.equal(exp.case_problem_ids[id],pid);assert.deepEqual(exp.case_equations[id].ids,MODELS[id]);assert.ok(problems.find(p=>p.id===pid).supplemental_examples.some(e=>e.id===id));assert.ok(link.references.some(e=>e.id===id));
   assert.ok(c.method_ids.length&&c.method_ids.every(mid=>methods.has(mid)));for(const mid of c.method_ids){assert.ok(link.method_ids.includes(mid));const m=methodRows.find(m=>m.id===mid),bindings=[m.depth_release,...(m.depth_additional_releases||[])].filter(Boolean);assert.ok(bindings.some(b=>b.group===group&&b.edition===r.edition&&b.case_ids.includes(id)),id+'/'+mid+'/scoped-execution-binding');}
   for(const eq of MODELS[id]){assert.ok(link.equation_ids.includes(eq));assert.ok(equations.find(e=>e.id===eq).supplemental_examples.includes(id));}assert.equal(ref.model,MODELS[id][0]);
   const chapter=chapters.find(c=>c.id==='validation-'+group);for(const [field,value] of [['problem_ids',pid],['code_problem_ids',pid],['execution_ids',id],['reference_ids',id]])assert.ok(chapter[field].includes(value),id+'/chapter-'+field);

   for(const field of ['title','summary','assumptions','algorithm','validation','limits'])for(const lang of ['ja','en'])assert.ok(c[field][lang].trim(),id+'/'+field+'/'+lang);
   assert.equal(c.gallery_figure,id+'-preview.png');const extra=c.additional_figures.filter(e=>e.file===c.gallery_figure);assert.equal(extra.length,1);for(const lang of ['ja','en'])assert.ok(extra[0].caption[lang].trim());
   for(const file of [id+'.png',c.gallery_figure])png(base+'results/'+file,manifest.files['results/'+file]);
   const item=gallery.find(p=>p.id===pid),supp=item.supplemental_execution_entries.find(e=>e.id===id);assert.ok(supp,id+'/gallery-supplemental-execution');assert.equal(supp.preview.url,'/'+base+'results/'+c.gallery_figure);assert.equal(supp.preview.sha256,manifest.files['results/'+c.gallery_figure]);
   const entry=json(`numerical-methods-atlas/validation/${id}/index.json`),html=bytes(`numerical-methods-atlas/validation/${id}/index.html`).toString();assert.equal(entry.problem_id,pid);assert.equal(entry.release.base,r.base);assert.equal(entry.release.passed_tests,r.tests);assert.ok(entry.release.code_urls.includes(r.base+'run.py'));assert.ok(entry.release.test_urls.length);
   for(const lang of ['ja','en']){assert.ok(html.includes(`id="${id}-${lang}-measurements"`));assert.equal(ref.view[lang],`/numerical-methods-atlas/validation/${id}/?lang=${lang}#${id}-${lang}-measurements`);assert.ok(entry.reading[lang].includes('/'+lang+'/read/'));}
   assert.equal(ref.dimension,id==='strang-boundary-order-reduction'?1:null);if(id!=='strang-boundary-order-reduction'){assert.equal(ref.domain_kind,'finite-dimensional-ivp');assert.deepEqual(ref.bounds,[]);}
  }
 }
 assert.equal(new Set(Object.values(PROBLEMS).filter(id=>!rows(baseline.gallery_items).some(p=>p.id===id))).size,8);
});

test('unmet original goals remain actual study data, separate from successful reporting checks and preserved first failures',()=>{
 for(const group of ['ode-adaptivity','steady-rk','dae-controls']){
  const r=registry().releases.find(r=>r.group===group),base=releaseBase(r),result=json(base+'results/result.json'),policy=json(base+'reporting-policy.json'),acceptance=sha(base+'acceptance.json');
  assert.equal(policy.original_input_sha256,sha(base+'inputs.json'));assert.equal(policy.original_acceptance_sha256,acceptance);
  for(const c of result.cases){
   if(!c.original_target_results)continue;
   assert.deepEqual(c.original_target_summary,originalSummary(c.original_target_results,acceptance),c.id+'/original-summary');
   const entry=json(`numerical-methods-atlas/validation/${c.id}/index.json`);assert.deepEqual(entry.measured.original_target_results,c.original_target_results);assert.deepEqual(entry.measured.original_target_summary,c.original_target_summary);
   const goals=c.original_study_goal_measurements||{};
   for(const [key,goal] of Object.entries(goals)){assert.ok(Object.hasOwn(c.original_target_results,key));assert.equal(goal.met,c.original_target_results[key]);assert.ok(Object.hasOwn(goal,'measured')&&Object.hasOwn(goal,'limit'));finite(goal);}
   if(Object.keys(goals).length||!c.original_target_summary.all_met){
    const html=bytes(`numerical-methods-atlas/validation/${c.id}/index.html`).toString();assert.ok(html.includes('data-original-target-status="'+(c.original_target_summary.all_met?'all-met':'unmet')+'"'));assert.ok(html.includes('Passing the separate reproduction/reporting checks does not mean that every original accuracy goal was met.'));
   }
   assert.ok(Object.values(c.checks).every(v=>v===true)); // Does not require original goals to be true or false.
  }
  if(group==='ode-adaptivity'){
   const h=base+policy.history_directory+'/',first=json(h+'original-result.json');assert.equal(sha(h+'original-result.json'),policy.original_result_sha256);assert.equal(first.passed,false);
   const firstValues=first.cases.flatMap(c=>Object.values(c.checks));assert.equal(firstValues.length,209);assert.equal(firstValues.filter(Boolean).length,208);assert.equal(first.cases.find(c=>c.id==='van-der-pol-stiff-transition').checks[policy.original_gate_id],false);
   const c=result.cases.find(c=>c.id==='van-der-pol-stiff-transition'),study=c.study_results.mu1_tight_global_goal,record=c.records.find(r=>r.run_id===policy.run_id);
   assert.equal(policy.current_false_required,false);assert.equal(study.requested_global_bound,2e-5);assert.equal(study.actual_sampled_weighted_linf,record.sampled_weighted_linf);assert.equal(study.target_met,record.sampled_weighted_linf<=2e-5);assert.equal(c.original_target_results[policy.original_gate_id],study.target_met);assert.ok(!Object.hasOwn(c.checks,policy.original_gate_id));
   const all=result.cases.flatMap(c=>Object.values(c.original_target_results));assert.equal(all.length,209);assert.deepEqual(result.original_target_summary,{met:all.filter(Boolean).length,total:209,all_met:all.every(Boolean),acceptance_sha256:acceptance});
  }else{
   const path=base+'history/first-attempt/summary.json',first=json(path);assert.equal(sha(path),policy.history_summary_sha256);assert.equal(first.original_result_sha256,policy.first_attempt_result_sha256);assert.equal(first.passed,false);assert.ok(first.cases.some(c=>Object.values(c.checks).some(v=>v===false)));
   for(const c of result.cases.filter(c=>Object.hasOwn(policy.study_goal_keys,c.id))){const goals=new Set(policy.study_goal_keys[c.id]);for(const [key,value] of Object.entries(c.original_target_results))if(!goals.has(key))assert.equal(c.checks[key],value);}
  }
 }
});

// Mutation controls exercise the projection boundary, not any numerical solver.
test('the dated method inverse rejects changed after values, extra fields and unrelated old science',()=>{
 const methods=json('catalog/atlas-methods.json').methods;const row=methods.find(m=>m.id==='dae');
 for(const mutate of [m=>{m.status='planned';},m=>{m.aliases.push('unreviewed-alias');},m=>{m.summary.en+=' unreviewed append';},m=>{m.unreviewed_field=true;}]){const bad=structuredClone(row);mutate(bad);assert.throws(()=>projectMethodBeforeBatch68(bad));}
 const unchanged=methods.find(m=>m.id==='ssprk33');assert.ok(unchanged);const bad=structuredClone(unchanged);bad.units='unreviewed physical unit';assert.throws(()=>projectMethodBeforeBatch68(bad));
});

test('NIST version dates remain distinct from unverified publication years',()=>{
 const card=json('catalog/atlas-reference-supplements.json').cases.find(r=>r.id==='shake-rattle-pendulum');
 const cite=card.citations.find(r=>r.url==='https://dlmf.nist.gov/22.4');assert.ok(cite);assert.equal(cite.publication_year,null);assert.equal(cite.source_year,2026);assert.equal(cite.year_role,'version');assert.equal(cite.version,'1.2.8');assert.equal(cite.release_date,'2026-09-15');assert.equal(cite.accessed_on,'2026-11-24');
});
