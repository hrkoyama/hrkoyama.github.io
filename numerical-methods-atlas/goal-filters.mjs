const key='atlas-goal-availability',domainKey='atlas-goal-domain';
const allowed=new Set(['all','run','code','reading','planned']);
const controllers=new WeakMap();
const tokens=value=>String(value||'').split(/\s+/).filter(Boolean);
export const goalMatches=(states,filter='all',domains='',domain='all')=>(filter==='all'||tokens(states).includes(filter))&&(domain==='all'||tokens(domains).includes(domain));
const read=name=>{try{return sessionStorage.getItem(name);}catch{return null;}};
const save=(name,value)=>{try{sessionStorage.setItem(name,value);}catch{}};
export function wireGoalFilters(scope=document){
 const roots=scope.dataset?.goalFilterRoot!==undefined?[scope]:[...scope.querySelectorAll('[data-goal-filter-root]')];
 return roots.map(root=>{
  if(controllers.has(root))return controllers.get(root);
  const field=root.querySelector('[data-goal-filter]'),domainField=root.querySelector('[data-goal-domain]'),reset=root.querySelector('[data-goal-reset]');
  const status=root.querySelector('[data-goal-count]'),empty=root.querySelector('[data-goal-empty]');
  const items=[...root.querySelectorAll('[data-goal-item]')];
  const domains=new Set(['all',...items.flatMap(item=>tokens(item.dataset.goalDomains))]);
  const total=new Set(items.map(item=>item.dataset.goalId)).size,ja=root.dataset.goalLanguage==='ja';
  function anchor(){
   let id;try{id=decodeURIComponent(globalThis.location?.hash?.slice(1)||'');}catch{return null;}
   if(!id)return null;
   return items.find(item=>item.id===id)||null;
  }
  function render(value,domainValue,persist=false){
   const selected=allowed.has(value)?value:'all',domain=domains.has(domainValue)?domainValue:'all';
   field.value=selected;domainField.value=domain;
   const visible=new Set();
   for(const item of items){item.hidden=!goalMatches(item.dataset.goalStates,selected,item.dataset.goalDomains,domain);if(!item.hidden)visible.add(item.dataset.goalId);}
   status.textContent=ja?`${visible.size} / ${total} 件の目的`:`${visible.size} of ${total} goals`;
   empty.hidden=visible.size!==0;
   if(persist){save(key,selected);save(domainKey,domain);}
  }
  function revealAnchor(){const target=anchor();if(target?.hidden)render('all','all',true);}
  function change(){
   render(field.value,domainField.value,true);
   if(anchor()?.hidden && globalThis.history && globalThis.location){
    history.replaceState(null,'',location.pathname+location.search);
   }
  }
  field.addEventListener('change',change);domainField.addEventListener('change',change);
  reset.addEventListener('click',()=>render('all','all',true));
  render(read(key),read(domainKey));revealAnchor();root.querySelector('[data-goal-controls]').hidden=false;
  const controller={revealAnchor,sync(){render(read(key),read(domainKey));revealAnchor();}};controllers.set(root,controller);return controller;
 });
}
if(typeof document!=='undefined'){
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>wireGoalFilters());else wireGoalFilters();
 globalThis.addEventListener('hashchange',()=>{
  for(const root of document.querySelectorAll('[data-goal-filter-root]'))controllers.get(root)?.revealAnchor();
 });
 globalThis.addEventListener('pageshow',event=>{
  if(event.persisted)for(const root of document.querySelectorAll('[data-goal-filter-root]'))controllers.get(root)?.sync();
 });
}
