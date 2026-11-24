import test,{after} from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {copyFileSync,mkdirSync,mkdtempSync,rmSync,writeFileSync} from 'node:fs';
import {join} from 'node:path';
import {tmpdir} from 'node:os';
import {unpackSearchIndex} from '../frontend/search/compact-index.mjs';

const root=new URL('../',import.meta.url);
// Render no indexes: isolate the source modules with their existing public data
// dependencies, so this test also works before aggregate asset generation.
const client=mkdtempSync(join(process.env.ATLAS_INDEX_SCRATCH||tmpdir(),'atlas-compact-codec-'));
after(()=>rmSync(client,{recursive:true,force:true}));
for(const directory of ['search','numerical-methods-atlas'])mkdirSync(join(client,directory));
writeFileSync(join(client,'package.json'),'{"type":"module"}');
for(const name of ['compact-index.mjs','engine.mjs','method-search.mjs','navigation.mjs'])copyFileSync(new URL('frontend/search/'+name,root),join(client,'search',name));
copyFileSync(new URL('frontend/search/home-search.js',root),join(client,'numerical-methods-atlas/home-search.js'));
for(const name of ['i18n.js','reading-urls.js'])copyFileSync(new URL('numerical-methods-atlas/'+name,root),join(client,'numerical-methods-atlas',name));
copyFileSync(new URL('search/goals-data.mjs',root),join(client,'search/goals-data.mjs'));
const {atlasSearch}=await import(pathToFileURL(join(client,'search/engine.mjs')));
const {searchChapters}=await import(pathToFileURL(join(client,'numerical-methods-atlas/home-search.js')));
function pack(index){
 // Exercise the production Python encoder and JS decoder together, without
 // generating indexes, opening scientific assets, or depending on NumPy.
 return JSON.parse(execFileSync('python3',['-B','-c',`
import json,sys
sys.path.insert(0,sys.argv[1])
from compact_search import pack_vocabulary,pack_deltas
index=json.load(sys.stdin)
index['terms']=pack_vocabulary(index['terms'])
index['vocabulary_encoding']='unicode-prefix-flat-v1'
index['term_encoding']='sorted-delta-varint-base64'
for row in index['entries']:
    value=row['search_terms']
    row['search_terms']={key:pack_deltas(ids) for key,ids in value.items()} if isinstance(value,dict) else pack_deltas(value)
json.dump(index,sys.stdout,ensure_ascii=False,separators=(',',':'))
`,fileURLToPath(new URL('scripts',root))],{input:JSON.stringify(index),encoding:'utf8',maxBuffer:32*1024*1024}));
}
const fixture=()=>({
 format:'compact-search-v1',kind:'atlas',term_encoding:'sorted-delta',
 terms:['a','aa','a😀','a😁','é','α','日','日本','😀','😀x','😁','𠮷'],
 entries:[{id:'codec-reading',kind:'chapter',chapter:'codec-reading',origin:'fixture',
  title:{ja:'日本と😀',en:'Unicode reference'},text:{ja:'日本 日 😀x',en:'a α'},
  headings:{ja:[{level:2,id:'exact-section',title:'日本'}],en:[{level:3,id:'unicode-section',title:'Unicode reference'}]},
  routes:{ja:'/numerical-methods-atlas/ja/read/codec-reading/',en:'/numerical-methods-atlas/en/read/codec-reading/'},
  search_terms:{ja:[6,1,2],en:[0,5]},keywords:['日本','Unicode']},
 {id:'empty',kind:'resource',title:{ja:'空',en:'Empty'},text:'',search_terms:[],headings:{ja:[],en:[]},routes:{en:'/numerical-methods-atlas/empty/'}}],
 details:{directory:'/search/details/',keys:[]},source_index:{url:'/unchanged.json',sha256:'0'.repeat(64)},scope:'unchanged',
});

test('Python code-point prefixes and canonical byte deltas preserve the full legacy unpacked API',()=>{
 const old=fixture(),before=structuredClone(old),next=pack(old);
 assert.deepEqual(old,before,'encoding does not mutate the caller');
 assert.deepEqual(unpackSearchIndex(next),unpackSearchIndex(old));
 assert.equal(unpackSearchIndex(unpackSearchIndex(next)),unpackSearchIndex(next));
 assert.deepEqual(next.terms.slice(4,8),[1,'😀',1,'😁'],'a shared astral prefix uses code points');
 for(const query of ['日本','日','Unicode','α','a','😀'])for(const language of ['ja','en']){
  assert.deepEqual(atlasSearch(next)(query,language,'atlas'),atlasSearch(old)(query,language,'atlas'));
 }
 const absolute={...fixture(),term_encoding:undefined};
 absolute.entries[0].search_terms={ja:[6,7,9],en:[0,5]};
 assert.deepEqual(unpackSearchIndex(absolute).entries,unpackSearchIndex(old).entries,'legacy absolute term IDs are still accepted');
 const empty={format:'compact-search-v1',kind:'atlas',term_encoding:'sorted-delta',terms:[],entries:[{search_terms:[]}]};
 assert.deepEqual(unpackSearchIndex(pack(empty)),unpackSearchIndex(empty));
});

test('one-, two- and three-byte unsigned deltas preserve boundary IDs without signed JS arithmetic',()=>{
 const index={format:'compact-search-v1',kind:'atlas',term_encoding:'sorted-delta',terms:Array.from({length:500000},(_,i)=>'w'+i),entries:[{search_terms:[0,127,1,16255,1,483615]}]};
 assert.deepEqual(unpackSearchIndex(pack(index)),unpackSearchIndex(index));
});

test('the production writer emits both codecs while keeping long text in its fixed detail file',()=>{
 const value=JSON.parse(execFileSync('python3',['-B','-c',`
import json,sys,tempfile
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from compact_search import write_compact
with tempfile.TemporaryDirectory(prefix='compact-writer-') as path:
    root=Path(path);(root/'numerical-methods-atlas').mkdir()
    source={'entries':[{'id':'example','headings':{'ja':[{'level':2,'id':'kept','title':'日本'}]},'text':{'ja':'日本 😀x '+('長い本文 '*150),'en':'Unicode α'}}]}
    (root/'numerical-methods-atlas/home-search-index.json').write_text(json.dumps(source,ensure_ascii=False))
    compact=json.loads(write_compact(root,source,'atlas').read_text())
    details={file.name:file.read_text() for file in (root/'search/details').glob('*.json')}
    print(json.dumps({'source':source,'compact':compact,'details':details},ensure_ascii=False))
`,fileURLToPath(new URL('scripts',root))],{encoding:'utf8'}));
 const {compact,source,details}=value,expanded=unpackSearchIndex(compact),entry=expanded.entries[0];
 // The public API resolves pooled references; filenames remain content addressed.
 assert.match(entry.text_ref,/^[a-f0-9]{64}$/);
 assert.deepEqual(Object.keys(details),[entry.text_ref+'.json']);
 assert.deepEqual(expanded.details.keys,[entry.text_ref]);
 const raw=details[entry.text_ref+'.json'],detail=JSON.parse(raw);
 assert.equal(createHash('sha256').update(raw).digest('hex'),entry.text_ref);
 assert.equal(compact.vocabulary_encoding,'unicode-prefix-flat-v1');
 assert.equal(compact.term_encoding,'sorted-delta-varint-base64');
 assert.equal(typeof compact.entries[0].search_terms.ja,'string');
 assert.deepEqual(entry.headings,source.entries[0].headings);
 assert.deepEqual(detail.text,source.entries[0].text);
 assert.equal(entry.text.ja,Array.from(source.entries[0].text.ja).slice(0,500).join(''));
 assert.equal(entry.search_text.ja,'日本 長い本文 😀x');
});

test('corrupt, overflowing, truncated, noncanonical and duplicate-ID byte streams fail closed',()=>{
 const b64=bytes=>Buffer.from(bytes).toString('base64');
 for(const value of ['!', 'AA=', 'AB==', b64([128]), b64([128,0]), b64([255,255,255,255,15]), b64([12]), b64([0,0]), b64([11,1]), 4, [], 'A'.repeat(2000004)]){
  const index=pack(fixture());index.entries[0].search_terms={ja:value};
  assert.throws(()=>unpackSearchIndex(index),undefined,JSON.stringify(value).slice(0,100));
 }
 const unknown=pack(fixture());unknown.term_encoding='unknown';assert.throws(()=>unpackSearchIndex(unknown));
});

test('prefixes enforce code-point bounds, scalar Unicode, term counts and bounded expansion',()=>{
 const expansion=[0,'x'.repeat(8201),...Array.from({length:1000},()=>[8201,'']).flat()];
 for(const terms of [[-1,'a'],[0.5,'a'],[1,'a'],[0,'a',2,'b'],[0,'a',1.5,'b'],[0,'a',0,4],[0,'\uD800'],[0,'\uDC00'],[0,'a',1,'b',0],expansion]){
  const index=pack(fixture());index.terms=terms;assert.throws(()=>unpackSearchIndex(index));
 }
 const excessive=pack(fixture());excessive.terms=new Array(1000002).fill(0);assert.throws(()=>unpackSearchIndex(excessive));
 const unknown=pack(fixture());unknown.vocabulary_encoding='unknown';assert.throws(()=>unpackSearchIndex(unknown));
});

test('both homepage and global consumers retain all heading fields, section IDs, scores and URLs',()=>{
 const old=fixture(),next=pack(old);
 for(const [query,language,section]of [['日本','ja','exact-section'],['Unicode','en','unicode-section']]){
  const before=searchChapters(old,query,language),after=searchChapters(next,query,language);
  assert.ok(before.length);assert.equal(before[0].section,section);assert.deepEqual(after,before);
 }
});
