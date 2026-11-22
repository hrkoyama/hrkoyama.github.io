import {makeSearch,excerpt,safePath} from './engine.mjs?v=c5253ad2c2b0';
import {appendMethodCard} from './method-search.mjs?v=e599bfbb1f40';
const main = document.querySelector('[data-search-index]');
const input = document.querySelector('#search-query');
const status = document.querySelector('#search-status');
const results = document.querySelector('#search-results');
const more = document.querySelector('#search-more');
const examples = document.querySelector('#search-examples');
const scopeControl=document.querySelector('#search-scope');
const related=document.querySelector('#search-related');
const relatedTitle=document.querySelector('#search-related-title');
const relatedRows=document.querySelector('#search-related-results');
const locale = () => ['ja','en'].includes(new URLSearchParams(location.search).get('lang')) ? new URLSearchParams(location.search).get('lang') : document.documentElement.lang === 'en' ? 'en' : 'ja';
const phrases = {
  ja: {loading:'検索対象を読み込んでいます…',ready:'公開ページ・資料 {count} 件を検索できます。',found:'「{query}」：{count} 件',none:'「{query}」に一致するページはありません。短い語や別の表記でお試しください。',failed:'検索データを読み込めませんでした。接続を確認して、もう一度お試しください。',ja:'日本語',en:'English',both:'日本語・English'},
  en: {loading:'Loading the search index…',ready:'Search {count} public pages and resources.',found:'{count} results for “{query}”',none:'No results for “{query}”. Try a shorter term or another spelling.',failed:'The search index could not be loaded. Check your connection and try again.',ja:'日本語',en:'English',both:'Japanese / English'}
};
const words = (key,values={}) => Object.entries(values).reduce((text,[key,value]) => text.replaceAll('{'+key+'}',String(value)),phrases[locale()][key]);
let engine, count=0, atlasCount=0, matches=[], query='', shown=20, version=0;
let loading;
function readQuery() {
  return (new URLSearchParams(location.hash.slice(1)).get('q') || '').trim().slice(0,200);
}
function label(doc) { return locale()==='en' && doc.titleEn ? doc.titleEn : doc.title; }
function showRows() {
  const direct=matches.filter(doc=>doc.kind==='method' || doc.executionPriority);
  const pages=matches.filter(doc=>doc.kind!=='method' && !doc.executionPriority);
  const fragment = document.createDocumentFragment(),secondary=document.createDocumentFragment();
  for (const doc of [...direct,...pages.slice(0,shown)]) {
    if(doc.kind==='method'){
      const item=document.createElement('li');appendMethodCard(item,doc,locale());fragment.append(item);continue;
    }
    const path = safePath(doc.url);
    if (!path) continue;
    const item=document.createElement('li');
    const heading=document.createElement('h2');
    const link=document.createElement('a');
    const url=new URL(path,location.origin);
    url.searchParams.set('lang',locale());
    link.href=url.pathname+url.search+url.hash;
    link.textContent=label(doc);
    heading.append(link);
    const meta=document.createElement('p');meta.className='search-meta';
    meta.textContent=doc.executionPriority?(locale()==='ja'?'固定入力の実行・検証例':'Runnable input and validation example'):(locale()==='en' ? doc.categoryEn : doc.categoryJa)+' · '+words(doc.lang);
    const summary=document.createElement('p');summary.className='search-excerpt';
    summary.textContent=doc.executionPriority && doc.execution?.snippet?.[locale()] ? doc.execution.snippet[locale()] : excerpt(doc.text,query);
    item.append(meta,heading,summary);(direct.length&&!doc.executionPriority?secondary:fragment).append(item);
  }
  results.replaceChildren(fragment);
  relatedRows.replaceChildren(secondary);
  related.hidden=!direct.length || !pages.length;
  relatedTitle.textContent=locale()==='ja'?`関連資料 ${pages.length}件`:`Related pages (${pages.length})`;
  more.hidden=shown>=pages.length;
  // Keep extra matches inside the disclosure when a method already answers the query.
  (direct.length?related:results.parentElement).append(more);
}
async function load() {
  if (engine) return;
  if (loading) return loading;
  loading=(async () => {
    const response=await fetch(main.dataset.searchIndex,{credentials:'omit'});
    if (!response.ok) throw Error('Search index HTTP '+response.status);
    const data=await response.json();
    if (!Array.isArray(data.documents) || data.documents.length>2000) throw Error('Invalid search index');
    engine=makeSearch(data.documents);count=data.documents.length;atlasCount=data.documents.filter(row=>row.url.startsWith('/numerical-methods-atlas/')).length;
  })();
  try {await loading;} finally {loading=null;}
}
async function render() {
  const ticket=++version;
  query=readQuery();input.value=query;shown=20;
  const scope=new URLSearchParams(location.search).get('scope')==='atlas'?'atlas':'all';
  scopeControl.value=scope;related.open=false;
  document.querySelectorAll('.site-search input').forEach(field => {field.value=query;});
  examples.hidden=!!query;
  status.textContent=words('loading');
  try {await load();} catch {
    status.textContent=words('failed');results.replaceChildren();related.hidden=true;more.hidden=true;return;
  }
  // Ignore an earlier response if the user changed the fragment during the fetch.
  if (ticket!==version)return;
  if (query!==readQuery()) {render();return;}
  matches=query ? engine(query,locale(),scope) : [];
  const methods=matches.filter(row=>row.kind==='method').length;
  const executions=matches.filter(row=>row.executionPriority).length;
  const counts=locale()==='ja'?[methods?`手法 ${methods}件`:'',executions?`実行例 ${executions}件`:'']:[methods?`${methods} method${methods===1?'':'s'}`:'',executions?`${executions} runnable example${executions===1?'':'s'}`:''];
  status.textContent=query ? methods||executions ? (locale()==='ja'?`「${query}」：${counts.filter(Boolean).join('・')}。公開済みの資料へ直接進めます。`:`${counts.filter(Boolean).join(', ')} for “${query}”. Open the available resources directly.`) : words(matches.length?'found':'none',{query,count:matches.length}) : words('ready',{count:scope==='atlas'?atlasCount:count});
  if(query && !matches.length && scope==='atlas')status.textContent+=(locale()==='ja'?' 検索範囲を「サイト全体」に変えることもできます。':' You can also change the scope to the whole site.');
  showRows();
}
scopeControl.addEventListener('change',()=>{
  const url=new URL(location.href);url.searchParams.set('scope',scopeControl.value);
  history.pushState(null,'',url);document.dispatchEvent(new CustomEvent('site-search-query'));
});
more.addEventListener('click',() => {shown+=20;showRows();});
document.addEventListener('site-search-query',render);
addEventListener('hashchange',render);
addEventListener('popstate',render);
render();
