import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {findMethods,appendMethodCard} from '../search/method-search.mjs';
import {makeSearch} from '../search/engine.mjs';

const origin='https://hrkoyama.github.io';
const root=new URL('../',import.meta.url);
const json=path=>JSON.parse(readFileSync(new URL(path,root),'utf8'));
const catalog=json('catalog/atlas-methods.json').methods;
const published=json('numerical-methods-atlas/methods/index.json').methods;
const byId=id=>published.find(method=>method.id===id);
const ids=results=>results.map(result=>result.id);
const path=value=>{const url=new URL(value,origin);return url.pathname+url.search+url.hash;};

test('every registered ID, bilingual name and curated alias reaches its own canonical method',()=>{
  assert.equal(catalog.length,143);
  assert.equal(new Set(catalog.map(method=>method.id)).size,143);
  for(const method of catalog){
    const queries=[[method.id,'ja'],[method.name.ja,'ja'],[method.name.en,'en'],
      ...(method.aliases||[]).map(alias=>[alias,'ja'])];
    for(const [query,language] of queries){
      const results=findMethods(catalog,query,language);
      const own=results.find(result=>result.id===method.id);
      assert.ok(own,`${method.id}: ${query}`);
      assert.equal(own.kind,'method');
      assert.equal(own.method,method,'the result retains the canonical record');
      assert.equal(own.exactMethod,true,`${query}: registered identities are exact hits`);
      assert.equal(own.score,results[0].score,`${query}: exact identities share the highest rank`);
      assert.equal(new Set(ids(results)).size,results.length,`${query}: one card per method`);
    }
  }
});

test('acronyms, fullwidth forms and Japanese suffixes identify methods without substring collisions',()=>{
  for(const query of ['KEEP','keep','KEEP法','ＫＥＥＰ法','KEEP コード','KEEP tests']){
    assert.deepEqual(ids(findMethods(catalog,query)),['keep'],query);
  }
  for(const [query,id] of [['CG','cg'],['CG法','cg'],['CT','ct'],['CT法','ct'],
    ['LBM','d2q9-bgk'],['格子ボルツマン法','d2q9-bgk'],['DG法','dg'],
    ['Roe法','roe'],['ロー法','roe'],['GSPH','gsph']]){
    assert.equal(findMethods(catalog,query)[0]?.id,id,query);
  }
  assert.ok(!ids(findMethods(catalog,'CG')).includes('bicgstab'));
  for(const id of ['hll','hlle','hllc','hlld'])assert.deepEqual(ids(findMethods(catalog,id)),[id],id);
  assert.equal(findMethods(catalog,'SPH')[0]?.id,'sph');
  assert.deepEqual(ids(findMethods(catalog,'GSPH')),['gsph']);
  assert.ok(!ids(findMethods(catalog,'GSPH')).includes('sph'));
});

test('family names retain legitimate alternatives instead of choosing an arbitrary variant',()=>{
  const lax=ids(findMethods(catalog,'Lax'));
  for(const id of ['lax-friedrichs','lax-wendroff'])assert.ok(lax.includes(id),id);
  assert.deepEqual(ids(findMethods(catalog,'WENO')),['weno-js','weno-z']);
  assert.deepEqual(ids(findMethods(catalog,'WENO法')),['weno-js','weno-z']);
  assert.deepEqual(ids(findMethods(catalog,'WENO-Z')),['weno-z']);
  assert.deepEqual(ids(findMethods(catalog,'WENO-JS')),['weno-js']);
});

test('empty, intent-only, unknown and markup queries do not invent method cards',()=>{
  for(const query of ['', '   ', '法', 'code tests', 'zxqv-no-such-method-908172', '<script>alert(1)</script>']){
    assert.deepEqual(findMethods(catalog,query),[],query);
  }
});

const documentFor=method=>({url:path(method.url),title:method.name.en,titleEn:'',
  text:method.summary.en,headings:method.name.en,lang:'both',categoryText:'Numerical methods',method});
const ordinary=(url,title,text)=>({url,title,text,headings:title,lang:'en',categoryText:'Notes'});

test('global search puts canonical cards first and Atlas scope excludes other sites',()=>{
  const keep={...byId('keep'),aliases:catalog.find(method=>method.id==='keep').aliases};
  const search=makeSearch([
    ordinary('/other-site/keep/','Keep the evidence','Keep the source and the evidence close.'),
    ordinary('/numerical-methods-atlas/en/read/bookkeeping/','Accounting notes','A bookkeeping parameter and a bookkeeper.'),
    ordinary('/numerical-methods-atlas/en/read/keep/','KEEP smooth-flow chapter','KEEP and entropy diagnostics.'),
    documentFor(keep),
  ]);
  for(const query of ['KEEP','KEEP法','ＫＥＥＰ法']){
    const results=search(query,'ja');
    assert.equal(results[0]?.method?.id,'keep',query);
    assert.deepEqual(results.filter(result=>result.kind==='method').map(result=>result.method.id),['keep']);
    assert.ok(!results.some(result=>result.url.includes('/bookkeeping/')),'bookkeeping is not KEEP');
  }
  assert.ok(search('KEEP','en').some(result=>result.url==='/other-site/keep/'));
  const scoped=search('KEEP','en','atlas');
  assert.equal(scoped[0].method.id,'keep');
  assert.ok(scoped.every(result=>result.url.startsWith('/numerical-methods-atlas/')));
});

test('ordinary keep and bookkeeping do not become canonical methods without method metadata',()=>{
  const search=makeSearch([
    ordinary('/notes/keep/','Keep the evidence','Keep your assumptions visible.'),
    ordinary('/notes/bookkeeping/','Bookkeeping','A bookkeeping parameter.'),
  ]);
  const results=search('KEEP','en');
  assert.deepEqual(results.map(result=>result.url),['/notes/keep/']);
  assert.ok(results.every(result=>!result.method && result.kind!=='method'));
  assert.deepEqual(search('KEEP法','ja'),[]);
  assert.deepEqual(search('', 'ja'),[]);
  assert.deepEqual(search('unregistered-identity-908172','ja'),[]);
});

class Element{
  constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.ownText='';this.classes=new Set();this.classList={add:(...names)=>names.forEach(name=>this.classes.add(name))};}
  set innerHTML(_){throw new Error('Method labels must be rendered as text, not HTML');}
  set textContent(value){this.ownText=String(value);this.children=[];}
  get textContent(){return this.ownText+this.children.map(child=>child.textContent??String(child)).join('');}
  append(...children){this.children.push(...children);}
  setAttribute(name,value){this[name]=value;}
}
const descendants=node=>[node,...(node.children||[]).flatMap(descendants)];
const links=node=>descendants(node).filter(child=>child.tag==='a');
function withDOM(run){
  const previousDocument=globalThis.document,previousLocation=globalThis.location;
  const head=new Element('head'),created=[];
  try{
    globalThis.location={origin};
    globalThis.document={head,
      querySelector:()=>head.children.find(node=>node.tag==='link'&&'methodSearchStyle' in node.dataset),
      createElement:tag=>{const node=new Element(tag);created.push(node);return node;}};
    return run({created,render:(method,language='ja')=>appendMethodCard(new Element('li'),{method,title:method.name[language]||method.name.en},language)});
  }finally{globalThis.document=previousDocument;globalThis.location=previousLocation;}
}

test('published method cards expose every real related code/test URL and preserve availability',()=>withDOM(({render})=>{
  assert.equal(published.length,143);
  assert.equal(published.filter(method=>method.status==='educational-example').length,94);
  for(const method of published){
    for(const language of ['ja','en']){
      const card=render(method,language),anchors=links(card),urls=anchors.map(anchor=>new URL(anchor.href,origin));
      assert.equal(card.dataset.methodId,method.id);
      assert.ok(urls.every(url=>url.origin===origin),method.id+' same-origin links');
      if(method.status==='educational-example'){
        assert.ok(method.code_urls.length && method.test_urls.length,method.id+' public source and checks');
        for(const url of [...method.code_urls,...method.test_urls]){
          assert.ok(urls.some(target=>target.href===new URL(url,origin).href),method.id+': '+url);
        }
      }else{
        assert.ok(!urls.some(url=>url.pathname.startsWith('/code/')),method.id+' no borrowed code');
        assert.match(card.textContent,language==='ja'?/コード・テストは未公開/:/Code and tests are not published/);
      }
    }
  }
}));

test('planned and reading-only cards refuse borrowed educational files and execution guides',()=>withDOM(({render})=>{
  for(const status of ['planned','reading-only']){
    const method={...byId('keep'),status,execution_examples:byId('cg').execution_examples};
    const card=render(method);
    assert.ok(!links(card).some(anchor=>anchor.href.startsWith('/code/')));
    assert.ok(!links(card).some(anchor=>anchor.textContent==='入力・実行・判定'));
    assert.match(card.textContent,/コード・テストは未公開/);
  }
}));

test('missing Japanese explanations link to the real English page and identify that language',()=>withDOM(({render})=>{
  const englishOnly=[{...published.find(method=>method.reading?.en),reading:{en:published.find(method=>method.reading?.en).reading.en}}];
  assert.ok(englishOnly.length>0);
  for(const method of englishOnly){
    const explanation=links(render(method,'ja')).find(anchor=>anchor.textContent==='解説（英語）');
    assert.ok(explanation,method.id);
    assert.equal(explanation.hreflang,'en');
    const expected=new URL(method.reading.en,origin);expected.searchParams.set('lang','en');
    assert.equal(new URL(explanation.href,origin).href,expected.href,method.id);
  }
}));

test('untrusted method labels stay text and hostile destinations never become action links',()=>withDOM(({render,created})=>{
  const markup='<img src=x onerror=alert(1)><script>alert(2)</script>';
  for(const unsafe of ['javascript:alert(1)','data:text/html,x','https://evil.example/method/',
    '//evil.example/method/','https://user:password@hrkoyama.github.io/code/x.py']){
    const method={...byId('keep'),name:{ja:markup,en:markup},summary:{ja:markup,en:markup},url:unsafe,
      reading:{ja:unsafe,en:unsafe},code_urls:[unsafe],test_urls:[unsafe],
      execution_examples:[{guide:{ja:unsafe,en:unsafe}}]};
    const card=render(method);
    assert.equal(links(card).length,0,unsafe);
    assert.ok(card.textContent.includes(markup),'literal label retained');
  }
  assert.ok(created.every(node=>!['script','img','iframe'].includes(node.tag)));
}));

test('planned methods with new detailed reading advertise reading without implying available code',()=>withDOM(({render})=>{
 for(const id of ['ewald','fdtd','quadrature']){
  const m=published.find(m=>m.id===id),card=render(m,'ja');assert.ok(card.textContent.includes('解説あり・実装予定'));assert.ok(links(card).some(a=>a.textContent==='解説'));assert.ok(!links(card).some(a=>a.href.startsWith('/code/')));
 }
}));
