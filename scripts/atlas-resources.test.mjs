import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const data=JSON.parse(read('catalog/atlas-methods.json'));
const base=data.code_base.slice(1);
const manifest=JSON.parse(read(base+'source-manifest.json'));
const verification=JSON.parse(read(base+'verification.json'));
const hash=b=>createHash('sha256').update(b).digest('hex');

test('planned methods never inherit available implementations or verified status',()=>{
  const items=data.methods;
  assert.equal(new Set(items.map(x=>x.id)).size,items.length);
  assert.equal(items.filter(x=>x.origin==='existing-coverage-catalog').length,90);
  for(const x of items.filter(x=>x.status==='planned')){
    assert.deepEqual(x.code_modules,[]);assert.deepEqual(x.test_files,[]);
    assert.ok(x.next_deliverable.ja&&x.next_deliverable.en);
    assert.match(x.limitations.en,/No dedicated implementation/);
  }
  for(const id of ['ewald','pme','spme']){
    const method=items.find(x=>x.id===id);
    assert.equal(method.status,'educational-example');
    assert.deepEqual(method.code_modules,[]);assert.deepEqual(method.test_files,[]);
    assert.equal(method.depth_release.group,'particles');
    assert.deepEqual(method.depth_release.case_ids,id==='ewald'?['ewald']:['spme']);
  }
  assert.equal(items.find(x=>x.id==='barnes-hut').status,'educational-example');
  assert.match(items.find(x=>x.id==='pm').limitations.en,/not.*Ewald/);
});

test('all advertised source and test files are present in the verified edition',()=>{
  for(const [name,expected] of Object.entries(manifest.files)){
    assert.ok(!name.includes('..')&&!name.startsWith('/'));
    const bytes=readFileSync(new URL(base+name,root));assert.equal(hash(bytes),expected,name);
  }
  for(const x of data.methods){
    for(const name of x.code_modules)assert.ok(manifest.files['numart/'+name+'.py'],x.id);
    for(const name of x.test_files)assert.ok(manifest.files['tests/'+name+'.py'],x.id);
  }
  const archive=readFileSync(new URL(base+'atlas-code-'+data.code_edition+'.zip',root));
  assert.equal(hash(archive),verification.archive_sha256);
  assert.equal(verification.failures+verification.errors,0);
  assert.equal(verification.tests,verification.passed+verification.skipped);
  assert.equal(verification.skipped_cases.length,verification.skipped);
});

test('each method has readable HTML, JSON and Markdown with valid reading-language fallbacks',()=>{
  for(const x of data.methods){
    const route='numerical-methods-atlas/methods/'+x.id+'/';
    for(const ext of ['html','json','md'])assert.ok(existsSync(new URL(route+'index.'+ext,root)));
    const record=JSON.parse(read(route+'index.json'));assert.equal(record.status,x.status);
    const html=read(route+'index.html');assert.ok(html.includes('data-site-language="ja"')&&html.includes('data-site-language="en"'));
    for(const path of Object.values(x.reading)){const u=new URL(path,'https://hrkoyama.github.io');assert.ok(existsSync(new URL(u.pathname.slice(1)+'index.html',root)));if(u.hash)assert.ok(read(u.pathname.slice(1)+'index.html').includes('id=\"'+u.hash.slice(1)+'\"'));}
    if(x.status!=='planned'&&!x.reading.ja)assert.ok(html.includes('英語の解説を読む'));
    assert.doesNotMatch(html,/https:\/\/github\.com\/koyamarium\//);
  }
});

test('discovery routes expose the catalog and downloads without private GitHub dependencies',()=>{
  const index=read('numerical-methods-atlas/methods/index.html');
  const ids=[...index.matchAll(/\sid="([^"]+)"/g)].map(x=>x[1]);assert.equal(ids.length,new Set(ids).size);
  const publicData=JSON.parse(read('numerical-methods-atlas/methods/index.json'));
  assert.equal(publicData.methods.length,data.methods.length);
  assert.equal(publicData.code_release.sha256,verification.archive_sha256);
  assert.ok(read('llms.txt').includes('/numerical-methods-atlas/methods/'));
  for(const name of ['index.html','content.en.json','content.ja.json','content.json'])assert.doesNotMatch(read('numerical-methods-atlas/'+name),/https:\/\/github\.com\/koyamarium\/(?:numerical-methods-atlas|the-art-of-numerical-algorithms)/);
});

test('thermostat overview is bilingual and distinguishes comparisons from executable examples',()=>{
  const methods=data.methods.filter(x=>x.group.id==='thermostats');
  assert.equal(methods.length,12);
  assert.equal(methods.filter(x=>x.tier==='basic').length,8);
  assert.ok(methods.every(x=>!x.code_modules.length&&x.references.length));
  assert.deepEqual(methods.filter(x=>x.status==='educational-example').map(x=>x.id),['langevin-thermostat']);
  assert.equal(methods.filter(x=>x.status==='planned').length,11);
  const langevin=methods.find(x=>x.id==='langevin-thermostat');
  assert.equal(langevin.depth_release.group,'models');
  assert.deepEqual(langevin.depth_release.case_ids,['langevin-harmonic']);
  const result=JSON.parse(read(`code/validated-examples/${langevin.depth_release.edition}/models/results/result.json`));
  const harmonic=result.cases.find(x=>x.id==='langevin-harmonic');
  assert.equal(harmonic.passed,true);assert.ok(Object.values(harmonic.checks).every(x=>x===true));
  for(const id of ['velocity-rescaling','stochastic-velocity-rescaling','nose-hoover'])assert.ok(methods.some(x=>x.id===id));
  for(const lang of ['ja','en']){
    const route=`/numerical-methods-atlas/${lang}/read/thermostats/`;
    const html=read(route.slice(1)+'index.html');
    assert.ok(html.includes(`hreflang="${lang==='ja'?'en':'ja'}"`));
    assert.ok(read(`numerical-methods-atlas/${lang}/read/index.html`).includes(route));
    assert.ok(JSON.parse(read('guide/index.json')).pages.some(x=>x.url==='https://hrkoyama.github.io'+route));
    assert.ok(html.includes(`/numerical-methods-atlas/validation/langevin-harmonic/?lang=${lang}`));
    assert.ok(html.includes('BAOAB'));
    assert.ok(html.includes(lang==='ja'?'他の11手法は実装予定':'other 11 methods remain planned'));
  }
  const html=read('numerical-methods-atlas/methods/nose-hoover/index.html');
  assert.ok(html.includes('のせフーバー')&&html.includes('解説あり・実装予定'));
  assert.ok(html.includes('/ja/read/thermostats/'));
});

test('the atlas purpose statement remains available on the detailed page and in its generated module',async()=>{
  const copy=JSON.parse(read('catalog/atlas-purpose.json'));
  const {configureLocale}=await import('../numerical-methods-atlas/i18n.js');
  const {atlasPurpose}=await import('../numerical-methods-atlas/atlas-purpose.js');
  const fallback=read('numerical-methods-atlas/explore/index.html');
  for(const lang of ['ja','en']){
    configureLocale({},lang);
    assert.ok(fallback.includes(copy[lang].title));
    assert.ok(atlasPurpose().includes(copy[lang].title));
  }
});

test('atlas-local search includes the map and new method names with safe destinations',async()=>{
  const {searchChapters}=await import('../numerical-methods-atlas/home-search.js');
  const index=JSON.parse(read('numerical-methods-atlas/home-search-index.json'));
  assert.equal(new Set(index.entries.map(x=>x.id)).size,index.entries.length);
  assert.equal(searchChapters(index,'手法の見取り図','ja')[0]?.url,'/numerical-methods-atlas/methods/?lang=ja');
  for(const [query,id] of [['のせフーバー','nose-hoover'],['ベロシティースケーリング','velocity-rescaling'],['CSVR','stochastic-velocity-rescaling']])assert.ok(searchChapters(index,query,'ja').some(x=>x.url===`/numerical-methods-atlas/methods/${id}/?lang=ja`));
  const entry={id:'x',title:{ja:'needle',en:'needle'},headings:{ja:[],en:[]},keywords:[],routes:{ja:'https://evil.example/'}};
  assert.equal(searchChapters({entries:[entry]},'needle','ja')[0].url,null);
});

test('efficiency techniques are excluded consistently from the map and roadmap',()=>{
  const excluded=data.editorial_policy.excluded_topics.map(x=>x.id);
  assert.deepEqual(excluded,['amr','parallelization','mixed-precision']);
  assert.ok(data.methods.every(x=>!excluded.includes(x.id)));
  assert.ok(!existsSync(new URL('numerical-methods-atlas/methods/amr/index.html',root)));
  for(const lang of ['ja','en']){
    const statement=data.editorial_policy.statement[lang];
    assert.ok(read('numerical-methods-atlas/explore/index.html').includes(statement));
    assert.ok(read('numerical-methods-atlas/methods/index.html').includes(statement));
    assert.ok(read(`numerical-methods-atlas/${lang}/read/roadmap/index.html`).includes(statement));
  }
  assert.doesNotMatch(read('numerical-methods-atlas/en/read/roadmap/index.html'),/AMR remains deferred/);
});
