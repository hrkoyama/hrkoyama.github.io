"""Analytically differentiated forcing for the CLOSED static-grey M1 PDE.

Both reduced-flux magnitude and direction vary. Independent complex-step
qualification is in references/mms_reference.py; no numerical differentiation
is used in the production forcing.
"""
import numpy as np


def state_and_forcing(x,y,time):
    shape=np.broadcast_shapes(np.shape(x),np.shape(y));x,y=np.broadcast_arrays(x,y)
    phase=2*np.pi*(x+y-time);theta=2*np.pi*(x-time);eta=2*np.pi*(y+time)
    energy=1+.1*np.sin(phase);g=np.stack([.2+.05*np.sin(theta),.1+.03*np.cos(eta)],axis=-1)
    e_space=.2*np.pi*np.cos(phase);de=[e_space,e_space,-e_space]
    gx=.1*np.pi*np.cos(theta);gy=-.06*np.pi*np.sin(eta);zero=np.zeros(shape)
    dg=[np.stack([gx,zero],axis=-1),np.stack([zero,gy],axis=-1),np.stack([-gx,gy],axis=-1)]
    f=np.sqrt(np.sum(g*g,axis=-1));n=g/f[...,None];s=np.sqrt(4-3*f*f)
    chi=(3+4*f*f)/(5+2*s);B=(3*chi-1)/2
    eye=np.eye(2);nn=n[..., :,None]*n[...,None,:]
    tensor=(1-chi)[...,None,None]/2*eye+B[...,None,None]*nn
    dchi=(8*f*(5+2*s)+(3+4*f*f)*6*f/s)/(5+2*s)**2
    dp=[];df=[]
    for ee,gg in zip(de,dg):
        ff=np.sum(g*gg,axis=-1)/f;cc=dchi*ff
        dn=gg/f[...,None]-g*ff[...,None]/f[...,None]**2
        dtensor=-.5*cc[...,None,None]*eye+1.5*cc[...,None,None]*nn+B[...,None,None]*(dn[..., :,None]*n[...,None,:]+n[..., :,None]*dn[...,None,:])
        dp.append(ee[...,None,None]*tensor+energy[...,None,None]*dtensor)
        df.append(ee[...,None]*g+energy[...,None]*gg)
    state=np.concatenate([energy[...,None],energy[...,None]*g],axis=-1)
    forcing=np.stack([de[2]+df[0][...,0]+df[1][...,1],df[2][...,0]+dp[0][...,0,0]+dp[1][...,0,1],df[2][...,1]+dp[0][...,0,1]+dp[1][...,1,1]],axis=-1)
    return state,forcing
