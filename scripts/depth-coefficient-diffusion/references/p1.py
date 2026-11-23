"""Independent aligned triangular weak-form reference, not the primary FV matrix."""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

def solve(n):
    # Two triangles per cell, independently integrated constant coefficient/source.
    y,x=np.mgrid[0:n+1,0:n+1];xy=np.column_stack([x.ravel()/n,y.ravel()/n]);j=(y[:-1,:-1]*(n+1)+x[:-1,:-1]).ravel()
    triangles=np.concatenate([np.stack([j,j+1,j+n+2],axis=1),np.stack([j,j+n+2,j+n+1],axis=1)])
    v=xy[triangles];det=(v[:,1,0]-v[:,0,0])*(v[:,2,1]-v[:,0,1])-(v[:,2,0]-v[:,0,0])*(v[:,1,1]-v[:,0,1]);area=det/2
    g=np.stack([v[:,1]-v[:,2],v[:,2]-v[:,0],v[:,0]-v[:,1]],axis=1);g=np.stack([g[:,:,1],-g[:,:,0]],axis=-1)/det[:,None,None]
    c=v.mean(axis=1);a=np.where((c[:,0]<.5)==(c[:,1]<.5),100.,1.)
    k=area[:,None,None]*a[:,None,None]*np.einsum('eai,ebi->eab',g,g)
    A=sparse.coo_matrix((k.ravel(),(np.repeat(triangles,3,axis=1).ravel(),np.tile(triangles,(1,3)).ravel())),shape=(len(xy),len(xy))).tocsr()
    b=np.bincount(triangles.ravel(),weights=np.repeat(area/3,3),minlength=len(xy));interior=np.flatnonzero(np.all((xy>0)&(xy<1),axis=1));u=np.zeros(len(xy));u[interior]=spsolve(A[interior][:,interior],b[interior])
    return u.reshape(n+1,n+1)

def evaluate(u,X,Y):
    n=len(u)-1;i=np.minimum((X*n).astype(int),n-1);j=np.minimum((Y*n).astype(int),n-1);r=X*n-i;s=Y*n-j
    return np.where(s<=r,(1-r)*u[j,i]+(r-s)*u[j,i+1]+s*u[j+1,i+1],(1-s)*u[j,i]+r*u[j+1,i+1]+(s-r)*u[j+1,i])
