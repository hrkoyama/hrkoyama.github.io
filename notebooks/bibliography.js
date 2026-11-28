(() => {
  'use strict';
  const cards = [...document.querySelectorAll('.bibliographic-card')];
  const search = document.getElementById('bibliography-search');
  const kind = document.getElementById('material-kind');
  const preview = document.getElementById('material-preview-filter');
  function english() {
    const selected = document.querySelector('[data-site-lang][aria-current="page"]');
    const requested = selected?.dataset.siteLang || new URL(location.href).searchParams.get('lang');
    if (requested === 'ja' || requested === 'en') return requested === 'en';
    try { return localStorage.getItem('hrkoyama.home.language') === 'en'; } catch { return false; }
  }
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, '');
  function render() {
    search.placeholder = english() ? 'Title, author, instructor or notebook ID' : 'タイトル・著者・講師名・ノートID';
    const terms = search.value.normalize('NFKC').trim().split(/\s+/).filter(Boolean).map(normalize);
    let total = 0;
    for (const card of cards) {
      const show = (kind.value === 'all' || card.dataset.kind === kind.value) &&
        (preview.value === 'all' || card.dataset.preview === preview.value) &&
        terms.every(term => normalize(card.dataset.search).includes(term));
      card.hidden = !show;
      if (show) total++;
    }
    document.getElementById('result-count').textContent = english() ? `${total} / ${cards.length} materials` : `${total} / ${cards.length}項目`;
    document.getElementById('no-results').hidden = total !== 0;
  }
  search.addEventListener('input', render);
  kind.addEventListener('change', render);
  preview.addEventListener('change', render);
  document.addEventListener('archive-language-change', render);
  function reveal() {
    const card = document.getElementById(location.hash.slice(1));
    if (!card?.classList.contains('bibliographic-card')) return;
    search.value = ''; kind.value = 'all'; preview.value = 'all'; render();
    card.scrollIntoView({block:'start'});
  }
  window.addEventListener('hashchange', reveal);
  render(); reveal();
})();
