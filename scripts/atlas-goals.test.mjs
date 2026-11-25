import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {goals,matchGoals} from '../search/goals-data.mjs';
import {findMethods} from '../search/method-search.mjs';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
import {homeOverviewPage} from '../numerical-methods-atlas/home-overview.js';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
const read=p=>JSON.parse(fs.readFileSync(new URL('../'+p,import.meta.url)));
const methods=read('numerical-methods-atlas/methods/index.json').methods;
const global=makeSearch(read('search/index.json').documents);
const local=read('numerical-methods-atlas/home-search-index.json');
test('new domains distinguish runnable atoms, reading-only molecular DFT, scoped Langevin distributions and biological models',()=>{
 for(const lang of ['ja','en']){
  for(const query of ['原子の電子状態を計算したい','compute atomic electronic states']){
   const rows=findMethods(methods,query,lang);assert.ok(rows.some(x=>x.method.id==='hartree-fock'));
   assert.ok(rows.some(x=>x.method.execution_examples.some(e=>e.id==='helium-ground-state')));
  }
  for(const query of ['分子のDFTを学びたい','explore molecular DFT']){
   for(const rows of [findMethods(methods,query,lang),global(query,lang,'atlas'),searchChapters(local,query,lang)]){
    const candidates=rows.filter(x=>x.purposeScope);assert.ok(candidates.length,query);
    for(const x of candidates){
     assert.notEqual(x.method.status,'educational-example',query);
     assert.equal(x.method.code_urls.length,0,query);assert.equal(x.method.test_urls.length,0,query);
     assert.equal(x.method.execution_examples.length,0,query);assert.ok(x.method.reading[lang]);
    }
   }
  }
 }
 assert.equal(methods.find(m=>m.id==='kohn-sham-dft').status,'educational-example','goal restrictions do not change the canonical atomic implementation status');
 const temperature=findMethods(methods,'温度を制御したい');
 const langevin=temperature.find(x=>x.method.id==='langevin-thermostat');assert.equal(langevin?.method.status,'educational-example');assert.ok(langevin.method.execution_examples.some(e=>e.id==='langevin-harmonic'));
 const csvr=temperature.find(x=>x.method.id==='stochastic-velocity-rescaling');assert.equal(csvr?.method.status,'educational-example');
 assert.deepEqual(new Set(csvr.method.execution_examples.map(x=>x.id)),new Set(['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic','projected-canonical-dof']));
 const deterministic=['velocity-rescaling','berendsen-thermostat','nose-hoover','nose-hoover-chains'];
 for(const id of deterministic){const actual=temperature.find(x=>x.method.id===id)?.method;assert.equal(actual?.status,'educational-example',id);assert.deepEqual(actual.execution_examples.map(x=>x.id),['deterministic-thermostat-contrasts']);assert.ok(actual.code_urls.length&&actual.test_urls.length);}
 assert.deepEqual(new Set(temperature.map(x=>x.method.id)),new Set(['langevin-thermostat','stochastic-velocity-rescaling',...deterministic]));
 const legacyBio=['bio-populations','bio-epidemics','bio-patterns','bio-reaction-fourier','bio-fhn'];
 const additions=[['bio-enzyme-qssa','enzyme-qssa'],['bio-lotka-volterra','lotka-volterra'],['bio-seir-linearization','seir-linearization']];
 const bio=findMethods(methods,'生物モデルを調べたい');
 const algorithms=bio.filter(x=>x.method.resource_type!=='model');
 assert.deepEqual(algorithms.map(x=>x.id),goals.find(row=>row.id==='biological-models').methods,'only explicitly selected canonical algorithms supplement the model resources');
 const models=bio.filter(x=>x.method.resource_type==='model');
 const runnable=models.filter(x=>x.method.status==='educational-example').map(x=>x.id);
 assert.deepEqual(runnable.slice(0,5),legacyBio,'the original five runnable model resources retain their order');
 assert.deepEqual(runnable,[...legacyBio,...additions.map(([id])=>id)],'only the three separately scoped models are added');
 const digest=path=>createHash('sha256').update(fs.readFileSync(new URL('../'+path,import.meta.url))).digest('hex');
 const freezePath='scripts/fixtures/atlas-batch78-87-freeze.json';
 assert.equal(digest(freezePath),'b5ea04031e443f0ec3c2e20e610034bcbbbc326f5884350d454df2fbad85b7ad');
 const packet=read(freezePath).canonical_packets['small-models'];
 for(const [file,hash] of [['source-manifest.json',packet.manifest_sha256],['verification.json',packet.verification_sha256],[packet.archive_file,packet.archive_sha256]])assert.equal(digest(packet.base+file),hash,file+' canonical packet identity');
 const canonical=read(packet.base+'cases.json'),manifest=read(packet.base+'source-manifest.json');
 assert.equal(digest(packet.base+'cases.json'),manifest.files['cases.json']);
 for(const lang of ['ja','en']){
  const scoped=findMethods(methods,'生物モデルを調べたい',lang);
  assert.equal(scoped.find(row=>row.id==='bio-excitation').method.status,'reading-only');
  assert.deepEqual(scoped.find(row=>row.id==='bio-excitation').method.execution_examples,[]);
  for(const [resourceID,caseID] of additions){
   const actual=scoped.find(row=>row.id===resourceID)?.method,source=canonical.find(row=>row.id===caseID),entry=read('numerical-methods-atlas/validation/'+caseID+'/index.json');
   assert.ok(actual&&source,resourceID);assert.equal(actual.status,'educational-example');
   assert.deepEqual(actual.supplemental_examples,[caseID]);assert.deepEqual(actual.execution_examples.map(row=>row.id),[caseID]);
   assert.deepEqual(actual.name,source.title);assert.deepEqual(actual.summary,source.limits);
   assert.equal(actual.reading[lang],'https://hrkoyama.github.io/numerical-methods-atlas/'+lang+'/read/validation-small-models/#'+caseID);
   assert.equal(entry.release.base,'https://hrkoyama.github.io/'+packet.base);
   assert.deepEqual(actual.code_urls,entry.release.code_urls);assert.deepEqual(actual.test_urls,entry.release.test_urls);
  }
 }
});
test('static new-domain sections have status labels and do not advertise atomic code for molecules or simulations for surveys',()=>{
 const html=fs.readFileSync(new URL('../numerical-methods-atlas/start/index.html',import.meta.url),'utf8');
 for(const id of ['molecular-dft'])for(const lang of ['ja','en']){
  const section=html.match(new RegExp(`<article[^>]+id="${id}-${lang}"[\\s\\S]*?</article>`))?.[0];assert.ok(section,id);
  assert.ok(section.includes('goal-availability'));assert.ok(!section.includes('href="https://hrkoyama.github.io/code/'));
  assert.ok(!section.includes('/code-and-data/examples/'));
 }
 for(const id of ['langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'])assert.ok(html.includes('/validation/'+id+'/'));
 assert.ok(html.includes('Langevin') && html.includes('BAOAB'));
 assert.ok(html.includes('Reading only; no dedicated implementation'));
});
test('the concise landing leads to the complete goal selector without duplicating its choices',()=>{
 const page=fs.readFileSync(new URL('../numerical-methods-atlas/start/index.html',import.meta.url),'utf8');
 for(const lang of ['ja','en']){
  configureLocale(read('numerical-methods-atlas/locales/messages.json'),lang);
  const runtime=homeOverviewPage(read('numerical-methods-atlas/coverage.json'));
  assert.ok(runtime.includes(`/numerical-methods-atlas/start/?lang=${lang}`));
  assert.equal((runtime.match(/class="home-goal-choice"/g)||[]).length,0);
  for(const g of goals){
   assert.ok(page.includes(`id="${g.id}-${lang}"`),'complete goal '+g.id);
   assert.ok(page.includes(`href="#${g.id}-${lang}"`),'direct goal '+g.id);
  }
  assert.ok(!runtime.includes('atlas-metrics')&&!runtime.includes('atlas-ways'));
 }
});
test('natural goal phrases reach conditional candidate methods through both searches',()=>{
 for(const [q,id] of [['衝撃波を計算したい','hllc'],['渦を低散逸で解きたい','keep'],['resolve a smooth vortex','keep'],['solve poisson equation','cg'],['磁場の発散誤差を抑えたい','ct'],['硬い方程式を時間積分したい','sdirk2'],['粒子の重力を計算したい','barnes-hut']]){
  for(const lang of ['ja','en']){
   for(const rows of [findMethods(methods,q,lang),global(q,lang,'atlas'),searchChapters(local,q,lang)]){
    const row=rows.find(x=>x.method?.id===id);assert.ok(row,q);assert.ok(row.purposeScope,q+' conditions');
   }
  }
 }
});
test('explicit scopes distinguish Euler shocks, smooth KEEP, magnetic operators and executable examples',()=>{
 for(const row of findMethods(methods,'衝撃波を計算したい','ja')){
  assert.ok((row.method.execution_examples || []).every(e=>['sod','shu-osher','shu-independent','saltzman-ale-piston','gsph-sod'].includes(e.id)),'Euler goal must not borrow MHD or unselected particle execution examples');
  assert.ok(!(row.method.execution_examples||[]).some(e=>e.id==='sph-pressure-acoustics'),'the shared GSPH method does not imply an acoustics shock example');
 }
 assert.ok(!matchGoals('相対論の衝撃波を計算したい').some(g=>g.id==='shocks'));
 assert.ok(!matchGoals('MHD shock waves').some(g=>g.id==='shocks'));
 assert.ok(!matchGoals('without shock waves').some(g=>g.id==='shocks'));
 assert.deepEqual(matchGoals('zxqvnotfound'),[]);
 assert.ok(!matchGoals('衝撃波を低散逸で計算したい').some(g=>g.id==='smooth-vortex'));
 assert.ok(!matchGoals('MHDを低散逸で解きたい').some(g=>g.id==='smooth-vortex'));
 assert.ok(!matchGoals('非圧縮の渦を低散逸で解きたい').some(g=>g.id==='smooth-vortex'));
 assert.match(goals.find(g=>g.id==='smooth-vortex').scope.en,/neither a shock stabilizer/);
 const magneticScope=goals.find(g=>g.id==='magnetic-divergence').scope.en;
 assert.match(magneticScope,/Brio.*1D fluxes/);
 assert.match(magneticScope,/GLM Fourier case is a constraint diagnostic, separately from general multidimensional MHD validation/);
 assert.match(magneticScope,/Separate spatial and time-integration errors/);
});
test('all goal resources exist and the bilingual static entry remains usable without script',()=>{
 const examples=read('catalog/atlas-execution-examples.json').examples;
 const html=fs.readFileSync(new URL('../numerical-methods-atlas/start/index.html',import.meta.url),'utf8');
 for(const g of goals){
  for(const lang of ['ja','en']){assert.ok(html.includes(`id="${g.id}-${lang}"`));assert.ok(g.scope[lang]);}
  for(const id of g.methods){const m=methods.find(m=>m.id===id);assert.ok(m,id);assert.ok(html.includes(m.url));}
  for(const id of g.examples){assert.ok(examples.some(e=>e.id===id));assert.ok(fs.existsSync(new URL('../numerical-methods-atlas/code-and-data/examples/'+id+'/index.html',import.meta.url)));}
 }
 assert.ok(html.includes('Related tests'));assert.ok(html.includes('関連テスト'));
});
