import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {findMethods} from '../search/method-search.mjs';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root = new URL('../', import.meta.url);
const text = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(text(path));
const saved = json('numerical-methods-atlas/assets/operator-splitting.json');
const catalog = json('catalog/atlas-methods.json').methods;
const published = json('numerical-methods-atlas/methods/index.json').methods;
const chapter = json('catalog/atlas-detailed-reading.json').chapters.find(c => c.id === 'operator-splitting');

test('search indexes the final published home, sharing counts and roadmap in the same build', () => {
  const refresh = JSON.parse(text('catalog/site-build-pipeline.json')).stages.map(stage=>stage.script);
  const purpose = 'scripts/build-atlas-purpose.py', search = 'scripts/build-atlas-search.py';
  assert.ok(refresh.indexOf(purpose) < refresh.indexOf(search));
  assert.ok(refresh.indexOf('scripts/build-atlas-sharing.py') < refresh.indexOf(search));
  assert.ok(refresh.lastIndexOf(purpose) > refresh.indexOf(search), 'finalize parent asset hashes after search');
  execFileSync('python3', ['-B', '-c', `
import importlib.util,json,pathlib,sys
root=pathlib.Path.cwd()
sys.path.insert(0,str(root/'scripts'))
spec=importlib.util.spec_from_file_location('atlas_search',root/'scripts/build-atlas-search.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
entries={e['id']:e for e in json.loads((root/'numerical-methods-atlas/home-search-index.json').read_text())['entries']}
for lang in ['ja','en']:
 for ident,path in [('roadmap',f'numerical-methods-atlas/{lang}/read/roadmap/index.html'),('public-resource-explore','numerical-methods-atlas/explore/index.html'),('public-resource-share','numerical-methods-atlas/share/index.html')]:
  expected=module.published_page(root/path,lang)
  assert entries[ident]['text'][lang]==expected['text'],(ident,lang,'stale published prose/counts')
`], {cwd:fileURLToPath(root)});
});

test('the fixed oscillator illustration reproduces local/global order against analytic rotation', () => {
  execFileSync('python3', ['scripts/verify-operator-splitting.py', '--check', 'numerical-methods-atlas/assets/operator-splitting.json'], {cwd:fileURLToPath(root)});
  const mul = (a, b) => a.map(row => b[0].map((_, j) => row.reduce((sum, x, k) => sum + x * b[k][j], 0)));
  const apply = (a, u) => a.map(row => row.reduce((sum, x, j) => sum + x * u[j], 0));
  const drift = h => [[1,h],[0,1]], kick = h => [[1,0],[-h,1]];
  const matrix = (method, h) => method === 'lie-trotter' ? mul(kick(h), drift(h))
    : method === 'reverse-lie-trotter' ? mul(drift(h), kick(h))
    : mul(drift(h/2), mul(kick(h), drift(h/2)));
  const close = (actual, expected) => assert.ok(Math.abs(actual-expected) < 3e-13, `${actual} vs ${expected}`);
  for (const [method, rows] of Object.entries(saved.methods)) {
    for (const row of rows) {
      const m = matrix(method, row.h);
      let u = [1,0];
      for (let n=0; n<row.n; n++) u = apply(m, u);
      u.forEach((value, j) => close(value, row.state[j]));
      close(Math.hypot(u[0]-Math.cos(1), u[1]+Math.sin(1)), row.global_error);
      const local = apply(m, [1,0]);
      close(Math.hypot(local[0]-Math.cos(row.h), local[1]+Math.sin(row.h)), row.local_defect);
      if (row.global_error_order) {
        assert.ok(Math.abs(row.global_error_order - (method === 'strang' ? 2 : 1)) < .08);
        assert.ok(Math.abs(row.local_defect_order - (method === 'strang' ? 3 : 2)) < .08);
      }
    }
  }
  const u = [1,.3], h = .1;
  apply(matrix('strang', -h), apply(matrix('strang', h), u)).forEach((x,j) => close(x,u[j]));
  assert.ok(Math.hypot(...apply(matrix('lie-trotter', -h), apply(matrix('lie-trotter', h), u)).map((x,j) => x-u[j])) > 1e-4);
  assert.notDeepEqual(saved.methods['lie-trotter'][0].state, saved.methods['reverse-lie-trotter'][0].state);
  assert.ok(saved.commuting_control.every(row => row.absolute_error < 1e-14));
});

test('both methods and their Japanese/Unicode aliases are canonical hits in both public searches', () => {
  const inline = json('numerical-methods-atlas/home-search-index.json');
  const global = makeSearch(json('search/index.json').documents);
  for (const [id, queries] of [
    ['lie-trotter', ['Lie–Trotter Splitting','Lie-Trotter splitting','Lie Trotter','リー・トロッター分割']],
    ['strang-splitting', ['Strang splitting','Strang分割法','ストラング分割','Strang–Marchuk splitting']],
  ]) {
    const original = catalog.find(m => m.id === id), method = published.find(m => m.id === id);
    assert.equal(original.status, 'educational-example');
    assert.equal(original.group.id, 'time');
    assert.ok(method.code_urls.some(url=>url.endsWith('/splitting/splitting.py')));
    assert.ok(method.test_urls.some(url=>url.endsWith('/splitting/test_splitting.py')));
    const expectedRunners=['reaction-diffusion-splitting','strang-boundary-order-reduction',...(id==='strang-splitting'?['multifrequency-resonance']:[])];
    assert.deepEqual(method.execution_examples.map(x=>x.id),expectedRunners);
    assert.equal(method.depth_release.group,'splitting');
    assert.equal(method.depth_release.code_edition,'2026-11-22');
    assert.deepEqual(method.depth_release.case_ids,['reaction-diffusion-splitting']);
    assert.deepEqual(method.depth_release.code_urls,['run.py','splitting.py','reference.py'].map(p=>'https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/'+p));
    const expectedAdditions=[{group:'ode-adaptivity',edition:'2026-11-24-r2',case_ids:['strang-boundary-order-reduction']},...(id==='strang-splitting'?[{group:'geometric-controls',edition:'2026-11-24',case_ids:['multifrequency-resonance']}]:[])];
    assert.deepEqual(method.depth_additional_releases.map(r=>({group:r.group,edition:r.code_edition,case_ids:r.case_ids})),expectedAdditions);
    for(const release of method.depth_additional_releases){
      const packetBase=`code/validated-examples/${release.code_edition}/${release.group}/`;
      assert.equal(release.code_base,'https://hrkoyama.github.io/'+packetBase);
      assert.deepEqual(release.examples.map(x=>x.id),release.case_ids);
      const metadata=JSON.parse(text(packetBase+'cases.json'));
      for(const caseId of release.case_ids)assert.ok(metadata.find(x=>x.id===caseId)?.method_ids.includes(id),caseId+'/actual-method-owner');
    }
    for (const lang of ['ja','en']) {
      assert.equal(method.reading[lang], `https://hrkoyama.github.io/numerical-methods-atlas/${lang}/read/operator-splitting/`);
      for (const query of queries) {
        assert.equal(findMethods(published,query,lang)[0]?.id, id, query);
        assert.equal(searchChapters(inline,query,lang)[0]?.method?.id, id, query);
        assert.equal(global(query,lang,'atlas')[0]?.method?.id, id, query);
      }
    }
  }
});

test('the bilingual reading retains formulas, comparison data, source access notes and working reproduction routes', () => {
  const expected = ['model','lie-trotter','strang','comparison','small-example','conditions','related-examples','reproduce','scoped-examples','publication-scope','sources'];
  const formulas = Object.keys(json('catalog/atlas-detailed-reading.json').formulas).filter(id => id.startsWith('splitting-'));
  assert.equal(formulas.length,10);
  for (const lang of ['ja','en']) {
    const prefix = `numerical-methods-atlas/${lang}/read/operator-splitting/`;
    const doc = json(prefix+'index.json'), html = text(prefix+'index.html'), md = text(prefix+'index.md');
    assert.deepEqual(doc.headings.map(h => h.id), expected);
    assert.ok(!html.includes('math-placeholder') && !html.includes('__COMPARISON'));
    assert.equal((chapter.html[lang].match(/<table\b/g)||[]).length, 2);
    assert.equal((doc.html.match(/<table\b/g)||[]).length, 2);
    assert.ok(doc.html.includes('id="supplement-reaction-diffusion-splitting"'));
    for (const method of ['lie-trotter','strang-splitting']) assert.equal(doc.implementation_status[method], 'educational-example');
    for (const rows of [saved.methods['lie-trotter'], saved.methods.strang]) {
      for (const row of rows) {
        const value = row.global_error.toExponential(6).replace(/e(-?)(\d)$/, 'e$10$2');
        assert.ok(html.includes(value), value);
        assert.ok(md.includes(value), value);
      }
    }
    assert.ok(md.includes('| --- |'));
    for (const url of ['/scripts/verify-operator-splitting.py','/numerical-methods-atlas/assets/operator-splitting.json']) {
      assert.ok(html.includes(url));
      assert.ok(text(url.slice(1)));
    }
    assert.ok(html.includes('schnakenberg-nonlinear') && html.includes('schnakenberg-pattern'));
    const spa = json(`numerical-methods-atlas/content.${lang}.json`);
    assert.equal(spa['operator-splitting'].html,doc.html);
    for (const target of chapter.linked_from) {
      const marker = '<!-- detailed-followup-operator-splitting -->';
      assert.equal(spa[target].html.split(marker).length,2);
      assert.equal(text(`numerical-methods-atlas/${lang}/read/${target}/index.html`).split(marker).length,2);
    }
  }
  assert.deepEqual(chapter.references,['trotter1959','strang1968','hairer2010-geometric-lecture2']);
  const bibliography = json('numerical-methods-atlas/references.json');
  assert.equal(bibliography.filter(r => r.doi?.toLowerCase() === '10.1090/s0002-9939-1959-0108732-6').length,1);
});
