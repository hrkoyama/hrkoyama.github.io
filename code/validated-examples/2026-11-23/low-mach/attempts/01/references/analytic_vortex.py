"""Analytic isentropic Euler vortex, independently evaluated and quadrature-averaged.

This is a whole-plane translating solution. On the finite periodic box we use
minimum-image coordinates; the Gaussian tails at the seams are a stated model
qualification, not an exactly periodic nonlinear analytic solution.
No primary numerical solver or Numart operator is imported here.
"""
import numpy as np

GAMMA = 1.4
BETA = 3.0
LENGTH = 20.0
BACKGROUND_VELOCITY = (1.0, 0.5)


def background_pressure(mach):
    if not np.isfinite(mach) or not 0 < mach <= 1:
        raise ValueError('Require a finite background Mach number in (0,1]')
    return sum(v*v for v in BACKGROUND_VELOCITY)/(GAMMA*mach*mach)


def _fields(x, y, time, mach):
    if not np.isfinite(time):
        raise ValueError('Finite analytic time required')
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError('Finite analytic coordinates required')
    X = (x-BACKGROUND_VELOCITY[0]*time+LENGTH/2) % LENGTH-LENGTH/2
    Y = (y-BACKGROUND_VELOCITY[1]*time+LENGTH/2) % LENGTH-LENGTH/2
    gaussian = np.exp(1-X*X-Y*Y)
    spin = BETA/(2*np.pi)*np.sqrt(gaussian)
    temperature_drop = (GAMMA-1)*BETA*BETA/(8*GAMMA*np.pi*np.pi)*gaussian
    p0 = background_pressure(mach)
    theta = 1-temperature_drop/p0
    if np.any(theta <= 0):
        raise ValueError('Analytic temperature is not positive')
    density = np.exp(np.log1p(-temperature_drop/p0)/(GAMMA-1))
    pressure = p0*np.exp(GAMMA*np.log1p(-temperature_drop/p0)/(GAMMA-1))
    u = BACKGROUND_VELOCITY[0]-Y*spin
    v = BACKGROUND_VELOCITY[1]+X*spin
    return X,Y,gaussian,spin,temperature_drop,theta,density,u,v,pressure,p0


def primitive(x, y, time=0.0, mach=0.1):
    """Return (rho,u,v,p), with Mach defined from the background velocity."""
    values = _fields(x,y,time,mach)
    return np.stack(values[6:10],axis=-1)


def conserved(x, y, time=0.0, mach=0.1):
    rho,u,v,p = np.moveaxis(primitive(x,y,time,mach),-1,0)
    return np.stack((rho,rho*u,rho*v,p/(GAMMA-1)+.5*rho*(u*u+v*v)),axis=-1)


def coordinates(n):
    if isinstance(n,bool) or not isinstance(n,int) or n < 4:
        raise ValueError('Require an integer grid size >=4')
    return (np.arange(n)+.5)*LENGTH/n-LENGTH/2


def cell_means(n, time=0.0, mach=0.1, order=8):
    """Tensor Gauss cell means of CONSERVED variables, not primitive means.

    Cell quadrature is numerical and must be qualified by order doubling. The
    continuous analytic field is exact away from the finite-box seam.
    """
    return _cell_average(conserved,n,time,mach,order)


def conserved_time_derivative(x, y, time=0.0, mach=0.1):
    """Analytic physical time derivative due to the background translation."""
    X,Y,g,a,drop,theta,rho,u,v,p,p0 = _fields(x,y,time,mach)
    U,V = BACKGROUND_VELOCITY
    Tdot = -2*drop*(U*X+V*Y)
    rhodot = rho*Tdot/((GAMMA-1)*p0*theta)
    pdot = GAMMA*p*Tdot/((GAMMA-1)*p0*theta)
    udot = -U*X*Y*a-V*(Y*Y-1)*a
    vdot = -U*(1-X*X)*a+V*X*Y*a
    Edot = pdot/(GAMMA-1)+.5*rhodot*(u*u+v*v)+rho*(u*udot+v*vdot)
    return np.stack((rhodot,rhodot*u+rho*udot,rhodot*v+rho*vdot,Edot),axis=-1)


def cell_means_time_derivative(n, time=0.0, mach=0.1, order=8):
    return _cell_average(conserved_time_derivative,n,time,mach,order)


def _cell_average(function, n, time, mach, order):
    coord = coordinates(n)
    if isinstance(order,bool) or not isinstance(order,int) or order < 2:
        raise ValueError('Require a Gauss order >=2')
    nodes,weights = np.polynomial.legendre.leggauss(order)
    half = LENGTH/(2*n)
    mean = np.zeros((n,n,4))
    for i in range(order):
        for j in range(order):
            mean += .25*weights[i]*weights[j]*function(
                coord[:,None]+half*nodes[i],coord[None,:]+half*nodes[j],time,mach)
    return mean


def analytic_euler_residual(x, y, time=0.0, mach=0.1):
    """Substitute hand-derived field derivatives into physical Euler equations.

    Returns residual and an absolute term scale. This independent algebraic
    qualification does not apply the primary finite-volume numerical operator.
    Points on a minimum-image seam are excluded from its analytic interpretation.
    """
    X,Y,g,a,drop,theta,rho,u,v,p,p0 = _fields(x,y,time,mach)
    T = p0*theta
    Tx,Ty = 2*X*drop,2*Y*drop
    rx,ry = rho*Tx/((GAMMA-1)*T),rho*Ty/((GAMMA-1)*T)
    px,py = GAMMA*p*Tx/((GAMMA-1)*T),GAMMA*p*Ty/((GAMMA-1)*T)
    ux,uy = X*Y*a,(Y*Y-1)*a
    vx,vy = (1-X*X)*a,-X*Y*a
    E = p/(GAMMA-1)+.5*rho*(u*u+v*v)
    Ex = px/(GAMMA-1)+.5*rx*(u*u+v*v)+rho*(u*ux+v*vx)
    Ey = py/(GAMMA-1)+.5*ry*(u*u+v*v)+rho*(u*uy+v*vy)
    qx = np.stack((rx,rx*u+rho*ux,rx*v+rho*vx,Ex),axis=-1)
    qy = np.stack((ry,ry*u+rho*uy,ry*v+rho*vy,Ey),axis=-1)
    qt = -BACKGROUND_VELOCITY[0]*qx-BACKGROUND_VELOCITY[1]*qy
    fx = np.stack((rx*u+rho*ux,rx*u*u+2*rho*u*ux+px,
                   rx*u*v+rho*ux*v+rho*u*vx,ux*(E+p)+u*(Ex+px)),axis=-1)
    gy = np.stack((ry*v+rho*vy,ry*u*v+rho*uy*v+rho*u*vy,
                   ry*v*v+2*rho*v*vy+py,vy*(E+p)+v*(Ey+py)),axis=-1)
    return qt+fx+gy,1+abs(qt)+abs(fx)+abs(gy)


def analytic_local_balance(x, y, time=0.0, mach=0.1):
    """Independent radial balance and divergence identities for point checks."""
    X,Y,g,a,drop,theta,rho,u,v,p,p0 = _fields(x,y,time,mach)
    pressure_gradient_over_density = np.stack((2*GAMMA*X*drop/(GAMMA-1),
                                               2*GAMMA*Y*drop/(GAMMA-1)),axis=-1)
    centripetal = -a[...,None]**2*np.stack((X,Y),axis=-1)
    return {'radial_momentum_residual':pressure_gradient_over_density+centripetal,
            'velocity_divergence':X*Y*a-X*Y*a,
            'entropy_ratio':p/rho**GAMMA,
            'background_pressure':p0}
