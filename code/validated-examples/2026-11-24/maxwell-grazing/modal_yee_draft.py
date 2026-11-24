"""UNEXECUTED prototype: actual single-ky Yee with local Lorentz midpoint ADE.

Not qualified,not a completed case. E/P/J integer times,H half times. Native
x-staggering retained. K=2sin(ky*dy/2)/dy represents the actual periodic-y
Yee stencil; continuum ky is used only by independent reference formulas.
CPML derivative memories are a proposed coordinate-stretch realization:
its dispersive coupling/stability/energy interpretation require review first.
"""
import numpy as np


def midpoint_electric(e,p,j,curl,epsilon,sigma,oscillator_strength,omega0,gamma,dt):
    a=dt/2;b=1+a*gamma+a*a*omega0**2
    free=np.where(oscillator_strength>0,(j-a*omega0**2*p)/b,0.)
    eb=(epsilon/a*e+curl-free)/(epsilon/a+sigma+a*oscillator_strength/b)
    jb=free+a*oscillator_strength/b*eb
    en=2*eb-e;pn=np.where(oscillator_strength>0,p+dt*jb,0.);jn=np.where(oscillator_strength>0,2*jb-j,0.)
    work_ohmic=dt*sigma*abs(eb)**2
    work_material=dt*np.divide(gamma*abs(jb)**2,oscillator_strength,out=np.zeros_like(oscillator_strength),where=oscillator_strength>0)
    return en,pn,jn,work_ohmic,work_material


def oscillator_energy(p,j,strength,omega0):
    return np.divide(abs(j)**2+omega0**2*abs(p)**2,2*strength,out=np.zeros_like(strength),where=strength>0)


def stretch_coefficients(rate,kappa,alpha,dt):
    if np.any(rate<0) or np.any(kappa<1) or np.any(alpha<0):raise ValueError('Passive stretch coefficients only')
    b=np.exp(-(rate/kappa+alpha)*dt);den=rate*kappa+kappa*kappa*alpha
    c=np.divide(rate*(b-1),den,out=np.zeros_like(rate),where=den>0)
    return b,c


def stretch(raw,previous,coefficients):
    b,c,kappa=coefficients;memory=b*previous+c*raw
    return raw/kappa+memory,memory


def node_derivative(face,h):
    z=np.zeros(len(face)+1,dtype=complex);z[1:-1]=np.diff(face)/h
    return z


def advance_s(state,g):
    e,hx,hy,p,j,psi_h,psi_e=state;dt=g['dt'];K=g['K'];derivative,ph=stretch(np.diff(e)/g['h'],psi_h,g['stretch_face'])
    xp=hx-dt*1j*K*e;yp=hy+dt*derivative
    derivative,pe=stretch(node_derivative(yp,g['h']),psi_e,g['stretch_node']);curl=derivative-1j*K*xp
    en,pn,jn,ohmic,loss=midpoint_electric(e,p,j,curl,g['epsilon_node'],g['sigma_node'],g['strength_node'],g['omega0'],g['gamma'],dt)
    en[[0,-1]]=0.;pn[[0,-1]]=0.;jn[[0,-1]]=0.
    return (en,xp,yp,pn,jn,ph,pe),dict(ohmic_density=ohmic,material_damping_density=loss)


def advance_p(state,g):
    ex,ey,h,px,py,jx,jy,psi_h,psi_e=state;dt=g['dt'];K=g['K'];derivative,ph=stretch(np.diff(ey)/g['h'],psi_h,g['stretch_face']);hp=h+dt*(1j*K*ex-derivative)
    derivative,pe=stretch(node_derivative(hp,g['h']),psi_e,g['stretch_node'])
    exn,pxn,jxn,ox,lx=midpoint_electric(ex,px,jx,1j*K*hp,g['epsilon_face'],g['sigma_face'],g['strength_face'],g['omega0'],g['gamma'],dt)
    eyn,pyn,jyn,oy,ly=midpoint_electric(ey,py,jy,-derivative,g['epsilon_node'],g['sigma_node'],g['strength_node'],g['omega0'],g['gamma'],dt)
    eyn[[0,-1]]=0.;pyn[[0,-1]]=0.;jyn[[0,-1]]=0.
    return (exn,eyn,hp,pxn,pyn,jxn,jyn,ph,pe),dict(ohmic_face=ox,ohmic_node=oy,material_damping_face=lx,material_damping_node=ly)
