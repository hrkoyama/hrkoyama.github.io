import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import {goalMatches,wireGoalFilters} from '../numerical-methods-atlas/goal-filters.mjs';
const root=new URL('../',import.meta.url);
const records=JSON.parse(execFileSync('python3',['-c',`import sys,json
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_goal_availability import goal_flags
r=Path('.')
m={x['id']:x for x in json.loads((r/'numerical-methods-atlas/methods/index.json').read_text())['methods']}
g=json.loads((r/'catalog/atlas-goals.json').read_text())['goals']
print(json.dumps([{'id':x['id'],'states':' '.join(goal_flags(x,m))} for x in g]))`],{cwd:root,encoding:'utf8'}));
function element(){return {hidden:false,value:'',textContent:'',events:{},addEventListener(name,fn){this.events[name]=fn;},fire(name){this.events[name]?.();}};}
function fixture(lang='ja',rows=records){
 const field=element(),reset=element(),status=element(),empty=element(),controls=element();controls.hidden=true;
 const items=rows.flatMap(row=>[false,true].map(article=>({...element(),id:article?row.id+'-'+lang:'',dataset:{goalId:row.id,goalStates:row.states}})));
 const nodes={'[data-goal-filter]':field,'[data-goal-reset]':reset,'[data-goal-count]':status,'[data-goal-empty]':empty,'[data-goal-controls]':controls};
 const scope={dataset:{goalFilterRoot:'',goalLanguage:lang},querySelector:s=>nodes[s],querySelectorAll:s=>s==='[data-goal-item]'?items:[]};
 return {scope,field,reset,status,empty,controls,items,choose(value){field.value=value;field.fire('change');},visible(){return [...new Set(items.filter(x=>!x.hidden).map(x=>x.dataset.goalId))];}};
}
function environment(fn,blocked=false){
 const saved=Object.fromEntries(['sessionStorage','location','history'].map(k=>[k,Object.getOwnPropertyDescriptor(globalThis,k)]));
 const values=new Map();
 const storage={getItem:k=>{if(blocked)throw Error('blocked');return values.get(k)||null;},setItem:(k,v)=>{if(blocked)throw Error('blocked');values.set(k,v);}};
 const loc={hash:'',pathname:'/numerical-methods-atlas/start/',search:'?lang=ja'};
 const history={replaceState(a,b,url){loc.hash='';this.last=url;}};
 for(const [k,value] of Object.entries({sessionStorage:storage,location:loc,history}))Object.defineProperty(globalThis,k,{value,configurable:true});
 try{fn(loc,history);}finally{for(const [k,d] of Object.entries(saved)){if(d)Object.defineProperty(globalThis,k,d);else delete globalThis[k];}}
}
test('published goals classify runnable examples as also having code/tests, without promoting reading or planned goals',()=>{
 assert.equal(records.length,10);
 for(const [filter,count] of [['all',10],['run',6],['code',7],['reading',2],['planned',1]])assert.equal(records.filter(r=>goalMatches(r.states,filter)).length,count,filter);
 assert.equal(records.find(r=>r.id==='molecular-dft').states,'reading');
 assert.equal(records.find(r=>r.id==='biological-models').states,'reading');
 assert.equal(records.find(r=>r.id==='temperature-control').states,'planned');
});
test('selection filters both navigation and articles, counts unique goals, persists across language/pages, and resets',()=>environment(()=>{
 const f=fixture();wireGoalFilters(f.scope);assert.equal(f.controls.hidden,false);
 f.choose('reading');assert.deepEqual(f.visible(),['molecular-dft','biological-models']);assert.equal(f.status.textContent,'2 / 10 件の目的');assert.equal(f.empty.hidden,true);
 assert.equal(f.items.filter(x=>!x.hidden).length,4);
 const en=fixture('en');wireGoalFilters(en.scope);assert.equal(en.field.value,'reading');assert.equal(en.status.textContent,'2 of 10 goals');
 en.choose('planned');assert.deepEqual(en.visible(),['temperature-control']);
 en.reset.fire('click');assert.equal(en.visible().length,10);assert.equal(en.field.value,'all');
 assert.equal(wireGoalFilters(en.scope).length,1);
}));
test('direct links reveal a hidden target; intentionally changing filters clears an excluded anchor',()=>environment((loc,history)=>{
 const first=fixture();wireGoalFilters(first.scope);first.choose('run');
 loc.hash='#biological-models-ja';
 const linked=fixture();wireGoalFilters(linked.scope);assert.equal(linked.field.value,'all');assert.ok(linked.visible().includes('biological-models'));
 linked.choose('planned');assert.equal(loc.hash,'');assert.equal(history.last,loc.pathname+loc.search);
}));
test('blocked storage, invalid values and zero matches remain usable',()=>environment(()=>{
 const f=fixture('en',records.filter(r=>r.states==='reading'));wireGoalFilters(f.scope);
 f.choose('run');assert.deepEqual(f.visible(),[]);assert.equal(f.empty.hidden,false);assert.equal(f.status.textContent,'0 of 2 goals');
 f.reset.fire('click');assert.equal(f.visible().length,2);assert.equal(f.empty.hidden,true);
 f.choose('invalid');assert.equal(f.field.value,'all');
},true));
test('generated bilingual home and goal pages provide all filters, matching attributes and progressive enhancement',()=>{
 for(const path of ['numerical-methods-atlas/index.html','numerical-methods-atlas/start/index.html']){
  const html=fs.readFileSync(new URL(path,root),'utf8');
  assert.ok(html.includes('data-goal-controls hidden'),'no dead controls without JavaScript');
  for(const value of ['all','run','code','reading','planned'])assert.ok(html.includes(`value="${value}"`));
  for(const record of records)assert.ok(html.includes(`data-goal-id="${record.id}" data-goal-states="${record.states}"`));
  assert.ok(html.includes('data-goal-language="ja"')&&html.includes('data-goal-language="en"'));
  assert.ok(html.includes('goal-filters.mjs?v=')&&html.includes('atlas-goal-filters.css?v='));
 }
});
