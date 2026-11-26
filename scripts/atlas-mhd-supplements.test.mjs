import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const added=['ct-glm-smooth-convergence','ct-glm-ot-convergence','ct-glm-constraint-control'];
const anchors=['problem-and-units','ct-share-the-same-edge-electric-field','glm-transport-and-damp-divergence-errors','measuring-b','verification-scope','time-evolution','hlld-and-standard-wave-tests','ct-contact-and-glm-scope-in-the-loop-test'];

test('the MHD overlay preserves the historical article and refuses malformed or unreviewed replacements',()=>{
 const source=String.raw`
import importlib.util,json,pathlib,re,sys
sys.path.insert(0,'scripts')
from atlas_reading_presentation import original_reading_document
spec=importlib.util.spec_from_file_location('mhd_supplements','scripts/build-atlas-mhd-supplements.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
config=json.loads(pathlib.Path('catalog/atlas-mhd-supplements.json').read_text())
for lang in ['ja','en']:
 document=json.loads(pathlib.Path('numerical-methods-atlas/content.'+lang+'.json').read_text())['mhd']
 static=original_reading_document(pathlib.Path('numerical-methods-atlas/'+lang+'/read/mhd/index.html').read_text())[0]
 article=re.findall('<article class="prose" lang="'+lang+'">(.*?)</article>',static,re.S)
 # Keep the historical outer article unambiguous.
 assert len(article)==1
 for body,kind in [(document['html'],'content'),(article[0],'static_article')]:
  original=m.historical_body(body,config,lang,kind)
  overlay=m.START+'<section>bounded overlay</section>'+m.END
  once=m.updated_body(original,overlay,config,lang,kind)
  assert m.updated_body(once,overlay,config,lang,kind)==once
  assert m.historical_body(once,config,lang,kind)==original
  for bad in [once+'<p>unreviewed change</p>',once+m.START,once+overlay]:
   try:m.historical_body(bad,config,lang,kind)
   except AssertionError:pass
   else:raise AssertionError('Changed article or malformed overlay was accepted')
sys.path.insert(0,'scripts/fixtures')
from legacy_overlay_presentation import check_builder
assert check_builder(m,pathlib.Path.cwd())['HTML_layout_and_Markdown_byte_noop']
print('historical MHD preservation and bounded-failure guards checked')
`;
 assert.match(execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8'}),/preservation and bounded-failure/);
});

test('MHD static pages and SPA expose only their scoped successful releases with original anchors intact',()=>{
 const config=json('catalog/atlas-mhd-supplements.json');
 const mapping=json('catalog/atlas-depth-expansion.json').case_problem_ids;
 const sourceBodies=[];
 for(const lang of ['ja','en']){
  const chapter=json(`numerical-methods-atlas/content.${lang}.json`).mhd;
  const page=read(`numerical-methods-atlas/${lang}/read/mhd/index.html`);
  const metadata=json(`numerical-methods-atlas/${lang}/read/mhd/supplements.json`);
  assert.equal(metadata.locale,lang);assert.equal(metadata.chapter,'mhd');
  assert.deepEqual(metadata.supplements.map(x=>x.id),config.supplemental_examples);
  assert.ok(page.includes(config.comparison_note[lang]));
  assert.ok(chapter.html.includes(config.comparison_note[lang]));
  assert.ok(page.includes(config.cleaning_note[lang]));
  assert.ok(chapter.html.includes(config.cleaning_note[lang]));
  assert.deepEqual(chapter.headings.map(x=>x.id),[...anchors,config.section_id]);
  for(const id of [...anchors,config.section_id]){
   assert.equal((chapter.html.match(new RegExp(`id="${id}"`,'g'))||[]).length,1);
   assert.equal((page.match(new RegExp(`id="${id}"`,'g'))||[]).length,1);
   assert.ok(page.includes(`href="#${id}"`));
  }
  for(const [path,digest] of Object.entries(metadata.source_sha256))assert.equal(sha(path),digest,path);
  for(const example of metadata.supplements){
   assert.equal(example.problem_id,mapping[example.id]);
   assert.ok(example.code_urls.length&&example.test_urls.length);
   for(const target of [example.url+'?lang='+lang,example.reading[lang],...example.code_urls,...example.test_urls,example.download,example.results,example.verification]){
    assert.ok(page.includes(target),example.id+'/'+target);
    assert.ok(chapter.html.includes(target),example.id+'/'+target);
   }
  }
  for(const phrase of config.historical_replacements[lang]){
   assert.ok(page.includes(phrase.new));assert.ok(chapter.html.includes(phrase.new));
   assert.ok(!page.includes(phrase.old));assert.ok(!chapter.html.includes(phrase.old));
  }
  assert.ok(page.includes('no additional physical problem')||page.includes('物理問題数へ非加算'));
  sourceBodies.push(chapter);
 }
 assert.deepEqual(json('numerical-methods-atlas/content.json').mhd,sourceBodies[1]);
});

test('the new comparison augments MHD entrances without promoting unrelated crossover routes',()=>{
 const depth=json('catalog/atlas-depth.json').fields.find(x=>x.id==='mhd');
 const goal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='magnetic-divergence');
 for(const id of added){assert.ok(depth.supplemental_examples.includes(id));assert.ok(goal.supplemental_examples.includes(id));}
 const mapping=json('catalog/atlas-depth-expansion.json').case_problem_ids;
 assert.equal(mapping['ct-glm-constraint-control'],null);
 assert.ok(!json('catalog/atlas-test-problems.json').problems.some(x=>x.id==='ct-glm-constraint-control'));
 assert.deepEqual(goal.methods,['ct','glm','hlld']);
 const reading=json('catalog/atlas-reading-index.json').groups;
 const group=reading.find(x=>x.chapters.includes('validation-mhd')).chapters;
 assert.equal(group[group.indexOf('validation-mhd')+1],'validation-mhd-convergence');
 assert.equal(reading.flatMap(x=>x.chapters).filter(x=>x==='validation-mhd-convergence').length,1);
 const cross=json('catalog/atlas-crossovers.json');
 const timing=cross.math_families.find(x=>x.id==='time-evolution');
 for(const lang of ['ja','en'])assert.ok(timing.reading.some(x=>x.url[lang]===`/numerical-methods-atlas/${lang}/read/validation-mhd-convergence/`));
 for(const route of cross.routes){
  for(const stage of route.stages)assert.ok(!(stage.supplemental_ids||[]).some(x=>added.includes(x)));
  for(const item of [route,...route.connections])assert.ok(!(item.coupled_validation.supplemental_ids||[]).some(x=>added.includes(x)));
 }
});
