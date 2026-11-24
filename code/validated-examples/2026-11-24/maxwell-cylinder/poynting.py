"""Physical-frequency closed-contour power with fourth-order face collocation.

The original two-point-collocated diagnostic is retained in cylinder_draft.
This diagnostic changes no evolved field or source. Four symmetric native
half nodes interpolate H at the integer E contour. The remaining line
integral is the original composite trapezoid, with explicit normal signs.
"""
import numpy as np


def physical_flux(phasors,grid,lower,upper):
    E,Hx,Hy=phasors;h=grid['h'];lo=int(round((lower-grid['x'][0])/h));hi=int(round((upper-grid['x'][0])/h))
    if lo<2 or hi>len(grid['x'])-3 or hi<=lo:raise ValueError('Four-point collocation needs two interior-node margins')
    weights=np.ones(hi-lo+1);weights[[0,-1]]=.5
    def hy_at(i):return (-Hy[i-2,lo:hi+1]+9*Hy[i-1,lo:hi+1]+9*Hy[i,lo:hi+1]-Hy[i+1,lo:hi+1])/16
    def hx_at(j):return (-Hx[lo:hi+1,j-2]+9*Hx[lo:hi+1,j-1]+9*Hx[lo:hi+1,j]-Hx[lo:hi+1,j+1])/16
    left=-.5*np.real(E[lo,lo:hi+1]*np.conj(hy_at(lo)))
    right=-.5*np.real(E[hi,lo:hi+1]*np.conj(hy_at(hi)))
    bottom=.5*np.real(E[lo:hi+1,lo]*np.conj(hx_at(lo)))
    top=.5*np.real(E[lo:hi+1,hi]*np.conj(hx_at(hi)))
    return h*np.sum(weights*(right-left+top-bottom))
