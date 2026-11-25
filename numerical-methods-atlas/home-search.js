// Generated from frontend/search/home-search.js by scripts/search_assets.py. Edit the source template.
import {atlasSearch} from '../search/engine.mjs?v=435452f9b73f';
import {currentLanguage} from './i18n.js';
import {readingURL} from './reading-urls.js';
import {appendMethodCard,tokenIncludes} from '../search/method-search.mjs?v=65b1257a6f10';
import {appendSearchNavigation,publicNavigationPath} from '../search/navigation.mjs?v=cbd24e09fe05';
const esc=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const normalizeSearch=value=>String(value).normalize('NFKC').toLocaleLowerCase().replace(/[‐‑‒–—−-]/g,' ').replace(/\s+/g,' ').trim();
const plain=value=>String(value).replace(/<[^>]*>/g,' ').replace(/&(?:amp|lt|gt|quot|#39|nbsp);/g,c=>({'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&#39;':"'",'&nbsp;':' '}[c])).replace(/\s+/g,' ').trim();
const executionIntents=new Set(['実行','コード','入力','検証','再現','ダウンロード','run','code','execute','execution','runnable','reproduce','validation','input','download','example']);
const kindLabels={
 equation:{ja:'方程式',en:'Equation'},
 reference:{ja:'厳密解・参照解',en:'Exact / reference solution'},
 problem:{ja:'テスト問題',en:'Test problem'},
 connection:{ja:'分野間のつながり',en:'Cross-field connection'},
 'execution-example':{ja:'実行例',en:'Runnable example'},
 method:{ja:'手法',en:'Method'},
 chapter:{ja:'解説章',en:'Reading chapter'},
 resource:{ja:'一覧・案内',en:'Index / guide'}
};

/** One logical chapter per record, with both editions and glossary aliases. */
export function buildHomeSearchIndex(english,japanese,coverage,glossary){
 return {version:1,scope:'chapter titles, section headings, model and method labels, glossary aliases',entries:Object.entries(english).map(([id,en])=>{
  const ja=japanese[id],items=coverage.items.filter(item=>item.chapter===id),terms=glossary.terms.filter(term=>term.chapter===id);
  return {id,title:{en:plain(en.title||id),ja:ja?plain(ja.title||en.title):null},headings:{en:en.headings.map(h=>({id:h.id,title:plain(h.title)})),ja:ja?ja.headings.map(h=>({id:h.id,title:plain(h.title)})):[]},keywords:[...new Set([...items.flatMap(item=>[item.label,item.group]),...terms.flatMap(term=>[term.en,term.ja,...(term.aliases||[])])].filter(Boolean))]};
 })};
}
function localSearchURL(entry,locale){
 const raw=entry.routes?.[locale],path=publicNavigationPath(raw);if(!path)return null;
 if(/^\/numerical-methods-atlas\/[a-z0-9/?=.-]+$/.test(path)&&!path.includes('..'))return path;
 if(entry.kind==='connection'&&/^\/numerical-methods-atlas\/connections\/\?lang=(ja|en)#(?:dft-md|reaction-transport|poisson-fields)-\1$/.test(path)&&path.startsWith('/numerical-methods-atlas/connections/?lang='+locale+'#'))return path;
 if(entry.kind==='equation'&&new RegExp('^/numerical-methods-atlas/equations/\\?lang='+locale+'#[a-z0-9-]+-'+locale+'$').test(path))return path;
 if(entry.kind==='reference'&&new RegExp('^/numerical-methods-atlas/solutions/\\?lang='+locale+'#solution-[a-z0-9-]+-'+locale+'$').test(path))return path;
 return null;
}
export function searchChapters(index,query,language='en'){
 const found=atlasSearch(index)(query,language,'atlas');
 const methods=found.some(result=>result.kind==='method');
 return found.map(result=>{
  const entry=result.atlasEntry,locale=result.locale||(language==='ja'&&entry?.title?.ja?'ja':entry?.title?.en?'en':'ja');
  if(result.kind==='method'){
   const path=publicNavigationPath(result.method.url);
   const url=path?new URL(path,'https://hrkoyama.github.io'):null;
   if(url)url.searchParams.set('lang',locale);
   return {...result,badge:kindLabels.method[locale],url:url?url.pathname+url.search+url.hash:null};
  }
  const title=entry?.title?.[locale]||result.titleEn||result.title;
  const headings=entry?.headings?.[locale]||[],q=normalizeSearch(query),words=q.split(' ');
  const heading=headings.find(h=>normalizeSearch(h.title).includes(q))||headings.find(h=>words.every(word=>tokenIncludes(normalizeSearch(h.title),word)));
  const kind=Object.hasOwn(kindLabels,result.kind)?result.kind:'chapter';
  const snippet=entry?.snippet?.[locale]||'';
  return {...result,id:entry?.id||result.id,title,locale,section:heading?.id||'',badge:kindLabels[kind][locale],
   detail:snippet||heading?.title||(entry?.keywords||[]).slice(0,4).join(' · '),
   url:publicNavigationPath(result.routes?.[locale]||result.url),
   related:methods&&!result.executionPriority&&!result.entityPriority};
 });
}

const copy={ja:{label:'アトラスを検索',placeholder:'例：KEEP法、Roe、WENO-Z、Sod 実行',hint:'手法の解説・公開コード・テストへ直接進めます。日英の名称・別名に対応し、検索語はこのブラウザ内で処理します。',related:'関連資料',all:'すべての結果をアトラス内で検索',button:'検索',empty:'キーワードを入力してください。',loading:'検索データを読み込んでいます…',none:'該当する項目がありません。別の用語や英語名でもお試しください。',failed:'検索データを読み込めませんでした。もう一度「検索」を押してください。',english:'英語の解説',count:(n,m)=>`${n}件が該当${n>m?`（上位${m}件を表示）`:''}`},en:{label:'Search the atlas',placeholder:'e.g. KEEP, Roe, WENO-Z, Sod run',hint:'Go directly to method explanations, published code and tests. Search English or Japanese names and aliases; search terms stay in this browser.',related:'Related resources',all:'View all atlas search results',button:'Search',empty:'Enter a keyword to find an entry.',loading:'Loading the search index…',none:'No entries match. Try another term or its Japanese name.',failed:'The search index could not load. Press Search to try again.',english:'English chapter',count:(n,m)=>`${n} matching entr${n===1?'y':'ies'}${n>m?` (showing ${m})`:''}`}};
export function homeSearchPage({compact=false,staticMode=false}={}){
 const lang=currentLanguage(),c=copy[lang];
 if(staticMode)return `<section class="page-width home-search home-search-fallback"><a class="home-search-static" href="/search/?scope=atlas&amp;lang=${lang}"><span>${c.label}</span><span aria-hidden="true">→</span></a></section>`;
 const goal=compact?'':`<p class="home-goal-entry"><a href="/numerical-methods-atlas/start/?lang=${lang}">${lang==='ja'?'目的から探す：流体・量子化学・温度制御・生物など':'Start with a goal: fluids, quantum chemistry, temperature control and biology'}</a></p>`;
 const hint=compact?(lang==='ja'?'手法名や計算したい内容で探せます。':'Search by method or by what you want to calculate.'):c.hint;
 const placeholder=compact?(lang==='ja'?'例：Bratu、Poisson、WENO':'e.g. Bratu, Poisson, WENO'):c.placeholder;
 return `<section class="page-width home-search${compact?' home-search-compact':''}" data-localize="false" aria-labelledby="home-search-label">${goal}<form role="search" id="home-search-form"><label for="home-search-input" id="home-search-label">${c.label}</label><div class="home-search-controls"><input id="home-search-input" type="search" placeholder="${esc(placeholder)}" aria-describedby="home-search-hint" autocomplete="off"><button type="submit">${c.button}</button></div><p id="home-search-hint">${hint}</p></form><p id="home-search-status" role="status" aria-live="polite"></p><ol id="home-search-results" hidden></ol><details id="home-search-related" hidden><summary id="home-search-related-label">${c.related}</summary><ol id="home-search-related-results"></ol></details><a id="home-search-all" class="text-link" href="/search/?scope=atlas&amp;lang=${lang}" hidden>${c.all}</a></section>`;
}
let indexPromise;
function loadIndex(){
 if(!indexPromise)indexPromise=fetch(new URL('../search/atlas-query-index.json?v=1110d7fafce3',import.meta.url)).then(r=>{if(!r.ok)throw Error('Search index unavailable');return r.json();}).catch(error=>{indexPromise=null;throw error;});
 return indexPromise;
}
export function wireHomeSearch(){
 const form=document.getElementById('home-search-form');if(!form)return;
 const input=form.querySelector('input'),status=document.getElementById('home-search-status'),list=document.getElementById('home-search-results'),language=currentLanguage(),c=copy[language];
 const related=document.getElementById('home-search-related'),relatedList=document.getElementById('home-search-related-results'),relatedLabel=document.getElementById('home-search-related-label'),allLink=document.getElementById('home-search-all');
 function renderResult(result,target){
  const li=document.createElement('li');
  if(result.method){appendMethodCard(li,result,language);target.append(li);return;}
  const a=document.createElement('a');a.href=result.url||readingURL(new URL('.',import.meta.url),result.id,result.locale,result.section);a.textContent=result.title;li.append(a);
  const badge=document.createElement('small');badge.className='home-search-kind';badge.textContent=result.badge;li.prepend(badge,document.createTextNode(' '));
  if(result.detail){const p=document.createElement('p');p.textContent=result.detail;li.append(p);}
  if(language==='ja'&&result.locale==='en'){const note=document.createElement('small');note.textContent=c.english;li.append(note);}
  appendSearchNavigation(li,result,language);
  target.append(li);
 }
 let version=0,timer,composing=false;
 async function update(){
  if(!form.isConnected)return;
  const ticket=++version,query=input.value.trim();list.hidden=true;list.replaceChildren();
  if(related){related.hidden=true;related.open=false;}
  if(relatedList)relatedList.replaceChildren();
  if(allLink)allLink.hidden=true;
  if(!query){status.textContent='';return;}
  status.textContent=c.loading;
  try{
   const index=await loadIndex();if(ticket!==version||!form.isConnected)return;
   const found=searchChapters(index,query,language),direct=found.filter(result=>!result.related),mentions=found.filter(result=>result.related),shown=direct.slice(0,8);
   status.textContent=found.length?c.count(direct.length,shown.length):c.none;
   for(const result of shown)renderResult(result,list);
   if(related&&relatedList&&mentions.length){
    for(const result of mentions.slice(0,8))renderResult(result,relatedList);
    if(relatedLabel)relatedLabel.textContent=`${c.related} (${mentions.length})`;
    related.hidden=false;
   }
   if(allLink){
    allLink.href=`/search/?scope=atlas&lang=${language}#q=${encodeURIComponent(query)}`;
    allLink.hidden=false;
   }
   list.hidden=!shown.length;
  }catch{if(ticket===version&&form.isConnected)status.textContent=c.failed;}
 }
 // Public word-search entry
 document.querySelectorAll('[data-atlas-word-search]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();input.focus({preventScroll:true});form.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});}));
 const schedule=()=>{clearTimeout(timer);++version;if(!composing)timer=setTimeout(update,120);};
 input.addEventListener('input',schedule);
 input.addEventListener('compositionstart',()=>{composing=true;clearTimeout(timer);++version;});
 input.addEventListener('compositionend',()=>{composing=false;schedule();});
 form.addEventListener('submit',event=>{event.preventDefault();clearTimeout(timer);update();});
}
