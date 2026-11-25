import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {searchChapters,wireHomeSearch} from '../numerical-methods-atlas/home-search.js';
import {configureLocale,currentLanguage} from '../numerical-methods-atlas/i18n.js';
import {makeSearch} from '../search/engine.mjs';

const root=new URL('../',import.meta.url);
const json=path=>JSON.parse(readFileSync(new URL(path,root),'utf8'));
const index=json('numerical-methods-atlas/home-search-index.json');
const discovery=json('catalog/atlas-execution-discovery.json');
const registry=json('catalog/atlas-execution-examples.json');
const route=(id,lang)=>`/numerical-methods-atlas/code-and-data/examples/${id}/?lang=${lang}`;
const queries={
  'barnes-hut':{ja:'Barnes Hut 実行',en:'Barnes Hut code'},
  'hydrogenic-atoms':{ja:'水素型原子 実行',en:'hydrogenic atoms run'},
  'helium-ground-state':{ja:'He SCF',en:'helium SCF code'},
  'advection-sine':{ja:'正弦波 移流 実行',en:'sine advection code'},
  sod:{ja:'Sod 実行',en:'Sod code'},
  'shu-osher':{ja:'Shu Osher 実行',en:'Shu Osher run'},
  'poisson-1d-dirichlet':{ja:'Poisson 1D 実行',en:'Poisson 1D code'},
  'poisson-2d-sine':{ja:'Poisson 2D 実行',en:'Poisson 2D code'},
  bratu:{ja:'Bratu 実行',en:'Bratu code'},
  'harmonic-oscillator':{ja:'調和振動子 実行',en:'harmonic oscillator code'},
  'stiff-cosine':{ja:'硬いODE 実行',en:'stiff cosine code'},
  'smooth-function-projection':{ja:'射影 実行',en:'Legendre projection code'},
  'periodic-particles':{ja:'周期粒子 実行',en:'periodic particles code'},
  'taylor-green':{ja:'Taylor Green 実行',en:'Taylor Green code'},
  'brio-wu':{ja:'Brio Wu 実行',en:'Brio Wu code'},
  'logistic-growth':{ja:'ロジスティック 実行',en:'logistic growth code'},
  'sir-epidemic':{ja:'SIR 実行',en:'SIR code'},
  'mc-integral':{ja:'mc-integral 実行',en:'mc-integral code'},
  'h2-rhf':{ja:'H2 実行',en:'H2 RHF code'},
  'periodic-he-dft':{ja:'周期DFT 実行',en:'periodic DFT code'},
  'periodic-he-forces':{ja:'原子間力 実行',en:'DFT forces code'},
  'gbm-sde':{ja:'幾何Brown運動 実行',en:'gbm-sde code'},
};

test('all twenty-two individual execution entries preserve curated names, outcomes and stable bilingual routes',()=>{
  const entries=index.entries.filter(entry=>entry.origin==='public-execution-discovery');
  assert.equal(entries.length,22);
  assert.equal(new Set(index.entries.map(entry=>entry.id)).size,index.entries.length);
  assert.deepEqual(entries.map(entry=>entry.id.replace(/^execution-/,'' )).sort(),Object.keys(queries).sort());
  for(const item of discovery.examples){
    const record=registry.examples.find(example=>example.id===item.id);
    const entry=entries.find(example=>example.id==='execution-'+item.id);
    assert.deepEqual(entry.title,record.name,item.id+' names');
    assert.deepEqual(entry.snippet,item.outcome,item.id+' outcomes');
    assert.equal(entry.kind,'execution-example',item.id+' kind');
    for(const keyword of item.keywords)assert.ok(entry.keywords.includes(keyword),item.id+' curated keyword');
    for(const lang of ['ja','en']){
      assert.equal(entry.routes[lang],route(item.id,lang));
      assert.ok(!entry.routes[lang].includes('#'));
      const pathname=new URL(entry.routes[lang],'https://hrkoyama.github.io').pathname;
      assert.ok(existsSync(new URL(pathname.slice(1)+'index.html',root)),item.id+' detail page');
    }
  }
});

test('bilingual problem, phenomenon and execution queries lead to the corresponding individual example',()=>{
  for(const [id,localized] of Object.entries(queries)){
    for(const lang of ['ja','en']){
      const first=searchChapters(index,localized[lang],lang)[0];
      assert.equal(first?.url,route(id,lang),localized[lang]);
      assert.equal(first.kind,'execution-example');
      assert.equal(first.badge,lang==='ja'?'実行例':'Runnable example');
      assert.equal(first.detail,discovery.examples.find(item=>item.id===id).outcome[lang]);
    }
  }
  for(const lang of ['ja','en']){
    const result=searchChapters(index,lang==='ja'?'Poisson コード':'Poisson code',lang)[0];
    assert.ok(['poisson-1d-dirichlet','poisson-2d-sine'].some(id=>result?.url===route(id,lang)));
  }
});

test('execution intent does not promote examples for generic or unrelated queries',()=>{
  const entry=(id,title,kind,keywords,focus=[])=>({id,title:{en:title,ja:null},headings:{en:[],ja:[]},keywords,focus_keywords:focus,kind,routes:{en:'/numerical-methods-atlas/'+id+'/'}});
  const synthetic={entries:[
    entry('spectral','Spectral methods','chapter',['spectral','spectral methods','code']),
    entry('guide','Get code, inputs and verification','resource',['code']),
    entry('poisson','Poisson numerical example','execution-example',['spectral','spectral methods','poisson','code','run'],['poisson']),
  ]};
  assert.equal(searchChapters(synthetic,'spectral methods')[0].id,'spectral');
  assert.equal(searchChapters(synthetic,'code')[0].id,'guide');
  assert.equal(searchChapters(synthetic,'Poisson code')[0].id,'poisson');
  for(const query of ['PBE code','AMR code','mixed precision code']){
    assert.ok(!searchChapters(index,query).some(row=>row.kind==='execution-example'),query+' unsupported execution claim');
  }
  for(const lang of ['ja','en']){
    const selected=searchChapters(index,'UHF code',lang).filter(row=>row.kind==='execution-example');
    assert.deepEqual(selected.map(row=>row.url),[`/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=${lang}`],'only the qualified fixed H2 model supports UHF execution');
    const packet=json('code/validated-examples/2026-11-25/quantum-small/cases.json');
    const fixed=(Array.isArray(packet)?packet:packet.cases).find(row=>row.id==='h2-rhf-uhf-fci');
    assert.match(fixed.limits.en,/two H2 geometries/);assert.match(fixed.limits.en,/spin contaminated/);assert.match(fixed.limits.en,/finite-basis only/);
  }
  assert.deepEqual(searchChapters(index,'zxqvnotfound123456789'),[]);
});

test('periodic Ewald and smooth-PME queries lead to their independent supplemental entries while the new slab correction retains its own scoped entry',()=>{
  for(const lang of ['ja','en'])for(const [query,id] of [['Ewald code','ewald'],['SPME code','spme']]){
    const result=searchChapters(index,query,lang).find(row=>row.url===`/numerical-methods-atlas/validation/${id}/?lang=${lang}`);
    assert.ok(result,query+' original periodic entry remains discoverable');
    assert.equal(result.kind,'execution-example');
    assert.equal(result.url,`/numerical-methods-atlas/validation/${id}/?lang=${lang}`);
    assert.equal(index.entries.find(entry=>entry.id===result.id).origin,'public-depth-validation');
    assert.ok(!registry.examples.some(example=>example.id===id),'supplement does not change the common22 registry');
  }
  const slab=searchChapters(index,'slab Ewald code','en');
  const method=slab.find(row=>row.method?.id==='slab-ewald')?.method;
  assert.equal(method.status,'educational-example');
  assert.ok(method.code_urls.length);
  assert.deepEqual(method.execution_examples.map(row=>row.id),['neutral-slab-yb']);
  assert.ok(slab.some(row=>row.kind==='execution-example'&&row.url==='/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en'));
});

test('the global site index discovers all detail pages and surfaces specific execution searches',()=>{
  const data=json('search/index.json');
  const search=makeSearch(data.documents);
  for(const item of discovery.examples){
    const path=route(item.id,'en').split('?')[0];
    const rows=data.documents.filter(document=>document.url===path);
    assert.equal(rows.length,1,item.id+' global index');
    assert.equal(rows[0].lang,'both',item.id+' bilingual global record');
  }
  for(const [query,lang,ids] of [
    ['Sod 実行','ja',['sod']],['Poisson code','en',['poisson-1d-dirichlet','poisson-2d-sine']],
    ['He SCF','ja',['helium-ground-state']],['射影 実行','ja',['smooth-function-projection']],
    ['Barnes Hut code','en',['barnes-hut']],
  ]){
    assert.ok(search(query,lang).slice(0,8).some(row=>ids.some(id=>row.url===route(id,lang).split('?')[0])),query);
  }
});

test('execution search retains same-site path validation and renders untrusted labels as text',async()=>{
  const unsafe=['javascript:alert(1)','data:text/html,x','https://evil.example/','//evil.example/',
    '/numerical-methods-atlas/../rights/','/numerical-methods-atlas/examples/x/#unsafe',
    '/numerical-methods-atlas/examples/x/?lang=en&next=https://evil.example/'];
  const item=url=>({id:'needle',title:{en:'needle <img src=x onerror=alert(1)>',ja:null},headings:{en:[],ja:[]},keywords:['needle','run'],focus_keywords:['needle'],snippet:{en:'Expected <script>alert(2)</script> result'},kind:'execution-example',routes:{en:url}});
  for(const url of unsafe)assert.deepEqual(searchChapters({entries:[item(url)]},'needle run'),[],url+' is rejected before ranking');
  const valid=route('sod','en');
  assert.equal(searchChapters({entries:[item(valid)]},'needle run')[0].url,valid);

  class Element{
    constructor(tag){this.tag=tag;this.children=[];this.listeners={};this.isConnected=true;this.textContent='';}
    set innerHTML(value){throw new Error('Untrusted search labels must not use innerHTML');}
    append(...values){this.children.push(...values);}
    prepend(...values){this.children.unshift(...values);}
    replaceChildren(...values){this.children=[...values];}
    addEventListener(name,listener){this.listeners[name]=listener;}
    querySelector(){return input;}
  }
  const input=new Element('input');input.value='needle run';
  const form=new Element('form'),status=new Element('p'),list=new Element('ol'),created=[];
  const nodes={'home-search-form':form,'home-search-status':status,'home-search-results':list};
  const oldDocument=globalThis.document,oldFetch=globalThis.fetch,locale=currentLanguage();
  try{
    configureLocale({},'en');
    globalThis.document={getElementById:id=>nodes[id],querySelectorAll:()=>[],
      createElement:tag=>{const node=new Element(tag);created.push(node);return node;},
      createTextNode:value=>({textContent:value})};
    globalThis.fetch=async()=>({ok:true,json:async()=>({entries:[item(valid)]})});
    wireHomeSearch();
    form.listeners.submit({preventDefault(){}});
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(list.children.length,1);
    assert.equal(list.hidden,false);
    assert.equal(created.find(node=>node.tag==='a').textContent,'needle <img src=x onerror=alert(1)>');
    assert.equal(created.find(node=>node.tag==='a').href,valid);
    assert.ok(created.some(node=>node.tag==='small'&&node.textContent==='Runnable example'));
    assert.ok(created.every(node=>!['script','img'].includes(node.tag)));
  }finally{
    globalThis.document=oldDocument;globalThis.fetch=oldFetch;configureLocale({},locale);
  }
});
