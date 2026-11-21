import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {makeSearch,safePath,normalize,excerpt} from '../search/engine.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../search/index.json',import.meta.url),'utf8'));
const search=makeSearch(data.documents);
test('the named method map is the first result in Japanese and English',()=>{
  for(const [query,lang] of [['手法の見取り図','ja'],['手法 見取り図','ja'],['map of numerical methods','en']]){
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
  const serialized=JSON.stringify(data);
  assert.ok(!serialized.includes('/Users/'));
  assert.ok(!serialized.includes('@gmail.com'));
  assert.ok(!data.documents.some(row=>row.url.startsWith('/search/')));
});
