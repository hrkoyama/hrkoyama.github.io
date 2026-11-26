import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
const version = createHash('sha256')
  .update(readFileSync(new URL('../site.css', import.meta.url)))
  .update(readFileSync(new URL('../site.js', import.meta.url)))
  .digest('hex').slice(0, 12);
const iconVersion = createHash('sha256')
  .update(readFileSync(new URL('../favicon.svg', import.meta.url)))
  .digest('hex').slice(0, 12);
const text = (ja, en) => `<span data-ui-ja="${ja}" data-ui-en="${en}">${ja} / ${en}</span>`;
export function decorateSite(html, { contentLanguage = '' } = {}) {
  html = html.replace(/<!-- site-head -->[\s\S]*?<!-- \/site-head -->\n?/g, '')
    .replace(/<!-- site-top -->[\s\S]*?<!-- \/site-top -->\n?/g, '')
    .replace(/<!-- site-bottom -->[\s\S]*?<!-- \/site-bottom -->\n?/g, '')
    .replace(/<style id="rights-notice-style">[\s\S]*?<\/style>/g, '')
    .replace(/<footer class="rights-notice"[\s\S]*?<\/footer>/g, '')
    .replace(/<link\b(?=[^>]*\brel=["'](?:shortcut\s+)?icon["'])[^>]*>\s*/gi, '');
  if (contentLanguage) html = html.replace(/<body([^>]*)>/, (_, attributes) => `<body${attributes.replace(/ data-content-language="[^"]*"/, '')} data-content-language="${contentLanguage}">`);
  const canonical = /<link rel="canonical" href="([^"]+)"/.exec(html)?.[1];
  const policyDescriptions = {
    'https://hrkoyama.github.io/hpci-policy/': 'A personal record of two secondments to MEXT and related committee work, with public sources on HPCI, post-K and AI for Science.',
    'https://hrkoyama.github.io/hpci-policy/history.html': 'Committee relationships, computing systems and FY2006–2025 major-program budget observations, with public primary sources.'
  };
  if (policyDescriptions[canonical]) html = html.replace(/<meta name="description" content="([^"]*)"[^>]*>/, (_, ja) => `<meta name="description" content="${ja}" data-description-ja="${ja}" data-description-en="${policyDescriptions[canonical]}">`);
  const alternates = canonical && !contentLanguage && !/rel="alternate"[^>]*hreflang=/.test(html) ? ['ja','en','x-default'].map(lang => `<link rel="alternate" hreflang="${lang}" href="${canonical}${lang === 'x-default' ? '' : '?lang=' + lang}">`).join('\n') + '\n' : '';
  const head = `<!-- site-head -->\n${alternates}<link rel="icon" href="/favicon.svg?v=${iconVersion}" type="image/svg+xml">\n<link rel="stylesheet" href="/site.css?v=${version}">\n<script src="/site.js?v=${version}" defer></script>\n<link rel="describedby" href="/llms.txt">\n<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">\n<!-- /site-head -->\n`;
  const fixedNote = contentLanguage ? `<p class="site-content-note">${text(contentLanguage === 'ja' ? 'このコンテンツの本文は日本語です。' : 'このコンテンツの本文は英語です。', contentLanguage === 'ja' ? 'This content is in Japanese.' : 'This content is in English.')}</p>` : '';
  const top = `<!-- site-top -->\n<div class="site-chrome site-top"><div class="site-inner"><a class="site-brand" href="/">Hiroshi Koyama</a><nav class="site-nav" aria-label="Site navigation"><a href="/">${text('ホーム', 'Home')}</a><a href="/rights/">${text('利用条件・AI方針', 'Rights &amp; AI policy')}</a></nav><nav class="site-languages" aria-label="言語 / Language"><a href="?lang=ja" data-site-lang="ja" lang="ja">日本語</a><a href="?lang=en" data-site-lang="en" lang="en">English</a></nav><form class="site-search" action="/search/" role="search" aria-label="サイト内検索 / Site search" data-site-search-form><input type="search" data-site-search-input aria-label="サイト内検索 / Search this site" placeholder="サイト内検索 / Search this site" maxlength="200" autocomplete="off" enterkeyhint="search"><button type="submit">${text('検索', 'Search')}</button></form>${fixedNote}</div></div>\n<!-- /site-top -->\n`;
  const footer = `<!-- site-bottom -->\n<footer class="site-chrome site-bottom"><div class="site-inner"><div class="site-legal"><p>© 2026 Hiroshi Koyama / 小山 洋</p><p>${text('公開資料のAI検索・要約・出典付き引用を歓迎します。', 'AI search, summaries and source-linked quotation are welcome.')}</p><p>${text('自作コード：MIT。本文・図・画像・PDF・データ・第三者資料は別条件です。', 'Original code: MIT. Text, figures, images, PDFs, data and third-party material have separate terms.')}</p><p class="site-credit">${text('Webサイト制作：ChatGPTとCodexの支援を利用。', 'Website developed with assistance from ChatGPT and Codex.')}</p></div><nav class="site-links" aria-label="Site policies and resources"><a href="/search/">${text('サイト内検索', 'Site search')}</a><a href="/rights/">${text('利用条件・AI方針', 'Rights &amp; AI policy')}</a><a href="/using/">${text('資料の使い方・引用', 'Use &amp; cite')}</a><a data-site-continuity-entry="footer" href="/rights/#site-continuity">${text('保存・継承への協力', 'Help preserve this site')}</a><a href="/llms.txt">${text('AI向け案内', 'AI site guide')}</a><a href="/sitemap.xml">${text('サイトマップ', 'Sitemap')}</a></nav></div></footer>\n<!-- /site-bottom -->\n`;
  return html.replace('</head>', head + '</head>').replace(/(<body[^>]*>)\s*/, '$1\n' + top).replace('</body>', footer + '</body>');
}
