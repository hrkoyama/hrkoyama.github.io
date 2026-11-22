(() => {
  'use strict';
  const key = 'hrkoyama.home.language';
  const supported = value => value === 'ja' || value === 'en';
  const requested = new URL(location.href).searchParams.get('lang');
  let saved;
  try { saved = localStorage.getItem(key); } catch {}
  const initial = supported(requested) ? requested : supported(saved) ? saved : 'ja';
  let activeLanguage = initial;
  const atlasSearchScope=()=>location.pathname.startsWith('/numerical-methods-atlas/') || new URLSearchParams(location.search).get('scope')==='atlas';
  function languageURL(language) {
    const alternate = document.body.dataset.contentLanguage && document.querySelector(`link[rel="alternate"][hreflang="${language}"]`);
    const destination = alternate ? new URL(alternate.href) : null;
    const url = destination ? new URL(destination.pathname + destination.search, location.origin) : new URL(location.href);
    url.searchParams.set('lang', language);
    url.hash = location.hash;
    if (!destination && document.body.dataset.siteLanguageAnchors === 'suffix') {
      let id;
      try { id = decodeURIComponent(location.hash.slice(1)); } catch { id = ''; }
      const counterpart = id.replace(/-(ja|en)$/, '-' + language);
      if (counterpart !== id && document.getElementById(counterpart)) url.hash = counterpart;
    }
    return url;
  }
  function apply(language) {
    if (!supported(language)) return;
    activeLanguage = language;
    try { localStorage.setItem(key, language); } catch {}
    if (!document.body.dataset.contentLanguage) document.documentElement.lang = language;
    document.querySelectorAll('.site-chrome').forEach(element => { element.lang = language; });
    document.querySelectorAll('[data-ui-ja][data-ui-en]').forEach(element => {
      element.textContent = language === 'en' ? element.dataset.uiEn : element.dataset.uiJa;
    });
    document.querySelectorAll('[data-site-language]').forEach(element => { element.hidden = element.dataset.siteLanguage !== language; });
    document.querySelectorAll('[data-site-search-input]').forEach(field => {
      const label=atlasSearchScope()?(language==='en'?'Search the atlas':'アトラスを検索'):(language === 'en' ? 'Search this site' : 'サイト内検索');
      field.placeholder = label;
      field.setAttribute('aria-label',label);
    });
    const title = document.querySelector('[data-page-title-ja][data-page-title-en]');
    if (title) document.title = language === 'en' ? title.dataset.pageTitleEn : title.dataset.pageTitleJa;
    const description = document.querySelector('meta[name="description"][data-description-ja]');
    if (description) description.content = language === 'en' ? description.dataset.descriptionEn : description.dataset.descriptionJa;
    for (const property of ['og:title', 'og:description']) {
      const meta = document.querySelector(`meta[property="${property}"]`);
      if (meta) meta.content = property === 'og:title' ? document.title : description?.content || meta.content;
    }
    document.querySelectorAll('a[href]').forEach(link => {
      if (link.hasAttribute('data-site-lang')) {
        link.href = languageURL(link.dataset.siteLang).href;
        if (link.dataset.siteLang === language) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current');
        return;
      }
      const raw = link.getAttribute('href');
      if (!raw || raw.startsWith('#') || link.hasAttribute('download')) return;
      const url = new URL(raw, location.href);
      if (url.origin !== location.origin || !(/\/$/.test(url.pathname) || /\.html$/.test(url.pathname))) return;
      url.searchParams.set('lang', supported(link.hreflang) ? link.hreflang : language); link.href = url.href;
      if(url.pathname==='/search/'){url.searchParams.set('scope',atlasSearchScope()?'atlas':'all');link.href=url.href;}
    });
  }
  apply(initial);
  // Resolve links at click time too: readers and charts can change the current fragment after load.
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link || link.hasAttribute('download')) return;
    if (link.hasAttribute('data-site-lang')) {
      link.href = languageURL(link.dataset.siteLang).href;
      return;
    }
    const raw = link.getAttribute('href');
    if (!raw || raw.startsWith('#')) return;
    const url = new URL(raw, location.href);
    if (url.origin === location.origin && (/\/$/.test(url.pathname) || /\.html$/.test(url.pathname))) {
      url.searchParams.set('lang', supported(link.hreflang) ? link.hreflang : activeLanguage);
      link.href = url.href;
    }
  }, true);
  // Search terms travel only in the URL fragment; the host never receives them.
  document.addEventListener('submit', event => {
    const form = event.target.closest('[data-site-search-form]');
    if (!form) return;
    event.preventDefault();
    const input = form.querySelector('[data-site-search-input]');
    const query = input.value.trim().slice(0, 200);
    const destination = new URL('/search/', location.origin);
    destination.searchParams.set('lang', activeLanguage);
    const scope=document.querySelector('#search-scope')?.value || (atlasSearchScope()?'atlas':'all');
    destination.searchParams.set('scope',scope==='atlas'?'atlas':'all');
    if (query) destination.hash = new URLSearchParams({ q: query }).toString();
    if (location.pathname === '/search/') {
      if (location.href !== destination.href) history.pushState(null, '', destination.href);
      document.dispatchEvent(new CustomEvent('site-search-query'));
    } else location.assign(destination.href);
  });
  // Existing bilingual archives own their content; their language controls also update the shared navigation.
  document.addEventListener('archive-language-change', event => apply(event.detail));
  document.addEventListener('site-search-query',()=>apply(activeLanguage));
  addEventListener('popstate',()=>apply(activeLanguage));
})();
