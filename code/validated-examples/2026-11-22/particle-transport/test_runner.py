"""Packaging contracts and preregistration guards, separate from solver tests."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import pytest
import run


@pytest.fixture
def config():return run.strict_json((run.HERE/'inputs.json').read_bytes())


@pytest.mark.parametrize('change',[
    lambda c:c['ewald']['acceptance'].update(force_error=1),
    lambda c:c['pic'].update(mesh_particles=1000000000),
    lambda c:c['dsmc'].update(seeds=True),
    lambda c:c.update(maximum_seconds=1000000),
])
def test_fixed_protocol_rejects_changed_criteria_and_budgets(config,change):
    modified=copy.deepcopy(config);change(modified)
    with pytest.raises(ValueError):run.validate_input(modified)


@pytest.mark.parametrize('payload',['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}'])
def test_ambiguous_or_nonfinite_json_is_rejected(payload):
    with pytest.raises(ValueError):run.strict_json(payload)


def test_original_input_and_design_provenance(config):
    assert hashlib.sha256((run.HERE/'inputs.json').read_bytes()).hexdigest()==run.INPUT_SHA256
    assert run.validate_input(config)==config
    protocol=json.loads((run.HERE/'protocol-history.json').read_text())
    assert protocol['locked_before_primary_pilot_and_reference'] is True
    assert protocol['post_pilot_criteria_changes'] is False


def test_existing_evidence_is_never_overwritten(config,tmp_path):
    (tmp_path/'previous.json').write_text('previous evidence')
    with pytest.raises(ValueError,match='new or empty'):run.execute(config,tmp_path)
    assert (tmp_path/'previous.json').read_text()=='previous evidence'


def test_public_cli_executes_every_case_and_saves_all_numeric_decisions(tmp_path):
    output=tmp_path/'independent-output'
    process=subprocess.run([sys.executable,'-W','error',str(run.HERE/'run.py'),'--input',str(run.HERE/'inputs.json'),'--output',str(output)],capture_output=True,text=True,timeout=115)
    assert process.returncode==0,process.stdout+'\n'+process.stderr
    result=run.strict_json((output/'result.json').read_bytes())
    assert result['passed'] is True and result['termination']=='fixed_inputs_completed'
    assert result['input_sha256']==run.INPUT_SHA256
    assert list(result['checks'])==run.CASE_IDS and all(v is True for v in result['checks'].values())
    for case in result['cases']:
        assert case['passed'] is True and all(v is True for v in case['checks'].values())
        assert case['metrics'] and case['records']
        assert (output/(case['id']+'.csv')).stat().st_size>0
        assert run.strict_json((output/(case['id']+'.json')).read_bytes())==case
