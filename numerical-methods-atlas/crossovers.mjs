// The complete map is readable before this optional filtering enhancement runs.
const controllers = new WeakMap();
const environments = new WeakMap();
const tokens = value => Array.isArray(value) ? value : String(value || '').split(/\s+/).filter(Boolean);

export const matchCrossover = (mathIds, math = 'all') => math === 'all' || tokens(mathIds).includes(math);
export const crossoverMatches = matchCrossover;

export function crossoverFilterURL(href, math = 'all') {
  const url = new URL(href);
  if (!math || math === 'all') url.searchParams.delete('math');
  else url.searchParams.set('math', math);
  return url;
}

function currentURL(environment) {
  try { return new URL(environment.location.href); } catch { return null; }
}

export function wireCrossovers(scope = document, environment = scope.defaultView || scope.ownerDocument?.defaultView || globalThis) {
  let peers = environments.get(environment);
  if (!peers) {
    peers = new Set();
    environments.set(environment, peers);
    environment.addEventListener?.('popstate', () => { for (const controller of peers) controller.sync(); });
    environment.addEventListener?.('hashchange', () => { for (const controller of peers) controller.revealAnchor(); });
    environment.addEventListener?.('pageshow', event => { if (event.persisted) for (const controller of peers) controller.sync(); });
  }
  const roots = scope.dataset?.crossoverRoot !== undefined ? [scope] : [...scope.querySelectorAll('[data-crossover-root]')];
  return roots.map(root => {
    if (controllers.has(root)) return controllers.get(root);
    const form = root.querySelector('[data-crossover-controls]');
    const select = root.querySelector('[data-crossover-math]');
    const reset = root.querySelector('[data-crossover-reset]');
    const status = root.querySelector('[data-crossover-count]');
    const empty = root.querySelector('[data-crossover-empty]');
    if (!form || !select || !reset || !status || !empty) return null;
    const cards = [...root.querySelectorAll('[data-crossover-card]')];
    const routes = [...root.querySelectorAll('[data-crossover-route]')];
    const items = [...cards, ...routes];
    const allowed = new Set(['all', ...(select.options ? [...select.options].map(option => option.value) : cards.flatMap(card => tokens(card.dataset.mathIds)))]);
    const ja = (root.lang || root.dataset.siteLanguage) === 'ja';
    function anchorRoute() {
      let id;
      try { id = decodeURIComponent(currentURL(environment)?.hash.slice(1) || ''); } catch { return null; }
      if (!id) return null;
      return routes.find(route => route.id === id || [...route.querySelectorAll('[id]')].some(child => child.id === id)) || null;
    }
    function writeURL(math, mode, clearAnchor = false) {
      const current = currentURL(environment);
      if (!current) return;
      const url = crossoverFilterURL(current.href, math);
      if (clearAnchor) url.hash = '';
      if (current.href !== url.href) {
        try { environment.history[mode === 'push' ? 'pushState' : 'replaceState'](environment.history.state, '', url.href); } catch {}
      }
    }
    function render(value, mode = 'replace') {
      const math = allowed.has(value) ? value : 'all';
      select.value = math;
      for (const item of items) item.hidden = !matchCrossover(item.dataset.mathIds, math);
      const visible = new Set(cards.filter(card => !card.hidden).map(card => card.dataset.routeId)).size;
      const total = new Set(cards.map(card => card.dataset.routeId)).size;
      status.textContent = ja ? `${visible} / ${total} の経路を表示` : `Showing ${visible} of ${total} routes`;
      empty.hidden = visible !== 0;
      if (mode) writeURL(math, mode, mode === 'push' && !!anchorRoute()?.hidden);
      return math;
    }
    function revealAnchor() {
      if (anchorRoute()?.hidden) {
        for (const controller of peers) controller.render('all', null);
        render('all', 'replace');
      }
    }
    function sync() {
      render(currentURL(environment)?.searchParams.get('math') || 'all', 'replace');
      revealAnchor();
    }
    function change(value) {
      const math = render(value, 'push');
      for (const controller of peers) if (controller !== api) controller.render(math, null);
    }
    const api = {render, sync, revealAnchor};
    controllers.set(root, api);
    peers.add(api);
    select.addEventListener('change', () => change(select.value));
    reset.addEventListener('click', () => change('all'));
    form.addEventListener('submit', event => event.preventDefault());
    sync();
    form.hidden = false;
    return api;
  }).filter(Boolean);
}

export const wireCrossoverFilters = wireCrossovers;

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => wireCrossovers());
  else wireCrossovers();
}
