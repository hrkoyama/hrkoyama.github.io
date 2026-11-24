"""Slow independent scalar one-step qualification; not used in any main evolution."""
import numpy as np
from geometry import C,W,OPP

def step(f,g,tau):
    n=g['n'];post=np.empty_like(f)
    for j in range(n):
        rho=sum(float(f[q,j]) for q in range(9))
        u=[sum(float(f[q,j])*int(C[q,d]) for q in range(9))/rho for d in range(2)]
        for q in range(9):
            dot=C[q,0]*u[0]+C[q,1]*u[1]
            target=W[q]*rho*(1+3*dot+4.5*dot*dot-1.5*(u[0]*u[0]+u[1]*u[1]))
            post[q,j]=float(f[q,j])+(target-f[q,j])/tau
    new=np.empty_like(f)
    for j in range(n):
        for q in range(9):
            kind=g['kind'][q,j];o=int(OPP[q]);d=g['fraction'][q,j]
            if kind==0:new[q,j]=post[q,int(g['source'][q,j])]
            elif kind in [1,2,3]:
                if d<.5:
                    new[q,j]=(2*d)*post[o,j]+(1-2*d)*post[o,int(g['back'][q,j])]-6*W[o]*g['wall_dot'][q,j]
                else:
                    new[q,j]=(post[o,j]+(2*d-1)*post[q,j]-6*W[o]*g['wall_dot'][q,j])/(2*d)
            else:new[q,j]=0.
    for a,j in enumerate(g['inlet']):
        u=g['inlet_speed'][a];r=(new[0,j]+new[2,j]+new[4,j]+2*(new[3,j]+new[6,j]+new[7,j]))/(1-u)
        new[1,j]=new[3,j]+2*r*u/3
        new[5,j]=new[7,j]+(new[4,j]-new[2,j])/2+r*u/6
        new[8,j]=new[6,j]+(new[2,j]-new[4,j])/2+r*u/6
    for j in g['outlet']:
        source=int(g['source'][1,j]);r0=sum(float(f[q,source]) for q in range(9))
        v=sum(float(f[q,source])*int(C[q,1]) for q in range(9))/r0
        u=-1+new[0,j]+new[2,j]+new[4,j]+2*(new[1,j]+new[5,j]+new[8,j])
        new[3,j]=new[1,j]-2*u/3
        new[6,j]=new[8,j]+(new[4,j]-new[2,j])/2-u/6+v/2
        new[7,j]=new[5,j]+(new[2,j]-new[4,j])/2-u/6-v/2
    return new
