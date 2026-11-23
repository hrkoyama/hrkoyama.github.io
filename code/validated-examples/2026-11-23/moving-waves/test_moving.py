import numpy as np
import pytest
from references import exact
import transport as s
import run

@pytest.mark.parametrize('n,k,l',[(8,1,1),(12,1,2),(16,2,1),(20,0,2)])
def test_actual_cgrid_stencil_matches_independent_symbol(n,k,l):
    coeff=np.array([.01,.02+.01j,-.03j]);q=exact.field(n,coeff,k,l)
    np.testing.assert_allclose(s.cgrid_rhs(q),exact.field(n,exact.symbol(n,k,l)@coeff,k,l),atol=2e-15)

@pytest.mark.parametrize('n',[8,12])
def test_periodic_cgrid_mass_and_energy_adjointness(n):
    q=np.random.default_rng(n).normal(size=(3,n,n));r=s.cgrid_rhs(q)
    assert abs(np.mean(r[0]))<2e-14
    assert abs(np.mean(np.sum(q*r,axis=0)))<3e-14

@pytest.mark.parametrize('n',[8,16])
def test_cgrid_zero_frequency_mode_is_actual_uniform_oscillation(n):
    q=np.broadcast_to(exact.zero_mode(0)[:,None,None],(3,n,n)).copy()
    out=s.cgrid_solve(q,.2,32)
    np.testing.assert_allclose(out['state'],np.broadcast_to(exact.zero_mode(.2)[:,None,None],q.shape),atol=1e-12)
    assert out['history'].shape==(5,3,n,n)

@pytest.mark.parametrize('n',[4,8,12])
def test_nonuniform_ale_gcl_constant_and_conservation(n):
    a=s.ale_solve(n,.37,constant=True)
    for x,m in zip(a['geometry'],a['history']):np.testing.assert_allclose(m/np.diff(x),1,atol=4e-15)
    assert abs(a['m'].sum()-1)<2e-15
    assert abs(a['stages'][:,6]).max()<3e-16

@pytest.mark.parametrize('t',[0.,.17,.5])
def test_analytic_moving_cell_mass_and_jacobian(t):
    xi=np.linspace(0,1,33);x=exact.faces(xi,t)
    assert np.diff(x).min()>0
    assert abs(exact.mass(x,t).sum()-1)<2e-15

@pytest.mark.parametrize('t',[.11,.43])
def test_face_velocity_derivative(t):
    xi=np.linspace(0,1,21);eps=1e-6
    np.testing.assert_allclose((exact.faces(xi,t+eps)-exact.faces(xi,t-eps))/(2*eps),exact.mesh_speed(xi,t),atol=1e-9)

def test_reference_qualifications():assert all(exact.qualification().values())

def test_discrete_balance_vector():
    n=16;L=exact.symbol(n);a=.01;k=-L[0,1].imag;l=-L[0,2].imag;c=L[1,2].real
    q=exact.field(n,np.array([a,-1j*l*a/c,1j*k*a/c]))
    assert np.max(abs(s.cgrid_rhs(q)))<3e-14

def test_frozen_scientific_sources():assert run.frozen()['shared_pytest_plus_main_budget_seconds']==120
