"""Original educational analytic s-Gaussian RHF for clamped-nuclei H2.

This module imports neither PySCF nor any integral/reference implementation.
Only normalized real s Gaussian contractions and two closed-shell electrons.
"""
from math import erf, exp, pi, sqrt
from itertools import product
import numpy as np
from scipy.linalg import eigh


def mm(a,b):
    # Explicit contraction avoids vendor-BLAS FP flag artifacts on tiny matrices.
    return np.einsum('ij,jk->ik',a,b,optimize=False)


def boys0(x):
    if x < 0 or not np.isfinite(x):
        raise ValueError('Boys argument must be finite and nonnegative')
    if x < 1e-7:
        return 1-x/3+x*x/10-x*x*x/42
    return .5*sqrt(pi/x)*erf(sqrt(x))


def normalization(a):
    return (2*a/pi)**.75


def primitive_overlap(a,A,b,B):
    p=a+b;mu=a*b/p
    return (pi/p)**1.5*exp(-mu*np.dot(A-B,A-B))


def primitive_kinetic(a,A,b,B):
    p=a+b;mu=a*b/p;r2=np.dot(A-B,A-B)
    return mu*(3-2*mu*r2)*primitive_overlap(a,A,b,B)


def primitive_nuclear(a,A,b,B,C):
    p=a+b;mu=a*b/p;P=(a*A+b*B)/p
    return -2*pi/p*exp(-mu*np.dot(A-B,A-B))*boys0(p*np.dot(P-C,P-C))


def primitive_eri(a,A,b,B,c,C,d,D):
    p=a+b;q=c+d;P=(a*A+b*B)/p;Q=(c*C+d*D)/q
    prefactor=2*pi**2.5/(p*q*sqrt(p+q))
    return prefactor*exp(-a*b/p*np.dot(A-B,A-B)-c*d/q*np.dot(C-D,C-D))*boys0(p*q/(p+q)*np.dot(P-Q,P-Q))


def basis_functions(definition,bond):
    if not np.isfinite(bond) or bond<=0:raise ValueError('Positive finite bond length required')
    functions=[]
    for z in [-bond/2,bond/2]:
        A=np.array([0.,0.,z])
        for shell in definition['shells']:
            exponents=np.asarray(shell['exponents'],float);coeff=np.asarray(shell['coefficients'],float)
            if not len(exponents) or exponents.shape!=coeff.shape or not np.isfinite(exponents).all() or not np.isfinite(coeff).all() or (exponents<=0).any():raise ValueError('Invalid s shell')
            weights=coeff*np.array([normalization(a) for a in exponents])
            norm=sum(weights[i]*weights[j]*primitive_overlap(a,A,b,A) for i,a in enumerate(exponents) for j,b in enumerate(exponents))
            if norm<=0:raise ValueError('Zero contraction norm')
            functions.append((A,exponents,weights/sqrt(norm)))
    return functions


def integrals(definition,bond):
    functions=basis_functions(definition,bond);n=len(functions)
    S=np.zeros((n,n));T=S.copy();V=S.copy();eri=np.zeros((n,n,n,n))
    nuclei=[np.array([0.,0.,z]) for z in [-bond/2,bond/2]]
    def pair(i,j,fn):
        A,aa,ca=functions[i];B,bb,cb=functions[j]
        return sum(wa*wb*fn(a,A,b,B) for a,wa in zip(aa,ca) for b,wb in zip(bb,cb))
    for i in range(n):
        for j in range(i+1):
            S[i,j]=S[j,i]=pair(i,j,primitive_overlap)
            T[i,j]=T[j,i]=pair(i,j,primitive_kinetic)
            V[i,j]=V[j,i]=sum(pair(i,j,lambda a,A,b,B:primitive_nuclear(a,A,b,B,C)) for C in nuclei)
    # Eightfold permutation symmetry avoids recomputing equivalent integrals.
    pairs=[(i,j) for i in range(n) for j in range(i+1)]
    for ij,(i,j) in enumerate(pairs):
        A,aa,ca=functions[i];B,bb,cb=functions[j]
        for k,l in pairs[:ij+1]:
            C,cc,ck=functions[k];D,dd,cl=functions[l]
            value=sum(wa*wb*wc*wd*primitive_eri(a,A,b,B,c,C,d,D)
                      for (a,wa),(b,wb),(c,wc),(d,wd) in product(zip(aa,ca),zip(bb,cb),zip(cc,ck),zip(dd,cl)))
            for p,q,r,s in [(i,j,k,l),(j,i,k,l),(i,j,l,k),(j,i,l,k),(k,l,i,j),(l,k,i,j),(k,l,j,i),(l,k,j,i)]:eri[p,q,r,s]=value
    return S,T,V,eri


def fock(H,eri,P):
    return H+np.einsum('kl,ijkl->ij',P,eri)-.5*np.einsum('kl,ikjl->ij',P,eri)


def solve(definition,bond,options):
    for key in ['energy_tolerance','density_tolerance','residual_tolerance','overlap_minimum']:
        if isinstance(options[key],bool) or not np.isfinite(options[key]) or options[key]<=0:raise ValueError('Positive finite SCF tolerances required')
    if type(options['max_cycles']) is not int or options['max_cycles']<1:raise ValueError('max_cycles must be a positive integer')
    if not np.isfinite(options['mixing']) or not 0<options['mixing']<=1:raise ValueError('mixing must lie in (0,1]')
    if not np.isfinite(options.get('initial_rotation',.15)):raise ValueError('Finite initial rotation required')
    S,T,V,eri=integrals(definition,bond);H=T+V;n=len(S)
    eig,U=eigh(S)
    if eig[0]<=options['overlap_minimum']:raise ValueError('Nearly linearly dependent overlap; no basis function is discarded')
    condition=float(eig[-1]/eig[0]);X=mm(U/np.sqrt(eig),U.T)
    _,C=eigh(H,S)
    # A controlled symmetry-breaking starting orbital makes SCF histories informative
    # even when the symmetric minimal-basis core guess is already self consistent.
    theta=options.get('initial_rotation',.15)
    orbital=np.cos(theta)*C[:,0]+np.sin(theta)*C[:,1]
    mixed=2*np.outer(orbital,orbital)
    previous_energy=None;previous_density=None;trace=[];converged=False
    for iteration in range(1,options['max_cycles']+1):
        orbital_energies,C=eigh(fock(H,eri,mixed),S)
        P=2*np.outer(C[:,0],C[:,0]);F=fock(H,eri,P)
        energy_electronic=float(.5*np.einsum('ij,ji',P,H+F));energy=energy_electronic+1/bond
        residual=mm(mm(X.T,mm(mm(F,P),S)-mm(mm(S,P),F)),X)
        commutator=float(np.linalg.norm(residual))
        dE=abs(energy-previous_energy) if previous_energy is not None else None
        dP=float(np.linalg.norm(P-previous_density)) if previous_density is not None else None
        trace.append(dict(iteration=iteration,energy_total=energy,delta_energy=dE,density_change=dP,scf_commutator_norm=commutator))
        if dE is not None and dE<=options['energy_tolerance'] and dP<=options['density_tolerance'] and commutator<=options['residual_tolerance']:
            converged=True;break
        mixed=(1-options['mixing'])*mixed+options['mixing']*P
        previous_energy=energy;previous_density=P
    rayleigh=np.diag(mm(mm(C.T,F),C))
    orbital_residual=float(np.linalg.norm(mm(X.T,mm(F,C)-mm(mm(S,C),np.diag(rayleigh)))))
    # Energy reconstructed independently from occupied-orbital Coulomb/exchange.
    c=C[:,0]
    coulomb=float(np.einsum('i,j,k,l,ijkl',c,c,c,c,eri))
    occupied_energy=2*float(np.einsum('i,ij,j',c,H,c))+coulomb+1/bond
    return dict(bond_bohr=bond,basis_id=definition['id'],nbf=n,energy_total=energy,energy_electronic=energy_electronic,nuclear_repulsion=1/bond,
                converged=converged,termination='converged' if converged else 'max_cycles',iterations=iteration,
                scf_commutator_norm=commutator,orbital_residual_norm=orbital_residual,
                orthogonality_max=float(np.abs(mm(mm(C.T,S),C)-np.eye(n)).max()),electron_count=float(np.trace(mm(P,S))),
                error_electron_count=abs(float(np.trace(mm(P,S)))-2),idempotency_norm=float(np.linalg.norm(mm(mm(P,S),P)-2*P)),
                energy_consistency_error=abs(energy-occupied_energy),overlap_min_eigenvalue=float(eig[0]),overlap_condition_number=condition,
                trace=trace,density=P.tolist(),orbital_coefficients=C.tolist())
