"""Fixed smooth functions; all transcendental grid coefficients are constants."""
import numpy as np
from tape import Node

Q=np.array([[4,1,.5,0],[1,3,-.25,.5],[.5,-.25,2,.25],[0,.5,.25,1.5]])
C=np.array([.5,-.25,.125,-.75])


def rectangular(x):
    a,b,c,d=(x[i]for i in range(4));r=x[[0,0,2]]+d
    return [(r*r).sum()+a*b,b.exp()+a*c+d*d,(a+b)*(c-d)+r.sum()/2]


def wide(x):
    n=x.value.size
    return [(x*x).sum()/n,x.exp().sum()/n,x[0]*x[-1]+x.sum()/n]


def bratu(x):
    n=x.value.size;p=x.pad()
    return (2*p[1:-1]-p[:-2]-p[2:])*(n+1)**2-2*x.exp()


def quadratic(x):
    total=x.tape.constant(0.)
    for i in range(4):
        total=total+float(C[i])*x[i]
        for j in range(4):total=total+.5*float(Q[i,j])*x[i]*x[j]
    return total


def energy(x):
    n=x.value.size;p=x.pad();a=(2*p[1:-1]-p[:-2]-p[2:])*(n+1)**2
    return (.5*(x*a).sum()-2*x.exp().sum())/(n+1)


def reverse_specs():
    rows=[{'id':'rectangular4x3','function':rectangular,'x':np.array([.25,-.5,.75,.5]),
           'v':np.array([.5,-.25,1.,-.5]),'w':np.array([.75,-.5,1.25])}]
    for kind in ['wide','bratu']:
        for n in [7,31]:
            grid=np.arange(1,n+1)/(n+1)
            x=.2*np.sin(np.pi*grid)+.05*np.cos(3*np.pi*grid)
            v=np.sin(2*np.pi*grid)+.3*np.cos(5*np.pi*grid);v=v/np.sqrt(np.sum(v*v))
            w=np.array([.75,-.5,1.25])if kind=='wide'else np.cos(np.pi*grid)-.2*np.sin(3*np.pi*grid)
            rows.append(dict(id=kind+str(n),function=wide if kind=='wide'else bratu,x=x,v=v,w=w))
    return rows


def hvp_specs():
    rows=[dict(id='quadratic4',function=quadratic,x=np.array([.25,-.5,.75,1.]),
               v=np.array([1.,-.5,.25,.75]),w=np.array([-.25,.5,1.,-1.]))]
    for n in [7,31]:
        grid=np.arange(1,n+1)/(n+1)
        rows.append(dict(id='bratu-energy'+str(n),function=energy,x=.2*np.sin(np.pi*grid),
                         v=np.sin(2*np.pi*grid)+.3*np.cos(3*np.pi*grid),w=np.cos(np.pi*grid)+.2*np.sin(4*np.pi*grid)))
    return rows
