"""Finite-window vacuum geometric sums; no primary time-step imports/calls."""
import numpy as np


def vacuum_monitors(spec,h,dy,dt,steps,polarization,coordinates):
    length=spec['domain'][1]-spec['domain'][0];n=int(round(length/h))
    q=2*np.pi*np.fft.fftfreq(n,d=h);center=np.sqrt(spec['carrier']**2-spec['ky']**2)
    selected=abs(q-center)<=9/spec['width'];q=q[selected]
    coefficients=np.sqrt(2*np.pi)*spec['width']/length*np.exp(-.5*((q-center)*spec['width'])**2)
    Q=2*np.sin(.5*q*h)/h;K=2*np.sin(.5*spec['ky']*dy)/dy
    omega=2*np.arcsin(.5*dt*np.sqrt(Q*Q+K*K))/dt
    frequencies=np.array(spec['frequencies']);theta=(frequencies[:,None]-omega[None,:])*dt
    series=steps*np.exp(.5j*(steps+1)*theta)*np.sinc(steps*theta/(2*np.pi))/np.sinc(theta/(2*np.pi))
    if polarization=='p':series*=np.exp(-.5j*theta)
    return np.array([dt*np.sum(series*coefficients[None,:]*np.exp(1j*q[None,:]*(x-spec['center'])),axis=1) for x in coordinates])


def discrete_q(omega,h,dt,K):
    O=2*np.sin(.5*np.asarray(omega)*dt)/dt
    return 2*np.arcsin(.5*h*np.sqrt(O*O-K*K))/h
