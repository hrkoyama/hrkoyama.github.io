"""Authored residuals and index-reduced fields; no projection or normalization."""
import numpy as np


def index1_residual(x,old,t,h):
    y,z=x
    return np.array([(y-old[0])/h+y-z+np.exp(-2*t/3),z**3-y**2])


def index1_jacobian(x,h):
    y,z=x
    return np.array([[1/h+1,-1.],[-2*y,3*z*z]])


def robertson_rhs(y):
    a=.04*y[0]-1e4*y[1]*y[2];b=3e7*y[1]*y[1]
    return np.array([-a,a-b,b])


def robertson_jacobian(y):
    return np.array([[-.04,1e4*y[2],1e4*y[1]],[.04,-1e4*y[2]-6e7*y[1],-1e4*y[1]],[0.,6e7*y[1],0.]])


def robertson_residual(y,old,h,formulation):
    value=y-old-h*robertson_rhs(y)
    if formulation=='residual_dae':value[2]=np.sum(y)-1
    elif formulation!='full_ode':raise ValueError('Unknown formulation')
    return value


def robertson_step_jacobian(y,h,formulation):
    value=np.eye(3)-h*robertson_jacobian(y)
    if formulation=='residual_dae':value[2]=1
    return value


def robertson_nodes(cfg,factor):
    pieces=[]
    for a,b,n in zip(cfg['window_boundaries'][:-1],cfg['window_boundaries'][1:],cfg['base_steps_per_window']):
        values=np.linspace(a,b,n*factor+1)
        pieces.extend(values if not pieces else values[1:])
    return np.array(pieces)


def consistent_pendulum(theta=.7):
    return np.array([np.sin(theta),-np.cos(theta),0.,0.,0.])


def pendulum_invariants(state):
    q=state[...,:2];v=state[...,2:4]
    radius=np.sum(q*q,axis=-1)
    return (radius-1)/2,np.sum(q*v,axis=-1),.5*np.sum(v*v,axis=-1)+q[...,1],radius


def pendulum_rhs(state,stabilized=False):
    q=state[:2];v=state[2:4];r2=float(np.sum(q*q))
    if not np.isfinite(r2) or r2<=0:raise ArithmeticError('Nonpositive radius squared')
    d=float(np.sum(q*v));c=(r2-1)/2
    lam=(float(np.sum(v*v))-q[1]+(2*d+c if stabilized else 0))/r2
    acceleration=-lam*q+np.array([0.,-1.])
    return np.array([v[0],v[1],acceleration[0],acceleration[1],-lam*d])


def rk4_path(initial,T,steps,stabilized=False,progress=None):
    h=T/steps;state=np.array(initial,copy=True);history=np.empty((steps+1,5));history[0]=state
    for k in range(steps):
        if progress:progress(step=k,stage=1,candidate=state,completed=history[:k+1])
        k1=pendulum_rhs(state,stabilized)
        if progress:progress(step=k,stage=1,candidate=state,rhs=k1,completed=history[:k+1])
        a=state+h*k1/2
        if progress:progress(step=k,stage=2,candidate=a,completed=history[:k+1])
        k2=pendulum_rhs(a,stabilized)
        if progress:progress(step=k,stage=2,candidate=a,rhs=k2,completed=history[:k+1])
        b=state+h*k2/2
        if progress:progress(step=k,stage=3,candidate=b,completed=history[:k+1])
        k3=pendulum_rhs(b,stabilized)
        if progress:progress(step=k,stage=3,candidate=b,rhs=k3,completed=history[:k+1])
        c=state+h*k3
        if progress:progress(step=k,stage=4,candidate=c,completed=history[:k+1])
        k4=pendulum_rhs(c,stabilized)
        if progress:progress(step=k,stage=4,candidate=c,rhs=k4,completed=history[:k+1])
        state=state+h*(k1+2*k2+2*k3+k4)/6
        if progress:progress(step=k,stage=5,candidate=state,completed=history[:k+1],phase="updated_candidate")
        if not np.isfinite(state).all():raise FloatingPointError('Nonfinite RK4 candidate')
        history[k+1]=state
    return history
