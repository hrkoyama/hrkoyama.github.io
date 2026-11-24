// Generated from frontend/search/navigation.mjs by scripts/search_assets.py. Edit the source template.
/** Explicit, source-built cross-navigation shared by both search interfaces. */
import {loadSearchDetail} from './compact-index.mjs?v=ce58bf7efa65';
const origin='https://hrkoyama.github.io';
const groups=['methods','equations','figures','references','code'];
const copy={
 ja:{label:'関連資料への入口',methods:'手法',equations:'方程式',figures:'問題の図',references:'厳密解・参照解',code:'実行コード',sourceCode:'コード・検証',missing:'未登録',details:'対応する資料と確認範囲',same:'同じ問題の参照',related:'関連モデルの参照',sameProblem:'同じ問題',relatedModel:'関連モデル',preview:'保存された図'},
 en:{label:'Related resource routes',methods:'Methods',equations:'Equations',figures:'Problem figures',references:'Exact / reference solutions',code:'Execution code',sourceCode:'Code & checks',missing:'Not registered',details:'Linked resources and their scope',same:'Same-problem reference',related:'Related-model reference',sameProblem:'Same problem',relatedModel:'Related model',preview:'Saved figure'}
};

/** Same-site paths only; preserve the locale/query/fragment supplied by sources. */
export function publicNavigationPath(value){
 if(typeof value!=='string'||!value||/[\s\\\u0000-\u001f]/u.test(value))return null;
 try{
  const raw=new URL(value,origin),decoded=decodeURIComponent(raw.pathname);
  if(raw.origin!==origin||raw.username||raw.password||raw.pathname.startsWith('//'))return null;
  // Reject traversal before URL normalization as well as encoded private paths.
  const supplied=value.replace(/^https:\/\/hrkoyama[.]github[.]io/i,'').split(/[?#]/,1)[0];
  if([supplied,decodeURIComponent(supplied),decoded].some(path=>path.split('/').some(part=>part==='..'||part==='.'||part.startsWith('.'))))return null;
  return raw.pathname+raw.search+raw.hash;
 }catch{return null;}
}
function ensureStyle(){
 if(document.querySelector('link[data-search-navigation-style]'))return;
 const link=document.createElement('link');link.rel='stylesheet';link.dataset.searchNavigationStyle='';
 link.href=new URL('./navigation.css?v=6f60fecbfc1e',import.meta.url).href;document.head.append(link);
}
const localized=(value,language)=>typeof value==='string'?value:value?.[language]||value?.en||value?.ja||'';
function node(tag,css,text){
 const element=document.createElement(tag);if(css)element.className=css;
 if(text!==undefined)element.textContent=String(text);return element;
}
function link(path,text,css){
 const element=node('a',css,text);element.href=path;return element;
}
function entryPath(entry,language){return publicNavigationPath(localized(entry?.url,language));}
function name(entry,language){return localized(entry?.name,language)||entry?.id||'';}
function relation(entry,c,key){
 return entry.relation==='same-problem'?(key==='references'?c.same:c.sameProblem):entry.relation==='related-model'?(key==='references'?c.related:c.relatedModel):'';
}
function appendScope(target,entry,language,c,key){
 const relationship=relation(entry,c,key),note=localized(entry.note,language);
 if(relationship)target.append(node('p','search-navigation-relation',relationship));
 if(note)target.append(node('p','search-navigation-note',note));
}
function appendNamedEntry(list,entry,language,c,key){
 const path=entryPath(entry,language);if(!path)return;
 const item=node('li','search-navigation-entry');item.dataset.searchNavigationEntry=String(entry.id||'');
 item.dataset.searchNavigationGroup=key;
 const a=link(path,name(entry,language),'search-navigation-named-link');item.append(a);
 appendScope(item,entry,language,c,key);list.append(item);
}
function appendPreview(target,entry,language,c){
 const image=entry.image,path=publicNavigationPath(image?.url),destination=entryPath(entry,language);
 if(!path||!destination||!Number.isInteger(image.width)||!Number.isInteger(image.height)||image.width<=0||image.height<=0)return false;
 const figure=node('figure','search-navigation-preview'),a=link(destination,'','search-navigation-picture');
 a.dataset.searchNavigationPicture=String(entry.id||'');
 const img=node('img');img.src=path;img.width=image.width;img.height=image.height;img.loading='lazy';img.decoding='async';
 img.alt=localized(image.caption,language)||name(entry,language);a.append(img);figure.append(a);
 const caption=localized(image.caption,language);figure.append(node('figcaption','search-navigation-note',name(entry,language)+(caption?' — '+caption:'')));
 target.append(figure);return true;
}

/** Add no inferred resources and never recover a purpose-restricted parent graph. */
function appendFullNavigation(item,result,language='ja'){
 language=language==='en'?'en':'ja';const c=copy[language];
 const graph=Object.hasOwn(result,'search_navigation')?result.search_navigation:result.method?.search_navigation;
 if(!graph||typeof graph!=='object'||!graph.groups)return item;
 const available=Object.fromEntries(groups.map(key=>[key,(Array.isArray(graph.groups[key])?graph.groups[key]:[]).filter(entry=>entry&&entryPath(entry,language))]));
 if(!groups.some(key=>available[key].length))return item;
 ensureStyle();
 const wrapper=node('div','search-navigation');wrapper.dataset.searchNavigation=String(graph.id||'');
 const nav=node('nav','search-navigation-groups');nav.setAttribute('aria-label',c.label);
 for(const key of groups){
  const entries=available[key];
  const categoryLabel=key==='code'&&entries.length&&entries.every(entry=>entry.availability==='source')?c.sourceCode:c[key];
  if(!entries.length){
   const missing=node('span','search-navigation-unavailable',c[key]);missing.dataset.searchNavigationCategory=key;
   missing.setAttribute('aria-label',c[key]+': '+c.missing);nav.append(missing);
  }else if(entries.length===1){
   const a=link(entryPath(entries[0],language),categoryLabel,'search-navigation-direct');a.dataset.searchNavigationCategory=key;nav.append(a);
  }else{
   const details=node('details','search-navigation-category');details.dataset.searchNavigationCategory=key;
   const summary=node('summary','',categoryLabel+' ('+entries.length+')'),list=node('ul','search-navigation-entry-list');
   for(const entry of entries)appendNamedEntry(list,entry,language,c,key);
   details.append(summary,list);nav.append(details);
  }
 }
 wrapper.append(nav);
 const graphNote=localized(graph.note,language),singles=groups.flatMap(key=>available[key].length===1?[{key,entry:available[key][0]}]:[]);
 const preview=groups.flatMap(key=>available[key]).find(entry=>entry.image&&publicNavigationPath(entry.image.url));
 if(graphNote||singles.length||preview){
  const details=node('details','search-navigation-context'),summary=node('summary','',c.details),body=node('div','search-navigation-context-body');
  if(graphNote)body.append(node('p','search-navigation-note',graphNote));
  if(singles.length){
   const list=node('ul','search-navigation-entry-list');
   for(const {key,entry}of singles)appendNamedEntry(list,entry,language,c,key);
   body.append(list);
  }
  if(preview)appendPreview(body,preview,language,c);
  details.append(summary,body);wrapper.append(details);
 }
 item.append(wrapper);return item;
}

/** The same labels and destinations, with large scope graphs opened on demand. */
export function appendSearchNavigation(item,result,language='ja'){
 const graph=Object.hasOwn(result,'search_navigation')?result.search_navigation:result.method?.search_navigation;
 if(!graph?.details_ref)return appendFullNavigation(item,result,language);
 if(!/^[a-f0-9]{64}$/.test(graph.details_ref)||!graph.counts||!graph.groups)return item;
 language=language==='ja'?'ja':'en';const c=copy[language];ensureStyle();
 const wrapper=node('div','search-navigation');wrapper.dataset.searchNavigation=String(graph.id||'');
 const nav=node('nav','search-navigation-groups');nav.setAttribute('aria-label',c.label);const disclosures=[];
 const hint=language==='ja'?'開くと関連資料を読み込みます。':'Open to load the related resources.';
 let loading=false;
 async function expand(){
  if(loading)return;loading=true;
  try{
   const data=await loadSearchDetail(graph.details_ref),full=data.search_navigation;
   if(!full||full.kind!==graph.kind||full.id!==graph.id||!full.groups)throw Error('Wrong search navigation');
   if(!item.isConnected)return;
   const holder=node('div');appendFullNavigation(holder,{...result,search_navigation:full},language);
   const replacement=holder.children[0];if(!replacement)throw Error('Missing search navigation');
   for(const {details,key}of disclosures)if(details.open){
    const next=key==='context'?replacement.querySelector('.search-navigation-context'):replacement.querySelector('[data-search-navigation-category="'+key+'"]');
    if(next)next.open=true;
   }
   item.insertBefore(replacement,wrapper);wrapper.remove();
  }catch{
   for(const {body}of disclosures)body.textContent=language==='ja'?'読み込めませんでした。もう一度開いてください。':'Could not load. Close and open again to retry.';
  }finally{loading=false;}
 }
 function disclosure(key,label,css){
  const details=node('details',css),summary=node('summary','',label),body=node('p','search-navigation-note',hint);
  details.append(summary,body);details.addEventListener('toggle',()=>{if(details.open)expand();});disclosures.push({details,key,body});return details;
 }
 for(const key of groups){
  const count=graph.counts[key],single=graph.groups[key]?.[0],path=single&&entryPath(single,language);
  if(!Number.isInteger(count)||count<0)return item;
  const label=key==='code'&&single?.availability==='source'?c.sourceCode:c[key];
  let category;
  if(count===1&&path)category=link(path,label,'search-navigation-direct');
  else if(count>0)category=disclosure(key,label+' ('+count+')','search-navigation-category');
  else{category=node('span','search-navigation-unavailable',c[key]);category.setAttribute('aria-label',c[key]+': '+c.missing);}
  category.dataset.searchNavigationCategory=key;nav.append(category);
 }
 wrapper.append(nav);wrapper.append(disclosure('context',c.details,'search-navigation-context'));item.append(wrapper);return item;
}
