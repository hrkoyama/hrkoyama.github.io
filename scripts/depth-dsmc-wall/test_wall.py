import numpy as np
from dsmc import simulate,stream_wall,totals


def test_short_wall_run_full_boundary_budget():
    cfg={'kind':'wall','cells':4,'length':2,'weight':1/16,'temperatures':[1,2],'speeds':[0,0],
         'dt':.01,'burn_in':.02,'sample_time':.02,'blocks':2,'bins':2,'sample_every':1,'hist_velocity':[-6,6]}
    data=simulate(cfg,361)
    assert data['max_budget']<1e-12
    assert np.all(np.isfinite(data['profiles']))


def test_multiple_wall_crossings_use_remaining_flight_time():
    class Fixed:
        def random(self,n):return np.full(n,.5)
        def normal(self,size):return np.zeros(size)
    x=np.array([.5]);v=np.array([[100.,0,0]]);before=totals(v,1)
    ledger,hits=stream_wall(x,v,.04,1,[10000,10000],[0,0],Fixed(),1)
    assert sum(hits)>=4 and 0<=x[0]<=1
    np.testing.assert_allclose(totals(v,1)-before,ledger.sum(axis=0),atol=1e-10,rtol=0)
