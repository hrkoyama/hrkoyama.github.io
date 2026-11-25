import {homeLandingCopy} from './atlas-home-data.js?v=e0ad4044e23f';
import {homeSearchPage,wireHomeSearch} from './home-search.js?v=90085eda7e79';
import {t,currentLanguage} from './i18n.js';
import {homeAreas,homeCopy,homePaths,homeReadingLanguages} from './home-overview-data.js?v=c7bda9b62571';
const esc=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=(key,values)=>esc(t(homeCopy[key],values));
const locale=lang=>['ja','en'].includes(lang)?lang:currentLanguage();

function routeURL(route,lang=currentLanguage()){
 lang=locale(lang);
 if(route.startsWith('/read/')){
  const [chapter,search='']=route.slice(6).split('?');
  const edition=homeReadingLanguages[chapter]?.includes(lang)?lang:'en';
  const section=new URLSearchParams(search).get('section');
  return `/numerical-methods-atlas/${edition}/read/${chapter}/`+(section?'#'+encodeURIComponent(section):'');
 }
 if(route.startsWith('/numerical-methods-atlas/')){
  const url=new URL(route,'https://hrkoyama.github.io');url.searchParams.set('lang',lang);
  return url.pathname+url.search+url.hash;
 }
 return '#'+route;
}
const link=(route,key,cls='',lang=currentLanguage())=>`<a href="${esc(routeURL(route,lang))}"${cls?` class="${cls}"`:''}>${esc(t(key))}</a>`;
const entryLink=(entry,lang)=>`<a href="${esc(routeURL(entry.route,lang))}" data-home-kind="${esc(entry.kind)}"><span>${esc(t(entry.name))}</span><span class="badge ${esc(entry.kind)}">${text(entry.kind)}</span></a>`;
const connection=(entries,label,lang)=>`<section class="connection"><h4 class="connection-label">${text(label)}</h4><ul>${entries.map(entry=>`<li>${entryLink(entry,lang)}</li>`).join('')}</ul></section>`;

export const resolveHomeArea=id=>homeAreas.find(area=>area.id===id)||homeAreas[0];
export function homeAreaURL(href,area){
 const url=new URL(href),parts=url.hash.slice(1).split('?'),query=new URLSearchParams(parts[1]||'');
 query.set('area',resolveHomeArea(area).id);url.hash='/?'+query.toString();return url.href;
}
export function homeAreaDetail(id,lang=currentLanguage(),{headingId='home-detail-title'}={}){
 const area=resolveHomeArea(id);lang=locale(lang);
 const groups=[area.groups[0],area.groups[1],area.execution||area.groups[2]];
 const related=area.execution?`<details class="area-related"><summary>${text('related-exhibits')}</summary><ul>${area.groups[2].map(entry=>`<li>${entryLink(entry,lang)}</li>`).join('')}</ul></details>`:'';
 const planned=area.plans?`<aside class="area-planned"><h4>${text('planned-label')}</h4><ul>${area.plans.map(entry=>`<li>${entryLink(entry,lang)}</li>`).join('')}</ul></aside>`:'';
 return `<p class="eyebrow">${esc(t(area.name))}</p><h3 id="${esc(headingId)}">${esc(t(area.question))}</h3><p class="detail-description">${esc(t(area.description))}</p>${groups.map((group,i)=>connection(group,['models-label','methods-label','verify-label'][i],lang)).join('')}${related}${planned}<div class="detail-footer">${link(area.overview,homeCopy['area-reading'],'',lang)}${link('/numerical-methods-atlas/methods/',homeCopy['inspect-scope'],'',lang)}${area.entry.startsWith('/read/')?'':link(area.entry,homeCopy['start-area'],'quiet-link',lang)}</div>`;
}

/** Configure the locale first; lang selects real reading editions and stable links. */
export function renderHomeMap(selected,lang=currentLanguage(),{staticMode=false}={}){
 const area=resolveHomeArea(selected);lang=locale(lang);
 const suffix=staticMode?'-'+lang:'';
 const heading=`<div class="section-heading"><div><p class="eyebrow">${text('map-eyebrow')}</p><h2 id="home-map-title${suffix}">${text('map-title')}</h2></div><p>${text('map-description')}</p></div>`;
 let body;
 if(staticMode){
  const directory=`<nav class="static-area-directory" aria-label="${text('static-directory')}"><ul>${homeAreas.map(entry=>`<li><a data-home-reading="${entry.id}" href="${esc(routeURL(entry.overview,lang))}">${esc(t(entry.name))}</a></li>`).join('')}</ul></nav>`;
  body=`<p class="static-map-note">${text('static-map-note')}</p>${directory}<div class="home-static-areas">${homeAreas.map(entry=>`<details class="static-domain" data-static-area="${entry.id}" id="atlas-area-${entry.id}-${lang}"${entry.id===area.id?' open':''}><summary><strong>${esc(t(entry.name))}</strong><span>${esc(t(entry.hint))}</span></summary><div class="domain-panel">${homeAreaDetail(entry.id,lang,{headingId:`home-detail-title-${entry.id}-${lang}`})}</div></details>`).join('')}</div>`;
 }else{
  body=`<div class="map-layout"><div class="map-index"><div class="domain-grid" role="group" aria-label="${text('map-label')}">${homeAreas.map(entry=>`<div class="domain-choice"><button type="button" class="domain-button" data-home-area="${entry.id}" aria-pressed="${entry.id===area.id}" aria-controls="home-domain-detail"><strong>${esc(t(entry.name))}</strong><span class="domain-hint">${esc(t(entry.hint))}</span></button><a class="domain-reading" data-home-reading="${entry.id}" href="${esc(routeURL(entry.overview,lang))}" aria-label="${esc(t(entry.name))}: ${text('area-reading')}">${text('area-reading')}</a></div>`).join('')}</div></div><section class="domain-panel" id="home-domain-detail" aria-labelledby="home-detail-title">${homeAreaDetail(area.id,lang)}</section></div><p class="home-selection-status" role="status" aria-live="polite"></p>`;
 }
 const map=`<section class="page-width overview" id="atlas-map${suffix}" aria-labelledby="home-map-title${suffix}">${heading}<p class="map-scope">${text('scope')}</p>${body}</section>`;
 return staticMode?`<div class="home-overview home-map-fallback" data-localize="false">${map}</div>`:map;
}

/** Retain the learning routes on the detailed exploration page. */
export function renderHomeGuides(lang=currentLanguage()){
 lang=locale(lang);
 return `<section class="page-width guided" aria-labelledby="home-start-title-${lang}"><h2 id="home-start-title-${lang}">${text('start-title')}</h2><p class="guided-intro">${text('start-description')}</p><div class="guided-list">${homePaths.map(path=>`<article class="guided-route"><p class="eyebrow">${esc(t(path.tag))}</p><h3>${esc(t(path.title))}</h3><p>${esc(t(path.description))}</p><ol>${path.links.map(([route,key])=>`<li>${link(route,key,'',lang)}</li>`).join('')}</ol></article>`).join('')}</div></section>`;
}

/** Small secondary routes shared by the front door and the reading directory. */
export function renderHomeBrowse(lang=currentLanguage(),{headingId}={}){
 lang=locale(lang);const ja=lang==='ja';headingId=headingId||'home-browse-title-'+lang;
 const cards=[
  {id:'solutions',title:ja?'厳密解・参照解':'Exact and reference solutions',description:ja?'計算結果を照合する基準を探す。':'Find a standard for checking a computed result.',visual:'<span class="home-browse-formula" aria-hidden="true">u<sub>exact</sub><br>u<sub>ref</sub></span>'},
  {id:'gallery',title:ja?'テスト問題（名前と図）':'Test problems by name and figure',description:ja?'問題名と保存済みの図から選ぶ。':'Choose a problem by name or stored figure.',visual:'<img src="/numerical-methods-atlas/assets/field-taylor-green.png" width="1575" height="690" loading="lazy" alt="'+(ja?'保存済みTaylor–Green渦の速度・圧力場':'Stored Taylor–Green velocity and pressure fields')+'">'},
  {id:'equations',title:ja?'方程式':'Equations',description:ja?'解きたい方程式から解説へ進む。':'Start with the equation you want to solve.',visual:'<span class="home-browse-formula" aria-hidden="true">F(u) = 0<br>∂<sub>t</sub>u = …</span>'},
 ];
 return `<nav class="page-width home-browse" aria-labelledby="${esc(headingId)}"><h2 id="${esc(headingId)}">${ja?'式や図から探す':'Browse by equations and figures'}</h2><ul class="home-browse-grid">${cards.map(card=>`<li><a class="home-browse-card" data-home-browse="${card.id}" href="/numerical-methods-atlas/${card.id}/?lang=${lang}"><span class="home-browse-visual">${card.visual}</span><span class="home-browse-copy"><strong>${esc(card.title)}</strong><span>${esc(card.description)}</span></span></a></li>`).join('')}</ul></nav>`;
}

/** The front door offers one search and three paths; inventories live beyond it. */
export function homeOverviewPage(coverage,selected,{staticMode=false}={}){
 const lang=currentLanguage(),copy=homeLandingCopy[lang],suffix=staticMode?'-'+lang:'';
 return `<div class="home-overview home-landing" id="home-overview${suffix}" data-localize="false">
 <header class="page-width landing-heading"><h1 id="home-landing-title${suffix}">${esc(copy.title)}</h1><p class="landing-description">${esc(copy.description)}</p></header>
 <div class="page-width landing-beginner"><p id="home-beginner-title${suffix}">${esc(copy.beginner.title)}</p><nav class="home-primary-actions" aria-labelledby="home-beginner-title${suffix}"><a data-home-beginner="web" href="${esc(copy.beginner.web.href)}">${esc(copy.beginner.web.label)}</a><a data-home-beginner="pdf" href="${esc(copy.beginner.pdf.href)}" type="application/pdf">${esc(copy.beginner.pdf.label)}</a></nav></div>
 <div class="page-width landing-purpose">${['why','connections','ai'].map(key=>`<p data-home-purpose="${key}">${esc(copy.introduction[key])}</p>`).join('')}</div>
 ${homeSearchPage({compact:true,staticMode})}
 <p class="page-width landing-ways">${esc(copy.introduction.ways)}</p>
 <nav class="page-width home-entrypoints" aria-label="${lang==='ja'?'3つの入口':'Three ways to begin'}"><ul class="home-entry-grid">${copy.entries.map(entry=>`<li><a class="home-entry" data-home-entry="${esc(entry.id)}" href="${esc(entry.href)}"><h2>${esc(entry.title)}</h2><p>${esc(entry.description)}</p><span class="home-entry-arrow" aria-hidden="true">→</span></a></li>`).join('')}</ul></nav>
 <section class="page-width home-reference-links home-kit-entry" aria-labelledby="home-kit-title${suffix}"><h2 id="home-kit-title${suffix}">${esc(copy.agent_kit.title)}</h2><p>${esc(copy.agent_kit.description)}</p><p><a href="${esc(copy.agent_kit.href)}">${esc(copy.agent_kit.label)}</a></p></section>
 <aside class="page-width home-reference-links" aria-labelledby="home-reference-title${suffix}"><h2 id="home-reference-title${suffix}">${lang==='ja'?'教科書・参考文献を探す':'Find textbooks and references'}</h2><p><a href="/numerical-methods-atlas/${lang}/read/textbooks/">${lang==='ja'?'教科書案内':'Textbook guide'}</a><a href="/numerical-methods-atlas/${lang}/read/references/">${lang==='ja'?'参考文献一覧':'Reference list'}</a></p></aside>
 ${renderHomeBrowse(lang,{headingId:'home-browse-title'+suffix})}
 <div class="page-width landing-feedback"><p>${esc(copy.introduction.feedback)}</p></div>
 ${copy.contact?`<p class="page-width home-reference-links"><span>${esc(copy.contact.label)}</span><a href="${esc(copy.contact.href)}">${esc(copy.contact.email)}</a></p>`:''}
 </div>`;
}
export function wireHomeOverview({rewriteLinks=html=>html}={}){
 const root=document.getElementById('home-overview');if(!root)return;
 wireHomeSearch();
}
