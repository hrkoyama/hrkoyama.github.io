"""Single root-authorized boundary component checker; never launch a main trajectory."""
from datetime import datetime,timezone
import argparse,hashlib,json,os
from pathlib import Path
import shutil,signal,subprocess,time,traceback
D=Path(__file__).resolve().parent
S=Path('/private/tmp/codex-scratch-501/a2aacc1bcdece796d5ad47fc3786ce9899b64a42ed7a69a36d15782d9e5b1459/batch38-47/lbm')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def dump(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--protocol-sha256',required=True);parser.add_argument('--review',type=Path,required=True);parser.add_argument('--review-sha256',required=True);args=parser.parse_args()
 protocol=D/'protocol.json';plan=json.loads(protocol.read_text())
 if sha(protocol)!=args.protocol_sha256 or sha(args.review)!=args.review_sha256:raise ValueError('Explicitly reviewed protocol/review differs')
 bindings={str(D/name):value for name,value in plan['files_sha256'].items()}
 bindings.update({r['path']:r['sha256'] for r in plan['evidence'].values()})
 for path,value in bindings.items():
  if sha(path)!=value:raise ValueError('Frozen file changed: '+path)
 attempt=D/'attempt01'
 if attempt.exists():raise ValueError('Fresh single attempt required')
 attempt.mkdir();shutil.copyfile(protocol,attempt/'protocol.json');shutil.copyfile(args.review,attempt/'independent-review.json');shutil.copytree(D/'source',attempt/'source')
 for name in ['DERIVATION.md','reference-scope.json']:shutil.copyfile(D/name,attempt/name)
 receipt=dict(started_at_utc=now(),protocol_sha256=sha(protocol),review_sha256=sha(args.review),deadline_seconds=30,bindings=len(bindings),
 scope='Exactly one reviewed compile+single-step component qualification; no main physical trajectory or reference generation.',passed=False,timed_out=False)
 dump(attempt/'receipt.json',receipt);start=time.monotonic()
 command=[plan['execution']['pinned_python'],'-B','-W','error',str(D/'source/check_repair.py'),'--output',str(attempt/'results')];receipt['command']=command
 try:
  env=dict(os.environ,**plan['execution']['environment'],TMPDIR=str(S));S.mkdir(parents=True,exist_ok=True)
  with (attempt/'stdout.log').open('w') as stdout,(attempt/'stderr.log').open('w') as stderr:
   process=subprocess.Popen(command,cwd=D/'source',env=env,stdout=stdout,stderr=stderr,start_new_session=True)
   try:code=process.wait(timeout=30)
   except subprocess.TimeoutExpired:
    receipt['timed_out']=True;os.killpg(process.pid,signal.SIGTERM)
    try:process.wait(timeout=2)
    except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
    code=process.returncode
  receipt['returncode']=code
  result=json.loads((attempt/'results/result.json').read_text());receipt['checks']=result['check_count']
  receipt['passed']=bool(code==0 and not receipt['timed_out'] and result['passed'] is True and result['check_count']==87 and result['expected_checks']==87 and set(result['checks'])==set(plan['planned_check_names']) and all(v is True for v in result['checks'].values()))
 except Exception as error:
  receipt['failure']=dict(type=type(error).__name__,message=str(error));(attempt/'wrapper-traceback.txt').write_text(traceback.format_exc())
 receipt['changed_bound_files']=[path for path,value in bindings.items() if sha(path)!=value]
 receipt['passed']=bool(receipt['passed'] and not receipt['changed_bound_files'])
 receipt.update(elapsed_seconds=time.monotonic()-start,finished_at_utc=now());dump(attempt/'receipt.json',receipt);print(json.dumps(receipt),flush=True)
 return 0 if receipt['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
