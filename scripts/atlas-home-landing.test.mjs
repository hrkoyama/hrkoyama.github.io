import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {homeOverviewPage} from '../numerical-methods-atlas/home-overview.js';
import {resolveHomeLegacyURL} from '../numerical-methods-atlas/home-navigation.mjs';

const root = new URL('../', import.meta.url);
const origin = 'https://hrkoyama.github.io';
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const messages = json('numerical-methods-atlas/locales/messages.json');
const coverage = json('numerical-methods-atlas/coverage.json');
const copy = json('catalog/atlas-home.json').landing;
const decode = value => value.replaceAll('&amp;', '&').replaceAll('&quot;', '"').replaceAll('&#39;', "'");
const attributes = tag => Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match => [match[1], decode(match[2])]));
const entries = html => [...html.matchAll(/<a\b[^>]*\bdata-home-entry="[^"]+"[^>]*>[\s\S]*?<\/a>/g)].map(match => ({...attributes(match[0]), html:match[0]}));
const ids = html => [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
function actualDestination(href) {
  const url = new URL(href, origin);
  assert.equal(url.origin, origin);
  const path = url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path, root)), href);
  return url;
}

test('the bilingual landing offers exactly one local search and the three requested entrances', () => {
  const expectedPaths = ['/numerical-methods-atlas/start/', '/numerical-methods-atlas/code-and-data/examples/', '/numerical-methods-atlas/explore/'];
  assert.deepEqual(copy.ja.entries.map(entry => entry.title), ['目的から探す','まず計算を試す','体系的に読む']);
  for (const lang of ['ja','en']) {
    configureLocale(messages, lang);
    const html = homeOverviewPage(coverage, 'quantum');
    const choices = entries(html);
    assert.deepEqual(choices.map(entry => entry['data-home-entry']), ['goals','try','read']);
    assert.equal((html.match(/<h1\b/g)||[]).length, 1);
    assert.equal((html.match(/<form\b[^>]*\brole="search"/g)||[]).length, 1);
    assert.equal((html.match(/\bid="home-search-input"/g)||[]).length, 1);
    assert.ok(html.indexOf('home-search-form') < html.indexOf('home-entrypoints'), 'search precedes the three paths');
    assert.ok(!/<input\b[^>]*\bname="(?:q|query|search)"/.test(html), 'keywords are not submitted to a server');
    assert.ok(!/home-goal-choice|data-home-area=|data-static-area=|data-goal-controls|atlas-metrics|atlas-crossover-teaser|atlas-way-grid|data-featured-example=/.test(html), 'detailed inventories do not compete on the landing');
    for (const [index, choice] of choices.entries()) {
      assert.ok(choice.html.includes(copy[lang].entries[index].title));
      const url = actualDestination(choice.href);
      assert.equal(url.pathname, expectedPaths[index]);
      assert.equal(url.searchParams.get('lang'), lang);
    }
    const allIds = ids(html); assert.equal(allIds.length, new Set(allIds).size);
  }
});

test('static and client landings keep the same entrances without requiring JavaScript to choose a path', () => {
  const rendered = JSON.parse(execFileSync(process.execPath, ['scripts/render-atlas-landing.mjs'], {cwd:fileURLToPath(root),encoding:'utf8'}));
  const homepage = read('numerical-methods-atlas/index.html');
  const fallback = homepage.match(/<!-- atlas-intro-fallback -->([\s\S]*?)<!-- \/atlas-intro-fallback -->/)?.[1];
  assert.ok(fallback, 'one server-readable landing fallback');
  assert.equal(entries(fallback).length, 6, 'three choices in each language');
  assert.ok(!homepage.includes('atlas-purpose-fallback'), 'the old full directory is not hidden in the homepage');
  assert.ok(!/data-static-area=|data-goal-controls|atlas-metrics|atlas-crossover-teaser/.test(fallback));
  for (const lang of ['ja','en']) {
    const html = rendered[lang], choices = entries(html);
    assert.equal(choices.length, 3);
    const published = entries(fallback).filter(choice => new URL(choice.href, origin).searchParams.get('lang') === lang);
    assert.deepEqual(published.map(choice => [choice['data-home-entry'],choice.href]), choices.map(choice => [choice['data-home-entry'],choice.href]), lang+' static choices match the shared renderer');
    assert.ok(html.includes(`id="home-overview-${lang}"`));
    assert.ok(!html.includes('<form'), 'non-JavaScript search opens the dedicated search page safely');
    const search = html.match(/<a\b[^>]*class="home-search-static"[^>]*>/)?.[0];
    assert.ok(search, lang+' static search destination');
    const searchURL = actualDestination(attributes(search).href);
    assert.equal(searchURL.pathname, '/search/');
    assert.equal(searchURL.searchParams.get('scope'), 'atlas');
    assert.equal(searchURL.searchParams.get('lang'), lang);
    assert.ok(!searchURL.searchParams.has('q'));
    for (const choice of choices) actualDestination(choice.href);
  }
  const allIds = ids(homepage); assert.equal(allIds.length, new Set(allIds).size);
});

test('old area bookmarks and meaningful goal filters still open the intended detailed pages', () => {
  const home = origin+'/numerical-methods-atlas/';
  assert.equal(resolveHomeLegacyURL(home+'?lang=ja&goal-domain=all&goal-availability=all','en'), null, 'the supplied all/all URL remains the concise landing');
  for (const lang of ['ja','en']) {
    const area = resolveHomeLegacyURL(home+`?lang=${lang}#/?area=quantum`, 'en');
    assert.equal(area, `/numerical-methods-atlas/explore/?lang=${lang}#atlas-area-quantum-${lang}`);
    const section = resolveHomeLegacyURL(home+`?lang=${lang}#/?section=atlas-map`, 'en');
    assert.equal(section, `/numerical-methods-atlas/explore/?lang=${lang}#atlas-map-${lang}`);
    for (const href of [area, section]) {
      const target = actualDestination(href);
      assert.ok(read('numerical-methods-atlas/explore/index.html').includes(`id="${target.hash.slice(1)}"`));
    }
    const goal = new URL(resolveHomeLegacyURL(home+`?lang=${lang}&goal-domain=quantum&goal-availability=run`), origin);
    assert.equal(goal.pathname, '/numerical-methods-atlas/start/');
    assert.equal(goal.searchParams.get('lang'), lang);
    assert.equal(goal.searchParams.get('goal-domain'), 'quantum');
    assert.equal(goal.searchParams.get('goal-availability'), 'run');
    assert.equal(resolveHomeLegacyURL(home+`?lang=${lang}#/read/adjoint`), null);
    assert.equal(resolveHomeLegacyURL(home+`?lang=${lang}#/coverage`), null);
    assert.equal(resolveHomeLegacyURL(home+`?lang=${lang}&goal-domain=unknown&goal-availability=invalid`), null);
  }
  assert.equal(resolveHomeLegacyURL(home+'#atlas-map-ja','en'), '/numerical-methods-atlas/explore/?lang=ja#atlas-map-ja');
  assert.equal(resolveHomeLegacyURL(home+'?lang=en#atlas-map-ja','ja'), '/numerical-methods-atlas/explore/?lang=en#atlas-map-en');
});

test('the next pages retain goals, executable choices and every field map with readable chapter links', () => {
  const explore = read('numerical-methods-atlas/explore/index.html');
  const start = read('numerical-methods-atlas/start/index.html');
  const chooser = read('numerical-methods-atlas/code-and-data/examples/index.html');
  const fields = ['foundations','waves','diffusion','approximation','particles','coupled','quantum','thermostats'];
  const goals = json('catalog/atlas-goals.json').goals;
  const examples = json('catalog/atlas-execution-examples.json').examples;
  assert.ok(!explore.includes('home-goal-choice'), 'the full goal selector belongs on its own page');
  assert.ok(!explore.includes('href="#/'), 'standalone reading directory opens interactive exhibits at the atlas root');
  assert.equal((explore.match(/class="guided-route"/g)||[]).length, 6, 'three reading paths in each language');
  for (const lang of ['ja','en']) {
    assert.ok(explore.includes(`data-site-language="${lang}"`));
    for (const field of fields) assert.ok(explore.includes(`id="atlas-area-${field}-${lang}"`), field+'/'+lang);
    assert.ok(explore.includes(`/numerical-methods-atlas/${lang}/read/`), lang+' chapter index');
    assert.ok(explore.includes(`/numerical-methods-atlas/methods/?lang=${lang}`), lang+' method directory');
    for (const goal of goals) assert.ok(start.includes(`id="${goal.id}-${lang}"`));
    for (const example of examples) assert.ok(chooser.includes('/code-and-data/examples/'+example.id+'/?lang='+lang));
  }
});

test('AI-readable registries and Markdown remain linked and preserve their scientific scope fields', () => {
  const llms = read('llms.txt');
  assert.ok(llms.includes('https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json'));
  assert.ok(llms.includes('https://hrkoyama.github.io/guide/packs/numerical.md'));
  assert.ok(llms.includes('index.md'));
  const methods = json('numerical-methods-atlas/methods/index.json').methods;
  const catalog = json('catalog/atlas-methods.json').methods;
  assert.deepEqual(methods.map(method => method.id), catalog.map(method => method.id));
  for (const method of methods) {
    const source = catalog.find(entry => entry.id === method.id);
    assert.equal(method.status, source.status, method.id);
    assert.deepEqual(method.limitations, source.limitations, method.id+' scope');
    assert.ok(Array.isArray(method.code_urls) && Array.isArray(method.test_urls));
    assert.ok(read(`numerical-methods-atlas/methods/${method.id}/index.md`).includes(method.name.en));
  }
  const registry = json('numerical-methods-atlas/code-and-data/examples.json');
  assert.deepEqual(registry.examples, json('catalog/atlas-execution-examples.json').examples);
  assert.ok(read('guide/packs/numerical.md').includes('hrkoyama.github.io/numerical-methods-atlas/'));
});
