// Generated from frontend/search/engine.mjs by scripts/search_assets.py. Edit the source template.
import {findMethods,tokenIncludes} from './method-search.mjs?v=4e232938761d';
import {unpackSearchIndex} from './compact-index.mjs?v=5ac38c56172d';
import {publicNavigationPath} from './navigation.mjs?v=cbd24e09fe05';
const ORIGIN = 'https://hrkoyama.github.io';
export function safePath(value) {
  try {
    const url = new URL(value, ORIGIN);
    if (url.origin !== ORIGIN || url.username || url.password || !url.pathname.startsWith('/') || url.pathname.startsWith('//')) return null;
    return url.pathname + url.search + url.hash;
  } catch { return null; }
}
export function normalize(value) {
  return String(value).normalize('NFKC').toLowerCase().replace(/[‐‑‒–—−-]/g,' ').replace(/\s+/g,' ').trim();
}
const stop = new Set(['the','a','an','of','and','or','in','for','to','with']);
export const searchVocabulary=text=>[...new Set(normalize(text).split(' ').filter(Boolean))].sort().join(' ');
const atlasEngines=new WeakMap();
export function atlasSearchPath(entry,language){
 const path=publicNavigationPath(entry.routes?.[language]);if(!path)return null;
 if(/^\/numerical-methods-atlas\/[a-z0-9/?=.-]+$/.test(path))return path;
 if(entry.kind==='connection'&&new RegExp('^/numerical-methods-atlas/connections/\\?lang='+language+'#(?:dft-md|reaction-transport|poisson-fields)-'+language+'$').test(path))return path;
 if(entry.kind==='equation'&&new RegExp('^/numerical-methods-atlas/equations/\\?lang='+language+'#[a-z0-9-]+-'+language+'$').test(path))return path;
 if(entry.kind==='reference'&&new RegExp('^/numerical-methods-atlas/solutions/\\?lang='+language+'#solution-[a-z0-9-]+-'+language+'$').test(path))return path;
 return null;
}
/** Both browser entry points use this exact atlas corpus and ranking function. */
export function atlasSearch(input){
 if(atlasEngines.has(input))return atlasEngines.get(input);
 const index=unpackSearchIndex(input);
 const documents=index.entries.flatMap(entry=>{
  const routes=Object.fromEntries(['ja','en'].map(language=>[language,atlasSearchPath(entry,language)]).filter(([,path])=>path));
  const url=routes.ja||routes.en;if(!url)return [];
  const text=entry.text||{},search=entry.search_text||text;
  const body=typeof text==='string'?text:Object.values(text).join(' ');
  const searchable=typeof search==='string'?search:Object.values(search).join(' ');
  return [{id:entry.id,url,
   title:entry.title.ja||entry.title.en,titleEn:entry.title.en||entry.title.ja,
   ...(entry.title_aliases?{title_aliases:entry.title_aliases}:{}),
   text:body,search_text:[searchable,...(entry.keywords||[])].join(' '),
   headings:[...(entry.headings?.ja||[]),...(entry.headings?.en||[])].map(h=>h.title).join(' '),
   lang:entry.title.ja&&entry.title.en?'both':entry.title.ja?'ja':'en',
   kind:entry.kind,routes,snippet:entry.snippet,method:entry.method,
   execution:entry.kind==='execution-example'?{title:entry.title,focus_keywords:entry.focus_keywords||[],snippet:entry.snippet}:undefined,
   search_navigation:entry.search_navigation,text_ref:entry.text_ref,
   categoryJa:'数値解析',categoryEn:'Numerical methods',categoryText:'数値解析 Numerical methods',atlasEntry:entry}];
 });
 const engine=makeSearch(documents);atlasEngines.set(input,engine);return engine;
}
export function makeSearch(documents) {
  const entries = documents.filter(doc => doc && typeof doc.text === 'string' && safePath(doc.url)).map(doc => ({
    doc, title: normalize(doc.title + ' ' + (doc.titleEn || '') + ' ' + (Array.isArray(doc.title_aliases)?doc.title_aliases.filter(value=>typeof value==='string').join(' '):'')),
    text: searchVocabulary(doc.search_text||doc.text), headings: normalize(doc.headings || ''), category: normalize(doc.categoryText || ''),
    family: safePath(doc.url).replace(/\/(ja|en)\//, '/')
  }));
  return function search(query, language = 'ja', scope = 'all') {
    const phrase = normalize(String(query).slice(0,200));
    if (!phrase) return [];
    const terms = [...new Set(phrase.split(/\s+/).filter(term => !stop.has(term)))];
    if (!terms.length) return [];
    const scoped=entries.filter(entry => {
      if(scope==='atlas'&&!entry.doc.url.startsWith('/numerical-methods-atlas/'))return false;
      const atlas=entry.doc.atlasEntry;
      const locale=atlas?.title?.[language]?language:atlas?.title?.en?'en':'ja';
      return !atlas || !!entry.doc.routes?.[locale];
    });
    const methods=findMethods(scoped.filter(entry=>entry.doc.method).map(entry=>entry.doc.method),query,language)
      .map(result=>({...result,url:safePath(result.method.url),lang:'both',text:result.method.summary?.[language] || '',categoryJa:'数値解析',categoryEn:'Numerical methods'})).filter(result=>result.url);
    const intentWords=new Set(['実行','コード','テスト','入力','検証','再現','ダウンロード','run','code','test','tests','execute','execution','runnable','reproduce','validation','input','download','example']);
    const intent=terms.some(term=>intentWords.has(term));
    const focus=terms.filter(term=>!intentWords.has(term));
    const executions=scoped.filter(entry=>{
      const record=entry.doc.execution;if(!record || !focus.length)return false;
      const identity=normalize((record.focus_keywords || []).join(' '));
      if(!focus.every(term=>tokenIncludes(identity,term)))return false;
      return intent || (focus.length>1 && !methods.some(result=>result.exactMethod) && Object.values(record.title).some(title=>focus.some(term=>tokenIncludes(normalize(title),term))));
    }).map(entry=>({...entry.doc,kind:'execution-example',executionPriority:true,score:20000}));
    const executionPaths=new Set(executions.map(doc=>doc.url));
    const best = new Map();
    for (const entry of scoped) {
      if(executionPaths.has(entry.doc.url))continue;
      if(methods.length && entry.doc.method)continue;
      const entityPriority=['equation','reference','connection'].includes(entry.doc.kind)&&[
        String(entry.doc.id||entry.doc.search_navigation?.id||'').replace(/^(?:equation|reference)-/,''),
        entry.doc.title,entry.doc.titleEn,...Object.values(entry.doc.name||{})
      ].filter(value=>typeof value==='string'&&value).some(identity=>normalize(identity)===phrase);
      const haystack = entry.title + ' ' + entry.category + ' ' + entry.text;
      if (!entityPriority&&!terms.every(term => tokenIncludes(haystack,term))) continue;
      let score = terms.reduce((total,term) => total + (entry.title.includes(term) ? 30 : entry.headings.includes(term) ? 16 : entry.category.includes(term) ? 12 : 1) + Math.min(8,Math.log2(1+entry.text.split(term).length-1)),0);
      if (entry.title.includes(phrase)) score += 50;
      if (entry.headings.includes(phrase)) score += 20;
      if (entry.category.includes(phrase) && /^\/[^/]+\/$/.test(safePath(entry.doc.url))) score += 45;
      if (entry.doc.lang === language || entry.doc.lang === 'both') score += 3;
      const result = { ...entry.doc, url:safePath(entry.doc.url), score, entityPriority };
      if (!best.has(entry.family) || best.get(entry.family).score < score) best.set(entry.family,result);
    }
    const pages=[...best.values()].sort((a,b) => b.score-a.score || a.url.localeCompare(b.url));
    return [...executions,...methods.filter(result=>result.exactMethod),...pages.filter(result=>result.entityPriority),...methods.filter(result=>!result.exactMethod),...pages.filter(result=>!result.entityPriority)];
  };
}
export function excerpt(text, query, limit = 180) {
  const clean = String(text).replace(/\s+/g,' ').trim();
  const terms = normalize(query).split(/\s+/).filter(Boolean);
  // String offsets are kept on the original string so scientific symbols and case are preserved.
  const lower = clean.toLowerCase();
  const positions = terms.map(term => lower.indexOf(term)).filter(index => index >= 0);
  const start = Math.max(0,(positions.length ? Math.min(...positions) : 0)-45);
  return (start ? '…' : '') + clean.slice(start,start+limit) + (clean.length>start+limit ? '…' : '');
}
