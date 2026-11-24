"""General directional M1 spectral/cone-splitting LF bound; c1.

No state/pressure projection. The exact physical-cone formulas are separate
from the explicit speed-only a1 extension on vacuum/allowed roundoff states.
"""
import numpy as np


def diagnostics():
    return dict(calls=0,vacuum_states=0,tiny_negative_energy_states=0,
                outside_cone_roundoff_states=0,maximum_outside_cone_excess=0.,maximum_speed=0.)


def wave_data(state,axis,record=None):
    if axis not in (0,1):raise ValueError('Coordinate axis0or1 required')
    e=state[...,0];F=state[...,1:]
    if not np.isfinite(state).all() or np.min(e)<-1e-13:raise ArithmeticError('Invalid M1 energy')
    g=np.zeros_like(F);np.divide(F,e[...,None],out=g,where=e[...,None]>0);q=np.sum(g*g,axis=-1)
    if np.max(q)>1+5e-12 or np.any((e<=0)&np.any(F!=0,axis=-1)):raise ArithmeticError('M1 state outside realizability cone')
    physical=(e>0)&(q<=1);speed=np.ones_like(e);cone=np.ones_like(e);eigen=np.ones(e.shape+(3,))
    if np.any(physical):
        qq=q[physical];gg=g[physical];s=np.sqrt(4-3*qq);v=3*gg/(2+s[...,None]);vn=v[...,axis];vt2=v[...,1-axis]**2
        delta=12*(1-qq)/((s+1)*(s+2))
        root=np.sqrt(delta*(3*delta+2*vt2));lam=np.stack([(2*vn-root)/(2+delta),vn,(2*vn+root)/(2+delta)],axis=-1)
        bound=(8*abs(vn)+np.sqrt(delta*(9*delta+8*vt2)))/(8+delta)
        selected=np.maximum(np.maximum(np.max(abs(lam),axis=-1),bound),abs(gg[...,axis]))
        eigen[physical]=lam;cone[physical]=bound;speed[physical]=selected
    if not np.isfinite(speed).all() or np.max(speed)>1+5e-12:raise ArithmeticError('Noncausal directional LF speed')
    if record is not None:
        record['calls']+=1;record['vacuum_states']+=int(np.count_nonzero(e==0));record['tiny_negative_energy_states']+=int(np.count_nonzero(e<0));record['outside_cone_roundoff_states']+=int(np.count_nonzero(q>1))
        record['maximum_outside_cone_excess']=max(record['maximum_outside_cone_excess'],float(np.max(q-1)))
        record['maximum_speed']=max(record['maximum_speed'],float(np.max(speed)))
    return dict(speed=speed,cone_bound=cone,eigenvalues=eigen,reduced_flux=g,squared_reduced_flux=q,physical_cone_mask=physical)


def directional_speed(state,axis,record=None):return wave_data(state,axis,record)['speed']
