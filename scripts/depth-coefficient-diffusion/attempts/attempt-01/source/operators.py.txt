"""Two distinct conservative/variational diffusion discretizations, unit square."""
import numpy as np
from scipy import sparse


def scalar_fv(n, patch=False):
    h=1/n; x=(np.arange(n)+.5)*h; X,Y=np.meshgrid(x,x)
    a=np.where(X<.5,1.,100.) if patch else np.where((X<.5)==(Y<.5),100.,1.)
    ids=np.arange(n*n).reshape(n,n); rows=[];cols=[];vals=[]
    diag=np.zeros((n,n)); b=np.zeros((n,n)) if patch else np.full((n,n),h*h)
    faces=[]; boundary=[]
    for axis in (0,1):
        left=(slice(None,-1),slice(None)) if axis==0 else (slice(None),slice(None,-1))
        right=(slice(1,None),slice(None)) if axis==0 else (slice(None),slice(1,None))
        t=2*a[left]*a[right]/(a[left]+a[right]);i=ids[left].ravel();j=ids[right].ravel()
        diag[left]+=t;diag[right]+=t
        rows.extend([i,j]);cols.extend([j,i]);vals.extend([-t.ravel(),-t.ravel()]);faces.append((i,j,t.ravel()))
    for side in range(4):
        if patch and side<2: continue  # y walls are homogeneous Neumann
        index=(0,slice(None)) if side==0 else (-1,slice(None)) if side==1 else (slice(None),0) if side==2 else (slice(None),-1)
        t=2*a[index];g=1. if patch and side==3 else 0.
        diag[index]+=t;b[index]+=t*g;boundary.append((ids[index].ravel(),t.ravel(),g))
    rows.append(ids.ravel());cols.append(ids.ravel());vals.append(diag.ravel())
    A=sparse.coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(n*n,n*n)).tocsr()
    return A,b.ravel(),(X.ravel(),Y.ravel(),a.ravel()),faces,boundary


def tensor():
    c,s=np.cos(np.pi/6),np.sin(np.pi/6); R=np.array([[c,-s],[s,c]])
    return np.einsum('ik,k,jk->ij',R,[1.,.01],R)


def shape(r,s):
    v=np.array([(1-r)*(1-s),(1+r)*(1-s),(1+r)*(1+s),(1-r)*(1+s)])/4
    grad=np.array([[-(1-s),-(1-r)],[(1-s),-(1+r)],[(1+s),(1+r)],[-(1+s),(1-r)]])/4
    return v,grad


def q1(n, mode='sine', quadrature=4):
    K=tensor();h=1/n; y,x=np.mgrid[0:n,0:n];i=(y*(n+1)+x).ravel(); el=np.stack([i,i+1,i+n+2,i+n+1],axis=1)
    points=np.stack(np.meshgrid(np.linspace(0,1,n+1),np.linspace(0,1,n+1)),axis=-1).reshape(-1,2)
    stiff=np.zeros((4,4)); load=np.zeros((len(el),4));q,w=np.polynomial.legendre.leggauss(quadrature)
    for r,wr in zip(q,w):
        for s,ws in zip(q,w):
            N,G=shape(r,s);G=G*2/h;weight=wr*ws*h*h/4
            stiff+=weight*np.einsum('ai,ij,bj->ab',G,K,G)
            X=(x.ravel()+(r+1)/2)*h;Y=(y.ravel()+(s+1)/2)*h
            f=np.full(len(el),-2*K[0,1]) if mode=='xy' else np.zeros(len(el)) if mode=='affine' else np.pi**2*((K[0,0]+K[1,1])*np.sin(np.pi*X)*np.sin(np.pi*Y)-2*K[0,1]*np.cos(np.pi*X)*np.cos(np.pi*Y))
            load+=weight*f[:,None]*N
    A=sparse.coo_matrix((np.broadcast_to(stiff,(len(el),4,4)).ravel(),(np.repeat(el,4,axis=1).ravel(),np.tile(el,(1,4)).ravel())),shape=(len(points),len(points))).tocsr()
    b=np.bincount(el.ravel(),weights=load.ravel(),minlength=len(points));interior=np.flatnonzero(np.all((points>0)&(points<1),axis=1));boundary=np.setdiff1d(np.arange(len(points)),interior)
    g=points[:,0]*points[:,1] if mode=='xy' else points[:,0]+2*points[:,1] if mode=='affine' else np.zeros(len(points))
    b=b[interior]-A[interior][:,boundary]@g[boundary]
    return A[interior][:,interior].tocsr(),b,points,el,interior,g


def q1_error(n,values,order=4):
    h=1/n;u=values.reshape(n+1,n+1);q,w=np.polynomial.legendre.leggauss(order);err=energy=norm=0.;K=tensor()
    for r,wr in zip(q,w):
        for s,ws in zip(q,w):
            N,G=shape(r,s);G*=2/h
            V=np.stack([u[:-1,:-1],u[:-1,1:],u[1:,1:],u[1:,:-1]],axis=-1)
            X,Y=np.meshgrid((np.arange(n)+(r+1)/2)*h,(np.arange(n)+(s+1)/2)*h)
            exact=np.sin(np.pi*X)*np.sin(np.pi*Y);diff=np.sum(V*N,axis=-1)-exact
            grad=np.einsum('...a,ai->...i',V,G)-np.stack([np.pi*np.cos(np.pi*X)*np.sin(np.pi*Y),np.pi*np.sin(np.pi*X)*np.cos(np.pi*Y)],axis=-1)
            weight=wr*ws*h*h/4;err+=weight*np.sum(diff*diff);norm+=weight*np.sum(exact*exact);energy+=weight*np.einsum('abi,ij,abj->',grad,K,grad)
    return float(np.sqrt(err/norm)),float(np.sqrt(energy))
