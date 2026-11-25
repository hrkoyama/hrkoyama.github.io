import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync, readFileSync, readdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {runInNewContext} from 'node:vm';
import {normalizeReadingQuery, matchesReadingChapter, wireReadingIndex} from '../numerical-methods-atlas/reading-index.mjs';

const root = new URL('../', import.meta.url);
const origin = 'https://hrkoyama.github.io';
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const catalog = json('catalog/atlas-reading-index.json');
const decode = value => value.replaceAll('&amp;', '&').replaceAll('&quot;', '"').replaceAll('&#39;', "'").replaceAll('&#x27;', "'").replaceAll('&lt;', '<').replaceAll('&gt;', '>');
const attributes = tag => Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match => [match[1], decode(match[2])]));
const main = html => {
  const match = html.match(/<main\b(?=[^>]*\bid="reading-index")[^>]*>([\s\S]*?)<\/main>/);
  assert.ok(match, 'one unified reading index main');
  return match[1];
};
const inventory = lang => readdirSync(new URL(`numerical-methods-atlas/${lang}/read/`, root), {withFileTypes:true})
  .filter(entry => entry.isDirectory() && existsSync(new URL(`numerical-methods-atlas/${lang}/read/${entry.name}/index.html`, root)))
  .map(entry => entry.name).sort();
const available = Object.fromEntries(['ja','en'].map(lang => [lang, inventory(lang)]));
const allChapters = [...new Set([...available.ja, ...available.en])].sort();
const routes = html => [...html.matchAll(/<a\b[^>]*\bhref="([^"]+)"/g)]
  .map(match => new URL(decode(match[1]), origin))
  .filter(url => /^\/numerical-methods-atlas\/(?:ja|en)\/read\/[^/]+\/$/.test(url.pathname));

test('one bilingual editorial catalog covers every existing chapter exactly once', () => {
  assert.ok(catalog.groups.length > 1);
  const groups = catalog.groups.map(group => group.id);
  assert.equal(new Set(groups).size, groups.length);
  const chapters = catalog.groups.flatMap(group => group.chapters);
  assert.equal(chapters.length, new Set(chapters).size, 'chapters are not appended to a second section');
  assert.deepEqual([...chapters].sort(), allChapters, 'existing chapter URLs are neither dropped nor invented');
  assert.deepEqual([...catalog.resource_chapters].sort(),['references','textbooks']);
  assert.ok(catalog.resource_chapters.every(id=>chapters.includes(id)),'learning resources retain their place in the complete index');
  for (const group of catalog.groups) {
    assert.match(group.id, /^[a-z0-9-]+$/);
    assert.ok(group.chapters.length > 0);
    for (const lang of ['ja','en']) {
      assert.ok(group.title[lang]?.trim(), group.id+'/'+lang+' title');
      assert.ok(group.description[lang]?.trim(), group.id+'/'+lang+' description');
    }
  }
});

test('the unified contents are rebuilt after legacy appenders and before public indexes', () => {
  const refresh = JSON.parse(read('catalog/site-build-pipeline.json')).stages.map(stage=>stage.script);
  const unified = refresh.indexOf('scripts/build-atlas-reading-index.py');
  assert.ok(unified > 0);
  for (const builder of ['build-quantum-examples.py','build-atlas-detailed-reading.py','build-atlas-depth-examples.py','build-atlas-h2.py','build-atlas-periodic.py','build-atlas-forces.py','build-atlas-quantum.py','build-thermostat-reading.py']) {
    const position = refresh.indexOf('scripts/'+builder);
    assert.ok(position >= 0 && position < unified, builder+' cannot append a second contents section afterward');
  }
  for (const builder of ['build-atlas-search.py','build-site-chrome.mjs','build-sitemap.py','build-guide.py','build-search.py']) {
    assert.ok(refresh.indexOf('scripts/'+builder) > unified, builder+' sees the final contents');
  }
});

test('both contents pages share group order and one consistent entry per real chapter', () => {
  const expectedIds = catalog.groups.flatMap(group => group.chapters);
  for (const lang of ['ja','en']) {
    const html = read(`numerical-methods-atlas/${lang}/read/index.html`), body = main(html);
    const record = json(`numerical-methods-atlas/${lang}/read/index.json`);
    const groups = [...body.matchAll(/<section\b[^>]*\bdata-reading-group="([^"]+)"[^>]*>/g)].map(match => match[1]);
    const entries = [...body.matchAll(/<li\b[^>]*\bdata-reading-chapter="([^"]+)"[^>]*>/g)].map(match => ({id:match[1], tag:match[0]}));
    assert.deepEqual(groups, catalog.groups.map(group => group.id));
    assert.deepEqual(entries.map(entry => entry.id), expectedIds);
    assert.deepEqual(record.groups.map(group => group.id), groups);
    assert.equal(record.language, lang);
    assert.equal(record.chapter_count, allChapters.length);
    assert.equal(routes(body).length, allChapters.length);
    assert.ok(!/<!--\s*(?:detailed-reading|depth-examples|h2-reading|periodic-reading|forces-reading|quantum-entry|thermostat-entry)\s*-->/.test(html), 'old append blocks are replaced by the unified catalog');
    assert.equal((body.match(/<h1\b/g)||[]).length, 1);
    const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
    assert.equal(ids.length, new Set(ids).size, 'no duplicated sidebar/main anchors');
    for (const entry of entries) {
      assert.ok(entry.tag.includes('data-search='), entry.id+' searchable text');
      assert.ok(!/\bhidden(?:\s|=|>)/.test(entry.tag), entry.id+' is available without JavaScript');
    }
    for (const group of record.groups) {
      assert.equal(group.title, catalog.groups.find(item => item.id === group.id).title[lang]);
      for (const chapter of group.chapters) {
        const editions = ['ja','en'].filter(edition => available[edition].includes(chapter.id));
        assert.deepEqual([...chapter.available_languages].sort(), [...editions].sort(), chapter.id+' editions');
        assert.equal(chapter.language, editions.includes(lang)?lang:editions.includes('en')?'en':editions[0]);
        const route = new URL(chapter.url, origin);
        assert.equal(route.origin, origin);
        assert.equal(route.pathname, `/numerical-methods-atlas/${chapter.language}/read/${chapter.id}/`);
        assert.ok(existsSync(new URL(route.pathname.slice(1)+'index.html', root)), chapter.url);
        assert.ok(chapter.title?.trim() && chapter.search_text?.includes(chapter.id));
      }
    }
  }
});

test('the complete index distinguishes lookup, suggested learning order and learning resources', () => {
  const expected = {
    ja:{title:'分野別の全章目次',purpose:/理論・導出・計算例/,reference:'手法・コードの対応表',referencePurpose:/適用条件・コード・検証例/},
    en:{title:'Complete chapter index',purpose:/theory, derivations and worked examples/,reference:'Methods and code reference',referencePurpose:/conditions, code and checks/}
  };
  const text = html => decode(html.replace(/<[^>]+>/g, '')).trim();
  for (const lang of ['ja','en']) {
    const html = read(`numerical-methods-atlas/${lang}/read/index.html`), body = main(html);
    const heading = body.match(/<header class="reading-heading">([\s\S]*?)<\/header>/)?.[1];
    assert.ok(heading, lang+' learning introduction is above the chapter groups');
    assert.equal(text(heading.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/)?.[1] || ''), expected[lang].title);
    assert.match(text(heading), expected[lang].purpose, 'readers are told to expect theory, derivations and examples');
    const related = heading.match(/<p class="reading-related">([\s\S]*?)<\/p>/)?.[1];
    assert.ok(related, 'the complementary reference is visible in the introduction, beyond the footer');
    assert.match(text(related), expected[lang].referencePurpose, 'the reference has a distinct lookup role');
    const link = related.match(/<a\b([^>]*)>([\s\S]*?)<\/a>/);
    assert.ok(link);
    assert.equal(text(link[2]), expected[lang].reference);
    const destination = new URL(attributes(link[1]).href, origin);
    assert.equal(destination.origin, origin);
    assert.equal(destination.pathname, '/numerical-methods-atlas/methods/');
    assert.equal(destination.searchParams.get('lang'), lang);
    assert.ok(existsSync(new URL('numerical-methods-atlas/methods/index.html', root)));
    const record = json(`numerical-methods-atlas/${lang}/read/index.json`);
    assert.equal(record.role,'complete-chapter-index');
    assert.equal(record.learning_guide.url,`/numerical-methods-atlas/explore/?lang=${lang}`);
    assert.match(heading,/\bdata-reading-index-role(?:\s|>)/);
    assert.match(body,/\bdata-reading-learning-guide(?:\s|>)/);
    assert.ok(record.classification_note.includes(String(catalog.groups.length)));
    const resourceRows = record.groups.flatMap(group => group.chapters).filter(row => row.kind === 'learning-resource');
    assert.deepEqual(resourceRows.map(row=>row.id).sort(),[...catalog.resource_chapters].sort());
    assert.equal((body.match(/\bdata-reading-resource-label(?:\s|>)/g)||[]).length,catalog.resource_chapters.length);
    assert.equal(record.title, expected[lang].title);
    assert.match(record.description, expected[lang].purpose, 'JSON presents the same learning purpose');
    const markdown = read(`numerical-methods-atlas/${lang}/read/index.md`);
    assert.ok(markdown.startsWith('# '+expected[lang].title+'\n\n'));
    assert.match(markdown, expected[lang].purpose, 'Markdown presents the same learning purpose');
  }
});

test('the shared language switch follows reciprocal contents editions through hreflang', () => {
  const implementation = read('site.js').match(/^  function languageURL\(language\) \{[\s\S]*?^  \}/m)?.[0];
  assert.ok(implementation, 'the shared language URL function is exercised');
  for (const lang of ['ja','en']) {
    const html = read(`numerical-methods-atlas/${lang}/read/index.html`);
    const head = html.match(/<head\b[^>]*>([\s\S]*?)<\/head>/)?.[1];
    assert.ok(head);
    const alternates = [...head.matchAll(/<link\b[^>]*>/g)]
      .map(match => attributes(match[0]))
      .filter(link => link.rel === 'alternate' && ['ja','en'].includes(link.hreflang));
    assert.equal(alternates.length, 2, 'one explicit link for each real contents edition');
    const body = attributes(html.match(/<body\b[^>]*>/)?.[0] || '');
    assert.equal(body['data-content-language'], lang, 'shared controls recognize a fixed-language page');
    for (const edition of ['ja','en']) {
      const alternate = alternates.find(link => link.hreflang === edition);
      assert.equal(alternate?.href, `${origin}/numerical-methods-atlas/${edition}/read/`);
      assert.ok(existsSync(new URL(`numerical-methods-atlas/${edition}/read/index.html`, root)));
      const fragment = `#reading-${catalog.groups[0].id}`;
      const location = new URL(`${origin}/numerical-methods-atlas/${lang}/read/?lang=${lang}${fragment}`);
      const document = {
        body:{dataset:{contentLanguage:body['data-content-language']}},
        querySelector:selector => selector === `link[rel="alternate"][hreflang="${edition}"]` ? alternate : null
      };
      const destination = runInNewContext(implementation+';languageURL(language).href', {document,location,language:edition,URL});
      assert.equal(destination, `${origin}/numerical-methods-atlas/${edition}/read/?lang=${edition}${fragment}`,
        'switching editions changes the route and preserves the category anchor');
    }
  }
});

test('chapter filtering recognizes mixed-language words and full-width input', () => {
  assert.equal(normalizeReadingQuery('  Ｂｒａｔｕ　逆問題  '), 'bratu 逆問題');
  const text = 'Bratu inverse problem 正則化 regularization nonlinear-solvers';
  assert.equal(matchesReadingChapter(text, ''), true);
  assert.equal(matchesReadingChapter(text, '   '), true);
  assert.equal(matchesReadingChapter(text, 'ＢＲＡＴＵ 正則化'), true);
  assert.equal(matchesReadingChapter(text, 'regularization inverse'), true);
  assert.equal(matchesReadingChapter(text, 'bratu quantum'), false);
});

test('filter controls handle IME, Enter, empty results and reset while keeping category links in sync', () => {
  const element = (dataset={}) => ({dataset,hidden:false,value:'',textContent:'',events:{},
    addEventListener(name,callback){this.events[name]=callback;},
    fire(name,event={}){this.events[name]?.(event);},focus(){this.focused=true;}});
  const controls=element(), input=element(), reset=element(), status=element(), empty=element();
  controls.hidden=true; empty.hidden=true;
  const chapters=[element({search:'stability 安定性'}),element({search:'Bratu inverse 逆問題'}),element({search:'FDTD 電磁場'})];
  const groups=[element({readingGroup:'foundations'}),element({readingGroup:'fields'})];
  groups[0].querySelectorAll=()=>chapters.slice(0,2); groups[1].querySelectorAll=()=>chapters.slice(2);
  const links=groups.map(group=>element({readingGroupLink:group.dataset.readingGroup}));
  const selectors={'[data-reading-controls]':controls,'[data-reading-input]':input,'[data-reading-reset]':reset,'[data-reading-count]':status,'[data-reading-empty]':empty};
  const page={dataset:{language:'ja'},querySelector:selector=>selectors[selector],querySelectorAll:selector=>({
    '[data-reading-chapter]':chapters,'[data-reading-group]':groups,'[data-reading-group-link]':links
  }[selector])};
  wireReadingIndex({querySelector:selector=>selector==='#reading-index'?page:null});
  assert.equal(controls.hidden,false);
  assert.equal(status.textContent,'3 / 3章');
  input.fire('compositionstart'); input.value='Ｂｒａｔｕ'; input.fire('input');
  assert.ok(chapters.every(chapter=>!chapter.hidden),'a partial IME composition does not filter the page');
  input.fire('compositionend');
  assert.deepEqual(chapters.map(chapter=>chapter.hidden),[true,false,true]);
  assert.deepEqual(groups.map(group=>group.hidden),[false,true]);
  assert.deepEqual(links.map(link=>link.hidden),[false,true]);
  assert.equal(status.textContent,'1 / 3章');
  let prevented=false; input.value='missing term'; controls.fire('submit',{preventDefault(){prevented=true;}});
  assert.ok(prevented,'Enter does not submit the query to a server');
  assert.ok(chapters.every(chapter=>chapter.hidden));
  assert.equal(empty.hidden,false);
  reset.fire('click');
  assert.equal(input.value,''); assert.equal(input.focused,true);
  assert.ok(chapters.every(chapter=>!chapter.hidden));
  assert.ok(groups.every(group=>!group.hidden)&&links.every(link=>!link.hidden));
  assert.equal(empty.hidden,true);
  assert.equal(status.textContent,'3 / 3章');
});

test('the filter stays local and the complete contents remain usable without JavaScript', () => {
  const module = read('numerical-methods-atlas/reading-index.mjs');
  assert.doesNotMatch(module, /\b(?:fetch|XMLHttpRequest|WebSocket|sendBeacon)\s*\(/);
  assert.doesNotMatch(module, /(?:location|history)\s*\.\s*(?:search|pushState|replaceState)/);
  for (const lang of ['ja','en']) {
    const html = read(`numerical-methods-atlas/${lang}/read/index.html`), body = main(html);
    const controls = body.match(/<[^>]+\bdata-reading-controls\b[^>]*>/)?.[0];
    assert.ok(controls && /\bhidden(?:\s|=|>)/.test(controls));
    const inputs = [...body.matchAll(/<input\b[^>]*\btype="search"[^>]*>/g)].map(match => attributes(match[0]));
    assert.equal(inputs.length, 1);
    assert.ok(inputs[0].id);
    assert.ok(body.includes(`for="${inputs[0].id}"`));
    assert.ok(!['q','query','search'].includes(inputs[0].name), 'keywords are not submitted to a server');
    const linkIds = [...body.matchAll(/\bdata-reading-group-link="([^"]+)"/g)].map(match => match[1]);
    assert.deepEqual(linkIds, catalog.groups.map(group => group.id));
    for (const tag of [...body.matchAll(/<section\b[^>]*\bdata-reading-group="[^"]+"[^>]*>/g)]) assert.ok(!/\bhidden(?:\s|=|>)/.test(tag[0]));
  }
});

test('edition selection has an explicit English fallback without inventing translated pages', () => {
  const output = execFileSync('python3', ['-B', '-c', String.raw`
import importlib.util,pathlib,sys
path=pathlib.Path('scripts/build-atlas-reading-index.py')
sys.path.insert(0,str(path.parent.resolve()))
spec=importlib.util.spec_from_file_location('reading_index_builder',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
assert module.edition_for('ja',['ja','en'])=='ja'
assert module.edition_for('en',['ja','en'])=='en'
assert module.edition_for('ja',['en'])=='en'
assert module.edition_for('en',['ja'])=='ja'
print('edition fallback checked')
`], {cwd:fileURLToPath(root),encoding:'utf8'});
  assert.match(output, /edition fallback checked/);
});
