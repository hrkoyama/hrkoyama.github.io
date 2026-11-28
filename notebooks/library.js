(() => {
  'use strict';
  const books = window.NOTEBOOKS.notebooks;
  const $ = id => document.getElementById(id);
  const groupNames = {'kyoto-u': ["京都大学理学部", "Faculty of Science, Kyoto University"], 'u-tokyo': ["東京大学大学院理学系研究科天文学専攻", "Department of Astronomy, Graduate School of Science, The University of Tokyo"]};
  let group = 'all';
  const countPages = items => items.reduce((n, book) => n + book.frames.length, 0);
  function english() {
    const selected = document.querySelector('[data-site-lang][aria-current="page"]');
    const requested = selected?.dataset.siteLang || new URL(location.href).searchParams.get('lang');
    if (requested === 'ja' || requested === 'en') return requested === 'en';
    try { return localStorage.getItem('hrkoyama.home.language') === 'en'; } catch { return false; }
  }
  function wording(element, ja, en) {
    element.dataset.uiJa = ja;
    element.dataset.uiEn = en;
    element.textContent = english() ? en : ja;
    return element;
  }
  function label(tag, ja, en, className) {
    const element = wording(document.createElement(tag), ja, en);
    if (className) element.className = className;
    return element;
  }
  function university(book) {
    return groupNames[book.group] || [book.group, book.group];
  }
  function sourceDetails(book) {
    const details = document.createElement('details');
    details.className = 'original-info';
    details.append(label('summary', '原本情報', 'Original record'));
    const list = document.createElement('dl');
    for (const [ja, en, value] of [
      ['ノートID', 'Notebook ID', book.id.toUpperCase()],
      ['元ファイル名', 'Original filename', book.source.split('/').pop()],
      ['保存元', 'Original location', book.source],
      ['整理用見出し', 'Archive title', book.display_title]
    ]) {
      const term = label('dt', ja, en);
      const detail = document.createElement('dd');
      detail.textContent = value;
      list.append(term, detail);
    }
    details.append(list);
    return details;
  }
  function render() {
    $('book-total').textContent = String(books.length);
    $('page-total').textContent = countPages(books).toLocaleString(english() ? 'en-US' : 'ja-JP');
    $('search').placeholder = english() ? 'Subject, instructor, year or original filename' : '科目・講師名・年・元ファイル名';
    const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, '');
    const terms = $('search').value.normalize('NFKC').trim().split(/\s+/).filter(Boolean).map(normalize);
    const shown = books.filter(book => (group === 'all' || book.group === group) &&
      terms.every(term => normalize(`${book.display_title} ${book.source} ${book.id} ${book.lecture_title || ''} ${book.lecturer || ''} ${book.lecture_year || ''} ${university(book).join(' ')} ${(book.related_materials || []).map(material => `${material.title} ${material.creator || ''}`).join(' ')}`).includes(term)));
    wording($('result-count'), `${shown.length} 冊 / ${countPages(shown).toLocaleString('ja-JP')} ページ`, `${shown.length} notebooks / ${countPages(shown).toLocaleString('en-US')} pages`);
    const grid = $('library-grid');
    grid.replaceChildren();
    for (const book of shown) {
      const card = document.createElement('article');
      card.className = 'notebook-card';
      const open = document.createElement('a');
      open.className = 'notebook-open';
      open.href = `notebook.html?id=${encodeURIComponent(book.id)}`;
      const cover = document.createElement('div');
      cover.className = 'cover';
      const image = document.createElement('img');
      image.src = book.frames[0].thumb;
      image.alt = '';
      image.loading = 'lazy';
      image.width = 290;
      image.height = 406;
      cover.append(image);
      const copy = document.createElement('div');
      copy.className = 'card-copy';
      const names = university(book);
      const school = label('p', names[0], names[1], 'card-school');
      const title = document.createElement('h2');
      title.textContent = book.lecture_title || book.display_title;
      if (!book.lecture_title) title.append(label('span', '整理用の見出し', 'Archive title', 'card-title-note'));
      const pages = label('p', `${book.frames.length} ページ`, `${book.frames.length} pages`, 'card-pages');
      const instructorJa = book.lecturer || '講師未確認';
      const instructorEn = book.lecturer || 'Instructor unconfirmed';
      const provisional = book.lecture_year_status ? book.lecture_year_status === 'provisional' : book.metadata_status === 'from_original';
      const yearJa = book.lecture_year ? `${book.lecture_year}年${provisional ? '（仮）' : ''}` : '年未確認';
      const yearEn = book.lecture_year ? `${book.lecture_year}${provisional ? ' (provisional)' : ''}` : 'Year unconfirmed';
      const meta = label('p', `${instructorJa} / ${yearJa}`, `${instructorEn} / ${yearEn}`, 'card-meta');
      const action = label('span', 'ノートを読む', 'Read this notebook', 'card-action');
      copy.append(school, title, pages, meta, action);
      open.append(cover, copy);
      card.append(open, sourceDetails(book));
      grid.append(card);
    }
    if (!shown.length) grid.append(label('p', '一致するノートがありません。検索語を変えてください。', 'No notebooks match. Try another search term.', 'empty-results'));
    document.querySelectorAll('[data-group]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.group === group)));
  }
  document.querySelectorAll('[data-group]').forEach(button => button.addEventListener('click', () => { group = button.dataset.group; render(); }));
  $('search').addEventListener('input', render);
  document.addEventListener('archive-language-change', render);
  render();
})();
