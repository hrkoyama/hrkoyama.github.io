import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

// Isolate only the production metadata function. The canonical packet loader is
// stubbed with tiny, explicit records; this suite does not qualify scientific code.
const repo = process.env.ATLAS_TEST_REPO || process.cwd();
const source = path.join(repo, 'scripts/atlas_equation_availability.py');
const python = process.env.ATLAS_STATIC_PYTHON || 'python3';
const sourceSha256 = createHash('sha256').update(readFileSync(source)).digest('hex');
if (process.env.ATLAS_EXPECT_SOURCE_SHA256) assert.equal(sourceSha256, process.env.ATLAS_EXPECT_SOURCE_SHA256);
const program = String.raw`
import ast, copy, hashlib, json, os, sys, tempfile
from pathlib import Path
from urllib.parse import urlsplit
from hashlib import sha256
source=Path(sys.argv[1]); raw=source.read_bytes()
assert os.environ['ATLAS_EXPECT_SOURCE_SHA256']==sha256(raw).hexdigest(), 'Source changed before fixture execution'
module=ast.parse(raw); funcs=[x for x in module.body if isinstance(x,ast.FunctionDef) and x.name=='equation_evidence']
assert len(funcs)==1
isolated=compile(ast.Module(body=funcs,type_ignores=[]),str(source),'exec')
def dump(p,v):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False))

def check(mode):
 with tempfile.TemporaryDirectory(prefix='equation-provenance-') as tmp:
  root=Path(tmp); scope={'ja':'固定例の範囲','en':'Scope of the fixed example'}
  survey_path='numerical-methods-atlas/assets/biological-models.json'
  survey={'models':[{'id':'legacy','status':'scoped-educational-example','execution_examples':['legacy-run'],'supplemental_examples':[],'implementation_scope':scope},{'id':'reading','status':'reading','execution_examples':[],'supplemental_examples':[]}]}
  dump(root/survey_path,survey)
  p='code/validated-examples/2000-01-01/reaction/cases.json'
  metadata=[{'id':'reaction-example','formulas':['f(x)=x+x^2']},{'id':'different-case','formulas':['f(x)=x+x^2']}]
  if mode=='dict-root': metadata={'cases':metadata}
  dump(root/p,metadata); digest=sha256((root/p).read_bytes()).hexdigest()
  formula={'kind':'verified-supplement','case_id':'reaction-example','path':p,'sha256':digest,'json_pointer':'/cases/0/formulas/0' if mode=='dict-root' else '/0/formulas/0','source_formula':'f(x)=x+x^2'}
  legacy={'id':'bio-legacy','group':'biology','status':'local-example','supplemental_examples':[],'formula_source':{'path':survey_path,'model_id':'legacy'},'execution_scope':scope}
  reading={'id':'bio-reading','group':'biology','status':'reading','supplemental_examples':[],'formula_source':{'path':survey_path,'model_id':'reading'}}
  new={'id':'reaction-model','group':'biology','status':'local-example','supplemental_examples':['reaction-example'],'formula_source':formula,'execution_scope':copy.deepcopy(scope)}
  equations=[legacy,reading,new]; common={'id':'legacy-run','equation_ids':['bio-legacy']}; discovery={'examples':[common]}
  example={'id':'reaction-example','formulas':['f(x)=x+x^2'],'source_sha256':{p:digest}}
  if mode=='legacy-scope': legacy['execution_scope']={'ja':'別','en':'Different'}
  elif mode=='legacy-status': legacy['status']='reading'
  elif mode=='reading-borrow': common['equation_ids'].append('bio-reading')
  elif mode=='survey-opt-out': new['id']='bio-reaction'
  elif mode=='unknown-kind': legacy['formula_source']['kind']='unrecognized'
  elif mode=='new-unknown-kind': formula['kind']='unrecognized'
  elif mode=='missing-provenance': del new['formula_source']
  elif mode=='unselected': new['supplemental_examples']=[]
  elif mode=='repeated-selected': new['supplemental_examples']*=2
  elif mode=='declared-stale-sha': formula['sha256']='0'*64
  elif mode=='actual-stale-bytes': (root/p).write_bytes((root/p).read_bytes()+b'\n')
  elif mode=='unbound-path': formula['path']='code/validated-examples/2000-01-01/other/cases.json'
  elif mode=='wrong-case': formula['json_pointer']='/1/formulas/0'
  elif mode=='negative-index': formula['json_pointer']='/-1/formulas/0'
  elif mode=='leading-zero-index': formula['json_pointer']='/00/formulas/0'
  elif mode=='leading-zero-formula': formula['json_pointer']='/0/formulas/00'
  elif mode=='extra-pointer-token': formula['json_pointer']='/0/formulas/0/extra'
  elif mode=='wrong-pointer-field': formula['json_pointer']='/0/not_formulas/0'
  elif mode=='escaped-pointer': formula['json_pointer']='/0/formulas/~0'
  elif mode=='wrong-formula': formula['source_formula']='f(x)=x'
  elif mode=='not-example-formula': example['formulas']=['g(x)=x']
  elif mode=='new-common-borrow': common['equation_ids'].append('reaction-model')
  elif mode=='new-reading-status': new['status']='reading'
  elif mode=='missing-en-scope': del new['execution_scope']['en']
  elif mode not in ('list-root','dict-root'): raise ValueError(mode)
  dump(root/'catalog/atlas-equations.json',equations);dump(root/'catalog/atlas-execution-discovery.json',discovery)
  registry={'verification_receipt':'https://hrkoyama.github.io/verification/fixture.json'}
  registry_path=root/'numerical-methods-atlas/code-and-data/examples.json';dump(registry_path,registry)
  dump(root/'verification/fixture.json',{'passed':True,'registry_sha256':sha256(registry_path.read_bytes()).hexdigest(),'examples':[{'id':'legacy-run','passed':True}]})
  def loader(_root,ids):
   assert _root==root
   return [copy.deepcopy(example) for ident in ids if ident=='reaction-example']
  namespace={'sha256':sha256,'json':json,'Path':Path,'urlsplit':urlsplit,'load_supplemental_examples':loader};exec(isolated,namespace)
  positive=mode in ('list-root','dict-root')
  try: result=namespace['equation_evidence'](root,equations,discovery)
  except (AssertionError,KeyError,IndexError,TypeError,ValueError) as exc:
   assert not positive, (mode,type(exc).__name__,str(exc))
   return {'mode':mode,'rejected':True,'exception':type(exc).__name__}
  assert positive, 'Invalid provenance accepted: '+mode
  assert result['supplemental_case_ids']==['reaction-example']
  assert result['source_sha256'][p]==digest
  assert result['common']['bio-legacy']==[common]
  assert not result['common']['bio-reading']
  return {'mode':mode,'accepted':True}
results=[check(x) for x in json.loads(sys.argv[2])]
assert sha256(source.read_bytes()).hexdigest()==sha256(raw).hexdigest(), 'Source changed during fixture execution'
print(json.dumps({'source_sha256':sha256(raw).hexdigest(),'checks':results,'scientific_imports':0,'packet_loader_stubbed':True}))
`;
function run(modes) {
  const out = execFileSync(python, ['-B', '-c', program, source, JSON.stringify(modes)], {
    encoding: 'utf8', timeout: 15000, maxBuffer: 1024 * 1024,
    env: { ...process.env, PYTHONDONTWRITEBYTECODE: '1', ATLAS_EXPECT_SOURCE_SHA256: sourceSha256 },
  });
  const result = JSON.parse(out);
  assert.equal(result.checks.length, modes.length);
  assert.equal(result.scientific_imports, 0);
  assert.equal(result.packet_loader_stubbed, true);
  assert.equal(result.source_sha256, sourceSha256);
}
test('equation provenance retains legacy survey constraints and rejects opt-out or unknown provenance', () => {
  run(['list-root', 'legacy-scope', 'legacy-status', 'reading-borrow', 'survey-opt-out', 'unknown-kind', 'new-unknown-kind', 'missing-provenance']);
});
test('equation provenance binds selected examples and actual source bytes', () => {
  run(['dict-root', 'unselected', 'repeated-selected', 'declared-stale-sha', 'actual-stale-bytes', 'unbound-path']);
});
test('equation provenance binds canonical pointer shape, case identity, and formula', () => {
  run(['wrong-case', 'negative-index', 'leading-zero-index', 'leading-zero-formula', 'extra-pointer-token', 'wrong-pointer-field', 'escaped-pointer', 'wrong-formula', 'not-example-formula']);
});
test('equation provenance cannot borrow common executions or omit bilingual scope', () => {
  run(['new-common-borrow', 'new-reading-status', 'missing-en-scope']);
});
