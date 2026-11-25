"""DRAFT 101: three-wave linear periodic educational model, not a DFT solid.

The rank-one kernel is authored, not a norm-conserving fitted element PSP.
Forces differentiate fixed-N Helmholtz free energy, including Fermi entropy.
"""
import math
import numpy as np
from io_utils import eigh_owned, mm, norm


def matrix(k,R,c):
    G=np.array(c['G'],float);p=G+k
    local=np.diag(.5*p*p).astype(complex)
    for i in range(len(G)):
        for j in range(len(G)):
            if abs(G[i]-G[j])==1:local[i,j]=c['local_V1']
    beta=np.exp(-.5*(p/c['projector_sigma'])**2)*np.exp(-1j*p*R)
    dbeta=-1j*p*beta
    nonlocal_part=c['projector_eta']*np.outer(beta,beta.conj())
    derivative=c['projector_eta']*(np.outer(dbeta,beta.conj())+np.outer(beta,dbeta.conj()))
    return local+nonlocal_part,derivative,beta


def cubic_reference(H,return_diagnostics=False):
    """Hermitian 3x3 characteristic-polynomial closed form, no second eigh."""
    q=float(np.trace(H).real/3);B=H-q*np.eye(3)
    p=math.sqrt(float(np.sum(abs(B)**2))/6)
    if p==0:
        values=np.array([q,q,q])
        return {'values':values,'r_raw':None,'r_used':None,'roundoff_clamp_active':False} if return_diagnostics else values
    A=B/p
    # Explicit determinant, independent of NumPy's eigensolver/determinant.
    determinant=A[0,0]*(A[1,1]*A[2,2]-A[1,2]*A[2,1])-A[0,1]*(A[1,0]*A[2,2]-A[1,2]*A[2,0])+A[0,2]*(A[1,0]*A[2,1]-A[1,1]*A[2,0])
    r=float(determinant.real/2)
    if abs(r)>1+1e-12:raise ValueError('Cubic invariant outside real-root range')
    used=max(-1.,min(1.,r));phi=math.acos(used)/3
    values=np.sort([q+2*p*math.cos(phi+2*math.pi*k/3) for k in range(3)])
    return {'values':values,'r_raw':r,'r_used':used,'roundoff_clamp_active':r!=used} if return_diagnostics else values


def occupations(energies,weights,T,N):
    energies=np.array(energies);weights=np.array(weights)[:,None]
    if T<=0 or not 0<N<2*energies.shape[1] or abs(float(weights.sum())-1)>1e-14:
        raise ValueError('Require positive temperature, normalized weights and an interior electron number')
    lo=float(energies.min()-100*T-1);hi=float(energies.max()+100*T+1)
    def values(mu):
        x=(energies-mu)/T;f=np.empty_like(x);positive=x>=0
        with np.errstate(under='ignore'):
            a=np.exp(-x[positive]);b=np.exp(x[~positive])
        f[positive]=2*a/(1+a);f[~positive]=2/(1+b)
        return f
    for _ in range(160):
        mu=(lo+hi)/2
        if float(np.sum(weights*values(mu)))<N:lo=mu
        else:hi=mu
    mu=(lo+hi)/2;f=values(mu);x=f/2;other=1-x
    first=np.zeros_like(x);second=np.zeros_like(x)
    first[x>0]=x[x>0]*np.log(x[x>0]);second[other>0]=other[other>0]*np.log(other[other>0])
    entropy=float(-2*np.sum(weights*(first+second)))
    internal=float(np.sum(weights*f*energies))
    return {'mu':mu,'f':f,'electrons':float(np.sum(weights*f)),
            'binary64_endpoint_occupations':int(np.count_nonzero((f==0)|(f==2))),
            'physical_clipping':False,'entropy_endpoints':'x log x = 0 at x=0; no epsilon floor',
            'entropy':entropy,'band_internal_energy':internal,'free_energy':internal-T*entropy}


def state(R,c,name,save):
    energies=[];bandforces=[];rows=[]
    for i,k in enumerate(c['k']):
        H,dH,beta=matrix(k,R,c);w,v=eigh_owned(H,name+'-k'+str(i),save)
        force=-np.real(np.sum(v.conj()*(mm(dH,v)),axis=0))
        oracle=cubic_reference(H,return_diagnostics=True)
        rows.append({'k':k,'R':R,'energies':w,'vectors':v,'projector_beta':beta,
                     'cubic_reference_error':float(np.max(abs(w-oracle['values']))),'cubic_oracle_diagnostics':oracle,
                     'hermiticity_error':float(np.max(abs(H-H.conj().T))),
                     'residual':float(norm(mm(H,v)-v*w)),
                     'band_forces':force})
        energies.append(w);bandforces.append(force)
    thermo=occupations(energies,c['weights'],c['temperature'],c['electrons'])
    totalforce=float(np.sum(np.array(c['weights'])[:,None]*thermo['f']*np.array(bandforces)))
    return {'rows':rows,'thermo':thermo,'force_minus_free_energy_gradient':totalforce}


def run(c,save):
    center=state(c['projector_R'],c,'101-center',save);differences=[]
    for i,h in enumerate(c['force_delta']):
        left=state(c['projector_R']-h,c,'101-minus'+str(i),save)
        right=state(c['projector_R']+h,c,'101-plus'+str(i),save)
        fd=-(right['thermo']['free_energy']-left['thermo']['free_energy'])/(2*h)
        differences.append({'delta':h,'force_fd_free_energy':fd,'analytic':center['force_minus_free_energy_gradient'],
                            'error':abs(fd-center['force_minus_free_energy_gradient'])})
    return {'center':center,'force_differences':differences,
            'primary_matrices':2,'auxiliary_displaced_matrices':8,
            'scope':'3 plane waves, 2 fixed k points, a rank-one authored projector and Fermi occupations. No self-consistent Hartree/XC, real metal, norm conservation or long MD validation.'}
