"""Linear mass-weighted constraints, actualDOF and canonical-start finite-time tests."""
from __future__ import annotations
from common import matmul,dot,array_norm
from fractions import Fraction as F
import math
import numpy as np
from common import corr,gamma_half_cdf,maxerr,normal_cdf
MASS=np.array([1.,2.,3.]);D2=np.array([1.,1.7**2,1.3**2])
CONFIGS=['none','COM','COM-relative','COM-relative-redundant']
ROWS=[[],[[1,2,3]],[[1,2,3],[1,-1,0]],[[1,2,3],[1,-1,0],[2,-2,0]]]


def basis(index):
    a=np.array([math.sqrt(2/3),-1/math.sqrt(3),0.]);b=np.array([1/math.sqrt(6),1/math.sqrt(3),-1/math.sqrt(2)])
    if index==0:return np.eye(3)
    return np.c_[a,b] if index==1 else b[:,None]


def rational_covariance(rows):
    # Exact RREF keeps independent originalrows; redundantGram never inverted as fullrank.
    independent=[];pivots=[];reduced=[]
    for row in rows:
        a=list(map(F,row))
        for pivot,b in zip(pivots,reduced):
            scale=a[pivot];a=[x-scale*y for x,y in zip(a,b)]
        nonzero=[j for j,x in enumerate(a) if x]
        if nonzero:
            pivot=nonzero[0];scale=a[pivot];a=[x/scale for x in a]
            pivots.append(pivot);reduced.append(a);independent.append(list(map(F,row)))
    r=len(independent);G=[[sum(a[k]*b[k]/F(k+1) for k in range(3)) for b in independent] for a in independent]
    aug=[row+[F(int(i==j)) for j in range(r)] for i,row in enumerate(G)]
    for i in range(r):
        pivot=next(k for k in range(i,r) if aug[k][i]);aug[i],aug[pivot]=aug[pivot],aug[i]
        s=aug[i][i];aug[i]=[x/s for x in aug[i]]
        for k in range(r):
            if k==i:continue
            s=aug[k][i];aug[k]=[x-s*y for x,y in zip(aug[k],aug[i])]
    inv=[row[r:] for row in aug]
    cov=[[F((i+1)*int(i==j))-sum(independent[a][i]*inv[a][b]*independent[b][j] for a in range(r) for b in range(r)) for j in range(3)] for i in range(3)]
    return 3-r,cov


def csvr(s,delta,tau,R,chi):
    s=np.asarray(s,dtype=float);R=np.asarray(R);chi=np.asarray(chi)
    if s.ndim<1 or s.shape[-1]<1 or not np.all(np.isfinite(s)):raise ValueError('Finite nonempty tangent vector required')
    if not math.isfinite(delta) or delta<0 or not math.isfinite(tau) or tau<=0:raise ValueError('Invalid bath duration/coupling')
    if not np.all(np.isfinite(R)) or not np.all(np.isfinite(chi)) or np.any(chi<0):raise ValueError('Invalid draws')
    if s.shape[-1]==1 and np.any(chi!=0):raise ValueError('f1requireszerochi-square')
    if delta==0:return s.copy()
    scale=np.max(np.abs(s),axis=-1)
    if np.any(scale==0):raise ValueError('Positive-timezeroK has no radial direction')
    reduced=s/scale[...,None];norm=np.sqrt(np.sum(reduced*reduced,axis=-1));unit=reduced/norm[...,None]
    rootK=scale*norm/math.sqrt(2);sigma=math.sqrt(-math.expm1(-delta/tau)/2)
    radial=math.exp(-delta/(2*tau))*rootK+sigma*R
    signed_radius=np.copysign(math.sqrt(2)*np.hypot(radial,sigma*np.sqrt(chi)),radial)
    answer=unit*signed_radius[...,None]
    if not np.all(np.isfinite(answer)):raise FloatingPointError('Nonfinite CSVR')
    return answer


def bath(s,delta,kind,g,budget):
    if s.shape[-1]<1 or not np.all(np.isfinite(s)):raise ValueError('PositiveDOF finite tangents required')
    if delta==0:return s.copy()
    if kind=='Langevin':
        noise=g.normal(size=s.shape);budget.tick('constraint_Langevin_normal',s.size)
        return math.exp(-delta)*s+math.sqrt(-math.expm1(-2*delta))*noise
    if np.any(np.max(np.abs(s),axis=-1)==0):raise ValueError('ValidatezeroK before RNG')
    normal=g.normal(size=s.shape[:-1]);budget.tick('constraint_CSVR_normal',normal.size)
    if s.shape[-1]>1:
        chi=g.chisquare(s.shape[-1]-1,size=s.shape[:-1]);budget.tick('constraint_CSVR_chisquare',chi.size)
    else:chi=np.zeros(s.shape[:-1])
    return csvr(s,delta,.5,normal,chi)


def verlet(r,s,h,K):
    s=s-h/2*(matmul(r,K.T));r=r+h*s;s=s-h/2*(matmul(r,K.T))
    return r,s


def matrix_exp(A):
    size=len(A);norm=float(array_norm(A,np.inf));scale=max(0,int(math.ceil(math.log2(norm/.25)))) if norm>.25 else 0
    B=A/(2**scale);out=np.eye(size);term=out.copy()
    for j in range(1,129):
        term=matmul(term,B)/j;out+=term
        if np.max(np.abs(term))<1e-18:break
    else:raise RuntimeError('Matrix exponential cap')
    for _ in range(scale):out=matmul(out,out)
    return out


def discrete_matrices(K,h):
    f=len(K);I=np.eye(f);O=np.diag(np.r_[np.ones(f),np.full(f,math.exp(-h/2))])
    V=np.block([[I-h*h*K/2,h*I],[-h*K+h**3*(matmul(K,K))/4,I-h*h*K/2]])
    B=np.diag(np.r_[np.zeros(f),np.full(f,-math.expm1(-h))])
    D=matmul(matmul(O,V),O);noise=matmul(matmul(matmul(O,V),B),(matmul(O,V)).T)+B
    return D,noise,O,V,B


def kinetic_cdfs(cov,points,angular):
    vals=np.linalg.eigvalsh(cov);f=len(vals)
    if np.min(vals)<=0:raise ValueError('PositiveGaussian covariance needed')
    if f==1:return [gamma_half_cdf(x/vals[0],1) for x in points]
    theta=np.arange(angular)*2*math.pi/angular
    if f==2:
        weights=np.ones(angular)/angular;factors=vals[0]*np.cos(theta)**2+vals[1]*np.sin(theta)**2
    else:
        z,w=np.polynomial.legendre.leggauss(angular//4)
        factors=((1-z*z)[:,None]*(vals[0]*np.cos(theta)[None,:]**2+vals[1]*np.sin(theta)[None,:]**2)+vals[2]*z[:,None]**2).reshape(-1)
        weights=np.broadcast_to(w[:,None]/(2*angular),(len(w),angular)).reshape(-1)
    result=[]
    for point in points:
        xx=point/factors
        if f==2:cdf=-np.expm1(-xx)
        else:cdf=np.array([math.erf(math.sqrt(x))-2*math.sqrt(x/math.pi)*math.exp(-x) for x in xx])
        result.append(float(matmul(weights,cdf)))
    return result


def references(index,K,h,budget,continuous):
    f=len(K);D,noise,O,V,B=discrete_matrices(K,h)
    S0=np.block([[np.linalg.inv(K),np.zeros((f,f))],[np.zeros((f,f)),np.eye(f)]])
    # Independently construct actualnoise-free splitmap from standardbasis columns.
    columns=[]
    for j in range(2*f):
        vec=np.eye(2*f)[:,j];r=vec[:f][None,:];s=math.exp(-h/2)*vec[f:][None,:]
        rr,ss=verlet(r,s,h,K);columns.append(np.r_[rr[0],math.exp(-h/2)*ss[0]])
    direct=np.array(columns).T
    sigma=math.sqrt(-math.expm1(-h));E=np.vstack([np.zeros((f,f)),sigma*np.eye(f)])
    J1=matmul(matmul(O,V),E);J2=E;noise_direct=matmul(J1,J1.T)+matmul(J2,J2.T)
    if maxerr(direct,D)>1e-13 or maxerr(noise_direct,noise)>1e-13:raise ValueError('Independent OBABO block qualification')
    rho=float(np.max(np.abs(np.linalg.eigvals(D))))
    if not rho<1:raise ValueError('Discrete bathmap unstable')
    Sh=np.linalg.solve(np.eye(4*f*f)-np.kron(D,D),noise.reshape(-1)).reshape(2*f,2*f)
    lyap=maxerr(Sh,matmul(matmul(D,Sh),D.T)+noise)/(1+float(np.max(np.abs(Sh))))
    if lyap>1e-12:raise ValueError('Discrete Lyapunov qualification')
    records=[];Sn=S0.copy();Dn=np.eye(2*f);targets={int(round(t/h)):t for t in [0,.5,1,2,4]}
    for j in range(int(round(4/h))+1):
        if j in targets:
            t=targets[j];cont,error=continuous[t]
            kc0=kinetic_cdfs(Sn[f:,f:],[.25,.5,1,2,4],128)
            kc1=kinetic_cdfs(Sn[f:,f:],[.25,.5,1,2,4],256)
            if maxerr(kc0,kc1)>1e-10:raise ValueError('Finite-time kinetic angular reference failed')
            records.append({'time':t,'canonical_start_covariance':Sn.copy(),'crosscov_to_initial':matmul(Dn,S0),
                'continuous_crosscov':cont,'continuous_companion_error':error,'K_CDF':kc1,'K_CDF_refinement':maxerr(kc0,kc1)})
            budget.tick('constraint_covariance_action')
        if j==round(4/h):break
        Sn=matmul(matmul(D,Sn),D.T)+noise;Dn=matmul(D,Dn)
    return records,{'spectral_radius':rho,'Lyapunov_residual':lyap,'stationary_covariance':Sh,
        'canonical_initial_covariance':S0,'Dh':D,'Qh':noise,'half_bath_B':B,
        'noise_identity':'Qh=(OhVh)B(OhVh)^T+B; initialSn=S0, stationarySh separately retained'}


def components(budget):
    checks={};records=[]
    for i in range(4):
        Q=basis(i);f=Q.shape[1];C=np.array(ROWS[i],dtype=float).reshape(-1,3)
        dof,cov=rational_covariance(ROWS[i]);rational=np.array([[float(x) for x in row] for row in cov])
        pmap=np.sqrt(MASS)[:,None]*Q;weighted=C/np.sqrt(MASS)[None,:]
        rank=int(np.linalg.matrix_rank(weighted)) if len(C) else 0
        checks['rank/'+str(i)]=dof==f==3-rank
        checks['projector/'+str(i)]=maxerr(matmul(Q.T,Q),np.eye(f))<1e-12 and (not len(C) or float(np.max(np.abs(matmul(weighted,Q))))<1e-12)
        checks['rational-covariance/'+str(i)]=maxerr(matmul(pmap,pmap.T),rational)<1e-12
        # Positive projected-isotropicOU identity, not a false negativecontrol.
        s=np.arange(1,f+1,dtype=float);xi=np.array([.3,-.7,1.1]);P0=matmul(Q,Q.T);a=math.exp(-.2);sigma=math.sqrt(1-a*a)
        checks['projected-OU-positive/'+str(i)]=maxerr(matmul(P0,matmul(a*Q,s)+sigma*xi),matmul(Q,a*s+matmul(sigma*Q.T,xi)))<1e-12
        records.append({'config':CONFIGS[i],'f':f,'Fraction_covariance':[[str(x) for x in row] for row in cov]})
    dof,cov=rational_covariance([[1,0,0],[0,1,0],[0,0,1]])
    checks['full-rank-zero-dimensional-fixture']=dof==0 and all(x==0 for row in cov for x in row)
    checks['redundant-common-latent']=np.array_equal(basis(2),basis(3))
    actions=[];signflips=0
    for s0 in [-1.,1.]:
        for R in [-4.,0.,4.]:
            actual=float(csvr(np.array([[s0]]),.2,.5,np.array([R]),np.array([0.]))[0,0])
            expected=math.exp(-.2)*s0+math.copysign(1.,s0)*math.sqrt(-math.expm1(-.4))*R
            actions.append({'s':s0,'R':R,'actual':actual,'same_draw_OU':expected})
            signflips+=actual*s0<0
    checks['six-signed-f1']=max(abs(x['actual']-x['same_draw_OU']) for x in actions)<1e-12 and signflips>=2
    for label,s,delta in [('f0',np.empty((1,0)),.2),('zeroK',np.zeros((1,1)),.2)]:
        try:csvr(s,delta,.5,np.array([0.]),np.array([0.]));checks[label+'-rejects']=False
        except ValueError:checks[label+'-rejects']=True
    s=np.array([[0.]]);owned=csvr(s,0,.5,np.array([0.]),np.array([0.]))
    checks['h0-owned-copy']=np.array_equal(owned,s) and not np.shares_memory(owned,s)
    # WrongambientDOF radial bath adds chi-square2 instead of chi-square0.
    good=csvr(np.array([[1.]]),.2,.5,np.array([0.]),np.array([0.]))
    ambient=basis(2)[:,0][None,:];bad=matmul(csvr(ambient,.2,.5,np.array([0.]),np.array([2.])),basis(2))
    checks['wrong-ambient-CSVR-detected']=maxerr(good,bad)>.01
    return checks,{'rational_fixtures':records,'signed_f1_actions':actions,'signflips':int(signflips),
            'DOF_negative':'Ambient3 radial rescaling on tangentf1 uses wrong conditionalenergy law; isotropicprojectedOU is valid',
            'redundant_seed_scope':'Productionseeds94003/94004 intentionally independent, no trajectory-equality claim'}


def run(rec,budget,inputs):
    checks,diag=components(budget)
    for k,v in checks.items():rec.check('constraints/'+k,v)
    rec.row('constraints-components',diag)
    families=0
    for index in range(4):
        Q=basis(index);f=Q.shape[1];K=matmul(Q.T,D2[:,None]*Q);L=np.linalg.cholesky(K)
        initial=np.random.Generator(np.random.PCG64(94001+index));zq=initial.normal(size=(1024,f));zp=initial.normal(size=(1024,f))
        r0=np.linalg.solve(L.T,zq.T).T;s0=zp.copy();budget.tick('constraint_initial_normal',2*1024*f)
        canonical_p=matmul(np.sqrt(MASS)[:,None]*Q,s0.T)
        S0=np.block([[np.linalg.inv(K),np.zeros((f,f))],[np.zeros((f,f)),np.eye(f)]])
        A=np.block([[np.zeros((f,f)),np.eye(f)],[-K,-np.eye(f)]])
        continuous={}
        for lag in [0.,.5,1.,2.,4.]:
            cont=matmul(matrix_exp(A*lag),S0)
            ev,U=np.linalg.eig(A*lag);comp=matmul(matmul(matmul(U,np.diag(np.exp(ev))),np.linalg.inv(U)),S0)
            error=maxerr(cont,comp.real)
            if np.max(np.abs(comp.imag))>1e-11 or error>5e-11:raise ValueError('Continuousmatrixcompanionfailed')
            continuous[lag]=(cont,error);budget.tick('constraint_continuous_exponential')

        rec.row('constraints-initial-'+str(index),{'config':CONFIGS[index],'f':f,'seed':94001+index,'Cholesky':'K=L L^T positive diagonal;r=L^-T z',
                'generator_final':initial.bit_generator.state},Q=Q,K_reduced=K,r=r0,s=s0,ambient_p=canonical_p.T)
        for kind,bathcode in [('Langevin',0),('CSVR',1)]:
            for h,hcode in [(.1,0),(.05,1)]:
                r=r0.copy();s=s0.copy();g=np.random.Generator(np.random.PCG64(np.random.SeedSequence([94000,index,bathcode,hcode])))
                saved=[np.c_[r,s]];times=[0.];steps=int(round(4/h));keys={int(round(t/h)) for t in [.5,1.,2.,4.]}
                reference,refmeta=references(index,K,h,budget,continuous) if kind=='Langevin' else (None,None)
                for j in range(steps):
                    budget.tick('constraint_primary_step');budget.own(case='constraints',config=CONFIGS[index],kind=kind,h=h,step=j,r=r,s=s)
                    previous_r=r;previous_s=s
                    s=bath(s,h/2,kind,g,budget);r,s=verlet(r,s,h,K)
                    budget.augment(stage='afterVerlet-beforesecondbath',candidate_r=r,candidate_s=s)
                    s=bath(s,h/2,kind,g,budget)
                    budget.augment(stage='OBABOcandidate',last_accepted_r=previous_r,last_accepted_s=previous_s,candidate_r=r,candidate_s=s)
                    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(s)):raise FloatingPointError('Nonfinite constrained ensemble')
                    if j+1 in keys:saved.append(np.c_[r,s]);times.append((j+1)*h)
                snap=np.stack(saved);diagnostics=[]
                for j,t in enumerate(times):
                    momenta=snap[j,:,f:];Kobs=.5*np.sum(momenta*momenta,axis=1);points=np.array([-2.,-1.,0.,1.,2.]);kp=np.array([.25,.5,1.,2.,4.])
                    canonical=[];discrete=[]
                    for a in range(f):
                        empirical=np.mean(momenta[:,a,None]<=points[None,:],axis=0);truth=np.array([normal_cdf(x) for x in points])
                        canonical.append(float(np.max(np.abs(empirical-truth))))
                        if reference is not None:
                            sigma=math.sqrt(reference[j]['canonical_start_covariance'][f+a,f+a]);finite=np.array([normal_cdf(x/sigma) for x in points]);discrete.append(float(np.max(np.abs(empirical-finite))))
                    empiricalK=np.mean(Kobs[:,None]<=kp[None,:],axis=0);canonK=np.array([gamma_half_cdf(x,f) for x in kp]);canonical.append(float(np.max(np.abs(empiricalK-canonK))))
                    if reference is not None:discrete.append(float(np.max(np.abs(empiricalK-reference[j]['K_CDF']))))
                    families+=f+1;eps=math.sqrt(math.log(2*220/.05)/(2*1024))
                    initial_s=snap[0,:,f:];lags=[corr(initial_s[:,a],momenta[:,a]) for a in range(f)]
                    product_SE=[float(np.std(initial_s[:,a]*momenta[:,a],ddof=1)/math.sqrt(1024)) for a in range(f)]
                    diagnostics.append({'time':t,'canonical_CDF_errors':canonical,'actual_discrete_Gaussian_CDF_errors':discrete if reference is not None else None,
                        'DKW_simultaneous_allowance':eps,'mean_K':float(Kobs.mean()),'variance_K':float(Kobs.var(ddof=1)),
                        'temperature_actual_f':float(2*Kobs.mean()/f),'temperature_wrong_ambient3':float(2*Kobs.mean()/3),
                        'signed_two_time_moments':lags,'product_empirical_SE_approximate':product_SE,
                        'K_two_time':corr(.5*np.sum(initial_s**2,axis=1),Kobs),
                        'reference':None if reference is None else reference[j],
                        'scope':'Canonicaltargetisastudy; Langevinfinite-timenullisactualS0transient,notstationarySh; CSVRACFempirical'})
                    rec.goal('constraints/canonicalCDF/%s/%s/%s/%s'%(index,kind,h,t),max(canonical)<=.08,actual=max(canonical),target=.08,DKW_allowance=eps)
                    if discrete:rec.goal('constraints/discreteCDF/%s/%s/%s'%(index,h,t),max(discrete)<=eps,actual=max(discrete),nominal_allowance=eps)
                ambient=np.sqrt(MASS)[None,:]*(matmul(snap[-1,:,f:],Q.T));constraint=np.array(ROWS[index],dtype=float).reshape(-1,3)
                residual=0. if not len(constraint) else float(np.max(np.abs(matmul(ambient/MASS,constraint.T))))
                rec.check('constraints/actual-tangent/%s/%s/%s'%(index,kind,h),residual<=1e-12*(1+float(np.max(np.abs(ambient)))))
                rec.row('constraints-%s-%s-%s'%(index,kind,h),{'config':CONFIGS[index],'f':f,'kind':kind,'h':h,'steps':steps,
                        'generator_final':g.bit_generator.state,'constraint_residual':residual,'diagnostics':diagnostics,'matrix_reference':refmeta},
                        time=np.array(times),state=snap,ambient_p=ambient,Q=Q)
    rec.check('constraints/CDF-family-count',families==220)
    rec.check('constraints/continuous-reference-count',budget.counts.get('constraint_continuous_exponential')==20)
    rec.check('constraints/discrete-covariance-count',budget.counts.get('constraint_covariance_action')==40)
    rec.check('constraints/initial-normal-count',budget.counts.get('constraint_initial_normal')==14336)
    rec.check('constraints/Langevin-normal-count',budget.counts.get('constraint_Langevin_normal')==1720320)
    rec.check('constraints/CSVR-normal-count',budget.counts.get('constraint_CSVR_normal')==983040)
    rec.check('constraints/CSVR-chi-square-count',budget.counts.get('constraint_CSVR_chisquare')==491520)
