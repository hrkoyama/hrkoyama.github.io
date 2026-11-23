"""Independent direct2P potential/analytic electric field, Lindbo--Tornberg Eq4.

Only lateral images; complete horizontal zero mode and matching self term.
No production Ewald function or3P extrapolation is imported.
"""
from itertools import product
import math
import numpy as np
from scipy.special import erfc,erfcx,erf

def screened(k,z,alpha,sign):
    b=k/(2*alpha)+sign*alpha*z;out=np.empty_like(k);positive=b>=0
    out[positive]=np.exp(-k[positive]**2/(4*alpha**2)-alpha**2*z*z)*erfcx(b[positive])
    out[~positive]=np.exp(sign*k[~positive]*z)*erfc(b[~positive])
    return out

def evaluate(sources,charges,lateral,alpha,rcut,kcut,targets=None,self_indices=None,include_zero=True):
    sources=np.array(sources,float);charges=np.asarray(charges,float);L=np.asarray(lateral,float)
    if abs(float(sum(charges)))>1e-13:raise ValueError('Neutral2P system required')
    sources[:,:2]%=L
    if targets is None:targets=sources.copy();self_indices=np.arange(len(sources))
    else:targets=np.array(targets,float)
    targets[:,:2]%=L
    if self_indices is None:self_indices=np.full(len(targets),-1,int)
    A=float(L[0]*L[1]);cut=[int(math.ceil(kcut*l/(2*math.pi))) for l in L]
    wave=np.array([[2*math.pi*i/L[0],2*math.pi*j/L[1]] for i in range(-cut[0],cut[0]+1) for j in range(-cut[1],cut[1]+1) if 0<(2*math.pi*i/L[0])**2+(2*math.pi*j/L[1])**2<=kcut*kcut]);norm=np.sqrt(np.sum(wave*wave,axis=1));images=list(product(*(range(-int(math.ceil(rcut/l))-1,int(math.ceil(rcut/l))+2) for l in L)))
    phi=np.zeros(len(targets));field=np.zeros_like(targets);zero_phi=np.zeros(len(targets))
    for i,t in enumerate(targets):
        for j,(source,q) in enumerate(zip(sources,charges)):
            rho=t[:2]-source[:2];z=float(t[2]-source[2])
            for a,b in images:
                if j==self_indices[i] and a==b==0:continue
                d=np.array([rho[0]+a*L[0],rho[1]+b*L[1],z]);r2=float(sum(v*v for v in d))
                if r2==0:raise ValueError('Coincident distinct2P points')
                if r2>rcut*rcut:continue
                r=math.sqrt(r2);v=math.erfc(alpha*r)/r;phi[i]+=q*v
                field[i]+=q*d*(v/r2+2*alpha/math.sqrt(math.pi)*math.exp(-alpha*alpha*r2)/r2)
            plus=screened(norm,z,alpha,1);minus=screened(norm,z,alpha,-1);phase=wave[:,0]*rho[0]+wave[:,1]*rho[1];c=np.cos(phase);s=np.sin(phase);h=(plus+minus)/norm
            phi[i]+=math.pi/A*q*np.sum(c*h)
            field[i,:2]+=math.pi/A*q*np.sum((s*h)[:,None]*wave,axis=0)
            field[i,2]-=math.pi/A*q*np.sum(c*(plus-minus))
            zp=-2*math.pi/A*q*(z*math.erf(alpha*z)+math.exp(-alpha*alpha*z*z)/(alpha*math.sqrt(math.pi)));zero_phi[i]+=zp
            if include_zero:phi[i]+=zp;field[i,2]+=2*math.pi/A*q*math.erf(alpha*z)
        if self_indices[i]>=0:phi[i]-=2*alpha/math.sqrt(math.pi)*charges[self_indices[i]]
    return phi,field,zero_phi

def energy_force(x,q,L,alpha=4.,rcut=2.5,kcut=64.,include_zero=True):
    phi,E,zero=evaluate(x,q,L,alpha,rcut,kcut,include_zero=include_zero)
    return .5*float(sum(float(a)*float(b) for a,b in zip(q,phi))),np.asarray(q)[:,None]*E,dict(potential=phi,zero_potential=zero,electric_field=E)
