import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

test('study summaries retain false outcomes and reject inconsistent or untyped metadata',()=>{
 const value=JSON.parse(execFileSync('python3',['-B','-c',String.raw`
import ast,copy,json,pathlib,re
path=pathlib.Path('scripts/build-atlas-depth-examples.py')
tree=ast.parse(path.read_text());namespace={'re':re}
node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='original_study_targets')
exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),namespace)
check=namespace['original_study_targets'];count=0
assert check({'checks':{'old':True}}) is None;count+=1
row={'original_target_results':{'accurate':False,'conserved':True},'original_target_summary':{'met':1,'total':2,'all_met':False,'acceptance_sha256':'a'*64}}
targets,summary=check(row);assert targets['accurate'] is False and summary['all_met'] is False;count+=1
all_met=copy.deepcopy(row);all_met['original_target_results']['accurate']=True;all_met['original_target_summary'].update(met=2,all_met=True)
assert check(all_met)[1]['all_met'] is True;count+=1
invalid=[]
for key,value in [('met',2),('total',3),('all_met',True),('acceptance_sha256','wrong')]:
    candidate=copy.deepcopy(row);candidate['original_target_summary'][key]=value;invalid.append(candidate)
candidate=copy.deepcopy(row);candidate['original_target_results']['accurate']=0;invalid.append(candidate)
candidate=copy.deepcopy(row);candidate['original_target_results']={};invalid.append(candidate)
candidate=copy.deepcopy(row);candidate['original_target_summary']['met']=True;invalid.append(candidate)
candidate=copy.deepcopy(row);candidate['original_target_summary']['total']=True;invalid.append(candidate)
candidate=copy.deepcopy(row);candidate['original_study_goal_measurements']={'accurate':{'met':True}};invalid.append(candidate)
for candidate in invalid:
    try:check(candidate)
    except AssertionError:count+=1
    else:raise AssertionError('Invalid study target metadata accepted')
print(json.dumps({'passed':True,'checks':count,'scientific_execution':False}))
`],{cwd:fileURLToPath(new URL('../',import.meta.url)),encoding:'utf8',timeout:30_000}));
 assert.deepEqual(value,{passed:true,checks:12,scientific_execution:false});
});
