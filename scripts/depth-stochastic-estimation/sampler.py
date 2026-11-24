"""Fixed two-dimensional correlated-Gaussian random-walk MH, no adaptation."""
import numpy as np

OBSERVABLES=['y1','y2','y1_squared','y2_squared','product','Q','sum_direction','difference_direction']


def target_logpdf(x,mean,rho):
    y=np.asarray(x)-np.asarray(mean)
    return -.5*(y[...,0]**2-2*rho*y[...,0]*y[...,1]+y[...,1]**2)/(1-rho*rho)-np.log(2*np.pi)-.5*np.log1p(-rho*rho)


def observable_arrays(chains,mean,rho):
    y=chains-np.asarray(mean);a,b=y[...,0],y[...,1]
    return np.stack((a,b,a*a,b*b,a*b,(a*a-2*rho*a*b+b*b)/(1-rho*rho),
                     (a+b)/np.sqrt(2*(1+rho)),(a-b)/np.sqrt(2*(1-rho))),axis=-1)


def truth_and_scales(rho):
    return np.array([0.,0.,1.,1.,rho,2.,0.,0.]),np.array([1.,1.,np.sqrt(2),np.sqrt(2),np.sqrt(1+rho*rho),2.,1.,1.])


def sample(cfg,seed,proposal,partial):
    if proposal not in cfg['proposals'] or not (-1<cfg['rho']<1):raise ValueError('Unsupported fixed Gaussian proposal/target')
    n=cfg['draws']+cfg['burn'];rho=cfg['rho'];L=np.array([[1.,0.],[rho,np.sqrt(1-rho*rho)]]);pid=list(cfg['proposals']).index(proposal)
    generators=[np.random.default_rng(np.random.SeedSequence([seed,pid,chain])) for chain in range(cfg['chains'])]
    normals=np.stack([g.normal(size=(n,2)) for g in generators],axis=1)
    log_uniform=np.stack([np.log1p(-g.random(n)) for g in generators],axis=1)
    increments=cfg['proposals'][proposal]*(normals@L.T if proposal=='preconditioned' else normals)
    x=np.asarray(cfg['initial_whitened'])@L.T+np.asarray(cfg['mean']);logp=target_logpdf(x,cfg['mean'],rho)
    chains=np.empty((cfg['chains'],cfg['draws'],2));accept=np.empty((cfg['chains'],n),bool)
    for j in range(n):
        partial.update(current=x.copy(),step=np.array(j),seed=np.array(seed),proposal=np.array(pid))
        trial=x+increments[j];next_logp=target_logpdf(trial,cfg['mean'],rho)
        yes=log_uniform[j]<next_logp-logp
        x=np.where(yes[:,None],trial,x);logp=np.where(yes,next_logp,logp);accept[:,j]=yes
        if j>=cfg['burn']:chains[:,j-cfg['burn']]=x
    return {'chains':chains,'accepted':accept,'initial':np.asarray(cfg['initial_whitened'])@L.T+np.asarray(cfg['mean'])}
