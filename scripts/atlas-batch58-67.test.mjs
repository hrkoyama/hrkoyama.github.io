import {projectMethodBeforeBatch68} from './fixtures/atlas-inventory.mjs';
// Frozen cohort protection and ten verified examples; science is not re-executed here.
// Data/hash checks only: no solver, renderer, network call or ZIP extraction.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createReadStream,readFileSync,statSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
async function streamSHA(path){
 const hash=createHash('sha256');
 for await(const chunk of createReadStream(new URL(path,root)))hash.update(chunk);
 return hash.digest('hex');
}
// Cross-language canonical metadata fingerprint. Numbers use their IEEE754
// bytes, avoiding Python/JS exponent-formatting and Unicode-escaping differences.
function typed(value){
 if(value===null)return Buffer.from('z');
 if(typeof value==='boolean')return Buffer.from(value?'b1':'b0');
 if(typeof value==='number'){
  assert.ok(Number.isFinite(value));const number=Buffer.alloc(8);number.writeDoubleBE(value);
  return Buffer.from('n'+number.toString('hex'));
 }
 if(typeof value==='string'){
  const text=Buffer.from(value);return Buffer.concat([Buffer.from('s'+text.length+':'),text]);
 }
 if(Array.isArray(value))return Buffer.concat([Buffer.from('a'+value.length+':'),...value.map(typed)]);
 const keys=Object.keys(value).sort((a,b)=>Buffer.compare(Buffer.from(a),Buffer.from(b)));
 return Buffer.concat([Buffer.from('o'+keys.length+':'),...keys.flatMap(key=>[typed(key),typed(value[key])])]);
}
const fingerprint=value=>createHash('sha256').update(typed(value)).digest('hex');
const pick=(row,keys)=>Object.fromEntries(keys.map(key=>[key,row[key]]));
const baseline=json('scripts/fixtures/atlas-batch58-67-baseline.json');
const expected=baseline.expected_new_groups,newGroups=Object.keys(expected);
const newIDs=Object.values(expected).flat();
const releaseBase=release=>`code/validated-examples/${release.edition}/${release.group}/`;
const sorted=value=>[...value].sort();
// This regression owns the historical cohort through batch67. Later batches
// have their own exact inventory checks; all earlier bytes/identities below
// remain mandatory, including the original baseline rather than new goldens.
const historicalGroups=new Set([...baseline.release_order,...newGroups]);
const historicalMethods=new Set([...Object.keys(baseline.methods),...baseline.expected_new_method_ids]);
const historicalEquations=new Set([...Object.keys(baseline.equations),...baseline.expected_new_equation_ids]);
function current(){
 const registry=json('numerical-methods-atlas/validation/releases.json');
 const releases=registry.releases.filter(row=>historicalGroups.has(row.group));
 return {...registry,releases,case_count:releases.reduce((n,row)=>n+row.case_ids.length,0)};
}
function oldMethodPointer(row){return row;}
function finite(value){
 if(typeof value==='number')assert.ok(Number.isFinite(value));
 else if(Array.isArray(value))value.forEach(finite);
 else if(value&&typeof value==='object')Object.values(value).forEach(finite);
}

test('batch58–67 preserves all 52 earlier immutable editions and every existing primary image',async()=>{
 assert.deepEqual(baseline.baseline_counts,{groups:52,cases:106,pytest:1352,methods:158,primary_figures:131,equations:70});
 const registry=current();
 assert.deepEqual(registry.releases.filter(row=>!newGroups.includes(row.group)).map(row=>row.group),baseline.release_order);
 for(const before of baseline.releases){
  // Preserve every prior edition, including its original MHD archive and pointer.
  for(const [path,hash] of Object.entries(before.immutable_files))assert.equal(await streamSHA(path),hash,path);
  const active=registry.releases.find(row=>row.group===before.release.group);assert.ok(active);
  assert.deepEqual(active,before.release);
 }
 const gallery=json('catalog/atlas-gallery.json').items,previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const [id,hash] of Object.entries(baseline.gallery_records_sha256))assert.equal(fingerprint(gallery.find(row=>row.id===id)),hash,id+'/old-gallery-record');
 for(const [id,hash] of Object.entries(baseline.preview_records_sha256))assert.equal(fingerprint(previews.find(row=>row.id===id)),hash,id+'/old-preview-record');
 for(const [path,hash] of Object.entries(baseline.preview_images_sha256))assert.equal(await streamSHA(path),hash,path+'/old-image');
});

test('all 158 existing method science and formula goldens remain, with one separately scoped dogleg method',()=>{
 const methods=json('catalog/atlas-methods.json').methods.map(projectMethodBeforeBatch68).filter(row=>historicalMethods.has(row.id));
 for(const [id,old] of Object.entries(baseline.methods)){
  const row=methods.find(value=>value.id===id);assert.ok(row,id);assert.equal(row.status,old.status,id+'/status');
  assert.equal(fingerprint(pick(row,old.stable_keys)),old.stable_sha256,id+'/scientific-fields');
  assert.equal(fingerprint(pick(row.metadata_review||{},old.review_keys)),old.review_sha256,id+'/old-review');
  for(const [field,languages] of Object.entries(old.text_prefixes))for(const [language,prefix] of Object.entries(languages)){
   const now=Buffer.from(row[field][language]);assert.ok(now.length>=prefix.utf8_bytes);
   assert.equal(createHash('sha256').update(now.subarray(0,prefix.utf8_bytes)).digest('hex'),prefix.sha256,id+'/'+field+'/'+language+'/old-prefix');
  }
  assert.deepEqual((row.references||[]).slice(0,old.reference_prefix_sha256.length).map(fingerprint),old.reference_prefix_sha256,id+'/references');
  assert.deepEqual((row.depth_additional_releases||[]).slice(0,old.additional_release_prefix_sha256.length).map(oldMethodPointer).map(fingerprint),old.additional_release_prefix_sha256,id+'/prior-releases');
  assert.deepEqual((row.supplemental_scope_profiles||[]).slice(0,old.scope_profile_prefix_sha256.length).map(fingerprint),old.scope_profile_prefix_sha256,id+'/prior-scope-profiles');
  if(old.primary_release)assert.deepEqual(oldMethodPointer(row.depth_release),old.primary_release,id+'/primary-release');
 }
 assert.deepEqual(sorted(methods.filter(row=>!Object.hasOwn(baseline.methods,row.id)).map(row=>row.id)),sorted(baseline.expected_new_method_ids));
 for(const id of baseline.expected_new_method_ids){
  const row=methods.find(value=>value.id===id);assert.equal(row.status,'educational-example');
  for(const field of ['name','summary','limitations'])for(const lang of ['ja','en'])assert.ok(row[field][lang].trim(),id+'/'+field+'/'+lang);
  assert.ok(row.references.length&&row.references.every(ref=>ref.url||ref.source||ref.doi));
 }
 const equations=json('catalog/atlas-equations.json').equations.filter(row=>historicalEquations.has(row.id));
 for(const [id,old] of Object.entries(baseline.equations))assert.equal(fingerprint(equations.find(row=>row.id===id)?.formula),old.formula_sha256,id+'/formula');
 assert.deepEqual(sorted(equations.filter(row=>!Object.hasOwn(baseline.equations,row.id)).map(row=>row.id)),sorted(baseline.expected_new_equation_ids));
});

test('four new groups expose ten fully verified cases and registry-derived test counts',async()=>{
 const registry=current();
 assert.deepEqual(sorted(registry.releases.filter(row=>!baseline.release_order.includes(row.group)).map(row=>row.group)),sorted(newGroups));
 assert.equal(newIDs.length,10);assert.equal(registry.releases.length,baseline.baseline_counts.groups+newGroups.length);
 assert.equal(registry.case_count,baseline.baseline_counts.cases+newIDs.length);
 const newRows=registry.releases.filter(row=>newGroups.includes(row.group));
 const expectedTests=baseline.baseline_counts.pytest+newRows.reduce((n,row)=>n+row.tests,0);
 assert.equal(registry.releases.reduce((n,row)=>n+row.tests,0),expectedTests);
 for(const [group,caseIDs] of Object.entries(expected)){
  const release=registry.releases.find(row=>row.group===group);assert.deepEqual(sorted(release.case_ids),sorted(caseIDs));
  assert.ok(Number.isInteger(release.tests)&&release.tests>0,group+'/registry-test-count');
  const base=releaseBase(release),v=json(base+'verification.json'),result=json(base+'results/result.json'),manifest=json(base+'source-manifest.json');
  assert.equal(release.base,'https://hrkoyama.github.io/'+base);
  assert.equal(v.passed,true);assert.equal(v.all_cases_rerun,true);
  assert.equal(v.tests,release.tests);assert.equal(v.passed_tests,release.tests);
  for(const key of ['failures','errors','skipped','returncode'])assert.equal(v[key],0,group+'/'+key);
  assert.equal(v.source_manifest_sha256,release.manifest_sha256);
  assert.equal(v.archive.sha256,release.archive_sha256);assert.equal(v.archive.file,release.archive);
  assert.equal(v.archive.bytes,statSync(new URL(base+release.archive,root)).size);
  for(const [path,hash] of [[base+'source-manifest.json',release.manifest_sha256],[base+'verification.json',release.verification_sha256],[base+'requirements.txt',release.requirements_sha256],[base+release.archive,release.archive_sha256]])assert.equal(await streamSHA(path),hash,path);
  assert.equal(manifest.group,group);assert.equal(manifest.version,release.edition);assert.deepEqual(sorted(manifest.case_ids),sorted(caseIDs));
  assert.equal(result.passed,true);assert.equal(typeof result.termination,'string');assert.ok(result.termination.length);assert.equal(result.input_sha256,sha(base+'inputs.json'));
  assert.deepEqual(sorted(Object.keys(result.checks)),sorted(caseIDs));assert.ok(Object.values(result.checks).every(value=>value===true));finite(result);
  assert.deepEqual(sorted(result.cases.map(row=>row.id)),sorted(caseIDs));
  for(const c of result.cases){
   assert.equal(c.passed,true);assert.ok(Object.keys(c.metrics).length,c.id+'/meaningful-metrics-required');
   assert.ok(Object.keys(c.checks).length&&Object.values(c.checks).every(value=>value===true));assert.ok(c.records.length||Object.keys(c.records).length);
  }
  for(const name of ['pre-run-contract.json','acceptance.json','inputs.json','cases.json','results/result.json'])assert.equal(sha(base+name),manifest.files[name],group+'/'+name);
 }
});

test('every new case binds bilingual pages, source methods, actual main and preview PNGs, and an immutable download',()=>{
 const registry=current(),exp=json('catalog/atlas-depth-expansion.json');
 const methods=new Set(json('catalog/atlas-methods.json').methods.map(row=>row.id));
 const problems=json('catalog/atlas-test-problems.json').problems,links=json('catalog/atlas-problem-links.json').problems;
 const refs=json('catalog/atlas-reference-supplements.json').cases,equations=json('catalog/atlas-equations.json').equations;
 for(const id of newIDs){
  const release=registry.releases.find(row=>row.case_ids.includes(id)),base=releaseBase(release),manifest=json(base+'source-manifest.json');
  const metadata=json(base+'cases.json');const c=(Array.isArray(metadata)?metadata:metadata.cases).find(row=>row.id===id);
  assert.ok(c.method_ids.length&&c.method_ids.every(mid=>methods.has(mid)),id+'/registered-methods');
  for(const field of ['title','summary','assumptions','algorithm','validation','limits'])for(const lang of ['ja','en'])assert.ok(c[field][lang].trim());
  assert.ok(c.references.length&&c.references.every(ref=>ref.id&&ref.title&&ref.review_level&&(ref.url||ref.doi||ref.source)));
  assert.equal(c.gallery_figure,id+'-preview.png');
  const extra=c.additional_figures.filter(row=>row.file===c.gallery_figure);assert.equal(extra.length,1);
  for(const lang of ['ja','en'])assert.ok(extra[0].caption[lang].trim());
  for(const filename of [id+'.png',c.gallery_figure]){
   const path=base+'results/'+filename,b=bytes(path);assert.equal(sha(path),manifest.files['results/'+filename]);
   assert.ok(b.subarray(0,8).equals(Buffer.from('89504e470d0a1a0a','hex')));assert.equal(b.toString('ascii',12,16),'IHDR');
   assert.ok(b.readUInt32BE(16)>0&&b.readUInt32BE(20)>0);
  }
  const pid=exp.case_problem_ids[id],link=links.find(row=>row.id===pid),reference=refs.find(row=>row.id===id);
  assert.ok(problems.some(row=>row.id===pid));assert.ok(link.references.some(row=>row.id===id));assert.ok(reference);
  for(const eqid of exp.case_equations[id].ids){assert.ok(link.equation_ids.includes(eqid));assert.ok(equations.find(row=>row.id===eqid).supplemental_examples.includes(id));}
  const entry=json(`numerical-methods-atlas/validation/${id}/index.json`),html=bytes(`numerical-methods-atlas/validation/${id}/index.html`).toString();
  assert.equal(entry.release.base,release.base);assert.equal(entry.release.passed_tests,release.tests);assert.equal(entry.gallery_figure,c.gallery_figure);
  assert.ok(entry.release.code_urls.some(url=>url===release.base+'run.py'));assert.ok(entry.release.test_urls.length);
  for(const lang of ['ja','en']){
   assert.ok(html.includes(`id="${id}-${lang}-measurements"`));
   assert.equal(reference.view[lang],`/numerical-methods-atlas/validation/${id}/?lang=${lang}#${id}-${lang}-measurements`);
   assert.ok(entry.reading[lang].includes('/'+lang+'/read/'));
  }
  assert.ok(html.includes(release.archive));
 }
});

test('algebraic derivative and optimization maps have no invented spatial dimension',()=>{
 const refs=json('catalog/atlas-reference-supplements.json').cases;
 const fields=Object.fromEntries(['globalization-difficult-starts','reverse-vjp-duality','hessian-vector-products','kink-branch-derivatives'].map(id=>[id,'finite-dimensional-nonlinear-map']).concat([['bfgs-lbfgs-controls','finite-dimensional-optimization']]));
 for(const [id,model] of Object.entries(fields)){
  const row=refs.find(value=>value.id===id);assert.equal(row.model,model);assert.equal(row.domain_kind,'finite-dimensional-algebra');assert.equal(row.dimension,null);assert.deepEqual(row.bounds,[]);
 }
 const equations=json('catalog/atlas-depth-expansion.json').case_equations;
 for(const id of ['bratu-fold-sensitivity','bratu-distributed-vjp','bratu-gn-lm-bounds','bratu-noise-regularization'])assert.deepEqual(equations[id].ids,['bratu']);
 assert.deepEqual(equations['diffusion-discrete-adjoint'].ids,['heat']);
 const method=json('catalog/atlas-methods.json').methods.find(row=>row.id==='dogleg-trust-region');
 assert.ok(method.assumptions.length&&method.assumptions_ja.length===method.assumptions.length);
 for(const key of ['units','units_ja','boundary_conditions','boundary_conditions_ja'])assert.ok(method[key].trim());
});
