"""Independent tensor-form exact references for restricted SRHD and full RMHD."""
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss


def tensor_state(w, bx, gamma):
    rho=w[...,0];v=w[...,1:4];p=w[...,4]
    B=np.concatenate([np.full(rho.shape+(1,),bx),w[...,5:]],axis=-1)
    W=1/np.sqrt(1-np.sum(v*v,axis=-1));h=1+gamma/(gamma-1)*p/rho
    u=np.concatenate([W[...,None],W[...,None]*v],axis=-1)
    b0=W*np.sum(v*B,axis=-1)
    b=np.concatenate([b0[...,None],B/W[...,None]+b0[...,None]*v],axis=-1)
    metric=np.diag([-1.,1.,1.,1.]);bsq=np.sum(b[...,1:]**2,axis=-1)-b0*b0
    T=(rho*h+bsq)[...,None,None]*u[..., :,None]*u[...,None,:]+(p+.5*bsq)[...,None,None]*metric-b[..., :,None]*b[...,None,:]
    U=np.concatenate([(rho*W)[...,None],T[...,0,1:4],T[...,0,0,None],B[...,1:]],axis=-1)
    F=np.concatenate([(rho*W*v[...,0])[...,None],T[...,1,1:4],T[...,1,0,None],v[...,0,None]*B[...,1:]-bx*v[...,1:]],axis=-1)
    return U,F


def collision_star(rho=1.,p=.1,v=.3,gamma=5/3):
    """Taub enthalpy quadratic + invariant shock relative velocity (RZ2001)."""
    ha=1+gamma/(gamma-1)*p/rho;ea=rho+p/(gamma-1)
    def downstream(pb):
        # Independent h-form Taub quadratic, not the production recovery equation.
        d=pb-p;k=(gamma-1)/gamma
        A=1-k*d/pb;B=k*d/pb;C=-ha*ha-ha*d/rho
        hb=(-B+np.sqrt(B*B-4*A*C))/(2*A)
        rb=gamma*pb/((gamma-1)*(hb-1));eb=rb+pb/(gamma-1)
        rel=np.sqrt((pb-p)*(eb-ea)/((ea+pb)*(eb+p)))
        return rb,hb,rel
    pb=brentq(lambda b:downstream(b)[2]-v,p*(1+1e-10),10.,xtol=1e-14)
    rb,hb,rel=downstream(pb);j2=-(pb-p)/(hb/rb-ha/rho)
    speed=np.sqrt(j2/(rb*rb+j2))
    return dict(pressure=pb,density=rb,enthalpy=hb,speed=speed,relative_velocity=rel,
                taub_residual=hb*hb-ha*ha-(pb-p)*(hb/rb+ha/rho))


def collision_means(edges,t,rho=1.,p=.1,v=.3,gamma=5/3):
    star=collision_star(rho,p,v,gamma)
    states=np.zeros((3,7));states[:,0]=[rho,star['density'],rho];states[:,4]=[p,star['pressure'],p];states[:,1]=[v,0,-v]
    cons,_=tensor_state(states,0.,gamma);a=.5-star['speed']*t;b=.5+star['speed']*t
    low=edges[:-1];high=edges[1:];width=high-low
    left=np.maximum(0,np.minimum(high,a)-low)/width
    right=np.maximum(0,high-np.maximum(low,b))/width
    middle=1-left-right
    return left[:,None]*cons[0]+middle[:,None]*cons[1]+right[:,None]*cons[2]


def alfven_speed(rho=1.,p=1.,bx=1.,eta=1.,gamma=4/3):
    K=rho+gamma*p/(gamma-1)+bx*bx*(1+eta*eta)
    return np.sqrt(2*bx*bx/(K+np.sqrt(K*K-4*eta*eta*bx**4)))


def alfven_primitive(x,t,rho=1.,p=1.,bx=1.,eta=1.,gamma=4/3):
    va=alfven_speed(rho,p,bx,eta,gamma);phase=2*np.pi*(np.asarray(x)-va*t)
    w=np.zeros(phase.shape+(7,),dtype=np.result_type(phase));w[...,0]=rho;w[...,4]=p
    w[...,5]=eta*bx*np.cos(phase);w[...,6]=eta*bx*np.sin(phase)
    w[...,2:4]=-va/bx*w[...,5:7]
    return w


def alfven_means(edges,t,rho=1.,p=1.,bx=1.,eta=1.,gamma=4/3):
    """Analytic conserved cell means: constant D,Sx,E; transverse harmonics."""
    va=alfven_speed(rho,p,bx,eta,gamma);W=1/np.sqrt(1-eta*eta*va*va)
    Z=(rho+gamma*p/(gamma-1))*W*W
    center=.5*(edges[:-1]+edges[1:]);sinc=np.sinc(np.diff(edges))
    phase=2*np.pi*(center-va*t);by=eta*bx*sinc*np.cos(phase);bz=eta*bx*sinc*np.sin(phase)
    q=np.zeros((len(center),7));q[:,0]=rho*W;q[:,1]=va*eta*eta*bx*bx
    q[:,2]=-va*(Z+bx*bx)*by/bx;q[:,3]=-va*(Z+bx*bx)*bz/bx
    q[:,4]=Z-p+.5*bx*bx*(1+eta*eta+eta*eta*va*va);q[:,5]=by;q[:,6]=bz
    return q


def independent_srhd(U,gamma):
    """B=0 scalar pressure recovery, independent of production Z root."""
    D=U[0];S=U[1:4];E=U[4];a=(gamma-1)/gamma
    def equation(p):
        v=S/(E+p);g=1-v@v
        if g<=0:return -1.
        return p-a*((E+p)*g-D*np.sqrt(g))
    p=brentq(equation,0.,(gamma-1)*E,xtol=1e-14)
    v=S/(E+p);rho=D*np.sqrt(1-v@v)
    w=np.array([rho,*v,p,0.,0.]);flux=np.array([D*v[0],S[0]*v[0]+p,S[1]*v[0],S[2]*v[0],S[0],0.,0.])
    return w,flux


def qualify():
    star=collision_star();rho=1.;p=.1;v=.3;g=5/3
    ws=np.array([[rho,v,0,0,p,0,0],[star['density'],0,0,0,star['pressure'],0,0]])
    U,F=tensor_state(ws,0.,g)
    # Left shock speed is negative; left state flows right into resting star.
    rh=F[1]-F[0]+star['speed']*(U[1]-U[0])
    va=alfven_speed();h=5.;disp=abs((h+2-va*va)*va*va-1)
    edges=np.linspace(0,1,18);nodes,weights=leggauss(12);x=.5*(edges[:-1,None]+edges[1:,None])+.5*np.diff(edges)[:,None]*nodes
    pointU,pointF=tensor_state(alfven_primitive(x,.173),1.,4/3)
    integrated=np.einsum('ijk,j->ik',pointU,weights)/2
    means=alfven_means(edges,.173);quadrature=float(np.max(abs(integrated-means)))
    # Tensor flux differentiated via complex step at independent non-grid coordinates.
    xp=np.array([.037,.219,.441,.783]);eps=1e-25
    u,f=tensor_state(alfven_primitive(xp.astype(complex)+1j*eps,.173),1.,4/3)
    du,df=u.imag/eps,f.imag/eps
    pde=float(np.max(abs(df-va*du)))
    checks={'Taub adiabat':abs(star['taub_residual'])<2e-12,
            'invariant relative velocity':abs(star['relative_velocity']-.3)<2e-13,
            'tensor Rankine Hugoniot':bool(np.max(abs(rh))<2e-12),
            'nonlinear Alfven dispersion':disp<2e-13,
            'independent tensor Gauss means':quadrature<3e-12,
            'tensor complex step PDE residual':pde<3e-11}
    checks={k:bool(v) for k,v in checks.items()}
    star={k:float(v) for k,v in star.items()}
    return dict(passed=all(checks.values()),checks=checks,collision_star=star,alfven_speed=float(va),
                rh_maximum=float(np.max(abs(rh))),quadrature_maximum=quadrature,pde_maximum=pde)
