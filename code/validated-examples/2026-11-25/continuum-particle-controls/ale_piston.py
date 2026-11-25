"""Fixed 2D Euler ALE skew-piston recipe.

Tan--Lv--Zhu(2023), Example8 initial geometry/e0 variant. Prescribed affine
mesh motion is not a material Lagrangian solver or a Lagrange/remap algorithm.
"""
import numpy as np
import time
from failure_support import NumericalFailure,own_failure


def mesh(nx, ny):
    xx, yy = np.meshgrid(np.linspace(0., 1., nx+1), np.linspace(0., .1, ny+1))
    initial = np.stack((xx+(.1-yy)*np.sin(np.pi*xx), yy), -1).reshape(-1, 2)
    cells = []
    faces, seen = [], {}
    for j in range(ny):
        for i in range(nx):
            a = j*(nx+1)+i
            nodes = [a, a+1, a+nx+2, a+nx+1]
            owner = len(cells)
            cells.append(nodes)
            for n0, n1 in zip(nodes, nodes[1:]+nodes[:1]):
                key = tuple(sorted((n0, n1)))
                if key in seen:
                    faces[seen[key]][3] = owner
                else:
                    seen[key] = len(faces)
                    faces.append([n0, n1, owner, -1])
    return initial, np.asarray(cells), np.asarray(faces)


def geometry(initial, cells, faces, t):
    points = initial.copy()
    points[:, 0] = t+(1-t)*initial[:, 0]
    velocities = np.zeros_like(points)
    velocities[:, 0] = 1-initial[:, 0]
    polygons = points[cells]
    nxt = np.roll(polygons, -1, axis=1)
    area = .5*np.sum(polygons[..., 0]*nxt[..., 1]-nxt[..., 0]*polygons[..., 1], axis=1)
    if np.min(area) <= 0:
        raise NumericalFailure('Nonpositive signed mesh area; no untangling',{'geometry_time':t},{'failed_points':points.copy(),'failed_areas':area.copy(),'cells':cells.copy()})
    edge = points[faces[:, 1]]-points[faces[:, 0]]
    normals = np.stack((edge[:, 1], -edge[:, 0]), -1)
    length = np.linalg.norm(normals, axis=1)
    normals /= length[:, None]
    w = .5*(velocities[faces[:, 0]]+velocities[faces[:, 1]])
    return points, area, normals, length, np.sum(w*normals, axis=1)


def primitive(U, gamma):
    rho = U[:, 0]
    if not np.isfinite(U).all() or np.min(rho)<=0:
        raise NumericalFailure('Invalid Euler density before division',{}, {'failed_conserved':U.copy()})
    velocity = U[:, 1:3]/rho[:, None]
    pressure = (gamma-1)*(U[:, 3]-.5*rho*np.sum(velocity**2, axis=1))
    if not np.isfinite(U).all() or np.min(rho) <= 0 or np.min(pressure) <= 0:
        raise NumericalFailure('Nonpositive/nonfinite Euler state; no floors',{}, {'failed_conserved':U.copy(),'failed_pressure':pressure.copy()})
    return rho, velocity, pressure


def ale_flux(U, normals, wn, gamma):
    rho, vel, pressure = primitive(U, gamma)
    un = np.sum(vel*normals, axis=1)
    F = U*(un-wn)[:, None]
    F[:, 1:3] += pressure[:, None]*normals
    F[:, 3] += pressure*un
    speed = np.abs(un-wn)+np.sqrt(gamma*pressure/rho)
    return F, speed


def face_flux(U, faces, normals, wn, gamma):
    left, right = faces[:, 2], faces[:, 3]
    L, R = U[left].copy(), U[np.maximum(right, 0)].copy()
    wall = right < 0
    rho, vel, pressure = primitive(L[wall], gamma)
    delta = 2*(wn[wall]-np.sum(vel*normals[wall], axis=1))
    reflected = vel+delta[:, None]*normals[wall]
    R[wall, 0] = rho
    R[wall, 1:3] = rho[:, None]*reflected
    R[wall, 3] = pressure/(gamma-1)+.5*rho*np.sum(reflected**2, axis=1)
    FL, sL = ale_flux(L, normals, wn, gamma)
    FR, sR = ale_flux(R, normals, wn, gamma)
    speeds = np.maximum(sL, sR)
    return .5*(FL+FR)-.5*speeds[:, None]*(R-L), speeds


def piston_reference(t, gamma=5/3, rho0=1., e0=1e-4, up=1.):
    p0 = (gamma-1)*rho0*e0
    c02 = gamma*p0/rho0
    half = .25*(gamma+1)*up
    speed = half+np.sqrt(half*half+c02)
    rho1 = rho0*speed/(speed-up)
    p1 = p0+rho0*speed*up
    return dict(shock_position=speed*t, speed=speed, rho0=rho0, p0=p0,
                rho1=rho1, p1=p1, piston_velocity=up)


def polygon_area(poly):
    if len(poly) < 3:
        return 0.
    arr = np.asarray(poly)
    return abs(.5*np.sum(arr[:, 0]*np.roll(arr[:, 1], -1)-arr[:, 1]*np.roll(arr[:, 0], -1)))


def area_left(poly, xcut):
    result = []
    for a, b in zip(poly, np.roll(poly, -1, axis=0)):
        ain, bin_ = a[0] <= xcut, b[0] <= xcut
        if ain:
            result.append(a)
        if ain != bin_:
            result.append(a+(xcut-a[0])/(b[0]-a[0])*(b-a))
    return polygon_area(result)


def conserved_cell_reference(points, cells, t, gamma=5/3, rho0=1., e0=1e-4):
    """Clip each actual quadrilateral; average conserved quantities, not p(U)."""
    ref = piston_reference(t, gamma, rho0, e0)
    before = np.array([rho0, 0., 0., rho0*e0])
    after = np.array([ref['rho1'], ref['rho1'], 0., ref['p1']/(gamma-1)+.5*ref['rho1']])
    values = []
    for poly in points[cells]:
        fraction = area_left(poly, ref['shock_position'])/polygon_area(poly)
        values.append(fraction*after+(1-fraction)*before)
    return np.asarray(values), ref


def run_piston(nx, ny, final_time=.6, gamma=5/3, rho0=1., e0=1e-4, cfl=.2, deadline=None):
    initial, cells, faces = mesh(nx, ny)
    points, areas, normals, lengths, wn = geometry(initial, cells, faces, 0.)
    Q = areas[:, None]*np.array([rho0, 0., 0., rho0*e0])
    start = np.sum(Q, axis=0)
    boundary_integral = np.zeros(4)
    max_gcl, t, steps = 0., 0., 0
    history = []
    left, right = faces[:, 2], faces[:, 3]
    interior, boundary = right >= 0, right < 0
    step_start_Q=Q.copy();step_start_points=points.copy();stage,stage_time,stage_points="initial",t,points
    try:
        while t < final_time:
            step_start_Q=Q.copy();step_start_points=points.copy()
            stage,stage_time,stage_points="step-start",t,points
            if deadline is not None and time.monotonic()>deadline:raise RuntimeError("Shared numerical wall budget exceeded")
            U = Q/areas[:, None]
            _, speed = face_flux(U, faces, normals, wn, gamma)
            denominator = np.zeros(len(cells))
            np.add.at(denominator, left, speed*lengths)
            np.add.at(denominator, right[interior], (speed*lengths)[interior])
            active_cfl = .01 if t < .01 else cfl
            dt = min(final_time-t, float(np.min(active_cfl*areas/denominator)))
            # Affine-in-time geometry is evaluated at the same midpoint in every flux.
            stage,stage_time="midpoint-geometry",t+.5*dt
            mid_points, _, normal_mid, length_mid, wn_mid = geometry(initial, cells, faces, t+.5*dt)
            stage,stage_time,stage_points="midpoint-flux",t+.5*dt,mid_points
            flux, _ = face_flux(U, faces, normal_mid, wn_mid, gamma)
            transfer = dt*length_mid[:, None]*flux
            delta = np.zeros_like(Q)
            np.add.at(delta, left, -transfer)
            np.add.at(delta, right[interior], transfer[interior])
            swept = np.zeros(len(cells))
            np.add.at(swept, left, dt*length_mid*wn_mid)
            np.add.at(swept, right[interior], -(dt*length_mid*wn_mid)[interior])
            Q += delta
            boundary_integral -= np.sum(transfer[boundary], axis=0)
            stage,stage_time="final-geometry",t+dt
            next_points, next_areas, normals, lengths, wn = geometry(initial, cells, faces, t+dt)
            max_gcl = max(max_gcl, float(np.max(np.abs(next_areas-areas-swept))))
            stage,stage_time,stage_points="final-positivity",t+dt,next_points
            rho, vel, pressure = primitive(Q/next_areas[:, None], gamma)
            t += dt
            steps += 1
            areas, points = next_areas, next_points
            history.append([t, dt, float(np.min(rho)), float(np.min(pressure)), float(np.min(areas))])
            if steps >= 20000:
                raise RuntimeError('Piston step cap')
    except Exception as error:
        failed_points=getattr(error,'state_arrays',{}).get('failed_points',stage_points)
        failure=own_failure(error,stage,stage_time,steps,{'step_start_Q':step_start_Q,'step_start_points':step_start_points},{'failed_Q':Q,'failed_points':failed_points,'reference_nodes':initial,'cells':cells,'faces':faces,'boundary_integral_at_failure':boundary_integral,'history_before_failure':np.asarray(history)})
        raise failure
    exact, reference = conserved_cell_reference(points, cells, t, gamma, rho0, e0)
    return dict(points=points, cells=cells, faces=faces, areas=areas, conserved=Q/areas[:, None],
                exact_conserved_average=exact, reference=reference, start_integrals=start,
                final_integrals=np.sum(Q, axis=0), boundary_integral=boundary_integral,
                conservation_defect=np.sum(Q, axis=0)-start-boundary_integral,
                max_GCL_error=max_gcl, history=np.asarray(history), steps=steps,
                mesh_motion='prescribed affine ALE; no material mesh/remap',
                sampling='area-average conserved exact shock; primitive of average is distinct')
