import numpy as np
import pytest
from scipy.sparse.linalg import spsolve
import operators as op
import multilevel as ml
from references import p1

def test_harmonic_transmission():
    A,b,(X,Y,a),faces,bd=op.scalar_fv(8,True);u=spsolve(A,b);exact=np.where(X<.5,X,.495+.01*X)/.505
    assert np.max(abs(u-exact))<5e-12
    assert np.max(abs(faces[1][2]*(u[faces[1][0]]-u[faces[1][1]])*8+1/.505))<5e-12

@pytest.mark.parametrize('mode',['affine','xy'])
def test_full_tensor_patch(mode):
    A,b,p,e,i,g=op.q1(8,mode);assert np.max(abs(A@g[i]-b))<5e-14

def test_cross_term_is_observable():
    A,b,p,e,i,g=op.q1(8,'xy');assert abs(op.tensor()[0,1])>.4
    assert np.linalg.norm(b-A@g[i])<1e-12
    assert abs(-2*op.tensor()[0,1])>.8

@pytest.mark.parametrize('cell',[True,False])
def test_geometric_full_rank_and_boundary(cell):
    P=ml.geometric_p(8,cell).toarray();assert np.linalg.matrix_rank(P)==P.shape[1]
    if cell:assert abs(P[0].sum()-.25)<1e-14
    else:assert abs(P[0].sum()-.25)<1e-14

@pytest.mark.parametrize('cell',[True,False])
@pytest.mark.parametrize('kind',['geometric','amg'])
def test_cycle_spd_linearity_galerkin(cell,kind):
    A=op.scalar_fv(8)[0] if cell else op.q1(8)[0];L=ml.hierarchy(A,kind,8,cell)
    B=np.column_stack([ml.cycle(L,v) for v in np.eye(A.shape[0])]);assert np.linalg.norm(B-B.T)<1e-11*np.linalg.norm(B);assert np.linalg.eigvalsh(B)[0]>0
    assert np.linalg.norm((L.coarse.A-L.P.T@A@L.P).data)<1e-12*np.linalg.norm(A.data)
    x=np.sin(np.arange(A.shape[0]));y=np.cos(np.arange(A.shape[0]));assert np.linalg.norm(ml.cycle(L,2*x-3*y)-2*ml.cycle(L,x)+3*ml.cycle(L,y))<1e-10

def test_independent_triangle_evaluator():
    X=np.array([.1,.2,.8,.9]);Y=np.array([.2,.1,.9,.8]);x,y=np.meshgrid(np.linspace(0,1,9),np.linspace(0,1,9));u=3*x-2*y+1
    assert np.max(abs(p1.evaluate(u,X,Y)-(3*X-2*Y+1)))<2e-15

def test_budget_exhaustion_true_residual():
    A,b=op.scalar_fv(16)[:2];L=ml.hierarchy(A,'geometric',16,True);u,d=ml.pcg(A,b,L,1e-14,1)
    assert d['iterations']==1 and not d['converged'] and d['termination']=='iteration_budget'
    assert abs(d['history'][-1]-np.linalg.norm(b-A@u)/np.linalg.norm(b))<1e-14
