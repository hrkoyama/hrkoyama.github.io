"""Strict classical status, one-sided directional values and trace AD are separate."""
import numpy as np
from tape import build


def piece(kind,value,direction):
    v=float(value);d=float(direction);at_kink=(v==0 if kind!='clip'else abs(v)==1)
    def function(x):
        if kind=='abs':return x if v>=0 else-x
        if kind=='relu':return x if v>=0 else x.tape.constant(0.)
        if kind=='clip':return x.tape.constant(-1.)if v<=-1 else x.tape.constant(1.)if v>=1 else x
        if kind=='branch':return x*x if v>=0 else 2*x
        raise ValueError(kind)
    tape,node,out=build(function,np.array(v),np.array(d))
    gradient,_=tape.reverse(out,np.array(1.))
    if at_kink:
        if kind=='abs':directional=abs(d)
        elif kind=='relu':directional=max(d,0.)
        elif kind=='clip':directional=max(d,0.)if v==-1 else min(d,0.)
        else:directional=0. if d>=0 else 2*d
        slope=None
    else:directional=float(gradient)*d;slope=float(gradient)
    return {'kind':kind,'x':v,'direction':d,'value':float(out.value),
            'status':'NONDIFFERENTIABLE'if at_kink else'SMOOTH','classical_slope':slope,
            'one_sided_directional':directional,
            'executed_branch_trace_slope':float(gradient)if kind=='branch'else None,
            'work':tape.inventory()}


def max_tie(direction):
    da,db=direction
    return {'kind':'max-tie','x':0.,'status':'NONDIFFERENTIABLE','value':0.,
            'classical_slope':None,'direction':list(direction),'one_sided_directional':max(da,db)}


def stopped(theta):
    tape,node,_=build(lambda x:x,np.array(theta));x=tape.constant(0.);history=[];status='MAXITER'
    for k in range(6):
        residual=abs(float(x.value-node.value));history.append({'k':k,'x':float(x.value),'residual':residual})
        if residual<=1/8:status='STOP_TOL';break
        if k==5:break
        x=.5*(x+node)
    slope,_=tape.reverse(x,np.array(1.))
    return {'kind':'stopped','theta':theta,'K':k,'value':float(x.value),'status':status,
            'classical_slope':None if theta in [.25,.5,1.] else float(slope),
            'frozen_trace_slope':float(slope),'converged_root_derivative':1.,'history':history,'work':tape.inventory()}


def inactive_log():
    calls=[]
    def log(x):calls.append(1);raise ValueError('This negative input must not evaluate log')
    tape,node,out=build(lambda x:log(x)if float(x.value)>0 else x*x,np.array(-1.))
    g,_=tape.reverse(out,np.array(1.))
    return {'kind':'inactive-log','x':-1.,'value':float(out.value),'classical_slope':float(g),
            'status':'SMOOTH_EXECUTED_BRANCH','invalid_log_calls':len(calls),'work':tape.inventory()}
