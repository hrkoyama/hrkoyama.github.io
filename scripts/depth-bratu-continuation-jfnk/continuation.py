"""Weighted hyperplane pseudo-arclength, assembled bordered Newton, and fold solve."""
import numpy as np
from scipy.sparse import bmat,csc_matrix,diags
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigh_tridiagonal
from problem import residual,analytic_jv,sparse_jacobian,jacobian_diagonals,l2,norm,dot,arc_norm,weighted_arc_dot


class NonlinearFailure(ArithmeticError):
    def __init__(self,message,**arrays):
        super().__init__(message);self.arrays={k:np.asarray(v) for k,v in arrays.items()}


def bordered(u,lam,tangent):
    n=len(u)
    return bmat([[sparse_jacobian(u,lam),csc_matrix(-np.exp(u)[:,None])],
                 [csc_matrix(tangent[None,:-1]/(n+1)),csc_matrix([[tangent[-1]]])]],format='csc')


def tangent_at(z,previous=None):
    n=len(z)-1
    if previous is None:
        state=spsolve(sparse_jacobian(z[:-1],z[-1]),np.exp(z[:-1]));t=np.r_[state,1.]
    else:t=spsolve(bordered(z[:-1],z[-1],previous),np.r_[np.zeros(n),1.])
    if not np.all(np.isfinite(t)) or arc_norm(t)==0:raise NonlinearFailure('Invalid arc tangent',z=z,t=t)
    t/=arc_norm(t)
    if previous is not None and weighted_arc_dot(t,previous)<0:t=-t
    return t


def arc_correct(predict,tangent,tolerance,maxiter,progress=None):
    z=predict.copy();history=[];states=[z.copy()]
    def equation(w):return np.r_[residual(w[:-1],w[-1]),weighted_arc_dot(w-predict,tangent)]
    def magnitude(g):return float(np.sqrt(dot(g[:-1],g[:-1])/len(g)+g[-1]**2))
    for iteration in range(maxiter+1):
        if progress is not None:progress(candidate=z,predictor=predict,tangent=tangent,iterate_states=states,residual_history=history,stage=np.array('before-corrector-equation'))
        g=equation(z);size=magnitude(g);history.append(size)
        if size<=tolerance:return z,np.array(history),np.array(states)
        if iteration==maxiter:break
        correction=spsolve(bordered(z[:-1],z[-1],tangent),-g)
        if not np.all(np.isfinite(correction)):break
        accepted=False
        for backtrack in range(14):
            alpha=2.**(-backtrack);trial=z+alpha*correction
            if progress is not None:progress(candidate=trial,predictor=predict,tangent=tangent,iterate_states=states,residual_history=history,stage=np.array('before-corrector-trial'))
            try:trialnorm=magnitude(equation(trial))
            except FloatingPointError:continue
            if trialnorm<=(1-1e-4*alpha)*size:
                z=trial;states.append(z.copy());accepted=True;break
        if not accepted:break
    raise NonlinearFailure('Pseudo-arclength corrector failed',candidate=z,predictor=predict,
                           tangent=tangent,residual_history=history,iterate_states=states)


def follow(n,ds,steps,tolerance=1e-10,maxiter=12,checkpoint=None,corrector_progress=None):
    z=np.zeros(n+1);t=tangent_at(z);states=[];tangents=[];rows=[];iterations=[]
    for step in range(steps+1):
        if corrector_progress is not None:
            arrays=dict(candidate=z,tangent=t,path_states=np.array(states+[z.copy()]),path_tangents=np.array(tangents+[t.copy()]),stage=np.array('before-path-diagnostics'))
            for k,item in enumerate(iterations):arrays['completed_corrector_states_'+str(k)]=item['states'];arrays['completed_corrector_residuals_'+str(k)]=item['residuals']
            corrector_progress(**arrays)
        lo,di,up=jacobian_diagonals(z[:-1],z[-1]);eigen=eigh_tridiagonal(di,lo,eigvals_only=True)
        fnorm=l2(residual(z[:-1],z[-1]));tr=analytic_jv(z[:-1],z[-1],t[:-1])-np.exp(z[:-1])*t[-1]
        row=dict(step=step,s=step*ds,lam=float(z[-1]),u_mid=float(z[n//2]),residual=fnorm,
                 tangent_lambda=float(t[-1]),tangent_equation=l2(tr),tangent_norm=arc_norm(t),
                 sigma_min=float(np.min(abs(eigen))),smallest_eigenvalue=float(eigen[0]))
        states.append(z.copy());tangents.append(t.copy());rows.append(row)
        if checkpoint is not None:checkpoint(np.array(states),np.array(tangents),rows,iterations)
        if step==steps:break
        new,history,corrector_states=arc_correct(z+ds*t,t,tolerance,maxiter,corrector_progress)
        iterations.append(dict(step=step+1,residuals=history,states=corrector_states))
        if corrector_progress is not None:
            arrays=dict(candidate=new,stage=np.array('completed-corrector-before-tangent'))
            for k,item in enumerate(iterations):arrays['completed_corrector_states_'+str(k)]=item['states'];arrays['completed_corrector_residuals_'+str(k)]=item['residuals']
            corrector_progress(**arrays)
        z=new;t=tangent_at(z,t)
    return dict(states=np.array(states),tangents=np.array(tangents),rows=rows,correctors=iterations)


def fixed_lambda(u,lam,tolerance=1e-10,maxiter=30,progress=None):
    u=np.array(u,dtype=float);states=[u.copy()];history=[]
    for iteration in range(maxiter+1):
        if progress is not None:progress(candidate=u,lam=np.array(lam),iterate_states=states,residual_history=history,stage=np.array('before-fixed-lambda-equation'))
        f=residual(u,lam);size=l2(f);history.append(size)
        if size<=tolerance:return dict(passed=True,u=u,states=np.array(states),residuals=np.array(history),reason='nonlinear residual')
        if iteration==maxiter:break
        correction=spsolve(sparse_jacobian(u,lam),-f);accepted=False
        if not np.all(np.isfinite(correction)):break
        for k in range(14):
            alpha=2.**(-k);trial=u+alpha*correction
            if progress is not None:progress(candidate=trial,lam=np.array(lam),iterate_states=states,residual_history=history,stage=np.array('before-fixed-lambda-trial'))
            try:trialnorm=l2(residual(trial,lam))
            except FloatingPointError:continue
            if trialnorm<=(1-1e-4*alpha)*size:
                u=trial;states.append(u.copy());accepted=True;break
        if not accepted:return dict(passed=False,u=u,states=np.array(states),residuals=np.array(history),reason='line search exhausted')
    return dict(passed=False,u=u,states=np.array(states),residuals=np.array(history),reason='iteration limit or nonfinite correction')


def fold_equations(w):
    n=(len(w)-1)//2;u,lam,v=w[:n],w[n],w[n+1:]
    return np.r_[residual(u,lam),analytic_jv(u,lam,v),dot(v,v)/(n+1)-1]


def fold_jacobian(w):
    n=(len(w)-1)//2;u,lam,v=w[:n],w[n],w[n+1:];exp=np.exp(u);J=sparse_jacobian(u,lam)
    return bmat([[J,csc_matrix(-exp[:,None]),None],
                 [diags(-lam*exp*v,format='csc'),csc_matrix((-exp*v)[:,None]),J],
                 [csc_matrix((1,n)),csc_matrix((1,1)),csc_matrix((2*v/(n+1))[None,:])]],format='csc')


def solve_fold(arc,tolerance=1e-10,maxiter=16,progress=None):
    z=arc['states'][int(np.argmax(arc['states'][:,-1]))];n=len(z)-1
    lo,di,up=jacobian_diagonals(z[:-1],z[-1]);ev,vec=eigh_tridiagonal(di,lo)
    v=vec[:,int(np.argmin(abs(ev)))];v/=np.sqrt(dot(v,v)/(n+1))
    if np.sum(v)<0:v=-v
    w=np.r_[z[:-1],z[-1],v];history=[];states=[w.copy()]
    def size(f):return float(np.sqrt(dot(f[:-1],f[:-1])/(n+1)+f[-1]**2))
    for iteration in range(maxiter+1):
        if progress is not None:progress(candidate=w,iterate_states=states,residual_history=history,stage=np.array('before-fold-equation'))
        f=fold_equations(w);current=size(f);history.append(current)
        if current<=tolerance:return dict(w=w,states=np.array(states),residuals=np.array(history))
        if iteration==maxiter:break
        delta=spsolve(fold_jacobian(w),-f);accepted=False
        for k in range(14):
            alpha=2.**(-k);trial=w+alpha*delta
            if progress is not None:progress(candidate=trial,iterate_states=states,residual_history=history,stage=np.array('before-fold-trial'))
            try:trialnorm=size(fold_equations(trial))
            except FloatingPointError:continue
            if trialnorm<=(1-1e-4*alpha)*current:w=trial;states.append(w.copy());accepted=True;break
        if not accepted:break
    raise NonlinearFailure('Augmented fold solve failed',candidate=w,iterate_states=states,residual_history=history)
