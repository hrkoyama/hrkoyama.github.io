"""Nonlinear periodic vorticity/active-buoyancy PDE; conservative centered flux differences and Heun.

Arrays have axes (x,y); velocities are centered derivatives of a discrete
streamfunction. Prescribed smooth bases are removed analytically, equivalent to
explicit steady base-maintaining forcing. No clipping or retry is performed.
"""
import numpy as np


class StageFailure(FloatingPointError):
    def __init__(self, omega, theta):
        super().__init__('Nonfinite stage; no repair is available')
        self.omega, self.theta = omega.copy(), theta.copy()


def derivative(q, h, axis):
    return (np.roll(q, -1, axis)-np.roll(q, 1, axis))/(2*h)


def laplacian(q, h):
    return sum((np.roll(q, -1, a)-2*q+np.roll(q, 1, a))/h**2 for a in (0, 1))


def streamfunction(omega, h):
    if h <= 0 or abs(omega.mean()) > max(1e-14, 1e-12*float(np.sqrt(np.mean(omega*omega)))):
        raise ValueError('Periodic Poisson requires positive spacing and zero mean vorticity')
    n, m = omega.shape
    symbol = 4/h**2*(np.sin(np.pi*np.fft.fftfreq(n))[:, None]**2
                      +np.sin(np.pi*np.fft.fftfreq(m))[None, :]**2)
    symbol[0, 0] = 1.
    transformed = np.fft.fft2(omega)/symbol
    transformed[0, 0] = 0.
    return np.fft.ifft2(transformed).real


def velocity(psi, h):
    return derivative(psi, h, 1), -derivative(psi, h, 0)


def conservative_advection(q, u, v, h):
    value = np.zeros_like(q)
    for axis, speed in enumerate((u, v)):
        face = .25*(speed+np.roll(speed, -1, axis))*(q+np.roll(q, -1, axis))
        value += (face-np.roll(face, 1, axis))/h
    return value


def profiles(y, width, buoyancy):
    shear = np.tanh(np.sin(y)/width)
    first = (1-shear**2)*np.cos(y)/width
    second = (1-shear**2)*(-np.sin(y)/width-2*shear*np.cos(y)**2/width**2)
    return shear, second, buoyancy*shear, buoyancy*first


def rhs(omega, theta, h, controls, case):
    psi = streamfunction(omega, h)
    u, v = velocity(psi, h)
    y = np.arange(omega.shape[1])*h
    shear, second, unused, gradient = profiles(y, controls['width'], controls['buoyancy'])
    rw = controls['viscosity']*laplacian(omega, h)-conservative_advection(omega, u, v, h)
    rt = controls['diffusivity']*laplacian(theta, h)-conservative_advection(theta, u, v, h)
    if case == 'kh-initial-growth':
        rw -= shear[None, :]*derivative(omega, h, 0)+second[None, :]*derivative(psi, h, 0)
    elif case == 'rt-initial-growth':
        rw += derivative(theta, h, 0)
        rt -= v*gradient[None, :]
    else:
        raise ValueError('Unknown instability case')
    return rw, rt


def initial(n, epsilon, case):
    h = 2*np.pi/n
    x = np.arange(n)*h
    if case == 'kh-initial-growth':
        omega = epsilon*np.cos(x[:, None])*(1+1.25*np.cos(2*x[None, :]))
        theta = np.zeros_like(omega)
    elif case == 'rt-initial-growth':
        theta = epsilon*np.cos(x[:, None])*(1-np.cos(x[None, :]))
        omega = np.zeros_like(theta)
    else:
        raise ValueError('Unknown instability case')
    return omega, theta


def solve(n, epsilon, case, controls, cfl_factor=1.):
    if n < 8 or n % 2 or epsilon <= 0 or not 0 < cfl_factor <= 1:
        raise ValueError('Invalid grid/amplitude/time control')
    if min(controls['viscosity'], controls['diffusivity'], controls['width']) <= 0:
        raise ValueError('Positive physical diffusion and layer width are required')
    h = 2*np.pi/n
    omega, theta = initial(n, epsilon, case)
    times = np.linspace(0., controls['final_time'][case], controls['snapshots'])
    t = 0.
    states = [(omega.copy(), theta.copy())]
    steps = 0
    diagnostic = dict(max_divergence=0., max_poisson_residual=0.,
                      max_mean_omega=0., max_mean_theta=0., finite=True)

    def observe(w, q):
        diagnostic['finite'] &= bool(np.isfinite(w).all() and np.isfinite(q).all())
        if not diagnostic['finite']:
            raise StageFailure(w, q)
        psi = streamfunction(w, h)
        u, v = velocity(psi, h)
        diagnostic['max_divergence'] = max(diagnostic['max_divergence'], float(np.max(abs(derivative(u, h, 0)+derivative(v, h, 1)))))
        diagnostic['max_poisson_residual'] = max(diagnostic['max_poisson_residual'], float(np.max(abs(-laplacian(psi, h)-w))))
        diagnostic['max_mean_omega'] = max(diagnostic['max_mean_omega'], float(abs(w.mean())))
        diagnostic['max_mean_theta'] = max(diagnostic['max_mean_theta'], float(abs(q.mean())))
        return u, v

    observe(omega, theta)
    for target in times[1:]:
        while t < target-8*np.finfo(float).eps:
            u, v = velocity(streamfunction(omega, h), h)
            base = 1. if case == 'kh-initial-growth' else 0.
            dt = min(target-t, controls['cfl']*cfl_factor/(
                (base+np.max(abs(u))+np.max(abs(v)))/h
                +4*max(controls['viscosity'], controls['diffusivity'])/h**2+1.))
            a, b = rhs(omega, theta, h, controls, case)
            wa, qa = omega+dt*a, theta+dt*b
            observe(wa, qa)
            a, b = rhs(wa, qa, h, controls, case)
            omega, theta = .5*(omega+wa+dt*a), .5*(theta+qa+dt*b)
            observe(omega, theta)
            t += dt
            steps += 1
        states.append((omega.copy(), theta.copy()))
    return {'omega': np.array([w for w, q in states]),
            'theta': np.array([q for w, q in states]), 'times': times,
            'h': h, 'steps': steps, **diagnostic}
