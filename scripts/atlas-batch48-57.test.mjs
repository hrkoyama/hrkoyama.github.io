import {projectCatalogBeforeFinal23} from './fixtures/atlas-final23-projection.mjs';
import {projectMethodBeforeBatch68} from './fixtures/atlas-inventory.mjs';
// DRAFT: install in scripts/ only after canonical packages/catalogs are ready.
// Data/hash checks only: no solver, renderer, network call or ZIP extraction.
import test from 'node:test';
import assert from 'node:assert/strict';
import {createReadStream,readFileSync,statSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
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
const baseline=json('scripts/fixtures/atlas-batch48-57-baseline.json');
const expected=baseline.expected_new_groups,newGroups=Object.keys(expected);
const newIDs=Object.values(expected).flat();
const releaseBase=release=>`code/validated-examples/${release.edition}/${release.group}/`;
const sorted=value=>[...value].sort();
// This regression owns the historical cohort through batch57. Later batches
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
function oldMethodPointer(row){
 const e=baseline.current_edition_exception;
 if(row.group===e.group&&row.edition===e.new_edition){
  assert.ok(row.case_ids.every(id=>e.case_ids.includes(id)));
  return {...row,edition:e.old_edition};
 }
 return row;
}
function finite(value){
 if(typeof value==='number')assert.ok(Number.isFinite(value));
 else if(Array.isArray(value))value.forEach(finite);
 else if(value&&typeof value==='object')Object.values(value).forEach(finite);
}

test('batch48–57 preserves all 47 earlier immutable editions and every existing primary image',async()=>{
 assert.deepEqual(baseline.baseline_counts,{groups:47,cases:97,pytest:1244,methods:152});
 const registry=current();
 assert.deepEqual(registry.releases.filter(row=>!newGroups.includes(row.group)).map(row=>row.group),baseline.release_order);
 for(const before of baseline.releases){
  // This includes the old Nov23 MHD archive even when its active pointer advances.
  for(const [path,hash] of Object.entries(before.immutable_files))assert.equal(await streamSHA(path),hash,path);
  const active=registry.releases.find(row=>row.group===before.release.group);assert.ok(active);
  if(active.group!==baseline.current_edition_exception.group)assert.deepEqual(active,before.release);
 }
 const gallery=projectCatalogBeforeFinal23('catalog/atlas-gallery.json',json('catalog/atlas-gallery.json')).items,previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const [id,hash] of Object.entries(baseline.gallery_records_sha256))assert.equal(fingerprint(gallery.find(row=>row.id===id)),hash,id+'/old-gallery-record');
 for(const [id,hash] of Object.entries(baseline.preview_records_sha256))assert.equal(fingerprint(previews.find(row=>row.id===id)),hash,id+'/old-preview-record');
 for(const [path,hash] of Object.entries(baseline.preview_images_sha256))assert.equal(await streamSHA(path),hash,path+'/old-image');
});

test('all 152 existing method science and formula goldens remain, with exactly six separately scoped methods',()=>{
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

test('five new groups expose nine fully verified cases and registry-derived test counts',async()=>{
 const registry=current();
 assert.deepEqual(sorted(registry.releases.filter(row=>!baseline.release_order.includes(row.group)).map(row=>row.group)),sorted(newGroups));
 assert.equal(newIDs.length,9);assert.equal(registry.releases.length,baseline.baseline_counts.groups+newGroups.length);
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
  if(group==='linear-algebra-spectral'){
   // Regression for the retained canonical failure: summaries must contain
   // actual measured values, not an empty dictionary or a dummy passed flag.
   const fields={
    'pivoted-direct-refinement':{max_relative_forward_error:'relative_forward_error',max_normwise_backward_error:'final_backward'},
    'symmetric-saddle-minres':{max_original_relative_residual:'true_relative_residual',max_relative_reference_error:'reference_error'},
    'restarted-shift-invert':{max_original_eigenpair_residual:'true_normalized_residual',max_operator_calls:'operator_calls'},
    'fem-mass-eigen':{max_generalized_residual:'true_relative_residual',max_M_orthogonality_defect:'M_orthogonality'},
   };
   for(const c of result.cases)for(const [metric,field] of Object.entries(fields[c.id])){
    assert.equal(typeof c.metrics[metric],'number');
    assert.equal(c.metrics[metric],Math.max(...c.records.map(row=>row[field])),c.id+'/'+metric+'/measured-record-summary');
   }
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

test('algebraic references keep null spatial dimensions while the string and Maxwell fields stay physical',()=>{
 const refs=json('catalog/atlas-reference-supplements.json').cases,solutions=json('numerical-methods-atlas/solutions/index.json').cases;
 const algebra={
  'pivoted-direct-refinement':'finite-dimensional-linear-system',
  'symmetric-saddle-minres':'finite-dimensional-linear-system',
  'restarted-shift-invert':'finite-dimensional-eigenproblem',
 };
 for(const [id,model] of Object.entries(algebra))for(const rows of [refs,solutions]){
  const row=rows.find(value=>value.id===id);assert.ok(row);assert.equal(row.model,model);
  assert.equal(row.domain_kind,'finite-dimensional-algebra');assert.equal(row.dimension,null);assert.deepEqual(row.bounds,[]);
 }
 const string=refs.find(row=>row.id==='fem-mass-eigen');assert.equal(string.model,'dirichlet-string-eigenproblem');assert.equal(string.dimension,1);assert.deepEqual(string.bounds,[[0,1]]);
 assert.equal(refs.find(row=>row.id==='cylinder-mie2d').model,'maxwell');
 for(const id of ['lorentz-oblique-sp','dispersive-grazing-pml'])assert.equal(refs.find(row=>row.id===id).model,'maxwell-lorentz');
 const exp=json('catalog/atlas-depth-expansion.json');
 for(const id of ['bratu-fold-continuation','bratu-matrix-free-jfnk'])assert.deepEqual(exp.case_equations[id].ids,['bratu']);
 // Existing atlas-solutions tests separately exercise all old 1D/2D/3D labels
 // and reject untagged/null/zero/bool dimensions. Do not duplicate the builder.
});

test('citation item 55 appends selected original-reading scope without inventing a tenth numerical case',()=>{
 const refs=json('catalog/atlas-method-primary-references.json').references;
 for(const [id,old] of Object.entries(baseline.citation55)){
  const row=refs.find(value=>value.id===id);assert.equal(fingerprint(pick(row,old.identity_keys)),old.identity_sha256,id+'/old-bibliographic-identity');
  assert.deepEqual(row.bibliographic_review,old.previous_source_review,id+'/prior-metadata-review');
  assert.equal(row.source_review.level,'full-text');assert.match(row.source_review.scope,/selected/i);
 }
 const arnoldi=refs.find(row=>row.id==='arnoldi1951').source_review;
 assert.match(arnoldi.representation,/OCR/);assert.match(arnoldi.representation,/unverified/i);
 assert.match(arnoldi.scope,/25.?26/);assert.match(arnoldi.scope,/28.?29/);assert.match(arnoldi.scope,/403/);assert.match(arnoldi.scope,/unverified/i);
 const lanczos=refs.find(row=>row.id==='lanczos1950').source_review;
 assert.match(lanczos.representation,/selected.*visually/i);assert.match(lanczos.scope,/266.?267/);assert.match(lanczos.scope,/271/);assert.match(lanczos.scope,/unnormalized/i);
 assert.equal(newIDs.length,9);assert.ok(!newIDs.some(id=>/arnoldi1951|lanczos1950|citation55/.test(id)));
});

test('only active MHD moves to November 24, retaining old November 23 bytes, inputs, criteria and all check identities',()=>{
 const before=baseline.releases.find(row=>row.release.group==='mhd-transport'),e=baseline.current_edition_exception;
 const release=current().releases.find(row=>row.group===e.group);assert.equal(release.edition,e.new_edition);
 assert.deepEqual(release.case_ids,before.release.case_ids);assert.equal(release.tests,before.release.tests);
 const base=releaseBase(release),manifest=json(base+'source-manifest.json'),result=json(base+'results/result.json'),v=json(base+'verification.json');
 assert.equal(sha(base+'inputs.json'),before.immutable_files[before.base+'inputs.json']);
 if(before.acceptance_file)assert.equal(sha(base+'acceptance.json'),before.immutable_files[before.acceptance_file]);
 assert.equal(result.passed,true);assert.equal(v.passed,true);assert.equal(v.passed_tests,47);
 for(const c of result.cases){assert.equal(fingerprint(sorted(Object.keys(c.checks))),before.case_check_key_hashes[c.id]);assert.ok(Object.values(c.checks).every(value=>value===true));}
 assert.equal(manifest.version,e.new_edition);assert.equal(sha(base+'source-manifest.json'),release.manifest_sha256);
});

// Document consultation/version dates are not inferred publication years.
test('official document dates distinguish access, version release and publication',()=>{
 const refs=current().releases.filter(row=>row.group.startsWith('maxwell-')).flatMap(row=>json(releaseBase(row)+'cases.json').flatMap(c=>[...c.references,...c.citations]));
 const undated=refs.filter(row=>['ansys-cylinder','meep-materials'].includes(row.id));assert.ok(undated.length);
 for(const r of undated){assert.equal(Object.hasOwn(r,'year'),false);assert.equal(r.accessed_on,'2026-11-24');}
 const nist=refs.filter(row=>row.id==='nist-wronskian');assert.ok(nist.length);
 for(const r of nist){assert.equal(r.year_role,'version');assert.equal(r.version,'1.2.8');assert.equal(r.release_date,'2026-09-15');assert.equal(r.accessed_on,'2026-11-24');}
 for(const r of refs.filter(row=>row.id==='johnson-pml'))assert.equal(r.year,2021);
 execFileSync('python3',['-B','-c',String.raw`
import ast
from pathlib import Path
a=ast.parse(Path('scripts/build-atlas-depth-examples.py').read_text())
f=next(n for n in a.body if isinstance(n,ast.FunctionDef) and n.name=='reference_label')
ns={};exec(compile(ast.Module(body=[f],type_ignores=[]),'reference-label-only','exec'),ns)
label=ns['reference_label']
assert label({'title':'Official formulation'})=='Official formulation'
unknown=label({'author':'Official author','title':'Undated documentation','accessed_on':'2026-11-24'})
assert '(n.d.)' in unknown and '[accessed 2026-11-24]' in unknown and '(2026)' not in unknown
version=label({'author':'NIST DLMF','title':'Identity','year':2026,'year_role':'version','version':'1.2.8','release_date':'2026-09-15','accessed_on':'2026-11-24'})
assert 'version 1.2.8, released 2026-09-15' in version and '[accessed 2026-11-24]' in version
assert label({'author':'Original author','title':'Paper','year':2021})=='Original author (2021). Paper'
`],{cwd:root,timeout:10_000});
});

test('coverage retains legacy scopes and uses only the exact primary supplemental profile',()=>{
 execFileSync('python3',['-B','-c',String.raw`
import ast,copy,json
from pathlib import Path
a=ast.parse(Path('scripts/atlas_method_scope.py').read_text())
f=next(n for n in a.body if isinstance(n,ast.FunctionDef) and n.name=='depth_coverage_scope')
ns={};exec(compile(ast.Module(body=[f],type_ignores=[]),'coverage-scope-only','exec'),ns);scope=ns['depth_coverage_scope']
methods=json.loads(Path('catalog/atlas-methods.json').read_text())['methods'];fallback=[]
for m in methods:
 if not m.get('depth_release'):continue
 for lang in ('ja','en'):
  value=scope(m,lang)
  if 'depth_scope' in m:assert value==m['depth_scope'][lang]
  else:
   matched=[p for p in m['supplemental_scope_profiles'] if p['release']==m['depth_release']];assert len(matched)==1
   assert value.startswith(matched[0]['scope'][lang]) and all(p[lang] in value for p in matched[0]['limits'])
 if 'depth_scope' not in m:fallback.append(m['id'])
legacy_fallback={'leapfrog','thomas','gmres','newton','fdtd','optimization','adjoint','automatic-differentiation'}
# Dated68 extension: four new methods plus four first primary-release bindings.
cohort=json.loads(Path('scripts/fixtures/atlas-batch68-77-baseline.json').read_text())
transition=json.loads(Path('scripts/fixtures/atlas-batch68-77-method-transition.json').read_text())
added68=set(cohort['expected_new_method_ids'])|{ident for ident,change in transition['transitions'].items() if 'depth_release' in change['before_absent'] and 'depth_release' in change['after']}
assert added68=={'bdf2','sdirk2','step-doubling','dae','rk45','jameson-steady-rk','shake','rattle'}
added23={'schrodinger','hartree-fock','kohn-sham-dft','scf','pseudopotentials'}
delta23=json.loads(Path('scripts/fixtures/atlas-final23-metadata-delta.json').read_text())
assert set(fallback)-added23==legacy_fallback|added68
assert set(fallback)&added23==added23
for ident in added23:
 assert 'depth_release' not in delta23['methods'][ident]['delta']['keys'], ident
 method=next(m for m in methods if m['id']==ident)
 assert method['depth_release']['group']=='quantum-small' and method['depth_release']['edition']=='2026-11-25'
 assert method['depth_release']['case_ids']
release={'group':'one','edition':'2026-11-24','case_ids':['fixed']}
profile={'release':release,'scope':{'ja':'固定例のみ。','en':'Fixed case only.'},'limits':[{'ja':'一般保証なし。','en':'No general guarantee.'}]}
other={'release':{**release,'group':'other'},'scope':{'ja':'別の例。','en':'UNRELATED RELEASE'},'limits':profile['limits']}
m={'depth_release':release,'supplemental_scope_profiles':[profile,other],'summary':{'en':'UNQUALIFIED GLOBAL SUMMARY'}}
assert scope(m,'en')=='Fixed case only. No general guarantee.'
for variant in [dict(m,supplemental_scope_profiles=[]),dict(m,supplemental_scope_profiles=[profile,profile]),dict(m,supplemental_scope_profiles=[other]),dict(m,supplemental_scope_profiles=[{**profile,'limits':[]}]),dict(m,supplemental_scope_profiles=[{**profile,'scope':{'en':'Missing Japanese'}}]),dict(m,depth_scope={})]:
 try:scope(variant,'en')
 except ValueError:pass
 else:raise AssertionError('Missing, duplicate or malformed primary scope was accepted')
`],{cwd:root,timeout:10_000});
});

test('six new method records retain the existing bilingual field types and rendered text',()=>{
 const rows=json('catalog/atlas-methods.json').methods;
 const escape=value=>value.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
 for(const id of baseline.expected_new_method_ids){
  const row=rows.find(m=>m.id===id),rendered=json(`numerical-methods-atlas/methods/${id}/index.json`);
  for(const key of ['assumptions','assumptions_ja']){assert.ok(Array.isArray(row[key])&&row[key].length&&row[key].every(v=>typeof v==='string'&&v.trim()));assert.deepEqual(rendered[key],row[key]);}
  for(const key of ['units','units_ja','boundary_conditions','boundary_conditions_ja']){assert.equal(typeof row[key],'string');assert.ok(row[key].trim());assert.equal(rendered[key],row[key]);}
  const html=bytes(`numerical-methods-atlas/methods/${id}/index.html`).toString();
  for(const value of [...row.assumptions,...row.assumptions_ja,row.units,row.units_ja,row.boundary_conditions,row.boundary_conditions_ja])assert.ok(html.includes(escape(value)),id+'/bilingual-condition-display');
 }
});

test('the verified author document is an external citation while hidden completion paths stay blocked',()=>{
 execFileSync('python3',['-B','-c',String.raw`
import ast,json,re
from pathlib import Path
from urllib.parse import urlsplit,unquote
a=ast.parse(Path('scripts/build-atlas-benchmark-backlog.py').read_text())
selected=[n for n in a.body if isinstance(n,ast.FunctionDef) and n.name=='checked_url' or isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PUBLIC_EXTERNAL_DOT_DOCUMENTS' for t in n.targets)]
ns={'re':re,'urlsplit':urlsplit,'unquote':unquote,'ORIGIN':'https://hrkoyama.github.io'}
exec(compile(ast.Module(body=selected,type_ignores=[]),'backlog-url-only','exec'),ns);check=ns['checked_url']
u='https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html'
assert check(u).netloc=='hplgit.github.io' and check(u+'#problem-8').fragment=='problem-8'
for value,same in [(u,True),(u+'?redirect=elsewhere',False),('https://hplgit.github.io.attacker.invalid/INF5620/doc/pub/._main_nonlin005.html',False),('https://hplgit.github.io/INF5620/doc/pub/%2e_main_nonlin005.html',False),('https://hplgit.github.io/other/.private',False),('/.git/config',True),('/code/%2e%2e/private',True),('/code/.hidden.json',False),('https://hrkoyama.github.io/INF5620/doc/pub/._main_nonlin005.html',False)]:
 try:check(value,same_site=same)
 except ValueError:pass
 else:raise AssertionError('Unsafe or unverified URL accepted: '+value)
assert check('/code/public.json',same_site=True).netloc=='hrkoyama.github.io'
for item in json.loads(Path('catalog/atlas-benchmark-backlog.json').read_text())['items']:
 for source in item.get('sources',[]):check(source['url'])
`],{cwd:root,timeout:10_000});
});
