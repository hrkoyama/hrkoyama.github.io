"""Numerical contracts, a regression for coupled noise, and failure behavior."""
import json
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
from models import gbm
from run import evaluate

ROOT=Path(__file__).parent


@pytest.mark.parametrize('case',['logistic-growth','sir-epidemic','mc-integral','gbm-sde'])
def test_fixed_case(case):
    result,header,rows=evaluate(ROOT/'inputs'/f'{case}.json')
    assert result['passed'] and rows and len(header)==len(rows[0])
    assert all(result['checks'].values())


@pytest.mark.parametrize('case',['logistic-growth','sir-epidemic','mc-integral','gbm-sde'])
def test_cli_serializes_numerical_results(case,tmp_path):
    result=subprocess.run([sys.executable,str(ROOT/'run.py'),'--input',str(ROOT/'inputs'/f'{case}.json'),'--output',str(tmp_path/'output')],capture_output=True)
    assert result.returncode==0,result.stderr.decode()
    assert json.loads((tmp_path/'output/result.json').read_text())['passed'] is True


def test_coupled_brownian_paths():
    p=json.loads((ROOT/'inputs/gbm-sde.json').read_text())
    rows=gbm(p)
    for _,_,exact in rows[1:]:
        np.testing.assert_array_equal(exact,rows[0][2])
    # Comparing independent endpoints would not show strong convergence.
    assert np.sqrt(np.mean((rows[-1][1]-rows[-1][2][::-1])**2))>10*np.sqrt(np.mean((rows[-1][1]-rows[-1][2])**2))


def test_false_tolerance_fails(tmp_path):
    p=json.loads((ROOT/'inputs/logistic-growth.json').read_text())
    p['acceptance']['max_error']=0
    path=tmp_path/'input.json';path.write_text(json.dumps(p))
    result=subprocess.run([sys.executable,str(ROOT/'run.py'),'--input',str(path),'--output',str(tmp_path/'output')],capture_output=True)
    assert result.returncode==1
    assert not json.loads((tmp_path/'output/result.json').read_text())['passed']


def test_refuses_overwrite(tmp_path):
    dest=tmp_path/'output';dest.mkdir();(dest/'keep.txt').write_text('keep')
    result=subprocess.run([sys.executable,str(ROOT/'run.py'),'--input',str(ROOT/'inputs/logistic-growth.json'),'--output',str(dest)],capture_output=True)
    assert result.returncode==2 and (dest/'keep.txt').read_text()=='keep'
