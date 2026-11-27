// Enhance only the optional details in the comparison indexes.
// Without JavaScript, the generated details remain open and all text is available.
const indexes = [...document.querySelectorAll('main[data-comparison-overview]')];
const solutionFilters = new Map();
const kindKey = 'atlas.comparison.solution-kind';
let savedKind = 'all';
try { savedKind = sessionStorage.getItem(kindKey) || 'all'; } catch {}

for (const main of indexes) {
  for (const section of main.querySelectorAll('[data-site-language]')) {
    const controls = section.querySelector('[data-comparison-solution-controls]');
    if (!controls) continue;
    const select = controls.querySelector('[data-comparison-solution-kind]');
    const count = controls.querySelector('[data-comparison-solution-count]');
    const cards = [...section.querySelectorAll('.solution-card[data-solution-kind]')];
    const allowed = [...select.options].map(option => option.value);
    const apply = value => {
      const kind = allowed.includes(value) ? value : 'all';
      select.value = kind;
      let shown = 0;
      for (const card of cards) {
        card.hidden = kind !== 'all' && card.dataset.solutionKind !== kind;
        if (!card.hidden) shown++;
      }
      count.textContent = section.lang === 'ja'
        ? `${shown} / ${cards.length} 件を表示`
        : `Showing ${shown} of ${cards.length}`;
      return kind;
    };
    solutionFilters.set(section, apply);
    select.addEventListener('change', () => {
      const kind = apply(select.value);
      for (const update of solutionFilters.values()) update(kind);
      try { sessionStorage.setItem(kindKey, kind); } catch {}
    });
    apply(savedKind);
    const originalCounts = section.querySelector('.solutions-summary');
    if (originalCounts) originalCounts.hidden = true;
    controls.hidden = false;
  }
}

function targetFor(hash) {
  if (!hash || hash.startsWith('#/')) return null;
  let id;
  try { id = decodeURIComponent(hash.slice(1)); } catch { return null; }
  const target = document.getElementById(id);
  return target && indexes.some(main => main.contains(target)) ? target : null;
}

function reveal(hash, scroll = false) {
  const target = targetFor(hash);
  if (!target) return;
  if (target.closest('.solution-card[hidden]')) {
    const section = target.closest('[data-site-language]');
    solutionFilters.get(section)?.('all');
    for (const update of solutionFilters.values()) update('all');
    try { sessionStorage.setItem(kindKey, 'all'); } catch {}
  }
  for (let parent = target.parentElement; parent; parent = parent.parentElement) {
    if (parent.tagName === 'DETAILS') parent.open = true;
  }
  if (scroll) requestAnimationFrame(() => {
    if (target.getClientRects().length) target.scrollIntoView({block: 'start'});
  });
}

const initialTarget = targetFor(location.hash);
for (const main of indexes) {
  for (const detail of main.querySelectorAll('details[data-comparison-detail]')) {
    detail.open = Boolean(initialTarget && detail.contains(initialTarget));
  }
  main.dataset.comparisonReady = 'true';
}
reveal(location.hash, true);
addEventListener('hashchange', () => reveal(location.hash, true));
// The fragment may already be current when the reader closes its parent detail.
document.addEventListener('click', event => {
  const link = event.target.closest?.('a[href]');
  if (!link || event.defaultPrevented) return;
  const url = new URL(link.href, location.href);
  if (url.origin === location.origin && url.pathname === location.pathname &&
      url.search === location.search) reveal(url.hash, true);
}, true);
