import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {normalizeMethodSearch, methodMatches, wireMethodMaps} from '../atlas-methods.mjs';

const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');
const catalog = JSON.parse(read('catalog/atlas-methods.json'));
const published = JSON.parse(read('numerical-methods-atlas/methods/index.json'));
const html = read('numerical-methods-atlas/methods/index.html');
const storageKey = 'hrkoyama.atlas.methodFilters.v1';
const statuses = ['all', 'educational-example', 'reading-only', 'planned'];
const expectedCounts = {'educational-example': 100, 'reading-only': 16, planned: 29};
const byId = new Map(catalog.methods.map(method => [method.id, method]));

const decode = value => value.replace(/&(?:amp|lt|gt|quot|#39|#x[\da-f]+|#\d+);/gi, entity => {
  const named = {'&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'"};
  if (entity in named) return named[entity];
  return String.fromCodePoint(parseInt(entity.slice(entity[2].toLowerCase() === 'x' ? 3 : 2, -1), entity[2].toLowerCase() === 'x' ? 16 : 10));
});
function attributes(source) {
  const result = {};
  for (const match of source.matchAll(/([a-zA-Z_:][-a-zA-Z0-9_:.]*)(?:\s*=\s*"([^"]*)")?/g)) result[match[1]] = decode(match[2] || '');
  return result;
}
const starts = [...html.matchAll(/<section\b([^>]*\bdata-method-map\b[^>]*)>/g)];
const maps = starts.map((match, index) => {
  const source = html.slice(match.index, starts[index + 1]?.index ?? html.indexOf('</main>', match.index));
  const rows = [...source.matchAll(/<li\b([^>]*\bdata-method-id="([^"]+)"[^>]*)>([\s\S]*?)<\/li>/g)]
    .map(row => ({id: row[2], attributes: attributes(row[1]), source: row[3]}));
  return {lang: attributes(match[1]).lang, attributes: attributes(match[1]), source, rows};
});
const mapFor = lang => {
  const map = maps.find(map => map.lang === lang);
  assert.ok(map, `Generated ${lang} method map is required`);
  return map;
};
const recordsFor = lang => mapFor(lang).rows.map(row => ({
  id: row.id, status: row.attributes['data-status'], search: row.attributes['data-search']
}));

test('all 145 canonical records retain exact IDs, statuses, scientific metadata and bilingual static membership', () => {
  assert.equal(catalog.methods.length, 145);
  assert.deepEqual(Object.fromEntries(Object.keys(expectedCounts).map(status => [status, catalog.methods.filter(method => method.status === status).length])), expectedCounts);
  assert.deepEqual(published.methods.map(method => method.id), catalog.methods.map(method => method.id));
  for (const original of catalog.methods) {
    const record = published.methods.find(method => method.id === original.id);
    for (const [key, value] of Object.entries(original)) {
      if (key === 'reading') {
        assert.deepEqual(record.reading, Object.fromEntries(Object.entries(value).map(([lang, path]) => [lang, 'https://hrkoyama.github.io' + path])));
      } else assert.deepEqual(record[key], value, `${original.id}.${key}`);
    }
  }
  assert.equal(maps.length, 2);
  const labels = {
    'educational-example': {ja: '教育用例・関連コードあり', en: 'Educational example / related code'},
    'reading-only': {ja: '解説あり・専用実装なし', en: 'Reading only / no dedicated implementation'}
  };
  for (const lang of ['ja', 'en']) {
    const map = mapFor(lang);
    assert.equal(map.attributes['data-site-language'], lang);
    const groupedIds = catalog.groups.flatMap(group => catalog.methods.filter(method => method.group.id === group.id).map(method => method.id));
    assert.deepEqual(map.rows.map(row => row.id), groupedIds);
    assert.equal(new Set(map.rows.map(row => row.id)).size, 145);
    for (const row of map.rows) {
      const method = byId.get(row.id);
      assert.equal(row.attributes['data-status'], method.status, row.id);
      assert.ok(!('hidden' in row.attributes), `${row.id}: readable before JavaScript`);
      assert.ok(row.source.includes(`href="${row.id}/`), `${row.id}: original method route`);
      assert.ok(decode(row.source).includes(method.name[lang]), row.id);
      const label = method.status === 'planned'
        ? (Object.keys(method.reading).length
          ? (lang === 'ja' ? '解説あり・実装予定' : 'Reading / implementation planned')
          : (lang === 'ja' ? 'Under construction / 収録予定' : 'Under construction / planned'))
        : labels[method.status][lang];
      assert.ok(decode(row.source).includes(label), `${row.id}: canonical status has the correct display label`);
      assert.ok(row.attributes['data-search'], `${row.id}: bilingual search corpus`);
      assert.ok(methodMatches({status: method.status, search: row.attributes['data-search']}, 'all', label), `${row.id}: displayed state label is searchable`);
    }
    assert.equal((map.source.match(/<details\b[^>]*class="reviewed-methods"/g) || []).length, 1);
    const reviewed = map.source.match(/<details\b[^>]*class="reviewed-methods"[^>]*>([\s\S]*?)<\/details>/)[1];
    assert.equal((reviewed.match(/<li>/g) || []).length, 24);
    assert.ok(!reviewed.includes('data-method-id'), 'The reviewed subset is not counted as duplicate method rows');
  }
});

test('controls progressively enhance the complete readable index with native accessible form controls', () => {
  assert.equal(attributes(html.match(/<body\b([^>]*)>/)[1])['data-site-language-anchors'], 'suffix');
  for (const lang of ['ja', 'en']) {
    const source = mapFor(lang).source;
    const form = source.match(/<form\b([^>]*\bdata-method-controls\b[^>]*)>/);
    assert.ok(form, lang);
    assert.ok('hidden' in attributes(form[1]), `${lang}: keep unusable controls hidden without JavaScript`);
    const input = attributes(source.match(/<input\b([^>]*\bdata-method-query\b[^>]*)>/)[1]);
    assert.equal(input.type, 'search'); assert.equal(input.maxlength, '200');
    assert.ok(input.id && source.includes(`for="${input.id}"`), `${lang}: query has a visible label`);
    const select = source.match(/<select\b([^>]*\bdata-method-status\b[^>]*)>([\s\S]*?)<\/select>/);
    assert.ok(select, lang);
    assert.deepEqual([...select[2].matchAll(/<option\b[^>]*value="([^"]+)"/g)].map(match => match[1]), statuses);
    assert.ok(source.match(/<button\b[^>]*type="button"[^>]*data-method-reset|<button\b[^>]*data-method-reset[^>]*type="button"/));
    const count = attributes(source.match(/<[a-z][a-z\d]*\b([^>]*\bdata-method-count\b[^>]*)>/)[1]);
    assert.equal(count.role, 'status'); assert.equal(count['aria-live'], 'polite'); assert.equal(count['aria-atomic'], 'true');
    assert.ok('hidden' in attributes(source.match(/<[a-z][a-z\d]*\b([^>]*\bdata-method-empty\b[^>]*)>/)[1]));
    assert.equal((source.match(/data-method-group-link=/g) || []).length, catalog.groups.length);
  }
});

test('normalization handles width, case, Unicode dashes and whitespace while preserving Japanese voiced marks', () => {
  assert.equal(normalizeMethodSearch('  ＣＧ\u3000\nCONJUGATE\t勾配 '), normalizeMethodSearch('cg conjugate 勾配'));
  for (const dash of ['‐', '‑', '–', '—', '−']) assert.equal(normalizeMethodSearch('Nose' + dash + 'Hoover'), normalizeMethodSearch('nose-hoover'));
  assert.equal(normalizeMethodSearch('か\u3099'), normalizeMethodSearch('が'));
  assert.notEqual(normalizeMethodSearch('ガ'), normalizeMethodSearch('カ'));
  assert.notEqual(normalizeMethodSearch('ば'), normalizeMethodSearch('は'));
});

test('actual bilingual names, aliases, groups and AND terms combine with exact canonical status membership', () => {
  for (const lang of ['ja', 'en']) {
    const records = recordsFor(lang); const lookup = new Map(records.map(record => [record.id, record]));
    assert.equal(records.filter(record => methodMatches(record)).length, 145);
    for (const [status, count] of Object.entries(expectedCounts)) {
      const actual = records.filter(record => methodMatches(record, status, ''));
      assert.equal(actual.length, count);
      assert.deepEqual(actual.map(record => record.id).sort(), catalog.methods.filter(method => method.status === status).map(method => method.id).sort());
    }
    for (const query of ['CG', 'ｃｇ', '共役勾配', 'Conjugate 勾配']) assert.ok(methodMatches(lookup.get('cg'), 'educational-example', query), `${lang}: ${query}`);
    for (const query of ['Nosé–Hoover', 'Nose-Hoover', 'のせフーバー', 'ノセ・フーバー', 'thermostats 温度制御']) assert.ok(methodMatches(lookup.get('nose-hoover'), 'planned', query), `${lang}: ${query}`);
    assert.ok(methodMatches(lookup.get('velocity-rescaling'), 'planned', 'ベロシティースケーリング'));
    assert.ok(methodMatches(lookup.get('stochastic-velocity-rescaling'), 'planned', 'CSVR'));
    assert.ok(!methodMatches(lookup.get('cg'), 'planned', 'CG'));
    assert.ok(!methodMatches(lookup.get('cg'), 'all', 'CG __absent_term__'));
    assert.ok(!methodMatches(lookup.get('nose-hoover'), 'educational-example', 'Nosé'));
  }
});

// A small DOM fixture exercises the public wiring API and real generated rows.
// It does not reproduce the filtering implementation or derive visibility itself.
class Element {
  constructor(tagName, attrs = {}) {
    this.tagName = tagName.toUpperCase(); this.attributes = {...attrs}; this.dataset = {};
    this.children = []; this.parentElement = null; this.handlers = new Map();
    this.hidden = 'hidden' in attrs; this.value = ''; this.textContent = ''; this.focused = false;
    for (const [name, value] of Object.entries(attrs)) if (name.startsWith('data-')) this.dataset[name.slice(5).replace(/-([a-z])/g, (_, letter) => letter.toUpperCase())] = value;
  }
  append(...nodes) { for (const node of nodes) { this.children.push(node); node.parentElement = this; } }
  getAttribute(name) { return this.attributes[name] ?? null; }
  setAttribute(name, value) { this.attributes[name] = String(value); if (name === 'hidden') this.hidden = true; }
  removeAttribute(name) { delete this.attributes[name]; if (name === 'hidden') this.hidden = false; }
  addEventListener(name, listener) { this.handlers.set(name, [...(this.handlers.get(name) || []), listener]); }
  removeEventListener(name, listener) { this.handlers.set(name, (this.handlers.get(name) || []).filter(fn => fn !== listener)); }
  dispatch(name, extra = {}) {
    const event = {type: name, target: this, currentTarget: this, defaultPrevented: false, isComposing: false,
      preventDefault() { this.defaultPrevented = true; }, ...extra};
    for (const listener of this.handlers.get(name) || []) listener(event);
    return event;
  }
  focus() { this.focused = true; }
  matches(selector) {
    const match = selector.trim().match(/^(?:([a-z]+))?\[([^=\]]+)(?:="([^"]*)")?\]$/i);
    if (!match) return this.tagName.toLowerCase() === selector.trim().toLowerCase();
    return (!match[1] || this.tagName.toLowerCase() === match[1].toLowerCase()) && match[2] in this.attributes && (match[3] === undefined || this.attributes[match[2]] === match[3]);
  }
  querySelectorAll(selector) {
    const found = [];
    for (const child of this.children) {
      if (selector.split(',').some(part => child.matches(part))) found.push(child);
      found.push(...child.querySelectorAll(selector));
    }
    return found;
  }
  querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  set innerHTML(_) { throw new Error('Filter state must never be interpreted as HTML'); }
}

function makeFixture() {
  const document = new Element('document');
  const sections = ['ja', 'en'].map(lang => {
    const section = new Element('section', {'data-method-map': '', 'data-site-language': lang, lang}); section.lang = lang;
    const form = new Element('form', {'data-method-controls': '', hidden: ''});
    const input = new Element('input', {'data-method-query': '', type: 'search', maxlength: '200'}); input.maxLength = 200;
    const select = new Element('select', {'data-method-status': ''}); select.value = 'all'; select.options = statuses.map(value => ({value}));
    const reset = new Element('button', {'data-method-reset': '', type: 'button'});
    const count = new Element('p', {'data-method-count': '', role: 'status', 'aria-live': 'polite', 'aria-atomic': 'true'});
    const empty = new Element('p', {'data-method-empty': '', hidden: ''});
    const groups = []; const links = []; const items = [];
    form.append(input, select, reset); section.append(form, count, empty);
    for (const group of catalog.groups) {
      const node = new Element('section', {'data-method-group': group.id});
      const groupCount = new Element('span', {'data-method-group-count': ''}); node.append(groupCount);
      const link = new Element('a', {'data-method-group-link': group.id, href: '#' + group.id + '-' + lang});
      for (const row of mapFor(lang).rows.filter(row => byId.get(row.id).group.id === group.id)) {
        const item = new Element('li', row.attributes); node.append(item); items.push(item);
      }
      section.append(link, node); groups.push({id: group.id, node, count: groupCount}); links.push(link);
    }
    document.append(section);
    return {section, lang, form, input, select, reset, count, empty, groups, links, items};
  });
  return {document, sections, ja: sections[0], en: sections[1]};
}
function memoryStorage(initial) {
  const values = new Map(initial === undefined ? [] : [[storageKey, initial]]);
  return {values, getItem(key) { return values.get(key) ?? null; }, setItem(key, value) { values.set(key, value); }, removeItem(key) { values.delete(key); }};
}
const visibleIds = section => section.items.filter(item => !item.hidden).map(item => item.dataset.methodId);
const numericWords = text => (text.match(/\d+/g) || []).map(Number);
function assertVisible(fixture, expected) {
  for (const section of fixture.sections) {
    assert.deepEqual([...visibleIds(section)].sort(), [...expected].sort(), section.lang);
    assert.equal(section.empty.hidden, expected.length !== 0);
    assert.ok(numericWords(section.count.textContent).includes(expected.length), section.count.textContent);
    assert.ok(numericWords(section.count.textContent).includes(145), section.count.textContent);
    for (const group of section.groups) {
      const count = expected.filter(id => byId.get(id).group.id === group.id).length;
      assert.equal(group.node.hidden, count === 0, group.id);
      assert.equal(section.links.find(link => link.dataset.methodGroupLink === group.id).hidden, count === 0, group.id);
      assert.ok(numericWords(group.count.textContent).includes(count), group.count.textContent);
    }
  }
}

test('DOM status and query filters synchronize both languages, group counts, jump links and zero/reset states', () => {
  const fixture = makeFixture(); const storage = memoryStorage();
  wireMethodMaps(fixture.document, storage);
  for (const section of fixture.sections) assert.equal(section.form.hidden, false);
  assertVisible(fixture, catalog.methods.map(method => method.id));
  fixture.ja.select.value = 'reading-only'; fixture.ja.select.dispatch('change');
  assert.equal(fixture.en.select.value, 'reading-only');
  assertVisible(fixture, catalog.methods.filter(method => method.status === 'reading-only').map(method => method.id));
  fixture.en.select.value = 'planned'; fixture.en.select.dispatch('change');
  assertVisible(fixture, catalog.methods.filter(method => method.status === 'planned').map(method => method.id));
  fixture.en.input.value = 'のせフーバー'; fixture.en.input.dispatch('input');
  assert.equal(fixture.ja.input.value, 'のせフーバー'); assert.equal(fixture.ja.select.value, 'planned');
  assertVisible(fixture, ['nose-hoover']);
  fixture.ja.input.value = '__no_matching_method__'; fixture.ja.input.dispatch('input');
  assertVisible(fixture, []);
  fixture.en.reset.dispatch('click');
  assertVisible(fixture, catalog.methods.map(method => method.id));
  for (const section of fixture.sections) { assert.equal(section.input.value, ''); assert.equal(section.select.value, 'all'); }
  assert.equal(fixture.en.input.focused, true); assert.equal(fixture.ja.input.focused, false);
  assert.equal(storage.getItem(storageKey), null);
});

test('session restoration retains the shared filter after reloading or changing language, and caps restored query length', () => {
  const storage = memoryStorage(); const first = makeFixture(); wireMethodMaps(first.document, storage);
  first.ja.select.value = 'planned'; first.ja.select.dispatch('change'); first.ja.input.value = 'Nose-Hoover'; first.ja.input.dispatch('input');
  assert.deepEqual(JSON.parse(storage.getItem(storageKey)), {status: 'planned', query: 'Nose-Hoover'});
  const reload = makeFixture(); wireMethodMaps(reload.document, storage);
  assertVisible(reload, ['nose-hoover', 'nose-hoover-chains']);
  for (const section of reload.sections) { assert.equal(section.select.value, 'planned'); assert.equal(section.input.value, 'Nose-Hoover'); }
  const oversized = makeFixture(); wireMethodMaps(oversized.document, memoryStorage(JSON.stringify({status: 'all', query: 'x'.repeat(250)})));
  for (const section of oversized.sections) assert.equal(section.input.value.length, 200);
});

test('denied or corrupt session storage cannot disable filters or reset', () => {
  const invalid = ['{bad json', 'null', '[]', JSON.stringify({status: 'unrecognized', query: ''}), JSON.stringify({status: 'planned', query: 7})];
  for (const raw of invalid) {
    const fixture = makeFixture(); assert.doesNotThrow(() => wireMethodMaps(fixture.document, memoryStorage(raw)));
    assertVisible(fixture, catalog.methods.map(method => method.id));
  }
  const denied = {getItem() { throw new Error('denied'); }, setItem() { throw new Error('denied'); }, removeItem() { throw new Error('denied'); }};
  const fixture = makeFixture(); assert.doesNotThrow(() => wireMethodMaps(fixture.document, denied));
  fixture.ja.select.value = 'educational-example'; assert.doesNotThrow(() => fixture.ja.select.dispatch('change'));
  assertVisible(fixture, catalog.methods.filter(method => method.status === 'educational-example').map(method => method.id));
  assert.doesNotThrow(() => fixture.ja.reset.dispatch('click'));
  assertVisible(fixture, catalog.methods.map(method => method.id)); assert.equal(fixture.ja.input.focused, true);
});

test('IME defers partial matching and form submission never navigates or commits unfinished composition', () => {
  const fixture = makeFixture(); const storage = memoryStorage(); wireMethodMaps(fixture.document, storage);
  fixture.ja.input.dispatch('compositionstart'); fixture.ja.input.value = 'のせ'; fixture.ja.input.dispatch('input', {isComposing: true});
  assertVisible(fixture, catalog.methods.map(method => method.id)); assert.equal(fixture.en.input.value, '');
  assert.equal(fixture.ja.form.dispatch('submit', {isComposing: true}).defaultPrevented, true);
  assertVisible(fixture, catalog.methods.map(method => method.id));
  fixture.ja.input.value = 'のせフーバー'; fixture.ja.input.dispatch('compositionend');
  assertVisible(fixture, ['nose-hoover']); assert.equal(fixture.en.input.value, 'のせフーバー');
  assert.equal(fixture.en.form.dispatch('submit').defaultPrevented, true);
  assertVisible(fixture, ['nose-hoover']);
  fixture.en.input.value = ''; fixture.en.input.dispatch('search');
  assertVisible(fixture, catalog.methods.map(method => method.id));
});

test('query text remains inert, preserves all source rows and never invokes HTML interpretation', () => {
  const fixture = makeFixture(); wireMethodMaps(fixture.document, memoryStorage());
  const payload = '<img src=x onerror="globalThis.__methodFilterInjected=true">';
  fixture.en.input.value = payload; assert.doesNotThrow(() => fixture.en.input.dispatch('input'));
  assertVisible(fixture, []);
  assert.equal(fixture.ja.input.value, payload); assert.equal(fixture.en.input.value, payload);
  assert.equal(globalThis.__methodFilterInjected, undefined);
  for (const section of fixture.sections) assert.equal(section.items.length, 145);
  fixture.ja.reset.dispatch('click'); assertVisible(fixture, catalog.methods.map(method => method.id));
});
