"""Independent pointwise analytic CPAW integration; no numerical evolution."""
import numpy as np


def wave_means(n,time):
    nodes,weights=np.polynomial.legendre.leggauss(16)
    x=(np.arange(n)[:,None]+.5+.5*nodes[None,:])/n
    phase=2*np.pi*(x-time)
    w=np.zeros((n,len(nodes),8));w[...,0]=1;w[...,4]=.1;w[...,5]=1
    w[...,6]=.1*np.cos(phase);w[...,7]=.1*np.sin(phase);w[...,2:4]=-w[...,6:8]
    q=w.copy();q[...,1:4]*=w[...,0,None]
    q[...,4]=w[...,4]/(2/3)+.5*w[...,0]*np.sum(w[...,1:4]**2,axis=-1)+.5*np.sum(w[...,5:8]**2,axis=-1)
    return .5*np.einsum('ijk,j->ik',q,weights)
