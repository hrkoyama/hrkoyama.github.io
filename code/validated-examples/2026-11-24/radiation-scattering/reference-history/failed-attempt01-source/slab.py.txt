"""Signed-angle conservative upwind FV for an isotropically scattering slab.

The scalar source is eliminated exactly from the discrete sweeps; this is NOT
the continuum Fredholm/product-integration reference used for validation.
Angular weights integrate each hemisphere separately, so incoming flux is pi
for unit radiance and the normalized discrete budget is exactly R+T+A=1.
"""
import numpy as np
from scipy.linalg import solve
from scipy.signal import lfilter


def directions(number):
    if number<2 or number%2:raise ValueError('Even signed ordinate count required')
    x,w=np.polynomial.legendre.leggauss(number//2)
    positive=.5*(x+1);weights=.5*w
    return np.r_[-positive[::-1],positive],np.r_[weights[::-1],weights]


def solve_slab(depth,albedo,cells,ordinates):
    if not 0<=albedo<=1 or depth<=0 or cells<2:raise ValueError('Physical slab controls required')
    mu,w=directions(ordinates);h=depth/cells;x=(np.arange(cells)+.5)*h
    distance=np.arange(cells)[:,None]-np.arange(cells)[None,:]
    response=np.zeros((cells,cells));incident=np.zeros(cells)
    for speed,weight in zip(mu,w):
        r=abs(speed)/(h+abs(speed));b=h/(h+abs(speed))
        offsets=distance if speed>0 else -distance
        response+=.5*weight*b*np.where(offsets>=0,r**np.maximum(offsets,0),0.)
        if speed>0:incident+=.5*weight*r**(np.arange(cells)+1)
    scalar=solve(np.eye(cells)-albedo*response,incident,assume_a='gen',check_finite=True)
    intensity=np.empty((ordinates,cells))
    for j,speed in enumerate(mu):
        r=abs(speed)/(h+abs(speed));b=h/(h+abs(speed))
        source=albedo*b*scalar
        if speed>0:intensity[j]=lfilter([1.],[1.,-r],source,zi=[r])[0]
        else:intensity[j]=lfilter([1.],[1.,-r],source[::-1],zi=[0.])[0][::-1]
    measured=.5*np.sum(w[:,None]*intensity,axis=0)
    residual=0.
    for j,speed in enumerate(mu):
        upstream=np.r_[1.,intensity[j,:-1]] if speed>0 else np.r_[intensity[j,1:],0.]
        residual=max(residual,float(np.max(abs(abs(speed)*(intensity[j]-upstream)/h+intensity[j]-albedo*measured))))
    left=mu<0;right=mu>0
    reflected=2*np.sum(w[left]*abs(mu[left])*intensity[left,0])
    transmitted=2*np.sum(w[right]*mu[right]*intensity[right,-1])
    absorbed=4*(1-albedo)*h*np.sum(measured)
    return dict(x=x,mu=mu,weights=w,intensity=intensity,scalar=measured,
                R=np.array(reflected),T=np.array(transmitted),A=np.array(absorbed),
                balance=np.array(abs(1-reflected-transmitted-absorbed)),
                residual=np.array(residual),source_residual=np.array(np.max(abs(measured-scalar))))
