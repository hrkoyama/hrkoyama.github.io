"""Small independently authored educational dense algorithms.

Reduced least-squares/Ritz problems use SciPy LAPACK. Global reference solves
and spectra are assembled separately. No production/scalability claim.
"""
import numpy as np
from scipy.linalg import lstsq, eig, eigh


def mv(a, x):
    return np.einsum('ij,j...->i...', a, x, optimize=False)


def mm(a, b):
    return np.einsum('ij,jk->ik', a, b, optimize=False)


def norm(x):
    return float(np.sqrt(np.sum(np.asarray(x)**2)))


def lu_factor(a, dtype=np.float64):
    u=np.array(a,dtype=dtype,copy=True);n=len(u);p=np.arange(n)
    if u.shape!=(n,n) or not np.isfinite(u).all():raise ValueError('finite square matrix required')
    for k in range(n):
        pivot=k+int(np.argmax(abs(u[k:,k])))
        if u[pivot,k]==0:raise ArithmeticError('singular pivot')
        if pivot!=k:u[[k,pivot]]=u[[pivot,k]];p[[k,pivot]]=p[[pivot,k]]
        if k+1<n:
            u[k+1:,k]/=u[k,k]
            u[k+1:,k+1:]-=u[k+1:,k,None]*u[None,k,k+1:]
    return u,p


def lu_solve(factor, b):
    u,p=factor;x=np.array(b,dtype=u.dtype,copy=True)[p];n=len(u)
    for k in range(n):x[k]-=np.sum(u[k,:k]*x[:k])
    for k in range(n-1,-1,-1):x[k]=(x[k]-np.sum(u[k,k+1:]*x[k+1:]))/u[k,k]
    return x


def cholesky(a,dtype=np.float64):
    a=np.asarray(a,dtype=dtype);n=len(a)
    if a.shape!=(n,n) or not np.allclose(a,a.T,rtol=0,atol=0):raise ValueError('symmetric matrix required')
    l=np.zeros_like(a)
    for i in range(n):
        for j in range(i+1):
            value=a[i,j]-np.sum(l[i,:j]*l[j,:j])
            if i==j:
                if value<=0:raise ArithmeticError('non-positive Cholesky pivot')
                l[i,j]=np.sqrt(value)
            else:l[i,j]=value/l[j,j]
    return l


def triangular(l,b,transpose=False):
    x=np.array(b,dtype=l.dtype,copy=True);n=len(l)
    indices=range(n-1,-1,-1) if transpose else range(n)
    for i in indices:
        x[i]=(x[i]-np.sum(l[i+1:,i]*x[i+1:]) if transpose else x[i]-np.sum(l[i,:i]*x[:i]))/l[i,i]
    return x


def chol_solve(l,b):
    b=np.asarray(b)
    if b.ndim==2:return np.column_stack([chol_solve(l,b[:,j]) for j in range(b.shape[1])])
    return triangular(l,triangular(l,b),True)


def refine(a,b,kind,steps,progress=lambda **x:None):
    if kind=='lu':
        f=lu_factor(a,np.float32);solve=lambda r:lu_solve(f,r)
        f64=lu_factor(a);u,p=f64;l=np.tril(u,-1)+np.eye(len(a));upper=np.triu(u)
        reconstruction=mm(l,upper);target=a[p]
        u32,p32=f;rec32=mm(np.tril(u32,-1).astype(float)+np.eye(len(a)),np.triu(u32).astype(float));target32=a[p32]
        growth=float(np.max(abs(upper))/np.max(abs(a)))
    elif kind=='cholesky':
        f=cholesky(a,np.float32);solve=lambda r:chol_solve(f,r)
        f64=cholesky(a);reconstruction=mm(f64,f64.T);target=a
        rec32=mm(f.astype(float),f.astype(float).T);target32=a;growth=1.
    else:raise ValueError('unknown factorization')
    x=solve(b).astype(float);history=[x.copy()];progress(x=x,history=np.array(history),stage=np.array('initial-solve'))
    for _ in range(steps):
        residual=b-mv(a,x) # float64 residual, float32 factor/triangular corrections
        x+=solve(residual).astype(float);history.append(x.copy());progress(x=x,history=np.array(history),stage=np.array('refinement'))
    scale=np.max(np.sum(abs(a),axis=1))
    return dict(x=x,history=np.array(history),factor_residual64=float(np.max(np.sum(abs(reconstruction-target),axis=1))/scale),factor_residual32=float(np.max(np.sum(abs(rec32-target32),axis=1))/scale),growth=growth)


def arnoldi(operator,start,dimension,inner=None,progress=lambda **x:None):
    inner=(lambda a,b:float(np.sum(a*b))) if inner is None else inner
    q=np.zeros((len(start),dimension+1));q[:,0]=start/np.sqrt(inner(start,start));h=np.zeros((dimension+1,dimension));calls=0
    for j in range(dimension):
        w=np.array(operator(q[:,j]),copy=True);calls+=1
        for _ in range(2):
            for i in range(j+1):
                v=inner(q[:,i],w);h[i,j]+=v;w-=v*q[:,i]
        squared=inner(w,w)
        if squared<0:raise ArithmeticError('negative inner-product norm')
        beta=np.sqrt(squared);h[j+1,j]=beta;progress(basis=q[:,:j+1],hessenberg=h[:j+2,:j+1],stage=np.array('Arnoldi-candidate'))
        if beta<=1e-13:return q[:,:j+1],h[:j+2,:j+1],calls,True
        q[:,j+1]=w/beta
    return q[:,:dimension],h,calls,False


def krylov_linear(a,b,method,tolerance,max_iterations,preconditioner=None,progress=lambda **x:None):
    n=len(a);l=np.eye(n) if preconditioner is None else cholesky(preconditioner)
    # Congruence, not left multiplication: preserve symmetric MINRES operator.
    invl=np.column_stack([triangular(l,np.eye(n)[:,j]) for j in range(n)])
    transformed=mm(mm(invl,a),invl.T);rhs=mv(invl,b);beta=norm(rhs);v0=rhs/beta
    q=np.zeros((n,max_iterations+1));q[:,0]=v0;h=np.zeros((max_iterations+1,max_iterations));history=[];orth=[];last=np.zeros(n);previous_beta=0.;diagonal=[]
    for j in range(max_iterations):
        w=mv(transformed,q[:,j])
        if method=='minres':
            if j:w-=previous_beta*q[:,j-1]
            alpha=float(np.sum(q[:,j]*w));diagonal.append(alpha);w-=alpha*q[:,j]
            for _ in range(2):
                for i in range(j+1):w-=float(np.sum(q[:,i]*w))*q[:,i]
            h[j,j]=alpha
            if j:h[j-1,j]=previous_beta
        elif method=='gmres':
            for _ in range(2):
                for i in range(j+1):
                    correction=float(np.sum(q[:,i]*w));h[i,j]+=correction;w-=correction*q[:,i]
        else:raise ValueError('unknown Krylov linear method')
        next_beta=norm(w);h[j+1,j]=next_beta;right=np.zeros(j+2);right[0]=beta
        progress(basis=q[:,:j+1],hessenberg=h[:j+2,:j+1],stage=np.array('before-reduced-lstsq'))
        y=lstsq(h[:j+2,:j+1],right,lapack_driver='gelsy')[0]
        z=mv(q[:,:j+1],y);last=mv(invl.T,z);true_residual=norm(b-mv(a,last))/norm(b)
        history.append(true_residual);orth.append(float(np.max(abs(mm(q[:,:j+1].T,q[:,:j+1])-np.eye(j+1)))));progress(x=last,history=np.array(history),basis=q[:,:j+1],stage=np.array('linear-iterate'))
        if true_residual<=tolerance:return dict(x=last,history=np.array(history),orthogonality=np.array(orth),iterations=j+1,converged=True,transform_symmetry=float(np.max(abs(transformed-transformed.T))))
        if next_beta<=1e-14:break
        q[:,j+1]=w/next_beta;previous_beta=next_beta
    return dict(x=last,history=np.array(history),orthogonality=np.array(orth),iterations=len(history),converged=False,transform_symmetry=float(np.max(abs(transformed-transformed.T))))


def curvature_guard(a,b):
    if float(np.sum(b*mv(a,b)))<=0:raise ArithmeticError('CG non-positive curvature: SPD prerequisite fails')


def restarted_eigen(a,start,restart,cycles,tolerance,shift=None,progress=lambda **x:None):
    factor=None if shift is None else lu_factor(a-shift*np.eye(len(a)))
    linear_errors=[];op_calls=[0];a_calls=0;history=[];vectors=[];start=start.copy();scale=float(np.max(np.sum(abs(a),axis=1)))
    def action(v):
        op_calls[0]+=1
        if factor is None:return mv(a,v)
        y=lu_solve(factor,v);res=norm(mv(a-shift*np.eye(len(a)),y)-v)/(norm(v)+norm(y)*scale)
        linear_errors.append(res)
        if res>2e-12:
            progress(shift_rhs=v,shift_candidate=y,shift_residual=np.array(res),stage=np.array('failed-shift-solve'))
            raise ArithmeticError('shift solve failed fixed residual guard')
        return y
    for cycle in range(cycles):
        q,h,_,happy=arnoldi(action,start,min(restart,len(a)),progress=progress)
        values,small=eig(h[:len(q.T),:]);j=int(np.argmax(abs(values)))
        if abs(values[j].imag)>1e-10 or np.max(abs(small[:,j].imag))>1e-10:raise ArithmeticError('unexpected complex Ritz pair for symmetric operator')
        vector=mv(q,small[:,j].real);vector/=norm(vector);av=mv(a,vector);a_calls+=1;value=float(np.sum(vector*av));residual=norm(av-value*vector)/(scale+abs(value))
        recovered=float(values[j].real) if shift is None else shift+1/float(values[j].real)
        orth=float(np.max(abs(mm(q.T,q)-np.eye(len(q.T)))));history.append([cycle+1,value,recovered,residual,op_calls[0],a_calls,orth]);vectors.append(vector.copy());start=vector;progress(vector=vector,history=np.array(history),vectors=np.array(vectors),stage=np.array('Ritz-restart'))
        if residual<=tolerance:break
    return dict(value=value,vector=vector,history=np.array(history),vectors=np.array(vectors),operator_calls=op_calls[0],residual_matrix_actions=a_calls,shift_solve_residuals=np.array(linear_errors),converged=bool(residual<=tolerance))


def mass_krylov(k,m,start,dimension,number,progress=lambda **x:None):
    l=cholesky(k);calls=[0]
    def action(v):calls[0]+=1;return chol_solve(l,mv(m,v))
    inner=lambda a,b:float(np.sum(a*mv(m,b)))
    q,h,_,happy=arnoldi(action,start,min(dimension,len(k)),inner,progress)
    kr=mm(q.T,mm(k,q));mr=mm(q.T,mm(m,q));values,y=eigh(kr,mr,driver='gvd');x=mm(q,y[:,:number])
    return dict(values=values[:number],vectors=x,basis=q,operator_calls=calls[0],happy_breakdown=happy)
