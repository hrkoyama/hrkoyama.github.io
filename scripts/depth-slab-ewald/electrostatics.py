"""Original orthorhombic3P tin-foil Ewald plus neutral YB slab correction.

Coulomb constant1; physical z is never independently wrapped for Mz.
Full +/- reciprocal lattice; energy coefficient2pi/V.
"""
from itertools import product
import numpy as np
from scipy.special import erfc

def validate(x,q,lengths):
    x=np.asarray(x,float);q=np.asarray(q,float);L=np.asarray(lengths,float)
    if x.ndim!=2 or x.shape[1]!=3 or q.shape!=(len(x),) or L.shape!=(3,):raise ValueError('Invalid particle/box shape')
    if not all(np.isfinite(a).all() for a in [x,q,L]) or np.min(L)<=0:raise ValueError('Finite positions/charges and positive box required')
    if abs(float(q.sum()))>1e-13:raise ValueError('Neutral cell required; no background')
    if np.any(np.linalg.norm(x[:,None]-x[None,:],axis=-1)[~np.eye(len(x),dtype=bool)]==0):raise ValueError('Coincident distinct sources')
    return x,q,L

def ewald3p(x,q,lengths,alpha=3.,real_cutoff=2.5,k_cutoff=64.):
    x,q,L=validate(x,q,lengths);x=x.copy();x[:,:2]%=L[:2]
    if alpha<=0 or real_cutoff<=0 or k_cutoff<=0:raise ValueError('Positive cutoffs/splitting required')
    phi=np.zeros(len(x));F=np.zeros_like(x);qq=q[:,None]*q[None,:];difference=x[:,None,:]-x[None,:,:]
    ranges=[range(-int(np.ceil(real_cutoff/l))-1,int(np.ceil(real_cutoff/l))+2) for l in L]
    for image in product(*ranges):
        d=difference+np.array(image)*L;r2=np.sum(d*d,axis=-1);mask=(r2>0)&(r2<=real_cutoff**2)
        inverse=np.zeros_like(r2);inverse[mask]=1/np.sqrt(r2[mask]);r=np.zeros_like(r2);r[mask]=1/inverse[mask]
        value=erfc(alpha*r)*inverse;phi+=np.sum(value*q[None,:],axis=1)
        factor=value*inverse**2+2*alpha/np.sqrt(np.pi)*np.exp(-alpha**2*r2)*inverse**2
        F+=np.einsum('ij,ijk->ik',qq*factor,d,optimize=False)
    counts=np.ceil(k_cutoff*L/(2*np.pi)).astype(int)
    integer=np.array(list(product(*(range(-n,n+1) for n in counts))),float);k=2*np.pi*integer/L;k2=np.sum(k*k,axis=1);keep=(k2>0)&(k2<=k_cutoff**2);k=k[keep];k2=k2[keep]
    phase=np.einsum('id,kd->ik',x,k,optimize=False);C=np.cos(phase);S=np.sin(phase);rhoC=np.sum(q[:,None]*C,axis=0);rhoS=np.sum(q[:,None]*S,axis=0);g=np.exp(-k2/(4*alpha**2))/k2;V=float(np.prod(L))
    phi+=4*np.pi/V*np.sum(g[None,:]*(C*rhoC[None,:]+S*rhoS[None,:]),axis=1)-2*alpha/np.sqrt(np.pi)*q
    F+=4*np.pi/V*q[:,None]*np.einsum('ik,kd->id',g[None,:]*(S*rhoC[None,:]-C*rhoS[None,:]),k,optimize=False)
    energy=.5*float(np.sum(q*phi))
    return energy,F,dict(potential=phi,reciprocal_count=len(k),volume=V)

def correction(x,q,lengths):
    x,q,L=validate(x,q,lengths);mz=float(np.sum(q*x[:,2]));V=float(np.prod(L));force=np.zeros_like(x);force[:,2]=-4*np.pi*q*mz/V
    return 2*np.pi*mz*mz/V,force

def corrected(x,q,lengths,alpha=3.,real_cutoff=2.5,k_cutoff=64.):
    energy,F,data=ewald3p(x,q,lengths,alpha,real_cutoff,k_cutoff);de,df=correction(x,q,lengths)
    return energy+de,F+df,dict(**data,uncorrected_energy=energy,uncorrected_force=F,correction_energy=de,correction_force=df)
