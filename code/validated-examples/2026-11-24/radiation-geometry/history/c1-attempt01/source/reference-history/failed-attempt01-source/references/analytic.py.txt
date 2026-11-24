"""Independent characteristic cell means; no numerical PDE solver imports."""
import numpy as np


def shadow(cells,time,order):
    edge=np.linspace(0,1,cells+1);h=1/cells;a=edge[:-1,None];b=np.minimum(edge[1:,None],time)
    nodes,weights=np.polynomial.legendre.leggauss(order);answer=np.zeros((cells,cells))
    # Include every y location where a circular chord crosses a grid x face.
    inside=edge[abs(edge-.35)<.12]
    cut=np.sqrt(.12**2-(inside-.35)**2)
    special=np.r_[.3,.7,.38,.62,.5-cut,.5+cut]
    for j in range(cells):
        split=np.unique(np.r_[edge[j],special[(special>edge[j])&(special<edge[j+1])],edge[j+1]])
        for lo,hi in zip(split[:-1],split[1:]):
            y=.5*(lo+hi)+.5*(hi-lo)*nodes;w=.5*(hi-lo)*weights
            beam=(y>=.3)&(y<=.7);chord=np.sqrt(np.maximum(.12**2-(y-.5)**2,0.))
            left=.35-chord;right=.35+chord
            before=np.maximum(np.minimum(b,left)-a,0.)
            lower=np.maximum(a,left);upper=np.minimum(b,right)
            middle=np.where(upper>lower,(np.exp(-40*(np.maximum(lower-left,0.)))-np.exp(-40*np.maximum(upper-left,0.)))/40,0.)
            after=np.maximum(b-np.maximum(a,right),0.)*np.exp(-40*(right-left))
            integral=np.where(b>a,before+middle+after,0.)
            answer[:,j]+=np.sum(integral*beam[None,:]*w[None,:],axis=1)/h**2
    return np.stack([answer,answer,np.zeros_like(answer)],axis=-1)


def beams(cells,time,order):
    h=1/cells;x=(np.arange(cells)+.5)*h;nodes,w=np.polynomial.legendre.leggauss(order)
    mean=lambda center: .5*np.sum(w[None,:]*np.exp(16*(np.cos(2*np.pi*(x[:,None]+.5*h*nodes-center))-1)),axis=1)
    ymean=mean(.5);one=mean(.25+time)[:,None]*ymean[None,:];two=mean(.75-time)[:,None]*ymean[None,:]
    return np.stack([one+two,one-two,np.zeros_like(one)],axis=-1)


def mms_state(x,y,time):
    e=1+.1*np.sin(2*np.pi*(x+y-time))
    return np.stack([e,e*(.2+.05*np.sin(2*np.pi*(x-time))),e*(.1+.03*np.cos(2*np.pi*(y+time)))],axis=-1)


def mms_cells(cells,time,order):
    h=1/cells;x=(np.arange(cells)+.5)*h;xx,yy=np.meshgrid(x,x,indexing='ij');nodes,w=np.polynomial.legendre.leggauss(order);out=np.zeros((cells,cells,3))
    for a,wa in zip(nodes,w):
        for b,wb in zip(nodes,w):out+=.25*wa*wb*mms_state(xx+.5*h*a,yy+.5*h*b,time)
    return out


def mms_pressure(state):
    # Algebraically direct tensor form, independent of the production rationalization.
    e=state[...,0];g=state[...,1:]/e[...,None];f2=np.sum(g*g,axis=-1);f=np.sqrt(f2)
    chi=(3+4*f2)/(5+2*np.sqrt(4-3*f2));n=g/f[...,None]
    return e[...,None,None]*((1-chi)[...,None,None]/2*np.eye(2)+(3*chi-1)[...,None,None]/2*n[..., :,None]*n[...,None,:])


def mms_forcing_complex_step(x,y,time):
    h=1e-30
    dx=mms_state(x+1j*h,y,time).imag/h;dy=mms_state(x,y+1j*h,time).imag/h;dt=mms_state(x,y,time+1j*h).imag/h
    px=mms_pressure(mms_state(x+1j*h,y,time)).imag/h;py=mms_pressure(mms_state(x,y+1j*h,time)).imag/h
    return np.stack([dt[...,0]+dx[...,1]+dy[...,2],dt[...,1]+px[...,0,0]+py[...,0,1],dt[...,2]+px[...,0,1]+py[...,1,1]],axis=-1)


def crossed(cells,time,order):
    h=1/cells;x=(np.arange(cells)+.5)*h;nodes,w=np.polynomial.legendre.leggauss(order)
    def integral(center):return .5*np.sum(w[None,:]*np.exp(16*(np.cos(2*np.pi*(x[:,None]+.5*h*nodes-center))-1)),axis=1)
    first=integral(.25+time)[:,None]*integral(.5)[None,:]
    second=integral(.5)[:,None]*integral(.25+time)[None,:]
    return np.stack([first+second,first,second],axis=-1)
