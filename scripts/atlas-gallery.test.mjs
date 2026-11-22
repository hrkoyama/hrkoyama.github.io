import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {galleryMatches} from '../atlas-gallery.mjs';
const root = new URL('../', import.meta.url);
const bytes = p => readFileSync(new URL(p, root));
const read = p => bytes(p).toString();
const json = p => JSON.parse(read(p));
const digest = p => createHash('sha256').update(bytes(p)).digest('hex');
const inventory = json('numerical-methods-atlas/test-cases/index.json');
const gallery = json('numerical-methods-atlas/gallery/index.json');
const html = read('numerical-methods-atlas/gallery/index.html');

test('the visual index covers the exact atlas-wide inventory with one card per language and working image-to-entry or reading links', () => {
  assert.deepEqual(gallery.items.map(x => x.id), inventory.problems.map(x => x.id));
  assert.equal(gallery.counts.test_problems, inventory.counts.test_problems);
  assert.equal(new Set(gallery.items.map(x => x.id)).size, gallery.items.length);
  assert.equal((html.match(/class="gallery-tile"/g) || []).length, 2 * gallery.items.length);
  for (const x of gallery.items) {
    assert.equal(digest(x.image.slice(1)), x.image_sha256, x.id);
    assert.equal(x.visual_input.id, x.id);
    assert.ok(x.caption.ja && x.caption.en);
    for (const lang of ['ja', 'en']) {
      const tile = html.split(`id="${x.id}-${lang}"`)[1].split('</li>')[0];
      const target = x.execution_entry?.url[lang] || x.supplemental_execution_entries?.[0]?.url[lang] || x.reading[lang];
      assert.ok(tile.includes(`class="gallery-image-link" href="${target}"`), x.id);
      assert.ok(tile.includes(`href="${x.reading[lang]}"`), `${x.id}: reading remains available`);
      assert.ok(tile.includes(`src="${x.image}"`));
      assert.ok(tile.includes('loading="lazy"'));
      const path = new URL(x.reading[lang]).pathname.slice(1) + 'index.html';
      assert.ok(read(path).includes('<main'));
    }
  }
  assert.ok(html.includes('data-gallery-group="all" aria-pressed="true"'));
});

test('scientific inputs and additional checks are receipted and the nine former code-only problems now have saved results', () => {
  for (const [path, hash] of Object.entries(gallery.source_sha256)) assert.equal(digest(path), hash, path);
  const calculations = json('numerical-methods-atlas/gallery/calculations.json');
  const verification = json('numerical-methods-atlas/gallery/verification.json');
  const computed = gallery.items.filter(x => x.source_kind === 'computed-preview');
  assert.deepEqual(Object.keys(calculations.cases).sort(), computed.map(x => x.id).sort());
  assert.equal(computed.length, 9);
  assert.equal(verification.errors + verification.failures, 0);
  assert.equal(verification.passed, verification.tests);
  for (const x of computed) {
    assert.equal(x.availability, 'saved-output');
    assert.ok(x.evidence.some(e => e.json_pointer === '/cases/' + x.id));
    const c = calculations.cases[x.id];
    assert.ok(c.inputs && c.checks && c.plot);
    assert.ok(!JSON.stringify(c).includes('null'), x.id + ': no nonfinite numeric data');
  }
  assert.equal(inventory.counts.saved_test_problems, inventory.problems.length);
  assert.equal(inventory.counts.code_test_problems, 0);
});

test('the quartic visual comes from the new frozen comparison while the harmonic BAOAB visual stays intact', () => {
  const base='code/validated-examples/2026-11-22/thermostats/';
  const cases=json(base+'cases.json');
  const manifest=json('numerical-methods-atlas/gallery/preview-manifest.json');
  const quartic=gallery.items.find(x=>x.id==='thermostatted-quartic');
  const metadata=cases.find(x=>x.id==='csvr-langevin-quartic');
  assert.equal(gallery.items.length,81);
  assert.equal(quartic.image,'/'+base+'results/csvr-langevin-quartic.png');
  assert.equal(quartic.image_sha256,digest(base+'results/csvr-langevin-quartic.png'));
  assert.deepEqual(quartic.caption,metadata.summary);
  assert.equal(quartic.source_kind,'existing-figure');
  assert.deepEqual(quartic.supplemental_execution_entries.map(x=>x.id),['csvr-langevin-quartic']);
  const harmonic=gallery.items.find(x=>x.id==='langevin-harmonic');
  assert.equal(harmonic.image,'/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png');
  assert.equal(harmonic.image_sha256,'0b199f45202724a444c1195b31cae227b9599d50bc92d6c793a93a90f2ff1c14');
  assert.ok(harmonic.caption.en.includes('BAOAB'));
  assert.deepEqual(harmonic.supplemental_execution_entries.map(x=>x.id),['langevin-harmonic','csvr-langevin-harmonic']);
  assert.equal(manifest.calculations_sha256,'d98cd75e1c58177bfc716e8b68d6bfba1358d5135ac8e2ee0989eb3df77942a6');
  for(const name of ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json','results/csvr-langevin-quartic.png'])assert.equal(manifest.source_sha256[base+name],digest(base+name));
  assert.equal(manifest.source_sha256['catalog/atlas-depth-expansion.json'],digest('catalog/atlas-depth-expansion.json'));
  assert.ok(!gallery.items.some(x=>x.id==='csvr-kinetic-kernel'));
});

test('filters combine domains with normalized multilingual AND searches and handle empty results', () => {
  const sample = {group: 'elliptic', search: 'Poisson–Robin 境界値 ＰＯＩＳＳＯＮ'};
  assert.ok(galleryMatches(sample, 'all', ''));
  assert.ok(galleryMatches(sample, 'elliptic', 'Ｐｏｉｓｓｏｎ robin'));
  assert.ok(galleryMatches(sample, 'all', '境界値'));
  assert.ok(!galleryMatches(sample, 'gravity', 'Poisson'));
  assert.ok(!galleryMatches(sample, 'all', 'Poisson wave'));
  assert.ok(galleryMatches(sample, 'all', 'Poisson-Robin'));
  for (const group of inventory.groups) {
    const visible = gallery.items.filter(x => galleryMatches({group: x.group, search: Object.values(x.name).join(' ')}, group.id, ''));
    assert.equal(visible.length, inventory.counts.groups[group.id]);
  }
});

test('homepage, discovery and old gallery navigation lead to the complete visual index while original tools remain reachable', () => {
  const app = read('numerical-methods-atlas/app.js');
  assert.ok(app.includes("if(type==='gallery'){location.replace('/numerical-methods-atlas/gallery/?lang='+currentLanguage());return;}"));
  assert.ok(app.includes('figures:gallery'));
  assert.equal(app.split('figures:gallery').length - 1, 1);
  assert.ok(html.includes('#/figures'));
  assert.ok(read('numerical-methods-atlas/atlas-purpose.js').includes('/numerical-methods-atlas/gallery/?lang='));
  assert.ok(json('search/index.json').documents.some(x => x.url === '/numerical-methods-atlas/gallery/'));
  assert.ok(json('numerical-methods-atlas/home-search-index.json').entries.some(x => x.id === 'visual-test-index'));
  assert.ok(read('llms.txt').includes('Atlas-wide visual test index'));
});
