import json
from pathlib import Path
import numpy as np
import pytest
import electrostatics as s
from references import twoperiodic as r
from protocol import frozen
ROOT=Path(__file__).parent
C=json.loads((ROOT/'inputs.json').read_text());X=np.array(C['positions']);Q=np.array(C['charges']);BOX=np.r_[C['lateral'],3.]

@pytest.mark.parametrize('axis',[0,1,2])
def test_correction_energy_gradient_and_neutrality(axis):
    h=1e-6;a=X.copy();b=X.copy();a[0,axis]+=h;b[0,axis]-=h
    derivative=-(s.correction(a,Q,BOX)[0]-s.correction(b,Q,BOX)[0])/(2*h)
    np.testing.assert_allclose(derivative,s.correction(X,Q,BOX)[1][0,axis],atol=2e-9)
    np.testing.assert_allclose(s.correction(X,Q,BOX)[1].sum(axis=0),0,atol=1e-15)

@pytest.mark.parametrize('alpha',[2.5,3.5])
def test_orthorhombic_ewald_energy_force(alpha):
    h=5e-6;a=X.copy();b=X.copy();a[1,0]+=h;b[1,0]-=h
    force=s.ewald3p(X,Q,BOX,alpha)[1][1,0]
    gradient=-(s.ewald3p(a,Q,BOX,alpha)[0]-s.ewald3p(b,Q,BOX,alpha)[0])/(2*h)
    assert abs(force-gradient)<3e-7

@pytest.mark.parametrize('axis',[0,1,2])
def test_independent_2p_energy_force(axis):
    h=5e-6;a=X.copy();b=X.copy();a[1,axis]+=h;b[1,axis]-=h
    gradient=-(r.energy_force(a,Q,C['lateral'])[0]-r.energy_force(b,Q,C['lateral'])[0])/(2*h)
    assert abs(gradient-r.energy_force(X,Q,C['lateral'])[1][1,axis])<3e-7

@pytest.mark.parametrize('method',['3p','2p'])
def test_charged_cells_rejected(method):
    with pytest.raises(ValueError):
        if method=='3p':s.corrected(X,Q+.1,BOX)
        else:r.energy_force(X,Q+.1,C['lateral'])

def test_permutation_and_neutral_translation():
    E,F,_=s.corrected(X,Q,BOX);order=np.array([3,1,0,2]);e,f,_=s.corrected(X[order]+[.11,.07,.13],Q[order],BOX)
    np.testing.assert_allclose(e,E,atol=1e-10);np.testing.assert_allclose(f,F[order],atol=1e-9)

def test_independent_splitting_identity():
    a=r.energy_force(X,Q,C['lateral'],3.);b=r.energy_force(X,Q,C['lateral'],4.)
    np.testing.assert_allclose(a[0],b[0],atol=1e-10);np.testing.assert_allclose(a[1],b[1],atol=1e-9)

def test_horizontal_zero_mode_and_asymptotic_gauge():
    phi,field,_=r.evaluate(X,Q,C['lateral'],4.,2.5,64.,np.array([[.37,.19,6.],[.37,.19,-6.]]))
    target=2*np.pi*np.sum(Q*X[:,2])/np.prod(C['lateral'])*np.array([1,-1])
    np.testing.assert_allclose(phi,target,atol=1e-10);np.testing.assert_allclose(field,0,atol=1e-10)
    assert abs(r.energy_force(X,Q,C['lateral'],include_zero=False)[0]-r.energy_force(X,Q,C['lateral'])[0])>1e-3

@pytest.mark.parametrize('sign',[-1,1])
def test_screened_exponential_does_not_overflow(sign):
    for z in [-20.,20.]:
        value=r.screened(np.array([1.,20.,64.]),z,4.,sign)
        assert np.isfinite(value).all() and np.min(value)>=0

def test_self_convention_keeps_regular_finite_part():
    E,F,a=r.energy_force(X,Q,C['lateral']);assert np.isfinite(E) and np.isfinite(F).all() and np.isfinite(a['potential']).all()

def test_frozen_sources():assert frozen(ROOT)['shared_pytest_plus_main_budget_seconds']==120
