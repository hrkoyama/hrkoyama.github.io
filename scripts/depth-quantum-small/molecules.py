"""DRAFT 98/99: explicitly supplied H s-Gaussians, two electrons, <=3 AOs.

Analytic primitive formulas adapted from the unchanged MIT-licensed atlas
molecular-hf/2026-11-22 source; generalizes nuclear positions, adds UHF/FCI/MP2.
No PySCF/SciPy imports. FCI is exact only in the specified finite AO span.
"""
import math
import itertools
import numpy as np
from io_utils import eigh_owned, mm, mv, dot, norm


def boys0(t):
    if t<0 or not math.isfinite(t):raise ValueError('Invalid Boys argument')
    if t<1e-7:return 1-t/3+t*t/10-t*t*t/42
    return .5*math.sqrt(math.pi/t)*math.erf(math.sqrt(t))


def overlap(a,A,b,B):
    p=a+b
    return (math.pi/p)**1.5*math.exp(-a*b/p*float(dot(A-B,A-B)))


def kinetic(a,A,b,B):
    p=a+b;mu=a*b/p
    return mu*(3-2*mu*float(dot(A-B,A-B)))*overlap(a,A,b,B)


def attraction(a,A,b,B,C):
    p=a+b;P=(a*A+b*B)/p
    return -2*math.pi/p*math.exp(-a*b/p*float(dot(A-B,A-B)))*boys0(p*float(dot(P-C,P-C)))


def repulsion(a,A,b,B,c,C,d,D):
    p=a+b;q=c+d;P=(a*A+b*B)/p;Q=(c*C+d*D)/q
    return 2*math.pi**2.5/(p*q*math.sqrt(p+q))*math.exp(-a*b/p*float(dot(A-B,A-B))-c*d/q*float(dot(C-D,C-D)))*boys0(p*q/(p+q)*float(dot(P-Q,P-Q)))


def integrals(positions,charges,basis):
    positions=np.array(positions,float);shell=basis['shells'][0]
    exponents=np.array(shell['exponents']);weights=np.array(shell['coefficients'])*(2*exponents/math.pi)**.75
    contraction_norm=sum(weights[i]*weights[j]*overlap(a,positions[0],b,positions[0]) for i,a in enumerate(exponents) for j,b in enumerate(exponents))
    weights=weights/math.sqrt(contraction_norm);n=len(positions)
    S=np.zeros((n,n));T=S.copy();V=S.copy();g=np.zeros((n,n,n,n))
    for i,A in enumerate(positions):
        for j,B in enumerate(positions):
            for a,wa in zip(exponents,weights):
                for b,wb in zip(exponents,weights):
                    S[i,j]+=wa*wb*overlap(a,A,b,B);T[i,j]+=wa*wb*kinetic(a,A,b,B)
                    V[i,j]+=wa*wb*sum(Z*attraction(a,A,b,B,C) for Z,C in zip(charges,positions))
    for i,j,k,l in itertools.product(range(n),repeat=4):
        A,B,C,D=[positions[x] for x in [i,j,k,l]]
        g[i,j,k,l]=sum(wa*wb*wc*wd*repulsion(a,A,b,B,c,C,d,D)
            for (a,wa),(b,wb),(c,wc),(d,wd) in itertools.product(zip(exponents,weights),repeat=4))
    enuc=sum(charges[i]*charges[j]/float(norm(positions[i]-positions[j])) for i in range(n) for j in range(i))
    return S,T+V,g,enuc


def focks(h,g,pa,pb):
    J=np.einsum('kl,ijkl->ij',pa+pb,g,optimize=False)
    return h+J-np.einsum('kl,ikjl->ij',pa,g,optimize=False),h+J-np.einsum('kl,ikjl->ij',pb,g,optimize=False)


def orthogonalizer(S,name,save):
    ev,U=eigh_owned(S,name+'-overlap',save)
    if ev[0]<=1e-8:raise ValueError('No overlap eigenvector removal is permitted')
    return mm(U/np.sqrt(ev),U.T)


def scf(S,h,g,enuc,c,name,save,broken=False):
    X=orthogonalizer(S,name,save);_,core=eigh_owned(mm(mm(X.T,h),X),name+'-core',save);core=mm(X,core)
    theta=c.get('UHF_initial_g_u_angle',.5) if broken else 0.
    ca=math.cos(theta)*core[:,0]+math.sin(theta)*core[:,1]
    cb=math.cos(theta)*core[:,0]-math.sin(theta)*core[:,1]
    pa=np.outer(ca,ca);pb=np.outer(cb,cb);oldenergy=None;trace=[]
    for step in range(c['max_cycles']):
        fa,fb=focks(h,g,pa,pb)
        _,va=eigh_owned(mm(mm(X.T,fa),X),name+'-a-'+str(step),save)
        _,vb=eigh_owned(mm(mm(X.T,fb),X),name+'-b-'+str(step),save)
        ca=mv(X,va[:,0]);cb=mv(X,vb[:,0]);na=np.outer(ca,ca);nb=np.outer(cb,cb)
        finala,finalb=focks(h,g,na,nb)
        energy=float(.5*np.sum((na+nb)*h)+.5*np.sum(na*finala+nb*finalb))+enuc
        residual=max(float(norm(mm(mm(X.T,mm(mm(f,p),S)-mm(mm(S,p),f)),X))) for f,p in [(finala,na),(finalb,nb)])
        change=float(norm(na-pa)+norm(nb-pb))
        trace.append({'step':step,'energy':energy,'commutator':residual,'density_change':change})
        save(name+'-iteration-'+str(step),{'density_alpha':na,'density_beta':nb,'trace_row':trace[-1]})
        if oldenergy is not None and abs(energy-oldenergy)<c['energy_tolerance'] and change<c['density_tolerance'] and residual<c['commutator_tolerance']:
            break
        pa=(1-c['mixing'])*pa+c['mixing']*na;pb=(1-c['mixing'])*pb+c['mixing']*nb;oldenergy=energy
    else:raise RuntimeError('SCF max_cycles; saved every candidate and history')
    eps,C=eigh_owned(mm(mm(X.T,finala),X),name+'-canonical',save);C=mm(X,C)
    return {'energy':energy,'C':C,'eps':eps,'pa':na,'pb':nb,'ca':ca,'cb':cb,'trace':trace,
            'commutator':residual,'electron_count':float(np.trace(mm(na+nb,S))),
            'spin_square':1-float(dot(ca,mv(S,cb)))**2,'overlap_orthogonality':float(np.max(abs(mm(mm(C.T,S),C)-np.eye(len(S))))),
            'converged':True,'X':X}


def transform(h,g,C):
    return mm(mm(C.T,h),C),np.einsum('ap,bq,cr,ds,abcd->pqrs',C,C,C,C,g,optimize=False)


def product_hamiltonian(h,g):
    n=len(h);out=np.zeros((n*n,n*n))
    for p,q,r,s in itertools.product(range(n),repeat=4):
        out[p*n+q,r*n+s]=h[p,r]*(q==s)+h[q,s]*(p==r)+g[p,r,q,s]
    return out


def apply_ops(bits,ops):
    sign=1
    for create,index in ops:
        occupied=bool(bits & (1<<index))
        if occupied==create:return None
        if bin(bits & ((1<<index)-1)).count('1')%2:sign=-sign
        bits=bits | (1<<index) if create else bits & ~(1<<index)
    return bits,sign


def fermion_reference(h,g):
    """Independent operator/sign assembly in the Nalpha=Nbeta=1 sector."""
    n=len(h);states=[(1<<p)|(1<<(n+q)) for p in range(n) for q in range(n)];where={b:i for i,b in enumerate(states)}
    out=np.zeros((n*n,n*n))
    for column,bits in enumerate(states):
        for p,q in itertools.product(range(n),repeat=2):
            for sigma in range(2):
                result=apply_ops(bits,[(False,q+sigma*n),(True,p+sigma*n)])
                if result and result[0] in where:out[where[result[0]],column]+=result[1]*h[p,q]
        for p,q,r,s in itertools.product(range(n),repeat=4):
            for sigma,tau in itertools.product(range(2),repeat=2):
                result=apply_ops(bits,[(False,q+sigma*n),(False,s+tau*n),(True,r+tau*n),(True,p+sigma*n)])
                if result and result[0] in where:out[where[result[0]],column]+=.5*result[1]*g[p,q,r,s]
    return out


def fci(h,g,C,enuc,name,save):
    hm,gm=transform(h,g,C);H=product_hamiltonian(hm,gm)
    values,vectors=eigh_owned(H,name+'-FCI',save)
    independent=fermion_reference(hm,gm);save(name+'-fermion-reference',{'matrix':independent})
    residual=float(norm(mv(H,vectors[:,0])-values[0]*vectors[:,0]))
    amplitude=vectors[:,0].reshape(len(h),len(h))
    return {'energy':float(values[0]+enuc),'residual':residual,'operator_assembly_error':float(np.max(abs(H-independent))),
            'singlet_spatial_symmetry_error':float(norm(amplitude-amplitude.T)),
            'matrix':H,'coefficients':vectors[:,0],'h_mo':hm,'eri_mo':gm}


def h2_oracles(S,h,g,enuc):
    s=S[0,1];C=np.array([[1/math.sqrt(2*(1+s)),1/math.sqrt(2*(1-s))],
                         [1/math.sqrt(2*(1+s)),-1/math.sqrt(2*(1-s))]])
    hm,gm=transform(h,g,C);A=gm[0,0,0,0];B=gm[1,1,1,1];J=gm[0,0,1,1];K=gm[0,1,0,1]
    linear=2*(hm[1,1]-hm[0,0])-2*A+2*J-4*K;quadratic=A+B-2*J+4*K
    candidates=[0.,1.]
    if quadratic>0:candidates.append(max(0.,min(1.,-linear/(2*quadratic))))
    E=lambda x:2*hm[0,0]+A+linear*x+quadratic*x*x+enuc
    x=min(candidates,key=E);a=2*hm[0,0]+A;b=2*hm[1,1]+B
    return {'RHF':float(E(0)),'UHF_symmetric_pair_variational_min':float(E(x)),'UHF_sin2theta':float(x),
            'FCI_even_singlet':float((a+b-math.hypot(a-b,2*K))/2+enuc),
            'scope':'Analytic gerade/ungerade two-AO H2 model; no general UHF global-minimum theorem.'}


def run(c98,c99,save):
    h2=[]
    for index,R in enumerate(c98['bonds_bohr']):
        name='98-H2-'+str(index);positions=[[0,0,-R/2],[0,0,R/2]]
        S,h,g,enuc=integrals(positions,[1,1],c98['basis']);save(name+'-integrals',{'S':S,'h':h,'eri':g,'enuc':enuc})
        rhf=scf(S,h,g,enuc,c98,name+'-RHF',save)
        uhf=scf(S,h,g,enuc,c98,name+'-UHF',save,broken=True)
        exact=fci(h,g,rhf['X'],enuc,name,save)
        h2.append({'bond':R,'RHF':rhf,'UHF':uhf,'FCI':exact,'oracle':h2_oracles(S,h,g,enuc)})
    S,h,g,enuc=integrals(c99['nuclei_bohr'],c99['charges'],c98['basis']);save('99-H3-integrals',{'S':S,'h':h,'eri':g,'enuc':enuc})
    rhf=scf(S,h,g,enuc,c99,'99-H3-RHF',save);exact=fci(h,g,rhf['C'],enuc,'99-H3',save)
    _,gm=transform(h,g,rhf['C']);eps=rhf['eps'];n=len(S)
    correction=sum(gm[0,a,0,b]**2/(2*eps[0]-eps[a]-eps[b]) for a in range(1,n) for b in range(1,n))
    independent=sum(exact['matrix'][0,a*n+b]**2/(2*eps[0]-eps[a]-eps[b]) for a in range(1,n) for b in range(1,n))
    return {'H2':h2,'H3plus':{'RHF':rhf,'MP2_energy':float(rhf['energy']+correction),'MP2_correlation':float(correction),
            'MP2_determinant_RS2_oracle':float(independent),'FCI':exact,'geometry':c99['nuclei_bohr'],
            'minimum_MP2_gap':float(min(eps[a]+eps[b]-2*eps[0] for a in range(1,n) for b in range(1,n)))}}
