"""New trapezoidal derivative-memory realization; old endpoint filter retained.

E/P/J integer, H half times. psi_h is evaluated at integer E times and psi_e
at half H times. Each filter uses its own preceding derivative. It is not
the already-qualified endpoint-held recurrence and needs new qualification.
"""
import numpy as np
import modal_yee_draft as core


def coefficients(rate,dt):
    a=.5*dt*np.asarray(rate)
    if np.any(a<0):raise ValueError('Nonnegative stretch rate required')
    return (1-a)/(1+a),-a/(1+a)


def filter_step(raw,old_raw,old_memory,coefficient):
    b,c=coefficient
    memory=b*old_memory+c*(raw+old_raw)
    return raw+memory,memory


def rates(x,length,layer,peak,order):
    return peak*(np.maximum(np.maximum(layer-x,x-(length-layer)),0)/layer)**order


def build(cells,length,dy,ky,courant,material,layer,peak,order,final_time):
    h=length/cells;maximum=courant/np.sqrt(1/h**2+(0. if ky==0 else 1/dy**2))
    steps=int(np.ceil(final_time/maximum/4))*4;dt=final_time/steps
    x=np.arange(cells+1)*h;xf=(np.arange(cells)+.5)*h
    m=material;ep=np.full(cells+1,m['epsilon_inf']);sigma=np.full(cells+1,m['sigma'])
    return dict(h=h,dt=dt,steps=steps,x=x,xf=xf,K=0. if ky==0 else 2*np.sin(ky*dy/2)/dy,
                epsilon_node=ep,sigma_node=sigma,strength_node=np.full(cells+1,m['delta_epsilon']*m['omega0']**2),
                omega0=m['omega0'],gamma=m['gamma'],
                filter_face=coefficients(rates(xf,length,layer,peak,order),dt),
                filter_node=coefficients(rates(x,length,layer,peak,order),dt),
                rate_node=rates(x,length,layer,peak,order),rate_face=rates(xf,length,layer,peak,order))


def initialize(reference,g):
    E,Hx,Hy,P,J=[reference[n][0].copy() for n in ['E','Hx','Hy','P','J']]
    E[[0,-1]]=0.;P[[0,-1]]=0.;J[[0,-1]]=0.
    raw_h=np.diff(E)/g['h'];raw_e=core.node_derivative(Hy,g['h'])
    return E,Hx,Hy,P,J,np.zeros_like(Hy),np.zeros_like(E),raw_h.copy(),raw_e.copy()


def magnetic(state,g):
    E,Hx,Hy,P,J,psi_h,psi_e,old_h,old_e=state
    derivative,new_h=filter_step(np.diff(E)/g['h'],old_h,psi_h,g['filter_face'])
    return Hx-1j*g['dt']*g['K']*E,Hy+g['dt']*derivative,new_h


def advance(state,g):
    E,Hx,Hy,P,J,psi_h,psi_e,old_h,old_e=state
    hp_x,hp_y,new_h=magnetic(state,g)
    raw_e=core.node_derivative(hp_y,g['h']);derivative,new_e=filter_step(raw_e,old_e,psi_e,g['filter_node'])
    curl=derivative-1j*g['K']*hp_x
    En,Pn,Jn,ohmic,loss=core.midpoint_electric(E,P,J,curl,g['epsilon_node'],g['sigma_node'],g['strength_node'],g['omega0'],g['gamma'],g['dt'])
    En[[0,-1]]=0.;Pn[[0,-1]]=0.;Jn[[0,-1]]=0.
    new=(En,hp_x,hp_y,Pn,Jn,new_h,new_e,np.diff(E)/g['h'],raw_e)
    return new,dict(ohmic=ohmic,material_loss=loss,psi_e=new_e,psi_h=new_h)


def integral(node,face,g):
    weight=np.ones(len(g['x']));weight[[0,-1]]=.5
    return g['h']*(np.sum(weight*node)+np.sum(face))


def modified_energy(state,g):
    E,Hx,Hy,P,J=state[:5];xp,yp,_=magnetic(state,g)
    node=.5*g['epsilon_node']*abs(E)**2+core.oscillator_energy(P,J,g['strength_node'],g['omega0'])+.5*np.real(Hx*np.conj(xp))
    face=.5*np.real(Hy*np.conj(yp))
    return float(integral(node,face,g))


def work(old,new,diagnostic,g):
    eb=.5*(old[0]+new[0]);_,_,next_h=magnetic(new,g)
    physical=float(integral(diagnostic['ohmic']+diagnostic['material_loss'],np.zeros(len(g['xf'])),g))
    pml=float(g['dt']*np.real(integral(np.conj(eb)*diagnostic['psi_e'],
                          .5*np.conj(new[2])*(diagnostic['psi_h']+next_h),g)))
    return physical,pml
