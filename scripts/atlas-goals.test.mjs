import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {goals,matchGoals} from '../search/goals-data.mjs';
import {findMethods} from '../search/method-search.mjs';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
const read=p=>JSON.parse(fs.readFileSync(new URL('../'+p,import.meta.url)));
const methods=read('numerical-methods-atlas/methods/index.json').methods;
const global=makeSearch(read('search/index.json').documents);
const local=read('numerical-methods-atlas/home-search-index.json');
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
 assert.ok(!matchGoals('相対論の衝撃波を計算したい').some(g=>g.id==='shocks'));
 assert.ok(!matchGoals('MHD shock waves').some(g=>g.id==='shocks'));
 assert.ok(!matchGoals('without shock waves').some(g=>g.id==='shocks'));
 assert.deepEqual(matchGoals('zxqvnotfound'),[]);
 assert.ok(!matchGoals('衝撃波を低散逸で計算したい').some(g=>g.id==='smooth-vortex'));
 assert.ok(!matchGoals('MHDを低散逸で解きたい').some(g=>g.id==='smooth-vortex'));
 assert.ok(!matchGoals('非圧縮の渦を低散逸で解きたい').some(g=>g.id==='smooth-vortex'));
 assert.match(goals.find(g=>g.id==='smooth-vortex').scope.en,/neither a shock stabilizer/);
 assert.match(goals.find(g=>g.id==='magnetic-divergence').scope.en,/does not validate multidimensional/);
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
