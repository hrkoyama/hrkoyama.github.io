import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {homeAreas} from '../numerical-methods-atlas/home-overview-data.js';
import {renderHomeMap, homeOverviewPage} from '../numerical-methods-atlas/home-overview.js';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {atlasPurpose} from '../numerical-methods-atlas/atlas-purpose.js';

const root = new URL('../', import.meta.url);
const origin = 'https://hrkoyama.github.io';
const atlas = origin + '/numerical-methods-atlas/';
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const bytes = path => readFileSync(new URL(path, root));
const digest = path => createHash('sha256').update(bytes(path)).digest('hex');
const messages = json('numerical-methods-atlas/locales/messages.json');
const purpose = json('catalog/atlas-purpose.json');
const methods = json('catalog/atlas-methods.json').methods;
const coverage = json('numerical-methods-atlas/coverage.json');
const examples = json('catalog/atlas-execution-examples.json');
const expectedAreas = ['foundations', 'waves', 'diffusion', 'approximation', 'particles', 'coupled', 'quantum', 'thermostats'];
const shareBase = 'numerical-methods-atlas/share/';
const decode = value => value.replace(/&(?:amp|lt|gt|quot|#\d+|#x[\da-f]+);/gi, entity => {
  const named = {'&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"'};
  if (entity.toLowerCase() in named) return named[entity.toLowerCase()];
  const hexadecimal = entity[2].toLowerCase() === 'x';
  return String.fromCodePoint(parseInt(entity.slice(hexadecimal ? 3 : 2, -1), hexadecimal ? 16 : 10));
});
const text = html => decode(html.replace(/<[^>]*>/g, ' ')).replace(/\s+/g, ' ').trim();
const hrefs = html => [...html.matchAll(/\shref="([^"]+)"/g)].map(match => decode(match[1]));
const ids = html => [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
function attrs(tag) {
  return Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match => [match[1], decode(match[2])]));
}
function meta(html, key) {
  const values = [...html.matchAll(/<meta\b[^>]*>/g)].map(match => attrs(match[0])).filter(tag => (tag.property || tag.name) === key);
  assert.equal(values.length, 1, `one ${key} metadata tag`);
  return values[0];
}
function localTarget(href, base = atlas) {
  const url = new URL(href, base);
  assert.equal(url.origin, origin, href);
  const path = decodeURIComponent(url.pathname).slice(1) + (url.pathname.endsWith('/') ? 'index.html' : '');
  assert.ok(existsSync(new URL(path, root)), href);
  if (url.hash && !url.hash.startsWith('#/')) assert.ok(ids(read(path)).includes(decodeURIComponent(url.hash.slice(1))), `${href}: real static anchor`);
  return url;
}
function staticAreas(source) {
  return [...source.matchAll(/<details\b([^>]*\bdata-static-area="([^"]+)"[^>]*)>([\s\S]*?)<\/details>/g)]
    .map(match => ({id: match[2], tag: attrs(match[1]), html: match[3]}));
}
function formatCopy(value) {
  const counts = {...coverage.counts, execution_examples: examples.examples.length};
  return value.replace(/\{(\w+)\}/g, (_, key) => {
    assert.ok(key in counts, `known copy substitution ${key}`); return String(counts[key]);
  });
}

test('orientation and sharing retain scientific counts and the already-verified execution registry', () => {
  assert.equal(methods.length, 147);
  assert.deepEqual(Object.fromEntries(['educational-example', 'reading-only', 'planned'].map(status => [status, methods.filter(method => method.status === status).length])),
    {'educational-example': 114, 'reading-only': 17, planned: 16});
  assert.equal(json('catalog/atlas-equations.json').equations.length, 46);
  assert.equal(json('numerical-methods-atlas/test-cases/index.json').problems.length, 83);
  assert.equal(examples.examples.length, 22);
  const receipt = json(new URL(examples.verification_receipt).pathname.slice(1));
  assert.equal(receipt.registry_source_mode, 'public-registry'); assert.equal(receipt.passed, true);
  assert.equal(digest('numerical-methods-atlas/code-and-data/examples.json'), receipt.registry_sha256);
  assert.deepEqual(json('numerical-methods-atlas/code-and-data/examples.json').examples, examples.examples);
  assert.ok(methods.filter(method => method.group.id === 'thermostats').every(method => method.status === (['langevin-thermostat', 'stochastic-velocity-rescaling'].includes(method.id) ? 'educational-example' : 'planned')));
});

test('the eight actual areas render in both languages with real reading/execution links and scoped new fields', () => {
  assert.deepEqual(homeAreas.map(area => area.id), expectedAreas);
  for (const lang of ['ja', 'en']) {
    configureLocale(messages, lang);
    const live = renderHomeMap('quantum', lang);
    assert.ok(ids(live).includes('atlas-map'));
    assert.deepEqual([...live.matchAll(/\bdata-home-area="([^"]+)"/g)].map(match => match[1]), expectedAreas);
    const source = renderHomeMap('quantum', lang, {staticMode: true});
    const areas = staticAreas(source);
    assert.deepEqual(areas.map(area => area.id), expectedAreas);
    for (const area of areas) {
      assert.equal(area.tag.id, `atlas-area-${area.id}-${lang}`);
      assert.ok(!area.html.includes('home-map.'), `${lang}/${area.id}: translated labels`);
    }
    const directory = [...source.matchAll(/<a\b([^>]*\bdata-home-reading="([^"]+)"[^>]*)>/g)];
    assert.deepEqual([...new Set(directory.map(match => match[2]))], expectedAreas);
    for (const match of directory) {
      const url = localTarget(attrs(match[1]).href);
      assert.ok(!url.hash.startsWith('#/'), `${match[2]}: readable without the SPA`);
    }
    for (const href of hrefs(source)) {
      const url = localTarget(href);
      if (url.pathname.includes('/code-and-data/examples/')) {
        assert.equal(url.hash, '', 'execution entries use stable paths');
        if (url.searchParams.has('lang')) assert.equal(url.searchParams.get('lang'), lang);
      }
    }
    const quantum = text(areas.find(area => area.id === 'quantum').html);
    assert.match(quantum, /He/);
    assert.match(quantum, lang === 'ja' ? /水素/ : /hydrogen/i);
    assert.match(quantum, lang === 'ja' ? /球対称|1s/ : /spherical|1s/i);
    assert.match(quantum, lang === 'ja' ? /交換のみ/ : /exchange.only/i);
    const quantumEntries = hrefs(areas.find(area => area.id === 'quantum').html)
      .map(href => new URL(href, atlas).pathname.match(/\/code-and-data\/examples\/([^/]+)\//)?.[1]).filter(Boolean);
    assert.deepEqual([...new Set(quantumEntries)].sort(), ['h2-rhf', 'helium-ground-state', 'hydrogenic-atoms', 'periodic-he-dft', 'periodic-he-forces']);
    const thermostatHTML = areas.find(area => area.id === 'thermostats').html;
    const thermostat = text(thermostatHTML);
    assert.match(thermostat, lang === 'ja' ? /予定|未実装|専用実装なし/ : /planned|not implemented|no dedicated/i);
    assert.ok(!homeAreas.find(area => area.id === 'thermostats').groups.flat().some(entry => entry.kind === 'execution'));
    assert.doesNotMatch(thermostatHTML, /\bdata-home-kind="execution"/);
  }
});

test('the read-only map renderer and detailed explore page retain all eight fields with unique language-specific IDs', () => {
  const rendered = JSON.parse(execFileSync(process.execPath, ['scripts/render-atlas-home-map.mjs'], {cwd: fileURLToPath(root), encoding: 'utf8', maxBuffer: 2_000_000}));
  assert.deepEqual(Object.keys(rendered).sort(), ['en', 'ja']);
  const homepage = read('numerical-methods-atlas/index.html');
  const fallback = read('numerical-methods-atlas/explore/index.html');
  assert.equal(staticAreas(fallback).length, 16);
  for (const page of [homepage, fallback]) {
    const allIds = ids(page); assert.equal(allIds.length, new Set(allIds).size);
  }
  assert.equal(staticAreas(homepage).length, 0, 'the detailed map has moved off the landing page');
  for (const lang of ['ja', 'en']) {
    assert.deepEqual(staticAreas(rendered[lang]).map(area => area.id), expectedAreas);
    assert.ok(ids(fallback).includes('atlas-map-' + lang));
    for (const area of expectedAreas) assert.ok(ids(fallback).includes(`atlas-area-${area}-${lang}`));
  }
});

test('present-tense purpose, scope and introductory metadata derive from the same bilingual copy', () => {
  const homepage = read('numerical-methods-atlas/index.html');
  const explore = read('numerical-methods-atlas/explore/index.html');
  const description = meta(homepage, 'description');
  const descriptions = read('numerical-methods-atlas/app.js').match(/^const atlasIntroDescriptions = (.*);$/m);
  assert.ok(descriptions, 'runtime descriptions are an explicit localized data object');
  assert.deepEqual(JSON.parse(descriptions[1]), Object.fromEntries(['ja', 'en'].map(lang => [lang, purpose[lang].meta_description])));
  for (const lang of ['ja', 'en']) {
    configureLocale(messages, lang);
    const source = atlasPurpose();
    for (const paragraph of purpose[lang].paragraphs) {
      assert.ok(text(source).includes(paragraph), `${lang}: runtime purpose`);
      assert.ok(text(explore).includes(paragraph), `${lang}: detailed static purpose`);
    }
    assert.ok(text(source).includes(purpose[lang].status_note));
    assert.ok(source.includes('<details>') && source.includes('<summary>'));
    assert.equal(description['data-description-' + lang], purpose[lang].meta_description);
    const runtime = homeOverviewPage(coverage, 'quantum');
    assert.ok(hrefs(runtime).some(href => new URL(href, atlas).pathname === '/numerical-methods-atlas/explore/'), `${lang}: direct detailed reading entrance`);
    assert.ok(hrefs(runtime).some(href => new URL(href, atlas).pathname === '/numerical-methods-atlas/code-and-data/examples/'));
    assert.ok(hrefs(explore).some(href => new URL(href, atlas).pathname === '/numerical-methods-atlas/share/'), `${lang}: sharing remains discoverable on the detail page`);
  }
  assert.doesNotMatch(homepage, /An English atlas/i);
});

test('sharing provides real 1200 by 630 PNG/SVG artwork and matching localized social metadata', () => {
  const catalog = json('catalog/atlas-sharing.json');
  const published = json(shareBase + 'sharing.json');
  const build = json(shareBase + 'build.json');
  const expectedCounts = {...coverage.counts, method_records: 147, educational_examples: 114, reading_only: 17, planned: 16, execution_examples: 22};
  for (const [key, value] of Object.entries(expectedCounts)) assert.equal(published.counts[key], value, key);
  assert.deepEqual(published.sources, build.sources);
  for (const [path, sha256] of Object.entries(build.sources)) assert.equal(digest(path), sha256, path);
  assert.equal(build.builder_sha256, digest('scripts/build-atlas-sharing.py'));
  assert.deepEqual([catalog.image.width, catalog.image.height], [1200, 630]);
  for (const lang of ['ja', 'en']) {
    const imagePath = shareBase + `atlas-intro-${lang}.png`;
    const png = bytes(imagePath);
    assert.equal(digest(imagePath), build.images[lang].png_sha256);
    assert.equal(digest(shareBase + `atlas-intro-${lang}.svg`), build.images[lang].svg_sha256);
    assert.deepEqual([...png.subarray(0, 8)], [137, 80, 78, 71, 13, 10, 26, 10]);
    assert.equal(png.toString('ascii', 12, 16), 'IHDR');
    assert.deepEqual([png.readUInt32BE(16), png.readUInt32BE(20)], [1200, 630]);
    const svg = read(shareBase + `atlas-intro-${lang}.svg`);
    const dimensions = attrs(svg.match(/<svg\b[^>]*>/)[0]);
    assert.equal(dimensions.width, '1200'); assert.equal(dimensions.height, '630');
    assert.ok(text(svg).includes(formatCopy(catalog.copy[lang].image.title)));
    const fixed = read(shareBase + lang + '/index.html');
    assert.match(fixed, new RegExp(`<html\\s+lang="${lang}"`));
    assert.equal(new URL(meta(fixed, 'og:image').content, origin).pathname.slice(1), imagePath);
    assert.equal(meta(fixed, 'twitter:card').content, 'summary_large_image');
    assert.equal(meta(fixed, 'twitter:image').content, meta(fixed, 'og:image').content);
    assert.equal(meta(fixed, 'og:image:width').content, '1200'); assert.equal(meta(fixed, 'og:image:height').content, '630');
    assert.ok(hrefs(fixed).some(href => new URL(href, origin).pathname === '/rights/'));
  }
  const homepage = read('numerical-methods-atlas/index.html');
  const image = meta(homepage, 'og:image').content;
  assert.match(image, /\/share\/atlas-intro-(?:ja|en)\.png$/);
  localTarget(image);
  assert.equal(meta(homepage, 'twitter:image').content, image);
  assert.equal(meta(homepage, 'twitter:card').content, 'summary_large_image');
});

test('bilingual sharing text uses scoped examples and confines sharing terms to the new introduction materials', () => {
  const catalog = json('catalog/atlas-sharing.json');
  const page = read(shareBase + 'index.html');
  for (const lang of ['ja', 'en']) {
    const short = read(shareBase + `atlas-intro-short-${lang}.txt`).trim();
    const paragraph = read(shareBase + `atlas-intro-paragraph-${lang}.txt`).trim();
    assert.ok(short.startsWith(formatCopy(catalog.copy[lang].short) + '\n'));
    assert.ok(paragraph.startsWith(formatCopy(catalog.copy[lang].paragraph) + '\n'));
    assert.ok(short.includes(catalog.atlas_url) && paragraph.includes(catalog.atlas_url));
    const published = json(shareBase + 'sharing.json');
    assert.equal(published.introductions[lang].short, formatCopy(catalog.copy[lang].short));
    assert.equal(published.introductions[lang].paragraph, formatCopy(catalog.copy[lang].paragraph));
    assert.equal(published.sharing_terms[lang], catalog.sharing_terms[lang]);
    assert.match(short, /22/);
    assert.match(short, lang === 'ja' ? /代表|例|問題/ : /representative|examples|problems/i);
    assert.match(short + paragraph, lang === 'ja' ? /固定入力/ : /fixed inputs/i);
    assert.match(paragraph, lang === 'ja' ? /参照|照合|許容誤差/ : /reference|comparisons|tolerances/i);
    assert.ok(text(page).includes(catalog.sharing_terms[lang]));
    const bundle = read(shareBase + `atlas-intro-${lang}.txt`);
    assert.ok(bundle.includes(catalog.atlas_url));
    assert.ok(/https:\/\/hrkoyama.github.io\/rights\//.test(bundle));
    assert.match(catalog.sharing_terms[lang], lang === 'ja' ? /リンク|サイト名|出典/ : /link|site name|credit|attribution/i);
    assert.match(catalog.sharing_terms[lang], lang === 'ja' ? /この(?:ページ|素材)|紹介/ : /these|specific|introduction/i);
    assert.match(catalog.sharing_terms[lang], lang === 'ja' ? /他の|第三者|各資料|既存/ : /other|third.party|existing/i);
  }
});
