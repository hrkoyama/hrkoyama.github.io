import test from 'node:test';import assert from 'node:assert/strict';import{readFileSync}from'node:fs';import{createHash}from'node:crypto';import{execFileSync}from'node:child_process';import{fileURLToPath}from'node:url';
const root=new URL('../',import.meta.url),read=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(read(p)),hash=b=>createHash('sha256').update(b).digest('hex');
const cfg=json('catalog/atlas-rkdg-pilot.json'),base=cfg.route.slice(1),summary=json(base+'summary.json');
test('published pilot binds both actually qualified source identities without changing base r2',()=>{
 assert.equal(hash(readFileSync(new URL(cfg.archive.slice(1),root))),cfg.archive_sha256);
 assert.equal(hash(readFileSync(new URL(base+'summary.json',root))),cfg.summary_sha256);
 assert.equal(summary.cost.amount,null);assert.equal(summary.cost.lower_cost_comparison_performed,false);
 assert.equal(summary.prompt_language,'ja');assert.equal(summary.trials.length,2);
 const expected={assembly:['c8c6b11b688a50a3082a9dedb6b8a663b55a7cd5358aa4ac20166b672299cc2a',2,2949.834583],repair:['4ed984a01c42fe9bb657c09c61361b086682d6aa611e9f478bf996c0b29b81d4',1,2866.545312]};
 for(const trial of summary.trials){
  const e=expected[trial.trial];assert.equal(trial.candidate_sha256,e[0]);assert.equal(trial.solver_repairs,e[1]);assert.equal(trial.subject_reported_elapsed_seconds,e[2]);
  assert.deepEqual(trial.counts,{smooth:12,directional:24,double_mach:9,temporal:3,negative_controls:1});assert.equal(trial.waveform_diagnostics,4);assert.equal(trial.negative_control_rejected,true);assert.equal(trial.raw_scalar_comparisons,240);
  for(const name of ['original-verdict.json','waveform-verdict.json']){const v=json(base+'evidence/'+trial.trial+'/'+name);assert.equal(v.passed,true);assert.deepEqual(v.failures,[]);}
 }
 const release=json('numerical-methods-atlas/agent-kits/rkdg2d/manifest.json');assert.equal(release.archive.sha256,cfg.base_archive_sha256);assert.equal(release.release,'2026-11-23-r2');assert.equal(release.reflection_6_passed,false);
});
test('report is bilingual, scoped, searchable and reachable from the prompt page',()=>{
 const html=read(base+'index.html');
 for(const text of ['data-site-language="ja"','data-site-language="en"','49配列','240','約49分','約48分','About 49 min','About 48 min','NumPy2.0.2','OS-enforced','4eps','未取得','不合格','5/6'])assert.ok(html.includes(text),text);
 assert.ok(read('numerical-methods-atlas/agent-kits/rkdg2d/index.html').includes(cfg.route+'?lang=ja'));
 assert.ok(read('llms.txt').includes(cfg.route));for(const f of ['index.md','index-en.md'])assert.ok(read(base+f).includes('verify_saved.py'));
 assert.doesNotMatch(html,/\/Users\/|\/private\/|manuscript-private|library-file:/);
});
test('result ZIP preserves source/data hashes, includes all49 arrays and no private poster material',()=>{
 const result=JSON.parse(execFileSync('python3',['-c',String.raw`
import sys,zipfile,hashlib,json,re
with zipfile.ZipFile(sys.argv[1]) as z:
 prefix='atlas-rkdg-agent-pilot/'
 for line in z.read(prefix+'SHA256SUMS.txt').decode().splitlines():
  sha,name=line.split(maxsplit=1);assert hashlib.sha256(z.read(prefix+name)).hexdigest()==sha
 counts={}
 for t in ['assembly','repair']:
  counts[t]=len([n for n in z.namelist() if n.startswith(prefix+'trials/'+t+'/arrays/') and n.endswith('.npz')])
  meta=json.loads(z.read(prefix+'summary.json'));row=next(r for r in meta['trials'] if r['trial']==t)
  assert hashlib.sha256(z.read(prefix+row['source'])).hexdigest()==row['candidate_sha256']
 for n in z.namelist():
  assert not re.search(r'poster|private-qr|\.pptx$|\.pdf$|\.png$|\.jpg$',n,re.I)
  if n.endswith(('.md','.py','.json','.jsonl')):assert not re.search(r'/Users/|/private/|library-file:',z.read(n).decode())
 print(json.dumps(counts))
`,fileURLToPath(new URL(cfg.archive.slice(1),root))],{encoding:'utf8'}));
 assert.deepEqual(result,{assembly:49,repair:49});
});
