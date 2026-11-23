import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const hash=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
const sha=value=>createHash('sha256').update(value).digest('hex');
const cases={ewald:['ewald','ewald-convergence'],pme:['spme','spme-convergence'],spme:['spme','spme-convergence'],pic:['pic','pic-conservation'],dsmc:['dsmc','dsmc-statistics'],'radiation-transport':['radiation-transport','radiation-convergence']};
const originals={ewald:'1d2155b9826e46f4034b346ae2bb0edbc49f59d9359ed0c0615e3315e453fc3f',pme:'c7fbd66a551c580846cbb5d870f2378946061a16991ee53d61d9602a42b49f01',spme:'1a86d3fa9c8aaf65f02c139488423d92983343d7849eaa0570e0d40779cb2cfb',pic:'d0b37b1660d9a2ffd2bd0c6410e42569819da0fb2cfafc0b52421c87cf0ef80d',dsmc:'2389a8fcf48c4a447bbf175b1593998f367d4fd5a9480736e1ae6e8a7cf5aa06','radiation-transport':'b424ceeac166acd845f3951a108610e2ed93a6e043a4598088a282b5d469b50c'};
const added=['ewald-convergence','spme-convergence','fmm-convergence','pic-conservation','dsmc-statistics','radiation-convergence'];
const physical={'ewald-convergence':'neutral-periodic-charges','spme-convergence':'neutral-periodic-charges','fmm-convergence':'logarithmic-particles','pic-conservation':'cold-plasma-pic','dsmc-statistics':'maxwell-collisions','radiation-convergence':'absorbing-slab'};

test('six detailed particle/transport chapters retain all historical paragraphs, equations and source IDs before adding separate releases',()=>{
 const data=json('catalog/atlas-detailed-reading.json');
 for(const [id,supplements] of Object.entries(cases)){
  const chapter=data.chapters.find(x=>x.id===id),old=structuredClone(chapter);
  delete old.scoped_supplements;delete old.publication_scope;
  if(id==='dsmc')old.references=old.references.slice(0,-1);
  for(const section of old.sections)for(const language of ['ja','en'])section.paragraphs[language]=section.paragraphs[language].slice(0,1);
  assert.equal(hash(old),originals[id],id+' historical content preserved');
  assert.deepEqual(chapter.sections.map(x=>x.id),['model','algorithm','conditions','verification']);
  assert.deepEqual(chapter.sections.flatMap(x=>x.formulas||[]),[id+'-1']);
  assert.deepEqual(chapter.scoped_supplements,supplements);
  for(const language of ['ja','en']){
   assert.ok(chapter.publication_scope[language]);
   const document=json(`numerical-methods-atlas/${language}/read/${id}/index.json`);
   assert.deepEqual(document.scoped_supplements.map(x=>x.id),supplements);
   for(const section of chapter.sections)for(const paragraph of section.paragraphs[language])assert.ok(document.html.includes(paragraph.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;')));
   for(const item of document.scoped_supplements)for(const target of [item.url+'?lang='+language,...item.code_urls,...item.test_urls,item.download,item.results,item.verification])assert.ok(document.html.includes(target),id+' '+target);
  }
 }
 const dsmc=data.chapters.find(x=>x.id==='dsmc');
 assert.equal(dsmc.references.at(-1),'scalas2015microcanonical');
 const reference=data.references.find(x=>x.id==='scalas2015microcanonical');
 assert.equal(reference.doi,'10.1103/PhysRevE.92.022140');
 assert.equal(reference.source_review.level,'abstract-and-metadata');
 assert.match(reference.source_review.scope,/derived and checked here/);
 assert.match(reference.source_review.scope,/neither a full-paper audit/);
 assert.match(data.chapters.find(x=>x.id==='pme').sections.at(-1).paragraphs.en.at(-1),/shares real-space\/self terms/);
 assert.match(data.chapters.find(x=>x.id==='pic').sections.find(x=>x.id==='conditions').paragraphs.en.at(-1),/thermal Landau damping/);
 assert.match(dsmc.sections.find(x=>x.id==='conditions').paragraphs.en.at(-1),/without positions/);
});

test('the bounded FMM overlay retains every byte of both historical gravity articles and keeps the 2D logarithmic model separate',()=>{
 const config=json('catalog/atlas-particle-transport-supplements.json');
 const start='<!-- atlas-particle-transport-supplements:start -->',end='<!-- atlas-particle-transport-supplements:end -->';
 const remove=body=>{
  assert.equal(body.split(start).length,2);assert.equal(body.split(end).length,2);
  return body.replace(/<!-- atlas-particle-transport-supplements:start -->[\s\S]*?<!-- atlas-particle-transport-supplements:end -->/,'');
 };
 assert.deepEqual(config.supplemental_examples,['fmm','fmm-convergence']);
 for(const language of ['ja','en']){
  const content=json(`numerical-methods-atlas/content.${language}.json`)['particle-gravity'];
  const page=read(`numerical-methods-atlas/${language}/read/particle-gravity/index.html`);
  const article=page.match(new RegExp(`<article class="prose" lang="${language}">([\\s\\S]*?)</article>`))[1];
  assert.equal(sha(remove(content.html)),config.historical_sha256[language].content);
  assert.equal(sha(remove(article)),config.historical_sha256[language].static_article);
  assert.equal(content.headings.filter(x=>x.id===config.section_id).length,1);
  assert.ok(page.includes(`href="#${config.section_id}"`));
  const supplements=json(`numerical-methods-atlas/${language}/read/particle-gravity/supplements.json`);
  const markdown=read(`numerical-methods-atlas/${language}/read/particle-gravity/supplements.md`);
  assert.deepEqual(supplements.supplements.map(x=>x.id),['fmm','fmm-convergence']);
  for(const item of supplements.supplements){
   assert.equal(item.problem_id,'logarithmic-particles');
   for(const target of [item.url+'?lang='+language,...item.code_urls,...item.test_urls,item.download,item.results,item.verification])for(const output of [content.html,article,markdown])assert.ok(output.includes(target));
  }
 }
 assert.match(config.intro.en,/negative-logarithmic kernel in 2D free space/);
 assert.match(config.comparison_note.en,/No monotonic error with depth/);
 assert.ok(read('scripts/refresh-site.py').includes("'scripts/build-atlas-particle-transport-supplements.py'"));
const python=String.raw`
import importlib.util,sys
sys.path.insert(0,'scripts')
spec=importlib.util.spec_from_file_location('overlay','scripts/build-atlas-particle-transport-supplements.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
config={'historical_sha256':{'en':{'content':module.digest('original')}}}
assert module.historical_body('original',config,'en','content')=='original'
assert module.historical_body('original'+module.START+'new'+module.END,config,'en','content')=='original'
for malformed in ['changed', 'original'+module.START, 'original'+module.START+module.END+module.START+module.END]:
 try:module.historical_body(malformed,config,'en','content')
 except AssertionError:pass
 else:raise AssertionError('historical drift or malformed overlay accepted')
`;
 execFileSync('python3',['-B','-c',python],{cwd:root,encoding:'utf8',timeout:30000});
});

test('one scoped goal and two depth fields expose six new checks without changing gravity, physical counts or reading-only crossover evidence',()=>{
 const goals=json('catalog/atlas-goals.json').goals;
 const goal=goals.find(x=>x.id==='particle-transport');
 assert.deepEqual(goal.methods,['ewald','pme','spme','fmm','pic','dsmc','radiation-transport']);
 assert.deepEqual(goal.examples,[]);
 assert.deepEqual(goal.supplemental_examples,['ewald','spme','fmm','pic','dsmc','radiation-transport',...added]);
 const gravity=goals.find(x=>x.id==='particle-gravity');
 assert.deepEqual(gravity.methods,['barnes-hut','pm']);assert.deepEqual(gravity.examples,['barnes-hut','periodic-particles']);
 assert.equal(gravity.supplemental_examples,undefined);
 const depth=json('catalog/atlas-depth.json').fields;
 assert.deepEqual(depth.find(x=>x.id==='particles').supplemental_examples,['ewald','spme','fmm','pic','dsmc',...added.slice(0,-1)]);
 assert.deepEqual(depth.find(x=>x.id==='transport').supplemental_examples,['radiation-transport','radiation-convergence']);
 const mapping=json('catalog/atlas-depth-expansion.json').case_problem_ids;
 for(const [id,problem] of Object.entries(physical))assert.equal(mapping[id],problem);
 assert.equal(new Set(Object.values(physical)).size,5);
 assert.equal(Object.values(mapping).filter(x=>x===null).length,5);
 const inventory=json('catalog/atlas-test-problems.json').problems;
 assert.equal(inventory.length,85);assert.ok(!inventory.some(x=>added.includes(x.id)));
 const ids=json('catalog/atlas-reading-index.json').groups.find(x=>x.id==='particles-transport').chapters;
 assert.equal(ids[ids.indexOf('validation-particles')+1],'validation-particle-transport');
 assert.equal(ids.filter(x=>x==='validation-particle-transport').length,1);
 const cross=json('catalog/atlas-crossovers.json');
 for(const route of cross.routes){
  assert.equal(route.coupled_validation.status,'not-executed');
  for(const stage of route.stages)assert.ok(!(stage.supplemental_ids||[]).some(x=>added.includes(x)));
  for(const item of [route,...route.connections]){
   assert.ok(!(item.coupled_validation.supplemental_ids||[]).some(x=>added.includes(x)));
  }
  for(const connection of route.connections){
   const historicalStatus={'dft-to-forces':'fixed-input','forces-to-md':'interface-only'}[connection.id]||'not-executed';
   assert.equal(connection.coupled_validation.status,historicalStatus,'preserve existing component evidence without transferring the particle checks');
  }
 }
 const stage=cross.routes.find(x=>x.id==='poisson-fields').stages.find(x=>x.id==='gravitational-field');
 assert.match(stage.gap.en,/does not validate gravity PM/);
 for(const language of ['ja','en'])assert.ok(stage.reading.some(x=>x.url[language]===`/numerical-methods-atlas/${language}/read/validation-particle-transport/`));
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(methods.length,147);assert.equal(methods.filter(x=>x.status==='educational-example').length,117);
});

test('all 80 historical gallery illustrations, image checksums and captions survive the new supplemental evidence',()=>{
 const items=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(x=>!['noh','sedov','double-mach','forward-step','isentropic-vortex'].includes(x.id));
 assert.equal(items.length,80);
 assert.equal(hash(items.map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}))),'25c25a4cb7ad5c54e5788b984d949c44994d3f1706ed36c4ef30a3ce36fa6c2b');
 const gallery=json('numerical-methods-atlas/gallery/index.json');
 assert.equal(gallery.items.length,85);assert.equal(gallery.items.filter(x=>x.runnable).length,44);
});
