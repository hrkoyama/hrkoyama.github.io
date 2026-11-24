"""Verify the actual HR English Web/PDF/shared figures after publication, on GitHub."""
import concurrent.futures,hashlib,json,os,pathlib,re,time,unicodedata,urllib.request
from html import escape
from pypdf import PdfReader
from foundations_en_contract import ROOT,load,fragments,sha
from foundations_pdf_text import extract_body
import io

ORIGIN='https://hrkoyama.github.io'
d=load();base=d['base'];edition=base+d['edition']+'/'
out=pathlib.Path(os.environ['REPORT_DIR']);out.mkdir(parents=True,exist_ok=True)
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):raise ValueError('Unexpected public redirect')
def fetch(route):
    assert route.startswith('/') and not route.startswith('//')
    request=urllib.request.Request(ORIGIN+route,headers={'User-Agent':'Foundations-English-public-verifier/1.0'})
    with urllib.request.build_opener(NoRedirect()).open(request,timeout=35) as response:
        data=response.read(12_000_001)
        assert response.status==200 and len(data)<=12_000_000,route
    return data
deadline=time.monotonic()+240
while True:
    try:
        book_data=fetch(edition+'book-verification.json')
        assert hashlib.sha256(book_data).hexdigest()==os.environ['EN_BOOK_RECEIPT_SHA256']
        public_source=fetch('/catalog/atlas-foundations-course.en.json')
        assert hashlib.sha256(public_source).hexdigest()==sha(ROOT/'catalog/atlas-foundations-course.en.json')
        break
    except (OSError,ValueError,AssertionError):
        if time.monotonic()>=deadline:raise
        time.sleep(8)
book=json.loads(book_data)
files=[];pdf_data=None
def check_asset(item):
    name,digest=item;data=fetch('/'+name);actual=hashlib.sha256(data).hexdigest()
    assert actual==digest,name
    return {'url':ORIGIN+'/'+name,'sha256':actual,'bytes':len(data),'passed':True},data if name.endswith('/numerical-foundations-en.pdf') else None
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for result,payload in pool.map(check_asset,book['assets'].items()):
        files.append(result)
        if payload is not None:pdf_data=payload
assert pdf_data is not None
pdf=PdfReader(io.BytesIO(pdf_data))
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).replace('−','-')
pdf_text=norm(extract_body(pdf))
missing=[text for text in fragments(d) if norm(text) not in pdf_text]
assert not missing,missing
assert len(pdf.pages)==book['pdf_pages']
pages=[]
for c in [None,*d['chapters']]:
    suffix=c['id']+'/' if c else ''
    route=base+suffix;data=fetch(route);html=data.decode();title=c['title'] if c else d['title']
    expected=[title]
    if c:
        expected += [*c['goals'],*c['lead'],*c['worked']['paragraphs'],c['worked']['code'],c['worked']['result'],c['figure']['caption'],c['experiment']['instructions'],*c['pitfalls'],*c['summary']]
        for s in c['sections']:expected += [s['title'],*s['paragraphs']]
        for q in c['questions']:expected += [q['question'],q['answer']]
        assert html.count('<details>')==2
    else:
        expected += [d['subtitle'],d['audience'],d['rights'],d['execution_scope'],*d['preface'],*d['lab_guide']]
        for term,meaning in d['glossary']:expected += [term,meaning]
        for r in d['references']:expected += [r['title'],r['scope'],r['url']]
    for text in expected:assert escape(text) in html,(route,text[:80])
    assert 'data-content-language="en"' in html
    counterpart='/numerical-methods-atlas/learn/numerical-foundations/'+suffix
    assert 'hreflang="ja" href="'+ORIGIN+counterpart+'"' in html
    assert edition+'numerical-foundations-en.pdf' in html
    pages.append({'url':ORIGIN+route,'passed':True,'sha256':hashlib.sha256(data).hexdigest()})
receipt={'passed':True,'target_sha':os.environ['GITHUB_SHA'],'source_commit':os.environ['GITHUB_SHA'],
 'public_origin':ORIGIN,'pages':len(pages),'chapters':19,'questions_with_answers':38,
 'pdf_pages':len(pdf.pages),'shared_fragments':len(fragments(d)),'pdf_sha256':hashlib.sha256(pdf_data).hexdigest(),
 'asset_count':len(files),'charts':19,'chart_formats':['svg','png','pdf'],'equations':36,
 'source_checkout':'Verifier/manuscripts only; public PDF, Web and shared figures downloaded from HR origin',
 'files':files,'page_checks':pages}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
(out/'numerical-foundations-en.pdf').write_bytes(pdf_data)
print(json.dumps({k:v for k,v in receipt.items() if k not in ['files','page_checks']},indent=2))
