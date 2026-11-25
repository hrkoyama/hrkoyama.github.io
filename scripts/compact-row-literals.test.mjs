import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {dirname,resolve} from 'node:path';
import {restoreRowLiterals,restoreRowPool,restoreRowShapes,restoreRowStrings,unpackSearchIndex} from '../frontend/search/compact-index.mjs';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const clone=x=>structuredClone(x);
function python(body,data=null){
 const code='import json,sys;sys.path.insert(0,sys.argv[1]);import compact_search as c;data=json.load(sys.stdin)\n'+body;
 const p=spawnSync(process.env.PYTHON||'python3',['-B','-c',code,resolve(root,'scripts')],{input:JSON.stringify(data),encoding:'utf8',maxBuffer:32*1024*1024,timeout:20000,env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}});
 assert.equal(p.error,undefined);assert.equal(p.status,0,p.stderr);return JSON.parse(p.stdout);
}
const produce=data=>python('sys.stdout.buffer.write(c.encoded(c.encode_row_literals(data)))',data);
function fixture(kind='atlas'){
 const value={format:'compact-search-v1',kind,terms:['alpha'],term_encoding:'sorted-delta',
  row_string_encoding:'shared-raw-strings-v1',row_strings:['a'.repeat(64),'Repeated 日本😀\uE000e\u0301'],
  row_structure_encoding:'key-shapes-v1',row_shapes:[['id','search_terms','title','values'],['__proto__','array']],
  details:{directory:'/search/details/',keys:['~s:0']},scope:'Unmapped 日本😀 header'};
 value[kind==='atlas'?'entries':'documents']=[[0,'one',[-1,0],'~s:1',[1,'~s:~~literal',[-1,1,true,null]]]];
 return value;
}
function minimal(strings=[]){return {format:'compact-search-v1',kind:'atlas',entries:[],terms:[],
 row_string_encoding:'shared-raw-strings-v1',row_strings:strings,
 row_structure_encoding:'key-shapes-v1',row_shapes:[],details:{directory:'/search/details/',keys:[]}};}
function wire(table,strings=[' ']){return {...minimal(strings),row_literal_encoding:'scalar-bijection-v1',row_literal_alphabet:table};}

test('row literal full pipeline preserves APIs, key order, callers and cache',()=>{
 for(const kind of ['atlas','site']){
  const original=fixture(kind),before=clone(original);
  const pair=python('old=c.encode_row_pool(data);sys.stdout.buffer.write(c.encoded({"old":old,"packed":c.encode_row_literals(old)}))',original);
  const saved=clone(pair.packed),actual=unpackSearchIndex(pair.packed),expected=unpackSearchIndex(original);
  assert.deepEqual(actual,expected);assert.equal(JSON.stringify(actual),JSON.stringify(expected));
  assert.deepEqual(restoreRowLiterals(pair.packed),pair.old);
  assert.deepEqual(restoreRowShapes(pair.packed),restoreRowShapes(pair.old));
  assert.deepEqual(restoreRowPool(pair.packed),restoreRowPool(pair.old));
  assert.deepEqual(restoreRowStrings(pair.packed),restoreRowStrings(pair.old));
  assert.deepEqual(original,before);assert.deepEqual(pair.packed,saved);
  assert.equal(unpackSearchIndex(pair.packed),actual);assert.equal(unpackSearchIndex(actual),actual);
  const row=actual[kind==='atlas'?'entries':'documents'][0];assert(Object.hasOwn(row.values,'__proto__'));assert.equal({}.polluted,undefined);
  for(const key of ['row_literal_encoding','row_literal_alphabet'])assert(!Object.hasOwn(actual,key));
 }
});

test('row literal scalar bijection is one pass with canonical codepoint ties',()=>{
 const simple=produce(minimal(['bbba']));assert.equal(simple.row_literal_alphabet,'ba');assert.deepEqual(simple.row_strings,['   !']);
 const original=minimal(['\uE000😀',' !\u0080\u0000"\\\x7f','e\u0301~s:0']);
 const packed=produce(original);assert.deepEqual(restoreRowLiterals(packed),original);
 const tied=produce(minimal(['\uE000😀']));assert.equal(tied.row_literal_alphabet,'\uE000😀');assert.deepEqual(tied.row_strings,[' !']);
});

test('row literal writer preserves Python numbers and unmapped header bytes',()=>{
 const result=python(
  'data["number_header"]={"10":1.0,"2":-0.0,"small":1e-100,"large":1e100}\n'+
  'data["entries"][0][4]=[-1,1,1.0,-0.0];data["row_shapes"]=data["row_shapes"][:1]\n'+
  'packed=c.encode_row_literals(data)\n'+
  'assert c.encoded(packed["number_header"])==c.encoded(data["number_header"])\n'+
  'sys.stdout.buffer.write(c.encoded({"before":data,"packed":packed}))',fixture());
 assert.deepEqual(restoreRowLiterals(result.packed),result.before);
 const actual=unpackSearchIndex(result.packed);assert(Object.is(actual.entries[0].values[2],-0));
 assert.deepEqual(actual.number_header,result.before.number_header);
});

test('row literal old formats, empty and unsupported subsets fall back exactly',()=>{
 const noShapes=minimal(['abcd']);delete noShapes.row_structure_encoding;delete noShapes.row_shapes;
 const noPool=minimal([]);delete noPool.row_string_encoding;delete noPool.row_strings;
 for(const clean of [minimal([]),{format:'compact-search-v1',kind:'atlas',entries:[],terms:[]},noShapes,noPool]){
  assert.deepEqual(produce(clean),clean);assert.equal(restoreRowLiterals(clean),clean);
  assert.doesNotThrow(()=>unpackSearchIndex(clean));
 }
 const status=python(
  'x={"format":"compact-search-v1","kind":"atlas","entries":[],"terms":[],"row_string_encoding":c.ENCODING,"row_strings":["".join(chr(0x1000+i) for i in range(8193))],"row_structure_encoding":"key-shapes-v1","row_shapes":[],"details":{"keys":[]}}\n'+
  'assert c.encode_row_literals(x) is x\n'+
  'v=0\n'+
  'for _ in range(63):v=[-1,v]\n'+
  'x["row_strings"]=[];x["row_shapes"]=[["v"]];x["entries"]=[[0,v]]\n'+
  'assert c.encode_row_literals(x) is x\n'+
  'sys.stdout.buffer.write(c.encoded({"ok":True,"boundary":x}))');
 assert(status.ok);assert.doesNotThrow(()=>unpackSearchIndex(status.boundary));
});

test('row literal unknown, orphan and conflicting mode headers fail closed',()=>{
 const good=produce(fixture());
 for(const change of [x=>delete x.row_literal_alphabet,x=>delete x.row_literal_encoding,x=>x.row_literal_encoding='unknown',
  x=>x.format='unpacked-search-v1',x=>x.kind='bad',x=>delete x.row_strings,x=>delete x.row_shapes,
  x=>x.row_string_encoding='unknown',x=>x.row_structure_encoding='unknown',x=>delete x.details.keys]){
  const bad=clone(good);change(bad);assert.throws(()=>unpackSearchIndex(bad));
 }
 assert.throws(()=>unpackSearchIndex({format:'unpacked-search-v1',row_literal_alphabet:'a'}));
 assert.throws(()=>produce(good));
});

test('row literal malformed alphabets, symbols and noncanonical frequencies reject',()=>{
 for(const table of ['', 'aa', '\uD800', Array.from({length:8193},(_,i)=>String.fromCodePoint(0x1000+i)).join('')])assert.throws(()=>restoreRowLiterals(wire(table)));
 for(const text of ['\0','\x1f','\x7f','"','\\','!','😀','\uD800'])assert.throws(()=>restoreRowLiterals(wire('a',[text])));
 for(const bad of [wire('ab',['!! ']),wire('ba',[' !']),wire('ab',['  '])])assert.throws(()=>restoreRowLiterals(bad));
 const wrong=wire('a');wrong.row_literal_alphabet=[];assert.throws(()=>restoreRowLiterals(wrong));
});

test('row literal sparse, prototype, nonfinite and nonshaped roots reject',()=>{
 const good=produce(fixture());
 for(const change of [x=>delete x.entries[0],x=>delete x.row_shapes[0][0],x=>delete x.row_strings[0],
  x=>Object.setPrototypeOf(x,{}),x=>Object.setPrototypeOf(x.details,{}),x=>Object.setPrototypeOf(x.entries,{}),
  x=>Object.setPrototypeOf(x.row_shapes[0],{}),x=>x.entries[0]={id:'object'},x=>x.entries[0][2]={bad:'object'},
  x=>x.row_strings[0]=null,x=>x.details.keys[0]=42,x=>x.entries[0][1]=Infinity]){
  const bad=clone(good);change(bad);assert.throws(()=>restoreRowLiterals(bad));
 }
});

test('row literal preflight enforces old and stricter marked-subset bounds',()=>{
 const rows=wire('a');rows.entries=new Array(2001);assert.throws(()=>restoreRowLiterals(rows));
 const pool=wire('a');pool.row_strings=new Array(50001);assert.throws(()=>restoreRowLiterals(pool));
 const nodes=wire('a');nodes.entries=[[0,[-1,...new Array(1000000).fill(0)]]];assert.throws(()=>restoreRowLiterals(nodes));
 const deep=wire('a');let v=0;for(let i=0;i<65;i++)v=[-1,v];deep.entries=[[0,v]];assert.throws(()=>restoreRowLiterals(deep));
 assert.throws(()=>restoreRowLiterals(wire('😀',[' '.repeat(500001)])));
 const schema=wire('a',[]);schema.row_shapes=[[' '.repeat(8200001)]];assert.throws(()=>restoreRowLiterals(schema));
 const total=wire('a',[]),text=' '.repeat(1000000);total.entries=[[0,...new Array(17).fill(text)]];assert.throws(()=>restoreRowLiterals(total));
});
