"""Regression for the scalar type that interrupted saved pendulum qualification."""
import json
import numpy as np
import pytest
from io_contract import save_json


def test_numpy_qualification_scalars_serialize_without_nonfinite_escape(tmp_path):
    target=tmp_path/'qualification.json'
    save_json(target,{'passed':np.bool_(True),'checks':{'AGM-K':np.float64(1)<=np.float64(2)},'iterations':np.int64(24),'error':np.float64(0.)})
    result=json.loads(target.read_text())
    assert result=={'passed':True,'checks':{'AGM-K':True},'iterations':24,'error':0.}
    assert type(result['checks']['AGM-K']) is bool
    before=target.read_bytes()
    with pytest.raises(ValueError):save_json(target,{'error':np.float64(np.nan)})
    assert target.read_bytes()==before
