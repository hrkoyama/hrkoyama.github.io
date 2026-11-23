"""Nonperiodic 2D streamfunction/vorticity FD flow; no pressure projection.

Array axes are (y,x), u=psi_y, v=-psi_x, omega=v_x-u_y=-laplacian(psi).
Each Heun stage solves Dirichlet Poisson and reimposes the SAME Thom closure.
"""
import numpy as np
from scipy.fft import dstn, idstn


def laplacian(q, h):
    return (q[1:-1, 2:]+q[1:-1, :-2]+q[2:, 1:-1]+q[:-2, 1:-1]-4*q[1:-1, 1:-1])/h**2


def poisson_dirichlet(rhs, boundary, h):
    """Solve -Delta_h q=rhs at interior nodes; boundary is prescribed, not periodic."""
    n = boundary.shape[0]
    if boundary.shape != (n, n) or rhs.shape != (n-2, n-2):
        raise ValueError('incompatible square Dirichlet grid')
    b = rhs.copy()
    b[0] += boundary[0, 1:-1]/h**2
    b[-1] += boundary[-1, 1:-1]/h**2
    b[:, 0] += boundary[1:-1, 0]/h**2
    b[:, -1] += boundary[1:-1, -1]/h**2
    lam = 4*np.sin(np.pi*np.arange(1, n-1)/(2*(n-1)))**2/h**2
    out = boundary.copy()
    out[1:-1, 1:-1] = idstn(dstn(b, type=1, norm='ortho')/(lam[:, None]+lam[None, :]), type=1, norm='ortho')
    return out


def velocity(psi, h, lid):
    u = np.zeros_like(psi); v = np.zeros_like(psi)
    u[1:-1, 1:-1] = (psi[2:, 1:-1]-psi[:-2, 1:-1])/(2*h)
    v[1:-1, 1:-1] = -(psi[1:-1, 2:]-psi[1:-1, :-2])/(2*h)
    u[-1, 1:-1] = lid
    # Stationary corners take precedence over the moving lid.
    return u, v


def thom_wall(omega, psi, h, lid):
    """Local first-order wall vorticity from no-slip Taylor expansion.

    Corners are the mean of their two adjacent wall values; the five-point
    interior stencil does not access corner omega. No exact MMS omega enters.
    """
    w = omega.copy()
    w[0, 1:-1] = -2*psi[1, 1:-1]/h**2
    w[-1, 1:-1] = -2*psi[-2, 1:-1]/h**2-2*lid/h
    w[1:-1, 0] = -2*psi[1:-1, 1]/h**2
    w[1:-1, -1] = -2*psi[1:-1, -2]/h**2
    w[0, 0] = (w[0, 1]+w[1, 0])/2
    w[0, -1] = (w[0, -2]+w[1, -1])/2
    w[-1, 0] = (w[-1, 1]+w[-2, 0])/2
    w[-1, -1] = (w[-1, -2]+w[-2, -1])/2
    return w


def manufactured(x, y, amplitude=8., viscosity=.01):
    """Closed-form polynomial derivatives, independent of finite differences."""
    def f(z): return z*z*(1-z)*(1-z)
    def d(z): return 2*z-6*z*z+4*z*z*z
    def dd(z): return 2-12*z+12*z*z
    def ddd(z): return -12+24*z
    a = amplitude
    psi = a*f(x)*f(y)
    u = a*f(x)*d(y); v = -a*d(x)*f(y)
    omega = -a*(dd(x)*f(y)+f(x)*dd(y))
    wx = -a*(ddd(x)*f(y)+d(x)*dd(y))
    wy = -a*(dd(x)*d(y)+f(x)*ddd(y))
    lw = -a*(24*f(y)+2*dd(x)*dd(y)+24*f(x))
    forcing = u*wx+v*wy-viscosity*lw
    return dict(psi=psi, u=u, v=v, omega=omega, forcing=forcing)


def stage(omega_interior, h, viscosity, lid, forcing):
    n = omega_interior.shape[0]+2
    boundary = np.zeros((n, n))
    psi = poisson_dirichlet(omega_interior, boundary, h)
    omega = boundary.copy(); omega[1:-1, 1:-1] = omega_interior
    omega = thom_wall(omega, psi, h, lid)
    u, v = velocity(psi, h, lid)
    wx = (omega[1:-1, 2:]-omega[1:-1, :-2])/(2*h)
    wy = (omega[2:, 1:-1]-omega[:-2, 1:-1])/(2*h)
    rhs = -u[1:-1, 1:-1]*wx-v[1:-1, 1:-1]*wy+viscosity*laplacian(omega, h)+forcing
    return rhs, psi, omega, u, v


def solve(n, viscosity=.01, lid=1., amplitude=0., residual_tolerance=1e-9,
          maximum_time=100., check_every=50, dt_safety=.15):
    if n < 5 or n % 2 != 1 or viscosity <= 0 or maximum_time <= 0:
        raise ValueError('odd grid >=5 and positive viscosity/time required')
    h = 1/(n-1); x = np.linspace(0, 1, n); X, Y = np.meshgrid(x, x)
    forcing = manufactured(X, Y, amplitude, viscosity)['forcing'][1:-1, 1:-1]
    # Fixed cap is conservative for these predeclared low-Re, small-amplitude inputs.
    dt = min(dt_safety*h*h/viscosity, .25*h/max(1., abs(lid)))
    w = np.zeros((n-2, n-2)); history = []; t = 0.; steps = 0
    initial = stage(w, h, viscosity, lid, forcing)
    history.append([0., 0., float(np.max(abs(initial[0]))), 0.])
    while t < maximum_time:
        step = min(dt, maximum_time-t)
        k1, _, _, _, _ = stage(w, h, viscosity, lid, forcing)
        candidate = w+step*k1
        k2, _, _, _, _ = stage(candidate, h, viscosity, lid, forcing)
        wnext = .5*w+.5*(candidate+step*k2)
        change = float(np.max(abs(wnext-w)))
        w = wnext; t += step; steps += 1
        if not np.all(np.isfinite(w)):
            raise FloatingPointError('nonfinite vorticity; no clipping/retry implemented')
        if steps % check_every == 0 or t == maximum_time:
            rhs, psi, omega, u, v = stage(w, h, viscosity, lid, forcing)
            residual = float(np.max(abs(rhs)))
            speed_courant = float(step*np.max(abs(u)+abs(v))/h)
            history.append([float(steps), t, residual, speed_courant])
            if residual <= residual_tolerance:
                break
    rhs, psi, omega, u, v = stage(w, h, viscosity, lid, forcing)
    return dict(x=x, y=x, psi=psi, omega=omega, u=u, v=v,
                forcing=forcing, history=np.asarray(history), time=t, steps=steps,
                residual=float(np.max(abs(rhs))), dt=dt, h=h,
                last_change=change, converged=bool(np.max(abs(rhs)) <= residual_tolerance),
                state_clip_count=0, retries=0)


def gradient(q, h):
    """Second-order central interior and one-sided nonperiodic boundary gradients."""
    gx = np.empty_like(q); gy = np.empty_like(q)
    gx[:, 1:-1] = (q[:, 2:]-q[:, :-2])/(2*h)
    gy[1:-1] = (q[2:]-q[:-2])/(2*h)
    gx[:, 0] = (-3*q[:, 0]+4*q[:, 1]-q[:, 2])/(2*h)
    gx[:, -1] = (3*q[:, -1]-4*q[:, -2]+q[:, -3])/(2*h)
    gy[0] = (-3*q[0]+4*q[1]-q[2])/(2*h)
    gy[-1] = (3*q[-1]-4*q[-2]+q[-3])/(2*h)
    return gx, gy


def pressure_manufactured(n):
    """Separate Dirichlet pressure-Poisson operator check; not cavity pressure."""
    x = np.linspace(0, 1, n); X, Y = np.meshgrid(x, x); h = 1/(n-1)
    exact = X*X+Y*Y+np.sin(np.pi*X)*np.sin(np.pi*Y)
    rhs = -4+2*np.pi**2*np.sin(np.pi*X)*np.sin(np.pi*Y)
    p = poisson_dirichlet(rhs[1:-1, 1:-1], exact, h)
    px, py = gradient(p, h)
    pxexact = 2*X+np.pi*np.cos(np.pi*X)*np.sin(np.pi*Y)
    pyexact = 2*Y+np.pi*np.sin(np.pi*X)*np.cos(np.pi*Y)
    return dict(p=p, p_exact=exact, px=px, py=py, px_exact=pxexact, py_exact=pyexact,
                rhs=rhs, x=x, y=x)
