import {equationCount,problemCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const execution=json('catalog/atlas-execution-examples.json');
const discovery=json('catalog/atlas-execution-discovery.json');
const publicDiscovery=json('numerical-methods-atlas/code-and-data/examples/index.json');
const base='https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/';
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
function locale(html,lang){
  const start=html.indexOf(`<section data-site-language="${lang}"`);assert.ok(start>=0);
  const rest=html.slice(start);let depth=0;
  for(const tag of rest.matchAll(/<\/?section\b[^>]*>/g)){
    depth+=tag[0].startsWith('</')?-1:1;
    if(depth===0)return rest.slice(0,tag.index+tag[0].length);
  }
  assert.fail('Unclosed locale section');
}

test('22 stable entry pages preserve the authoritative execution records and their public receipt binding',()=>{
  assert.equal(publicDiscovery.examples.length,22);
  assert.equal(publicDiscovery.registry_sha256,sha('numerical-methods-atlas/code-and-data/examples.json'));
  const receipt=json(new URL(execution.verification_receipt).pathname.slice(1));
  assert.equal(receipt.registry_sha256,publicDiscovery.registry_sha256);
  assert.equal(receipt.passed,true);
  for(const original of execution.examples){
    const prefix='numerical-methods-atlas/code-and-data/examples/'+original.id+'/';
    const entry=json(prefix+'index.json');
    for(const [key,value] of Object.entries(original))assert.deepEqual(entry[key],value,original.id+'.'+key);
    assert.equal(entry.url,base+original.id+'/');
    assert.equal(entry.public_rerun.passed,true);
    assert.equal(entry.registry_sha256,receipt.registry_sha256);
    assert.ok(read(prefix+'index.html').includes('<link rel="canonical" href="'+entry.url+'">'));
  }
});

test('each language of each dedicated page exposes its own purpose, exact input/run/output conditions and source terms',()=>{
  for(const item of discovery.examples){
    const original=execution.examples.find(x=>x.id===item.id);
    const prefix='numerical-methods-atlas/code-and-data/examples/'+item.id+'/';
    const html=read(prefix+'index.html');
    for(const lang of ['ja','en']){
      const section=locale(html,lang);
      assert.equal((section.match(/<h1>/g)||[]).length,1,item.id+'/'+lang+' single page title');
      assert.ok(section.includes('<h2>'),item.id+'/'+lang+' h2 subsections');
      assert.doesNotMatch(section,/<h3>/,item.id+'/'+lang+' does not skip h2 in its content hierarchy');
      for(const value of [item.outcome[lang],original.name[lang],original.scope[lang],original.assumptions[lang],original.units[lang],original.boundaries[lang]])assert.ok(section.includes(escape(value)),item.id+'/'+lang+' correct local text');
      for(const asset of [original.inputs,...original.outputs])assert.ok(section.includes('href="'+escape(asset.url)+'"'),item.id+' artifact');
      assert.ok(section.includes(escape(original.commands.install+'\n'+original.commands.run)),item.id+' commands');
      assert.ok(section.includes('href="'+escape(original.release.download)+'"'),item.id+' edition');
      for(const criterion of original.checks)assert.ok(section.includes(escape(criterion.description[lang])),item.id+' criterion');
      assert.ok(section.includes('href="'+original.terms.code_license+'"'));
      assert.ok(section.includes('href="'+original.terms.content_and_data+'"'));
      assert.ok(section.includes('href="index.json"')&&section.includes('href="index.md"'));
    }
  }
});

test('Markdown retains array selectors and result fields, so H/He acceptance criteria remain executable descriptions',()=>{
  for(const example of execution.examples){
    const markdown=read('numerical-methods-atlas/code-and-data/examples/'+example.id+'/index.md');
    assert.ok(markdown.includes(example.inputs.sha256));
    for(const check of [...example.checks,...example.expected_failures]){
      const rows=markdown.split('\n').filter(line=>line.startsWith('- '+check.id+' / '));
      assert.equal(rows.length,2,example.id+'/'+check.id+' bilingual criteria');
      for(const line of rows){
        assert.ok(line.includes(check.pointer));
        if(check.field)assert.ok(line.includes('field='+check.field),example.id+' selected field');
        if(check.where){
          assert.ok(line.includes('where='));
          for(const [key,value] of Object.entries(check.where))assert.ok(line.replaceAll(' ','').includes(JSON.stringify(key)+':'+JSON.stringify(value)),example.id+' selector '+key);
        }
      }
    }
  }
});

test('every verified example is reachable from words, formulas and its image through the matching problem page',()=>{
  const search=json('numerical-methods-atlas/home-search-index.json');
  const formulas=read('numerical-methods-atlas/equations/index.html');
  const gallery=json('numerical-methods-atlas/gallery/index.json');
  const galleryHtml=read('numerical-methods-atlas/gallery/index.html');
  for(const item of discovery.examples){
    const result=search.entries.find(x=>x.id==='execution-'+item.id);assert.ok(result,item.id+' word route');
    const visual=gallery.items.find(x=>x.id===item.problem_id);assert.ok(visual);
    for(const lang of ['ja','en']){
      const target=base+item.id+'/?lang='+lang;
      assert.equal(result.routes[lang],new URL(target).pathname+new URL(target).search);
      assert.ok(locale(formulas,lang).includes('href="'+target+'"'),item.id+' formula route');
      assert.equal(visual.execution_entry.url[lang],target);
      const tile=galleryHtml.split(`id="${item.problem_id}-${lang}"`)[1].split('</li>')[0];
      const imageTarget=tile.match(/<a\b[^>]*class="gallery-image-link"[^>]*href="([^"]+)"/)?.[1];
      assert.ok(imageTarget,item.id+' image route');
      const hub=new URL(imageTarget,'https://hrkoyama.github.io');
      assert.equal(hub.pathname,`/numerical-methods-atlas/problems/${item.problem_id}/`);
      assert.equal(hub.searchParams.get('lang'),lang);
      const problem=json(hub.pathname.slice(1)+'index.json');
      const verified=problem.executions.find(example=>example.id===item.id&&example.kind==='common');
      assert.equal(verified?.guide[lang],target,item.id+' hub retains the same verified execution');
      assert.ok(locale(read(hub.pathname.slice(1)+'index.html'),lang).includes('href="'+target+'"'),item.id+' visible hub execution route');
      const badge=tile.match(/<p class="gallery-execution-badge">([\s\S]*?)<\/p>/)?.[1];
      assert.ok(badge?.includes('href="'+target+'"'),item.id+' direct run badge');
    }
  }
  assert.equal(json('numerical-methods-atlas/equations/index.json').equations.length,equationCount);
  assert.equal(gallery.items.length,problemCount);
});

test('the concise homepage leads to the full execution chooser with the existing starting calculations',()=>{
  const home=read('numerical-methods-atlas/index.html');
  const chooser=read('numerical-methods-atlas/code-and-data/examples/index.html');
  for(const lang of ['ja','en']){
    for(const id of ['poisson-2d-sine','barnes-hut','helium-ground-state','hydrogenic-atoms'])assert.ok(chooser.includes(base+id+'/?lang='+lang),id+' chooser route');
    assert.ok(home.includes(base.replace('https://hrkoyama.github.io','')+'?lang='+lang));
  }
  assert.ok(!home.includes('data-featured-example='), 'the choices live one page beyond the compact landing');
});

test('the shared chooser also exposes the separate supplementary registry and named fixed-input cases in both languages',()=>{
  const html=read('numerical-methods-atlas/code-and-data/examples/index.html');
  const registry=json('numerical-methods-atlas/validation/releases.json');
  const count=registry.releases.reduce((n,row)=>n+row.case_ids.length,0);
  const selected=['sem-poisson-2d','fr-periodic-advection','level-set-translation','level-set-rotation','reaction-diffusion-splitting'];
  for(const lang of ['ja','en']){
    const section=locale(html,lang);
    assert.ok(section.includes('id="supplementary-examples-'+lang+'"'));
    assert.ok(section.includes('/numerical-methods-atlas/validation/?lang='+lang));
    assert.ok(section.includes(lang==='ja'?`${registry.releases.length}群・${count}ケース`:`${count} fixed-input cases in ${registry.releases.length} groups`));
    for(const id of selected){
      assert.ok(section.includes('href="/numerical-methods-atlas/validation/'+id+'/?lang='+lang+'"'),id);
      assert.ok(read('numerical-methods-atlas/validation/'+id+'/index.html').includes('data-site-language="'+lang+'"'));
    }
    assert.equal((section.match(/data-entry-id=/g)||[]).length,execution.examples.length,'shared examples remain a separate inventory');
  }
});
