import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync, readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {homeOverviewPage} from '../numerical-methods-atlas/home-overview.js';

const root = new URL('../', import.meta.url), origin = 'https://hrkoyama.github.io';
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const decode = value => value.replaceAll('&amp;', '&').replaceAll('&quot;', '"').replaceAll('&#39;', "'").replaceAll('&#x27;', "'").replaceAll('&lt;', '<').replaceAll('&gt;', '>');
const text = html => decode(html.replace(/<[^>]+>/g, '')).trim();
const attrs = tag => Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match => [match[1], decode(match[2])]));
const ids = html => [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);

function links(html) {
  const stack = [], result = [], voids = new Set(['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']);
  for (const match of html.matchAll(/<!--[\s\S]*?-->|<\/?([a-z][\w:-]*)\b[^>]*>/gi)) {
    if (!match[1]) continue;
    const tag = match[0], name = match[1].toLowerCase();
    if (tag.startsWith('</')) {
      const index = stack.findLastIndex(parent => parent.name === name);
      if (index >= 0) stack.splice(index);
      continue;
    }
    const element = {name,...attrs(tag),hidden:/(?:^|\s)hidden(?:\s|=|\/?>)/.test(tag)};
    if (name === 'a' && element.href) {
      const end = html.indexOf('</a>', match.index + tag.length);
      result.push({...element,text:text(html.slice(match.index + tag.length,end)),parents:[...stack]});
    }
    if (!voids.has(name) && !tag.endsWith('/>')) stack.push(element);
  }
  return result;
}

function destination(href) {
  const url = new URL(href, origin);
  assert.equal(url.origin, origin);
  assert.ok(existsSync(new URL(url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':''), root)), href);
  return url;
}

function resourceLinksAreVisible(html, lang, where) {
  for (const [chapter,label] of [['textbooks',/教科書|textbook/i],['references',/文献|reference/i]]) {
    const found = links(html).filter(link => new URL(link.href, origin).pathname === `/numerical-methods-atlas/${lang}/read/${chapter}/`);
    assert.ok(found.length, `${where}: ${chapter} has a direct real-edition link`);
    assert.ok(found.some(link => ![...link.parents,link].some(element => element.name === 'details' || element.hidden || element['aria-hidden'] === 'true')),
      `${where}: ${chapter} is available without opening details or running JavaScript`);
    for (const link of found) {
      destination(link.href);
      assert.match(link.text, label);
    }
  }
}

test('compact reading navigation runs after the chapter directory and before search indexing', () => {
  const refresh = JSON.parse(read('catalog/site-build-pipeline.json')).stages.map(stage=>stage.script);
  const navigation = refresh.indexOf('scripts/build-atlas-reading-navigation.py');
  assert.ok(navigation > refresh.indexOf('scripts/build-atlas-reading-index.py'));
  assert.ok(navigation < refresh.indexOf('scripts/build-atlas-search.py'));
});

test('every original chapter uses two compact navigation groups with current state only on the actual resource page', () => {
  for (const lang of ['ja','en']) {
    const content = json(`numerical-methods-atlas/content.${lang}.json`);
    const labels = lang === 'ja' ? ['学ぶ・調べる','教科書・文献'] : ['Learn and look up','Books and references'];
    const checked = [];
    for (const chapter of Object.keys(content)) {
      const html = read(`numerical-methods-atlas/${lang}/read/${chapter}/index.html`);
      if (!html.includes('src="/numerical-methods-atlas/reading.js"')) continue;
      checked.push(chapter);
      const sidebars = [...html.matchAll(/<aside\b[^>]*class="[^"]*\breading-nav\b[^"]*"[^>]*>([\s\S]*?)<\/aside>/g)];
      assert.equal(sidebars.length,1,lang+'/'+chapter+' has one compact reading navigation');
      const sidebar = sidebars[0][1];
      assert.doesNotMatch(sidebar,/各章へ|Go to chapters/i);
      const groups = [...sidebar.matchAll(/<nav\b([^>]*\bdata-reading-navigation-group="[^"]+"[^>]*)>([\s\S]*?)<\/nav>/g)];
      assert.deepEqual(groups.map(group => attrs(group[1])['data-reading-navigation-group']),['learn','resources']);
      assert.deepEqual(groups.map(group => attrs(group[1])['aria-label']),labels);
      assert.deepEqual(groups.map(group => text(group[2].match(/<h2\b[^>]*>([\s\S]*?)<\/h2>/)?.[1] || '')),labels);
      const expected = [
        [`/numerical-methods-atlas/${lang}/read/`,'/numerical-methods-atlas/methods/'],
        [`/numerical-methods-atlas/${lang}/read/textbooks/`,`/numerical-methods-atlas/${lang}/read/references/`]
      ];
      assert.equal(links(sidebar).length,4,'the former flat algorithm list is replaced, rather than appended to');
      for (const [index,group] of groups.entries()) {
        const entries = links(group[2]);
        assert.deepEqual(entries.map(link => destination(link.href).pathname),expected[index]);
        assert.ok(entries.every(link => ![...link.parents,link].some(element => element.name === 'details' || element.hidden)));
      }
      const active = links(sidebar).filter(link => link['aria-current'] === 'page');
      assert.deepEqual(active.map(link => new URL(link.href,origin).pathname),
        ['textbooks','references'].includes(chapter) ? [`/numerical-methods-atlas/${lang}/read/${chapter}/`] : [],
        'a regular algorithm chapter does not mark a learning index or a resource as its current page');
    }
    assert.ok(['textbooks','references','stability'].every(chapter => checked.includes(chapter)), 'the original reading template is exercised for resources and an algorithm');
  }
});

test('navigation changes preserve textbooks and stability articles, anchors and local contents', () => {
  for (const lang of ['ja','en']) {
    const content = json(`numerical-methods-atlas/content.${lang}.json`);
    for (const chapter of ['textbooks','stability']) {
      const html = read(`numerical-methods-atlas/${lang}/read/${chapter}/index.html`);
      const article = html.match(/<article\b[^>]*>([\s\S]*?)<\/article>/)?.[1];
      assert.ok(article);
      assert.equal(text(article), text(content[chapter].html), `${lang}/${chapter}: the source article remains intact`);
      assert.deepEqual(ids(article), ids(content[chapter].html), `${lang}/${chapter}: all existing article anchors survive`);
      const toc = html.match(/<aside\b[^>]*class="chapter-toc"[^>]*>([\s\S]*?)<\/aside>/)?.[1];
      assert.ok(toc);
      assert.deepEqual(links(toc).map(link => link.href), content[chapter].headings.filter(heading => heading.level === 2).map(heading => '#'+heading.id));
      const canonical = [...html.matchAll(/<link\b[^>]*>/g)].map(match => attrs(match[0])).find(link => link.rel === 'canonical');
      assert.equal(canonical?.href, `${origin}/numerical-methods-atlas/${lang}/read/${chapter}/`);
      assert.ok(ids(html).includes('main'), 'the skip-to-content target is retained');
    }
  }
});

test('textbooks and references are labeled as learning resources in both editions', () => {
  for (const lang of ['ja','en']) for (const chapter of ['textbooks','references']) {
    const html = read(`numerical-methods-atlas/${lang}/read/${chapter}/index.html`);
    const topline = html.match(/<div class="chapter-topline">([\s\S]*?)<\/div>/)?.[1];
    assert.ok(topline);
    assert.equal(text(topline.match(/<span\b[^>]*>([\s\S]*?)<\/span>/)?.[1] || ''),lang === 'ja' ? '学習資料' : 'LEARNING RESOURCES');
  }
});

test('both home renderings and the published fallback visibly expose textbooks and references while retaining three entrances', () => {
  const messages = json('numerical-methods-atlas/locales/messages.json'), coverage = json('numerical-methods-atlas/coverage.json');
  const rendered = JSON.parse(execFileSync(process.execPath, ['scripts/render-atlas-landing.mjs'], {cwd:fileURLToPath(root),encoding:'utf8'}));
  const fallback = read('numerical-methods-atlas/index.html').match(/<!-- atlas-intro-fallback -->([\s\S]*?)<!-- \/atlas-intro-fallback -->/)?.[1];
  assert.ok(fallback);
  for (const lang of ['ja','en']) {
    configureLocale(messages,lang);
    const dynamic = homeOverviewPage(coverage,'foundations');
    for (const [mode,html] of [['client',dynamic],['static',rendered[lang]]]) {
      resourceLinksAreVisible(html,lang,lang+' '+mode+' home');
      assert.deepEqual([...html.matchAll(/\bdata-home-entry="([^"]+)"/g)].map(match => match[1]), ['goals','try','read']);
      const resources = html.match(/<aside\b[^>]*class="[^"]*\bhome-reference-links\b[^"]*"[^>]*>([\s\S]*?)<\/aside>/)?.[1];
      assert.ok(resources, 'resources have a named home section');
      assert.match(text(resources),lang === 'ja' ? /教科書・参考文献を探す/ : /Find textbooks and references/);
      resourceLinksAreVisible(resources,lang,lang+' '+mode+' named resource section');
      assert.ok(html.indexOf('home-reference-links') > html.indexOf('home-entrypoints'),'the search and three entrances retain their priority');
    }
    assert.equal((dynamic.match(/<form\b[^>]*\brole="search"/g)||[]).length,1);
    resourceLinksAreVisible(fallback,lang,lang+' published home fallback');
  }
});

test('the systematic-reading page exposes both resource destinations outside collapsed catalogues', () => {
  const html = read('numerical-methods-atlas/explore/index.html');
  const record = json('numerical-methods-atlas/explore/index.json'), markdown = read('numerical-methods-atlas/explore/index.md');
  const sections = [...html.matchAll(/<section\b([^>]*class="[^"]*\bstudy-references\b[^"]*"[^>]*)>([\s\S]*?)<\/section>/g)];
  assert.equal(sections.length,2,'one visible resource section per language');
  for (const lang of ['ja','en']) {
    resourceLinksAreVisible(html,lang,lang+' explore');
    const section = sections.find(section => attrs(section[1])['aria-labelledby'] === 'study-references-title-'+lang);
    assert.ok(section);
    assert.match(text(section[2]),lang === 'ja' ? /教科書・参考文献/ : /Textbooks and references/);
    resourceLinksAreVisible(section[2],lang,lang+' named explore resource section');
    for (const chapter of ['textbooks','references']) {
      const route = `/numerical-methods-atlas/${lang}/read/${chapter}/`;
      assert.equal(record.learning_resources[lang][chapter],route);
      assert.ok(markdown.includes(origin+route),'Markdown retains the same learning-resource destination');
    }
  }
});
