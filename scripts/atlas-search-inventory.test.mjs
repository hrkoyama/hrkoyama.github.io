import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {copyFileSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync} from 'node:fs';
import {join} from 'node:path';
import {tmpdir} from 'node:os';
import {pathToFileURL, fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const scratch = process.env.ATLAS_INDEX_SCRATCH || tmpdir();
const read = path => readFileSync(path, 'utf8');
const hash = path => createHash('sha256').update(readFileSync(path)).digest('hex');
const write = (root, path, value) => {
  const target = join(root, path);
  mkdirSync(join(target, '..'), {recursive:true});
  writeFileSync(target, typeof value === 'string' ? value : JSON.stringify(value));
};
const chapterPath = (language, id) => `numerical-methods-atlas/${language}/read/${id}/index.html`;
const page = (title, body = '', language = 'en') => `<!doctype html><html lang="${language}"><head><title>Stale head title</title></head><body><header>HeaderExcludedToken</header><main><aside class="reading-nav"><h2 id="sidebar">SidebarExcludedToken</h2></aside><article><header class="chapter-heading"><h1>${title}</h1></header>${body}<nav>NavigationExcludedToken</nav><script>ScriptExcludedToken</script><p hidden>HiddenExcludedToken</p><p aria-hidden="true">AriaHiddenExcludedToken</p></article></main><footer>FooterExcludedToken</footer></body></html>`;

function fixture() {
  mkdirSync(scratch, {recursive:true});
  const directory = mkdtempSync(join(scratch, 'atlas-search-inventory-'));
  const method = {id:'fixture-newton',name:{ja:'試験Newton法',en:'Fixture Newton'},aliases:['fixturemethodalias'],group:{ja:'非線形',en:'Nonlinear'},status:'reading-only',url:'https://hrkoyama.github.io/numerical-methods-atlas/methods/fixture-newton/',execution_examples:[]};
  write(directory, 'catalog/atlas-methods.json', {methods:[method],scientific_status:'unchanged'});
  write(directory, 'catalog/atlas-depth-expansion.json', {groups:[],case_problem_ids:{},routine_policy:'unchanged'});
  write(directory, 'catalog/atlas-test-problems.json', {problems:[],scientific_count:0});
  write(directory, 'catalog/atlas-crossovers.json', {title:{ja:'関連',en:'Connections'},intro:{ja:'説明',en:'Overview'},math_families:[],routes:[]});
  write(directory, 'catalog/atlas-detailed-reading.json', {chapters:[{id:'detailed',title:{en:'Stale catalog title'},keywords:['detailedalias'],methods:['fixture-newton']}]});
  write(directory, 'numerical-methods-atlas/methods/index.json', {methods:[method]});
  write(directory, 'numerical-methods-atlas/coverage.json', {items:[{chapter:'ordinary',label:'coveragealias',group:'Foundations',status:'reading-only'}],counts:{methods:1}});
  write(directory, 'numerical-methods-atlas/glossary.json', {terms:[{chapter:'ordinary',en:'Glossary term',ja:'用語',aliases:['ordinarysynonym']}]});
  write(directory, 'numerical-methods-atlas/translation-status.json', {chapters:{ordinary:{status:'draft'}},reviewed:0});
  for (const language of ['ja','en']) {
    write(directory, `numerical-methods-atlas/content.${language}.json`, {ordinary:{title:'Obsolete metadata title',html:'Obsolete metadata body',headings:[]}});
    write(directory, chapterPath(language, 'ordinary'), page('Initial ordinary title '+language,'<h2 id="initial-section">Initial section</h2><p>InitialBodyToken</p>',language));
    write(directory, chapterPath(language, 'deleted'), page('DeletedPageToken '+language,'<p>DeletedBodyToken</p>',language));
    write(directory, `numerical-methods-atlas/${language}/read/ordinary/index.json`, {title:'Obsolete per-chapter title',status:'frozen'});
  }
  write(directory, chapterPath('en','detailed'), page('Published detailed title','<p>DetailedBodyToken</p>'));
  write(directory, 'numerical-methods-atlas/new-guide/index.html', '<main><section data-site-language="ja"><h1>新しい案内</h1><p>GuideJapaneseToken</p></section><section data-site-language="en"><h1>New published guide</h1><p>GuideEnglishToken</p></section></main>');
  // Poisoned seed proves that the previous generated index is never an input.
  write(directory, 'numerical-methods-atlas/home-search-index.json', {version:1,entries:[{id:'ghost',title:{ja:'GhostSeedToken',en:'GhostSeedToken'},headings:{ja:[],en:[]},keywords:['GhostSeedToken'],routes:{en:'/numerical-methods-atlas/en/read/ghost/'}}]});
  write(directory, 'package.json', {type:'module'});
  for (const file of ['numerical-methods-atlas/home-search.js','numerical-methods-atlas/i18n.js','numerical-methods-atlas/reading-urls.js','search/method-search.mjs','search/methods.css','search/goals-data.mjs']) {
    const target = join(directory,file); mkdirSync(join(target,'..'),{recursive:true}); copyFileSync(join(root,file),target);
  }
  write(directory, 'numerical-methods-atlas/home-overview.js', "import {} from './home-search.js';\n");
  return directory;
}

function rebuild(directory) {
  // Isolate the two validated execution registries: these tests exercise their
  // integration shape without opening or rerunning frozen scientific releases.
  execFileSync('python3', ['-B','-c', `
import runpy, sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]).parent))
module = runpy.run_path(sys.argv[1])
main = module['main']
main.__globals__['load_discovery'] = lambda root: {'examples': [{
    'id': 'fixture-run', 'problem_id': 'fixture-problem',
    'execution': {'name': {'ja': '試験実行', 'en': 'Fixture run'}},
    'keywords': ['fixture-execution'], 'outcome': {'ja': '保存結果', 'en': 'Stored result'},
}]}
main.__globals__['load_supplemental_examples'] = lambda root, ids: []
main(Path(sys.argv[2]))
`, join(root,'scripts/build-atlas-search.py'), directory], {cwd:directory,encoding:'utf8'});
  return JSON.parse(read(join(directory,'numerical-methods-atlas/home-search-index.json')));
}

test('rebuild follows published H1, sections and body after edits, additions and deletions, preserving scientific metadata', async t => {
  const directory = fixture();
  t.after(() => rmSync(directory,{recursive:true,force:true}));
  const protectedFiles = [
    'catalog/atlas-methods.json','catalog/atlas-test-problems.json','catalog/atlas-depth-expansion.json','catalog/atlas-detailed-reading.json',
    'numerical-methods-atlas/methods/index.json','numerical-methods-atlas/coverage.json','numerical-methods-atlas/translation-status.json',
    'numerical-methods-atlas/content.ja.json','numerical-methods-atlas/content.en.json',
    'numerical-methods-atlas/en/read/ordinary/index.json','numerical-methods-atlas/ja/read/ordinary/index.json',
  ];
  const before = protectedFiles.map(path => hash(join(directory,path)));
  const first = rebuild(directory);
  assert.ok(first.entries.some(entry => entry.chapter === 'deleted'));
  assert.ok(!JSON.stringify(first).includes('GhostSeedToken'));

  for (const language of ['ja','en']) {
    write(directory, chapterPath(language,'ordinary'), page(`Current <em>ordinary</em> &amp; title ${language}`,'<h2 id="current-section">Current <code>heading</code> &amp; section</h2><p>FreshBodyToken</p>',language));
    rmSync(join(directory,`numerical-methods-atlas/${language}/read/deleted`),{recursive:true});
    write(directory,chapterPath(language,'new-chapter'),page('NewChapterToken '+language,'<p>NewBodyToken</p>',language));
  }
  write(directory,chapterPath('en','english-only'),page('EnglishOnlyToken','<p>EnglishOnlyBodyToken</p>'));
  write(directory,chapterPath('ja','japanese-only'),page('日本語のみの章','<p>JapaneseOnlyBodyToken</p>','ja'));
  const index = rebuild(directory), ordinary = index.entries.find(entry => entry.chapter === 'ordinary');
  assert.deepEqual(ordinary.title,{ja:'Current ordinary & title ja',en:'Current ordinary & title en'});
  assert.deepEqual(ordinary.headings.en,[{level:2,id:'current-section',title:'Current heading & section'}]);
  assert.ok(ordinary.text.en.includes('FreshBodyToken'));
  assert.ok(ordinary.keywords.includes('coveragealias') && ordinary.keywords.includes('ordinarysynonym'));
  const canonical = index.entries.filter(entry => entry.kind === 'chapter');
  assert.deepEqual(canonical.map(entry => entry.chapter).sort(),['detailed','english-only','japanese-only','new-chapter','ordinary']);
  assert.equal(new Set(canonical.map(entry => entry.id)).size,canonical.length);
  assert.equal(canonical.find(entry => entry.chapter === 'detailed').id,'reading-detailed','legacy public chapter identity remains stable');
  assert.equal(canonical.find(entry => entry.chapter === 'detailed').origin,'detailed-reading');
  assert.equal(canonical.find(entry => entry.chapter === 'english-only').title.ja,null);
  assert.deepEqual(canonical.find(entry => entry.chapter === 'english-only').routes,{en:'/numerical-methods-atlas/en/read/english-only/'});
  for (const excluded of ['Initial ordinary title','InitialBodyToken','Initial section','Obsolete metadata','Obsolete per-chapter','Stale catalog title','GhostSeedToken','DeletedPageToken','DeletedBodyToken','HeaderExcludedToken','FooterExcludedToken','NavigationExcludedToken','SidebarExcludedToken','ScriptExcludedToken','HiddenExcludedToken','AriaHiddenExcludedToken']) {
    assert.ok(!JSON.stringify(index).includes(excluded),excluded+' is absent from regenerated search');
  }
  assert.deepEqual(protectedFiles.map(path => hash(join(directory,path))),before,'search generation never rewrites scientific catalogs, status or content metadata');
  const methods = JSON.parse(read(join(directory,'numerical-methods-atlas/methods/index.json'))).methods;
  assert.deepEqual(index.entries.find(entry => entry.id === 'registry-fixture-newton').method,methods[0]);
  assert.equal(index.entries.filter(entry => entry.origin === 'public-execution-discovery').length,1);
  const {searchChapters} = await import(pathToFileURL(join(directory,'numerical-methods-atlas/home-search.js')).href);
  for (const [query,chapter] of [['FreshBodyToken','ordinary'],['ordinarysynonym','ordinary'],['NewBodyToken','new-chapter']]) {
    assert.ok(searchChapters(index,query,'en').some(entry => entry.url === `/numerical-methods-atlas/en/read/${chapter}/`),query);
  }
  assert.equal(searchChapters(index,'EnglishOnlyToken','ja')[0].locale,'en');
  assert.equal(searchChapters(index,'JapaneseOnlyBodyToken','en')[0].url,'/numerical-methods-atlas/ja/read/japanese-only/');
  assert.deepEqual(searchChapters(index,'DeletedPageToken','en'),[]);
  const stable = read(join(directory,'numerical-methods-atlas/home-search-index.json'));
  rebuild(directory);
  assert.equal(read(join(directory,'numerical-methods-atlas/home-search-index.json')),stable,'an unchanged inventory rebuild is deterministic');
});

test('current public guides are discovered from HTML and their language sections stay separate', t => {
  const directory = fixture();
  t.after(() => rmSync(directory,{recursive:true,force:true}));
  const index = rebuild(directory);
  const guide = index.entries.find(entry => entry.id === 'public-resource-new-guide');
  assert.deepEqual(guide.title,{ja:'新しい案内',en:'New published guide'});
  assert.ok(guide.text.ja.includes('GuideJapaneseToken'));
  assert.ok(!guide.text.ja.includes('GuideEnglishToken'));
  assert.ok(guide.text.en.includes('GuideEnglishToken'));
  write(directory,'numerical-methods-atlas/new-guide/index.html','<main><section data-site-language="ja"><h1>改訂した案内</h1></section><section data-site-language="en"><h1>Revised guide</h1></section></main>');
  assert.equal(rebuild(directory).entries.find(entry => entry.id === guide.id).title.en,'Revised guide');
  rmSync(join(directory,'numerical-methods-atlas/new-guide'),{recursive:true});
  assert.ok(!rebuild(directory).entries.some(entry => entry.id === guide.id));
});
