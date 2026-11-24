// Storage-only fixtures: no generators, solvers, downloads or numerical imports.
import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {unpackSearchIndex as unpack,restoreRowStrings,restoreRowPool,ROW_STRING_LIMITS} from '../frontend/search/compact-index.mjs';
const root=new URL('../',import.meta.url),python=process.env.PYTHON||'python3';
globalThis.fetch=()=>{throw Error('No network in storage fixtures');};
const clone=x=>structuredClone(x);
const fixture=()=>({format:'compact-search-v1',kind:'atlas',terms:['one'],term_encoding:'sorted-delta',
 entries:[{id:'one',title:{ja:'日本語😀の共通見出し',en:'shared title'},search_terms:[0],raw:'~s:0 literal',
   nested:JSON.parse('{"__proto__":"日本語😀の共通見出し","constructor":"shared title","value":["~s:0 literal"]}')},
  {id:'two',title:{ja:'日本語😀の共通見出し',en:'shared title'},search_terms:[0],raw:'~s:0 literal'}],
 details:{directory:'/search/details/',keys:['a'.repeat(64),'a'.repeat(64)]},scope:'Full unchanged public API'});
function produce(value,success=true){
 const p=spawnSync(python,['-B','-c',
  'import json,sys;sys.path.insert(0,sys.argv[1]);from compact_search import encode_row_strings,encode_row_pool;data=json.load(sys.stdin);data=encode_row_pool(encode_row_strings(data));json.dump(data,sys.stdout,ensure_ascii=False,allow_nan=False)',
  fileURLToPath(new URL('scripts',root))],{input:JSON.stringify(value),encoding:'utf8',timeout:5000,maxBuffer:12*1024*1024,env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}});
 if(!success){assert.notEqual(p.status,0);return;}
 assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);
}
const b64=values=>{const bytes=[];for(let n of values){while(n>=128){bytes.push((n%128)|128);n=Math.floor(n/128);}bytes.push(n);}return Buffer.from(bytes).toString('base64');};
const pool=(strings,prefixes)=>({format:'compact-search-v1',kind:'atlas',row_string_encoding:'shared-raw-strings-v1',row_strings:strings,row_pool_encoding:'unicode-prefix-columns-v1',row_pool_prefixes:b64(prefixes),terms:[],entries:[]});

test('pool prefixes preserve every value, own key order, escaped raw token, caller and cached API',()=>{
 for(const kind of ['atlas','site']){
  const x=fixture();x.kind=kind;if(kind==='site'){x.documents=x.entries;delete x.entries;}
  const before=clone(x),next=produce(x),saved=clone(next),expected=unpack(x),actual=unpack(next);
  assert.equal(next.row_pool_encoding,'unicode-prefix-columns-v1');assert.deepEqual(actual,expected);
  assert.equal(JSON.stringify(actual),JSON.stringify(expected));assert.deepEqual(x,before);assert.deepEqual(next,saved);
  assert.equal(unpack(next),actual);assert.equal(unpack(actual),actual);assert.deepEqual(produce(x),next);
  assert.equal({}.polluted,undefined);assert.ok(Object.hasOwn(actual[kind==='atlas'?'entries':'documents'][0].nested,'__proto__'));
  for(const k of ['row_pool_encoding','row_pool_prefixes','row_strings','row_string_encoding'])assert.ok(!Object.hasOwn(actual,k));
 }
});

test('old raw pool and unpooled payloads remain accepted, including empty optional pool',()=>{
 const next=produce(fixture()),raw=restoreRowPool(next),saved=clone(raw);
 assert.deepEqual(unpack(raw),unpack(next));assert.deepEqual(raw,saved);assert.equal(restoreRowPool(raw),raw);
 const old={format:'unpacked-search-v1',entries:[]};assert.equal(unpack(old),old);
 assert.deepEqual(restoreRowStrings(pool([],[])),{format:'compact-search-v1',kind:'atlas',terms:[],entries:[]});
});

test('prefixes count Unicode scalar values and preserve pool IDs over multi-byte lengths',()=>{
 const p=pool(['😀abc','😁','中\uE000','end'],[0,1,0,2]);
 assert.deepEqual(restoreRowPool(p).row_strings,['😀abc','😀😁','中\uE000','中\uE000end']);
 const text='α'.repeat(500);assert.deepEqual(restoreRowPool(pool([text,'!'],[0,500])).row_strings,[text,text+'!']);
});

test('missing, orphan, unknown, wrong-kind and wrong-format pool headers fail closed',()=>{
 for(const change of [x=>delete x.row_pool_prefixes,x=>delete x.row_pool_encoding,
  x=>x.row_pool_encoding='unknown',x=>x.row_pool_encoding=undefined,x=>x.kind='bad',
  x=>x.format='unpacked-search-v1',x=>delete x.row_string_encoding,x=>x.row_string_encoding='unknown']){
  const x=produce(fixture());change(x);assert.throws(()=>unpack(x));
 }
 assert.throws(()=>unpack({format:'unpacked-search-v1',row_pool_prefixes:''}));
 assert.throws(()=>unpack({format:'unpacked-search-v1',row_pool_encoding:'unicode-prefix-columns-v1'}));
});

test('noncanonical base64 and overlong, truncated, overflow or wrong-count varints fail closed',()=>{
 for(const value of [null,[],3,'AA','AB==','gAA=','gA==','/////w8=','AA==\n','_w==','-w==','AAAA']){
  const x=pool(['a'],[0]);x.row_pool_prefixes=value;assert.throws(()=>restoreRowPool(x),undefined,JSON.stringify(value));
 }
 assert.throws(()=>restoreRowPool(pool(['a'],[1])));
 assert.throws(()=>restoreRowPool(pool(['a','b'],[0])));
 assert.throws(()=>restoreRowPool(pool(['a'],[0,0])));
});

test('dense scalar unique pools retain original string, count and aggregate UTF16 limits',()=>{
 for(const strings of [null,{},[null],['\uD800'],['a','a'],['a'.repeat(ROW_STRING_LIMITS.stringUnits+1)]]){
  const x=pool([],[]);x.row_strings=strings;x.row_pool_prefixes=typeof strings?.length==='number'?b64(new Array(strings.length).fill(0)):'';
  assert.throws(()=>restoreRowPool(x));
 }
 const sparse=pool(['a','b'],[0,0]);delete sparse.row_strings[1];assert.throws(()=>restoreRowPool(sparse));
 assert.throws(()=>restoreRowPool(pool(new Array(ROW_STRING_LIMITS.pool+1).fill(''),[])));
 const first='x'.repeat(1000),suffixes=[first,...Array.from({length:9000},(_,i)=>String(i))];
 assert.throws(()=>restoreRowPool(pool(suffixes,[0,...new Array(9000).fill(1000)])));
 assert.throws(()=>restoreRowPool(pool(['😀'.repeat(500000),'x'],[0,500000])));
});

test('producer refuses reserved headers, invalid pools and non-scalar input',()=>{
 for(const change of [x=>x.row_pool_encoding='x',x=>x.row_pool_prefixes='',x=>x.row_strings=[],x=>x.entries[0].raw='\uD800']){
  const x=fixture();change(x);produce(x,false);
 }
});
