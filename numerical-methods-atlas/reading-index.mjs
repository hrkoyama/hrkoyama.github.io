export const normalizeReadingQuery=value=>String(value).normalize('NFKC').toLocaleLowerCase().replace(/[‐‑‒–—−_-]/g,' ').replace(/\s+/g,' ').trim();
export function matchesReadingChapter(text,query) {
 const hay=normalizeReadingQuery(text),words=normalizeReadingQuery(query).split(' ').filter(Boolean);
 return words.every(word=>hay.includes(word));
}

export function wireReadingIndex(root=document) {
 const page=root.querySelector('#reading-index')||root;
 const controls=page.querySelector('[data-reading-controls]');
 if(!controls)return;
 const input=page.querySelector('[data-reading-input]'),reset=page.querySelector('[data-reading-reset]');
 const status=page.querySelector('[data-reading-count]'),empty=page.querySelector('[data-reading-empty]');
 const chapters=[...page.querySelectorAll('[data-reading-chapter]')],groups=[...page.querySelectorAll('[data-reading-group]')];
 const links=[...page.querySelectorAll('[data-reading-group-link]')];
 let composing=false;
 function apply() {
  let shown=0;
  for(const chapter of chapters){chapter.hidden=!matchesReadingChapter(chapter.dataset.search,input.value);if(!chapter.hidden)shown++;}
  for(const group of groups){group.hidden=![...group.querySelectorAll('[data-reading-chapter]')].some(row=>!row.hidden);}
  for(const link of links)link.hidden=Boolean(groups.find(group=>group.dataset.readingGroup===link.dataset.readingGroupLink)?.hidden);
  status.textContent=page.dataset.language==='ja'?`${shown} / ${chapters.length}章`:`${shown} of ${chapters.length} chapters`;
  empty.hidden=shown!==0;
 }
 controls.hidden=false;
 controls.addEventListener('submit',event=>{event.preventDefault();apply();});
 input.addEventListener('input',()=>{if(!composing)apply();});
 input.addEventListener('compositionstart',()=>{composing=true;});
 input.addEventListener('compositionend',()=>{composing=false;apply();});
 reset.addEventListener('click',()=>{input.value='';apply();input.focus();});
 apply();
}

if(typeof document!=='undefined')wireReadingIndex();
