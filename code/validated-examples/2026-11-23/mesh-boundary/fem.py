import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve,splu,onenormest,LinearOperator
from references import fields


def mesh(n,family):
    if family in ['uniform','graded']:
        t=np.linspace(-1,1,2*n+1);Y,X=np.meshgrid(t,t,indexing='ij');points=np.column_stack((X.ravel(),Y.ravel()));width=2*n
    else:
        t=np.linspace(0,1,n+1);Y,X=np.meshgrid(t,t,indexing='ij');points=np.column_stack((X.ravel(),Y.ravel()));width=n
    cells=[]
    for j in range(width):
        for i in range(width):
            if family in ['uniform','graded'] and i>=n and j<n:continue
            a=j*(width+1)+i;b=a+1;c=a+width+1;d=c+1;cells.extend([[a,b,d],[a,d,c]])
    cells=np.array(cells);used=np.unique(cells);rename=np.full(len(points),-1);rename[used]=np.arange(len(used));points=points[used];cells=rename[cells]
    if family=='graded':points*=np.max(abs(points),axis=1)[:,None]
    if family=='warped':
        x,y=points.T;window=np.sin(np.pi*x)*np.sin(np.pi*y)
        points+=.2/n*np.column_stack((window*np.sin(2*np.pi*y),window*np.cos(2*np.pi*x)))
    edges=np.sort(np.concatenate([cells[:,[0,1]],cells[:,[1,2]],cells[:,[2,0]]]),axis=1)
    unique,count=np.unique(edges,axis=0,return_counts=True);boundary=np.zeros(len(points),dtype=bool);boundary[np.unique(unique[count==1])]=True
    return points,cells,boundary


def geometry(points,cells):
    t=points[cells];J=np.stack((t[:,1]-t[:,0],t[:,2]-t[:,0]),axis=-1);det=np.linalg.det(J)
    if np.min(det)<=0:raise ArithmeticError('Nonpositive triangle Jacobian')
    gradients=np.einsum('ai,eij->eaj',np.array([[-1.,-1.],[1.,0.],[0.,1.]]),np.linalg.inv(J))
    return det/2,gradients


def quadrature(order):
    z,w=leggauss(order);s,t=np.meshgrid((z+1)/2,(z+1)/2,indexing='ij');ws,wt=np.meshgrid(w/2,w/2,indexing='ij')
    return np.column_stack((1-s.ravel(),(s*(1-t)).ravel(),(s*t).ravel())),(ws*wt*s).ravel()


def norms(points,cells,u,family,order=8,corner_order=48):
    area,G=geometry(points,cells);exact=fields.corner if family in ['uniform','graded'] else fields.smooth
    grad=np.einsum('ea,eak->ek',u[cells],G);tot=np.zeros(2)
    at_origin=np.any(np.all(points[cells]==0,axis=2),axis=1) if family in ['uniform','graded'] else np.zeros(len(cells),dtype=bool)
    for selected,q in [(~at_origin,order),(at_origin,corner_order)]:
        if not np.any(selected):continue
        tr=cells[selected].copy()
        if np.any(selected & at_origin):
            for j,row in enumerate(tr):tr[j]=np.roll(row,-np.flatnonzero(np.all(points[row]==0,axis=1))[0])
        N,w=quadrature(q);x=np.einsum('qa,eak->eqk',N,points[tr]);value,gradient=exact(x)
        interp=np.einsum('qa,ea->eq',N,u[tr]);weight=2*area[selected,None]*w[None,:]
        tot[0]+=np.sum(weight*(interp-value)**2);tot[1]+=np.sum(weight*np.sum((grad[selected,None,:]-gradient)**2,axis=-1))
    return np.sqrt(tot)


def solve(n,family):
    points,cells,boundary=mesh(n,family);area,G=geometry(points,cells);N,w=quadrature(6)
    ke=area[:,None,None]*np.einsum('eik,ejk->eij',G,G)
    K=coo_matrix((ke.ravel(),(np.repeat(cells,3,axis=1).ravel(),np.tile(cells,(1,3)).ravel())),shape=(len(points),len(points))).tocsr()
    F=np.zeros(len(points));exact=fields.corner if family in ['uniform','graded'] else fields.smooth
    if family not in ['uniform','graded']:
        x=np.einsum('qa,eak->eqk',N,points[cells]);f=2*np.pi**2*fields.smooth(x)[0]
        fe=2*area[:,None]*np.einsum('q,qa,eq->ea',w,N,f);np.add.at(F,cells.ravel(),fe.ravel())
    u=np.zeros(len(points));u[boundary]=exact(points[boundary])[0];free=~boundary;A=K[free][:,free];b=F[free]-K[free][:,boundary]@u[boundary];u[free]=spsolve(A,b)
    error=norms(points,cells,u,family);fine=norms(points,cells,u,family,12,96)
    lengths=np.stack([np.linalg.norm(points[cells[:,(j+1)%3]]-points[cells[:,j]],axis=1) for j in range(3)],axis=1)
    angles=[]
    for j in range(3):
        a=points[cells[:,(j+1)%3]]-points[cells[:,j]];bvec=points[cells[:,(j+2)%3]]-points[cells[:,j]]
        angles.append(np.arctan2(2*area,np.sum(a*bvec,axis=1)))
    lu=splu(A.tocsc());inv=LinearOperator(A.shape,matvec=lu.solve,rmatvec=lu.solve)
    cond=float(np.max(np.asarray(abs(A).sum(axis=0)))*onenormest(inv))
    row=dict(n=n,family=family,dofs=int(free.sum()),l2=float(error[0]),h1=float(error[1]),
        quadrature_relative_gap=float(np.max(abs(fine-error)/fine)),minimum_area=float(area.min()),
        minimum_angle_degrees=float(np.rad2deg(np.min(angles))),maximum_aspect=float(np.max(lengths.max(axis=1)**2/(2*area))),
        condition_one_norm_estimate=cond,residual=float(np.max(abs(A@u[free]-b))),
        boundary_error=float(np.max(abs(u[boundary]-exact(points[boundary])[0]))),
        symmetry=float(abs(A-A.T).max()) if (A-A.T).nnz else 0.)
    return row,dict(points=points,cells=cells,u=u,reference=exact(points)[0],boundary=boundary)
