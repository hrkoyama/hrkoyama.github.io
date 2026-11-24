"""Small forward directional AD: no identity seeds or dense Jacobian builder."""
from dataclasses import dataclass
import numpy as np


@dataclass
class Dual:
    value: np.ndarray
    tangent: np.ndarray
    __array_priority__ = 1000

    def __post_init__(self):
        self.value=np.asarray(self.value,dtype=float)
        self.tangent=np.asarray(self.tangent,dtype=float)
        if self.value.shape!=self.tangent.shape:raise ValueError('Dual shapes differ')

    @staticmethod
    def coerce(x):
        return x if isinstance(x,Dual) else Dual(np.asarray(x,dtype=float),np.zeros_like(x,dtype=float))

    def __getitem__(self,key):return Dual(self.value[key],self.tangent[key])
    def __add__(self,x):
        x=self.coerce(x);return Dual(self.value+x.value,self.tangent+x.tangent)
    __radd__=__add__
    def __neg__(self):return Dual(-self.value,-self.tangent)
    def __sub__(self,x):return self+(-self.coerce(x))
    def __rsub__(self,x):return self.coerce(x)+(-self)
    def __mul__(self,x):
        x=self.coerce(x);return Dual(self.value*x.value,self.tangent*x.value+self.value*x.tangent)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x);return Dual(self.value/x.value,(self.tangent*x.value-self.value*x.tangent)/x.value**2)
    def __array_ufunc__(self,ufunc,method,*args,**kwargs):
        if method!='__call__' or kwargs:return NotImplemented
        if ufunc is np.exp:
            value=np.exp(self.value);return Dual(value,value*self.tangent)
        if ufunc is np.negative:return -self
        ops={np.add:'__add__',np.subtract:'__sub__',np.multiply:'__mul__',np.divide:'__truediv__'}
        if ufunc in ops:return getattr(self.coerce(args[0]),ops[ufunc])(args[1])
        return NotImplemented


def pad_zero(x):
    if isinstance(x,Dual):return Dual(np.r_[0.,x.value,0.],np.r_[0.,x.tangent,0.])
    return np.r_[0.,x,0.]
