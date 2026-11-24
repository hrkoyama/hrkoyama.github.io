import test from 'node:test';
import assert from 'node:assert/strict';
import {searchDOM,flushSearch,descendants} from './fixtures/search-dom.mjs';

const index={entries:[{id:'execution-sod',kind:'execution-example',title:{ja:'Sod衝撃波管',en:'Sod shock tube'},text:{ja:'Sod test shock tube',en:'Sod test shock tube'},focus_keywords:['Sod'],routes:{ja:'/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja',en:'/numerical-methods-atlas/code-and-data/examples/sod/?lang=en'}}]};
const response=data=>({ok:true,json:async()=>data});
const first=dom=>descendants(dom.nodes('search-results')).find(x=>x.tag==='a')?.href;
let sequence=0;
async function boot(dom){
 const main=dom.document.querySelector('[data-search-index]');
 main.dataset.searchIndex='/pending-site-index.json';main.dataset.atlasSearchIndex='/atlas-index.json';
 await import('../search/search.js?failure-order='+sequence++);await flushSearch();
}
for(const language of ['ja','en']){
 test(language+': obsolete all-site failure cannot erase the newer atlas result',async()=>{
  let reject;const pending=new Promise((_,no)=>{reject=no;});
  const dom=searchDOM({kind:'site',language,query:'Sod test',fetch:async url=>String(url).includes('pending-site')?pending:response(index)});
  try{
   dom.location.search='?scope=all&lang='+language;await boot(dom);
   dom.location.search='?scope=atlas&lang='+language;dom.fireWindow('popstate');await flushSearch();
   const expected=first(dom),status=dom.nodes('search-status').textContent;
   assert.equal(expected,'/numerical-methods-atlas/code-and-data/examples/sod/?lang='+language);
   reject(Error('obsolete request failed'));await flushSearch();
   assert.equal(first(dom),expected);assert.equal(dom.nodes('search-status').textContent,status);
  }finally{dom.restore();}
 });
 test(language+': obsolete failure cannot replace the ready state after clearing the query',async()=>{
  let reject;const pending=new Promise((_,no)=>{reject=no;});
  const dom=searchDOM({kind:'site',language,query:'Sod test',fetch:async()=>pending});
  try{
   await boot(dom);dom.location.hash='';dom.fireWindow('hashchange');await flushSearch();
   const ready=dom.nodes('search-status').textContent;
   reject(Error('obsolete request failed'));await flushSearch();
   assert.equal(dom.nodes('search-status').textContent,ready);assert.equal(dom.nodes('search-results').children.length,0);
  }finally{dom.restore();}
 });
 test(language+': a current failure remains visible and the same query can retry',async()=>{
  let attempts=0;const dom=searchDOM({kind:'site',language,query:'Sod test',fetch:async()=>{if(++attempts===1)throw Error('current failure');return response(index);}});
  try{
   await boot(dom);assert.match(dom.nodes('search-status').textContent,language==='ja'?/読み込めませんでした/:/could not be loaded/);
   dom.fireWindow('popstate');await flushSearch();assert.ok(first(dom)?.includes('/sod/'));assert.equal(attempts,2);
  }finally{dom.restore();}
 });
 test(language+': obsolete successful response cannot replace a newer scope',async()=>{
  let resolve;const pending=new Promise(yes=>{resolve=yes;});
  const dom=searchDOM({kind:'site',language,query:'Sod test',fetch:async url=>String(url).includes('pending-site')?pending:response(index)});
  try{
   dom.location.search='?scope=all&lang='+language;await boot(dom);
   dom.location.search='?scope=atlas&lang='+language;dom.fireWindow('popstate');await flushSearch();const expected=first(dom);
   resolve(response({documents:[{url:'/using/',title:'Sod test',text:'Sod test',lang:language}]}));await flushSearch();assert.equal(first(dom),expected);
  }finally{dom.restore();}
 });
}
