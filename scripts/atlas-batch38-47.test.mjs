import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const baseline=json('scripts/fixtures/atlas-batch38-47-baseline.json');
const expected={
 'lbm-cavity':['lbm-cavity-re100'],
 'lbm-taylor-green':['lbm-taylor-green'],
 'lbm-annulus':['lbm-annular-couette-control'],
 'lbm-curved-boundary':['lbm-cylinder-re20'],
 'radiation-scattering':['isotropic-scattering-slab'],
 'radiation-matter':['su-olson-diffusion1996','su-olson-transport1997'],
 'radiation-geometry':['shadow-absorber2d','opposing-beams2d'],
 'stochastic-accuracy':['gbm-weak-moments','ou-weak-moments','gbm-milstein-strong'],
 'stochastic-estimation':['normal-tail-importance','correlated-gaussian-mcmc'],
};
const ids=Object.values(expected).flat();

test('batch38–47 preserves existing scientific files, search details, equations and references',()=>{
 for(const [path,hash] of Object.entries(baseline.immutable_files))assert.equal(sha(path),hash,path);
 for(const [path,hash] of Object.entries(baseline.incoming_ea8564_preservation.immutable_files))assert.equal(sha(path),hash,path+'/preserved-incoming-release');
 const methods=json('catalog/atlas-methods.json').methods;
 for(const [id,status] of Object.entries(baseline.method_statuses))assert.equal(methods.find(x=>x.id===id)?.status,status,id);
 const appendFields=new Set(['summary','limitations','depth_release','depth_additional_releases','supplemental_scope_profiles','metadata_review']);
 const firstScopeMethods=new Set(['backward-euler','d2q9-bgk','monte-carlo','sde']);
 for(const m of methods){
  assert.deepEqual(Object.fromEntries(Object.entries(m).filter(([k])=>!appendFields.has(k)&&!(firstScopeMethods.has(m.id)&&k==='depth_scope'))),baseline.method_nonappend_fields[m.id],m.id+'/preserved-science');
  if(firstScopeMethods.has(m.id))for(const lang of ['ja','en'])assert.ok(m.depth_scope[lang].trim(),m.id+'/new-scoped-release-description');
  assert.deepEqual(Object.fromEntries(Object.entries(m.metadata_review||{}).filter(([k])=>k!=='supplemental_review')),baseline.method_review_nonappend_fields[m.id],m.id+'/preserved-review');
 }
 for(const [id,old] of Object.entries(baseline.method_append_fields_before_batch38)){
  const current=methods.find(x=>x.id===id);
  for(const key of ['summary','limitations'])for(const lang of ['ja','en'])assert.ok(current[key][lang].startsWith(old[key][lang]),id+'/'+key+'/'+lang+'/preserved-description');
  if(old.depth_release)assert.deepEqual(current.depth_release,old.depth_release,id+'/preserved-primary-release');
  for(const key of ['depth_additional_releases','supplemental_scope_profiles'])assert.deepEqual((current[key]||[]).slice(0,(old[key]||[]).length),old[key]||[],id+'/'+key+'/preserved-prefix');
 }
 const equations=json('catalog/atlas-equations.json').equations;
 for(const [id,formula] of Object.entries(baseline.equation_formulas))assert.deepEqual(equations.find(x=>x.id===id)?.formula,formula,id);
 for(const [oldRows,currentRows] of [[baseline.problem_records,json('catalog/atlas-test-problems.json').problems],[baseline.equation_records,equations]])for(const old of oldRows){
  const current=currentRows.find(x=>x.id===old.id);
  const fixed=row=>Object.fromEntries(Object.entries(row).filter(([k])=>k!=='supplemental_examples'));
  assert.deepEqual(fixed(current),fixed(old),old.id+'/preserved-model-or-problem');
  for(const entry of old.supplemental_examples||[])assert.ok(current.supplemental_examples.some(x=>JSON.stringify(x)===JSON.stringify(entry)),old.id+'/preserved-example');
 }
 assert.deepEqual(equations.filter(x=>!Object.hasOwn(baseline.equation_formulas,x.id)).map(x=>x.id).sort(),['static-grey-transfer','non-equilibrium-diffusion-exchange','static-grey-m1','scalar-ito-diffusion','gaussian-probability-model'].sort());
 const refs=json('catalog/atlas-reference-supplements.json').cases;
 for(const old of baseline.reference_supplements)assert.deepEqual(refs.find(x=>x.id===old.id),old,old.id);
 assert.equal(sha('catalog/atlas-execution-examples.json'),baseline.common_registry_sha256);
});

test('batch38–47 retains all primary gallery records and old release metadata',()=>{
 const gallery=json('catalog/atlas-gallery.json').items;
 for(const old of baseline.gallery_items)assert.deepEqual(gallery.find(x=>x.id===old.id),old,old.id);
 assert.equal(gallery.length,baseline.gallery_items.length+9);
 const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const old of baseline.preview_manifest_items)assert.deepEqual(previews.find(x=>x.id===old.id),old,old.id);
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.deepEqual(registry.releases.filter(x=>!Object.hasOwn(expected,x.group)),baseline.release_registry.releases);
 assert.equal(registry.case_count,baseline.release_registry.case_count+ids.length);
 assert.deepEqual(registry.releases.filter(x=>Object.hasOwn(expected,x.group)).map(x=>x.group),Object.keys(expected));
});

test('all new packets expose actual verified results and immutable archive identities',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 for(const [group,names] of Object.entries(expected)){
  const release=registry.releases.find(x=>x.group===group);assert.ok(release,group);
  assert.deepEqual([...release.case_ids].sort(),[...names].sort());
  const base=`code/validated-examples/${release.edition}/${group}/`;
  const v=json(base+'verification.json'),result=json(base+'results/result.json'),manifest=json(base+'source-manifest.json');
  assert.equal(v.passed,true);assert.equal(v.all_cases_rerun,true);
  for(const key of ['failures','errors','skipped'])assert.equal(v[key],0,group+'/'+key);
  assert.ok(v.passed_tests>0);assert.equal(result.passed,true);assert.equal(result.input_sha256,sha(base+'inputs.json'));
  assert.deepEqual(Object.keys(result.checks).sort(),[...names].sort());assert.ok(Object.values(result.checks).every(x=>x===true));
  for(const c of result.cases){assert.equal(c.passed,true);assert.ok(c.records.length);assert.ok(Object.keys(c.checks).length);assert.ok(Object.values(c.checks).every(x=>x===true));}
  for(const name of names){assert.ok(manifest.files[`results/${name}.png`]);assert.ok(manifest.files[`results/${name}-preview.png`]);assert.ok(Object.keys(manifest.files).some(p=>p.startsWith(`results/${name}`)&&p.endsWith('.csv')));}
  for(const key of ['pre-run-contract.json','acceptance.json'])assert.ok(manifest.files[key]);
  for(const key of ['archive','manifest','verification','requirements']){
   const file=key==='archive'?release.archive:key==='manifest'?'source-manifest.json':key==='verification'?'verification.json':'requirements.txt';assert.equal(sha(base+file),release[key+'_sha256']);
  }
 }
});

test('new examples connect bilingual executable pages, equations, references and problem images',()=>{
 const exp=json('catalog/atlas-depth-expansion.json'),problems=json('catalog/atlas-test-problems.json').problems,links=json('catalog/atlas-problem-links.json').problems,refs=json('catalog/atlas-reference-supplements.json').cases,equations=json('catalog/atlas-equations.json').equations;
 for(const id of ids){
  const pid=exp.case_problem_ids[id],link=links.find(x=>x.id===pid),reference=refs.find(x=>x.id===id);
  assert.ok(problems.some(x=>x.id===pid));assert.ok(link?.references.some(x=>x.id===id));assert.ok(reference?.citations.every(x=>x.role&&x.title&&x.url));
  for(const mid of exp.case_equations[id].ids){assert.ok(link.equation_ids.includes(mid));assert.ok(equations.find(x=>x.id===mid).supplemental_examples.includes(id));}
  const html=bytes(`numerical-methods-atlas/validation/${id}/index.html`).toString();
  for(const lang of ['ja','en']){assert.ok(html.includes(`id="${id}-${lang}-measurements"`));assert.equal(reference.view[lang],`/numerical-methods-atlas/validation/${id}/?lang=${lang}#${id}-${lang}-measurements`);}
 }
 for(const id of ['shadow-absorber2d','opposing-beams2d']){
  assert.deepEqual(exp.case_equations[id].ids,['static-grey-transfer','static-grey-m1']);
  assert.equal(refs.find(x=>x.id===id).model,'static-grey-transfer');
  assert.ok(!exp.case_equations[id].ids.includes('m1-radiation'));
 }
 for(const id of ['lbm-cavity-re100','lbm-taylor-green','lbm-annular-couette-control','lbm-cylinder-re20']){
  assert.deepEqual(exp.case_equations[id].ids,['bgk','navier-stokes']);
  assert.equal(refs.find(x=>x.id===id).model,'navier-stokes');
  const entry=json('numerical-methods-atlas/validation/'+id+'/index.json');
  const kernelURL=entry.release.base+'kernel.cpp';
  assert.ok(entry.release.code_urls.includes(kernelURL),id+'/distributed-native-kernel-link');
  assert.ok(bytes('numerical-methods-atlas/validation/'+id+'/index.html').toString().includes('href="'+kernelURL+'"'),id+'/visible-native-kernel-link');
 }
 assert.equal(links.find(x=>x.id==='langevin-harmonic').references.find(x=>x.id==='ou-weak-moments').relation,'related-model');
 const probability=json('catalog/atlas-depth.json').fields.find(x=>x.id==='probability');
 for(const id of ['gbm-weak-moments','ou-weak-moments','gbm-milstein-strong','normal-tail-importance','correlated-gaussian-mcmc'])assert.ok(probability.supplemental_examples.includes(id),id+'/field-entrance');
 const particleGoal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='particle-transport');
 for(const id of ['isotropic-scattering-slab','su-olson-diffusion1996','su-olson-transport1997','shadow-absorber2d','opposing-beams2d'])assert.ok(particleGoal.supplemental_examples.includes(id),id+'/goal-entrance');
});
