import {wireGoalFilters} from './goal-filters.mjs?v=4b109b47d93c';
import {atlasPurpose,atlasMetrics,atlasExamples,atlasGoalStart} from './atlas-purpose.js?v=dfb5071428b4';
import {homeSearchPage,wireHomeSearch} from './home-search.js?v=d661d07809d9';
import {t,currentLanguage} from './i18n.js';
import {homeAreas,homeCopy,homePaths,homeReadingLanguages} from './home-overview-data.js?v=e1228a79f331';
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

export function homeOverviewPage(coverage,selected){
 const area=resolveHomeArea(selected),c=coverage.counts,lang=currentLanguage();
 return `<div class="home-overview" id="home-overview" data-area="${area.id}" data-localize="false">
 ${atlasGoalStart()}
 <section class="page-width home-scope-summary" aria-label="${lang==='ja'?'現在の収録範囲':'Current coverage'}">${atlasMetrics()}</section>
 ${atlasPurpose()}
 ${homeSearchPage()}
 ${atlasExamples()}

 ${renderHomeMap(area.id,lang)}
 <section class="page-width guided" aria-labelledby="home-start-title"><h2 id="home-start-title">${text('start-title')}</h2><p class="guided-intro">${text('start-description')}</p><div class="guided-list">${homePaths.map(path=>`<article class="guided-route"><p class="eyebrow">${esc(t(path.tag))}</p><h3>${esc(t(path.title))}</h3><p>${esc(t(path.description))}</p><ol>${path.links.map(([route,key])=>`<li>${link(route,key)}</li>`).join('')}</ol></article>`).join('')}</div></section>
 <section class="page-width evidence"><div class="evidence-inner"><div><p class="eyebrow">KEEP THE EVIDENCE CLOSE</p><h2>${text('evidence-title')}</h2><p>${text('evidence-description',{chapters:c.reading_chapters,sources:c.references,biology:c.biological_entries})}</p></div><div class="evidence-links">${link('/coverage',homeCopy.inventory)}${link('/gallery',homeCopy.gallery)}${link('/glossary',homeCopy.glossary)}</div></div></section>
 <aside class="page-width future"><p>${text('future')} ${link('/read/roadmap?section=planned-quantum-chemistry-and-dft',homeCopy.roadmap)}</p></aside>
 </div>`;
}
export function wireHomeOverview({rewriteLinks=html=>html}={}){
 const root=document.getElementById('home-overview');if(!root)return;
 wireHomeSearch();wireGoalFilters(root);
 for(const button of root.querySelectorAll('[data-home-area]'))button.addEventListener('click',()=>{
  const area=resolveHomeArea(button.dataset.homeArea);root.dataset.area=area.id;
  history.replaceState(null,'',homeAreaURL(location.href,area.id));
  root.querySelector('#home-domain-detail').innerHTML=rewriteLinks(homeAreaDetail(area.id));
  root.querySelectorAll('[data-home-area]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  root.querySelector('.home-selection-status').textContent=t(homeCopy.selected,{area:t(area.name)});
  if(matchMedia('(max-width:700px)').matches)root.querySelector('#home-domain-detail').scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});
 });
}
