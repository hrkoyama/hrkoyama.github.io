import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {searchChapters,homeSearchPage,wireHomeSearch} from '../numerical-methods-atlas/home-search.js';
import {configureLocale,currentLanguage} from '../numerical-methods-atlas/i18n.js';

const root=new URL('../',import.meta.url);
const json=path=>JSON.parse(readFileSync(new URL(path,root),'utf8'));
const methods=json('numerical-methods-atlas/methods/index.json').methods;
const published=json('numerical-methods-atlas/home-search-index.json');
// Exercise the integration against public method records even before the
// generator has refreshed the checked-in index during development.
const index={...published,entries:published.entries.map(entry=>entry.origin==='public-method-registry'
  ? {...entry,method:methods.find(method=>entry.id==='registry-'+method.id)} : entry)};

test('the generated inline index contains public canonical method metadata',()=>{
  const entries=published.entries.filter(entry=>entry.kind==='method');
  assert.equal(entries.length,147);
  for(const method of methods){
    const entry=entries.find(entry=>entry.method?.id===method.id);
    assert.ok(entry,method.id+' generated canonical metadata');
    assert.deepEqual(entry.method.name,method.name);
    assert.deepEqual(entry.method.reading,method.reading);
    assert.deepEqual(entry.method.code_urls,method.code_urls);
    assert.deepEqual(entry.method.test_urls,method.test_urls);
    assert.equal(entry.method.status,method.status);
  }
});

test('method IDs, bilingual names and curated aliases reach every cataloged method',()=>{
  assert.equal(methods.length,147);
  for(const method of methods){
    for(const [query,language] of [[method.id,'ja'],[method.name.ja,'ja'],[method.name.en,'en'],...(method.aliases||[]).map(alias=>[alias,'ja'])]){
      const found=searchChapters(index,query,language).filter(result=>result.method);
      const own=found.find(result=>result.method.id===method.id);
      assert.ok(own,method.id+': '+query);
      assert.equal(own.kind,'method');
      assert.equal(own.url,`/numerical-methods-atlas/methods/${method.id}/?lang=${language}`);
      assert.equal(new Set(found.map(result=>result.method.id)).size,found.length,query+' duplicate method cards');
    }
  }
});

test('acronyms and Japanese method suffixes show canonical cards before chapter mentions',()=>{
  for(const query of ['KEEP','KEEP法','ＫＥＥＰ法','keep']){
    const found=searchChapters(index,query,'ja');
    assert.equal(found[0].method?.id,'keep',query);
    assert.deepEqual(found.filter(result=>result.method).map(result=>result.method.id),['keep']);
    assert.ok(found.filter(result=>!result.method).every(result=>result.related),query+' mentions are secondary');
  }
  for(const [query,id] of [['Roe法','roe'],['Thomas法','thomas'],['HLLD','hlld'],['WENO-Z','weno-z'],['のせフーバー','nose-hoover']]){
    assert.equal(searchChapters(index,query,'ja')[0].method?.id,id,query);
  }
  assert.ok(!searchChapters(index,'KEEP','ja').some(result=>result.method?.id==='kohn-sham-dft'));
});

test('named executable cases retain priority over method cards and broad chapter mentions',()=>{
  for(const [query,language,ids] of [
    ['Sod 実行','ja',['sod']],['Poisson code','en',['poisson-1d-dirichlet','poisson-2d-sine']],
    ['He SCF','ja',['helium-ground-state']],['Barnes Hut code','en',['barnes-hut']],
  ]){
    const first=searchChapters(index,query,language)[0];
    assert.equal(first?.kind,'execution-example',query);
    assert.ok(ids.some(id=>first.url===`/numerical-methods-atlas/code-and-data/examples/${id}/?lang=${language}`),query);
  }
  for(const query of ['PBE code','UHF code','slab-ewald code']){
    assert.ok(!searchChapters(index,query,'en').some(result=>result.kind==='execution-example'),query+' unsupported runnable claim');
  }
  for(const [query,id] of [['Ewald code','ewald'],['SPME code','spme']]){
    const rows=searchChapters(index,query,'en');
    assert.equal(rows[0]?.kind,'execution-example');
    assert.equal(rows[0]?.url,`/numerical-methods-atlas/validation/${id}/?lang=en`);
    const method=rows.find(row=>row.method?.id===id)?.method;
    assert.equal(method.status,'educational-example');
    assert.deepEqual(method.execution_examples.map(example=>example.id),[id]);
  }
});

test('inline cards expose real code and test destinations, collapse mentions and keep the scoped full search',async()=>{
  class Element{
    constructor(tag){this.tag=tag;this.children=[];this.listeners={};this.dataset={};this.isConnected=true;this.textContent='';this.classList={add:()=>{}};}
    set innerHTML(value){throw new Error('Search labels must be rendered as text');}
    append(...values){this.children.push(...values);}
    prepend(...values){this.children.unshift(...values);}
    replaceChildren(...values){this.children=[...values];}
    setAttribute(name,value){this[name]=value;}
    addEventListener(name,listener){this.listeners[name]=listener;}
    querySelector(){return input;}
  }
  const input=new Element('input');input.value='KEEP';
  const form=new Element('form'),status=new Element('p'),list=new Element('ol'),related=new Element('details'),relatedList=new Element('ol'),relatedLabel=new Element('summary'),all=new Element('a'),head=new Element('head');
  const nodes={'home-search-form':form,'home-search-status':status,'home-search-results':list,
    'home-search-related':related,'home-search-related-results':relatedList,'home-search-related-label':relatedLabel,'home-search-all':all};
  const oldDocument=globalThis.document,oldFetch=globalThis.fetch,oldLocation=globalThis.location,locale=currentLanguage();
  const descendants=node=>[node,...(node.children||[]).flatMap(descendants)];
  try{
    configureLocale({},'ja');
    assert.ok(homeSearchPage().includes('scope=atlas&amp;lang=ja'));
    globalThis.location={origin:'https://hrkoyama.github.io'};
    globalThis.document={head,getElementById:id=>nodes[id],querySelectorAll:()=>[],
      querySelector:()=>head.children.find(node=>node.tag==='link'),
      createElement:tag=>new Element(tag),createTextNode:value=>({textContent:value})};
    globalThis.fetch=async()=>({ok:true,json:async()=>index});
    wireHomeSearch();
    form.listeners.submit({preventDefault(){}});
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(list.children.length,1,'one direct method card');
    assert.equal(list.children[0].dataset.methodId,'keep');
    const links=descendants(list).filter(node=>node.tag==='a').map(node=>node.href);
    assert.ok(links.some(url=>url.includes('/ja/read/keep/')),'direct explanation');
    assert.ok(links.some(url=>url.endsWith('/numart/keep.py')),'direct published source');
    assert.ok(links.some(url=>url.endsWith('/tests/test_keep.py')),'direct published test');
    assert.equal(related.hidden,false);
    assert.equal(related.open,false);
    assert.ok(relatedList.children.length>0);
    assert.match(relatedLabel.textContent,/関連資料/);
    assert.equal(all.href,'/search/?scope=atlas&lang=ja#q=KEEP');
    assert.equal(all.hidden,false);
    input.value='のせフーバー';form.listeners.submit({preventDefault(){}});
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(list.children[0].dataset.methodId,'nose-hoover');
    const planned=descendants(list);
    assert.ok(!planned.some(node=>node.tag==='a'&&node.href?.startsWith('/code/')),'planned methods have no borrowed code or tests');
    assert.ok(planned.some(node=>node.textContent==='コード・テストは未公開'));
    input.value='';form.listeners.submit({preventDefault(){}});
    assert.equal(list.hidden,true);
    assert.equal(related.hidden,true);
    assert.equal(all.hidden,true);
  }finally{
    globalThis.document=oldDocument;globalThis.fetch=oldFetch;globalThis.location=oldLocation;configureLocale({},locale);
  }
});
