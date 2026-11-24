"""UNEXECUTED genuine2D scattered-field Yee prototype for E_z cylinder.

Localized polarization-contrast forcing removes the analytic incident field.
It is not a total-field proxy/FDFD/Born approximation. Full scattered field
acts back through epsilon. Vacuum four-side split PML does not overlap the
cylinder; no claim yet about long-time/window/curved-grid convergence.
"""
import numpy as np


def build_grid(cells,length,dt,radius,epsilon,layer,strength,order=3):
    h=length/cells
    if dt*np.sqrt(2)/h>=1 or epsilon<1:raise ValueError('Strict vacuum CFL and dielectricepsilon>=1 required')
    if not 0<radius<length/2-layer:raise ValueError('Cylinder must not overlapPML')
    x=np.arange(cells+1)*h-length/2;xh=(np.arange(cells)+.5)*h-length/2
    def damping(z):return strength*(np.maximum(abs(z)-(length/2-layer),0)/layer)**order
    X,Y=np.meshgrid(x,x,indexing='ij');eps=1+(epsilon-1)*((X*X+Y*Y)<radius*radius)
    return dict(h=h,dt=dt,x=x,xh=xh,epsilon=eps,gx=damping(x)[:,None],gy=damping(x)[None,:],gxh=damping(xh)[:,None],gyh=damping(xh)[None,:])


def incident(x,time,omega,dt,h,amplitude=1.):
    argument=h*np.sin(omega*dt/2)/dt
    if abs(argument)>=1:raise ValueError('Incident discrete vacuum branch unresolved')
    k=2/h*np.arcsin(argument)
    return amplitude*np.exp(1j*(k*x-omega*time))


def zero_state(g):
    n=len(g['x'])-1
    return tuple(np.zeros(shape,dtype=complex) for shape in [(n+1,n+1),(n+1,n+1),(n+1,n),(n,n+1)])


def advance(state,g,time,omega,amplitude=1.):
    ex,ey,hx,hy=state;e=ex+ey;dt=g['dt'];h=g['h'];eps=g['epsilon'];ax=.5*dt*g['gyh'];ay=.5*dt*g['gxh']
    xp=((1-ax)*hx-dt*np.diff(e,axis=1)/h)/(1+ax);yp=((1-ay)*hy+dt*np.diff(e,axis=0)/h)/(1+ay)
    xn=np.zeros_like(ex);yn=np.zeros_like(ey);ax=.5*dt*g['gx'][1:-1];ay=.5*dt*g['gy'][:,1:-1]
    # The contrast support lies wholly outsidePML;its source uses an exact
    # difference of the discrete incident mode,not a continuum derivative.
    inc_change=(incident(g['x'],time+dt,omega,dt,h,amplitude)-incident(g['x'],time,omega,dt,h,amplitude))[:,None]
    xn[1:-1,1:-1]=((1-ax)*ex[1:-1,1:-1]+dt*np.diff(yp,axis=0)[:,1:-1]/(h*eps[1:-1,1:-1])-(eps[1:-1,1:-1]-1)/eps[1:-1,1:-1]*inc_change[1:-1])/(1+ax)
    yn[1:-1,1:-1]=((1-ay)*ey[1:-1,1:-1]-dt*np.diff(xp,axis=1)[1:-1,:]/(h*eps[1:-1,1:-1]))/(1+ay)
    return xn,yn,xp,yp


def scattered_flux(phasors,g,lower,upper):
    """Time-average outward2D flux from same-frequency component phasors.

    Caller must accumulate E(integer time) and H(half time) with their OWN
    exp(+i omega time). No implicit amplitude2 or phase/time collocation.
    """
    e,hx,hy=phasors;h=g['h'];lo=int(round((lower-g['x'][0])/h));hi=int(round((upper-g['x'][0])/h));w=np.ones(hi-lo+1);w[[0,-1]]=.5
    if lo<1 or hi>=len(g['x'])-1:raise ValueError('Interior closed contour required')
    left=-.5*np.real(e[lo,lo:hi+1]*np.conj(.5*(hy[lo-1,lo:hi+1]+hy[lo,lo:hi+1])))
    right=-.5*np.real(e[hi,lo:hi+1]*np.conj(.5*(hy[hi-1,lo:hi+1]+hy[hi,lo:hi+1])))
    bottom=.5*np.real(e[lo:hi+1,lo]*np.conj(.5*(hx[lo:hi+1,lo-1]+hx[lo:hi+1,lo])))
    top=.5*np.real(e[lo:hi+1,hi]*np.conj(.5*(hx[lo:hi+1,hi-1]+hx[lo:hi+1,hi])))
    return h*np.sum(w*(right-left+top-bottom))
