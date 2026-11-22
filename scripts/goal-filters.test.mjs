import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import {goalMatches,goalFilterURL,wireGoalFilters} from '../numerical-methods-atlas/goal-filters.mjs';
const root=new URL('../',import.meta.url);
const records=JSON.parse(execFileSync('python3',['-c',`import sys,json
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_goal_availability import goal_flags
r=Path('.')
m={x['id']:x for x in json.loads((r/'numerical-methods-atlas/methods/index.json').read_text())['methods']}
g=json.loads((r/'catalog/atlas-goals.json').read_text())['goals']
print(json.dumps([{'id':x['id'],'states':' '.join(goal_flags(x,m)),'domains':' '.join(x['domains'])} for x in g]))`],{cwd:root,encoding:'utf8'}));
function element(){return {hidden:false,value:'',textContent:'',events:{},addEventListener(name,fn){this.events[name]=fn;},focus(){this.focused=true;},select(){this.selected=true;},fire(name){return this.events[name]?.();}};}
function fixture(lang='ja',rows=records){
 const field=element(),domain=element(),reset=element(),status=element(),empty=element(),controls=element(),copy=element(),copyFeedback=element(),copyFallback=element(),copyURL=element();controls.hidden=true;
 const items=rows.flatMap(row=>[false,true].map(article=>({...element(),id:article?row.id+'-'+lang:'',dataset:{goalId:row.id,goalStates:row.states,goalDomains:row.domains}})));
 const nodes={'[data-goal-copy]':copy,'[data-goal-copy-feedback]':copyFeedback,'[data-goal-copy-fallback]':copyFallback,'[data-goal-copy-url]':copyURL,'[data-goal-domain]':domain,'[data-goal-filter]':field,'[data-goal-reset]':reset,'[data-goal-count]':status,'[data-goal-empty]':empty,'[data-goal-controls]':controls};
 const scope={dataset:{goalFilterRoot:'',goalLanguage:lang},querySelector:s=>nodes[s],querySelectorAll:s=>s==='[data-goal-item]'?items:[]};
 return {scope,field,domain,reset,status,empty,controls,items,copy,copyFeedback,copyFallback,copyURL,choose(value){field.value=value;field.fire('change');},chooseDomain(value){domain.value=value;domain.fire('change');},visible(){return [...new Set(items.filter(x=>!x.hidden).map(x=>x.dataset.goalId))];}};
}
function environment(fn,blocked=false){
 const saved=Object.fromEntries(['sessionStorage','location','history','navigator'].map(k=>[k,Object.getOwnPropertyDescriptor(globalThis,k)]));
 const values=new Map();
 const storage={getItem:k=>{if(blocked)throw Error('blocked');return values.get(k)||null;},setItem:(k,v)=>{if(blocked)throw Error('blocked');values.set(k,v);}};
 const loc=new URL('https://hrkoyama.github.io/numerical-methods-atlas/start/?lang=ja');
 const entries=[loc.href];let index=0;
 const history={state:{atlas:'retained'},replaceState(state,b,url){this.state=state;loc.href=new URL(url,loc).href;entries[index]=loc.href;this.last=loc.href;},pushState(state,b,url){this.state=state;loc.href=new URL(url,loc).href;entries.splice(++index);entries.push(loc.href);this.last=loc.href;},back(){if(index>0)loc.href=entries[--index];},forward(){if(index+1<entries.length)loc.href=entries[++index];}};
 for(const [k,value] of Object.entries({sessionStorage:storage,location:loc,history,navigator:{clipboard:{writeText:async()=>{}}}}))Object.defineProperty(globalThis,k,{value,configurable:true});
 const restore=()=>{for(const [k,d] of Object.entries(saved)){if(d)Object.defineProperty(globalThis,k,d);else delete globalThis[k];}};
 let result;try{result=fn(loc,history,values);}catch(error){restore();throw error;}
 if(result?.then)return result.finally(restore);restore();return result;
}
test('published goals classify runnable examples as also having code/tests, without promoting reading or planned goals',()=>{
 assert.equal(records.length,14);
 for(const [filter,count] of [['all',14],['run',12],['code',13],['reading',1],['planned',0]])assert.equal(records.filter(r=>goalMatches(r.states,filter)).length,count,filter);
 assert.equal(records.find(r=>r.id==='molecular-dft').states,'reading');
 assert.equal(records.find(r=>r.id==='biological-models').states,'run code');
 assert.equal(records.find(r=>r.id==='temperature-control').states,'run code');
});
test('selection filters both navigation and articles, counts unique goals, persists across language/pages, and resets',()=>environment(()=>{
 const f=fixture();const [homeController]=wireGoalFilters(f.scope);assert.equal(f.controls.hidden,false);
 f.choose('reading');assert.deepEqual(f.visible(),['molecular-dft']);assert.equal(f.status.textContent,'1 / 14 件の目的');assert.equal(f.empty.hidden,true);
 assert.equal(f.items.filter(x=>!x.hidden).length,2);
 const en=fixture('en');wireGoalFilters(en.scope);assert.equal(en.field.value,'reading');assert.equal(en.status.textContent,'1 of 14 goals');
 en.chooseDomain('temperature');en.choose('run');assert.deepEqual(en.visible(),['temperature-control']);
 homeController.sync();assert.equal(f.field.value,'run');assert.equal(f.domain.value,'temperature');assert.deepEqual(f.visible(),['temperature-control'],'restored pages use the latest session selection');
 en.reset.fire('click');assert.equal(en.visible().length,14);assert.equal(en.field.value,'all');assert.equal(en.domain.value,'all');
 assert.equal(wireGoalFilters(en.scope).length,1);
}));
test('direct links reveal a hidden target; intentionally changing filters clears an excluded anchor',()=>environment((loc,history)=>{
 const first=fixture();wireGoalFilters(first.scope);first.choose('run');first.chooseDomain('quantum');
 loc.hash='#biological-models-ja';
 const linked=fixture();wireGoalFilters(linked.scope);assert.equal(linked.field.value,'all');assert.equal(linked.domain.value,'all');assert.ok(linked.visible().includes('biological-models'));
 linked.choose('planned');assert.equal(loc.hash,'');assert.equal(history.last,loc.href);
}));
test('blocked storage, invalid values and zero matches remain usable',()=>environment(()=>{
 const f=fixture('en',records.filter(r=>r.states==='reading'));wireGoalFilters(f.scope);
 f.choose('run');assert.deepEqual(f.visible(),[]);assert.equal(f.empty.hidden,false);assert.equal(f.status.textContent,'0 of 1 goals');
 f.reset.fire('click');assert.equal(f.visible().length,1);assert.equal(f.empty.hidden,true);
 f.choose('invalid');f.chooseDomain('invalid');assert.equal(f.field.value,'all');assert.equal(f.domain.value,'all');
},true));
test('generated bilingual home and goal pages provide all filters, matching attributes and progressive enhancement',()=>{
 for(const path of ['numerical-methods-atlas/index.html','numerical-methods-atlas/start/index.html']){
  const html=fs.readFileSync(new URL(path,root),'utf8');
  assert.ok(html.includes('data-goal-controls hidden'),'no dead controls without JavaScript');
  assert.ok(html.includes('data-goal-copy>共有リンクをコピー')&&html.includes('data-goal-copy>Copy share link'));
  assert.ok(html.includes('data-goal-copy-url readonly')&&html.includes('data-goal-copy-feedback role="status"'));
  for(const value of ['all','run','code','reading','planned'])assert.ok(html.includes(`value="${value}"`));
  for(const record of records)assert.ok(html.includes(`data-goal-id="${record.id}" data-goal-states="${record.states}" data-goal-domains="${record.domains}"`));
  for(const domain of JSON.parse(fs.readFileSync(new URL('catalog/atlas-goals.json',root),'utf8')).domains)assert.ok(html.includes(`value="${domain.id}"`));
  assert.ok(html.includes('data-goal-language="ja"')&&html.includes('data-goal-language="en"'));
  assert.ok(html.includes('goal-filters.mjs?v=')&&html.includes('atlas-goal-filters.css?v='));
 }
});

test('field and availability intersect, overlapping MHD membership does not duplicate goals, and empty combinations reset',()=>environment(()=>{
 const f=fixture();wireGoalFilters(f.scope);
 for(const [domain,availability,ids] of [
  ['quantum','run',['atomic-electrons','molecular-hf','periodic-dft','periodic-forces']],
  ['quantum','reading',['molecular-dft']],
  ['biology','code',['biological-models']],
  ['temperature','run',['temperature-control']],
  ['fluid','code',['shocks','smooth-vortex','magnetic-divergence']],
  ['mhd','code',['magnetic-divergence']],
  ['diffusion','run',['poisson']],
  ['time','run',['stiff-time','stochastic-calculation']],
  ['gravity','run',['particle-gravity']]
 ]){
  f.chooseDomain(domain);f.choose(availability);assert.deepEqual(f.visible(),ids,domain+' + '+availability);
  assert.equal(f.status.textContent,`${ids.length} / 14 件の目的`);assert.equal(f.empty.hidden,ids.length!==0);
 }
 const en=fixture('en');wireGoalFilters(en.scope);assert.equal(en.domain.value,'gravity');assert.equal(en.field.value,'run');
 f.chooseDomain('temperature');f.choose('reading');assert.equal(f.empty.hidden,false);f.reset.fire('click');assert.equal(f.visible().length,14);assert.equal(f.domain.value,'all');assert.equal(f.field.value,'all');
}));
test('changing only the field clears an excluded anchor and direct links reset a conflicting field',()=>environment((loc,history)=>{
 const f=fixture();const [controller]=wireGoalFilters(f.scope);
 loc.hash='#magnetic-divergence-ja';f.chooseDomain('quantum');assert.equal(loc.hash,'');assert.equal(history.last,loc.href);
 loc.hash='#magnetic-divergence-ja';controller.revealAnchor();assert.equal(f.domain.value,'all');assert.ok(f.visible().includes('magnetic-divergence'));
}));

test('URL conditions override session preferences, missing partners and unknown values resolve to all',()=>environment((loc,history,values)=>{
 values.set('atlas-goal-domain','biology');values.set('atlas-goal-availability','reading');
 loc.search='?lang=en&goal-domain=quantum&goal-availability=run';
 const f=fixture('en');const [controller]=wireGoalFilters(f.scope);assert.deepEqual(f.visible(),['atomic-electrons','molecular-hf','periodic-dft','periodic-forces']);
 assert.equal(values.get('atlas-goal-domain'),'quantum');
 loc.search='?lang=en&goal-domain=quantum';controller.sync();assert.equal(f.field.value,'all');assert.deepEqual(f.visible(),['atomic-electrons','molecular-dft','molecular-hf','periodic-dft','periodic-forces']);
 loc.search='?lang=en&goal-domain=unknown&goal-availability=invalid';controller.sync();assert.equal(f.visible().length,14);assert.equal(loc.searchParams.get('goal-domain'),'all');assert.equal(loc.searchParams.get('goal-availability'),'all');
 loc.search='?lang=en&goal-domain=all&goal-availability=all';values.set('atlas-goal-domain','biology');controller.sync();assert.equal(f.visible().length,14);
}));
test('filter URLs preserve unrelated parameters and anchors; changes, back/forward and reset restore their own conditions',()=>environment((loc,history)=>{
 loc.search='?lang=ja&view=compact';loc.hash='#top';
 const f=fixture();const [controller]=wireGoalFilters(f.scope);
 f.chooseDomain('quantum');f.choose('run');
 const shared=loc.href;assert.equal(loc.searchParams.get('goal-domain'),'quantum');assert.equal(loc.searchParams.get('goal-availability'),'run');assert.equal(loc.searchParams.get('view'),'compact');assert.equal(loc.hash,'#top');assert.deepEqual(history.state,{atlas:'retained'});
 history.back();controller.sync();assert.equal(f.domain.value,'quantum');assert.equal(f.field.value,'all');assert.equal(f.visible().length,5);
 history.forward();controller.sync();assert.equal(loc.href,shared);assert.deepEqual(f.visible(),['atomic-electrons','molecular-hf','periodic-dft','periodic-forces']);
 f.reset.fire('click');assert.equal(loc.searchParams.get('goal-domain'),'all');assert.equal(loc.searchParams.get('goal-availability'),'all');
 history.back();controller.sync();assert.equal(loc.href,shared);assert.deepEqual(f.visible(),['atomic-electrons','molecular-hf','periodic-dft','periodic-forces']);
 const url=goalFilterURL('https://hrkoyama.github.io/numerical-methods-atlas/start/?lang=en&view=compact#atomic-electrons-en','run','quantum');
 assert.equal(url.searchParams.get('lang'),'en');assert.equal(url.hash,'#atomic-electrons-en');assert.equal(url.searchParams.get('view'),'compact');
}));
test('URL conditions work when storage is unavailable and conflicting direct anchors normalize the shared URL',()=>environment((loc)=>{
 loc.search='?lang=ja&goal-domain=quantum&goal-availability=run';
 const f=fixture();const [controller]=wireGoalFilters(f.scope);assert.deepEqual(f.visible(),['atomic-electrons','molecular-hf','periodic-dft','periodic-forces']);
 loc.hash='#magnetic-divergence-ja';controller.revealAnchor();assert.equal(loc.searchParams.get('goal-domain'),'all');assert.equal(loc.searchParams.get('goal-availability'),'all');assert.equal(loc.hash,'#magnetic-divergence-ja');
},true));
test('only same-origin home, purpose and language links carry the current conditions, including copied or new-tab links',()=>environment(()=>{
 const link=href=>({href,getAttribute(){return this.href;},hasAttribute(){return false;},setAttribute(name,value){this.href=value;}});
 const links=[link('/numerical-methods-atlas/start/?lang=en#atomic-electrons-en'),link('/numerical-methods-atlas/?lang=ja'),link('?lang=en'),link('#top'),link('/numerical-methods-atlas/methods/?lang=ja'),link('https://example.org/numerical-methods-atlas/')];
 const f=fixture();f.scope.ownerDocument={querySelectorAll:()=>links};wireGoalFilters(f.scope);f.chooseDomain('quantum');f.choose('run');
 for(const target of links.slice(0,3)){const url=new URL(target.href);assert.equal(url.searchParams.get('goal-domain'),'quantum');assert.equal(url.searchParams.get('goal-availability'),'run');}
 assert.equal(new URL(links[0].href).hash,'#atomic-electrons-en');assert.equal(new URL(links[0].href).searchParams.get('lang'),'en');
 assert.equal(links[3].href,'#top');assert.equal(links[4].href,'/numerical-methods-atlas/methods/?lang=ja');assert.equal(links[5].href,'https://example.org/numerical-methods-atlas/');
}));

test('copy uses the latest selected conditions, display language and anchor, announces success and clears on changes',()=>environment(async(loc)=>{
 const written=[];navigator.clipboard.writeText=async text=>written.push(text);
 const f=fixture();wireGoalFilters(f.scope);f.chooseDomain('quantum');f.choose('run');loc.hash='#atomic-electrons-ja';
 await f.copy.fire('click');assert.equal(written[0],loc.href);assert.equal(f.copyFeedback.textContent,'共有リンクをコピーしました。');assert.equal(f.copyFeedback.hidden,false);assert.equal(f.copyFallback.hidden,true);assert.equal(f.copy.disabled,false);
 f.choose('reading');assert.equal(f.copyFeedback.hidden,true);assert.equal(f.copyFeedback.textContent,'');
 await f.copy.fire('click');assert.equal(new URL(written[1]).searchParams.get('goal-availability'),'reading');assert.equal(new URL(written[1]).hash,'');
 const en=fixture('en');wireGoalFilters(en.scope);await en.copy.fire('click');assert.equal(new URL(written[2]).searchParams.get('lang'),'en');assert.equal(en.copyFeedback.textContent,'Share link copied.');
}));
test('denied and unavailable clipboard show a selectable share URL, without a false success message',()=>environment(async()=>{
 for(const lang of ['ja','en']){
  navigator.clipboard=lang==='ja'?{writeText:async()=>{throw Error('denied');}}:undefined;
  const f=fixture(lang);wireGoalFilters(f.scope);f.chooseDomain('biology');f.choose('code');await f.copy.fire('click');
  assert.equal(f.copyFallback.hidden,false);assert.equal(f.copyFeedback.hidden,false);assert.ok(f.copyURL.focused&&f.copyURL.selected);assert.equal(f.copy.disabled,false);
  const url=new URL(f.copyURL.value);assert.equal(url.searchParams.get('goal-domain'),'biology');assert.equal(url.searchParams.get('goal-availability'),'code');assert.equal(url.searchParams.get('lang'),lang);
  assert.match(f.copyFeedback.textContent,lang==='ja'?/コピーできませんでした/:/Could not copy/);
  f.reset.fire('click');assert.equal(f.copyFallback.hidden,true);assert.equal(f.copyURL.value,'');
 }
}));
test('a pending clipboard response cannot leave stale feedback after a filter change or history restoration',()=>environment(async()=>{
 for(const reject of [false,true]){
  let finish;navigator.clipboard.writeText=()=>new Promise((resolve,fail)=>{finish=()=>reject?fail(Error('denied')):resolve();});
  const f=fixture();const [controller]=wireGoalFilters(f.scope);const pending=f.copy.fire('click');assert.equal(f.copy.disabled,true);
  if(reject)controller.sync();else f.chooseDomain('quantum');finish();await pending;
  assert.equal(f.copyFeedback.hidden,true);assert.equal(f.copyFallback.hidden,true);assert.equal(f.copy.disabled,false);
 }
}));
