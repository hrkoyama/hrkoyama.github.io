"""Independent analytic Noh state and split quadrature on Cartesian cells.

Only gamma=5/3, rho0=1, unit inward speed, exactly zero upstream pressure.
Point formulas are analytic. Disk-cut cell means use numerical Gauss
integration with explicit geometric splits, and must be called quadrature
references rather than closed-form exact cell means.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def points(radius, time):
    radius = np.asarray(radius, dtype=float)
    if time < 0 or np.any(radius < 0):
        raise ValueError('Nonnegative radius and time required')
    post = radius < time/3
    upstream = np.ones_like(radius)
    np.divide(time, radius, out=upstream, where=radius > 0)
    upstream = np.where(radius > 0, 1+upstream, 1.)
    return np.where(post, 16., upstream), np.where(post, 16/3, 0.), np.where(post, 0., -1.)


def inverse_radius_primitive(x, y):
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
    out = np.zeros_like(x)
    ix, iy = x != 0, y != 0
    out[ix] += x[ix]*np.arcsinh(y[ix]/abs(x[ix]))
    out[iy] += y[iy]*np.arcsinh(x[iy]/abs(y[iy]))
    return out


def inverse_radius_rectangle(a, b, c, d):
    f = inverse_radius_primitive
    return f(b, d)-f(a, d)-f(b, c)+f(a, c)


def cell_means(edges, time, order=64):
    if time < 0 or order < 8 or order % 2:
        raise ValueError('Nonnegative time and even quadrature order>=8 required')
    edges = np.asarray(edges, float)
    if edges.ndim != 1 or np.any(np.diff(edges) <= 0) or not np.isfinite(edges).all():
        raise ValueError('Increasing finite faces required')
    a, c = np.meshgrid(edges[:-1], edges[:-1])
    b, d = np.meshgrid(edges[1:], edges[1:])
    area = (b-a)*(d-c)
    integral = inverse_radius_rectangle(a, b, c, d)
    rho = 1+time*integral/area
    post_area = np.zeros_like(rho)
    rs = time/3
    far = np.hypot(np.maximum(abs(a), abs(b)), np.maximum(abs(c), abs(d)))
    near_x = np.where((a <= 0) & (b >= 0), 0, np.minimum(abs(a), abs(b)))
    near_y = np.where((c <= 0) & (d >= 0), 0, np.minimum(abs(c), abs(d)))
    inside = far <= rs
    outside = np.hypot(near_x, near_y) >= rs
    rho[inside] = 16.
    post_area[inside] = area[inside]
    nodes, weights = leggauss(order)
    for j, i in np.argwhere(~inside & ~outside):
        xl, xr, yl, yr = a[j, i], b[j, i], c[j, i], d[j, i]
        lo, hi = max(xl, -rs), min(xr, rs)
        cuts = [lo, hi]
        if lo < 0 < hi:
            cuts.append(0.)
        for edge in (yl, yr):
            if abs(edge) < rs:
                cross = math.sqrt(rs*rs-edge*edge)
                cuts.extend(x for x in (-cross, cross) if lo < x < hi)
        disk_area, disk_inverse = 0., 0.
        cuts = sorted(set(cuts))
        for left, right in zip(cuts[:-1], cuts[1:]):
            # x=rs*sin(theta) removes the square-root endpoint singularity.
            tl, tr = np.arcsin(np.clip(np.array([left,right])/rs,-1,1))
            angle = .5*(tl+tr)+.5*(tr-tl)*nodes
            x = rs*np.sin(angle)
            height = rs*np.cos(angle)
            jacobian = .5*(tr-tl)*rs*np.cos(angle)
            bottom, top = np.maximum(yl, -height), np.minimum(yr, height)
            keep = top > bottom
            length = np.where(keep, top-bottom, 0.)
            inverse = np.where(keep, np.arcsinh(top/abs(x))-np.arcsinh(bottom/abs(x)), 0.)
            disk_area += float(np.dot(weights*jacobian, length))
            disk_inverse += float(np.dot(weights*jacobian, inverse))
        post_area[j, i] = disk_area
        rho[j, i] += (15*disk_area-time*disk_inverse)/area[j, i]
    return rho, (16/3)*post_area/area


def total_mass(time, radius=.5):
    if time < 0 or time/3 >= radius:
        raise ValueError('Shock must remain inside all square boundaries')
    return 4*radius**2+8*radius*time*math.asinh(1)+math.pi*time**2
