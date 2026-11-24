"""Closed-form continuum fields; no solver or kinetic populations are imported."""
import numpy as np

def tgv(x,y,t,U=.2,nu=.1):
    a=U*np.exp(-2*nu*t)
    return dict(u=a*np.sin(x)*np.cos(y),v=-a*np.cos(x)*np.sin(y),
                p=.25*a*a*(np.cos(2*x)+np.cos(2*y)),energy=.25*a*a)

def annulus(x,y,Ui=.02,Ri=.2,Ro=.4,center=(.5,.5),nu=.01):
    x=np.asarray(x)-center[0];y=np.asarray(y)-center[1];r2=x*x+y*y
    A=-Ui*Ri/(Ro*Ro-Ri*Ri);B=Ui*Ri*Ro*Ro/(Ro*Ro-Ri*Ri)
    angular=A+B/r2
    p=.5*A*A*r2+A*B*np.log(r2)-.5*B*B/r2
    return dict(u=-angular*y,v=angular*x,p=p,A=A,B=B,torque=-4*np.pi*nu*B)

def qualify_tgv():
    # Independent Fourier differentiation of sampled analytic fields. Reference
    # qualification of continuous NS, not of the LBM's discrete kinetic equation.
    n=16;x=2*np.pi*(np.arange(n)+.5)/n;xx,yy=np.meshgrid(x,x)
    t=.37;nu=.1;field=tgv(xx,yy,t,.2,nu);u,v,p=[field[k] for k in ['u','v','p']]
    k=np.fft.fftfreq(n,d=1/n)
    def derivative(a,axis):
        multiplier=1j*(k[:,None] if axis==0 else k[None,:])
        return np.fft.ifft2(np.fft.fft2(a)*multiplier).real
    def lap(a):return np.fft.ifft2(-(k[:,None]**2+k[None,:]**2)*np.fft.fft2(a)).real
    ux,uy=derivative(u,1),derivative(u,0);vx,vy=derivative(v,1),derivative(v,0)
    rx=-2*nu*u+u*ux+v*uy+derivative(p,1)-nu*lap(u)
    ry=-2*nu*v+u*vx+v*vy+derivative(p,0)-nu*lap(v)
    return {'Fourier divergence':float(np.max(abs(ux+vy))),
            'Fourier NS x':float(np.max(abs(rx))),'Fourier NS y':float(np.max(abs(ry))),
            'mean pressure gauge':abs(float(np.mean(p))),
            'analytic mean energy':abs(float(np.mean((u*u+v*v)/2))-field['energy'])}

def qualify_annulus():
    r=np.array([.201,.237,.319,.399]);phi=np.array([.13,.77,1.59,4.21])
    x=.5+r*np.cos(phi);y=.5+r*np.sin(phi);a=annulus(x,y)
    A,B=a['A'],a['B'];v=A*r+B/r;dv=A-B/r**2;ddv=2*B/r**3
    pressure_derivative=A*A*r+2*A*B/r+B*B/r**3
    h=1e-25;ux=annulus(x+1j*h,y)['u'].imag/h;uy=annulus(x,y+1j*h)['u'].imag/h
    vx=annulus(x+1j*h,y)['v'].imag/h;vy=annulus(x,y+1j*h)['v'].imag/h
    px=annulus(x+1j*h,y)['p'].imag/h;py=annulus(x,y+1j*h)['p'].imag/h
    return {'radial viscous equation':float(np.max(abs(ddv+dv/r-v/r**2))),
            'radial pressure equation':float(np.max(abs(pressure_derivative-v*v/r))),
            'Cartesian divergence':float(np.max(abs(ux+vy))),
            'Cartesian x momentum':float(np.max(abs(a['u']*ux+a['v']*uy+px))),
            'Cartesian y momentum':float(np.max(abs(a['u']*vx+a['v']*vy+py))),
            'inner wall speed':abs(A*.2+B/.2-.02),'outer wall speed':abs(A*.4+B/.4)}
