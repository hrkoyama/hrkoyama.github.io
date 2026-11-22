const key='atlas-goal-availability';
const allowed=new Set(['all','run','code','reading','planned']);
const controllers=new WeakMap();
export const goalMatches=(states,filter='all')=>filter==='all'||String(states).split(/\s+/).includes(filter);
const read=()=>{try{return sessionStorage.getItem(key);}catch{return null;}};
const save=value=>{try{sessionStorage.setItem(key,value);}catch{}};
export function wireGoalFilters(scope=document){
 const roots=scope.dataset?.goalFilterRoot!==undefined?[scope]:[...scope.querySelectorAll('[data-goal-filter-root]')];
 return roots.map(root=>{
  if(controllers.has(root))return controllers.get(root);
  const field=root.querySelector('[data-goal-filter]'),reset=root.querySelector('[data-goal-reset]');
  const status=root.querySelector('[data-goal-count]'),empty=root.querySelector('[data-goal-empty]');
  const items=[...root.querySelectorAll('[data-goal-item]')];
  const total=new Set(items.map(item=>item.dataset.goalId)).size,ja=root.dataset.goalLanguage==='ja';
  let selected='all';
  function anchor(){
   let id;try{id=decodeURIComponent(globalThis.location?.hash?.slice(1)||'');}catch{return null;}
   if(!id)return null;
   return items.find(item=>item.id===id)||null;
  }
  function render(value,persist=false){
   selected=allowed.has(value)?value:'all';field.value=selected;
   const visible=new Set();
   for(const item of items){item.hidden=!goalMatches(item.dataset.goalStates,selected);if(!item.hidden)visible.add(item.dataset.goalId);}
   status.textContent=ja?`${visible.size} / ${total} 件の目的`:`${visible.size} of ${total} goals`;
   empty.hidden=visible.size!==0;
   if(persist)save(selected);
  }
  function revealAnchor(){const target=anchor();if(target?.hidden)render('all',true);}
  field.addEventListener('change',()=>{
   render(field.value,true);
   if(anchor()?.hidden && globalThis.history && globalThis.location){
    history.replaceState(null,'',location.pathname+location.search);
   }
  });
  reset.addEventListener('click',()=>render('all',true));
  render(read());revealAnchor();root.querySelector('[data-goal-controls]').hidden=false;
  const controller={revealAnchor,sync(){render(read());revealAnchor();}};controllers.set(root,controller);return controller;
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
