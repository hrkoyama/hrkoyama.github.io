#!/usr/bin/env python3
"""Index only published, same-site HTML and explicitly allowlisted public metadata."""
from pathlib import Path
from compact_search import write_compact
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
from atlas_search_methods import search_methods,version_method_search,version_navigation_imports
import re,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://hrkoyama.github.io'
CATEGORIES={
 'astronomy-step-by-step':('宇宙物理の教材','Astrophysics'),
 'numerical-methods-atlas':('数値解析','Numerical methods'),
 'the-art-of-thermal-instability':('熱的不安定性','Thermal instability'),
 'notebooks':('大学ノート','College Notes'),
 'gordon-bell':('ゴードンベル賞','Gordon Bell archive'),
 'hpci-policy':('計算科学政策','Computing policy'),
 'guide':('研究相談','Research Compass'),
 'academic-roots':('学術系譜','Academic Roots'),
 'other':('プロフィール・利用条件','Profile & site information')
}
class PublicText(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.stack=[];self.parts=[];self.headings=[];self.title=[];self.titles={};self.document_lang='ja';self.content_lang='';self.sections=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.document_lang=a.get('lang','ja')
  if tag=='body':self.content_lang=a.get('data-content-language','')
  if a.get('data-site-language'):self.sections.add(a['data-site-language'])
  if tag=='title' and any(entry[0]=='head' for entry in self.stack):self.titles={lang:a.get('data-page-title-'+lang,'') for lang in ['ja','en']}
  parent=self.stack[-1] if self.stack else ('',False,False)
  inside=parent[1] or tag=='main'
  blocked=parent[2] or tag in {'script','style','noscript','nav','header','footer','button','input','textarea','select','option','svg','canvas','template','annotation','annotation-xml'} or bool(set(a.get('class','').split()) & {'site-chrome','search-navigation','execution-resource-navigation','method-route-navigation','problem-routes'})
  if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append((tag,inside,blocked))
  if inside and not blocked and tag in {'p','h1','h2','h3','h4','li','tr','section','article','br','div'}:self.parts.append(' ')
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:del self.stack[i:];break
  if tag in {'p','h1','h2','h3','h4','li','tr','section','article','div'}:self.parts.append(' ')
 def handle_data(self,text):
  if any(entry[0]=='head' for entry in self.stack) and any(entry[0]=='title' for entry in self.stack):self.title.append(text)
  if self.stack and self.stack[-1][1] and not self.stack[-1][2]:
   self.parts.append(text)
   if any(entry[0] in {'h1','h2','h3'} for entry in self.stack):self.headings.append(text+' ')
def flatten(value):
 if isinstance(value,dict):return ' '.join(flatten(v) for k,v in value.items() if k not in {'url','reference_url','local_path','source','image','thumb','doi','sha256'} and not k.endswith('_url'))
 if isinstance(value,list):return ' '.join(map(flatten,value))
 return str(value) if value is not None and not isinstance(value,bool) else ''
def record(url,title,title_en,text,lang,category):
 ja,en=CATEGORIES[category]
 return {'url':url,'title':title,'titleEn':title_en,'text':re.sub(r'\s+',' ',text).strip(),'lang':lang,'categoryJa':ja,'categoryEn':en,'categoryText':ja+' '+en}
documents=[]
navigation=json.loads((ROOT/'search/atlas-navigation.json').read_text())
method_records={urlparse(method['url']).path:method for method in search_methods(ROOT,navigation)}
atlas_index=json.loads((ROOT/'numerical-methods-atlas/home-search-index.json').read_text())
execution_records={urlparse(entry['routes']['en']).path:entry for entry in atlas_index['entries'] if entry.get('kind')=='execution-example'}
atlas_records={}
for entry in atlas_index['entries']:
 if 'search_navigation' not in entry:continue
 for route in entry['routes'].values():
  parsed_route=urlparse(route)
  # Equation/reference entities share an index page but keep distinct fragments.
  if parsed_route.fragment:continue
  previous=atlas_records.get(parsed_route.path)
  if previous is not None and previous['search_navigation']!=entry['search_navigation']:
   raise ValueError('Conflicting canonical atlas navigation: '+parsed_route.path)
  atlas_records[parsed_route.path]=entry
urls=sorted({node.text for node in ET.parse(ROOT/'sitemap.xml').findall('.//{*}loc')})
for url in urls:
 parsed=urlparse(url)
 assert parsed.scheme=='https' and parsed.netloc=='hrkoyama.github.io' and not parsed.query and not parsed.fragment,url
 if parsed.path in ['/search/','/notebooks/notebook.html']:continue
 path=ROOT/unquote(parsed.path).lstrip('/')
 if path.is_dir():path=path/'index.html'
 assert path.is_file(),url
 if path.suffix!='.html':continue
 parser=PublicText();parser.feed(re.sub(r'(<\/?h)\s+([1-6])',r'\1\2',path.read_text()))
 text=''.join(parser.parts).strip();title=parser.titles.get('ja') or ''.join(parser.title).strip()
 if not title or not text:raise ValueError('Missing public main text: '+url)
 category=parsed.path.split('/')[1]
 if category not in CATEGORIES:category='other'
 lang='both' if parser.sections=={'ja','en'} or parsed.path in ['/guide/','/numerical-methods-atlas/'] or parsed.path.startswith('/hpci-policy/') else parser.content_lang or parser.document_lang
 if '/ja/' in parsed.path:lang='ja'
 if '/en/' in parsed.path:lang='en'
 if parsed.path=='/gordon-bell/':text+=' '+flatten(json.loads((ROOT/'gordon-bell/data.json').read_text()))
 if parsed.path=='/hpci-policy/':
  for name in ['content.json','committees.json','comparison.json']:text+=' '+flatten(json.loads((ROOT/'hpci-policy'/name).read_text()))
 if parsed.path=='/hpci-policy/history.html':text+=' '+flatten(json.loads((ROOT/'hpci-policy/history.json').read_text()))
 doc=record(parsed.path,title,parser.titles.get('en',''),text,lang,category);doc['headings']=''.join(parser.headings).strip()
 if parsed.path in method_records:doc['method']=method_records[parsed.path]
 if parsed.path in execution_records:doc['execution']=execution_records[parsed.path]
 if parsed.path in atlas_records:
  entry=atlas_records[parsed.path]
  doc['kind']=entry['kind'];doc['routes']=entry['routes'];doc['search_navigation']=entry['search_navigation']
 documents.append(doc)
for entity in navigation['entities']:
 kind=entity['kind']
 if kind not in {'equation','reference'}:raise ValueError('Unexpected fragment entity: '+entity['id'])
 identity=entity['id'].removeprefix(kind+'-')
 route=entity['routes'].get('ja') or entity['routes']['en']
 parsed_route=urlparse(route)
 if parsed_route.netloc and (parsed_route.scheme!='https' or parsed_route.netloc!='hrkoyama.github.io'):
  raise ValueError('Non-public search entity route: '+route)
 if not parsed_route.path.startswith('/numerical-methods-atlas/') or not parsed_route.fragment:
  raise ValueError('Missing atlas entity fragment: '+route)
 # The source-built entity text contains only this definition and its notes.
 # Never reuse all of the neighboring equation/reference index page's prose.
 text=' '.join([flatten(entity['title']),flatten(entity.get('text',{})),flatten(entity.get('keywords',[])),flatten(entity.get('headings',{}))])
 doc=record(parsed_route.path+('?' + parsed_route.query if parsed_route.query else '')+'#'+parsed_route.fragment,
            entity['title'].get('ja') or entity['title']['en'],entity['title'].get('en',''),text,'both','numerical-methods-atlas')
 doc.update({'id':entity['id'],'kind':kind,'routes':entity['routes'],
             'snippet':entity.get('snippet',{}),
             'headings':flatten(entity.get('headings',{})),
             'search_navigation':navigation['nodes'][kind+':'+identity]})
 documents.append(doc)
raw=(ROOT/'notebooks/catalog.js').read_text()
notebooks=json.loads(raw.split('=',1)[1].strip().removesuffix(';'))['notebooks']
for notebook in notebooks:
 fields={key:notebook.get(key) for key in ['display_title','lecture_title','lecturer','lecture_period','lecture_year','lecture_year_basis','notes']}
 fields['related_materials']=[{key:material.get(key) for key in ['title','creator','label']} for material in notebook.get('related_materials',[])]
 assert re.fullmatch(r'n[0-9]+',notebook['id'])
 text='大学ノート 自筆ノート 講義ノート College Notes Handwritten lecture notebook '+flatten(fields)
 documents.append(record('/notebooks/notebook.html?id='+notebook['id'],notebook.get('lecture_title') or notebook['display_title'],'',text,'ja','notebooks'))
assert len({doc['url'] for doc in documents})==len(documents)
assert all(not re.search(r'koyam(?:arium|ahr)@gmail[.]com',doc['text']) for doc in documents)
inputs={'sitemap.xml','notebooks/catalog.js','gordon-bell/data.json'}
inputs.add('numerical-methods-atlas/methods/index.json')
inputs.add('numerical-methods-atlas/home-search-index.json')
inputs.add('search/atlas-navigation.json')
inputs.update('hpci-policy/'+name for name in ['content.json','committees.json','comparison.json','history.json'])
for url in urls:
 parsed=urlparse(url)
 if parsed.path in ['/search/','/notebooks/notebook.html']:continue
 path=ROOT/unquote(parsed.path).lstrip('/')
 if path.is_dir():path=path/'index.html'
 if path.suffix=='.html':inputs.add(path.relative_to(ROOT).as_posix())
receipts={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(inputs)}
source_data={'version':1,'documents':documents,'sourceSha256':receipts,'navigation_source_sha256':navigation['source_sha256']}
data=json.dumps(source_data,ensure_ascii=False,separators=(',',':'))+'\n'
(ROOT/'search/index.json').write_text(data)
compact_path=write_compact(ROOT,source_data,'site')
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:12]
js=ROOT/'search/search.js'
shared=ROOT/'search/method-search.mjs'
shared_hash=version_method_search(ROOT)
for module in [ROOT/'search/engine.mjs',js]:
 text=re.sub(r"from './method-search[.]mjs(?:\?v=[a-f0-9]+)?'","from './method-search.mjs?v="+shared_hash+"'",module.read_text())
 module.write_text(version_navigation_imports(ROOT,text))
js.write_text(re.sub(r"from './engine\.mjs(?:\?v=[a-f0-9]+)?'", "from './engine.mjs?v="+digest(ROOT/'search/engine.mjs')+"'",js.read_text()))
page=ROOT/'search/index.html';html=page.read_text()
for name in ['search.js','search.css']:
 html=re.sub(r'(/search/'+re.escape(name)+r')(?:\?v=[a-f0-9]+)?',r'\1?v='+digest(ROOT/'search'/name),html)
html=re.sub(r'data-search-index="[^"]+"','data-search-index="/search/query-index.json?v='+digest(compact_path)+'"',html)
html=re.sub(r'\sdata-atlas-search-index="[^"]*"|\sdata-search-count="[^"]*"|\sdata-atlas-search-count="[^"]*"','',html)
atlas_compact=ROOT/'search/atlas-query-index.json'
atlas_count=len(atlas_index['entries'])
html=html.replace('data-search-index="','data-atlas-search-index="/search/atlas-query-index.json?v='+digest(atlas_compact)+'" data-search-count="'+str(len(documents))+'" data-atlas-search-count="'+str(atlas_count)+'" data-search-index="',1)
page.write_text(html)
print('Built site search:',len(documents),'public pages/resources;',len(data.encode()),'bytes;',len(notebooks),'notebook records. No PDF/image OCR or external content.')
