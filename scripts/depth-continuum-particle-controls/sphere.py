"""Fixed spherical transport and axisymmetric shallow-water recipes.

Prescribed scalar transport and a zonally symmetric SWE subproblem are distinct.
This is neither the seven-case Williamson suite nor a general dynamical core.
"""
import numpy as np
import time
from failure_support import NumericalFailure,own_failure


def lonlat_grid(nlon, nlat):
    lon = (np.arange(nlon) + .5) * (2*np.pi/nlon)
    edges = np.linspace(-np.pi/2, np.pi/2, nlat+1)
    lat = .5*(edges[1:]+edges[:-1])
    ll, pp = np.meshgrid(lon, lat)
    xyz = np.stack((np.cos(pp)*np.cos(ll), np.cos(pp)*np.sin(ll), np.sin(pp)), -1)
    areas = np.broadcast_to((np.sin(edges[1:])-np.sin(edges[:-1]))[:, None]*(2*np.pi/nlon), ll.shape).copy()
    return lon, lat, xyz, areas


def rotate(x, axis, angle):
    axis = np.asarray(axis, dtype=float)
    axis = axis/np.linalg.norm(axis)
    return x*np.cos(angle)+np.cross(axis, x)*np.sin(angle)+np.sum(x*axis, axis=-1)[..., None]*axis*(1-np.cos(angle))


def cosine_bell(xyz, center, radius=1/3):
    r = np.arccos(np.clip(np.sum(xyz*center, axis=-1), -1., 1.))
    return np.where(r < radius, .5*(1+np.cos(np.pi*r/radius)), 0.)


def analytic_bell_mass(radius):
    """Direct integral of the unit-peak cosine cap over a unit sphere."""
    if not 0<radius<np.pi:raise ValueError('Require cap radius strictly between zero and pi')
    cosine=np.cos(radius);k=np.pi/radius
    return float(np.pi*((1-cosine)+(1+cosine)/(1-k*k)))


def bilinear_pole_periodic(q, xyz):
    """Cell-center interpolation with explicit across-pole longitude half-turn."""
    ny, nx = q.shape
    lon = np.mod(np.arctan2(xyz[..., 1], xyz[..., 0]), 2*np.pi)
    lat = np.arcsin(np.clip(xyz[..., 2], -1., 1.))
    sx, sy = lon*nx/(2*np.pi)-.5, (lat+np.pi/2)*ny/np.pi-.5
    ix, iy = np.floor(sx).astype(int), np.floor(sy).astype(int)
    fx, fy = sx-ix, sy-iy

    def gather(yy, xx):
        below, above = yy < 0, yy >= ny
        reflected_y = np.where(below, -yy-1, np.where(above, 2*ny-yy-1, yy))
        reflected_x = xx + np.where(below | above, nx//2, 0)
        return q[reflected_y, reflected_x % nx]

    if nx % 2:
        raise ValueError('Even longitude count is required for exact half-turn indexing')
    return ((1-fx)*(1-fy)*gather(iy, ix)+fx*(1-fy)*gather(iy, ix+1)
            +(1-fx)*fy*gather(iy+1, ix)+fx*fy*gather(iy+1, ix+1))


def transport(nlon, nlat, steps, tilt, period=1., radius=1/3, deadline=None):
    lon, lat, xyz, areas = lonlat_grid(nlon, nlat)
    # This sign matches u=cos(phi)cos(alpha)+sin(phi)cos(lon)sin(alpha),
    # v=-sin(lon)sin(alpha), with angular frequency 2*pi/period.
    axis = np.array([-np.sin(tilt), 0., np.cos(tilt)])
    center = np.array([0., -1., 0.])
    q0 = cosine_bell(xyz, center, radius)
    q = q0.copy()
    departure = rotate(xyz, axis, -2*np.pi/steps)
    snapshots = [(0., q.copy())]
    i=-1;step_start_q=q.copy();stage='initial';stage_time=0.
    try:
        for i in range(steps):
            step_start_q=q.copy();stage="transport-step-start";stage_time=i*period/steps
            if deadline is not None and time.monotonic()>deadline:raise RuntimeError("Shared numerical wall budget exceeded")
            stage="transport-interpolation";stage_time=(i+1)*period/steps
            q = bilinear_pole_periodic(q, departure)
            if not np.isfinite(q).all():
                raise FloatingPointError('Nonfinite sphere transport')
            if (i+1) in {steps//4, steps//2, 3*steps//4, steps}:
                snapshots.append(((i+1)*period/steps, q.copy()))
    except Exception as error:
        failure=own_failure(error,stage,stage_time,max(0,i),{'step_start_q':step_start_q},{'failed_q':q,'xyz':xyz,'departure_xyz':departure,'areas':areas})
        raise failure
    # Point-valued exact return on this same grid; area weights are quadrature.
    exact = cosine_bell(rotate(xyz, axis, -2*np.pi), center, radius)
    mass0, mass = float(np.sum(q0*areas)), float(np.sum(q*areas))
    analytic_mass=analytic_bell_mass(radius)
    return dict(lon=lon, lat=lat, xyz=xyz, areas=areas, initial=q0, final=q,
                exact=exact, snapshots=snapshots, initial_mass=mass0, final_mass=mass,
                analytic_bell_mass=analytic_mass,initial_quadrature_mass_error=mass0-analytic_mass,
                initial_quadrature_mass_relative_error=(mass0-analytic_mass)/analytic_mass,
                relative_L1=float(np.sum(areas*np.abs(q-exact))/np.sum(areas*np.abs(exact))),
                mass_drift=(mass-mass0)/mass0,
                reference_sampling='exact point values; spherical-band quadrature weights',
                conservative=False, equations='prescribed scalar advection, not nonlinear SWE')


def zonal_exact(phi, a=1., g=1., omega=2., u0=.5, h0=10.):
    return np.array([h0-(a*omega*u0+.5*u0*u0)*np.sin(phi)**2/g,
                     u0*np.cos(phi), np.zeros_like(phi)])


def analytic_zonal_force(phi,a=1.,g=1.,omega=2.,u0=.5):
    u=u0*np.cos(phi)
    exact_dh=-(2*a*omega*u0+u0*u0)*np.sin(phi)*np.cos(phi)/g
    return (2*omega*np.sin(phi)+u*np.tan(phi)/a)*u+g*exact_dh/a


def zonal_rhs(state, phi, a=1., g=1., omega=2.):
    """Full nonlinear axisymmetric primitive momenta, conservative h flux.

    Pole ghost parity is scalar-even and tangent-vector-odd; pole mass flux zero.
    No equilibrium residual is subtracted and no manufactured source is added.
    """
    h, u, v = state
    if not np.isfinite(state).all() or np.min(h)<=0:
        raise NumericalFailure('Invalid spherical SWE RHS state; no repair',{}, {'failed_state':state.copy(),'latitude':phi.copy()})
    dphi = np.pi/len(phi)
    cosphi = np.cos(phi)
    he = np.pad(h, 1, mode='reflect')
    # Nearest ghost centers reflect across coordinate poles, not across centers.
    he[0], he[-1] = h[0], h[-1]
    ue, ve = np.pad(u, 1), np.pad(v, 1)
    ue[0], ue[-1], ve[0], ve[-1] = -u[0], -u[-1], -v[0], -v[-1]
    dh = (he[2:]-he[:-2])/(2*dphi)
    du = (ue[2:]-ue[:-2])/(2*dphi)
    dv = (ve[2:]-ve[:-2])/(2*dphi)
    edges = np.linspace(-np.pi/2, np.pi/2, len(phi)+1)
    flux = .5*(he[:-1]+he[1:])*.5*(ve[:-1]+ve[1:])*np.cos(edges)
    flux[0] = flux[-1] = 0.
    # Exact latitude-band area gives telescoping finite-volume mass conservation.
    band = np.sin(edges[1:])-np.sin(edges[:-1])
    ht = -(flux[1:]-flux[:-1])/(a*band)
    coriolis = 2*omega*np.sin(phi)+u*np.tan(phi)/a
    ut = -v*du/a+coriolis*v
    vt = -v*dv/a-coriolis*u-g*dh/a
    return np.array([ht, ut, vt])


def zonal_balance(nlat, final_time=.2, cfl=.1, a=1., g=1., omega=2., u0=.5, h0=10., deadline=None):
    edges = np.linspace(-np.pi/2, np.pi/2, nlat+1)
    phi = .5*(edges[1:]+edges[:-1])
    state = zonal_exact(phi, a, g, omega, u0, h0)
    initial = state.copy()
    try:
        initial_rhs = zonal_rhs(state, phi, a, g, omega)
    except Exception as error:
        raise own_failure(error,'initial-RHS',0.,0,{'step_start_state':state},{'failed_state':state,'latitude':phi})
    weights = np.sin(edges[1:])-np.sin(edges[:-1])
    mass0 = float(np.sum(weights*state[0]))
    t, count = 0., 0
    step_start_state=state.copy();stage,stage_time,stage_state='initial',t,state
    try:
        while t < final_time:
            step_start_state=state.copy();stage,stage_time,stage_state="step-start",t,state
            if deadline is not None and time.monotonic()>deadline:raise RuntimeError("Shared numerical wall budget exceeded")
            dt = min(final_time-t, cfl*a*(np.pi/nlat)/float(np.max(np.abs(state[2])+np.sqrt(g*state[0]))))
            stage,stage_time,stage_state="k1",t,state
            k1 = zonal_rhs(stage_state, phi, a, g, omega)
            stage,stage_time,stage_state="k2",t+.5*dt,state+.5*dt*k1
            k2 = zonal_rhs(stage_state, phi, a, g, omega)
            stage,stage_time,stage_state="k3",t+.5*dt,state+.5*dt*k2
            k3 = zonal_rhs(stage_state, phi, a, g, omega)
            stage,stage_time,stage_state="k4",t+dt,state+dt*k3
            k4 = zonal_rhs(stage_state, phi, a, g, omega)
            state = state+dt*(k1+2*k2+2*k3+k4)/6
            stage,stage_time,stage_state="final",t+dt,state
            if not np.isfinite(state).all() or np.min(state[0]) <= 0:
                raise FloatingPointError('Invalid spherical SWE state; no repair allowed')
            t += dt
            count += 1
            if count > 20000:
                raise RuntimeError('Sphere step cap')
    except Exception as error:
        failure=own_failure(error,stage,stage_time,count,{'step_start_state':step_start_state},{'failed_state':stage_state,'latitude':phi,'weights':weights})
        raise failure
    return dict(phi=phi, weights=weights, initial=initial, final=state,
                initial_rhs=initial_rhs, steps=count, final_time=t,
                mass_defect=float((np.sum(weights*state[0])-mass0)/mass0),
                reference='analytic stationary nondimensional W92-test2-type axisymmetric subproblem')
