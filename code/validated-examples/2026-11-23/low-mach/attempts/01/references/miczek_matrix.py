"""Small dense-matrix oracle for Miczek flux preconditioning.

Direct matrix assembly/eigendecomposition is intentionally separate from the
primary polynomial-action implementation. Used only at fixed diagnostic states,
never for any independent PDE simulation. Dimensional standard Euler has the
paper's global pressure-rescaling Mach parameter set to one; the physical low
Mach number instead enters through the large background pressure/sound speed.
"""
import numpy as np

GAMMA = 1.4


def _state(w):
    w = np.asarray(w,float)
    if w.shape != (4,) or not np.all(np.isfinite(w)) or w[0] <= 0 or w[3] <= 0:
        raise ValueError('Require one finite positive primitive state (rho,u,v,p)')
    return w


def _normal(normal):
    if np.isscalar(normal):
        if normal not in (0,1):
            raise ValueError('Cartesian axis must be0 or1')
        normal = (1.,0.) if normal == 0 else (0.,1.)
    n = np.asarray(normal,float)
    if n.shape != (2,) or not np.isfinite(n).all() or abs(float(n@n)-1) > 1e-13:
        raise ValueError('Require a unit face normal')
    return n


def primitive_to_conserved_jacobian(w):
    rho,u,v,p = _state(w)
    return np.array([[1.,0.,0.,0.],
                     [u,rho,0.,0.],
                     [v,0.,rho,0.],
                     [.5*(u*u+v*v),rho*u,rho*v,1/(GAMMA-1)]])


def conserved_to_primitive_jacobian(w):
    rho,u,v,p = _state(w)
    g = GAMMA-1
    return np.array([[1.,0.,0.,0.],
                     [-u/rho,1/rho,0.,0.],
                     [-v/rho,0.,1/rho,0.],
                     [.5*g*(u*u+v*v),-g*u,-g*v,g]])


def primitive_matrices(w, normal=0, mach_cutoff=.01, preconditioned=True):
    rho,u,v,p = _state(w)
    nx,ny = _normal(normal)
    if not np.isfinite(mach_cutoff) or not 0 < mach_cutoff <= 1:
        raise ValueError('Require0<Mcut<=1')
    c = np.sqrt(GAMMA*p/rho)
    un = nx*u+ny*v
    A = np.eye(4)*un
    A[0,1],A[0,2] = rho*nx,rho*ny
    A[1,3],A[2,3] = nx/rho,ny/rho
    A[3,1],A[3,2] = GAMMA*p*nx,GAMMA*p*ny
    mu = min(1.,max(float(np.hypot(u,v)/c),float(mach_cutoff)))
    delta = 1/mu-1 if preconditioned else 0.
    P = np.eye(4)
    P[0,1],P[0,2] = rho*delta*nx/c,rho*delta*ny/c
    P[1,3],P[2,3] = -delta*nx/(rho*c),-delta*ny/(rho*c)
    P[3,1],P[3,2] = rho*c*delta*nx,rho*c*delta*ny
    return A,P


def primitive_diffusion_matrix(w, normal=0, mach_cutoff=.01, preconditioned=True):
    A,P = primitive_matrices(w,normal,mach_cutoff,preconditioned)
    K = P@A
    values,vectors = np.linalg.eig(K)
    scale = max(1.,float(np.max(abs(values))))
    if np.max(abs(np.imag(values))) > 1e-10*scale:
        raise ValueError('Expected real preconditioned characteristic speeds')
    absolute = (vectors*np.abs(np.real(values))[None,:])@np.linalg.inv(vectors)
    result = np.linalg.solve(P,absolute)
    if np.max(abs(np.imag(result))) > 1e-9*max(1.,float(np.max(abs(result)))):
        raise ValueError('Dense diffusion oracle has unexpected imaginary content')
    return np.real(result)


def conserved_matrices(w, normal=0, mach_cutoff=.01, preconditioned=True):
    J = primitive_to_conserved_jacobian(w)
    Ji = conserved_to_primitive_jacobian(w)
    A,P = primitive_matrices(w,normal,mach_cutoff,preconditioned)
    D = primitive_diffusion_matrix(w,normal,mach_cutoff,preconditioned)
    return J@A@Ji,J@D@Ji


def energy_scaling(w):
    """Map conservative perturbations to acoustic energy plus entropy variables.

    Components: (dp/(rho*c), du, dv, c*(drho/rho-dp/(rho*c*c))).
    Euclidean norms in these coordinates avoid measuring huge background-energy
    units as if they were velocity error. This is an explicit stated diagnostic
    norm, not a theorem bounding arbitrary nonlinear solutions.
    """
    rho,u,v,p = _state(w)
    c = np.sqrt(GAMMA*p/rho)
    S = np.array([[0.,0.,0.,1/(rho*c)],
                  [0.,1.,0.,0.],
                  [0.,0.,1.,0.],
                  [c/rho,0.,0.,-1/(rho*c)]])
    return S@conserved_to_primitive_jacobian(w)
