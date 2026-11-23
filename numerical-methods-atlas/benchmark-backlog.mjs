/** Browser-only filters for saved backlog records; never start a calculation. */
const names=['field','priority','state','kind'];
const normalize=value=>String(value||'').normalize('NFKC').toLowerCase().replace(/\s+/g,' ').trim();
const controllers=new WeakMap();
export function backlogMatches(record,filters={}){
 for(const name of names){
  const wanted=filters[name]||'all',actual=name==='field'?record.field_id:record[name];
  if(wanted!=='all'&&wanted!==actual)return false;
 }
 const words=normalize(filters.query).split(' ').filter(Boolean);
 const corpus=normalize(record.search||[record.id,...Object.values(record.title||{}),record.current,...(record.tasks||[])].join(' '));
 return words.every(word=>corpus.includes(word));
}
export function wireBenchmarkBacklog(scope=document){
 const roots=scope.dataset?.backlogRoot!==undefined?[scope]:[...scope.querySelectorAll('[data-backlog-root]')];
 return roots.map(root=>{
  if(controllers.has(root))return controllers.get(root);
  const controls=root.querySelector('[data-backlog-controls]'),query=root.querySelector('[data-backlog-query]');
  const selects=Object.fromEntries(names.map(name=>[name,root.querySelector(`[data-backlog-filter="${name}"]`)]));
  const items=[...root.querySelectorAll('[data-backlog-item]')],groups=[...root.querySelectorAll('[data-backlog-field-group]')];
  const count=root.querySelector('[data-backlog-count]'),empty=root.querySelector('[data-backlog-empty]');
  const reset=root.querySelector('[data-backlog-reset]'),ja=root.dataset.backlogRoot==='ja';
  const allowed=Object.fromEntries(names.map(name=>[name,new Set(['all',...items.map(item=>item.dataset['backlog'+name[0].toUpperCase()+name.slice(1)])])]));
  const rows=items.map(item=>({item,record:{id:item.dataset.backlogId,field_id:item.dataset.backlogField,priority:item.dataset.backlogPriority,state:item.dataset.backlogState,kind:item.dataset.backlogKind,search:item.dataset.backlogSearch}}));
  function currentURL(){try{return new URL(globalThis.location.href);}catch{return null;}}
  function target(){
   let id;try{id=decodeURIComponent(globalThis.location?.hash?.slice(1)||'');}catch{return null;}
   return rows.find(row=>row.item.querySelector('details')?.id===id)||null;
  }
  function render(write=false){
   const filters=Object.fromEntries(names.map(name=>[name,allowed[name].has(selects[name].value)?selects[name].value:'all']));filters.query=query.value;
   for(const name of names)selects[name].value=filters[name];
   let shown=0;
   for(const row of rows){row.item.hidden=!backlogMatches(row.record,filters);if(!row.item.hidden)shown++;}
   for(const group of groups)group.hidden=!rows.some(row=>row.record.field_id===group.dataset.backlogFieldGroup&&!row.item.hidden);
   count.textContent=ja?`${shown} / ${rows.length} 件の候補`:`${shown} of ${rows.length} candidates`;empty.hidden=shown!==0;
   if(write){
    const url=currentURL();if(url){
     for(const name of names)filters[name]==='all'?url.searchParams.delete('backlog-'+name):url.searchParams.set('backlog-'+name,filters[name]);
     // Free text stays in browser memory, including on reload/citation clicks.
     // Only categorical filter values are carried in the URL.
     url.searchParams.delete('backlog-query');
     if(target()?.item.hidden)url.hash='';
     try{history.replaceState(history.state,'',url.href);}catch{}
    }
   }
   return shown;
  }
  function showAll(write=true){for(const name of names)selects[name].value='all';query.value='';return render(write);}
  function revealAnchor(){
   const row=target();if(!row)return;
   if(row.item.hidden)showAll(true);
   row.item.querySelector('details').open=true;
  }
  function sync(){
   const url=currentURL();for(const name of names)selects[name].value=allowed[name].has(url?.searchParams.get('backlog-'+name))?url.searchParams.get('backlog-'+name):'all';
   query.value='';render();revealAnchor();
  }
  for(const name of names)selects[name].addEventListener('change',()=>render(true));
  query.addEventListener('input',()=>render(true));root.querySelector('form')?.addEventListener('submit',event=>{event.preventDefault();render(true);});
  reset.addEventListener('click',()=>showAll());sync();controls.hidden=false;
  const controller={sync,revealAnchor,render};controllers.set(root,controller);return controller;
 });
}
if(typeof document!=='undefined'){
 const boot=()=>wireBenchmarkBacklog();
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
 globalThis.addEventListener('hashchange',()=>{for(const root of document.querySelectorAll('[data-backlog-root]'))controllers.get(root)?.revealAnchor();});
 globalThis.addEventListener('popstate',()=>{for(const root of document.querySelectorAll('[data-backlog-root]'))controllers.get(root)?.sync();});
}
