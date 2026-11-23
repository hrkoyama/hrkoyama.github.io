import json
from pathlib import Path
import numpy as np
import pytest
import fmm
from references.direct import direct,octahedron
from protocol import frozen
ROOT=Path(__file__).parent
C=json.loads((ROOT/'inputs.json').read_text());X=np.array(C['positions']);M=np.array(C['masses'])

@pytest.mark.parametrize('p',[3,5,7])
def test_barycentric_polynomial_partition_and_derivative(p):
    t=np.array([-.61,.17,.77]);nodes=fmm.chebyshev(p)[0];B,D=fmm.basis(t,p)
    np.testing.assert_allclose(B.sum(axis=1),1,atol=2e-15);np.testing.assert_allclose(D.sum(axis=1),0,atol=2e-14)
    np.testing.assert_allclose(np.einsum('ij,j->i',B,nodes**(p-1)),t**(p-1),atol=2e-14);np.testing.assert_allclose(np.einsum('ij,j->i',D,nodes**(p-1)),(p-1)*t**(p-2),atol=2e-13)

@pytest.mark.parametrize('index',[0,2,4])
def test_exact_chebyshev_node_derivative_limit(index):
    z=fmm.chebyshev(5)[0];B,D=fmm.basis([z[index]],5)
    np.testing.assert_allclose(np.einsum('ij,j->i',D,z**3),3*z[index]**2,atol=2e-14);assert B[0,index]==1

def test_upward_m2m_equals_independent_parent_anterpolation():
    p=3;node=fmm.build(X,np.zeros(3),1.,0,2,True,8);counts=dict(p2m=0,m2m=0);fmm.up(node,X,M,p,counts);B=[fmm.basis(X[:,i],p)[0] for i in range(3)];expected=np.einsum('n,na,nb,nc->abc',M,*B,optimize=False)
    np.testing.assert_allclose(node.W,expected,atol=3e-15);assert counts['m2m']>0

@pytest.mark.parametrize('p',[3,5])
def test_l2l_and_physical_gradient_polynomial_golden(p):
    parent=fmm.Node(np.zeros(3),1.,np.array([],int),0);child=fmm.Node(np.array([.5,-.5,.5]),.5,np.array([],int),1);grid=fmm.grid(parent,p);values=(grid[:,0]**2+grid[:,0]*grid[:,1]-2*grid[:,2]).reshape(p,p,p);coarse=fmm.transfer(parent,child,values,p);points=np.array([[.41,-.37,.62],[.57,-.64,.31]]);phi,a=fmm.local_values(child,coarse,points,p);exact=points[:,0]**2+points[:,0]*points[:,1]-2*points[:,2]
    np.testing.assert_allclose(phi,exact,atol=2e-14);np.testing.assert_allclose(a,np.column_stack((-2*points[:,0]-points[:,1],-points[:,0],np.full(2,2.))),atol=5e-14)

@pytest.mark.parametrize('R',[.6,.9,1.2])
def test_finite_octahedron_exact_potential_and_acceleration(R):
    x=np.r_[np.eye(3)*.2,-np.eye(3)*.2];p,a=direct(x,np.full(6,1/6),np.array([[0,0,R]]));ep,ea=octahedron(.2,R)
    np.testing.assert_allclose([p[0],a[0,2]],[ep,ea],atol=2e-14);np.testing.assert_allclose(a[0,:2],0,atol=2e-14)

def test_unequal_mass_pair_reciprocity_and_sign():
    x=np.array([[-.5,0,0],[.5,0,0]]);m=np.array([.2,.8]);p,a=direct(x,m)
    np.testing.assert_allclose(p,[-.8,-.2],atol=1e-15);np.testing.assert_allclose(a,[[.8,0,0],[-.2,0,0]],atol=1e-15);np.testing.assert_allclose(np.sum(m[:,None]*a,axis=0),0,atol=1e-15)

def test_actual_deep_tree_has_nonzero_complete_chain_and_unique_owners():
    a,c=fmm.solve(X,M,3,3);assert np.all(a['leaf_depths']==3);assert c['chain_pairs']>0 and np.linalg.norm(a['chain_potential'])>1e-10;np.testing.assert_array_equal(a['ownership'],a['expected_ownership'])

def test_adaptive_unequal_levels_keep_overfull_bucket_and_ownership():
    a,c=fmm.solve(np.array(C['adaptive_positions']),M,3,3,False,8);assert len(np.unique(a['leaf_depths']))>1 and c['overfull_leaves']>0;np.testing.assert_array_equal(a['ownership'],a['expected_ownership'])

def test_actual_far_field_acceleration_matches_separate_direct_sum():
    a,c=fmm.solve(X,M,5,2);p,ref=direct(X,M);assert c['far_pairs']>0;assert np.linalg.norm(a['acceleration']-ref)/np.linalg.norm(ref)<.05

def test_distinct_coincident_sources_rejected():
    with pytest.raises(ValueError):fmm.solve(np.zeros((2,3)),np.full(2,.5),3,2)

def test_single_source_self_field_omitted():
    a,c=fmm.solve(np.array([[.17,.13,-.1]]),np.ones(1),3,2);np.testing.assert_array_equal(a['potential'],[0.]);np.testing.assert_array_equal(a['acceleration'],np.zeros((1,3)))

def test_frozen_sources():assert frozen(ROOT)['shared_pytest_plus_main_budget_seconds']==120
