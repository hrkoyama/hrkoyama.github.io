// Lossless storage codec: targeted metadata tests, no generation or network.
import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {dirname,resolve} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {restoreRowStrings,ROW_STRING_LIMITS,unpackSearchIndex as candidate} from '../frontend/search/compact-index.mjs';
const repo=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const legacy=candidate;
const python=process.env.PYTHON||'python3';
globalThis.fetch=()=>{throw Error('No network in codec tests');};
const clone=value=>structuredClone(value),long='Repeated metadata string, retained exactly. '.repeat(3);
const fixture=()=>({format:'compact-search-v1',kind:'atlas',terms:['a','b','日本','~s:0'],term_encoding:'sorted-delta',
 entries:[{id:'one',search_terms:[0,1,1],text:long,title:{ja:long,en:'First'},text_ref:'a'.repeat(64)},
 {id:'two',search_terms:{ja:[2],en:[0,1]},text:long,details_ref:'b'.repeat(64)}],
 details:{directory:'/search/details/',keys:['a'.repeat(64),'b'.repeat(64)]},
 source_index:{url:'/unchanged.json',sha256:'0'.repeat(64)},scope:'All fields retained.'});
function encode(value){
 const code="import json,sys;sys.path.insert(0,'scripts');from compact_search import encode_row_strings;print(json.dumps(encode_row_strings(json.load(sys.stdin)),ensure_ascii=False,allow_nan=False))";
 const p=spawnSync(python,['-B','-c',code],{cwd:repo,input:JSON.stringify(value),encoding:'utf8',env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'},maxBuffer:4*1024*1024,timeout:5000});
 assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);
}
const packed=encode(fixture());

test('Python pooling preserves Unicode, every escaped prefix, raw pool strings, complete headers and cache identity',()=>{
 const original=fixture();
 original.entries[0].literal=['~s:0','~s:','~s:~0','~s:00','~s:constructor','~s:~~'];
 original.entries[0].astral='😀𠮷'.repeat(32);original.entries[1].astral=original.entries[0].astral;
 original.entries[0].rawPrefix='~s:0'+long;original.entries[1].rawPrefix=original.entries[0].rawPrefix;
 const before=clone(original),next=encode(original),snapshot=clone(next);
 assert.equal(next.row_string_encoding,'shared-raw-strings-v1');assert.deepEqual(next.terms,original.terms);
 assert.deepEqual(restoreRowStrings(next),original);assert.deepEqual(candidate(next),legacy(original));
 assert.equal(candidate(next),candidate(next));assert.equal(candidate(candidate(next)),candidate(next));
 assert.deepEqual(original,before);assert.deepEqual(next,snapshot);
 assert.ok(!Object.hasOwn(candidate(next),'row_string_encoding'));assert.ok(!Object.hasOwn(candidate(next),'row_strings'));
 const raw=clone(packed);raw.row_strings=['~s:0'];raw.entries[0].sentinel='~s:0';
 // Replace every pre-existing reference before selecting this deliberately raw pool.
 raw.entries=[{id:'raw',search_terms:[],sentinel:'~s:0'}];raw.details.keys=[];
 assert.equal(candidate(raw).entries[0].sentinel,'~s:0','pool contents are not recursively decoded');
});

test('old compact arrays, absolute term IDs and already unpacked objects retain the legacy API',()=>{
 const old=fixture();assert.equal(restoreRowStrings(old),old);assert.deepEqual(candidate(old),legacy(old));
 const absolute=fixture();delete absolute.term_encoding;absolute.entries[0].search_terms=[0,1,2];
 assert.deepEqual(candidate(absolute),legacy(absolute));
 const unpacked=legacy(old);assert.equal(candidate(unpacked),unpacked);
 const noPool={format:'compact-search-v1',kind:'atlas',terms:[],entries:[{search_terms:[],text:'~s:0'}]};
 assert.deepEqual(encode(noPool),noPool);assert.deepEqual(candidate(noPool),legacy(noPool));
});

test('unknown codecs and malformed, noncanonical or out-of-range references fail closed',()=>{
 for(const ref of ['~s:','~s:-1','~s:+0','~s:00','~s:01','~s:A','~s:0.0','~s:!','~s:zzzz','~s:11111','~s:constructor']){
  const value=clone(packed);value.entries[0].bad=ref;assert.throws(()=>candidate(value),undefined,ref);
 }
 for(const encoding of ['unknown','shared-raw-strings-v2',null,3]){
  const value=clone(packed);value.row_string_encoding=encoding;assert.throws(()=>candidate(value));
 }
 const orphan=fixture();orphan.row_strings=[];assert.throws(()=>candidate(orphan));
 const notCompact={format:'unpacked-search-v1',row_string_encoding:'unknown'};assert.throws(()=>candidate(notCompact));
});

test('invalid pools, Unicode, row structure and existing vocabulary guards are rejected',()=>{
 for(const pool of [null,{},[3],['same','same'],['\uD800'],['\uDC00']]){
  const value=clone(packed);value.row_strings=pool;assert.throws(()=>candidate(value));
 }
 for(const change of [v=>delete v.row_strings,v=>{v.entries=[null];},v=>{v.entries=new Array(1);},v=>{v.entries[0].bad=new Array(2);},v=>{v.entries[0].bad=NaN;},v=>{v.entries[0].bad=()=>{};},v=>{v.entries[0]['\uD800']='bad';},v=>{v.details.keys={};},v=>{v.term_encoding='unknown';}]){
  const value=clone(packed);change(value);assert.throws(()=>candidate(value));
 }
});

test('pool size, individual strings, aggregate units, nesting, node and reconstruction limits are enforced',()=>{
 const L=ROW_STRING_LIMITS;
 let value=clone(packed);value.row_strings=new Array(L.pool+1).fill('x');assert.throws(()=>candidate(value));
 value=clone(packed);value.row_strings=['x'.repeat(L.stringUnits+1)];assert.throws(()=>candidate(value));
 value=clone(packed);value.row_strings=Array.from({length:9},(_,i)=>String(i)+'x'.repeat(999999));assert.throws(()=>candidate(value));
 value=clone(packed);value.row_strings=['x'.repeat(L.stringUnits)];value.entries=[{search_terms:[],many:new Array(17).fill('~s:0')}];value.details.keys=[];assert.throws(()=>candidate(value));
 value=clone(packed);let nested=null;for(let i=0;i<L.depth+2;i++)nested=[nested];value.entries[0].deep=nested;assert.throws(()=>candidate(value));
 value=clone(packed);value.entries[0].many=new Array(L.nodes+1);assert.throws(()=>candidate(value));
 value=clone(packed);value.entries=new Array(L.rows+1).fill({search_terms:[]});assert.throws(()=>candidate(value));
});

test('own prototype-like keys are preserved as data without pollution; inherited prototypes are rejected',()=>{
 assert.equal(Object.prototype.poolCodecPolluted,undefined);
 const original=fixture();const attack=JSON.parse('{"__proto__":{"poolCodecPolluted":true},"constructor":{"prototype":{"poolCodecPolluted":true}},"prototype":"own data"}');
 Object.defineProperty(original.entries[0],'__proto__',{value:attack.__proto__,enumerable:true,writable:true});
 original.entries[0].constructor=attack.constructor;original.entries[0].prototype=attack.prototype;
 const next=candidate(encode(original));assert.deepEqual(next,legacy(original));
 assert.ok(Object.hasOwn(next.entries[0],'__proto__'));assert.equal(next.entries[0].__proto__.poolCodecPolluted,true);
 assert.equal(Object.prototype.poolCodecPolluted,undefined);assert.equal(({}).poolCodecPolluted,undefined);
 const inherited=clone(packed);inherited.entries[0]=Object.assign(Object.create({poolCodecPolluted:true}),inherited.entries[0]);assert.throws(()=>candidate(inherited));
 const array=clone(packed);array.entries[0].extra=[];Object.setPrototypeOf(array.entries[0].extra,Object.create(Array.prototype));assert.throws(()=>candidate(array));
 assert.equal(Object.prototype.poolCodecPolluted,undefined);
});

test('only row values and details keys are decoded, leaving vocabulary and other headers exact',()=>{
 const original=fixture();original.scope='~s:0';original.source_index.url='~s:0';original.details.directory='~s:0';
 const next=encode(original),restored=restoreRowStrings(next);
 assert.equal(next.scope,'~s:0');assert.equal(next.source_index.url,'~s:0');assert.equal(next.details.directory,'~s:0');
 assert.deepEqual(restored,original);assert.deepEqual(candidate(next),legacy(original));
 assert.deepEqual(next.terms,original.terms);assert.deepEqual(restored.details.keys,original.details.keys);
});
