import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
function python(source) {
  return execFileSync('python3', ['-B', '-c', source], {cwd:root, encoding:'utf8'});
}

test('knowledge-pack captures remain stable until source pages or extracted records change', () => {
  assert.match(python(String.raw`
import sys
sys.path.insert(0,'scripts')
from guide_snapshot import capture_stamp
pages=[{'url':'https://hrkoyama.github.io/numerical-methods-atlas/en/read/a/','sha256':'old'}]
records=[{'text':'original text'}]
old={'capturedAt':'2026-11-22T00:00:00+00:00','pages':pages,'records':records}
later='2026-11-23T00:00:00+00:00'
assert capture_stamp(old,list(pages),list(records),later)==old['capturedAt']
assert capture_stamp(old,[{**pages[0],'sha256':'new'}],records,later)==later
assert capture_stamp(old,pages,[{'text':'edited text'}],later)==later
assert capture_stamp(old,pages+[{**pages[0],'url':pages[0]['url']+'new/'}],records,later)==later
assert capture_stamp(None,pages,records,later)==later
print('source-sensitive capture checked')
`), /source-sensitive capture checked/);
});

test('both sitemaps follow additions, deletions and published canonicals on every rebuild', () => {
  assert.match(python(String.raw`
import importlib.util,pathlib,tempfile,xml.etree.ElementTree as ET
spec=importlib.util.spec_from_file_location('sitemap','scripts/build-sitemap.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as folder:
 root=pathlib.Path(folder)
 def page(name,url,extra=''):
  p=root/name;p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text('<html><head><link rel="canonical" href="'+url+'">'+extra+'</head><body>Public</body></html>')
 home='https://hrkoyama.github.io/'
 first=home+'numerical-methods-atlas/en/read/first/'
 second=home+'numerical-methods-atlas/en/read/second/'
 page('index.html',home)
 page('numerical-methods-atlas/en/read/first/index.html',first)
 page('docs/private.html',home+'hidden/')
 page('numerical-methods-atlas/hidden.html',home+'numerical-methods-atlas/hidden/','<meta name="robots" content="noindex">')
 def urls(name):return {n.text for n in ET.parse(root/name).findall('.//{*}loc')}
 m.build(root)
 assert urls('sitemap.xml')=={home,first}
 assert urls('numerical-methods-atlas/sitemap.xml')=={first}
 (root/'numerical-methods-atlas/en/read/first/index.html').unlink()
 page('numerical-methods-atlas/en/read/second/index.html',second)
 m.build(root)
 assert urls('sitemap.xml')=={home,second}
 assert urls('numerical-methods-atlas/sitemap.xml')=={second}
 before=(root/'sitemap.xml').read_bytes(),(root/'numerical-methods-atlas/sitemap.xml').read_bytes()
 m.build(root)
 assert before==((root/'sitemap.xml').read_bytes(),(root/'numerical-methods-atlas/sitemap.xml').read_bytes())
print('live sitemap inventory checked')
`), /live sitemap inventory checked/);
});

test('reading-directory titles follow the published chapter heading rather than stale metadata', () => {
  assert.match(python(String.raw`
import importlib.util,json,pathlib,tempfile
spec=importlib.util.spec_from_file_location('reading','scripts/build-atlas-reading-index.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as folder:
 atlas=pathlib.Path(folder);page=atlas/'en/read/example';page.mkdir(parents=True)
 (page/'index.html').write_text('<html><body><h1>Updated &amp; <em>verified</em> title</h1></body></html>')
 (page/'index.json').write_text(json.dumps({'title':'Old JSON title'}))
 documents={'en':{'example':{'title':'Old content title'}}}
 assert m.chapter_title(atlas,'example','en',documents)=='Updated & verified title'
 (page/'index.html').write_text('<html><body><h1>Renamed again</h1></body></html>')
 assert m.chapter_title(atlas,'example','en',documents)=='Renamed again'
print('published chapter title checked')
`), /published chapter title checked/);
});
