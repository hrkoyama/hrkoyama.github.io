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

test('existing chapter sidebars show their own field and collapse other-field routes', () => {
  const catalog = json('catalog/atlas-reading-index.json'), resources = catalog.resource_chapters;
  for (const lang of ['ja','en']) {
    const content = json(`numerical-methods-atlas/content.${lang}.json`);
    const record = json(`numerical-methods-atlas/${lang}/read/index.json`), checked = [];
    for (const chapter of Object.keys(content)) {
      const html = read(`numerical-methods-atlas/${lang}/read/${chapter}/index.html`);
      if (!html.includes('src="/numerical-methods-atlas/reading.js"')) continue;
      checked.push(chapter);
      const field = record.groups.find(group => group.chapters.some(row => row.id === chapter));
      assert.ok(field, `${lang}/${chapter} has a single canonical field`);
      const sidebars = [...html.matchAll(/<aside\b[^>]*class="[^"]*\breading-nav\b[^"]*"[^>]*>([\s\S]*?)<\/aside>/g)];
      assert.equal(sidebars.length,1,lang+'/'+chapter+' has one contextual reading navigation');
      const sidebar = sidebars[0][1];
      const groups = [...sidebar.matchAll(/<nav\b([^>]*\bdata-reading-navigation-group="[^"]+"[^>]*)>([\s\S]*?)<\/nav>/g)];
      assert.deepEqual(groups.map(group => attrs(group[1])['data-reading-navigation-group']),['field','learn','resources']);
      assert.equal(attrs(groups[0][1])['data-reading-current-field'],field.id);
      const peers = resources.includes(chapter) ? [] : field.chapters.filter(row => !resources.includes(row.id));
      const peerLinks = links(groups[0][2]).filter(link => link['data-reading-field-chapter']);
      assert.deepEqual(peerLinks.map(link => link['data-reading-field-chapter']),peers.map(row => row.id));
      assert.deepEqual(peerLinks.map(link => destination(link.href).pathname),peers.map(row => row.url));
      const other = sidebar.match(/<details\b[^>]*\bdata-reading-other-fields[^>]*>/)?.[0];
      assert.ok(other,'other fields are available through native disclosure');
      assert.doesNotMatch(other,/\bopen(?:\s|=|>)/,'other fields start collapsed');
      const otherLinks = links(sidebar).filter(link => link['data-reading-other-field']);
      assert.deepEqual(otherLinks.map(link => link['data-reading-other-field']),catalog.groups.filter(group => group.id !== field.id).map(group => group.id));
      for (const link of otherLinks) {
        assert.equal(destination(link.href).pathname,`/numerical-methods-atlas/${lang}/read/`);
        assert.equal(new URL(link.href,origin).hash,'#reading-'+link['data-reading-other-field']);
        assert.ok(link.parents.some(parent => parent.name === 'details'));
      }
      const expected = [
        ['/numerical-methods-atlas/explore/',`/numerical-methods-atlas/${lang}/read/`,'/numerical-methods-atlas/methods/'],
        [`/numerical-methods-atlas/${lang}/read/textbooks/`,`/numerical-methods-atlas/${lang}/read/references/`]
      ];
      for (const [index,group] of groups.slice(1).entries()) {
        const entries = links(group[2]);
        assert.deepEqual(entries.map(link => destination(link.href).pathname),expected[index]);
        assert.ok(entries.every(link => ![...link.parents,link].some(element => element.name === 'details' || element.hidden)));
      }
      assert.match(sidebar,/\bdata-reading-all-chapters(?:\s|>)/);
      const active = links(sidebar).filter(link => link['aria-current'] === 'page');
      assert.deepEqual(active.map(link => new URL(link.href,origin).pathname),[`/numerical-methods-atlas/${lang}/read/${chapter}/`]);
      assert.equal(links(sidebar).length,1+peers.length+catalog.groups.length-1+5,'other chapters are not flattened into every sidebar');
    }
    assert.ok(['textbooks','references','stability'].every(chapter => checked.includes(chapter)));
  }
});

test('navigation renderer binds current fields, resource roles and actual edition fallback without rewriting pages', () => {
  const output = execFileSync('python3', ['-B','-c',String.raw`
import copy,hashlib,importlib.util,json,pathlib,tempfile
path=pathlib.Path('scripts/build-atlas-reading-navigation.py')
spec=importlib.util.spec_from_file_location('reading_navigation',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
root=pathlib.Path.cwd();catalog=json.loads((root/'catalog/atlas-reading-index.json').read_text())
for language in ['ja','en']:
 record=json.loads((root/'numerical-methods-atlas'/language/'read/index.json').read_text())
 for chapter in ['stability','textbooks','references']:
  html=module.navigation(language,chapter,record,catalog['resource_chapters'])
  field=next(g for g in record['groups'] if any(c['id']==chapter for c in g['chapters']))
  assert 'data-reading-current-field="'+field['id']+'"' in html
  assert html.count('aria-current="page"')==1
  assert '<details data-reading-other-fields>' in html
  assert 'data-reading-all-chapters' in html
 try:module.navigation(language,'not-a-chapter',record,catalog['resource_chapters'])
 except ValueError:pass
 else:raise AssertionError('unknown chapter accepted')
 duplicate=copy.deepcopy(record);duplicate['groups'].append(next(g for g in record['groups'] if any(c['id']=='stability' for c in g['chapters'])))
 try:module.navigation(language,'stability',duplicate,catalog['resource_chapters'])
 except ValueError:pass
 else:raise AssertionError('ambiguous field accepted')
# Only read fixtures are prepared: no builder or site generator is invoked.
with tempfile.TemporaryDirectory(prefix='reading-nav-contract-') as temporary:
 fixture=pathlib.Path(temporary);(fixture/'catalog').mkdir();small={'groups':[{'id':'one','chapters':['only-en']}],'resource_chapters':[]}
 source=fixture/'catalog/atlas-reading-index.json';source.write_text(json.dumps(small));digest=hashlib.sha256(source.read_bytes()).hexdigest()
 row={'id':'only-en','title':'English only','language':'en','url':'/numerical-methods-atlas/en/read/only-en/'}
 for language in ['ja','en']:
  folder=fixture/'numerical-methods-atlas'/language/'read';folder.mkdir(parents=True)
  record={'language':language,'source_sha256':digest,'groups':[{'id':'one','title':'One','chapters':[row]}]}
  (folder/'index.json').write_text(json.dumps(record))
 page=fixture/'numerical-methods-atlas/en/read/only-en/index.html';page.parent.mkdir();page.write_text('<h1>English only</h1>')
 records,_=module.reading_records(fixture);assert row['url'] in module.navigation('ja','only-en',records['ja'],[])
 target=fixture/'numerical-methods-atlas/ja/read/index.json';record=json.loads(target.read_text());record['groups'][0]['chapters'][0]['url']='https://other.example/read/only-en/';target.write_text(json.dumps(record))
 try:module.reading_records(fixture)
 except ValueError:pass
 else:raise AssertionError('foreign edition accepted')
print('field ownership, resource roles, unknown/ambiguous negatives and real-edition fallback checked')
`],{cwd:fileURLToPath(root),encoding:'utf8'});
  assert.match(output,/field ownership, resource roles/);
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

test('the learning guide distinguishes suggested paths from the complete index and keeps resource links visible', () => {
  const html = read('numerical-methods-atlas/explore/index.html');
  const record = json('numerical-methods-atlas/explore/index.json'), markdown = read('numerical-methods-atlas/explore/index.md');
  assert.equal(record.role,'learning-guide');
  assert.equal((html.match(/\bdata-learning-guide-role(?:\s|>)/g)||[]).length,2);
  assert.equal((html.match(/\bdata-learning-guide-paths=/g)||[]).length,2);
  const sections = [...html.matchAll(/<section\b([^>]*class="[^"]*\bstudy-references\b[^"]*"[^>]*)>([\s\S]*?)<\/section>/g)];
  assert.equal(sections.length,2,'one visible resource section per language');
  for (const lang of ['ja','en']) {
    const title = lang === 'ja' ? '学習ガイド：おすすめの順番' : 'Learning guide: suggested order';
    assert.equal(record.title[lang],title);
    assert.ok(html.includes('<h1>'+title+'</h1>'));
    const paths = html.indexOf('data-learning-guide-paths="'+lang+'"');
    const map = html.indexOf('id="atlas-map-'+lang+'"');
    const references = html.indexOf('id="study-references-title-'+lang+'"');
    assert.ok(paths >= 0 && map > paths && references > map,'suggested learning paths and field map precede supporting references');
    assert.equal(record.chapters[lang],`/numerical-methods-atlas/${lang}/read/`);
    const toc = links(html).filter(link => new URL(link.href,origin).pathname === record.chapters[lang]);
    assert.ok(toc.some(link => link.text === (lang === 'ja' ? '分野別の全章目次' : 'Complete chapter index')));
    assert.ok(markdown.includes(origin+record.chapters[lang]));
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
