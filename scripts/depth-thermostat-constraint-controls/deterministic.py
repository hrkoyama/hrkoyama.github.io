"""Authored symmetric NH/NHC subflows and deterministic-temperature contrasts."""
from __future__ import annotations
from common import matmul,dot,array_norm
from decimal import Decimal,localcontext
import math
import numpy as np
from common import adaptive,corr,maxerr,order
OMEGA=np.array([1.,1.7])


def phi1(z):
    z=np.asarray(z,dtype=float);out=np.empty_like(z);small=np.abs(z)<1e-5
    zs=z[small];v=np.ones_like(zs)/math.factorial(7)
    for k in range(5,-1,-1):v=v*zs+1/math.factorial(k+1)
    out[small]=v;out[~small]=np.expm1(z[~small])/z[~small]
    return out


def force(q,kappa):return -OMEGA**2*q-kappa*q*q*q

def physical_energy(q,p,kappa):return .5*np.sum(p*p+OMEGA**2*q*q,axis=-1)+kappa/4*np.sum(q**4,axis=-1)

def masses(M,tau):return np.array([2*tau*tau]+[tau*tau]*(M-1))

def extended(q,p,xi,eta,kappa,tau):
    return physical_energy(q,p,kappa)+.5*np.sum(masses(xi.shape[-1],tau)*xi*xi,axis=-1)+2*eta[...,0]+np.sum(eta[...,1:],axis=-1)


def bath(p,xi,eta,duration,tau,budget):
    incoming_p=p;incoming_xi=xi;incoming_eta=eta
    p=p.copy();xi=xi.copy();eta=eta.copy();M=xi.shape[-1];Q=masses(M,tau)
    budget.augment(stage='NH-bath',bath_input_p=incoming_p,bath_input_xi=incoming_xi,bath_input_eta=incoming_eta,
                   bath_candidate_p=p,bath_candidate_xi=xi,bath_candidate_eta=eta)
    d=duration/2  # exactly2subcycles per O, hence d=h/4 per outer halfbath
    def B(j,delta):
        f=(np.sum(p*p,axis=-1)-2)/Q[0] if j==0 else (Q[j-1]*xi[...,j-1]**2-1)/Q[j]
        if j+1<M:
            zz=-xi[...,j+1]*delta
            budget.augment(bath_subflow='B'+str(j+1),subflow_duration=delta,subflow_driving=f,subflow_exponent=zz)
            xi[...,j]=np.exp(zz)*xi[...,j]+delta*f*phi1(zz)
        else:
            budget.augment(bath_subflow='B'+str(j+1),subflow_duration=delta,subflow_driving=f)
            xi[...,j]+=delta*f
        budget.tick('NH_B_subflow')
    for _ in range(2):
        eta+=d/2*xi;budget.tick('NH_E_subflow')
        for j in range(M-1,-1,-1):B(j,d/2)
        p*=np.exp(-xi[...,:1]*d);budget.tick('NH_A_subflow')
        for j in range(M):B(j,d/2)
        eta+=d/2*xi;budget.tick('NH_E_subflow')
        budget.tick('NH_subcycle')
        if not all(np.all(np.isfinite(a)) for a in [p,xi,eta]):raise FloatingPointError('Nonfinite bath subflow')
    return p,xi,eta


def radial(p,duration,tau,kind):
    p=np.asarray(p);K=.5*np.sum(p*p,axis=-1)
    if np.any(K<=0):raise ValueError('Positive kinetic energy required for radial direction')
    target=1+(K-1)*math.exp(-duration/tau) if kind=='Berendsen' else np.ones_like(K)
    if np.any(target<=0):raise ValueError('Radial inverse leaves positive-energy domain')
    return p*np.sqrt(target/K)[...,None]


def step(q,p,xi,eta,h,tau,kappa,kind,budget):
    if kind in ['NH','NHC3']:p,xi,eta=bath(p,xi,eta,h/2,tau,budget)
    else:p=radial(p,h/2,tau,kind);budget.tick('deterministic_radial_bath')
    budget.augment(stage='VV-firstforce',VV_input_q=q,VV_input_p=p)
    p=p+h/2*force(q,kappa);budget.augment(stage='VV-drift',VV_halfkick_p=p)
    q=q+h*p;budget.augment(stage='VV-secondforce',VV_candidate_q=q,VV_candidate_p=p)
    p=p+h/2*force(q,kappa);budget.augment(stage='VV-complete-beforesecondbath',VV_candidate_q=q,VV_candidate_p=p)
    budget.tick('deterministic_force',2)
    # eta is NOT advanced by velocityVerlet.
    if kind in ['NH','NHC3']:p,xi,eta=bath(p,xi,eta,h/2,tau,budget)
    else:p=radial(p,h/2,tau,kind);budget.tick('deterministic_radial_bath')
    return q,p,xi,eta


def direct_rhs(t,z,M,kappa,tau):
    # Independent fullODE; does not import/compose the splitting subflows.
    q=z[:2];p=z[2:4];x=z[4:4+M];Q=[2*tau*tau]+[tau*tau]*(M-1)
    dq=p.copy();dp=np.array([-q[0]-kappa*q[0]**3,-1.7**2*q[1]-kappa*q[1]**3])-x[0]*p
    dx=np.empty(M);dx[0]=(dot(p,p)-2)/Q[0]
    for j in range(1,M):dx[j]=(Q[j-1]*x[j-1]**2-1)/Q[j]
    for j in range(M-1):dx[j]-=x[j+1]*x[j]
    return np.r_[dq,dp,dx,x]


def canonical_initial(kappa,seed,budget):
    g=np.random.Generator(np.random.PCG64(seed));q=g.normal(size=(384,2))/OMEGA
    normals=768;uniforms=0;candidates=768
    # Declared initialuniforms are drawn even for kappa0; no hidden stream changes.
    u=g.random((384,2));uniforms+=768
    accepted=np.ones((384,2),dtype=bool) if kappa==0 else u<np.exp(-kappa*q**4/4)
    while not np.all(accepted):
        ids=np.where(~accepted);count=len(ids[0]);candidates+=count
        if candidates>100000:raise RuntimeError('Fixed canonical rejection cap')
        proposal=g.normal(size=count)/OMEGA[ids[1]];u=g.random(count)
        normals+=count;uniforms+=count;q[ids]=proposal;accepted[ids]=u<np.exp(-kappa*proposal**4/4)
        budget.tick('canonical_rejection_round')
    p=g.normal(size=(384,2));bathnormal=g.normal(size=(384,3));normals+=768+1152
    p[256:]*=1.4
    return q,p,bathnormal,{'seed':seed,'normal_draws':normals,'uniform_draws':uniforms,'coordinate_candidates':candidates,
                         'generator_final':g.bit_generator.state,'order':'rejectionbyincreasing(replica,coordinate),thenp,thenbathnormal'}


def static_reference(kappa,Q):
    z,w=np.polynomial.legendre.leggauss(Q);points=np.array([-2.,-1.,0.,1.,2.]);energies=np.array([.5,1.,2.,4.,6.])
    norms=[];qvar=[];umean=[];uvar=[];cdfs=[]
    def integral(fn,lo,hi):
        x=(z+1)*(hi-lo)/2+lo;return np.sum(w*fn(x))*(hi-lo)/2
    for omega in [1.,1.7]:
        lim=10/omega
        def U(x):return .5*omega*omega*x*x+kappa*x**4/4
        norm=integral(lambda x:np.exp(-U(x)),-lim,lim);norms.append(norm)
        um=integral(lambda x:U(x)*np.exp(-U(x)),-lim,lim)/norm;umean.append(um)
        uvar.append(integral(lambda x:U(x)**2*np.exp(-U(x)),-lim,lim)/norm-um*um)
        qvar.append(integral(lambda x:x*x*np.exp(-U(x)),-lim,lim)/norm)
        cdfs.append([integral(lambda x:np.exp(-U(x)),-lim,a)/norm for a in points])
    def turn(E,omega):
        if kappa==0:return math.sqrt(2*E)/omega
        aa=omega*omega/2
        return math.sqrt(2*E/(aa+math.sqrt(aa*aa+kappa*E)))
    hc=[]
    theta=(z+1)*math.pi/4;weights=w*math.pi/4  # positivequadrant, with x=Xsin(theta)
    for E in energies:
        X=turn(E,1.);x=X*np.sin(theta);ux=.5*x*x+kappa*x**4/4;remaining=E-ux
        if np.any(remaining<=0):raise FloatingPointError('Quadrature turningpoint ownership')
        Y=np.array([turn(e,1.7) for e in remaining]);y=Y[:,None]*np.sin(theta)[None,:]
        u=ux[:,None]+.5*1.7**2*y*y+kappa*y**4/4
        if np.any(E-u<0):raise FloatingPointError('Quadrature crossed fixed energy shell')
        jac=X*np.cos(theta)[:,None]*Y[:,None]*np.cos(theta)[None,:]
        hc.append(float(4*np.sum(weights[:,None]*weights[None,:]*jac*np.exp(-u)*(-np.expm1(-(E-u))))/(norms[0]*norms[1])))
    return {'normalizers':norms,'q_variance':qvar,'u_mean':float(sum(umean)),'u_variance':float(sum(uvar)),
            'h_mean':1+float(sum(umean)),'h_variance':1+float(sum(uvar)),'position_cdf':cdfs,'energy_cdf':hc,
            'Gaussian_unnormalized_omitted_tail_bounds':[2*math.exp(-50)/(10*o) for o in [1.,1.7]],'Q':Q}


def components(budget):
    checks={};phierrors=[]
    for v in [0.,-1e-12,1e-12,-1e-6,1e-6,-.1,.1]:
        with localcontext() as c:
            c.prec=100;d=Decimal.from_float(v);truth=Decimal(1) if not d else (d.exp()-1)/d
        phierrors.append(abs(float(phi1(np.array(v)))-float(truth)))
    checks['phi1-limit-and-branches']=max(phierrors)<5e-15
    q=np.array([[.3,-.4]]);p=np.array([[.5,-.2]])
    reversals=[];derivatives=[]
    for M,kind in [(1,'NH'),(3,'NHC3')]:
        xi=np.array([[.1,-.05,.02]])[:,:M];eta=np.zeros_like(xi)
        for kappa in [0.,.2]:
            for tau in [.25,1.]:
                z=np.r_[q[0],p[0],xi[0],eta[0]];f=direct_rhs(0,z,M,kappa,tau)
                grad=np.r_[OMEGA**2*q[0]+kappa*q[0]**3,p[0],masses(M,tau)*xi[0],[2.]+[1.]*(M-1)]
                derivatives.append(abs(float(matmul(grad,f)))/(1+np.sum(np.abs(grad*f))))
                for h in [.1,.05]:
                    q1,p1,x1,e1=step(q.copy(),p.copy(),xi.copy(),eta.copy(),h,tau,kappa,kind,budget)
                    q2,p2,x2,e2=step(q1,-p1,-x1,e1,h,tau,kappa,kind,budget)
                    reversals.append(max(maxerr(q2,q),maxerr(-p2,p),maxerr(-x2,xi),maxerr(e2,eta)))
    checks['fullODE-Hext-derivative']=max(derivatives)<1e-13
    checks['physical-R-reversal']=max(reversals)<1e-10
    inverse=[]
    for tau in [.25,1.]:
        for ratio in [.25,1.,4.]:
            pp=np.array([[math.sqrt(2*ratio),0.]])
            plus=radial(pp,.025,tau,'Berendsen');back=radial(plus,-.025,tau,'Berendsen')
            inverse.append(maxerr(back,pp))
    checks['Berendsen-local-inverse']=max(inverse)<1e-13
    try:radial(np.array([[math.sqrt(.5),0.]]),-1,1,'Berendsen');checks['Berendsen-invalid-rejected']=False
    except ValueError:checks['Berendsen-invalid-rejected']=True
    s=radial(p,.1,1,'rescale');s2=radial(2*p,.1,1,'rescale')
    checks['rescale-noninjective-idempotent']=maxerr(s,s2)<1e-14 and maxerr(radial(s,.1,1,'rescale'),s)<1e-14
    # Unexcited physical q=p=0 remains atzero underfiniteNH/NHC; limited counterexample only.
    zeros=np.zeros((1,2));zz=np.zeros((1,3))
    qz,pz,_,_=step(zeros,zeros,zz,zz,.05,1.,0.,'NHC3',budget)
    checks['unexcited-invariant-control']=np.array_equal(qz,zeros) and np.array_equal(pz,zeros)
    return checks,{'phi1_errors':phierrors,'reversal_errors':reversals,'Hext_derivative_residuals':derivatives,
                   'local_inverse_errors':inverse,'nonergodicity_scope':'Physicalzero invariant subset only, not generic-start failure theorem'}


def run(rec,budget,inputs):
    checks,diag=components(budget)
    for k,v in checks.items():rec.check('NH/'+k,v)
    rec.row('NH-components',diag)
    static={}
    for kappa in [0.,.2]:
        r0=static_reference(kappa,128);r1=static_reference(kappa,256)
        keys=['normalizers','q_variance','u_mean','u_variance','h_mean','h_variance','position_cdf','energy_cdf']
        spread=max(maxerr(r0[k],r1[k]) for k in keys)
        qualified=spread<=1e-8
        if kappa==0:
            es=np.array([.5,1.,2.,4.,6.]);qualified=qualified and maxerr(r1['energy_cdf'],1-np.exp(-es)*(1+es))<1e-10
        rec.check('NH/static-reference/'+str(kappa),qualified);static[kappa]=r1
        rec.row('NH-static-reference-'+str(kappa),{'kappa':kappa,'spread':spread,'qualified':qualified,'coarse':r0,'fine':r1})
        for M,kind in [(1,'NH'),(3,'NHC3')]:
            xi=np.array([.1,-.05,.02])[:M];z0=np.r_[.3,-.4,.5,-.2,xi,np.zeros(M)];ts=np.arange(17)/16
            refs=[];ledgers=[]
            for rt,at in [(2e-11,2e-13),(2e-13,2e-15)]:
                budget.own(case='NH-fullODE-reference',kind=kind,kappa=kappa,tau=1.,rtol=rt,atol=at)
                yy,ll=adaptive(lambda t,z:direct_rhs(t,z,M,kappa,1.),z0,ts,budget,rt,at,5000,first_step=1e-3)
                refs.append(yy);ledgers.append(ll)
            rspread=float(np.max(np.abs(refs[0]-refs[1])/(1+np.abs(refs[1]))));rq=rspread<=1e-8
            rec.check('NH/short-reference/%s/%s'%(kind,kappa),rq)
            rec.row('NH-short-reference-%s-%s'%(kind,kappa),{'spread_scaled':rspread,'qualified':rq,'solvers':ledgers},time=ts,state=refs[-1],companion=refs[0])
            errors=[];drifts=[]
            for denom in [512,1024]:
                q=z0[:2][None,:].copy();p=z0[2:4][None,:].copy();x=z0[4:4+M][None,:].copy();e=np.zeros_like(x)
                ys=[z0.copy()];h=1/denom
                for j in range(denom):
                    budget.tick('NH_short_step');budget.own(case='NH-short',kind=kind,kappa=kappa,step=j,q=q,p=p,xi=x,eta=e)
                    q,p,x,e=step(q,p,x,e,h,1.,kappa,kind,budget)
                    if (j+1)%(denom//16)==0:ys.append(np.r_[q[0],p[0],x[0],e[0]])
                ys=np.stack(ys);err=float(np.max(np.abs(ys-refs[-1])/(1+np.abs(refs[-1]))));errors.append(err)
                H=extended(ys[:,:2],ys[:,2:4],ys[:,4:4+M],ys[:,4+M:],kappa,1.)
                drift=float(np.max(np.abs(H-H[0]))/(1+abs(H[0])));drifts.append(drift)
                rec.row('NH-short-%s-%s-%s'%(kind,kappa,denom),{'scaled_fullstate_error':err,'Hext_scaled_drift':drift},time=ts,state=ys,reference=refs[-1],Hext=H)
            oo=order(*errors,max(20*rspread,1e-13));ho=order(*drifts,1e-13)
            rec.goal('NH/short-accuracy/%s/%s'%(kind,kappa),errors[-1]<=2e-5 if rq else None,actual=errors[-1],target=2e-5)
            rec.goal('NH/short-order/%s/%s'%(kind,kappa),oo>=1.7 if oo is not None and rq else None,actual=oo,target=1.7)
            rec.goal('NH/Hext/%s/%s'%(kind,kappa),drifts[-1]<=2e-5,actual=drifts[-1],target=2e-5,scope='Predeclaredstudygoal,notrigorousflowbound')
            rec.goal('NH/Hext-order/%s/%s'%(kind,kappa),ho>=1.7 if ho is not None else None,actual=ho,target=1.7)
    family_count=0
    for kappa,seed in [(0.,93001),(.2,93002)]:
        q0,p0,bathnormal,initledger=canonical_initial(kappa,seed,budget);reference=static[kappa]
        rec.row('NH-initial-'+str(kappa),initledger,q=q0,p=p0,bath_normal=bathnormal)
        for kind in ['NH','NHC3','Berendsen','rescale']:
            for tau in [.25,1.]:
                for h in [.1,.05]:
                    M=3 if kind=='NHC3' else 1;q=q0.copy();p=p0.copy();xi=bathnormal[:,:M]/np.sqrt(masses(M,tau));eta=np.zeros_like(xi)
                    saved=[np.c_[q,p,xi,eta]];times=[0.];K=[];steps=int(round(24/h));keys={int(round(t/h)) for t in [20.,20.5,21.,22.,24.]}
                    for j in range(steps):
                        budget.tick('NH_statistical_step');budget.own(case='deterministic-baths',kind=kind,tau=tau,h=h,kappa=kappa,step=j,q=q,p=p,xi=xi,eta=eta)
                        previous=(q,p,xi,eta)
                        q,p,xi,eta=step(q,p,xi,eta,h,tau,kappa,kind,budget)
                        budget.augment(stage='fullstepcandidate',last_accepted_q=previous[0],last_accepted_p=previous[1],
                                       candidate_q=q,candidate_p=p,candidate_xi=xi,candidate_eta=eta)
                        if not all(np.all(np.isfinite(a)) for a in [q,p,xi,eta]):raise FloatingPointError('Nonfinite deterministic ensemble')
                        K.append([float(np.mean(.5*np.sum(p[:256]**2,axis=-1))),float(np.mean(.5*np.sum(p[256:]**2,axis=-1)))])
                        if j+1 in keys:saved.append(np.c_[q,p,xi,eta]);times.append((j+1)*h)
                    snap=np.stack(saved);diagnostics=[]
                    for label,sl in [('canonical',slice(0,256)),('heated',slice(256,None))]:
                        z=snap[1,sl];qq=z[:,:2];pp=z[:,2:4];kin=.5*np.sum(pp*pp,axis=1);H=physical_energy(qq,pp,kappa)
                        points=np.array([-2.,-1.,0.,1.,2.]);es=np.array([.5,1.,2.,4.,6.])
                        errors=[float(np.max(np.abs(np.mean(qq[:,i,None]<=points[None,:],axis=0)-reference['position_cdf'][i]))) for i in [0,1]]
                        errors += [float(np.max(np.abs(np.mean(kin[:,None]<=es[None,:],axis=0)-(1-np.exp(-es))))),
                                   float(np.max(np.abs(np.mean(H[:,None]<=es[None,:],axis=0)-reference['energy_cdf'])))]
                        family_count+=4;eps=math.sqrt(math.log(2*256/.05)/(2*len(qq)))
                        means=np.r_[qq.mean(axis=0),kin.mean(),H.mean()];truth=np.array([0.,0.,1.,reference['h_mean']])
                        variances=np.r_[qq.var(axis=0,ddof=1),kin.var(ddof=1),H.var(ddof=1)];vtruth=np.r_[reference['q_variance'],1.,reference['h_variance']]
                        meanerr=float(np.max(np.abs(means-truth)/(1+np.abs(truth))));varerr=float(np.max(np.abs(variances-vtruth)/vtruth))
                        rid='%s/%s/%s/%s/%s'%(kappa,kind,tau,h,label)
                        rec.goal('NH/CDF/'+rid,max(errors)<=.08,actual=max(errors),target=.08,DKW_allowance=eps,
                                 simultaneous_classification='certified_hit' if max(errors)+eps<=.08 else 'certified_miss' if max(errors)-eps>.08 else 'unresolved',family_count_total=256)
                        rec.goal('NH/mean/'+rid,meanerr<=.1,actual=meanerr,target=.1)
                        rec.goal('NH/variance/'+rid,varerr<=.2,actual=varerr,target=.2)
                        lags=[]
                        for kk in range(1,6):
                            later=snap[kk,sl];lags.append({'lag':times[kk]-20,'q1':corr(qq[:,0],later[:,0]),'p1':corr(pp[:,0],later[:,2]),
                                  'K':corr(kin,.5*np.sum(later[:,2:4]**2,axis=1))})
                        diagnostics.append({'ensemble':label,'replicas':len(qq),'CDF_errors_q1_q2_K_H':errors,'DKW_allowance':eps,
                            'means':means,'canonical_means':truth,'variances':variances,'canonical_variances':vtruth,'lags':lags,
                            'scope':'Independentinitialreplicas; time20finiteobservation,notmixingproof'})
                    rec.row('NH-stat-%s-%s-%s-%s'%(kappa,kind,tau,h),{'kind':kind,'kappa':kappa,'tau':tau,'h':h,'steps':steps,'diagnostics':diagnostics},
                            time=np.array(times),state=snap,kinetic_mean_history=np.array(K))
    rec.check('NH/CDF-family-count',family_count==256)
