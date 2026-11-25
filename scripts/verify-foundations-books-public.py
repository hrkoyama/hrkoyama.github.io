"""Thin actual-HR delivery check for already QA-verified new print editions.

Full text/font/layout/visual checks belong to the hash-bound book QA receipt.
This checker verifies identical public bytes, metadata and primary download links.
It does not rerun calculations, render or reinterpret text to bypass QA failures.
"""
import argparse,hashlib,json,re,time
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import HTTPRedirectHandler,ProxyHandler,Request,build_opener
from foundations_books import REGISTRY,load_book_chain,need,relative
ORIGIN='https://hrkoyama.github.io'
def sha(raw):return hashlib.sha256(raw).hexdigest()
class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args):return None
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':self.links.append(dict(attrs))
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--registry-sha256',required=True);p.add_argument('--target-sha',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    need(re.fullmatch('[0-9a-f]{64}',a.registry_sha256) and re.fullmatch('[0-9a-f]{40}',a.target_sha),'Exact actual registry/source SHA required')
    output=a.output.resolve();checkout=Path(__file__).resolve().parents[1];need(not output.is_relative_to(checkout) and not output.exists(),'Fresh verification output outside checkout required');output.mkdir(parents=True)
    report={'schema_version':1,'passed':False,'target_sha':a.target_sha,'public_origin':ORIGIN,'kind':'new-foundations-book-delivery-only','started_at_utc':datetime.now(timezone.utc).isoformat(),'files':[],'fresh_full_text_font_or_visual_QA':False,'frozen_QA_proof_required':True,'numerical_execution':False};deadline=time.monotonic()+180;cache={}
    def fetch(name):
        relative(name)
        if name in cache:return cache[name]
        url=ORIGIN+'/'+quote(name,safe='/')+'?sha='+a.target_sha;cap=5*1024*1024 if name.endswith('.pdf') else 2*1024*1024
        need(time.monotonic()<deadline,'Public-book delivery deadline exceeded')
        with build_opener(ProxyHandler({}),NoRedirect()).open(Request(url,headers={'User-Agent':'Foundations-book-public-delivery/1','Accept-Encoding':'identity'}),timeout=min(20,deadline-time.monotonic())) as response:
            raw=response.read(cap+1);need(response.status==200 and len(raw)<=cap and response.geturl()==url,'Invalid/redirected/oversized public response')
        report['files'].append({'url':url,'sha256':sha(raw),'bytes':len(raw)});cache[name]=raw;return raw
    try:
        # Wait only for the exact new registry. No old-edition or prior-SHA success shortcut.
        while True:
            try:raw=fetch(REGISTRY);need(sha(raw)==a.registry_sha256,'Registry not yet deployed');break
            except (OSError,ValueError):
                cache.pop(REGISTRY,None);need(time.monotonic()+2<deadline,'Current public book registry did not arrive');time.sleep(2)
        books=load_book_chain(fetch);report['registry_sha256']=a.registry_sha256
        for language in ['ja','en']:
            row=books['primary'][language];route=row['web'].lstrip('/')+'index.html';html=fetch(route).decode();block=re.search(r'<div class="downloads">(.*?)</div>',html,re.S);need(block is not None,'Course downloads block missing');parser=Links();parser.feed(block[1])
            href='/'+row['pdf']['path'];need(parser.links and parser.links[0].get('href')==href,'New PDF is not the primary course download')
            need(any(x.get('href')=='/'+row['previous_pdf']['path'] for x in parser.links),'Old PDF alternate link missing')
        home=json.loads(fetch('catalog/atlas-home.json'))
        for language in ['ja','en']:need(home['landing'][language]['beginner']['pdf']['href']=='/'+books['primary'][language]['pdf']['path'],'Homepage PDF source points to wrong edition')
        report.update(passed=True,layout_edition=books['current_layout_edition'],pdfs={language:books['primary'][language]['pdf'] for language in ['ja','en']})
    except BaseException as error:report['failure']={'type':type(error).__name__,'message':str(error)}
    finally:
        report['completed_at_utc']=datetime.now(timezone.utc).isoformat();dest=output/'receipt.json';dest.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':report['passed'],'receipt':str(dest)}));return 0 if report['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
