import numpy as np


def corner(x):
    r=np.hypot(x[...,0],x[...,1]);theta=np.mod(np.arctan2(x[...,1],x[...,0]),2*np.pi)
    u=r**(2/3)*np.sin(2*theta/3)
    # No quadrature point is placed at the singular vertex.
    with np.errstate(divide='ignore',invalid='ignore'):
        a=(2/3)*r**(-1/3)
        grad=np.stack((a*np.sin(-theta/3),a*np.cos(-theta/3)),axis=-1)
    return u,grad


def smooth(x):
    a,b=x[...,0],x[...,1];u=np.sin(np.pi*a)*np.sin(np.pi*b)
    return u,np.stack((np.pi*np.cos(np.pi*a)*np.sin(np.pi*b),np.pi*np.sin(np.pi*a)*np.cos(np.pi*b)),axis=-1)


def viscous(x,y):
    s=x*x+y*y;D=x*x-y*y;A=-s*s+5*s-4;B=5-2*s;C=-2.
    u=A*(1+x*y);v=.5*A*D
    ux=2*x*B+2*x*x*y*B+A*y;uy=2*y*B+2*x*y*y*B+A*x
    vx=x*(A+D*B);vy=y*(-A+D*B)
    uxx=2*B+4*x*x*C+6*x*y*B+4*x**3*y*C
    uyy=2*B+4*y*y*C+6*x*y*B+4*x*y**3*C
    uxy=4*x*y*C+A+2*s*B+4*x*x*y*y*C
    vxx=A+(D+4*x*x)*B+2*x*x*D*C
    vyy=-A+(D-4*y*y)*B+2*y*y*D*C
    vxy=2*x*y*D*C;mu=1+.2*s;mx=.4*x;my=.4*y
    fx=-(2*mx*ux+2*mu*uxx+my*(uy+vx)+mu*(uyy+vxy))
    fy=-(mx*(uy+vx)+mu*(uxy+vxx)+2*my*vy+2*mu*vyy)
    velocity=np.stack((u,v),axis=-1)
    gradient=np.stack((np.stack((ux,uy),axis=-1),np.stack((vx,vy),axis=-1)),axis=-2)
    return velocity,gradient,np.stack((fx,fy),axis=-1)


def stress(x,y):
    v,G,f=viscous(x,y);return (1+.2*(x*x+y*y))[...,None,None]*(G+np.swapaxes(G,-1,-2))


def qualify():
    points=np.array([[1.2,.3],[-.8,1.2],[.4,-1.6]])
    h=2e-5;x,y=points.T
    # Independent Cartesian finite differentiation of stress, not the source formula.
    dx=(stress(x+h,y)-stress(x-h,y))/(2*h)
    dy=(stress(x,y+h)-stress(x,y-h))/(2*h)
    residual=-dx[:,:,0]-dy[:,:,1]-viscous(x,y)[2]
    theta=np.linspace(0,2*np.pi,71)
    boundary=max(np.max(abs(viscous(r*np.cos(theta),r*np.sin(theta))[0])) for r in [1.,2.])
    xx=np.array([[.3,.4],[-.3,.4],[-.4,-.2]])
    e=1e-5
    value,gradient=corner(xx)
    fd=np.stack([(corner(xx+e*np.eye(2)[j])[0]-corner(xx-e*np.eye(2)[j])[0])/(2*e) for j in range(2)],axis=-1)
    return dict(checks={'Cartesian stress/source identity':bool(np.max(abs(residual))<2e-6),
                        'annulus no-slip trace':bool(boundary<2e-13),
                        'corner analytic gradient':bool(np.max(abs(fd-gradient))<2e-9)},
                stress_source_residual=float(np.max(abs(residual))),boundary_trace=float(boundary))
