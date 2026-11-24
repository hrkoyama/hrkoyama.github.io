"""UNEXECUTED independent continuum formulas; not a qualified oracle/cache.

Convention exp(i*k*x-i*omega*t),c=epsilon0=mu0=1. Cylinder is infinite in z,
2D ordinary Bessel/Hankel functions,not3D spherical Mie. Original derivation
from E/normal derivative continuity; DLMF Wronskian must qualify signs first.
"""
import numpy as np
from scipy.special import jv,jvp,hankel1,h1vp


def outgoing_root(z):
    q=np.sqrt(np.asarray(z,dtype=complex))
    return np.where((q.imag<0)|((q.imag==0)&(q.real<0)),-q,q)


def lorentz_epsilon(omega,material):
    w=np.asarray(omega,dtype=float)
    if np.any(w<=0):raise ValueError('Positive frequencies only')
    c=material
    if not all(np.isfinite(c[k]) for k in ['epsilon_inf','delta_epsilon','omega0','gamma','sigma']) or min(c['epsilon_inf'],c['omega0'])<=0 or min(c['delta_epsilon'],c['gamma'],c['sigma'])<0:raise ValueError('Finite passive Lorentz material required')
    f=c['delta_epsilon']*c['omega0']**2;den=c['omega0']**2-w*w-1j*c['gamma']*w
    if f and np.any(den==0):raise ValueError('Undamped real pole has no finite frequency reference')
    susceptibility=f/den if f else np.zeros_like(w,dtype=complex)
    return c['epsilon_inf']+susceptibility+1j*c['sigma']/w


def slab(omega,ky,material,width,polarization):
    """s:E_z amplitude;p:H_z amplitude;outer vacuum on both sides."""
    if not np.isfinite(width) or width<0:raise ValueError('Nonnegative finite width required')
    w=np.asarray(omega,dtype=float);eps=lorentz_epsilon(w,material);q0=outgoing_root(w*w-ky*ky);q=outgoing_root(eps*w*w-ky*ky)
    if polarization not in ['s','p'] or np.any(q0.imag!=0) or np.any(q0.real<=0):raise ValueError('Resolved propagating vacuum incidence required')
    y0=q0;y=q if polarization=='s' else q/eps
    rho=(y0-y)/(y0+y);z=np.exp(2j*q*width);den=1-rho*rho*z
    r=rho*(1-z)/den;t=(1-rho*rho)*np.exp(1j*q*width)/den;a=(1+rho)/den;b=-rho*a*z
    return dict(omega=w,epsilon=eps,q0=q0,q=q,r=r,t=t,a=a,b=b,R=abs(r)**2,T=abs(t)**2)


def internal_electric(x,coefficients,ky,polarization):
    z=coefficients;w=z['omega'];q=z['q'];eps=z['epsilon'];x=np.asarray(x)
    forward=z['a'][:,None]*np.exp(1j*q[:,None]*x);back=z['b'][:,None]*np.exp(-1j*q[:,None]*x)
    if polarization=='s':return (forward+back,)
    return (-ky/(eps*w))[:,None]*(forward+back),(q/(eps*w))[:,None]*(forward-back)


def direct_absorptance(omega,ky,material,width,polarization,panels=4):
    """Volume Ohmic+oscillator work;not defined by1-R-T."""
    z=slab(omega,ky,material,width,polarization);nodes,weights=np.polynomial.legendre.leggauss(16)
    x=np.concatenate([(j+.5*(nodes+1))*width/panels for j in range(panels)]);weights=np.tile(weights*width/(2*panels),panels)
    components=internal_electric(x,z,ky,polarization);norm=sum(abs(e)**2 for e in components);w=z['omega'];f=material['delta_epsilon']*material['omega0']**2
    loss=material['sigma']+material['gamma']*w*w*f/abs(material['omega0']**2-w*w-1j*material['gamma']*w)**2
    return loss*np.sum(norm*weights,axis=1)/(z['q0'].real/w)


def cylinder_coefficients(k0,radius,epsilon,maximum_order,polarization='s'):
    if k0<=0 or radius<=0 or epsilon<=0 or maximum_order<0:raise ValueError('Positive lossless dielectric data required')
    if polarization not in ['s','p']:raise ValueError('s:E_z;p:H_z')
    n=np.arange(-maximum_order,maximum_order+1);x=k0*radius;m=np.sqrt(epsilon);beta=m if polarization=='s' else 1/m
    J=jv(n,x);Jm=jv(n,m*x);Jp=jvp(n,x);Jmp=jvp(n,m*x);H=hankel1(n,x);Hp=h1vp(n,x)
    a=(beta*Jmp*J-Jm*Jp)/(Jm*Hp-beta*Jmp*H)
    return n,a


def cylinder_scattering_width(k0,radius,epsilon,maximum_order=24):
    n,a=cylinder_coefficients(k0,radius,epsilon,maximum_order)
    return dict(scattering=4/k0*np.sum(abs(a)**2),extinction=-4/k0*np.sum(a.real),orders=n,coefficients=a)


def cylinder_exterior_field(x,y,k0,radius,epsilon,maximum_order=24):
    x,y=np.broadcast_arrays(x,y);r=np.hypot(x,y);theta=np.arctan2(y,x)
    if np.any(r<radius):raise ValueError('Exterior series only')
    n,a=cylinder_coefficients(k0,radius,epsilon,maximum_order)
    return np.sum((1j**n*a)*hankel1(n,k0*r[...,None])*np.exp(1j*theta[...,None]*n),axis=-1)
