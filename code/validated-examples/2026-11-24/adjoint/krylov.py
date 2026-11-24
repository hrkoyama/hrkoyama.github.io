"""Reviewed numerical GMRES body; status instrumentation lives outside."""
import math
import numpy as np
def dot(a,b):return float(np.sum(np.asarray(a)*np.asarray(b)))
def norm(a):return float(np.sqrt(dot(a,a)))

def gmres(operator,b,preconditioner,restart,maxiter,rtol):
    if not callable(operator):raise TypeError('Matrix-free operator must be callable')
    n=len(b);x=np.zeros(n);target=max(1e-14,rtol*norm(b));history=[norm(b)];iterations=0
    while history[-1]>target and iterations<maxiter:
        r=b if iterations==0 else b-operator(x);beta=norm(r);base=x.copy();m=min(restart,maxiter-iterations,n)
        V=np.zeros((n,m+1));Z=np.zeros((n,m));H=np.zeros((m+1,m));cs=np.zeros(m);sn=np.zeros(m);g=np.zeros(m+1)
        V[:,0]=r/beta;g[0]=beta
        for k in range(m):
            Z[:,k]=preconditioner(V[:,k]);w=np.array(operator(Z[:,k]),copy=True)
            for _ in range(2):
                for i in range(k+1):
                    coefficient=dot(V[:,i],w);H[i,k]+=coefficient;w-=coefficient*V[:,i]
            H[k+1,k]=norm(w);breakdown=H[k+1,k]<=32*np.finfo(float).eps*max(1,norm(H[:k+1,k]))
            if not breakdown:V[:,k+1]=w/H[k+1,k]
            for i in range(k):
                a,bv=H[i,k],H[i+1,k];H[i,k]=cs[i]*a+sn[i]*bv;H[i+1,k]=-sn[i]*a+cs[i]*bv
            length=math.hypot(H[k,k],H[k+1,k])
            if length==0:raise ArithmeticError('GMRES singular small triangular factor')
            cs[k]=H[k,k]/length;sn[k]=H[k+1,k]/length;H[k,k]=length;H[k+1,k]=0.
            g[k+1]=-sn[k]*g[k];g[k]*=cs[k]
            y=np.empty(k+1)
            for i in range(k,-1,-1):y[i]=(g[i]-dot(H[i,i+1:k+1],y[i+1:]))/H[i,i]
            x=base+np.einsum('ij,j->i',Z[:,:k+1],y);true=norm(b-operator(x));history.append(true);iterations+=1
            if not np.isfinite(true):raise FloatingPointError('Nonfinite GMRES residual')
            if true<=target:return dict(x=x,passed=True,iterations=iterations,residuals=np.array(history),basis_columns=k+2)
            if breakdown:return dict(x=x,passed=False,iterations=iterations,residuals=np.array(history),basis_columns=k+2)
    return dict(x=x,passed=history[-1]<=target,iterations=iterations,residuals=np.array(history),basis_columns=min(restart+1,n+1))
