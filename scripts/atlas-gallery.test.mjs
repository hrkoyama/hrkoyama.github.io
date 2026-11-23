import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {galleryMatches} from '../atlas-gallery.mjs';
const root = new URL('../', import.meta.url);
const bytes = p => readFileSync(new URL(p, root));
const read = p => bytes(p).toString();
const json = p => JSON.parse(read(p));
const digest = p => createHash('sha256').update(bytes(p)).digest('hex');
const inventory = json('numerical-methods-atlas/test-cases/index.json');
const gallery = json('numerical-methods-atlas/gallery/index.json');
const html = read('numerical-methods-atlas/gallery/index.html');

test('new MHD accuracy and active-cleaning evidence preserve the earlier OT illustration and add only the equilibrium card',()=>{
 const base='code/validated-examples/2026-11-22/mhd-convergence/';
 const cases=json(base+'cases.json');
 const item=gallery.items.find(x=>x.id==='advected-magnetostatic-equilibrium');
 const metadata=cases.find(x=>x.id==='ct-glm-smooth-convergence');
 assert.equal(gallery.items.length,87);assert.equal(gallery.counts.runnable_problems,47);
 assert.equal(gallery.counts.supplemental_release_case_count,49);
 assert.equal(item.image,'/'+base+'results/ct-glm-smooth-convergence.png');
 assert.equal(item.image_sha256,digest(base+'results/ct-glm-smooth-convergence.png'));
 assert.deepEqual(item.caption,metadata.summary);
 assert.deepEqual(item.supplemental_execution_entries.map(x=>x.id),['ct-glm-smooth-convergence']);
 const ot=gallery.items.find(x=>x.id==='orszag-tang');
 assert.equal(ot.image,'/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp');
 assert.equal(ot.image_sha256,'38c260ae5d3a5031e733b365eb00c6ea04c9182a059a317bd1735e0c3dc0e6af');
 assert.deepEqual(ot.supplemental_execution_entries.map(x=>x.id),['ct-glm-independent','ct-glm-ot-convergence']);
 assert.ok(!gallery.items.some(x=>x.id==='ct-glm-constraint-control'));
 const manifest=json('numerical-methods-atlas/gallery/preview-manifest.json');
 const addedSources=['particle-transport'].flatMap(group=>{
  const base='code/validated-examples/2026-11-22/'+group+'/';
  const cases=json(base+'cases.json');
  return ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json',...cases.map(x=>'results/'+x.id+'.png')].map(name=>base+name);
 });
 const nohBase='code/validated-examples/2026-11-23-r3/noh/';
 const nohSources=['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json','results/noh-shock.png','results/noh-shock-preview.png'].map(name=>nohBase+name);
 const currentNohSources=nohSources.map(path=>path.replace('2026-11-23-r3/noh/','2026-11-23-r5/noh/'));
 assert.equal(Object.keys(manifest.source_sha256).length,127+new Set(addedSources).size+nohSources.length+currentNohSources.length+49+7+7);
 for(const path of nohSources)assert.equal(manifest.source_sha256[path],digest(path),path);
 for(const path of currentNohSources)assert.equal(manifest.source_sha256[path],digest(path),path);
 for(const path of addedSources)assert.equal(manifest.source_sha256[path],digest(path),path);
 // Splitting adds a supplementary run link, while this preview keeps the
 // historical onset image. Its full release provenance belongs to the gallery
 // index resolver rather than to the unchanged preview-image receipt.
 const splittingBase='code/validated-examples/2026-11-22/splitting/';
 for(const name of ['cases.json','source-manifest.json','verification.json','results/result.json','atlas-splitting-2026-11-22.zip']){
  const path=splittingBase+name;assert.equal(gallery.source_sha256[path],digest(path),path);
 }
 const splittingManifest=json(splittingBase+'source-manifest.json');
 for(const name of ['inputs.json','results/reaction-diffusion-splitting.png'])assert.equal(splittingManifest.files[name],digest(splittingBase+name),name);
 for(const name of ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json',...cases.map(x=>'results/'+x.id+'.png')])assert.equal(manifest.source_sha256[base+name],digest(base+name));
});

test('six particle/transport checks retain all five historical images and add only explicitly bound evidence',()=>{
 const base='code/validated-examples/2026-11-22/particle-transport/';
 const cases=json(base+'cases.json');
 const additions={
  'neutral-periodic-charges':['ewald-convergence','spme-convergence'],
  'logarithmic-particles':['fmm-convergence'],
  'cold-plasma-pic':['pic-conservation'],
  'maxwell-collisions':['dsmc-statistics'],
  'absorbing-slab':['radiation-convergence'],
 };
 const oldImages={'neutral-periodic-charges':'ewald','logarithmic-particles':'fmm','cold-plasma-pic':'pic','maxwell-collisions':'dsmc','absorbing-slab':'radiation-transport'};
 const manifest=json('numerical-methods-atlas/gallery/preview-manifest.json');
 for(const [problem,ids] of Object.entries(additions)){
  const item=gallery.items.find(x=>x.id===problem);
  assert.equal(item.image,'/code/validated-examples/2026-11-22/particles/results/'+oldImages[problem]+'.png');
  for(const id of ids){
   const entry=item.supplemental_execution_entries.find(x=>x.id===id);
   assert.ok(entry,problem+' '+id);assert.equal(entry.group,'particle-transport');
   assert.deepEqual(entry.title,cases.find(x=>x.id===id).title);
   assert.ok(entry.download.endsWith('/particle-transport/atlas-particle-transport-2026-11-22.zip'));
  }
 }
 for(const name of ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json',...cases.map(x=>'results/'+x.id+'.png')])assert.equal(manifest.source_sha256[base+name],digest(base+name));
 assert.equal(gallery.counts.supplemental_case_count,44);
 assert.equal(gallery.counts.supplemental_release_case_count,49);
 assert.equal(gallery.counts.runnable_problems,47);
});

test('optional domain buttons and image policies start collapsed while names, reset and current count remain visible', () => {
  const protectedFiles = ['preview-manifest.json','calculations.json','verification.json'].map(name => 'numerical-methods-atlas/gallery/'+name).concat('catalog/atlas-gallery.json');
  const before = protectedFiles.map(digest);
  // Execute only the HTML/index builder with filesystem writes intercepted.
  // Preview calculation and rendering scripts are never invoked.
  const generated = JSON.parse(execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',['-B','-c',`
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json, runpy, sys
from unittest.mock import patch
from xml.etree import ElementTree as ET
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root/'scripts'))
writes = {}
def capture(path, text, *args, **kwargs):
    writes[str(path.resolve().relative_to(root))] = text
    return len(text)
with patch.object(Path, 'write_text', capture), patch.object(ET.ElementTree, 'write', lambda *args, **kwargs: None), redirect_stdout(StringIO()):
    runpy.run_path(str(root/'scripts/build-atlas-gallery.py'))
print(json.dumps({'html': writes['numerical-methods-atlas/gallery/index.html'], 'index': json.loads(writes['numerical-methods-atlas/gallery/index.json'])}))
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:8*1024*1024}));
  assert.deepEqual(generated.index,gallery,'all catalog cards, names, images, status and source receipts remain identical');
  assert.deepEqual(generated.html.match(/<li class="gallery-tile"[\s\S]*?<\/li>/g),html.match(/<li class="gallery-tile"[\s\S]*?<\/li>/g),'the complete rendered cards are unchanged');
  assert.deepEqual(generated.html.match(/<p class="gallery-note"[\s\S]*?<\/p>/g),html.match(/<p class="gallery-note"[\s\S]*?<\/p>/g),'all image-condition and counting explanations are retained');
  const sections = [...generated.html.matchAll(/<section\b[^>]*data-gallery\b[^>]*>([\s\S]*?)<\/section>/g)];
  assert.equal(sections.length,2);
  for (const [index,match] of sections.entries()) {
    const section = match[1], ja = index === 0;
    const disclosures = [...section.matchAll(/<details\b([^>]*)>([\s\S]*?)<\/details>/g)];
    assert.equal(disclosures.length,2);
    assert.ok(disclosures.every(row => !/\bopen(?:\s|=|$)/.test(row[1])),'both native disclosures are closed by default');
    assert.ok(disclosures[0][1].includes('gallery-domain-filter'));
    assert.ok(disclosures[0][2].includes('<summary>'+(ja?'分野で絞り込む':'Filter by domain')+'</summary>'));
    assert.equal((disclosures[0][2].match(/data-gallery-group=/g)||[]).length,inventory.groups.length+1);
    assert.ok(disclosures[1][1].includes('gallery-policy'));
    assert.ok(disclosures[1][2].includes('<summary>'+(ja?'図の条件・検証範囲・数え方':'Image conditions, validation scope and counting rules')+'</summary>'));
    assert.equal((disclosures[1][2].match(/class="gallery-note"/g)||[]).length,3);
    const visible = section.replace(/<details\b[^>]*>[\s\S]*?<\/details>/g,'');
    for (const selector of ['type="search"','data-gallery-reset','data-gallery-runnable','data-gallery-count','class="gallery-grid"']) assert.ok(visible.includes(selector),selector+' is visible without expanding optional controls');
    assert.ok(!visible.includes('data-gallery-group='));
  }
  assert.deepEqual(protectedFiles.map(digest),before,'no preview receipts or image mapping files need regeneration');
});

test('the visual index covers the exact atlas-wide inventory with one card per language and working image-to-problem links', () => {
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
      const target = tile.match(/<a\b[^>]*class="gallery-image-link"[^>]*href="([^"]+)"/)?.[1];
      assert.ok(target,x.id+' image opens its problem page');
      const hub = new URL(target,'https://hrkoyama.github.io');
      assert.equal(hub.pathname,`/numerical-methods-atlas/problems/${x.id}/`);
      assert.equal(hub.searchParams.get('lang'),lang);
      assert.ok(read(hub.pathname.slice(1)+'index.html').includes('<main'));
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
  assert.equal(gallery.items.length,87);
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

test('nonlinear Schnakenberg runs are additional entrances and retain the saved onset illustration',()=>{
  const identifiers=['schnakenberg-nonlinear','schnakenberg-pattern'];
  const item=gallery.items.find(x=>x.id==='turing-schnakenberg');
  assert.equal(gallery.items.length,87);
  assert.equal(gallery.counts.runnable_problems,47);
  assert.equal(item.image,'/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png');
  assert.equal(item.image_sha256,'d960e2701881dcd027d21d7d17f2a43c9e14157f1ab8a401e4cb69d95be88893');
  assert.deepEqual(item.supplemental_execution_entries.map(x=>x.id),['turing-schnakenberg',...identifiers,'reaction-diffusion-splitting']);
  const manifest=json('numerical-methods-atlas/gallery/preview-manifest.json');
  const base='code/validated-examples/2026-11-22/biology/';
  for(const name of ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json',...identifiers.map(x=>'results/'+x+'.png')])assert.equal(manifest.source_sha256[base+name],digest(base+name));
  assert.equal(manifest.calculations_sha256,'d98cd75e1c58177bfc716e8b68d6bfba1358d5135ac8e2ee0989eb3df77942a6');
});

test('the bimodal MCMC visual is one new physical target and preserves the old standard-normal illustration',()=>{
  const base='code/validated-examples/2026-11-22/mcmc/';
  const metadata=json(base+'cases.json').find(x=>x.id==='mcmc-multimodal-mixing');
  const problem=gallery.items.find(x=>x.id==='mcmc-bimodal-mixture');
  assert.equal(gallery.items.length,87);assert.equal(gallery.counts.runnable_problems,47);
  assert.equal(problem.image,'/'+base+'results/mcmc-multimodal-mixing.png');
  assert.equal(problem.image_sha256,digest(base+'results/mcmc-multimodal-mixing.png'));
  assert.deepEqual(problem.caption,metadata.summary);
  assert.deepEqual(problem.supplemental_execution_entries.map(x=>x.id),['mcmc-multimodal-mixing']);
  assert.ok(!gallery.items.some(x=>x.id==='mcmc-diagnostic-reference'));
  const old=gallery.items.find(x=>x.id==='gaussian-mcmc');
  assert.equal(old.image,'/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png');
  assert.equal(old.image_sha256,'a84e814bcce77c66f1886d01931a061b2317984e35e6e5fbf71dfa33a85e1c44');
  assert.deepEqual(old.supplemental_execution_entries.map(x=>x.id),['gaussian-mcmc']);
  const manifest=json('numerical-methods-atlas/gallery/preview-manifest.json');
  for(const name of ['cases.json','inputs.json','source-manifest.json','verification.json','results/result.json','results/mcmc-multimodal-mixing.png','results/mcmc-diagnostic-reference.png'])assert.equal(manifest.source_sha256[base+name],digest(base+name));
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
