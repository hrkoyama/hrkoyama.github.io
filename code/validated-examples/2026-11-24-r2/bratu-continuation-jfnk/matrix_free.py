"""Callable-only right-preconditioned GMRES and inexact JFNK; no nonlinear Jacobian assembly."""
import math
import numpy as np
from dual import Dual
from problem import residual,analytic_jv,poisson_inverse,dot,norm,l2


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


class Evaluator:
    def __init__(self,lam,mode):
        if mode not in ['analytic','central-fd','forward-ad']:raise ValueError('Unknown Jv mode')
        self.lam=lam;self.mode=mode;self.counts=dict(primal_residual=0,jv=0,zero_jv=0,dual_residual=0,preconditioner=0,validation_analytic_jv=0)
    def function(self,u):
        self.counts['primal_residual']+=1;return residual(u,self.lam)
    def operator(self,u,v):
        self.counts['jv']+=1
        if norm(v)==0:
            self.counts['zero_jv']+=1;return np.zeros_like(v)
        if self.mode=='analytic':return analytic_jv(u,self.lam,v)
        if self.mode=='forward-ad':
            self.counts['dual_residual']+=1;return residual(Dual(u,v),self.lam).tangent
        step=np.finfo(float).eps**(1/3)*(1+norm(u))/norm(v)
        return (self.function(u+step*v)-self.function(u-step*v))/(2*step)
    def precondition(self,v):
        self.counts['preconditioner']+=1;return poisson_inverse(v)


def inexact_newton(n,lam,branch,mode,settings,checkpoint=None):
    x=np.arange(1,n+1)/(n+1);u=np.zeros(n) if branch=='lower' else 4*np.sin(np.pi*x)
    ev=Evaluator(lam,mode);states=[u.copy()];rows=[];linear_histories=[];previous=None;all_trials=[]
    if checkpoint is not None:checkpoint(states,rows,ev.counts)
    for iteration in range(settings['max_newton']+1):
        f=ev.function(u);current=l2(f)
        if current<=settings['nonlinear_tolerance']:
            return dict(passed=True,u=u,states=np.array(states),rows=rows,linear_histories=linear_histories,
                        counts=ev.counts,final_residual=current,reason='nonlinear residual',line_trials=all_trials)
        if iteration==settings['max_newton']:break
        eta=settings.get('constant_eta')
        if eta is None:eta=settings['eta_initial'] if previous is None else min(settings['eta_max'],max(settings['eta_min'],settings['eta_gamma']*(current/previous)**settings['eta_power']))
        inner=gmres(lambda v:ev.operator(u,v),-f,ev.precondition,settings['restart'],settings['max_linear'],eta)
        linear_histories.append(inner['residuals'])
        ev.counts['validation_analytic_jv']+=1;exact_ratio=norm(analytic_jv(u,lam,inner['x'])+f)/norm(f)
        row=dict(iteration=iteration,residual=current,eta=eta,linear_iterations=inner['iterations'],linear_ratio=inner['residuals'][-1]/norm(f),analytic_linear_ratio=exact_ratio,basis_columns=inner['basis_columns'],alpha=0.,accepted_residual=current)
        if not inner['passed']:return dict(passed=False,u=u,states=np.array(states),rows=rows+[row],linear_histories=linear_histories,counts=ev.counts,final_residual=current,reason='inner iteration failed',line_trials=all_trials)
        accepted=False
        for k in range(settings['max_backtracks']):
            alpha=2.**(-k);trial=u+alpha*inner['x']
            try:trialnorm=l2(ev.function(trial))
            except FloatingPointError:
                all_trials.append(dict(iteration=iteration,backtrack=k,accepted=False,representable=False,state=trial.copy()));continue
            accept=trialnorm<=(1-settings['armijo']*alpha)*current
            all_trials.append(dict(iteration=iteration,backtrack=k,accepted=bool(accept),representable=True,residual=trialnorm,state=trial.copy()))
            if accept:previous=current;u=trial;states.append(u.copy());row['alpha']=alpha;row['accepted_residual']=trialnorm;accepted=True;break
        rows.append(row)
        if checkpoint is not None:checkpoint(states,rows,ev.counts)
        if not accepted:break
    return dict(passed=False,u=u,states=np.array(states),rows=rows,linear_histories=linear_histories,counts=ev.counts,
                final_residual=l2(ev.function(u)),reason='outer iteration or line search limit',line_trials=all_trials)
