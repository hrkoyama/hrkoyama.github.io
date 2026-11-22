import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {galleryMatches} from '../atlas-gallery.mjs';

const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const discovery = json('catalog/atlas-execution-discovery.json');
const gallery = json('numerical-methods-atlas/gallery/index.json');
const html = read('numerical-methods-atlas/gallery/index.html');
const runnable = new Map(discovery.examples.map(example => [example.problem_id, example]));
const supplemental = new Map(json('catalog/atlas-test-problems.json').problems.filter(x => x.supplemental_examples?.length).map(x => [x.id, x.supplemental_examples]));

test('the shared22 and separate supplements have distinct runnable entrances; all83 retain images and readings', () => {
  const previews = new Map(json('numerical-methods-atlas/gallery/preview-manifest.json').items.map(x => [x.id, x]));
  assert.equal(gallery.items.length, 83);
  assert.equal(runnable.size, 22);
  assert.equal(gallery.counts.runnable_problems, 39);
  assert.equal(gallery.counts.common_runnable_problems, 22);
  assert.equal(gallery.counts.supplemental_runnable_problems, 20);
  assert.equal(gallery.counts.supplemental_case_count, 25);
  assert.equal(gallery.counts.supplemental_release_case_count, 29);
  assert.equal(gallery.items.filter(x => x.runnable).length, 39);
  assert.equal((html.match(/class="gallery-execution-badge"/g) || []).length, 44);
  assert.equal((html.match(/data-supplemental-execution=/g) || []).length, 50);
  for (const item of gallery.items) {
    const example = runnable.get(item.id);
    const extra = supplemental.get(item.id) || [];
    assert.equal(item.runnable, Boolean(example || extra.length), item.id);
    assert.deepEqual(item.supplemental_execution_entries.map(x => x.id), extra.map(x => x.id));
    assert.deepEqual(item.caption, previews.get(item.id).caption, `${item.id}: preserve original caption`);
    assert.equal(item.image, previews.get(item.id).image, `${item.id}: preserve illustration`);
    for (const lang of ['ja', 'en']) {
      const tile = html.split(`id="${item.id}-${lang}"`)[1].split('</li>')[0];
      const primary = tile.match(/<a\b[^>]*class="gallery-image-link"[^>]*href="([^"]+)"/)?.[1];
      assert.ok(primary,item.id+' image retains a direct problem entrance');
      const hub = new URL(primary,'https://hrkoyama.github.io');
      assert.equal(hub.pathname,`/numerical-methods-atlas/problems/${item.id}/`);
      assert.equal(hub.searchParams.get('lang'),lang);
      assert.equal(tile.includes('class="gallery-execution-badge"'), Boolean(example), item.id);
      assert.ok(tile.includes(`data-runnable="${Boolean(example || extra.length)}"`), item.id);
      assert.ok(tile.includes(`href="${item.reading[lang]}"`), `${item.id}: keep reading link`);
      assert.ok(tile.includes(`href="${item.image}"`), `${item.id}: full-size illustration remains available`);
      if (example) {
        const target = `https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/${example.id}/?lang=${lang}`;
        assert.equal(item.execution_entry.url[lang], target);
        const badge = tile.match(/<p class="gallery-execution-badge">([\s\S]*?)<\/p>/)?.[1];
        assert.ok(badge?.includes(`href="${target}"`),item.id+' direct run badge is preserved');
        assert.ok(read(new URL(target).pathname.slice(1) + 'index.html').includes('<main'));
      } else assert.equal(item.execution_entry, null);
      for (const entry of item.supplemental_execution_entries) {
        const original = extra.find(x => x.id === entry.id);
        const url = `https://hrkoyama.github.io${original.url}?lang=${lang}`;
        assert.equal(entry.url[lang], url);
        assert.ok(tile.includes(`data-supplemental-execution="${entry.id}"`));
        assert.ok(tile.includes(`href="${url}"`));
        assert.ok(read(new URL(url).pathname.slice(1) + 'index.html').includes('<main'));
        assert.ok(entry.code_urls.length && entry.test_urls.length);
        const output = json(new URL(entry.results).pathname.slice(1));
        const result = output.cases.find(x => x.id === entry.id);
        assert.equal(result.passed, true);assert.ok(Object.values(result.checks).every(x => x === true));
      }
    }
  }
});

test('runnable filtering combines with domain and normalized bilingual AND searches without hiding any case by default', () => {
  const records = gallery.items.map(item => ({
    group: item.group, runnable: item.runnable,
    search: [item.id, ...Object.values(item.name), ...(runnable.get(item.id)?.keywords || [])].join(' ')
  }));
  assert.equal(records.filter(x => galleryMatches(x, 'all', '')).length, 83);
  assert.equal(records.filter(x => galleryMatches(x, 'all', '', true)).length, 39);
  for (const group of new Set(records.map(x => x.group))) {
    assert.equal(records.filter(x => galleryMatches(x, group, '', true)).length,
      gallery.items.filter(x => x.group === group && x.runnable).length);
  }
  assert.ok(galleryMatches({group: 'time', runnable: 'true', search: 'Stiff–cosine 硬い 余弦'}, 'time', 'ＳＴＩＦＦ-cosine 余弦', true));
  assert.ok(!galleryMatches({group: 'time', runnable: 'false', search: 'Stiff–cosine 硬い 余弦'}, 'time', '余弦', true));
  assert.ok(!galleryMatches({group: 'time', runnable: true, search: 'Stiff–cosine 硬い 余弦'}, 'gravity', '余弦', true));
});

test('native toggle controls announce state and captions distinguish saved illustrations from fixed-input reruns', () => {
  for (const lang of ['ja', 'en']) {
    assert.ok(html.includes(`data-gallery-runnable aria-pressed="false" aria-describedby="gallery-illustration-note-${lang}"`));
    assert.ok(html.includes(`id="gallery-illustration-note-${lang}"`));
  }
  assert.equal((html.match(/<button type="button" data-gallery-runnable/g) || []).length, 2);
  assert.ok(html.includes('実行・検証例あり 39'));
  assert.ok(html.includes('Runnable and validated: 39'));
  assert.ok(html.includes('画像と固定入力の条件は一致するとは限りません'));
  assert.ok(html.includes('these need not match'));
  assert.ok(html.includes('data-gallery-count role="status" aria-live="polite"'));
});

test('toggle, group, search, no-results and reset interactions preserve independent Japanese/English states', async () => {
  const element = (properties = {}) => ({
    ...properties, attributes: {}, handlers: {},
    setAttribute(name, value) { this.attributes[name] = value; },
    addEventListener(name, fn) { this.handlers[name] = fn; },
    focus() { this.focused = true; }
  });
  const makeSection = lang => {
    const input = element({value: ''});
    const buttons = ['all', ...new Set(gallery.items.map(x => x.group))].map(group => element({dataset: {galleryGroup: group}}));
    const tiles = gallery.items.map(item => element({hidden: false, dataset: {
      group: item.group, runnable: String(item.runnable), search: Object.values(item.name).join(' ')
    }}));
    const status = element(); const empty = element({hidden: true});
    const toggle = element(); const reset = element();
    const one = new Map([['input[type="search"]', input], ['[data-gallery-count]', status],
      ['[data-gallery-empty]', empty], ['[data-gallery-runnable]', toggle], ['[data-gallery-reset]', reset]]);
    return {lang, input, buttons, tiles, status, empty, toggle, reset,
      querySelector: selector => one.get(selector),
      querySelectorAll: selector => selector === '[data-gallery-group]' ? buttons : tiles};
  };
  const sections = ['ja', 'en'].map(makeSection);
  const previous = globalThis.document;
  globalThis.document = {querySelectorAll: () => sections};
  try { await import('../atlas-gallery.mjs?discovery-gallery-interactions'); }
  finally {
    if (previous === undefined) delete globalThis.document;
    else globalThis.document = previous;
  }
  const visible = section => section.tiles.filter(tile => !tile.hidden).length;
  const [ja, en] = sections;
  assert.equal(visible(ja), 83); assert.equal(visible(en), 83);
  ja.toggle.handlers.click();
  assert.equal(visible(ja), 39); assert.equal(visible(en), 83);
  assert.equal(ja.toggle.attributes['aria-pressed'], 'true');
  ja.buttons.find(button => button.dataset.galleryGroup === 'gravity').handlers.click();
  assert.equal(visible(ja), gallery.items.filter(x => x.group === 'gravity' && x.runnable).length);
  ja.input.value = '周期'; ja.input.handlers.input();
  assert.equal(visible(ja), gallery.items.filter(x => x.group === 'gravity' && x.runnable && Object.values(x.name).join(' ').includes('周期')).length);
  ja.input.value = '__no_matching_problem__'; ja.input.handlers.input();
  assert.equal(visible(ja), 0); assert.equal(ja.empty.hidden, false);
  assert.ok(ja.status.textContent.includes('0 / 83'));
  ja.reset.handlers.click();
  assert.equal(visible(ja), 83); assert.equal(ja.empty.hidden, true);
  assert.equal(ja.input.value, ''); assert.equal(ja.input.focused, true);
  assert.equal(ja.toggle.attributes['aria-pressed'], 'false');
  assert.equal(ja.buttons[0].attributes['aria-pressed'], 'true');
  assert.equal(visible(en), 83);
  en.toggle.handlers.click();
  assert.equal(visible(en), 39); assert.ok(en.status.textContent.includes('Showing 39 of 83'));
  assert.equal(visible(ja), 83);
});
