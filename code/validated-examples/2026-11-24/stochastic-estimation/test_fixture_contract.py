"""Immutable external-reference data guards are distinct from fresh sampler output."""
import hashlib
import numpy as np
import pytest
from run import fixed_diagnostic_array


def test_exact_diagnostic_fixture_rejects_forged_data_without_demanding_fresh_identity():
    fixture=np.arange(32,dtype=float).reshape(2,16,1);x=np.asarray(fixture[:,:,0],dtype='<f8',order='C')
    row={'key':'fixed','prefix':16,'column':0,'shape':[2,16],'sha256':hashlib.sha256(x.tobytes()).hexdigest()}
    np.testing.assert_array_equal(fixed_diagnostic_array({'fixed':fixture},row),x)
    fresh=fixture+.125
    assert not np.array_equal(fresh,fixture) # fresh data are recorded and scientifically gated separately
    with pytest.raises(ValueError,match='fixture bytes'):fixed_diagnostic_array({'fixed':fresh},row)
    with pytest.raises(ValueError,match='fixture bytes'):fixed_diagnostic_array({'fixed':fixture},dict(row,shape=[1,32]))
