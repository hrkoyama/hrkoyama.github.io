import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../',import.meta.url));
const fixture = String.raw`
import importlib.util,json,pathlib,sys,tempfile
from html import escape
import xml.etree.ElementTree as ET

spec=importlib.util.spec_from_file_location('atlas_indexes',pathlib.Path('scripts/check-atlas-indexes.py'))
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
ORIGIN='https://hrkoyama.github.io'

def write(root,path,value):
    target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(value)

def page(root,route,title,body=''):
    write(root,route.strip('/')+'/index.html' if route!='/' else 'index.html',
          '<!doctype html><html><head><link rel="canonical" href="'+ORIGIN+route+'"></head><body><main><h1>'+escape(title)+'</h1>'+body+'</main></body></html>')

def sitemap(root,path,urls):
    document=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for url in sorted(urls):ET.SubElement(ET.SubElement(document,'url'),'loc').text=url
    write(root,path,ET.tostring(document,encoding='unicode'))

def seed(root):
    chapters={'common':{'ja':'共通の章','en':'Common chapter'},'english-only':{'en':'English only'}}
    urls={'/','/numerical-methods-atlas/'}
    page(root,'/','Home');page(root,'/numerical-methods-atlas/','Atlas')
    for chapter,editions in chapters.items():
        for language,title in editions.items():
            route='/numerical-methods-atlas/'+language+'/read/'+chapter+'/'
            page(root,route,title);urls.add(route)
    for language in ['ja','en']:
        rows=[];links=[];markdown=[]
        for chapter,editions in chapters.items():
            edition=language if language in editions else 'en'
            route='/numerical-methods-atlas/'+edition+'/read/'+chapter+'/'
            rows.append(dict(id=chapter,title=editions[edition],url=route,language=edition,available_languages=list(editions)))
            links.append('<a href="'+route+'"><span>'+escape(editions[edition])+'</span><span aria-hidden="true">→</span></a>')
            markdown.append('- ['+editions[edition]+']('+ORIGIN+route+')')
        route='/numerical-methods-atlas/'+language+'/read/';urls.add(route)
        page(root,route,'Contents',''.join(links))
        write(root,route.strip('/')+'/index.json',json.dumps(dict(language=language,chapter_count=2,groups=[dict(chapters=rows)])))
        write(root,route.strip('/')+'/index.md','\n'.join(markdown)+'\n')
    write(root,'numerical-methods-atlas/home-overview-data.js','export const homeReadingLanguages = '+json.dumps({chapter:list(editions) for chapter,editions in chapters.items()})+';\n')
    entries=[dict(id=chapter,chapter=chapter,kind='chapter',title={language:editions.get(language) for language in ['ja','en']},
                  routes={language:'/numerical-methods-atlas/'+language+'/read/'+chapter+'/' for language in editions}) for chapter,editions in chapters.items()]
    # A resource may have its own label while pointing to a chapter. It is not a second canonical chapter entry.
    entries.append(dict(id='resource-alias',kind='resource',title={'en':'A different resource label'},routes={'en':'/numerical-methods-atlas/en/read/common/'}))
    write(root,'numerical-methods-atlas/home-search-index.json',json.dumps(dict(entries=entries)))
    sitemap(root,'sitemap.xml',[ORIGIN+url for url in urls])
    sitemap(root,'numerical-methods-atlas/sitemap.xml',[ORIGIN+url for url in urls if url.startswith('/numerical-methods-atlas/')])

with tempfile.TemporaryDirectory(prefix='atlas-index-fixture-') as directory:
    root=pathlib.Path(directory);seed(root)
    exec(sys.argv[1])
    print(json.dumps(module.audit(root)))
`;

function run(mutation='') {
  return JSON.parse(execFileSync('python3',['-B','-c',fixture,mutation],{cwd:root,encoding:'utf8'}));
}

function hasError(result, phrase) {
  assert.ok(result.errors.some(error => error.includes(phrase)),phrase+'\n'+result.errors.join('\n'));
}

test('a tiny valid bilingual inventory includes an English fallback and checking never changes its files', () => {
  const result = run(String.raw`
before={str(path.relative_to(root)):path.read_bytes() for path in root.rglob('*') if path.is_file()}
assert module.check(root)==[]
after={str(path.relative_to(root)):path.read_bytes() for path in root.rglob('*') if path.is_file()}
assert before==after
`);
  assert.equal(result.chapters,2);
  assert.equal(result.chapter_editions,3);
  assert.deepEqual(result.errors,[]);
});

test('changing a published title rejects independently stale HTML, JSON, Markdown and chapter search', () => {
  const result = run(String.raw`
path=root/'numerical-methods-atlas/ja/read/common/index.html'
path.write_text(path.read_text().replace('共通の章','改訂された章'))
`);
  for (const suffix of ['html','json','md']) hasError(result,'ja/read/index.'+suffix+': stale title for common');
  hasError(result,'home-search-index.json: stale ja title for common');
});

test('an added English-only chapter cannot disappear from any reading inventory or sitemap', () => {
  const result = run("page(root,'/numerical-methods-atlas/en/read/new-chapter/','New chapter')");
  for (const language of ['ja','en']) for (const suffix of ['html','json','md']) hasError(result,language+'/read/index.'+suffix);
  for (const name of ['home-overview-data.js','home-search-index.json chapter IDs','sitemap.xml','numerical-methods-atlas/sitemap.xml']) hasError(result,name);
  assert.ok(result.errors.some(error => error.includes('new-chapter')));
});

test('deleted chapters are rejected rather than retained in append-only generated lists', () => {
  const result = run(String.raw`
for language in ['ja','en']:(root/('numerical-methods-atlas/'+language+'/read/common/index.html')).unlink()
`);
  for (const name of ['ja/read/index.html','en/read/index.json IDs','home-overview-data.js','home-search-index.json chapter IDs','numerical-methods-atlas/sitemap.xml']) hasError(result,name);
  assert.ok(result.errors.some(error => error.includes('extra=[')&&error.includes('common')));
});

test('a hand-edited HTML title fails even when JSON, Markdown and metadata remain unchanged', () => {
  const result = run(String.raw`
path=root/'numerical-methods-atlas/en/read/index.html'
path.write_text(path.read_text().replace('Common chapter','Pinned obsolete label'))
`);
  assert.deepEqual(result.errors,['numerical-methods-atlas/en/read/index.html: stale title for common']);
});

test('a missing translation must use its actual published edition and language availability', () => {
  const result = run(String.raw`
path=root/'numerical-methods-atlas/ja/read/index.json';data=json.loads(path.read_text())
entry=data['groups'][0]['chapters'][1]
entry.update(url='/numerical-methods-atlas/ja/read/english-only/',language='ja',available_languages=['ja','en'])
path.write_text(json.dumps(data))
`);
  hasError(result,'incorrect edition route for english-only');
  hasError(result,'stale available languages for english-only');
});

test('both canonical chapter duplication and wrong route targets are detected', () => {
  const result = run(String.raw`
path=root/'numerical-methods-atlas/home-search-index.json';data=json.loads(path.read_text())
data['entries'][0]['routes']['en']='/numerical-methods-atlas/en/read/ghost/'
data['entries'].append(data['entries'][0].copy());path.write_text(json.dumps(data))
`);
  hasError(result,'duplicate canonical chapter entries');
  hasError(result,'incorrect en route for common');
});

test('root sitemap coverage also includes new canonical pages outside the atlas', () => {
  const result = run("page(root,'/about/','About')");
  assert.equal(result.errors.length,1);
  hasError(result,'sitemap.xml: inventory differs; missing=[https://hrkoyama.github.io/about/]');
});

test('duplicate sitemap URLs fail even when their set of targets is complete', () => {
  const result = run(String.raw`
path=root/'numerical-methods-atlas/sitemap.xml';tree=ET.parse(path)
urls=[node.text for node in tree.findall('.//{*}loc')]
sitemap(root,'numerical-methods-atlas/sitemap.xml',urls+[urls[0]])
`);
  assert.deepEqual(result.errors,['numerical-methods-atlas/sitemap.xml: duplicate canonical URLs']);
});
