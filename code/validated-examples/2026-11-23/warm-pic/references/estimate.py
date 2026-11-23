"""Fixed-window estimators shared deliberately by linear reference and PIC data."""
import numpy as np
from scipy.optimize import least_squares


def selected(t,y,window):
    mask=(t>=window[0]-1e-12)&(t<=window[1]+1e-12)
    if np.count_nonzero(mask)<20 or not np.isfinite(y).all():raise ValueError('Insufficient finite fixed-window samples')
    return t[mask],y[mask]


def damped(t,y,window,initial):
    t,y=selected(t,y,window);center=.5*(window[0]+window[1]);s=t-center;scale=float(np.sqrt(np.mean(y*y)))
    if scale<=0:raise ValueError('Unresolved zero signed field signal')
    def model(parameters):
        gamma,omega=parameters;e=np.exp(gamma*s);a=e*np.cos(omega*s);b=e*np.sin(omega*s)
        aa=np.sum(a*a);bb=np.sum(b*b);ab=np.sum(a*b);ay=np.sum(a*y);by=np.sum(b*y);det=aa*bb-ab*ab
        if det<=0:raise ValueError('Singular phase fit')
        ca=(ay*bb-by*ab)/det;cb=(by*aa-ay*ab)/det
        return ca*a+cb*b,float(np.hypot(ca,cb))
    fit=least_squares(lambda p:(model(p)[0]-y)/scale,initial,bounds=([-.5,.5],[.1,2.5]),ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=200)
    if not fit.success:raise ValueError('Damped sinusoid fit failed')
    predicted,amplitude=model(fit.x);g,w=map(float,fit.x)
    return dict(gamma=g,omega=w,relative_fit_residual=float(np.sqrt(np.mean((predicted-y)**2))/scale),minimum_envelope=amplitude*float(np.exp(min(g*(window[0]-center),g*(window[1]-center)))),samples=len(t))


def growing(t,y,window):
    t,y=selected(t,y,window)
    if np.any(y==0) or not (np.all(y>0) or np.all(y<0)):raise ValueError('Growing fixed window crosses zero; no sample exclusions allowed')
    z=np.log(abs(y));s=t-t.mean();gamma=float(np.sum(s*(z-z.mean()))/np.sum(s*s));intercept=float(z.mean());pred=np.sign(y[0])*np.exp(intercept+gamma*s)
    return dict(gamma=gamma,omega=0.,relative_fit_residual=float(np.sqrt(np.mean((pred-y)**2)/np.mean(y*y))),minimum_envelope=float(np.min(abs(pred))),samples=len(t))


def fit(case,t,y,window,root):
    return damped(t,y,window,[root.imag,root.real]) if case=='thermal-landau-damping' else growing(t,y,window)
