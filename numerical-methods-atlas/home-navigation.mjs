import {homeAreas} from './home-overview-data.js?v=16e8220e0bbb';
import {homeNavigationData} from './atlas-home-data.js?v=c4da2d83fbfd';

/** Preserve existing home bookmarks after moving detailed navigation. */
export function resolveHomeLegacyURL(href, language='en') {
 const url=new URL(href), raw=url.hash.slice(1), [path,query='']=raw.split('?');
 const options=new URLSearchParams(query);
 let lang=['ja','en'].includes(url.searchParams.get('lang'))?url.searchParams.get('lang'):language==='ja'?'ja':'en';
 const oldMap=path.match(/^atlas-map(?:-(ja|en))?$/);
 const isHome=!path||path==='/'||path==='home'||path==='/home';
 const area=options.get('area')||url.searchParams.get('area');
 const selected=homeAreas.find(row=>row.id===area);
 if(oldMap || isHome&&(selected||options.get('section')==='atlas-map')) {
  if(oldMap?.[1]&&!url.searchParams.has('lang'))lang=oldMap[1];
  return '/numerical-methods-atlas/explore/?lang='+lang+'#'+(selected?'atlas-area-'+selected.id+'-'+lang:'atlas-map-'+lang);
 }
 if(!isHome)return null;
 const domain=homeNavigationData.goalDomains.includes(url.searchParams.get('goal-domain'))?url.searchParams.get('goal-domain'):'all';
 const availability=['run','code','reading','planned'].includes(url.searchParams.get('goal-availability'))?url.searchParams.get('goal-availability'):'all';
 if(domain==='all'&&availability==='all')return null;
 return '/numerical-methods-atlas/start/?'+new URLSearchParams({lang,'goal-domain':domain,'goal-availability':availability}).toString();
}
