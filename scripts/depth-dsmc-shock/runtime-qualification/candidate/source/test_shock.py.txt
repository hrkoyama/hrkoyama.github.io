import numpy as np
from dsmc import (RHO2,TEMP2,U1,U2,FluxSampler,stream_open,totals)


def test_open_reservoir_particle_momentum_energy_budget():
    x=np.array([.001,.999]);v=np.array([[-5.,1,2],[5.,-1,1]])
    rng=np.random.default_rng(371);before=totals(v,.01)
    states=[(1.,1.,U1),(RHO2,TEMP2,U2)]
    samplers=[FluxSampler(U1,1),FluxSampler(-U2,TEMP2)]
    y,w,ledger,crossings=stream_open(x,v,.001,1,.01,states,samplers,rng)
    assert crossings[:,1].tolist()==[1,1]
    assert np.all((y>=0)&(y<1))
    np.testing.assert_allclose(totals(w,.01)-before,ledger.sum(axis=0),atol=3e-15,rtol=0)


def test_rankine_hugoniot_fluxes_independent_gamma_formulas():
    gamma=5/3;mach=2
    compression=(gamma+1)*mach**2/((gamma-1)*mach**2+2)
    pressure=1+2*gamma/(gamma+1)*(mach**2-1)
    assert abs(RHO2-compression)<1e-15
    assert abs(TEMP2-pressure/compression)<1e-15
    def flux(n,u,t):return np.array([n*u,n*u*u+n*t,n*u*(.5*u*u+2.5*t)])
    np.testing.assert_allclose(flux(1,U1,1),flux(RHO2,U2,TEMP2),rtol=2e-15,atol=0)
