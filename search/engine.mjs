import {findMethods,tokenIncludes} from './method-search.mjs?v=c52d8b139bcb';
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
export function makeSearch(documents) {
  const entries = documents.filter(doc => doc && typeof doc.text === 'string' && safePath(doc.url)).map(doc => ({
    doc, title: normalize(doc.title + ' ' + (doc.titleEn || '')),
    text: normalize(doc.text), headings: normalize(doc.headings || ''), category: normalize(doc.categoryText || ''),
    family: safePath(doc.url).replace(/\/(ja|en)\//, '/')
  }));
  return function search(query, language = 'ja', scope = 'all') {
    const phrase = normalize(String(query).slice(0,200));
    if (!phrase) return [];
    const terms = [...new Set(phrase.split(/\s+/).filter(term => !stop.has(term)))];
    if (!terms.length) return [];
    const scoped=entries.filter(entry => scope!=='atlas' || entry.doc.url.startsWith('/numerical-methods-atlas/'));
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
      const haystack = entry.title + ' ' + entry.category + ' ' + entry.text;
      if (!terms.every(term => tokenIncludes(haystack,term))) continue;
      let score = terms.reduce((total,term) => total + (entry.title.includes(term) ? 30 : entry.headings.includes(term) ? 16 : entry.category.includes(term) ? 12 : 1) + Math.min(8,Math.log2(1+entry.text.split(term).length-1)),0);
      if (entry.title.includes(phrase)) score += 50;
      if (entry.headings.includes(phrase)) score += 20;
      if (entry.text.includes(phrase)) score += 4;
      if (entry.category.includes(phrase) && /^\/[^/]+\/$/.test(safePath(entry.doc.url))) score += 45;
      if (entry.doc.lang === language || entry.doc.lang === 'both') score += 3;
      const result = { ...entry.doc, url:safePath(entry.doc.url), score };
      if (!best.has(entry.family) || best.get(entry.family).score < score) best.set(entry.family,result);
    }
    return [...executions,...methods,...[...best.values()].sort((a,b) => b.score-a.score || a.url.localeCompare(b.url))];
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
