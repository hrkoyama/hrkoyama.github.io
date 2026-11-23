#!/usr/bin/env python3
"""Verify the published pilot ZIP and reassess stored evidence, never evolve PDEs."""
from pathlib import Path,PurePosixPath
import argparse,json,hashlib,urllib.request,urllib.error,zipfile,stat,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1];ORIGIN='https://hrkoyama.github.io'
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args):raise ValueError('Unexpected redirect')
def fetch(url,limit):
 assert url.startswith(ORIGIN+'/')
 with urllib.request.build_opener(NoRedirect()).open(urllib.request.Request(url,headers={'User-Agent':'Atlas-RKDG-pilot-public-verifier/1.0'}),timeout=40) as f:b=f.read(limit+1)
 assert len(b)<=limit;return b
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--wait-seconds',type=int,default=0);a=p.parse_args()
 cfg=json.loads((ROOT/'catalog/atlas-rkdg-pilot.json').read_text());expected=(ROOT/cfg['route'].lstrip('/')/'manifest.json').read_bytes();a.output.mkdir(parents=True,exist_ok=False)
 deadline=time.monotonic()+a.wait_seconds
 while True:
  try:
   data=fetch(ORIGIN+cfg['route']+'manifest.json',1000000);assert data==expected;break
  except (OSError,ValueError,AssertionError,urllib.error.URLError):
   if time.monotonic()>=deadline:raise
   time.sleep(min(10,max(0,deadline-time.monotonic())))
 b=fetch(ORIGIN+cfg['archive'],64*1024*1024);assert sha(b)==cfg['archive_sha256'] and len(b)==cfg['archive_bytes'];archive=a.output/'results.zip';archive.write_bytes(b)
 with zipfile.ZipFile(archive) as z:
  for i in z.infolist():
   name=PurePosixPath(i.filename);assert not name.is_absolute() and '..' not in name.parts and name.parts[0]=='atlas-rkdg-agent-pilot';assert not stat.S_ISLNK(i.external_attr>>16)
  z.extractall(a.output)
 bundle=a.output/'atlas-rkdg-agent-pilot'
 for line in (bundle/'SHA256SUMS.txt').read_text().splitlines():
  digest,name=line.split(maxsplit=1);rel=PurePosixPath(name);assert not rel.is_absolute() and '..' not in rel.parts;assert sha((bundle/name).read_bytes())==digest
 assert sha((a.base/'SHA256SUMS.txt').read_bytes())==cfg['base_sha256sums_sha256']
 results=[]
 for trial in ['assembly','repair']:
  cmd=[sys.executable,str(bundle/'verify_saved.py'),'--trial',trial,'--base',str(a.base.resolve()),'--output',str((a.output/'audit').resolve())]
  r=subprocess.run(cmd,capture_output=True,text=True)
  (a.output/(trial+'.stdout')).write_text(r.stdout);(a.output/(trial+'.stderr')).write_text(r.stderr)
  result={'trial':trial,'exit_code':r.returncode};results.append(result);assert r.returncode==0,r.stderr
 report={'passed':True,'archive_sha256':sha(b),'new_pde_runs':0,'trials':results,'scope':'Published saved-data reassessment, not new AI generation or a fresh full PDE campaign.'}
 (a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
