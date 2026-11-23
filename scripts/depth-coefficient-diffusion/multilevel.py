"""Fixed symmetric Galerkin V-cycles; matrix-only SA and geometric P differ."""
from dataclasses import dataclass
import numpy as np
from scipy import sparse,linalg

@dataclass
class Level:
    A:object
    omega:float
    P:object=None
    coarse:object=None
    factor:object=None

def geometric_p(n,cell):
    nc=n//2
    fine=(np.arange(n)+.5)/n if cell else np.arange(1,n)/n
    coarse=(np.arange(nc)+.5)/nc if cell else np.arange(1,nc)/nc
    rows=[];cols=[];data=[]
    for i,x in enumerate(fine):
        if cell:
            z=x*nc-.5;j=int(np.floor(z));t=z-j
            for k,v in ((j,1-t),(j+1,t)):
                k2=0 if k<0 else nc-1 if k>=nc else k
                rows.append(i);cols.append(k2);data.append(-v if k!=k2 else v)
        else:
            z=x*nc;j=int(np.floor(z));t=z-j
            for k,v in ((j,1-t),(j+1,t)):
                if 0<k<nc:rows.append(i);cols.append(k-1);data.append(v)
    p=sparse.coo_matrix((data,(rows,cols)),shape=(len(fine),len(coarse))).tocsr()
    return sparse.kron(p,p,format='csr')

def aggregate(A,strength=.08):
    # Greedy graph-star rule from existing atlas foundations-conditioning, with provenance.
    labels=np.full(A.shape[0],-1); neighbors=[]
    for i in range(len(labels)):
        js=A.indices[A.indptr[i]:A.indptr[i+1]];v=np.abs(A.data[A.indptr[i]:A.indptr[i+1]]);off=v[js!=i];mx=float(max(off)) if len(off) else 0.
        neighbors.append(js[(js!=i)&(v>=strength*mx)])
    count=0
    for i in sorted(range(len(labels)),key=lambda j:(-len(neighbors[j]),j)):
        if labels[i]>=0:continue
        available=neighbors[i][labels[neighbors[i]]<0]
        if not len(available) and len(neighbors[i]):
            labels[i]=labels[max(neighbors[i],key=lambda j:abs(A[i,j]))];continue
        labels[i]=count;labels[available]=count;count+=1
    return sparse.csr_matrix((np.ones(len(labels)),(np.arange(len(labels)),labels)),shape=(len(labels),count))

def hierarchy(A,kind,n=None,cell=None):
    A=A.tocsr();bound=float(np.max(np.asarray(abs(A).sum(axis=1)).ravel()/A.diagonal()));omega=.5/bound
    level=Level(A,omega)
    if len(A.diagonal())<=16:
        level.factor=linalg.cho_factor(A.toarray(),check_finite=True);return level
    if kind=='geometric':P=geometric_p(n,cell)
    else:
        T=aggregate(A);P=(T-omega*sparse.diags(1/A.diagonal())@A@T).tocsr()
        if P.shape[1]>=A.shape[0]:raise RuntimeError('No aggregation reduction')
    Ac=(P.T@A@P).tocsr();Ac=(Ac+Ac.T)*.5;level.P=P
    level.coarse=hierarchy(Ac,kind,n//2 if n else None,cell)
    return level

def cycle(L,b):
    if L.coarse is None:return linalg.cho_solve(L.factor,b)
    x=np.zeros_like(b);d=L.omega/L.A.diagonal()
    for _ in range(2):x+=d*(b-L.A@x)
    x+=L.P@cycle(L.coarse,L.P.T@(b-L.A@x))
    for _ in range(2):x+=d*(b-L.A@x)
    return x

def pcg(A,b,L,tol=1e-8,budget=200):
    x=np.zeros_like(b);r=b.copy();z=cycle(L,r);p=z.copy();rz=float(np.sum(r*z));scale=np.linalg.norm(b);hist=[1.]
    if not np.isfinite(scale) or scale<=0 or not np.isfinite(rz) or rz<=0:raise ValueError('Nonzero finite RHS and SPD preconditioner required')
    for k in range(budget):
        ap=A@p;pap=float(np.sum(p*ap))
        if not np.isfinite(pap) or pap<=0:raise ArithmeticError('Nonpositive/nonfinite PCG curvature')
        alpha=rz/pap;x+=alpha*p;r=b-A@x;hist.append(float(np.linalg.norm(r)/scale))
        if hist[-1]<=tol:break
        z=cycle(L,r);new=float(np.sum(r*z))
        if not np.isfinite(new) or new<=0:raise ArithmeticError('Nonpositive/nonfinite preconditioned residual')
        p=z+(new/rz)*p;rz=new
    return x,{'history':hist,'iterations':len(hist)-1,'converged':bool(hist[-1]<=tol),'termination':'residual_tolerance' if hist[-1]<=tol else 'iteration_budget'}

def levels(L):
    sizes=[];nnz=[]
    while L is not None:sizes.append(L.A.shape[0]);nnz.append(L.A.nnz);L=L.coarse
    return {'sizes':sizes,'nnz':nnz,'grid_complexity':sum(sizes)/sizes[0],'operator_complexity':sum(nnz)/nnz[0]}
