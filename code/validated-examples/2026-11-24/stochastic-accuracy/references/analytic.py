"""Authored finite-moment identities, evaluated with Decimal; no path solver."""
from decimal import Decimal as D, localcontext


def gbm(cfg,n,precision=80):
    with localcontext() as ctx:
        ctx.prec=precision;mu=D(str(cfg['mu']));s=D(str(cfg['sigma']));T=D(str(cfg['T']));x=D(str(cfg['initial']));h=T/n;a=1+mu*h
        truth=[x*(mu*T).exp(),x*x*((2*mu+s*s)*T).exp()]
        discrete=[x*a**n,x*x*(a*a+s*s*h)**n]
        fourth=x**4*(a**4+6*a*a*s*s*h+3*s**4*h*h)**n
        exact_fourth=x**4*((4*mu+6*s*s)*T).exp()
        mixed1=x*x*((mu*h).exp()*(a+s*s*h))**n
        mixed2=x**4*(((2*mu+s*s)*h).exp()*((a+2*s*s*h)**2+s*s*h))**n
        variance=[discrete[1]+truth[1]-2*mixed1-(discrete[0]-truth[0])**2,
                  fourth+exact_fourth-2*mixed2-(discrete[1]-truth[1])**2]
        return {'continuous':truth,'discrete':discrete,'bias':[a-b for a,b in zip(discrete,truth)],'paired_variance':variance,'raw_variance':[discrete[1]-discrete[0]**2,fourth-discrete[1]**2]}


def ou(cfg,n,precision=80):
    with localcontext() as ctx:
        ctx.prec=precision;k=D(str(cfg['kappa']));s=D(str(cfg['sigma']));T=D(str(cfg['T']));x=D(str(cfg['initial']));theta=D(str(cfg['theta']));h=T/n;a=1-k*h;b=(-k*h).exp()
        mt=theta+(x-theta)*(-k*T).exp();me=theta+(x-theta)*a**n
        vt=s*s*(1-(-2*k*T).exp())/(2*k);ve=s*s*h*(1-a**(2*n))/(1-a*a)
        cov=s*s*(1-b)/k*(1-(a*b)**n)/(1-a*b)
        truth=[mt,mt*mt+vt];discrete=[me,me*me+ve]
        variance=[ve+vt-2*cov,2*(ve*ve+vt*vt-2*cov*cov)+4*(me*me*ve+mt*mt*vt-2*me*mt*cov)]
        return {'continuous':truth,'discrete':discrete,'bias':[a-b for a,b in zip(discrete,truth)],'paired_variance':variance,'raw_variance':[ve,2*ve*ve+4*me*me*ve],'joint_covariance':cov}


def strong(cfg,n,method,precision=80):
    with localcontext() as ctx:
        ctx.prec=precision;mu=D(str(cfg['mu']));s=D(str(cfg['sigma']));T=D(str(cfg['T']));x=D(str(cfg['initial']));h=T/n;a=1+mu*h
        A=a*a+s*s*h;K=(mu*h).exp()*(a+s*s*h)
        if method=='milstein':A+=s**4*h*h/2;K+=(mu*h).exp()*s**4*h*h/2
        elif method!='em':raise ValueError('Unknown strong method')
        B=((2*mu+s*s)*T).exp();mse=x*x*(A**n+B-2*K**n)
        if mse<=0:raise ArithmeticError('Nonpositive analytic MSE; no floor')
        return {'A':A,'K':K,'mse':mse,'rms':mse.sqrt()}


def encode(value):
    if isinstance(value,D):return float(value)
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,list):return [encode(v) for v in value]
    return value
