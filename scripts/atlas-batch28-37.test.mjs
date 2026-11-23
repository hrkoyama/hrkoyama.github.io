import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
const root=fileURLToPath(new URL('../',import.meta.url));
const bytes=p=>readFileSync(join(root,p));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const baseline=json('scripts/fixtures/atlas-batch28-37-baseline.json');
const concurrent=json('scripts/fixtures/atlas-batch28-37-concurrent.json');
const expected={
 'coefficient-diffusion':['checkerboard-diffusion','rotated-anisotropic-diffusion'],
 'slab-ewald':['neutral-slab-yb'],
 'fmm3d':['fmm3d-inverse-r'],
 'gravity-dynamics':['gravity-kepler','gravity-plummer-short'],
 'warm-pic':['thermal-landau-damping','thermal-two-stream'],
 'pic-spatial':['pic-independent-spatial'],
 'dsmc-wall':['dsmc-couette','dsmc-fourier'],
 'dsmc-shock':['dsmc-planar-shock'],
};
const newIds=Object.values(expected).flat();

test('concurrent compact search details and scoped HF/KS notes survive integration',()=>{
 for(const p of concurrent.immutable_content_addressed_details)assert.equal(sha(p),p.split('/').at(-1).slice(0,-5),p);
 const equations=json('catalog/atlas-equations.json').equations;
 for(const [id,note] of Object.entries(concurrent.scoped_equation_notes))assert.deepEqual(equations.find(x=>x.id===id).note,note,id);
});

test('packager preserves native SPARTA text only in its reference-input subtree',()=>{
 execFileSync('python3',['-B','-c',String.raw`
import importlib.util
from pathlib import Path
p=Path('scripts/package-depth-examples.py')
s=importlib.util.spec_from_file_location('packager',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
for path in ['pytest.ini','references/native-inputs/case/base/seed/input.sparta','references/native-inputs/case/base/seed/hs.species','references/native-inputs/case/base/seed/hs.vss']:
 assert m.source_member_allowed(path),path
for path in ['random.sparta','random.species','references/other/hs.vss','spa_mac','binary.exe','source.tar.gz']:
 assert not m.source_member_allowed(path),path
`],{cwd:root,timeout:30_000});
});

test('reference rendering accepts titled official sources without inventing author metadata',()=>{
 execFileSync('python3',['-B','-c',String.raw`
import importlib.util,sys
sys.path.insert(0,'scripts')
s=importlib.util.spec_from_file_location('builder','scripts/build-atlas-depth-examples.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
c={'references':[{'id':'official-doc','title':'Official formulation','url':'https://example.org/formulation','review_level':'selected-official','review_scope':'Selected derivation only; no solver run.'}]}
html=m.reference_html(c,'ja','fixture')
assert m.reference_label(c['references'][0])=='Official formulation'
assert 'Official formulation' in html and 'Selected derivation only; no solver run.' in html
assert 'None' not in html
`],{cwd:root,timeout:30_000});
});

test('batch28–37 preserves every prior scientific distribution and reference identity',()=>{
 for(const [p,h] of Object.entries(baseline.immutable_files)) assert.equal(sha(p),h,p);
 const methods=json('catalog/atlas-methods.json').methods;
 for(const [id,status] of Object.entries(baseline.method_statuses)) assert.equal(methods.find(x=>x.id===id)?.status,id==='slab-ewald'?'educational-example':status,id);
 assert.equal(baseline.method_statuses['slab-ewald'],'planned');
 assert.deepEqual(methods.find(x=>x.id==='slab-ewald').depth_release,{group:'slab-ewald',edition:'2026-11-23',case_ids:['neutral-slab-yb']});
 for(const [id,fields] of Object.entries(baseline.method_scientific_fields)){
  const current=methods.find(x=>x.id===id);for(const [key,value] of Object.entries(fields))assert.deepEqual(current[key],value,id+'/'+key);
 }
 for(const [id,references] of Object.entries(baseline.method_reference_fields))assert.deepEqual(methods.find(x=>x.id===id).references,references,id+'/references');
 const q1=methods.find(x=>x.id==='q1-fem');assert.match(q1.name.en,/scalar diffusion/);assert.match(q1.code_mapping_scope,/scalar full-tensor/);
 const equations=json('catalog/atlas-equations.json').equations;
 for(const [id,formula] of Object.entries(baseline.equation_formulas)) assert.deepEqual(equations.find(x=>x.id===id)?.formula,formula,id);
 const refs=json('catalog/atlas-reference-supplements.json').cases;
 for(const old of baseline.reference_supplements) assert.deepEqual(refs.find(x=>x.id===old.id),old,old.id);
});

test('batch28–37 preserves all primary gallery records and prior release metadata',()=>{
 const gallery=json('catalog/atlas-gallery.json').items;
 for(const old of baseline.gallery_items) assert.deepEqual(gallery.find(x=>x.id===old.id),old,old.id);
 const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const old of baseline.preview_manifest_items) assert.deepEqual(previews.find(x=>x.id===old.id),old,old.id);
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.deepEqual(registry.releases.filter(x=>!Object.hasOwn(expected,x.group)),baseline.release_registry.releases);
 assert.equal(registry.case_count,baseline.release_registry.case_count+newIds.length);
 assert.deepEqual(registry.releases.filter(x=>Object.hasOwn(expected,x.group)).map(x=>x.group),Object.keys(expected));
});

test('new fixed-input packets expose verified booleans, finite CSV and reviewed source contracts',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 for(const [group,ids] of Object.entries(expected)){
  const release=registry.releases.find(x=>x.group===group);assert.ok(release,group);
  assert.deepEqual([...release.case_ids].sort(),[...ids].sort());
  const base=`code/validated-examples/${release.edition}/${group}/`;
  const result=json(base+'results/result.json');const verification=json(base+'verification.json');
  assert.equal(verification.passed,true);assert.equal(verification.all_cases_rerun,true);assert.equal(verification.failures,0);assert.equal(verification.errors,0);assert.equal(verification.skipped,0);
  assert.equal(result.passed,true);assert.equal(result.input_sha256,sha(base+'inputs.json'));
  assert.deepEqual(Object.keys(result.checks).sort(),[...ids].sort());assert.ok(Object.values(result.checks).every(x=>x===true));
  for(const c of result.cases){assert.equal(c.passed,true);assert.ok(c.records.length);assert.ok(Object.keys(c.checks).length);assert.ok(Object.values(c.checks).every(x=>x===true));}
  const manifest=json(base+'source-manifest.json');
  for(const id of ids){assert.ok(Object.keys(manifest.files).some(p=>p.startsWith(`results/${id}`)&&p.endsWith('.csv')),id);assert.ok(manifest.files[`results/${id}.png`],id);assert.ok(manifest.files[`results/${id}-preview.png`],id);}
  assert.ok(manifest.files['pre-run-contract.json']);assert.ok(manifest.files['acceptance.json']);
  for(const key of ['archive','manifest','verification','requirements']){
   const file=key==='archive'?release.archive:key==='manifest'?'source-manifest.json':key==='verification'?'verification.json':'requirements.txt';assert.equal(sha(base+file),release[key+'_sha256']);
  }
 }
});

test('each new case connects equations, methods, reference, gallery and bilingual executable pages',()=>{
 const galleryHtml=bytes('numerical-methods-atlas/gallery/index.html').toString();
 const expansion=json('catalog/atlas-depth-expansion.json');const refs=json('catalog/atlas-reference-supplements.json').cases;const problems=json('catalog/atlas-test-problems.json').problems;const links=json('catalog/atlas-problem-links.json').problems;const gallery=json('catalog/atlas-gallery.json').items;const equations=json('catalog/atlas-equations.json').equations;
 for(const id of newIds){
  const pid=expansion.case_problem_ids[id];assert.ok(problems.some(x=>x.id===pid),id);assert.ok(gallery.some(x=>x.id===pid),id);
  if(pid===id)for(const lang of ['ja','en']){const tile=galleryHtml.match(new RegExp(`<li class="gallery-tile" id="${id}-${lang}"[\\s\\S]*?</li>`))?.[0];assert.ok(tile,id+'/'+lang);assert.equal((tile.match(/<img /g)||[]).length,1,id+'/'+lang+'/one-primary-preview');assert.ok(tile.includes(`data-supplemental-execution="${id}"`),id);}
  const link=links.find(x=>x.id===pid);assert.ok(link.references.some(x=>x.id===id),id);
  const reference=refs.find(x=>x.id===id);assert.ok(reference,id);assert.ok(reference.citations.every(x=>x.role&&x.title&&x.url));
  if(['neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short'].includes(id))assert.equal(reference.dimension,3,id);
  for(const model of expansion.case_equations[id].ids){assert.ok(link.equation_ids.includes(model));assert.ok(equations.find(x=>x.id===model).supplemental_examples.includes(id));}
  const html=bytes(`numerical-methods-atlas/validation/${id}/index.html`).toString();
  for(const lang of ['ja','en']){assert.ok(html.includes(`id="${id}-${lang}-measurements"`),id+'/'+lang);assert.equal(reference.view[lang],`/numerical-methods-atlas/validation/${id}/?lang=${lang}#${id}-${lang}-measurements`);assert.ok(reference.reading[lang]);}
 }
});

test('Thomas curation separates unread original, archival finding aid and related chapter references',()=>{
 const c=json('numerical-methods-atlas/reading/thomas-provenance.json');assert.equal(c.sequence,29);assert.equal(c.new_scientific_cases,0);assert.equal(c.original_full_text_read,false);assert.equal(c.original.year,1949);assert.equal(c.original.doi,null);assert.equal(c.original.report_number,null);
 assert.ok(c.references.some(x=>x.role==='archival-finding-aid'));assert.ok(c.references.some(x=>x.role==='signed-historical-correspondence'));
 assert.ok(c.chapter_context_roles.some(x=>x.role==='Crank-Nicolson-reprint-not-Thomas'&&x.url.endsWith('BF02127704')));
 const method=json('catalog/atlas-methods.json').methods.find(x=>x.id==='thomas');assert.equal(method.status,baseline.method_statuses.thomas);assert.equal(method.bibliographic_original.review_level,'original-unread-secondary-bibliographic-lead');
});
