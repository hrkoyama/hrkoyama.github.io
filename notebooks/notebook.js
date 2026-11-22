(() => {
 'use strict';
 const $=id=>document.getElementById(id);
 const groupNames={'kyoto-u':['京都大学','Kyoto University'],'u-tokyo':['東京大学','The University of Tokyo']};
 function english(){
  const selected=document.querySelector('[data-site-lang][aria-current="page"]');
  const requested=selected?.dataset.siteLang||new URL(location.href).searchParams.get('lang');
  if(requested==='ja'||requested==='en')return requested==='en';
  try{return localStorage.getItem('hrkoyama.home.language')==='en';}catch{return false;}
 }
 function wording(element,ja,en){element.dataset.uiJa=ja;element.dataset.uiEn=en;element.textContent=english()?en:ja;return element;}

 const id=new URLSearchParams(location.search).get('id')||'n060';
 const book=window.NOTEBOOKS.notebooks.find(b=>b.id===id);
 if(!book){$('book-main').replaceChildren();const box=document.createElement('section');box.className='book-error';const p=document.createElement('p');p.textContent='このノートは見つかりませんでした。';const a=document.createElement('a');a.href='index.html';a.textContent='書庫一覧へ戻る';box.append(p,a);$('book-main').append(box);return;}
 const frames=book.frames;let current=0;
 document.title=`${book.lecture_title||book.display_title}${book.lecturer?' / '+book.lecturer:''} | 大学ノート`;
 $('book-title').textContent=book.lecture_title||book.display_title;
 wording($('book-id'),`ノートID：${book.id.toUpperCase()}`,`Notebook ID: ${book.id.toUpperCase()}`);
 wording($('book-source'),`保存元：${book.source}`,`Original location: ${book.source}`);
 const university=groupNames[book.group]||[book.group,book.group];wording($('book-group'),university[0],university[1]);
 const provisional=book.lecture_year_status?book.lecture_year_status==='provisional':book.metadata_status==='from_original';
 const yearJa=book.lecture_year?`${book.lecture_year}年${provisional?'（推定）':''}`:'未確認';
 const yearEn=book.lecture_year?`${book.lecture_year}${provisional?' (provisional)':''}`:'unconfirmed';
 wording($('book-status'),`講師名：${book.lecturer||'未確認'}　／　年：${yearJa}`,`Instructor: ${book.lecturer||'unconfirmed'} / Year: ${yearEn}`);
 wording($('book-count'),`収録 ${frames.length} ページ / 原本 ${book.source_pages} ページ`,`${frames.length} published pages / ${book.source_pages} original pages`);
 $('page-count').textContent=String(frames.length).padStart(2,'0');$('book-pdf').href=book.pdf;
 $('lecture-title').textContent=book.lecture_title||'未確認';$('lecturer').textContent=book.lecturer||'未確認';
 wording($('lecture-year'),yearJa,yearEn);
 $('lecture-period').textContent=book.lecture_period||'—';$('lecture-notes').textContent=book.notes||'—';
 $('metadata-explanation').textContent=(book.metadata_sources||[]).some(s=>s.source==='user')?'ノート作成者が確認した情報を反映しています。年を原本や対応資料から仮入力した場合は、その旨を併記しています。':(book.metadata_sources||[]).some(s=>s.source==='related_handout')?'原本と対応する配布資料から情報を確認しています。姓のみの記載や、年の仮入力はその旨を併記しています。':book.metadata_status==='from_original'?'原本の見出し・氏名・日付をもとに整理しています。推定の年は区別して表示しています。':'講義名・講師名・年は、確認できたものから追記します。';
 if(book.lecture_year_basis)$('metadata-explanation').textContent+=' '+book.lecture_year_basis;
 const fieldNames={lecture_title:'講義名',lecturer:'講師名',lecture_year:'年',notes:'追記'};
 for(const s of book.metadata_sources||[]){const li=document.createElement('li');if(s.source==='user'){li.textContent=`${fieldNames[s.field]||s.field}：作成者の確認「${s.value}」`;}else if(s.source==='related_handout'){li.textContent=`${fieldNames[s.field]||s.field}：配布プリント「${s.source_label}」p.${s.source_pages.join('・')}の記載「${s.excerpt}」から確認${s.field==='lecturer'&&(s.name_scope==='surname'||s.status?.includes('姓のみ'))?'（姓のみ）':''}${s.status?.includes('仮入力')?'（仮入力）':''}`;}else{li.textContent=`${fieldNames[s.field]||s.field}：原本 p.${s.source_pages.join('・')}「${s.excerpt}」`;if(s.source_pages.some(p=>!frames.some(f=>f.source_page===p)))li.textContent+='（該当ページは閲覧版未収録）';}$('metadata-sources').append(li);}

 // Only curated, public-safe bibliographic metadata is available here.
 if (book.related_materials?.length) {
  const section=document.createElement('section');section.className='lecture-info related-materials';section.id='related-materials';
  const put=(tag,ja,en)=>{const el=document.createElement(tag);el.dataset.uiJa=ja;el.dataset.uiEn=en;el.textContent=typeof english==='function'&&english()?en:ja;return el;};
  const title=put('h2','対応する資料の目録','Related material records');
  section.append(title,put('p','資料の本文・画像・PDFは非公開です。リンク先では表題・氏名と、自筆ノートとの関係を紹介しています。','The material text, images and PDFs remain private. Links show bibliographic information and its relationship to this notebook.'));
  const list=document.createElement('ul');list.className='material-records';
  for(const material of book.related_materials){
   const item=document.createElement('li');const a=document.createElement('a');a.href=`bibliography.html#${encodeURIComponent(material.id)}`;a.textContent=material.title;
   const relation=document.createElement('p');relation.className='material-relation';relation.textContent=material.label;
   item.append(a,relation);
   if(material.creator){const person=document.createElement('p');person.className='material-creator';person.textContent=`資料の氏名表記：${material.creator}`;item.append(person);}
   list.append(item);
  }
  section.append(list);$('lecture-info').after(section);
 }
 wording($('selection-note'),frames.length===book.source_pages?'原本のページ順で収録しています。':'原本の一部を収録。ページ番号は原本に対応します。',frames.length===book.source_pages?'Pages retain their original order.':'Selected pages only; numbering follows the original notebook.');
 const buttons=[];
 frames.forEach((f,i)=>{
  const li=document.createElement('li');const b=document.createElement('button');b.type='button';
  const im=document.createElement('img');im.src=f.thumb;im.alt='';im.loading='lazy';
  const text=document.createElement('span');const small=document.createElement('small');small.textContent=String(i+1).padStart(2,'0');
  const strong=document.createElement('strong');wording(strong,`原本 p.${f.source_page}`,`Original p.${f.source_page}`);text.append(small,strong);b.append(im,text);
  b.addEventListener('click',()=>choose(i));li.append(b);$('page-list').append(li);buttons.push(b);
  const opt=document.createElement('option');opt.value=String(i);wording(opt,`原本 p.${f.source_page}（${i+1}/${frames.length}）`,`Original p.${f.source_page} (${i+1}/${frames.length})`);$('page-select').append(opt);
 });
 function render(){const f=frames[current];$('page-image').src=f.image;$('page-image').alt=`${book.display_title} 原本${f.source_page}ページ目`;$('image-link').href=f.image;
  $('page-kicker').textContent=`ORIGINAL PAGE ${String(f.source_page).padStart(2,'0')}${f.redacted?' / 個人情報をマスク':''}`;wording($('page-title'),`原本 p.${f.source_page} / 収録 ${current+1} of ${frames.length}`,`Original p.${f.source_page} / published ${current+1} of ${frames.length}`);
  $('page-select').value=String(current);$('prev').disabled=current===0;$('next').disabled=current===frames.length-1;
  buttons.forEach((b,i)=>{if(i===current)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
  wording($('reader-status'),`原本${f.source_page}ページ目を表示中。`,`Showing original page ${f.source_page}.`);
  $('prev').setAttribute('aria-label',english()?'Previous page':'前のページ');$('next').setAttribute('aria-label',english()?'Next page':'次のページ');
 }
 function choose(i,hash=true){if(!Number.isInteger(i)||i<0||i>=frames.length)return;current=i;render();$('image-viewport').scrollTo(0,0);if(hash)history.replaceState(null,'',`#p${frames[current].source_page}`);}
 $('prev').addEventListener('click',()=>choose(current-1));$('next').addEventListener('click',()=>choose(current+1));$('page-select').addEventListener('change',e=>choose(Number(e.target.value)));
 $('zoom').addEventListener('input',e=>{$('image-panels').style.setProperty('--zoom',`${e.target.value}%`);$('zoom-label').textContent=`${e.target.value}%`;});
 $('image-viewport').addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();choose(current+(e.key==='ArrowRight'?1:-1));}});
 function hash(){const match=/^#p(\d+)$/.exec(location.hash);if(match){const i=frames.findIndex(f=>f.source_page===Number(match[1]));if(i>=0)choose(i,false);}}
 window.addEventListener('hashchange',hash);render();hash();
})();
