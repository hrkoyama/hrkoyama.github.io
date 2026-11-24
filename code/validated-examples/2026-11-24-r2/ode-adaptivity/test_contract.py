import json
from pathlib import Path
import sys
import numpy as np
import pytest
import io_contract
import reference_eval
import run


def test_json_serializes_numpy_scalars_as_native_bool(tmp_path):
    path=tmp_path/'record.json';io_contract.save_json(path,{'passed':np.bool_(True),'error':np.float64(.01),'count':np.int64(3)})
    data=json.loads(path.read_text());assert type(data['passed']) is bool and data['passed'] and data['error']==.01


def test_nonfinite_csv_not_silently_blank_or_string(tmp_path):
    with pytest.raises(ValueError,match='Nonfinite'):io_contract.save_csv(tmp_path/'bad.csv',[{'step':1,'error':float('nan')}])


def test_failed_candidate_npz_preserves_invalid_raw_array(tmp_path):
    trace=io_contract.Trace(tmp_path,'failure');trace('failed-stage',candidate=np.array([1.,np.nan]),scaled_residual=float('inf'));trace.close()
    with np.load(tmp_path/'failure-active.npz',allow_pickle=False) as packet:
        assert np.isnan(packet['candidate'][1])
        assert packet['failed-stage__scaled_residual'].shape==() and np.isinf(packet['failed-stage__scaled_residual'])
    row=json.loads((tmp_path/'failure-stages.jsonl').read_text());assert row['nonfinite_candidate_saved_to_npz'] is True


def test_reference_freshness_rejects_forged_input_hash(tmp_path):
    root=tmp_path/'source';(root/'references/cache').mkdir(parents=True)
    for name in reference_eval.DEPENDENCIES:
        p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('{}')
    q={'passed':True,'checks':{str(k):True for k in range(52)},'input_sha256':'0'*64,'acceptance_sha256':reference_eval.digest(root/'acceptance.json'),
       'source_sha256':{name:reference_eval.digest(root/name) for name in reference_eval.DEPENDENCIES}}
    (root/'references/cache/qualification.json').write_text(json.dumps(q))
    with pytest.raises(ValueError,match='Stale reference input'):reference_eval.Cache(root)


def test_main_fresh_output_guard_preserves_existing_file(tmp_path,monkeypatch):
    out=tmp_path/'old';out.mkdir();sentinel=out/'keep';sentinel.write_text('old')
    monkeypatch.setattr(sys,'argv',['run','--input',str(Path(__file__).with_name('inputs.json')),'--output',str(out)])
    with pytest.raises(FileExistsError):run.main()
    assert sentinel.read_text()=='old'


def test_main_rejects_altered_input_before_creating_output(tmp_path,monkeypatch):
    given=tmp_path/'altered.json';given.write_text('{}');out=tmp_path/'new'
    monkeypatch.setattr(sys,'argv',['run','--input',str(given),'--output',str(out)])
    with pytest.raises(ValueError,match='frozen input'):run.main()
    assert not out.exists()


def test_late_diagnostic_failure_keeps_entered_case_records(tmp_path,monkeypatch):
    source=tmp_path/'source';source.mkdir();inp=source/'inputs.json'
    inp.write_text(json.dumps({'runs':[{'id':str(k),'case_id':'robertson-stiff-kinetics'} for k in range(60)]}))
    (source/'acceptance.json').write_text('{}')
    (source/'pre-run-contract.json').write_text(json.dumps({'files_sha256':{'inputs.json':io_contract.digest(inp)}}))
    monkeypatch.setattr(run,'__file__',str(source/'run.py'));monkeypatch.setattr(run,'Cache',lambda source:None)
    def stop(case,*args):
        case['records'].append({'run_id':'completed-candidate','error':.01});case['passed']=True
        raise RuntimeError('late oracle failure')
    monkeypatch.setattr(run.experiments,'run_stiff',stop)
    out=tmp_path/'result';monkeypatch.setattr(sys,'argv',['run','--input',str(inp),'--output',str(out)])
    assert run.main()==1
    result=json.loads((out/'result.json').read_text())
    assert result['passed'] is False and result['cases'][0]['passed'] is False
    assert result['cases'][0]['records'][0]['error']==.01 and 'late oracle failure' in result['failure']['message']
