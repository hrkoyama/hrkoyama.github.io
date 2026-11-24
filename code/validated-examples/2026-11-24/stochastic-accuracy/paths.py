"""Scalar EM/Milstein paths; pathwise coupling is distinct from weak error."""
import hashlib
import numpy as np


def digest(array):
    return hashlib.sha256(np.asarray(array,dtype='<f8',order='C').tobytes()).hexdigest()


def grouped_increments(fine, steps):
    if fine.ndim!=2 or steps<1 or fine.shape[1]%steps:
        raise ValueError('A two-dimensional exactly nested increment table is required')
    return fine.reshape(len(fine),steps,fine.shape[1]//steps).sum(axis=2)


def bridge_coefficients(kappa,h):
    c=-np.expm1(-kappa*h)/kappa
    variance=-np.expm1(-2*kappa*h)/(2*kappa)
    residual=variance-c*c/h
    if not (np.isfinite(residual) and residual>0):
        raise ArithmeticError('OU conditional variance is not strictly positive; no repair')
    return c/h,np.sqrt(residual)


def gbm_step(x,dw,h,mu,sigma,method):
    factor=1+mu*h+sigma*dw
    if method=='milstein':factor=factor+.5*sigma*sigma*(dw*dw-h)
    elif method!='em':raise ValueError('Unknown GBM method')
    return x*factor


def simulate_batch(cfg,seed,methods,partial):
    """Save the fine driver digest and reuse ONE exact endpoint at every level.

    Block sums define the chosen nesting. A subsequent sum of the coarse blocks
    may differ from the one stored fine sum by floating-point association.
    """
    rng=np.random.default_rng(seed);levels=cfg['steps'];nf=max(levels);m=cfg['paths_per_batch'];hf=cfg['T']/nf
    fine=rng.normal(size=(m,nf))*np.sqrt(hf)
    partial.update(seed=np.array(seed),fine_increments=fine,step=np.array(0))
    terminal_w=fine.sum(axis=1)
    exact_path=np.empty((nf+1,16));exact_path[0]=cfg['initial']
    if cfg['kind']=='gbm':
        exact=cfg['initial']*np.exp((cfg['mu']-.5*cfg['sigma']**2)*cfg['T']+cfg['sigma']*terminal_w)
        wpath=np.concatenate((np.zeros((16,1)),np.cumsum(fine[:16],axis=1)),axis=1)
        exact_path[:]=(cfg['initial']*np.exp((cfg['mu']-.5*cfg['sigma']**2)*np.arange(nf+1)[None,:]*hf+cfg['sigma']*wpath)).T
    elif cfg['kind']=='ou':
        alpha,beta=bridge_coefficients(cfg['kappa'],hf)
        bridge=rng.normal(size=(m,nf));kicks=alpha*fine+beta*bridge
        partial['bridge_normals']=bridge
        exact=np.full(m,cfg['initial']);decay=np.exp(-cfg['kappa']*hf)
        for j in range(nf):
            exact=cfg['theta']+decay*(exact-cfg['theta'])+cfg['sigma']*kicks[:,j]
            exact_path[j+1]=exact[:16]
    else:raise ValueError('Unknown scalar process')
    endpoints=np.empty((len(methods),len(levels),m));examples=np.empty((len(methods),nf+1,16));examples[:,0]=cfg['initial'];association=[]
    for k,n in enumerate(levels):
        dw=grouped_increments(fine,n);h=cfg['T']/n
        association.append(float(np.max(np.abs(dw.sum(axis=1)-terminal_w))))
        for method_id,method in enumerate(methods):
            x=np.full(m,cfg['initial']);partial.update(current=x,level=np.array(n),method=np.array(method_id))
            for j in range(n):
                partial.update(current=x,step=np.array(j))
                if cfg['kind']=='gbm':x=gbm_step(x,dw[:,j],h,cfg['mu'],cfg['sigma'],method)
                else:
                    if method!='em':raise ValueError('Only EM is used for OU')
                    x=x+cfg['kappa']*(cfg['theta']-x)*h+cfg['sigma']*dw[:,j]
                if n==nf:examples[method_id,j+1]=x[:16]
            endpoints[method_id,k]=x
    return dict(endpoints=endpoints,exact=exact,terminal_w=terminal_w,exact_examples=exact_path,
                numerical_examples=examples,association_error=np.array(association)),digest(fine)
