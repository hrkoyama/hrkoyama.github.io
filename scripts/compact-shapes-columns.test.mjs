// Storage-only fixtures. No generators, solvers, release extraction or network.
import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {unpackSearchIndex as unpack,restoreRowShapes,ROW_STRING_LIMITS} from '../frontend/search/compact-index.mjs';
const root=new URL('../',import.meta.url),python=process.env.PYTHON||'python3';
globalThis.fetch=()=>{throw Error('No network in storage fixtures');};
const clone=x=>structuredClone(x);
const fixture=()=>({format:'compact-search-v1',kind:'atlas',vocabulary_encoding:'unicode-prefix-flat-v1',
 terms:[0,'a😀',1,'😁',0,'日本\uE000'],term_encoding:'sorted-delta',
 entries:[{id:'one',search_terms:[0,1,1],title:{ja:'共通見出し',en:'Same title'},
  nested:[[],{},[-1,0],[{first:'共通見出し',second:'~s:0 literal'}]],text:'Same title'},
  {id:'two',search_terms:[1],title:{ja:'共通見出し',en:'Same title'},text:'literal',empty:{}}],
 details:{directory:'/search/details/',keys:['a'.repeat(64)]},source_index:{url:'/same.json',sha256:'0'.repeat(64)},scope:'Full unchanged API'});
function encode(value,success=true){
 const p=spawnSync(python,['-B','-c',
  'import json,sys;sys.path.insert(0,sys.argv[1]);from compact_search import encode_row_strings,encode_vocabulary_alphabet,encode_vocabulary_columns,encode_row_shapes;data=json.load(sys.stdin);data=encode_row_strings(data);data=encode_vocabulary_alphabet(data);data=encode_vocabulary_columns(data);data=encode_row_shapes(data);json.dump(data,sys.stdout,ensure_ascii=False,allow_nan=False)',
  fileURLToPath(new URL('scripts',root))],{input:JSON.stringify(value),encoding:'utf8',timeout:5000,maxBuffer:6*1024*1024,
  env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}});
 if(!success){assert.notEqual(p.status,0);return;}
 assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);
}

test('key shapes and prefix columns preserve whole headers, key order, Unicode, arrays, cache and caller',()=>{
 const old=fixture(),before=clone(old),next=encode(old),snapshot=clone(next),expected=unpack(old);
 assert.equal(next.row_structure_encoding,'key-shapes-v1');assert.equal(next.vocabulary_encoding,'unicode-prefix-alphabet-columns-v1');
 assert.deepEqual(unpack(next),expected);assert.equal(JSON.stringify(unpack(next)),JSON.stringify(expected));
 assert.deepEqual(old,before);assert.deepEqual(next,snapshot);assert.equal(unpack(next),unpack(next));
 assert.equal(unpack(unpack(next)),unpack(next));assert.deepEqual(encode(old),next);
 for(const key of ['row_shapes','row_structure_encoding','vocabulary_prefixes','vocabulary_alphabet'])assert.ok(!Object.hasOwn(unpack(next),key));
 for(const kind of ['atlas','site']){
  const x=fixture();x.kind=kind;if(kind==='site'){x.documents=x.entries;delete x.entries;}
  assert.deepEqual(unpack(encode(x)),unpack(x));
 }
});

test('shape-only and all legacy formats remain supported, including empty rows',()=>{
 const x=fixture(),next=encode(x),flat=clone(next),prefixes=Buffer.from(flat.vocabulary_prefixes,'base64');
 // This fixture has only one-byte prefixes; reconstruct the legacy alphabet wire.
 flat.terms=flat.terms.flatMap((s,i)=>[prefixes[i],s]);flat.vocabulary_encoding='unicode-prefix-alphabet-v1';delete flat.vocabulary_prefixes;
 assert.deepEqual(unpack(flat),unpack(x));
 const empty={format:'compact-search-v1',kind:'atlas',terms:[],entries:[]};assert.deepEqual(unpack(encode({...empty,vocabulary_encoding:'unicode-prefix-flat-v1'})),unpack({...empty,vocabulary_encoding:'unicode-prefix-flat-v1'}));
 const plain={format:'unpacked-search-v1',entries:[]};assert.equal(unpack(plain),plain);
});

test('prototype-looking keys are own data with no prototype pollution and key order survives',()=>{
 const x=fixture();x.entries[0].hostile=JSON.parse('{"__proto__":{"polluted":"no"},"constructor":"data","2":"two","1":"one"}');
 const actual=unpack(encode(x)),expected=unpack(x);assert.deepEqual(actual,expected);assert.equal(JSON.stringify(actual),JSON.stringify(expected));
 assert.ok(Object.hasOwn(actual.entries[0].hostile,'__proto__'));assert.equal({}.polluted,undefined);
});

test('missing, orphan, wrong-kind, wrong-format and unknown structure headers fail closed',()=>{
 for(const change of [x=>delete x.row_shapes,x=>x.row_structure_encoding='unknown',x=>x.row_shapes=null,
  x=>x.kind='unknown',x=>x.format='unpacked-search-v1']){
  const x=encode(fixture());change(x);assert.throws(()=>unpack(x));
 }
 assert.throws(()=>unpack({format:'compact-search-v1',kind:'atlas',terms:[],entries:[],row_shapes:[]}));
 assert.throws(()=>restoreRowShapes({format:'unpacked-search-v1',row_structure_encoding:'key-shapes-v1',row_shapes:[]}));
});

test('malformed shapes, duplicate keys/layouts, unused shapes, arity, tags and sparse arrays are rejected',()=>{
 for(const change of [x=>x.row_shapes.push(['unused']),x=>x.row_shapes.push(x.row_shapes[0]),
  x=>x.row_shapes[0].push(x.row_shapes[0][0]),x=>x.row_shapes[0][0]=3,x=>x.row_shapes[0][0]='\uD800',
  x=>x.entries[0][0]=-1,x=>x.entries[0][0]=0.5,x=>x.entries[0][0]=99999,
  x=>x.entries[0].pop(),x=>x.entries[0].push(null),x=>delete x.entries[0][1],
  x=>x.entries[0][1]={unencoded:true},x=>x.entries[0][1]=[0],x=>x.entries[0][1]=Infinity]){
  const x=encode(fixture());change(x);assert.throws(()=>unpack(x));
 }
 const huge=encode(fixture());huge.row_shapes=new Array(ROW_STRING_LIMITS.pool+1).fill([]);assert.throws(()=>unpack(huge));
 const many=encode(fixture());many.entries=new Array(ROW_STRING_LIMITS.rows+1).fill(many.entries[0]);assert.throws(()=>unpack(many));
 const deep=encode(fixture());let v=null;for(let i=0;i<ROW_STRING_LIMITS.depth+1;i++)v=[-1,v];deep.entries[0][1]=v;assert.throws(()=>unpack(deep));
});

test('vocabulary columns reject noncanonical base64, overlong/truncated/overflow values and mismatched counts',()=>{
 for(const value of [null,3,[],{},'AA','AB==','gAA=','gA==','/////w8=','AA==','AAAAAAAA','-w==','_w==','AA==\n']){
  const x=encode(fixture());x.vocabulary_prefixes=value;assert.throws(()=>unpack(x),undefined,JSON.stringify(value));
 }
 for(const change of [x=>delete x.vocabulary_prefixes,x=>x.vocabulary_encoding='unknown',
  x=>x.vocabulary_encoding='unicode-prefix-alphabet-v1',x=>delete x.terms[0],x=>x.terms.push('a')]){
  const x=encode(fixture());change(x);assert.throws(()=>unpack(x));
 }
 const orphan=fixture();orphan.vocabulary_prefixes='AAAA';assert.throws(()=>unpack(orphan));
});

test('prefix codepoint and restored UTF16 budgets still guard columns before reconstruction',()=>{
 const x=fixture();x.terms=[0,'😀',1,'a'];for(const row of x.entries)row.search_terms=[0,1];
 assert.deepEqual(unpack(encode(x)),unpack(x));
 const bad=encode(x);bad.vocabulary_prefixes=Buffer.from([0,2]).toString('base64');assert.throws(()=>unpack(bad));
 const suffix=' '.repeat(4101),prefixes=Buffer.from([0,...Array.from({length:1000},()=>[0x85,0x20]).flat()]).toString('base64');
 const large={format:'compact-search-v1',kind:'atlas',vocabulary_encoding:'unicode-prefix-alphabet-columns-v1',vocabulary_alphabet:'😀',
  vocabulary_prefixes:prefixes,terms:[suffix,...new Array(1000).fill('')],entries:[{search_terms:[0]}]};
 assert.throws(()=>unpack(large));
});
