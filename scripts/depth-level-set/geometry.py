"""Analytic rigid motions and piecewise-linear geometric measurements.

No numerical advection or redistancing routine is imported here. Coordinates,
time, velocity and phi are nondimensional; phi is negative inside the circle.
"""
import math
import numpy as np


def center(config, time):
    initial = np.asarray(config['center'], dtype=float)
    if config['motion'] == 'translation':
        return initial + time*np.asarray(config['velocity'])
    pivot = np.asarray(config['pivot'])
    theta = config['omega']*time
    rotation = np.array([[math.cos(theta), -math.sin(theta)],
                         [math.sin(theta), math.cos(theta)]])
    return pivot + rotation @ (initial-pivot)


def distance(config, x, y, time):
    cx, cy = center(config, time)
    return np.hypot(x-cx, y-cy)-config['radius']


def grid(n):
    axis = (np.arange(n)+.5)/n
    return np.meshgrid(axis, axis, indexing='xy')


def negative_triangle_fraction(a, b, c):
    """Exact negative-area fraction of a LINEAR field on one triangle."""
    values = np.stack((a,b,c))
    count = np.sum(values < 0, axis=0)
    answer = np.where(count == 3, 1., 0.)
    for i in range(3):
        u, v, w = values[i], values[(i+1)%3], values[(i+2)%3]
        first = np.divide(u, u-v, out=np.zeros_like(u), where=u != v)
        second = np.divide(u, u-w, out=np.zeros_like(u), where=u != w)
        product = first*second
        answer = np.where((count == 1)&(u < 0), product, answer)
        answer = np.where((count == 2)&(u >= 0), 1-product, answer)
    return answer


def area(phi, dx):
    a,b,c,d = phi[:-1,:-1],phi[:-1,1:],phi[1:,1:],phi[1:,:-1]
    # Each center-to-center square is split along its SW--NE diagonal.
    # The enclosed circle stays strictly inside this covered rectangle.
    return float(.5*dx*dx*np.sum(negative_triangle_fraction(a,b,c)+negative_triangle_fraction(a,c,d)))


def crossings(phi, x, y):
    """Zero crossings on horizontal/vertical grid edges, with linear interpolation.

    These are samples of the reconstructed interface, NOT a Hausdorff distance.
    """
    points = []
    for a,b,xa,xb,ya,yb in [(phi[:,:-1],phi[:,1:],x[:,:-1],x[:,1:],y[:,:-1],y[:,1:]),
                           (phi[:-1],phi[1:],x[:-1],x[1:],y[:-1],y[1:])]:
        mask = ((a < 0)&(b >= 0))|((b < 0)&(a >= 0))
        if np.any(mask):
            fraction = a[mask]/(a[mask]-b[mask])
            points.append(np.column_stack((xa[mask]+fraction*(xb[mask]-xa[mask]),
                                           ya[mask]+fraction*(yb[mask]-ya[mask]))))
    if not points:
        raise RuntimeError('The zero interface disappeared')
    return np.concatenate(points)


def measure(phi, config, time):
    n = len(phi); dx = 1/n; x,y = grid(n)
    if phi.shape != (n,n) or not np.isfinite(phi).all():
        raise ValueError('A finite square field is required')
    points = crossings(phi,x,y)
    cx,cy = center(config,time)
    radial = np.abs(np.hypot(points[:,0]-cx,points[:,1]-cy)-config['radius'])
    reference = distance(config,x,y,time)
    band = np.abs(reference) <= 2*dx
    gx = (phi[1:-1,2:]-phi[1:-1,:-2])/(2*dx)
    gy = (phi[2:,1:-1]-phi[:-2,1:-1])/(2*dx)
    interior_band = band[1:-1,1:-1]
    exact_area = math.pi*config['radius']**2
    numeric_area = area(phi,dx)
    if not np.any(interior_band):
        raise RuntimeError('Empty interface diagnostic band')
    angle = np.arctan2(points[:,1]-cy,points[:,0]-cx)
    return {'time':float(time),'area':numeric_area,
            'relative_area_bias':numeric_area/exact_area-1,
            'interface_max_radial_error':float(radial.max()),
            'interface_rms_radial_error':float(np.sqrt(np.mean(radial**2))),
            'band_phi_rms_error':float(np.sqrt(np.mean((phi[band]-reference[band])**2))),
            'band_distance_gradient_rms':float(np.sqrt(np.mean((np.hypot(gx,gy)[interior_band]-1)**2))),
            'crossing_count':len(points)}, points[np.argsort(angle)]
