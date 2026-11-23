"""Independent unordered scalar Cartesian pair reference; no tree helper."""
import math
import numpy as np

def direct(x,m,targets=None,self_indices=None):
    x=np.asarray(x);m=np.asarray(m)
    if targets is not None:
        targets=np.asarray(targets);phi=np.zeros(len(targets));a=np.zeros_like(targets)
        if self_indices is None:self_indices=np.full(len(targets),-1,int)
        for i,t in enumerate(targets):
            for j,(s,mass) in enumerate(zip(x,m)):
                if j==self_indices[i]:continue
                d=[float(t[k]-s[k]) for k in range(3)];r=math.sqrt(sum(v*v for v in d))
                if r==0:raise ValueError('Coincidence')
                phi[i]-=mass/r
                for k in range(3):a[i,k]-=mass*d[k]/r**3
        return phi,a
    phi=np.zeros(len(x));a=np.zeros_like(x)
    for i in range(len(x)):
        for j in range(i):
            d=[float(x[i,k]-x[j,k]) for k in range(3)];r=math.sqrt(sum(v*v for v in d))
            if r==0:raise ValueError('Coincident sources')
            phi[i]-=m[j]/r;phi[j]-=m[i]/r
            for k in range(3):a[i,k]-=m[j]*d[k]/r**3;a[j,k]+=m[i]*d[k]/r**3
    return phi,a

def octahedron(a,R):
    if R<=a:raise ValueError('Outer-axis probe required')
    phi=-(1/(R-a)+1/(R+a)+4/math.sqrt(R*R+a*a))/6
    az=-(1/(R-a)**2+1/(R+a)**2+4*R/(R*R+a*a)**1.5)/6
    return phi,az
