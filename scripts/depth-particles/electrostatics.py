"""Original tiny-cell Ewald and B-spline smooth-PME educational solvers.

Coulomb constant is one; neutral cubic cells, conducting/tin-foil boundary.
The PME variant is Essmann-type smooth PME, not Darden's original Lagrange PME.
"""
from itertools import product
from math import comb, factorial, pi, sqrt
import numpy as np
from scipy.special import erfc


def validate(positions, charges, length):
    x=np.asarray(positions,dtype=float);q=np.asarray(charges,dtype=float)
    if x.ndim!=2 or x.shape[1]!=3 or q.shape!=(len(x),) or len(x)<2:
        raise ValueError('Need N x 3 positions and N charges')
    if not np.isfinite(x).all() or not np.isfinite(q).all() or not np.isfinite(length) or length<=0:
        raise ValueError('Finite coordinates/charges and positive cell required')
    if abs(q.sum())>1e-12: raise ValueError('Neutral cells only; no neutralizing background correction')
    x=x%length
    delta=x[:,None,:]-x[None,:,:];delta-=length*np.rint(delta/length)
    distance=np.linalg.norm(delta,axis=-1);np.fill_diagonal(distance,np.inf)
    if distance.min()<1e-7*length:raise ValueError('Coincident periodic particles')
    return x,q


def real_space(x,q,length,alpha,images):
    if alpha<=0 or images<0:raise ValueError('Positive alpha and nonnegative image cutoff required')
    shifts=np.array(list(product(range(-images,images+1),repeat=3)),dtype=float)*length
    d=x[:,None,None,:]-x[None,:,None,:]+shifts[None,None,:,:]
    r=np.linalg.norm(d,axis=-1)
    valid=r>1e-12*length;safe=np.where(valid,r,1.)
    qq=q[:,None,None]*q[None,:,None]
    kernel=np.where(valid,erfc(alpha*safe)/safe,0.)
    energy=.5*np.sum(qq*kernel)
    factor=np.where(valid,erfc(alpha*safe)/safe**3+2*alpha/sqrt(pi)*np.exp(-(alpha*safe)**2)/safe**2,0.)
    force=np.sum(qq[:,:,:,None]*factor[:,:,:,None]*d,axis=(1,2))
    return float(energy),force


def reciprocal_vectors(length,kmax):
    if not isinstance(kmax,int) or kmax<1:raise ValueError('Positive integer reciprocal cutoff required')
    n=np.array(list(product(range(-kmax,kmax+1),repeat=3)),dtype=float)
    n=n[np.any(n!=0,axis=1)]
    return 2*pi/length*n


def ewald(positions,charges,length=1.,alpha=5.6,images=2,kmax=12):
    x,q=validate(positions,charges,length)
    real_energy,force=real_space(x,q,length,alpha,images)
    k=reciprocal_vectors(length,kmax);k2=np.sum(k*k,axis=1)
    phase=np.exp(1j*np.einsum('ia,ka->ik',x,k,optimize=False));s=np.sum(q[:,None]*phase,axis=0);g=np.exp(-k2/(4*alpha**2))/k2
    reciprocal=2*pi/length**3*np.sum(g*np.abs(s)**2)
    force+=4*pi/length**3*q[:,None]*np.einsum('ik,ka->ia',np.imag(phase*np.conj(s))*g,k,optimize=False)
    self_energy=-alpha/sqrt(pi)*np.dot(q,q)
    return float(real_energy+reciprocal+self_energy),force


def cardinal_spline(x,order,derivative=False):
    """Cardinal M_p and its first derivative, support [0,p]."""
    if order not in (4,6,8):raise ValueError('Supported even spline orders: 4,6,8')
    degree=order-2 if derivative else order-1
    answer=np.zeros_like(np.asarray(x,dtype=float))
    for k in range(order+1):answer+=(-1)**k*comb(order,k)*np.maximum(np.asarray(x)-k,0.)**degree
    return answer/factorial(degree)


def assignment(position,length,mesh,order):
    u=np.asarray(position)*mesh/length
    indices=[];weights=[];derivatives=[]
    for value in u:
        j=np.arange(int(np.floor(value))-order//2+1,int(np.floor(value))+order//2+1)
        arg=value-j+order/2
        indices.append(j%mesh);weights.append(cardinal_spline(arg,order))
        derivatives.append(cardinal_spline(arg,order,True)*mesh/length)
    return indices,weights,derivatives


def spme(positions,charges,length=1.,alpha=5.6,images=2,mesh=40,order=6):
    x,q=validate(positions,charges,length)
    if not isinstance(mesh,int) or mesh<2*order:raise ValueError('Mesh must be at least twice spline order')
    density=np.zeros((mesh,)*3);stencils=[]
    for position,charge in zip(x,q):
        ind,w,dw=assignment(position,length,mesh,order);stencils.append((ind,w,dw))
        density[np.ix_(*ind)]+=charge*np.einsum('i,j,k->ijk',*w)
    modes=np.fft.fftfreq(mesh)*mesh;omega=2*pi*modes/mesh
    nodal=np.arange(1,order);bs=cardinal_spline(nodal,order)
    transfer=np.sum(np.exp(-1j*np.outer(omega,nodal))*bs,axis=1)
    correction=1/np.abs(transfer)**2
    k=2*pi*modes/length;k2=k[:,None,None]**2+k[None,:,None]**2+k[None,None,:]**2
    green=np.zeros_like(k2);nonzero=k2>0
    green[nonzero]=np.exp(-k2[nonzero]/(4*alpha**2))/k2[nonzero]
    green*=correction[:,None,None]*correction[None,:,None]*correction[None,None,:]
    qhat=np.fft.fftn(density)
    reciprocal=2*pi/length**3*np.sum(green*np.abs(qhat)**2)
    grid_potential=4*pi/length**3*mesh**3*np.fft.ifftn(green*qhat).real
    real_energy,force=real_space(x,q,length,alpha,images)
    for i,(ind,w,dw) in enumerate(stencils):
        local=grid_potential[np.ix_(*ind)]
        for axis in range(3):
            factors=[dw[j] if j==axis else w[j] for j in range(3)]
            force[i,axis]-=q[i]*np.sum(local*np.einsum('i,j,k->ijk',*factors))
    energy=real_energy+reciprocal-alpha/sqrt(pi)*np.dot(q,q)
    return float(energy),force,float(abs(density.sum()-q.sum()))


def nacl_theta_reference(epsabs=1e-12,terms=20):
    """Independent 1D Jacobi-theta integral for the 3D NaCl Madelung sum.

    M = 2/sqrt(pi) integral_0^infinity (1-theta4(0,exp(-u*u))**3) du.
    Modular theta4/theta2 transformation is used for u<1; no 3D Ewald sums.
    """
    from math import exp
    from scipy.integrate import quad
    if not 0<epsabs<1e-4 or terms<8:raise ValueError('Accurate theta integration requires eps<1e-4 and >=8 terms')
    def theta(u):
        if u==0:return 0.
        if u<1:return sqrt(pi)/u*2*sum(exp(-pi*pi*(n+.5)**2/u**2) for n in range(terms))
        return 1+2*sum((-1)**n*exp(-n*n*u*u) for n in range(1,terms+1))
    f=lambda u:2/sqrt(pi)*(1-theta(u)**3)
    a,ea=quad(f,0,1,epsabs=epsabs/2,epsrel=epsabs)
    b,eb=quad(f,1,9,epsabs=epsabs/2,epsrel=epsabs)
    # Integral from 9 to infinity is exponentially negligible (<1e-35).
    return a+b,ea+eb
