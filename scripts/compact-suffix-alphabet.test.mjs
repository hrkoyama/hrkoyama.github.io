// Metadata codec only: no generation, science, release extraction or network.
import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {unpackSearchIndex as unpack,VOCABULARY_ALPHABET_LIMIT} from '../frontend/search/compact-index.mjs';
const root=new URL('../',import.meta.url),python=process.env.PYTHON||'python3';
globalThis.fetch=()=>{throw Error('No network in codec fixtures');};
const clone=x=>structuredClone(x),mode='unicode-prefix-alphabet-v1';
const fixture=()=>({format:'compact-search-v1',kind:'atlas',vocabulary_encoding:'unicode-prefix-flat-v1',
 terms:[0,'a😀',1,'😁',0,'日本\uE000~s:"\\'],term_encoding:'sorted-delta',
 entries:[{id:'all',search_terms:[0,1,1],title:{ja:'日本',en:'Unicode'},
   headings:{en:[{id:'kept',level:2,title:'Unchanged section'}]},text:'~s:0 literal'}],
 details:{directory:'/search/details/',keys:['a'.repeat(64)]},
 source_index:{url:'/original.json',sha256:'0'.repeat(64)},scope:'Same full API'});
function encode(value,success=true){
 const p=spawnSync(python,['-B','-c',
  'import json,sys;sys.path.insert(0,sys.argv[1]);from compact_search import encode_vocabulary_alphabet;json.dump(encode_vocabulary_alphabet(json.load(sys.stdin)),sys.stdout,ensure_ascii=False,allow_nan=False)',
  fileURLToPath(new URL('scripts',root))],{input:JSON.stringify(value),encoding:'utf8',
  env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'},timeout:5000,maxBuffer:4*1024*1024});
 if(!success){assert.notEqual(p.status,0);return;}
 assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);
}

test('one-pass alphabet preserves astral/BMP/PUA/literal text, full headers, caller and cache identity',()=>{
 const old=fixture(),before=clone(old),next=encode(old),snapshot=clone(next),expected=unpack(old);
 assert.equal(next.vocabulary_encoding,mode);assert.ok(next.vocabulary_alphabet.includes('\uE000'));
 assert.deepEqual(unpack(next),expected);assert.deepEqual(old,before);assert.deepEqual(next,snapshot);
 assert.equal(unpack(next),unpack(next));assert.equal(unpack(unpack(next)),unpack(next));
 assert.ok(!Object.hasOwn(unpack(next),'vocabulary_alphabet'));
 assert.deepEqual(encode(old),next,'canonical deterministic mapping');
 for(const kind of ['atlas','site']){
  const x=fixture();x.kind=kind;if(kind==='site'){x.documents=x.entries;delete x.entries;}
  assert.deepEqual(unpack(encode(x)),unpack(x));
 }
});

test('frequency descending and original scalar tie order are canonical',()=>{
 const x=fixture();x.terms=[0,'bbaa'];x.entries[0].search_terms=[0];
 const packed=encode(x);assert.equal(packed.vocabulary_alphabet,'ab');assert.equal(packed.terms[1],'!!  ');
 const tie=clone(packed);tie.vocabulary_alphabet='ba';assert.throws(()=>unpack(tie));
 const descending=clone(packed);descending.terms[1]='!!! ';assert.throws(()=>unpack(descending));
 const unused=clone(packed);unused.vocabulary_alphabet+='c';assert.throws(()=>unpack(unused));
});

test('empty and over8192 scalar alphabets preserve the valid old mode',()=>{
 const empty=fixture();empty.terms=[];empty.entries[0].search_terms=[];
 assert.deepEqual(encode(empty),empty);assert.deepEqual(unpack(encode(empty)),unpack(empty));
 const large=fixture();large.terms=[0,Array.from({length:VOCABULARY_ALPHABET_LIMIT+1},(_,i)=>String.fromCodePoint(0x4000+i)).join('')];large.entries[0].search_terms=[0];
 assert.deepEqual(encode(large),large);assert.deepEqual(unpack(encode(large)),unpack(large));
});

test('unknown/orphan/wrongformat/wrongkind headers and missing companion fail closed',()=>{
 const packed=encode(fixture());
 for(const change of [x=>delete x.vocabulary_alphabet,x=>x.vocabulary_encoding='unknown',
  x=>x.vocabulary_encoding='unicode-prefix-flat-v1',x=>x.kind='unknown',x=>x.format='unpacked-search-v1']){
  const x=clone(packed);change(x);assert.throws(()=>unpack(x));
 }
 assert.throws(()=>unpack({format:'unpacked-search-v1',vocabulary_encoding:mode}));
 for(const value of [null,3,[],{},'', 'aa','\uD800','\uDC00','a'.repeat(2*VOCABULARY_ALPHABET_LIMIT+1)]){
  const x=clone(packed);x.vocabulary_alphabet=value;assert.throws(()=>unpack(x));
 }
});

test('JSON quote/backslash/DEL/control holes, outofrange codes and non-scalar suffixes are rejected',()=>{
 for(const code of ['"','\\','\u007f','\u001f','\u0080','😀','\uD800','\uDC00']){
  const x=encode(fixture());x.vocabulary_alphabet='a';x.terms=[0,code];x.entries[0].search_terms=[0];
  assert.throws(()=>unpack(x),undefined,JSON.stringify(code));
 }
});

test('original codepoint prefix lengths and restored UTF16 expansion limits remain exact',()=>{
 const x=fixture();x.terms=[0,'😀',1,'a'];x.entries[0].search_terms=[0,1];
 assert.deepEqual(unpack(encode(x)),unpack(x));
 const bad=encode(x);bad.terms[2]=2;assert.throws(()=>unpack(bad));
 const expansion={format:'compact-search-v1',kind:'atlas',vocabulary_encoding:mode,vocabulary_alphabet:'😀',
  terms:[0,' '.repeat(4101),...Array.from({length:1000},()=>[4101,'']).flat()],
  term_encoding:'sorted-delta',entries:[{search_terms:[0]}]};
 assert.throws(()=>unpack(expansion),'restored two-unit scalars count toward8.2M before prefix allocation');
 const many={...expansion,terms:new Array(1000002).fill(0)};assert.throws(()=>unpack(many));
});

test('encoder rejects invalid prefixes, surrogate suffixes and reserved/alreadyencoded companions',()=>{
 for(const terms of [[true,'a'],[-1,'a'],[1,'a'],[0.5,'a'],[0,'\uD800'],[0,'a',2,'b']]){
  const x=fixture();x.terms=terms;encode(x,false);
 }
 const x=fixture();x.vocabulary_alphabet='a';encode(x,false);
 encode(encode(fixture()),false);
});
