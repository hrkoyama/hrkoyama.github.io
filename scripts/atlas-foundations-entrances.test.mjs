import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const hash=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
const cases={amg:['sa-amg','amg-conditioning'],'qr-svd':['qr-svd-factorization','qr-svd-conditioning'],eigensolvers:['krylov-eigenvalues','krylov-eigen-conditioning'],quadrature:['gauss-adaptive-quadrature','quadrature-conditioning']};
const originals={amg:['8f75af0e84c7d4a092244152b4148404b59e81c63d05d8a11973011791067b5e',1],'qr-svd':['3ad80bb9c1348d4c0378e54a5367fd9eb9ad55cdb5477423270af8e2f69f19a3',2],eigensolvers:['7a8068607dc3046a6cf66ff05a94455beb96b82ff84e5494b9b6b1cbdef2a5a5',2],quadrature:['85e46d38af5e4e18e043fbf73acdba4cf18d0addccb438d2a2752109a0701fb3',2]};

test('four canonical chapters preserve every historical section, formula, source and paragraph before adding separate conditioning releases',()=>{
 const data=json('catalog/atlas-detailed-reading.json');
 for(const [id,supplements] of Object.entries(cases)){
  const chapter=data.chapters.find(x=>x.id===id),old=structuredClone(chapter);
  delete old.scoped_supplements;delete old.publication_scope;
  old.references=old.references.slice(0,originals[id][1]);
  for(const section of old.sections)for(const lang of ['ja','en'])section.paragraphs[lang]=section.paragraphs[lang].slice(0,1);
  assert.equal(hash(old),originals[id][0],id+' retains its pre-addition scientific content and source IDs');
  assert.deepEqual(chapter.sections.map(x=>x.id),['model','algorithm','conditions','verification']);
  assert.deepEqual(chapter.scoped_supplements,supplements);
  assert.deepEqual(chapter.sections.flatMap(x=>x.formulas||[]),[id==='eigensolvers'?'eigensolvers-1':id+'-1']);
  for(const lang of ['ja','en']){
   assert.ok(chapter.publication_scope[lang]);
   assert.ok(chapter.sections.find(x=>x.id==='conditions').paragraphs[lang].length>1);
   assert.ok(chapter.sections.find(x=>x.id==='verification').paragraphs[lang].length>1);
  }
 }
 const references=new Map(data.references.map(x=>[x.id,x]));
 for(const id of ['vanek2001','demmel-veselic1992','lapack-ls-error','lapack-eigen-error','gonnet2010']){
  const reference=references.get(id);assert.ok(reference?.source_review.scope_ja);assert.ok(reference.source_review.scope);
  assert.ok(['metadata','abstract-and-metadata','full-text'].includes(reference.source_review.level));
 }
 for(const id of ['lapack-ls-error','lapack-eigen-error']){assert.equal(references.get(id).type,'misc');assert.equal(references.get(id).doi,undefined);}
 assert.match(data.chapters.find(x=>x.id==='amg').sections.at(-1).paragraphs.en.at(-1),/does not establish mesh convergence/);
 assert.match(data.chapters.find(x=>x.id==='eigensolvers').sections.at(-1).paragraphs.en.at(-1),/Passing a residual check alone/);
});

test('AMG algebraic diagnostics remain outside physical counts and the Poisson goal retains its original PDE example',()=>{
 const config=json('catalog/atlas-depth-expansion.json');
 assert.equal(config.case_problem_ids['amg-conditioning'],null);
 const goal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='poisson');
 assert.deepEqual(goal.supplemental_examples,['sa-amg']);
 assert.deepEqual(goal.examples,['poisson-1d-dirichlet','poisson-2d-sine']);
 const note=goal.resources.find(x=>x.id==='amg-conditioning-reading');
 assert.equal(note.status,'reading-only');assert.deepEqual(note.code_urls,[]);assert.deepEqual(note.test_urls,[]);assert.deepEqual(note.execution_examples,[]);
 for(const lang of ['ja','en'])assert.equal(note.reading[lang],`/numerical-methods-atlas/${lang}/read/validation-foundations-conditioning/#amg-conditioning`);
 const depth=json('catalog/atlas-depth.json').fields.find(x=>x.id==='foundations');
 assert.deepEqual(depth.supplemental_examples,[...Object.values(cases).map(x=>x[0]),...Object.values(cases).map(x=>x[1])]);
 const problemCatalog=json('catalog/atlas-test-problems.json');
 assert.match(problemCatalog.excluded_examples.en.at(-1),/amg-conditioning/);
 const inventory=problemCatalog.problems;
 assert.equal(inventory.length,87);assert.ok(!inventory.some(x=>x.id==='amg-conditioning'));
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(methods.length,147);assert.equal(methods.filter(x=>x.status==='educational-example').length,117);
});

test('conditioning readings enter contents and crossovers without borrowing evidence for coupled applications',()=>{
 const ids=json('catalog/atlas-reading-index.json').groups.find(x=>x.id==='linear-approximation').chapters;
 assert.equal(ids[ids.indexOf('validation-foundations')+1],'validation-foundations-conditioning');
 assert.equal(ids.filter(x=>x==='validation-foundations-conditioning').length,1);
 const cross=json('catalog/atlas-crossovers.json');
 for(const [family,chapter] of [['elliptic-solves','amg'],['stability-spectrum','eigensolvers']])for(const lang of ['ja','en'])assert.ok(cross.math_families.find(x=>x.id===family).reading.some(x=>x.url[lang]===`/numerical-methods-atlas/${lang}/read/${chapter}/#scoped-examples`));
 const added=Object.values(cases).map(x=>x[1]);
 for(const route of cross.routes){
  for(const stage of route.stages)assert.ok(!(stage.supplemental_ids||[]).some(x=>added.includes(x)));
  for(const item of [route,...route.connections])assert.ok(!(item.coupled_validation.supplemental_ids||[]).some(x=>added.includes(x)));
 }
});

test('the shared scoped renderer labels algebraic diagnostics without MCMC-specific generic claims',()=>{
 const source=String.raw`
import ast,html,pathlib
source=pathlib.Path('scripts/build-atlas-detailed-reading.py').read_text();tree=ast.parse(source)
names={'link','heading','paragraph','scoped_supplement_html','scoped_supplement_markdown'}
functions=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names]
scope={'escape':html.escape};exec(compile(ast.Module(body=functions,type_ignores=[]),'scoped-reading-renderer','exec'),scope)
case={'id':'amg-conditioning','problem_id':None,'title':{'ja':'AMG条件数','en':'AMG conditioning'},'summary':{'ja':'代数的対照','en':'Algebraic control'},'limits':{'ja':'PDE格子収束は対象外','en':'No PDE mesh convergence'},'url':'/numerical-methods-atlas/validation/amg-conditioning/','reading':{lang:'/numerical-methods-atlas/'+lang+'/read/validation-foundations-conditioning/#amg-conditioning' for lang in ['ja','en']},'code_urls':['/code/condition.py'],'test_urls':['/code/test_condition.py'],'download':'/code/condition.zip','results':'/code/result.json','verification':'/code/verification.json'}
for lang in ['ja','en']:
 html=scope['scoped_supplement_html']([case],lang);md=scope['scoped_supplement_markdown']([case],lang)
 assert ('物理問題数へ非加算' if lang=='ja' else 'no additional physical problem') in html
 assert ('物理問題数へ非加算' if lang=='ja' else 'no physical-problem increment') in md
 assert ('一般保証' if lang=='ja' else 'general mathematical guarantee') in html
 assert 'mixing' not in html and 'mixing' not in md and '混合' not in html and '混合' not in md
 for target in [case['url']+'?lang='+lang,case['reading'][lang],*case['code_urls'],*case['test_urls'],case['download'],case['results'],case['verification']]:assert target in html and target in md
`;
 execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8',timeout:30000});
});

test('all 80 historical illustrations, checksums and captions remain unchanged',()=>{
 const items=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(x=>!['noh','sedov','double-mach','forward-step','isentropic-vortex','guderley','zalesak'].includes(x.id));
 assert.equal(items.length,80);
 assert.equal(hash(items.map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}))),'25c25a4cb7ad5c54e5788b984d949c44994d3f1706ed36c4ef30a3ce36fa6c2b');
});
