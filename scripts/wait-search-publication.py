#!/usr/bin/env python3
"""Wait for this checkout's reviewed search assets at the sole publication origin."""
import datetime,gzip,hashlib,json,pathlib,time,urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
FILES=['numerical-methods-atlas/index.html','search/index.html','search/atlas-query-index.json','search/search.js','numerical-methods-atlas/home-search.js','numerical-methods-atlas/code-and-data/examples/index.html']
def main():
    expected={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in FILES}
    deadline=time.monotonic()+360;attempts=0;last=[]
    while True:
        attempts+=1;rows=[]
        try:
            for path,digest in expected.items():
                req=urllib.request.Request('https://hrkoyama.github.io/'+path,headers={'User-Agent':'Atlas-search-public-performance','Accept-Encoding':'gzip','Cache-Control':'no-cache'})
                with urllib.request.urlopen(req,timeout=30) as response:
                    raw=response.read((ROOT/path).stat().st_size+1_000_000)
                    if response.headers.get('Content-Encoding')=='gzip':raw=gzip.decompress(raw)
                actual=hashlib.sha256(raw).hexdigest();rows.append({'path':path,'sha256':actual,'passed':actual==digest})
            if all(r['passed'] for r in rows):break
        except OSError as error:rows.append({'passed':False,'error':type(error).__name__})
        last=rows
        if time.monotonic()>=deadline:raise RuntimeError('Expected HR search publication not reached: '+json.dumps(last))
        print('Waiting for matching public search assets, attempt',attempts,flush=True);time.sleep(10)
    out=ROOT/'test-results/search-performance';out.mkdir(parents=True,exist_ok=True)
    (out/'public-version-check.json').write_text(json.dumps({'passed':True,'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attempts':attempts,'origin':'https://hrkoyama.github.io','files':rows},indent=2)+'\n')
if __name__=='__main__':main()
