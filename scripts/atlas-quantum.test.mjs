import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const data=json('catalog/atlas-quantum.json');
const methods=json('catalog/atlas-methods.json').methods.filter(x=>x.group.id==='quantum');
const coverage=json('numerical-methods-atlas/coverage.json');

test('each curated quantum topic has bilingual equations, valid source links and explicit limits with implementation scope distinguished',()=>{
  assert.deepEqual(data.sections.map(x=>x.id).sort(),methods.map(x=>x.id).sort());
  assert.equal(methods.length,20);
  const references=new Map(data.references.map(x=>[x.id,x]));
  for(const x of methods){
    assert.equal(x.status,(x.quantum_examples?.length||x.molecular_examples?.length||x.periodic_examples?.length)?'educational-example':'reading-only');
    assert.deepEqual(x.code_modules,[]);assert.deepEqual(x.test_files,[]);
    const s=data.sections.find(y=>y.id===x.id);
    assert.ok(s.references.length&&s.references.every(id=>references.has(id)));
    for(const lang of ['ja','en']){
      const page=read(`numerical-methods-atlas/${lang}/read/quantum-chemistry/index.html`);
      assert.ok(page.includes('data-quantum-id="'+x.id+'"'));
      assert.ok(page.includes('id="'+x.id+'"'));
      assert.ok(page.includes(s.caution[lang]));
      assert.ok(s.paragraphs[lang].length>=2);
      assert.ok(!page.includes('katex-error'));
      assert.ok(json(`numerical-methods-atlas/content.${lang}.json`)['quantum-chemistry']);
    }
  }
  assert.ok(read('numerical-methods-atlas/ja/read/quantum-chemistry/index.html').includes('katex-mathml'));
  assert.equal(new Set(data.references.map(x=>x.doi.toLowerCase())).size,data.references.length);
});

test('quantum additions reconcile model, method and publication counts across the common atlas',()=>{
  const quantum=coverage.items.filter(x=>x.origin==='curated-quantum-reading');
  assert.equal(quantum.filter(x=>x.kind==='method').length,methods.length);
  assert.equal(quantum.filter(x=>x.kind==='equation').length,4);
  assert.equal(quantum.filter(x=>x.status==='local-example'&&x.kind==='method').length,9);
  assert.equal(quantum.filter(x=>x.status==='local-example'&&x.kind==='equation').length,3);
  assert.equal(coverage.counts.methods,coverage.items.filter(x=>x.kind==='method').length);
  assert.equal(coverage.counts.equations,coverage.items.filter(x=>x.kind==='equation').length);
  assert.equal(coverage.counts.papers,coverage.publications.filter(x=>['article','inproceedings'].includes(x.type)).length);
  assert.equal(coverage.counts.references,coverage.publications.length);
  assert.equal(new Set(coverage.publications.map(x=>x.identity)).size,coverage.publications.length);
  const library=json('numerical-methods-atlas/references.json');
  for(const r of data.references){
    assert.equal(library.filter(x=>x.doi?.toLowerCase()===r.doi.toLowerCase()).length,1);
    assert.equal(coverage.publications.filter(x=>x.identity==='doi:'+r.doi.toLowerCase()).length,1);
    assert.ok(read('numerical-methods-atlas/assets/references.bib').includes(r.doi));
  }
  for(const [path,expected] of Object.entries(coverage.public_extension_sha256)){
    assert.equal(createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex'),expected,path);
  }
  assert.deepEqual(json('numerical-methods-atlas/assets/site-coverage.json'),coverage);
});

test('DFT is discoverable by Japanese, English and aliases, and all new equations link to the appropriate section',()=>{
  const index=json('numerical-methods-atlas/home-search-index.json');
  for(const query of ['量子化学','DFT','密度汎関数','Kohn–Sham']){
    const hits=searchChapters(index,query,'ja');
    assert.ok(hits.some(x=>x.url?.includes('quantum-chemistry')||x.url?.includes('kohn-sham-dft')),query);
  }
  for(const lang of ['ja','en']){
    assert.ok(json('guide/index.json').pages.some(x=>x.url===`https://hrkoyama.github.io/numerical-methods-atlas/${lang}/read/quantum-chemistry/`));
    const page=read(`numerical-methods-atlas/${lang}/read/site-coverage/index.html`);
    assert.ok(page.includes('quantum-extension'));
    assert.ok(page.includes(String(coverage.counts.methods))&&page.includes(String(coverage.counts.papers)));
    if(lang==='ja')assert.ok(page.includes(`ローカル実験のある項目は${coverage.counts.local_methods}、文献解説のみは${coverage.counts.reading_methods}です`));
    else assert.ok(page.includes(`${coverage.counts.journal_articles} journal-article records`));
  }
  const models=json('numerical-methods-atlas/equations/index.json').equations.filter(x=>x.group==='quantum');
  assert.equal(models.length,4);
  for(const x of models)for(const url of Object.values(x.reading))assert.ok(new URL(url).hash);
  const app=read('numerical-methods-atlas/app.js');
  assert.equal(app.split('const atlasDocumentVersions =').length-1,1);
  for(const lang of ['ja','en'])assert.ok(app.includes(createHash('sha256').update(readFileSync(new URL(`numerical-methods-atlas/content.${lang}.json`,root))).digest('hex').slice(0,12)));
});

test('only executed quantum examples enter test-problem counts and specialist AI is deferred until 2027',()=>{
  assert.equal(data.verification_plan.filter(x=>x.state==='verified-educational-example').length,5);
  assert.equal(data.verification_plan.length,5);
  assert.equal(data.verification_plan.filter(x=>x.state==='planned').length,0);
  const tests=json('numerical-methods-atlas/test-cases/index.json');
  assert.equal(tests.problems.length,82);
  assert.equal(tests.problems.filter(x=>x.chapter==='quantum-atoms').length,2);
  assert.ok(!tests.problems.some(x=>x.chapter==='quantum-chemistry'));
  const work=json('catalog/atlas-work-queue.json').items;
  const ai=work.find(x=>x.id==='atlas-specialist-ai');
  assert.equal(ai.state,'deferred-until-2027');assert.equal(ai.target_year,2027);
  for(const lang of ['ja','en']){
    const roadmap=read(`numerical-methods-atlas/${lang}/read/roadmap/index.html`);
    assert.ok(roadmap.includes(ai.title[lang])&&roadmap.includes(ai.scope[lang]));
    assert.ok(roadmap.indexOf('id="atlas-work-queue"')<roadmap.indexOf('id="current-priority-shock-methods"'));
    assert.ok(roadmap.indexOf('id="atlas-roadmap-history"')<roadmap.indexOf('id="current-priority-shock-methods"'));
    assert.doesNotMatch(roadmap,/現在の最優先：衝撃波手法|承認済みの次の作業|Current priority: shock methods|Authorized next work/);
    assert.ok(!roadmap.includes('implementation and the dedicated literature review have not'));
  }
  const translations=json('numerical-methods-atlas/locales/messages.json');
  assert.ok(!translations['home-map.future'].ja.includes('未着手分野'));
  assert.ok(!translations['planned.quantum.status'].en.includes('have not started'));
});

test('band symmetry distinguishes little groups, SOC and antiunitary assumptions from a verified band calculation',()=>{
  const s=data.sections.find(x=>x.id==='band-symmetry');
  assert.ok(s&&s.subsections.length===4);
  assert.ok(s.formula.some(f=>f.includes('G_{\\mathbf k}')));
  assert.ok(s.subsections.find(x=>x.id==='band-symmetry-soc-tr').formula.some(f=>f.includes('\\Theta^2=-1')));
  for(const lang of ['ja','en']){
    const page=read(`numerical-methods-atlas/${lang}/read/quantum-chemistry/index.html`);
    for(const child of s.subsections)assert.ok(page.includes('id="'+child.id+'"'));
    assert.ok(page.includes(lang==='ja'?'高対称線の図だけで大域的なバンドギャップを断定しません':'it alone does not establish the global band gap'));
  }
  assert.ok(read('llms.txt').includes(data.sections.length+' bilingual introductory topics'));
});
