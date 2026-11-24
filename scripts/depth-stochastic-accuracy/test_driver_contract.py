"""Actual CLI/envelope and failure-retention regressions, without long physics."""
import json
from pathlib import Path
import numpy as np
import pytest
import support


def setup(tmp_path,monkeypatch):
    root=tmp_path/'source';root.mkdir()
    (root/'inputs.json').write_text(json.dumps({'cases':{'fixture':{}}}))
    (root/'acceptance.json').write_text(json.dumps({'limits':{}}))
    contract={'files_sha256':{n:support.sha(root/n) for n in ['inputs.json','acceptance.json']},'planned_case_gates':1}
    support.write(root/'pre-run-contract.json',contract)
    out=tmp_path/'results';monkeypatch.setattr('sys.argv',['run.py','--input',str(root/'inputs.json'),'--output',str(out)])
    return root,out


def test_real_cli_completes_strict_case_json_and_numeric_csv(tmp_path,monkeypatch):
    root,out=setup(tmp_path,monkeypatch)
    def experiment(cfg,limits,output,cases,partial):
        assert list(cfg['cases'])==['fixture'] and limits=={}
        row=support.case_record('fixture',cases);row['checks']['oracle']=True
        row['records'].append({'steps':1});support.csv_numeric(output/'fixture.csv',['steps','value'],[[1,2.]])
        support.finish_case(row,output)
    support.run(experiment,root)
    result=json.loads((out/'result.json').read_text())
    assert result['passed'] is True and result['failure'] is None and result['termination']=='fixed_budget_completed'
    assert result['checks']=={'fixture':True} and result['numerical_gate_count']==1 and result['cases'][0]['records']
    assert (out/'fixture.csv').read_text().splitlines()==['steps,value','1,2.0']


def test_real_cli_retains_partial_candidate_and_failure(tmp_path,monkeypatch):
    root,out=setup(tmp_path,monkeypatch)
    def broken(cfg,limits,output,cases,partial):
        partial['x']=np.array([1.,2.]);raise ArithmeticError('intentional fixture failure')
    with pytest.raises(SystemExit):support.run(broken,root)
    result=json.loads((out/'result.json').read_text());assert result['passed'] is False and result['failure']['type']=='ArithmeticError'
    with np.load(out/'failed-candidate-state.npz') as z:np.testing.assert_array_equal(z['x'],[1.,2.])


def test_real_cli_rejects_empty_case_records(tmp_path,monkeypatch):
    root,out=setup(tmp_path,monkeypatch)
    def incomplete(cfg,limits,output,cases,partial):
        row=support.case_record('fixture',cases);row['checks']['oracle']=True;support.finish_case(row,output)
    with pytest.raises(SystemExit):support.run(incomplete,root)
    result=json.loads((out/'result.json').read_text());assert result['passed'] is False and 'records' in result['failure']['message']


def test_csv_guard_rejects_nonfinite_ragged_and_duplicate_columns(tmp_path):
    for columns,rows in [(['x'],[[float('nan')]]),(['x'],[[1,2]]),(['x','x'],[[1,2]])]:
        with pytest.raises((ValueError,ArithmeticError)):support.csv_numeric(tmp_path/'bad.csv',columns,rows)


def test_completed_candidates_survive_a_later_fit_failure(tmp_path,monkeypatch):
    import run as driver
    root=tmp_path/'source';root.mkdir();(root/'references').mkdir();out=tmp_path/'results';out.mkdir()
    ident='fixture-weak';c={'seeds':[1,2],'steps':[2,4,8],'T':1.,'paths_per_batch':4}
    cfg={'cases':{ident:c}};support.write(root/'inputs.json',cfg)
    limits={'brownian_sum_roundoff_eps_factor':64,'weak_mcse_factor':5.,'calibration_absolute_allowance':1e-12,
            'weak_mcse_ratio':[.4,2.],'weak_resolution_3se_fraction':.3}
    support.write(root/'acceptance.json',{'limits':limits})
    reference={'passed':True,'checks':{'analytic':True},'input_sha256':support.sha(root/'inputs.json'),
               'acceptance_sha256':support.sha(root/'acceptance.json'),'records':{ident:[{'bias':[-.01,-.01],
               'paired_variance':[1.,1.],'discrete':[1.,1.]} for _ in c['steps']]}}
    support.write(root/'references/reference.json',reference);monkeypatch.setattr(driver,'HERE',root)
    def candidate(cfg,seed,methods,partial):
        return {'endpoints':np.full((1,3,4),1.+seed/100),'exact':np.ones(4),
                'association_error':np.zeros(3),'terminal_w':np.zeros(4)},str(seed)
    def failed_fit(*args):raise ArithmeticError('intentional post-candidate fit failure')
    monkeypatch.setattr(driver,'simulate_batch',candidate);monkeypatch.setattr(driver,'fit_order',failed_fit)
    with pytest.raises(ArithmeticError,match='post-candidate'):driver.experiment(cfg,limits,out,[],{})
    with np.load(out/(ident+'.npz')) as z:assert z['endpoints'].shape==(2,1,3,4)
    checkpoint=json.loads((out/(ident+'-candidate-checkpoint.json')).read_text())
    assert checkpoint['completed_batches']==2 and checkpoint['seeds']==[1,2]
