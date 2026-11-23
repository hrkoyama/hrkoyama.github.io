import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';
import {atlasSearch,makeSearch,searchVocabulary} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
import {unpackSearchIndex,searchDetailURL} from '../search/compact-index.mjs';
import {appendSearchNavigation} from '../search/navigation.mjs';
import {searchDOM,descendants,flushSearch} from './fixtures/search-dom.mjs';

const root=new URL('../',import.meta.url),read=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(read(p));
const fullHome=json('numerical-methods-atlas/home-search-index.json'),fullSite=json('search/index.json');
const atlas=json('search/atlas-query-index.json'),site=json('search/query-index.json');
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
const detail=key=>json('search/details/'+key+'.json');

test('model notes distinguish actual atomic, molecular and periodic scopes without changing the formulation',()=>{
 const source=json('catalog/atlas-equations.json').equations;
 const hf=source.find(x=>x.id==='hartree-fock-model'),ks=source.find(x=>x.id==='kohn-sham-model');
 assert.match(hf.note.ja,/He/);assert.match(hf.note.ja,/H₂ RHF/);
 assert.match(ks.note.ja,/Dirac/);assert.match(ks.note.ja,/VWN5/);
 assert.doesNotMatch(ks.note.ja,/周期系は未実装/);
 const html=read('numerical-methods-atlas/equations/index.html');
 for(const value of [hf.note.ja,hf.note.en,ks.note.ja,ks.note.en])assert.ok(html.includes(value));
 assert.ok(html.includes('periodic-he-dft')&&html.includes('periodic-he-forces')&&html.includes('h2-rhf'));
});

test('both interfaces use one atlas ranking for execution intent, aliases and Japanese/English queries',()=>{
 const engine=atlasSearch(atlas),full=atlasSearch(fullHome);
 const cases=[['Sod test','sod'],['Poisson テスト','poisson-1d-dirichlet'],['SEM Poisson 実行','sem-poisson-2d'],['FR periodic advection test','fr-periodic-advection'],['FR periodic advection run','fr-periodic-advection']];
 for(const [query,id]of cases)for(const lang of ['ja','en']){
  const browser=engine(query,lang,'atlas'),inline=searchChapters(atlas,query,lang);
  assert.ok(browser[0].url.includes('/'+id+'/'),query);assert.equal(browser[0].executionPriority,true);
  assert.ok(inline[0].url.includes('/'+id+'/'),query);assert.equal(inline[0].executionPriority,true);
  assert.deepEqual(browser.map(x=>[x.id,x.kind,x.score]),full(query,lang,'atlas').map(x=>[x.id,x.kind,x.score]),query+' full/compact parity');
 }
 for(const query of ['KEEP','Nek5000','周期DFT','ＷＥＮＯ－Ｚ','Kohn–Sham','GSPH','zxqv-not-a-method'])for(const lang of ['ja','en']){
  assert.deepEqual(engine(query,lang,'atlas').map(x=>[x.id,x.kind,x.score]),full(query,lang,'atlas').map(x=>[x.id,x.kind,x.score]));
 }
 for(const method of json('catalog/atlas-methods.json').methods)for(const query of [method.id,...Object.values(method.name)]){
  assert.deepEqual(engine(query,'ja','atlas').filter(x=>x.kind==='method').map(x=>x.id),full(query,'ja','atlas').filter(x=>x.kind==='method').map(x=>x.id),query);
 }
});

test('compact corpora preserve every normalized text token, source record and fixed detail hash within byte budgets',()=>{
 const budgets=json('search/budgets.json');
 for(const [kind,packed,original,field,file,source]of [
  ['atlas',atlas,fullHome,'entries','search/atlas-query-index.json','numerical-methods-atlas/home-search-index.json'],
  ['site',site,fullSite,'documents','search/query-index.json','search/index.json']]){
  const raw=readFileSync(new URL(file,root)),expanded=unpackSearchIndex(packed);
  assert.equal(unpackSearchIndex(expanded),expanded,'decoding is idempotent across both entry-point loaders');
  assert.ok(raw.length<=budgets[kind].decoded_bytes,file+' decoded budget');assert.ok(gzipSync(raw,{level:9}).length<=budgets[kind].gzip_bytes,file+' gzip budget');
  assert.equal(packed.source_index.url,'/'+source);assert.equal(packed.source_index.sha256,digest(readFileSync(new URL(source,root))));
  assert.equal(expanded[field].length,original[field].length);
  for(let i=0;i<original[field].length;i++){
   const before=original[field][i],after=expanded[field][i];assert.equal(after.id,before.id);assert.equal(after.url,before.url);
   assert.deepEqual(after.routes,before.routes);
   const a=typeof before.text==='string'?{all:before.text}:before.text||{},b=typeof after.search_text==='string'?{all:after.search_text}:after.search_text;
   for(const [lang,text]of Object.entries(a))assert.equal(searchVocabulary(b[lang]),searchVocabulary(text),kind+'/'+i+'/'+lang+' retains token membership');
   if(after.text_ref)assert.deepEqual(detail(after.text_ref).text,before.text);
  }
  for(const key of packed.details.keys){assert.match(key,/^[a-f0-9]{64}$/);assert.equal(digest(readFileSync(new URL('search/details/'+key+'.json',root))),key);}
 }
 const search=makeSearch(unpackSearchIndex(site).documents),old=makeSearch(fullSite.documents);
 for(const query of ['Lane Emden','量子力学','HPCI','熱的不安定性','Schrödinger','0.15'])assert.deepEqual(search(query,'ja').map(x=>x.url),old(query,'ja').map(x=>x.url),query);
});

test('large navigation graphs load on opening, preserve all scoped routes and never transmit query text',async()=>{
 const entry=atlas.entries.find(x=>Object.values(x.search_navigation?.counts||{}).some(n=>n>2));assert.ok(entry);
 const graph=entry.search_navigation,full=detail(graph.details_ref).search_navigation;
 const dom=searchDOM({fetch:async(url,options)=>{
  assert.equal(options.credentials,'omit');assert.match(new URL(url).pathname,/\/search\/details\/[a-f0-9]{64}[.]json$/);assert.equal(new URL(url).search,'');
  return {ok:true,json:async()=>({search_navigation:full})};
 }});
 try{
  const target=dom.document.createElement('li');dom.document.body.append(target);appendSearchNavigation(target,{search_navigation:graph},'ja');
  assert.equal(dom.fetches.length,0);
  const key=Object.keys(graph.counts).find(k=>graph.counts[k]>2);
  const expand=target.querySelector('[data-search-navigation-category="'+key+'"]');expand.open=true;expand.fire('toggle');await flushSearch();
  assert.equal(dom.fetches.length,1);assert.ok(target.textContent.includes(full.note.ja));
  const links=descendants(target).filter(x=>x.tag==='a').map(x=>x.href);
  for(const item of full.groups[key]){const u=new URL(item.url.ja,'https://hrkoyama.github.io');assert.ok(links.includes(u.pathname+u.search+u.hash),item.id);}
 }finally{dom.restore();}
 for(const key of ['../private','https://evil.example/x','javascript:alert(1)','a'.repeat(63)])assert.throws(()=>searchDetailURL(key));
 assert.throws(()=>unpackSearchIndex({format:'compact-search-v1',kind:'site',terms:['x'],documents:[{search_terms:[9]}]}));
});

test('global atlas search waits for a query and loads the same compact corpus as the homepage',async()=>{
 const dom=searchDOM({kind:'site',query:'',index:atlas});
 try{
  const main=dom.document.querySelector('[data-search-index]');main.dataset.atlasSearchIndex='/search/atlas-query-index.json?v=fixture';main.dataset.atlasSearchCount=String(atlas.entries.length);
  await import('../search/search.js?priority-one-empty-query');await flushSearch();assert.equal(dom.fetches.length,0);
  dom.location.hash='q=Sod%20test';dom.fireWindow('hashchange');await flushSearch();
  assert.equal(dom.fetches[0].url,'/search/atlas-query-index.json?v=fixture');
  const first=descendants(dom.nodes('search-results')).find(x=>x.tag==='a');assert.ok(first.href.includes('/examples/sod/'));
  assert.ok(dom.fetches.every(x=>!x.url.includes('Sod')&&!x.url.includes('test')));
 }finally{dom.restore();}
 const html=read('search/index.html');assert.match(html,/data-atlas-search-index="\/search\/atlas-query-index[.]json[?]v=/);assert.match(html,/data-search-index="\/search\/query-index[.]json[?]v=/);
 const homeScript=read('numerical-methods-atlas/home-search.js');assert.match(homeScript,/new URL\('[.][.]\/search\/atlas-query-index[.]json[?]v=/);
});
