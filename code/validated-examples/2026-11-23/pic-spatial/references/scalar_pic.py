"""Independently authored scalar CIC + explicit dense DFT electrostatic PIC.

No primary/FFT deposition/gather routine is imported. All particles source a
fresh field in this implementation at every Verlet kick. Same time algorithm
and mathematical spatial convention are intentional; independence is coding
of the spatial pipeline, not a different continuum model or time integrator.
"""
import cmath,math
import numpy as np


def field(positions,n,length,weights=None,wrong_sign=False):
    xp=list(map(float,positions));wp=[length/len(xp)]*len(xp) if weights is None else list(map(float,weights));density=[0.]*n;shape=[]
    if n<4 or len(xp)<2 or len(wp)!=len(xp) or min(wp)<=0:raise ValueError('Invalid independent scalar input')
    for x,w in zip(xp,wp):
        z=(x%length)/(length/n);j=math.floor(z);r=z-j;j%=n;shape.append((j,r));density[j]+=w*(1-r)/(length/n);density[(j+1)%n]+=w*r/(length/n)
    charge=[1-q for q in density]
    transformed=[sum(charge[j]*cmath.exp(-2j*math.pi*m*j/n) for j in range(n)) for m in range(n)]
    efourier=[]
    for m,rho in enumerate(transformed):
        signed=m if m<=(n-1)//2 else m-n
        if m==0 or (n%2==0 and m==n//2):efourier.append(0j)
        else:efourier.append(rho/(1j*(2*math.pi*signed/length)))
    electric=[(sum(efourier[m]*cmath.exp(2j*math.pi*m*j/n) for m in range(n))/n).real for j in range(n)]
    acceleration=[(1. if wrong_sign else -1.)*((1-r)*electric[j]+r*electric[(j+1)%n]) for j,r in shape]
    return np.array(acceleration),np.array(electric),np.array(charge)


def advance(x_initial,v_initial,n,length,dt,steps,weights=None):
    positions=list(map(float,x_initial));velocity=list(map(float,v_initial));a,e,rho=field(positions,n,length,weights);xh=[];vh=[];eh=[];rh=[]
    for iteration in range(steps+1):
        xh.append(positions.copy());vh.append(velocity.copy());eh.append(e.copy());rh.append(rho.copy())
        if iteration==steps:break
        for i in range(len(positions)):
            velocity[i]=velocity[i]+dt*a[i]/2
            positions[i]=positions[i]+dt*velocity[i]
        a,e,rho=field(positions,n,length,weights)
        for i in range(len(positions)):velocity[i]=velocity[i]+dt*a[i]/2
    return dict(x=np.array(xh),v=np.array(vh),electric=np.array(eh),charge=np.array(rh),times=np.arange(steps+1)*dt)
