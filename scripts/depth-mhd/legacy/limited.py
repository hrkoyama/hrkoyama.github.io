import numpy as np

def limited(a,b,kind='mc'):
    if kind not in ('mc','minmod','first'): raise ValueError('Unknown limiter')
    if kind=='first': return np.zeros_like(a)
    same=a*b>0
    magnitude=np.minimum(abs(a),abs(b)) if kind=='minmod' else np.minimum(.5*abs(a+b),2*np.minimum(abs(a),abs(b)))
    return np.where(same,np.sign(a)*magnitude,0.)
