import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {makeSearch,safePath,normalize,excerpt} from '../search/engine.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../search/index.json',import.meta.url),'utf8'));
const search=makeSearch(data.documents);
test('execution intent keeps the requested published input and validation pages expanded',()=>{
  for(const [query,id] of [['Poisson code','poisson-1d-dirichlet'],['Barnes Hut code','barnes-hut'],['WENO-Z run','shu-osher'],['He SCF','helium-ground-state']]){
    const first=search(query,'ja','atlas')[0];
    assert.equal(first?.url,`/numerical-methods-atlas/code-and-data/examples/${id}/`,query);
    assert.equal(first?.executionPriority,true,query);
    assert.equal(first?.kind,'execution-example',query);
  }
  assert.equal(search('WENO-Z','ja','atlas')[0]?.method?.id,'weno-z');
  for(const lang of ['ja','en']){
    const rows=search('GSPH code',lang,'atlas').filter(row=>row.executionPriority);
    assert.deepEqual(rows.map(row=>row.url).sort(),['/numerical-methods-atlas/validation/gsph-sod/','/numerical-methods-atlas/validation/sph-pressure-acoustics/']);
    assert.ok(rows.every(row=>row.kind==='execution-example'));
    assert.ok(!search('GSPH zxqvnotfound123 code',lang,'atlas').some(row=>row.executionPriority));
  }
});
test('the public search page has one search container and no merge markers',()=>{
  const html=fs.readFileSync(new URL('../search/index.html',import.meta.url),'utf8');
  assert.equal((html.match(/<main\b/g)||[]).length,1);
  assert.equal((html.match(/data-search-index=/g)||[]).length,1);
  assert.ok(!/^(?:<{7}|>{7})(?:\s|$)/m.test(html));
});
test('the named methods and code reference is the first result in Japanese and English',()=>{
  for(const [query,lang] of [['手法・コードの対応表','ja'],['手法 対応表','ja'],['methods and code reference','en']]){
    assert.equal(search(query,lang)[0]?.url,'/numerical-methods-atlas/methods/',query);
  }
});
test('thermostat spellings resolve to explicit method records',()=>{
  for(const [query,id] of [['のせフーバー','nose-hoover'],['Nose-Hoover','nose-hoover'],['ベロシティースケーリング','velocity-rescaling'],['CSVR','stochastic-velocity-rescaling']]){
    assert.ok(search(query,'ja').some(x=>x.url===`/numerical-methods-atlas/methods/${id}/`),query);
  }
});
test('astronomy translations collapse to the chosen language and the actual chapter ranks first',()=>{
  assert.equal(search('Lane Emden','ja')[0].url,'/astronomy-step-by-step/ja/advanced/lane-emden/');
  assert.equal(search('Lane Emden','en')[0].url,'/astronomy-step-by-step/en/advanced/lane-emden/');
  const paths=search('Lane Emden','en').map(row=>row.url.replace(/\/(ja|en)\//,'/'));
  assert.equal(paths.length,new Set(paths).size);
});
test('notebook metadata resolves individual viewer IDs, and policy / thermal resources are searchable',()=>{
  assert.ok(search('量子力学').some(row=>/^\/notebooks\/notebook.html\?id=n\d+$/.test(row.url)));
  assert.ok(search('HPCI').some(row=>row.url.startsWith('/hpci-policy/')));
  assert.equal(search('熱的不安定性')[0].url,'/the-art-of-thermal-instability/');
  assert.ok(search('Poisson').slice(0,5).some(row=>row.url.startsWith('/numerical-methods-atlas/')));
});
test('confirmed material metadata finds its own notebook without indexing private contents',()=>{
  for(const query of ['千葉 柾司','膨張宇宙における構造形成']){
    assert.ok(search(query).some(row=>row.url==='/notebooks/notebook.html?id=n051'),query);
  }
  assert.ok(search('Maxwell方程式').some(row=>row.url==='/notebooks/notebook.html?id=n075'));
  const interstellar=data.documents.find(row=>row.url==='/notebooks/notebook.html?id=n090');
  assert.ok(interstellar.text.includes('1999')&&interstellar.text.includes('仮入力'));
  const nuclear=data.documents.find(row=>row.url==='/notebooks/notebook.html?id=n049');
  assert.equal(nuclear.title,'原子核物理学');
  assert.ok(!JSON.stringify(data).includes('private_reason'));
  assert.ok(data.documents.filter(row=>row.url.startsWith('/notebooks/notebook.html?')).every(row=>!/(?:course_material|exercise_solution|same_source|reference_article)/.test(row.text)));
});
test('unknown and empty queries do not leak arbitrary fallback results',()=>{
  assert.deepEqual(search('zxqvnotfound123456789'),[]);
  assert.deepEqual(search('  '),[]);
  assert.deepEqual(search('the and of'),[]);
});
test('results cannot navigate to another host, a dangerous scheme or a credential URL',()=>{
  for(const url of ['javascript:alert(1)','data:text/html,x','https://evil.example/','//evil.example/','https://hrkoyama.github.io//evil.example/','https://hrkoyama.github.io.evil.example/','https://me@hrkoyama.github.io/'])assert.equal(safePath(url),null,url);
  assert.equal(safePath('/notebooks/notebook.html?id=n024'),'/notebooks/notebook.html?id=n024');
  const untrusted=makeSearch([{url:'javascript:alert(1)',title:'needle',text:'needle',lang:'en'},{url:'/rights/',title:'needle',text:'needle',lang:'en'}]);
  assert.deepEqual(untrusted('needle').map(row=>row.url),['/rights/']);
});
test('case, full-width letters and scientific dashes are normalized without altering snippets',()=>{
  assert.equal(normalize('ＬＡＮＥ–ＥＭＤＥＮ'),'lane emden');
  assert.ok(search('ＨＰＣＩ').length>0);
  const text='The Lane–Emden equation has a known n=1 solution.';
  assert.ok(excerpt(text,'Lane').includes('Lane–Emden'));
});
test('the built index includes public content only, with clean titles and all notebook records',()=>{
  assert.equal(data.documents.filter(row=>/^\/notebooks\/notebook.html\?id=/.test(row.url)).length,41);
  assert.ok(data.documents.every(row=>safePath(row.url) && row.title.length<400 && row.text.trim()));
  // The owner publishes this exact bilingual contact on these two pages only.
  // Inline labels and links join in the atlas index, so fix their exact tokens.
  // Mask only complete whitespace-delimited tokens in those documents' text;
  // every other field, document and Gmail address retains the privacy guard.
  const publicContact='hrkoyamacontact@gmail.com';
  const contactTokens=new Map([
    ['/',[publicContact,publicContact]],
    ['/numerical-methods-atlas/',['連絡先'+publicContact,'Contact'+publicContact]]
  ]);
  for(const [url,tokens] of contactTokens){
    const rows=data.documents.filter(row=>row.url===url);
    assert.equal(rows.length,1,url+' has exactly one indexed document');
    assert.deepEqual(rows[0].text.split(/\s+/).filter(token=>token.includes('@gmail.com')),tokens,url+' has only the two authorized contact tokens');
  }
  const privacyData={...data,documents:data.documents.map(row=>contactTokens.has(row.url)
    ? {...row,text:row.text.split(/(\s+)/).map(token=>contactTokens.get(row.url).includes(token)?'[public contact]':token).join('')}
    : row)};
  const serialized=JSON.stringify(privacyData);
  assert.ok(!serialized.includes('/Users/'));
  assert.ok(!serialized.includes('@gmail.com'));
  assert.ok(!data.documents.some(row=>row.url.startsWith('/search/')));
});
