"""Version-pinned tie threshold/mask regressions; no Markov sampling."""
import json
from pathlib import Path
import numpy as np
import pytest
from diagnostics import tail_thresholds

FIXTURES=json.loads((Path(__file__).parent/'references/tail-quantile-fixtures.json').read_text())['fixtures']

@pytest.mark.parametrize('fixture',FIXTURES,ids=['upper8192','upper32768','lower32768'])
def test_declared_tail_quantile_tie_mask_and_exact_golden(fixture):
    f=fixture;value=float.fromhex(f['repeated_value_hex']);n=f['n'];below=f['below_count'];ties=f['tie_count']
    x=np.r_[np.full(below,value-1),np.full(ties,value),np.full(n-below-ties,value+1)]
    index=0 if f['probability']==.05 else 1
    q=tail_thresholds(x)[index];old=np.quantile(x,f['probability'],method='linear')
    assert float(q).hex()==f['reference_threshold_hex']
    assert float(old).hex()==f['numpy_threshold_hex']
    assert int(np.sum(x<=q))==f['reference_true_count']
    assert int(np.sum(x<=old))==f['numpy_true_count']
    assert q!=old and int(np.sum((x<=q)!=(x<=old)))==ties
