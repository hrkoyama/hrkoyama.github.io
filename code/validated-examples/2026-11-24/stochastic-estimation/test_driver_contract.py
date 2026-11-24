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
