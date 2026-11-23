import numpy as np
import pytest
import fem,annulus,boundary,run
from references import fields

@pytest.mark.parametrize('family',['uniform','graded','square','warped'])
def test_mesh_positive_and_p1_partition(family):
    p,c,b=fem.mesh(4,family);area,G=fem.geometry(p,c)
    assert area.min()>0 and b.any()
    np.testing.assert_allclose(G.sum(axis=1),0,atol=4e-14)
    assert abs(area.sum()-(3 if family in ['uniform','graded'] else 1))<2e-14

@pytest.mark.parametrize('q',[2,4,8])
def test_duffy_moments(q):
    N,w=fem.quadrature(q)
    assert abs(w.sum()-.5)<2e-15
    np.testing.assert_allclose(w@N,np.full(3,1/6),atol=2e-15)

@pytest.mark.parametrize('p',[np.array([[.3,.4]]),np.array([[-.4,.3]]),np.array([[-.4,-.3]])])
def test_corner_gradient(p):
    e=1e-6;value,G=fields.corner(p)
    fd=np.column_stack([(fields.corner(p+e*np.eye(2)[j])[0]-fields.corner(p-e*np.eye(2)[j])[0])/(2*e) for j in range(2)])
    np.testing.assert_allclose(G,fd,atol=2e-9)

def test_analytic_manufactured_source():assert all(fields.qualify()['checks'].values())

def test_viscous_rational_point_golden():
    u,G,f=fields.viscous(np.array([1.]),np.array([1.]))
    np.testing.assert_allclose(u[0],[4.,0.],atol=1e-14)
    np.testing.assert_allclose(G[0],[[6.,6.],[2.,-2.]],atol=1e-14)
    np.testing.assert_allclose(f[0],[25.6,20.8],atol=1e-13)

def test_warped_affine_patch_gradient():
    p,c,b=fem.mesh(6,'warped');area,G=fem.geometry(p,c)
    value=p[:,0]+2*p[:,1]-.7
    np.testing.assert_allclose(np.einsum('ea,eak->ek',value[c],G),np.broadcast_to([1.,2.],(len(c),2)),atol=3e-14)

@pytest.mark.parametrize('kind',['neumann','robin'])
def test_poisson_actual_solve_and_flux(kind):
    r,a=boundary.solve(8,kind)
    assert r['residual']<2e-13 and r['flux_balance']<2e-12 and r['boundary_residual']<2e-14
    assert a['u'].shape==(8,8)

def test_neumann_rejects_physical_incompatibility():
    with pytest.raises(ValueError):boundary.solve(8,'neumann',forcing_offset=1)

def test_neumann_constant_nullspace_and_gauge():
    A,b,u,f,source=boundary.assemble(8,'neumann')
    np.testing.assert_array_equal(A@np.ones(64),np.zeros(64))
    a,x=boundary.solve(8,'neumann');b,y=boundary.solve(8,'neumann',.25)
    np.testing.assert_allclose(y['u']-x['u'],.25,atol=3e-14)

def test_polar_shape_geometry_and_partition():
    N,Nr,Nt=annulus.shape(.31,.72)
    assert abs(N.sum()-1)<1e-15 and Nr.sum()==0 and Nt.sum()==0
    G=annulus.gradients(Nr,Nt,np.array([1.4]),np.array([.6]),.1,.2)
    np.testing.assert_allclose(G.sum(axis=1),0,atol=2e-15)

def test_vector_viscous_actual_block_solve():
    r,a=annulus.solve(4)
    assert r['residual']<2e-12 and r['reaction_balance']<2e-12 and r['work_identity']<2e-12
    assert a['u'].shape==(5,8,2) and r['boundary_error']==0

def test_frozen_sources():assert run.frozen()['shared_pytest_plus_main_budget_seconds']==120
