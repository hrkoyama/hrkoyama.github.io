const key='atlas-goal-availability',domainKey='atlas-goal-domain';
const availabilityParam='goal-availability',domainParam='goal-domain';
const allowed=new Set(['all','run','code','reading','planned']);
const controllers=new WeakMap();
const tokens=value=>String(value||'').split(/\s+/).filter(Boolean);
const goalPaths=new Set(['/numerical-methods-atlas/','/numerical-methods-atlas/index.html','/numerical-methods-atlas/start/','/numerical-methods-atlas/start/index.html']);
export const goalMatches=(states,filter='all',domains='',domain='all')=>(filter==='all'||tokens(states).includes(filter))&&(domain==='all'||tokens(domains).includes(domain));
export function goalFilterURL(href,availability,domain){
 const url=new URL(href);url.searchParams.set(domainParam,domain);url.searchParams.set(availabilityParam,availability);return url;
}
const read=name=>{try{return sessionStorage.getItem(name);}catch{return null;}};
const save=(name,value)=>{try{sessionStorage.setItem(name,value);}catch{}};
const currentURL=()=>{try{return new URL(globalThis.location.href);}catch{return null;}};
function updateLinks(root,availability,domain){
 const url=currentURL();if(!url)return;
 const scope=root.ownerDocument||root;
 for(const link of scope.querySelectorAll('a[href]')){
  const raw=link.getAttribute('href');if(!raw||raw.startsWith('#')||link.hasAttribute('download'))continue;
  const target=new URL(raw,url);
  if(target.origin===url.origin&&goalPaths.has(target.pathname))link.setAttribute('href',goalFilterURL(target.href,availability,domain).href);
 }
}
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
  function writeURL(mode,clearAnchor=false){
   const current=currentURL();if(!current)return;
   const url=goalFilterURL(current.href,field.value,domainField.value);if(clearAnchor)url.hash='';
   if(url.href!==current.href){try{history[mode==='push'?'pushState':'replaceState'](history.state,'',url.href);}catch{}}
  }
  function render(value,domainValue,mode='replace'){
   const selected=allowed.has(value)?value:'all',domain=domains.has(domainValue)?domainValue:'all';
   field.value=selected;domainField.value=domain;
   const visible=new Set();
   for(const item of items){item.hidden=!goalMatches(item.dataset.goalStates,selected,item.dataset.goalDomains,domain);if(!item.hidden)visible.add(item.dataset.goalId);}
   status.textContent=ja?`${visible.size} / ${total} 件の目的`:`${visible.size} of ${total} goals`;
   empty.hidden=visible.size!==0;
   save(key,selected);save(domainKey,domain);
   if(mode)writeURL(mode,mode==='push'&&anchor()?.hidden);
   updateLinks(root,selected,domain);
  }
  function revealAnchor(){const target=anchor();if(target?.hidden)render('all','all');}
  function sync(){
   const params=currentURL()?.searchParams;
   const explicit=params?.has(availabilityParam)||params?.has(domainParam);
   render(explicit?params.get(availabilityParam):read(key),explicit?params.get(domainParam):read(domainKey));revealAnchor();
  }
  function change(){render(field.value,domainField.value,'push');}
  field.addEventListener('change',change);domainField.addEventListener('change',change);
  reset.addEventListener('click',()=>render('all','all','push'));
  sync();root.querySelector('[data-goal-controls]').hidden=false;
  const controller={revealAnchor,sync};controllers.set(root,controller);return controller;
 });
}
if(typeof document!=='undefined'){
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>wireGoalFilters());else wireGoalFilters();
 globalThis.addEventListener('hashchange',()=>{
  for(const root of document.querySelectorAll('[data-goal-filter-root]'))controllers.get(root)?.revealAnchor();
 });
 globalThis.addEventListener('popstate',()=>{
  for(const root of document.querySelectorAll('[data-goal-filter-root]'))controllers.get(root)?.sync();
 });
 globalThis.addEventListener('pageshow',event=>{
  if(event.persisted)for(const root of document.querySelectorAll('[data-goal-filter-root]'))controllers.get(root)?.sync();
 });
}
