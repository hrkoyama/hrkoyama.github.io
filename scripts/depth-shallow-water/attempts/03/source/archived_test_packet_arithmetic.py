"""Regression for binary64 subnormal dry momentum; no numerical floor."""
import numpy as np
import pytest
import shallow_water as sw


def test_rounded_zero_water_packet_does_not_create_dry_momentum():
    tiny=np.nextafter(0.,1.)
    state=np.zeros((6,2));state[2]=[tiny,5*tiny]
    lf,rf,common,speed,data=sw.interfaces(state,np.zeros(6),dict(kind='transmissive'),9.81,packet_data=True)
    # A signed-flux evaluation rounds incoming h to zero but hu to nonzero.
    signed=state-.04*(lf[1:]-rf[:-1])
    assert np.any((signed[:,0]==0)&(signed[:,1]!=0))
    stable,stay=sw.packet_update(state,data,.04)
    assert stay>=0
    assert np.all(stable[:,0]>=0)
    assert np.all(stable[stable[:,0]==0,1]==0)
    assert stable[:,0].sum()==state[:,0].sum()


@pytest.mark.parametrize('bed_scale',[0.,.1])
def test_packet_update_is_algebraic_hll_with_bed_source(bed_scale):
    x=np.linspace(0,1,40);bed=bed_scale*np.sin(4*x)
    state=np.column_stack((1+.1*np.cos(3*x),.2+.05*np.sin(2*x)))
    lf,rf,common,speed,data=sw.interfaces(state,bed,dict(kind='transmissive'),9.81,packet_data=True)
    ratio=.1/speed
    signed=state-ratio*(lf[1:]-rf[:-1])
    stable,stay=sw.packet_update(state,data,ratio)
    assert stay>=0
    np.testing.assert_allclose(stable,signed,rtol=3e-15,atol=3e-16)
