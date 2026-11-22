import copy,hashlib,json
from pathlib import Path
import numpy as np
import pytest
from run import ROOT,block_average,cell_average_1d,glm_mode,run,validate_config
from legacy.mhd import solve_orszag_tang

@pytest.fixture(scope='module')
def config():return json.loads((ROOT/'inputs.json').read_text())
@pytest.fixture(scope='module')
def result(tmp_path_factory):return run(ROOT/'inputs.json',tmp_path_factory.mktemp('mhd'))
def test_all_independent_cases_accept(result):
    assert len(result['cases'])==4 and result['passed']
    assert all(c['passed'] and all(c['checks'].values()) for c in result['cases'])
def test_1d_conservative_restriction():
    a=np.column_stack((np.arange(8),(np.arange(8)+.5)/8,np.arange(8)**2))
    assert np.allclose(cell_average_1d(a,4,0,1,[2])[:,0],(np.arange(8)**2).reshape(4,2).mean(1))
    assert np.isclose(cell_average_1d(a,3,0,1,[2]).mean(),a[:,2].mean())
def test_2d_restriction_orientation():
    v=np.arange(16).reshape(4,4);a=np.column_stack((np.arange(16),v.ravel()))
    assert np.allclose(block_average(a,2,[1])[...,0],v.T.reshape(2,2,2,2).mean((1,3)))
def test_reference_hashes_are_recorded():
    for name in ['ot','brio','shu']:
        p=json.loads((ROOT/'references'/('athena-'+name+'-provenance.json')).read_text())
        assert p['source']['repository']=='PrincetonUniversity/athena' and len(p['source']['commit'])==40
        for row in p['records']:
            assert hashlib.sha256((ROOT/'references'/row['data_file']).read_bytes()).hexdigest()==row['sha256']
def test_intermediate_reference_miss_retained(result):
    c=next(c for c in result['cases'] if c['id']=='shu-independent')
    assert not c['reference_records'][0]['target_reached'] and c['reference_records'][-1]['target_reached']
    assert all(r['target']==.005 for r in c['reference_records'])
def test_ct_native_constraint_is_preserved():
    r=solve_orszag_tang(n=16,method='ct',final_time=.015)
    assert np.max(abs(r.divergence))<1e-12
    assert np.all(np.isfinite(r.q))
def test_glm_second_order_and_damping(config):
    r=glm_mode(config['glm_mode']);assert r['passed']
    assert 1.9<r['metrics']['observed_order']<2.1
@pytest.mark.parametrize('change',[('ot','time',.1),('brio','cfl',0),('shu','grids',[100,100]),('glm_mode','speed',0)])
def test_reject_incompatible_physics(config,change):
    c=copy.deepcopy(config);g,k,v=change;c[g][k]=v
    with pytest.raises(ValueError):validate_config(c)
