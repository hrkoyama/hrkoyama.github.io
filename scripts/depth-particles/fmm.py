"""Uniform-tree complex-variable 2D Laplace FMM with P2M/M2M/M2L/L2L/P2P.

Potential kernel is -log(r); electric field is -grad(phi), without self terms.
Free-space square domain, no periodic images, adaptivity or asymptotic timing claim.
"""
from math import comb
import numpy as np


def direct(z,q):
    delta=z[:,None]-z[None,:];np.fill_diagonal(delta,1.)
    potential=-np.sum(np.log(np.abs(delta))*q[None,:],axis=1)
    reciprocal=1/delta;np.fill_diagonal(reciprocal,0.)
    field=np.sum(reciprocal*q[None,:],axis=1)
    return potential,np.column_stack((field.real,-field.imag))


def fmm(z,q,order=12,depth=3):
    z=np.asarray(z,dtype=complex);q=np.asarray(q,dtype=float)
    if z.ndim!=1 or q.shape!=z.shape or len(z)<2 or not np.isfinite(z).all() or not np.isfinite(q).all():
        raise ValueError('Finite particle vectors required')
    if not np.all((z.real>=0)&(z.real<1)&(z.imag>=0)&(z.imag<1)) or depth<1 or not 1<=order<=20:
        raise ValueError('Unit-square particles, depth>=1 and 1<=order<=20 required')
    if len(np.unique(z))!=len(z):raise ValueError('Coincident particles')
    centers=lambda level,i,j:complex(i+.5,j+.5)/2**level
    moments={};locals_={};bins={}
    for level in range(depth+1):
        n=2**level
        for i in range(n):
            for j in range(n):
                moments[level,i,j]=np.zeros(order+1,complex)
                locals_[level,i,j]=np.zeros(order+1,complex)
    n=2**depth
    for index,value in enumerate(z):bins.setdefault((int(value.real*n),int(value.imag*n)),[]).append(index)
    for (i,j),ids in bins.items():
        w=z[ids]-centers(depth,i,j)
        moments[depth,i,j]=np.array([np.dot(q[ids],w**k) for k in range(order+1)])
    # Upward translation of moments, not direct recomputation at coarse levels.
    for level in range(depth-1,-1,-1):
        for i in range(2**level):
            for j in range(2**level):
                out=moments[level,i,j]
                for di in range(2):
                    for dj in range(2):
                        child=(level+1,2*i+di,2*j+dj);offset=centers(*child)-centers(level,i,j)
                        for k in range(order+1):
                            out[k]+=sum(comb(k,l)*offset**(k-l)*moments[child][l] for l in range(k+1))
    cache={};m2l_count=0;l2l_count=0
    for level in range(1,depth+1):
        n=2**level
        for i in range(n):
            for j in range(n):
                parent=locals_[level-1,i//2,j//2]
                offset=centers(level,i,j)-centers(level-1,i//2,j//2)
                local=locals_[level,i,j]
                for l in range(order+1):local[l]+=sum(comb(k,l)*parent[k]*offset**(k-l) for k in range(l,order+1))
                l2l_count+=1
                for pi in range(max(0,i//2-1),min(n//2,i//2+2)):
                    for pj in range(max(0,j//2-1),min(n//2,j//2+2)):
                        for si in (2*pi,2*pi+1):
                            for sj in (2*pj,2*pj+1):
                                if max(abs(si-i),abs(sj-j))<=1:continue
                                key=(level,i-si,j-sj)
                                if key not in cache:
                                    d=complex(i-si,j-sj)/n;t=np.zeros((order+1,order+1),complex)
                                    t[0,0]=np.log(d)
                                    for l in range(1,order+1):t[l,0]=(-1)**(l+1)/(l*d**l)
                                    for k in range(1,order+1):
                                        for l in range(order+1):t[l,k]=-(-1)**l*comb(k+l-1,l)/(k*d**(k+l))
                                    cache[key]=t
                                local+=np.sum(cache[key]*moments[level,si,sj][None,:],axis=1);m2l_count+=1
    potential=np.zeros(len(z));field=np.zeros(len(z),complex);near_pairs=0
    for (i,j),ids in bins.items():
        w=z[ids]-centers(depth,i,j);coeff=locals_[depth,i,j]
        f=np.polynomial.polynomial.polyval(w,coeff)
        derivative=np.polynomial.polynomial.polyval(w,np.arange(1,order+1)*coeff[1:])
        for si in range(max(0,i-1),min(n,i+2)):
            for sj in range(max(0,j-1),min(n,j+2)):
                other=bins.get((si,sj),[])
                if not other:continue
                delta=z[ids,None]-z[None,other];valid=np.array(ids)[:,None]!=np.array(other)[None,:]
                safe=np.where(valid,delta,1.)
                f+=np.sum(np.log(safe)*q[None,other],axis=1)
                derivative+=np.sum(np.where(valid,1/safe,0.)*q[None,other],axis=1)
                near_pairs+=int(valid.sum())
        potential[ids]=-f.real;field[ids]=derivative
    return potential,np.column_stack((field.real,-field.imag)),dict(m2l_translations=m2l_count,l2l_translations=l2l_count,near_pairs=near_pairs,all_pairs=len(z)*(len(z)-1))
