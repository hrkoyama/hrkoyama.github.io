import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {atlasPurpose,atlasMetrics} from '../numerical-methods-atlas/atlas-purpose.js';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const coverage=JSON.parse(read('numerical-methods-atlas/coverage.json'));

test('the three browse routes are available in both languages before the purpose text',()=>{
  const copy=JSON.parse(read('catalog/atlas-purpose.json'));
  for(const lang of ['ja','en']){
    configureLocale({},lang);const html=atlasPurpose();
    assert.equal((html.match(/class="atlas-way"/g)||[]).length,3);
    assert.ok(html.indexOf('atlas-ways')<html.indexOf('atlas-purpose'));
    for(const item of copy[lang].browse)assert.ok(html.includes(item.title));
    assert.ok(html.includes('/numerical-methods-atlas/equations/?lang='+lang));
    assert.ok(html.includes('/numerical-methods-atlas/gallery/?lang='+lang));
    assert.ok(html.includes('data-atlas-word-search'));
  }
});
test('prominent counts use the atlas-wide problem inventory, with scoped wave cases retained',()=>{
  const inventory=JSON.parse(read('numerical-methods-atlas/test-cases/index.json'));
  assert.equal(coverage.counts.test_problems,inventory.problems.length);
  assert.ok(coverage.counts.test_problems>coverage.counts.gallery_cases);
  assert.equal(coverage.counts.gallery_cases,JSON.parse(read('numerical-methods-atlas/equation-gallery.json')).cases.length);
  assert.equal(coverage.counts.methods,coverage.items.filter(x=>x.kind==='method').length);
  assert.equal(coverage.counts.equations,coverage.items.filter(x=>x.kind==='equation').length);
  for(const lang of ['ja','en']){
    configureLocale({},lang);const html=atlasMetrics();
    for(const key of ['methods','papers','equations','test_problems'])assert.ok(html.includes('<strong>'+coverage.counts[key]+'</strong>'));
    assert.ok(html.includes('/numerical-methods-atlas/test-cases/'));
    assert.equal((html.match(/<a href=/g)||[]).length,4);
  }
});
test('equation records link to existing chapters in both languages and expose a matching public index',()=>{
  const source=JSON.parse(read('catalog/atlas-equations.json'));
  const published=JSON.parse(read('numerical-methods-atlas/equations/index.json'));
  const html=read('numerical-methods-atlas/equations/index.html');
  assert.equal(new Set(source.equations.map(x=>x.id)).size,source.equations.length);
  const models=coverage.items.filter(x=>x.kind==='equation');
  assert.deepEqual(source.equations.map(x=>x.id).sort(),models.map(x=>x.id).sort());
  assert.equal(source.equations.length,coverage.counts.equations);
  assert.equal(published.equations.length,source.equations.length);
  for(const x of source.equations){
    assert.ok(x.formula.length&&x.note.ja&&x.note.en);
    for(const lang of ['ja','en'])assert.ok(existsSync(new URL(`numerical-methods-atlas/${lang}/read/${x.chapter}/index.html`,root)));
  }
  assert.equal((html.match(/data-equation-id=/g)||[]).length,2*source.equations.length);
  assert.ok(html.includes('全'+coverage.counts.equations+'方程式・モデル'));
  assert.equal(published.counts.local_example,coverage.counts.local_equations);
  assert.equal(published.counts.reading_only,coverage.counts.reading_equations);
});

test('every displayed model has static math and valid deep links without inflating implementation status',()=>{
  const published=JSON.parse(read('numerical-methods-atlas/equations/index.json'));
  const html=read('numerical-methods-atlas/equations/index.html');
  const implementedBiology=['bio-logistic','bio-sir','bio-turing','bio-schnakenberg','bio-fitzhugh-nagumo'];
  assert.equal(published.equations.filter(x=>x.id.startsWith('bio-')).length,22);
  assert.equal(published.equations.filter(x=>x.id.startsWith('bio-')&&x.status==='reading').length,17);
  for(const x of published.equations){
    const expected=coverage.items.find(item=>item.kind==='equation'&&item.id===x.id);
    assert.equal(x.status,expected.status);
    assert.equal(x.chapter,expected.chapter);
    for(const [lang,url] of Object.entries(x.reading)){
      const target=new URL(url),path=target.pathname.slice(1)+'index.html';
      assert.ok(existsSync(new URL(path,root)));
      if(target.hash)assert.ok(read(path).includes('id="'+target.hash.slice(1)+'"'),x.id+' '+lang);
      assert.ok(html.includes('id="'+x.id+'-'+lang+'"'));
    }
    if(x.id.startsWith('bio-')){
      assert.equal(x.status,implementedBiology.includes(x.id)?'local-example':'reading');
      if(implementedBiology.includes(x.id)){
        assert.ok(x.execution_scope.ja&&x.execution_scope.en);
        assert.ok(x.execution_examples.length||x.supplemental_execution_examples.length);
      }else{
        assert.deepEqual(x.execution_examples,[]);
        assert.deepEqual(x.supplemental_execution_examples,[]);
      }
      assert.ok(x.reading.ja.includes('#')&&x.reading.en.includes('#'));
    }
  }
  assert.ok(html.includes('katex-mathml')&&html.includes('application/x-tex'));
  assert.ok(!html.includes('katex-error'));
  assert.ok(!html.includes('This initial index is separate'));
  assert.ok(html.includes('id="advection-ja"')&&html.includes('id="diffusion-ja"')&&html.includes('id="poisson-ja"'));
});
