import {matchGoals} from './goals-data.mjs?v=0b94e1580a3d';
// Both the atlas and the site search use these identities and availability links.
export const normalizeMethodQuery = value => String(value).normalize('NFKC').toLowerCase()
  .replace(/[‐‑‒–—−-]/g,' ').replace(/\s+/g,' ').trim();
const intents = new Set(['法','方式','スキーム','手法','解説','コード','テスト','検証','実行','入力','論文','実装','method','methods','scheme','schemes','code','test','tests','validation','run','implementation','explanation','paper']);
export function tokenIncludes(text, term) {
  if (!term) return false;
  if (!/^[a-z0-9]+$/.test(term)) return text.includes(term);
  const escaped = term.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  return new RegExp('(^|[^a-z0-9])'+escaped+'(?=$|[^a-z0-9])','u').test(text);
}
export function methodIdentities(method) {
  return [...new Set([method.id, ...Object.values(method.name || {}), ...(method.aliases || [])]
    .filter(value => typeof value === 'string' && value.trim()).map(normalizeMethodQuery))];
}
export function findMethods(methods, query, language='ja') {
  const goals=matchGoals(query);
  if(goals.length){
    const ids=[...new Set(goals.flatMap(goal=>goal.methods))];
    return ids.flatMap(id=>{const method=methods.find(m=>m.id===id);if(!method)return [];
      return [{id,kind:'method',title:method.name[language] || method.name.en,locale:language,method,exactMethod:false,score:9000,purposeScope:goals.filter(g=>g.methods.includes(id)).map(g=>g.scope[language]).join(' ')}];});
  }
  const phrase = normalizeMethodQuery(String(query).slice(0,200));
  if (!phrase) return [];
  const focus = phrase.split(' ').filter(word => !intents.has(word));
  if (!focus.length) return [];
  const focused = focus.join(' ');
  // Strip a Japanese method suffix only when the remaining name is registered.
  const forms = [...new Set([phrase, focused, focused.replace(/(?:法|方式|スキーム)$/u,'').trim()])].filter(Boolean);
  return methods.flatMap(method => {
    const identities = methodIdentities(method);
    const exact = identities.some(name => forms.includes(name));
    const matched = exact || identities.some(name => focus.every(word => tokenIncludes(name,word)));
    if (!matched) return [];
    const locale = method.name?.[language] ? language : 'en';
    const prefix=identities.some(name=>name.startsWith(focused+' '));
    return [{id:method.id, kind:'method', title:method.name?.[locale] || method.id,
      locale, method, exactMethod:exact, score:exact ? 10000 : prefix ? 1200 : 1000}];
  }).sort((a,b) => b.score-a.score || a.id.localeCompare(b.id));
}

const origin = 'https://hrkoyama.github.io';
function publicPath(value) {
  if (typeof value !== 'string' || !value) return null;
  try {
    const url = new URL(value,origin);
    if (url.origin !== origin || url.username || url.password || url.pathname.startsWith('//')) return null;
    return url.pathname+url.search+url.hash;
  } catch {return null;}
}
const labels = {
  ja:{method:'手法',reading:'解説',english:'解説（英語）',code:'関連コード',tests:'関連テスト',run:'入力・実行・判定',details:'適用条件・文献',files:'すべての関連ファイル',missing:'コード・テストは未公開',noReading:'専用解説は未公開',scope:'コードとテストは関連する教育用例です。手法の全変種の検証を意味しません。',
    status:{'educational-example':'教育用例あり','reading-only':'解説のみ',planned:'収録予定'}},
  en:{method:'Method',reading:'Explanation',english:'Explanation (English)',code:'Related code',tests:'Related tests',run:'Inputs, run & checks',details:'Conditions & references',files:'All related files',missing:'Code and tests are not published',noReading:'Dedicated explanation is not published',scope:'Related educational code and checks; they do not validate every variant of this method.',
    status:{'educational-example':'Educational example','reading-only':'Reading only',planned:'Planned'}}
};
function ensureStyle() {
  if (document.querySelector('link[data-method-search-style]')) return;
  const link=document.createElement('link');link.rel='stylesheet';link.dataset.methodSearchStyle='';
  link.href=new URL('./methods.css?v=efa8031daab4',import.meta.url).href;document.head.append(link);
}
/** Text nodes and same-site URLs only, including on the atlas's inline results. */
export function appendMethodCard(item,result,language='ja') {
  ensureStyle();
  const m=result.method,c=labels[language] || labels.ja;
  item.classList.add('method-search-card');item.dataset.methodId=m.id;
  const meta=document.createElement('p');meta.className='method-search-meta';
  meta.textContent=[c.method,m.group?.[language],c.status[m.status] || m.status].filter(Boolean).join(' · ');
  const heading=document.createElement('h2');
  const link=(url,text,lang) => {
    const path=publicPath(url);if (!path) return null;
    const a=document.createElement('a'),u=new URL(path,location.origin);
    if (u.pathname.endsWith('/') || u.pathname.endsWith('.html')) u.searchParams.set('lang',lang || language);
    a.href=u.pathname+u.search+u.hash;a.textContent=text;if(lang)a.hreflang=lang;return a;
  };
  const titleLink=link(m.url,m.name?.[language] || m.name?.en || m.id);
  if(titleLink)heading.append(titleLink);else heading.textContent=result.title;
  const otherName=document.createElement('p');otherName.className='method-search-name';
  otherName.textContent=m.name?.[language==='ja'?'en':'ja'] || '';
  const summary=document.createElement('p');summary.className='method-search-summary';summary.textContent=m.summary?.[language] || m.summary?.en || '';
  const actions=document.createElement('nav');actions.className='method-search-actions';
  actions.setAttribute('aria-label',(m.name?.[language] || m.id)+(language==='ja'?'の資料':' resources'));
  const reading=m.reading?.[language] || m.reading?.en;
  const readingLang=m.reading?.[language] ? language : 'en';
  const add=(url,text,lang) => {const a=link(url,text,lang);if(a)actions.append(a);};
  if(reading)add(reading,readingLang!==language?c.english:c.reading,readingLang);
  // Availability is explicit in the catalog; planned records never borrow code.
  const hasCode=m.status==='educational-example';
  const code=hasCode?(m.code_urls || []).filter(publicPath):[];
  const tests=hasCode?(m.test_urls || []).filter(publicPath):[];
  if(code.length)add(code[0],c.code);
  if(tests.length)add(tests[0],c.tests);
  if(hasCode)for(const example of m.execution_examples || [])add(example.guide?.[language] || example.guide?.en,c.run+': '+(example.name?.[language] || example.id));
  add(m.url,c.details);
  item.append(meta,heading);if(otherName.textContent)item.append(otherName);if(summary.textContent)item.append(summary);item.append(actions);
  if(result.purposeScope){const scope=document.createElement('p');scope.className='method-search-note';scope.textContent=result.purposeScope;item.insertBefore(scope,heading);}
  const note=document.createElement('p');note.className='method-search-note';
  note.textContent=code.length || tests.length ? c.scope : c.missing;
  if(!reading)note.textContent+=' · '+c.noReading;
  item.append(note);
  if(code.length>1 || tests.length>1) {
    const details=document.createElement('details'),summary=document.createElement('summary'),list=document.createElement('ul');
    summary.textContent=c.files;details.append(summary,list);
    for(const [title,urls] of [[c.code,code],[c.tests,tests]])for(const url of urls){
      const li=document.createElement('li');const a=link(url,title+': '+new URL(url,origin).pathname.split('/').pop());if(a){li.append(a);list.append(li);}
    }
    item.append(details);
  }
  return item;
}
