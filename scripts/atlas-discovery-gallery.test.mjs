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

test('the 22 runnable problems have image entrances and bilingual badges; all 67 retain their images and readings', () => {
  const previews = new Map(json('numerical-methods-atlas/gallery/preview-manifest.json').items.map(x => [x.id, x]));
  assert.equal(gallery.items.length, 67);
  assert.equal(runnable.size, 22);
  assert.equal(gallery.counts.runnable_problems, 22);
  assert.equal(gallery.items.filter(x => x.runnable).length, 22);
  assert.equal((html.match(/class="gallery-execution-badge"/g) || []).length, 44);
  for (const item of gallery.items) {
    const example = runnable.get(item.id);
    assert.equal(item.runnable, Boolean(example), item.id);
    assert.deepEqual(item.caption, previews.get(item.id).caption, `${item.id}: preserve original caption`);
    assert.equal(item.image, previews.get(item.id).image, `${item.id}: preserve illustration`);
    for (const lang of ['ja', 'en']) {
      const tile = html.split(`id="${item.id}-${lang}"`)[1].split('</li>')[0];
      const target = example
        ? `https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/${example.id}/?lang=${lang}`
        : item.reading[lang];
      assert.ok(tile.includes(`class="gallery-image-link" href="${target}"`), item.id);
      assert.equal(tile.includes('class="gallery-execution-badge"'), Boolean(example), item.id);
      assert.ok(tile.includes(`data-runnable="${Boolean(example)}"`), item.id);
      assert.ok(tile.includes(`href="${item.reading[lang]}"`), `${item.id}: keep reading link`);
      assert.ok(tile.includes(`href="${item.image}"`), `${item.id}: full-size illustration remains available`);
      if (example) {
        assert.equal(item.execution_entry.url[lang], target);
        assert.ok(read(new URL(target).pathname.slice(1) + 'index.html').includes('<main'));
      } else assert.equal(item.execution_entry, null);
    }
  }
});

test('runnable filtering combines with domain and normalized bilingual AND searches without hiding any case by default', () => {
  const records = gallery.items.map(item => ({
    group: item.group, runnable: item.runnable,
    search: [item.id, ...Object.values(item.name), ...(runnable.get(item.id)?.keywords || [])].join(' ')
  }));
  assert.equal(records.filter(x => galleryMatches(x, 'all', '')).length, 67);
  assert.equal(records.filter(x => galleryMatches(x, 'all', '', true)).length, 22);
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
  assert.ok(html.includes('実行・検証例あり 22'));
  assert.ok(html.includes('Runnable and validated: 22'));
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
  assert.equal(visible(ja), 67); assert.equal(visible(en), 67);
  ja.toggle.handlers.click();
  assert.equal(visible(ja), 22); assert.equal(visible(en), 67);
  assert.equal(ja.toggle.attributes['aria-pressed'], 'true');
  ja.buttons.find(button => button.dataset.galleryGroup === 'gravity').handlers.click();
  assert.equal(visible(ja), gallery.items.filter(x => x.group === 'gravity' && x.runnable).length);
  ja.input.value = '周期'; ja.input.handlers.input();
  assert.equal(visible(ja), gallery.items.filter(x => x.group === 'gravity' && x.runnable && Object.values(x.name).join(' ').includes('周期')).length);
  ja.input.value = '__no_matching_problem__'; ja.input.handlers.input();
  assert.equal(visible(ja), 0); assert.equal(ja.empty.hidden, false);
  assert.ok(ja.status.textContent.includes('0 / 67'));
  ja.reset.handlers.click();
  assert.equal(visible(ja), 67); assert.equal(ja.empty.hidden, true);
  assert.equal(ja.input.value, ''); assert.equal(ja.input.focused, true);
  assert.equal(ja.toggle.attributes['aria-pressed'], 'false');
  assert.equal(ja.buttons[0].attributes['aria-pressed'], 'true');
  assert.equal(visible(en), 67);
  en.toggle.handlers.click();
  assert.equal(visible(en), 22); assert.ok(en.status.textContent.includes('Showing 22 of 67'));
  assert.equal(visible(ja), 67);
});
