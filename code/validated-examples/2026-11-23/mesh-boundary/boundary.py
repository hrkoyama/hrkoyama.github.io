"""Cell-centred 2D Poisson with explicit Neumann/Robin face fluxes."""
import numpy as np
from scipy.sparse import coo_matrix,bmat,csr_matrix
from scipy.sparse.linalg import spsolve,cg


def assemble(n,kind,forcing_offset=0.):
    h=1/n;y,x=np.meshgrid((np.arange(n)+.5)*h,(np.arange(n)+.5)*h,indexing='ij')
    if kind=='neumann':ref=np.cos(2*np.pi*x)*np.cos(2*np.pi*y);f=8*np.pi**2*ref
    else:ref=np.cos(np.pi*x)*np.cos(2*np.pi*y)+x+y;f=5*np.pi**2*np.cos(np.pi*x)*np.cos(2*np.pi*y)
    rhs=(f+forcing_offset).ravel()*h*h;rows=[];cols=[];vals=[];diagonal=np.zeros(n*n);faces=[]
    for j in range(n):
        for i in range(n):
            k=j*n+i
            for dj,di in [(0,-1),(0,1),(-1,0),(1,0)]:
                jj,ii=j+dj,i+di
                if 0<=jj<n and 0<=ii<n:
                    rows.append(k);cols.append(jj*n+ii);vals.append(-1.);diagonal[k]+=1
                else:
                    if kind=='neumann':alpha,beta,g,exact_flux=0.,1.,0.,0.
                    elif di!=0:alpha,beta,g,exact_flux=0.,1.,float(di),float(di)
                    else:
                        alpha,beta=1.,.5
                        yy=0. if dj<0 else 1.;xx=x[j,i]
                        exact_value=np.cos(np.pi*xx)+xx+yy;exact_flux=float(dj)
                        g=alpha*exact_value+beta*exact_flux
                    denominator=beta+alpha*h/2
                    diagonal[k]+=h*alpha/denominator;rhs[k]+=h*g/denominator
                    faces.append([k,di,dj,alpha,beta,g,exact_flux])
    rows+=list(range(n*n));cols+=list(range(n*n));vals+=diagonal.tolist()
    A=coo_matrix((vals,(rows,cols)),shape=(n*n,n*n)).tocsr()
    return A,rhs,ref,np.array(faces),f


def solve(n,kind,mean=0.,forcing_offset=0.):
    A,b,ref,faces,f=assemble(n,kind,forcing_offset);h=1/n;compat=float(b.sum())
    if kind=='neumann':
        if abs(compat)>1e-11*max(1,np.sum(abs(b))):raise ValueError('Incompatible Neumann source; no mean subtraction')
        w=np.full(n*n,h*h);C=csr_matrix(w[:,None]);aug=bmat([[A,C],[C.T,None]],format='csr')
        full=spsolve(aug,np.r_[b,mean]);u=full[:-1];lagrange=float(full[-1])
        other,info=cg(A,b,rtol=1e-12,atol=1e-14,maxiter=4000)
        if info:raise ArithmeticError('Projected-compatible CG did not converge')
        other+=mean-np.mean(other);solver_gap=float(np.max(abs(other-u)))
        ref=ref+mean
    else:u=spsolve(A,b);lagrange=0.;solver_gap=0.
    k=faces[:,0].astype(int);alpha,beta,g=faces[:,3],faces[:,4],faces[:,5]
    normal_gradient=(g-alpha*u[k])/(beta+alpha*h/2)
    boundary_value=u[k]+h/2*normal_gradient
    boundary_residual=alpha*boundary_value+beta*normal_gradient-g
    row=dict(n=n,family=kind,mean=mean,l2=float(np.sqrt(np.mean((u.reshape(n,n)-ref)**2))),
        linf=float(np.max(abs(u.reshape(n,n)-ref))),residual=float(np.max(abs(A@u-b))),
        compatibility=abs(compat),mean_error=float(abs(np.mean(u)-mean)) if kind=='neumann' else 0.,
        nullspace_defect=float(np.max(abs(A@np.ones(n*n)))) if kind=='neumann' else 0.,
        solver_gap=solver_gap,lagrange_multiplier=lagrange,
        boundary_residual=float(np.max(abs(boundary_residual))),
        boundary_flux_error=float(np.max(abs(normal_gradient-faces[:,6]))),
        flux_balance=float(abs(h*np.sum(normal_gradient)+h*h*np.sum(f))),
        symmetry=float(abs(A-A.T).max()) if (A-A.T).nnz else 0.)
    return row,dict(x=(np.arange(n)+.5)/n,u=u.reshape(n,n),reference=ref,forcing=f,
                    face_records=faces,normal_gradient=normal_gradient,boundary_value=boundary_value,
                    boundary_residual=boundary_residual,volumes=np.full((n,n),h*h))
