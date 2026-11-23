"""Rigidly rotated slotted-disk cell areas from polygon/circle intersections.

This evaluator integrates the indicator over each cell. It never samples a
pixel mask or evolves a PDE. Polygon edges are split at their circle crossings;
Green's theorem gives a triangle contribution inside and a circular sector
outside. The disk-minus-slot is partitioned into three disjoint convex pieces
to avoid subtracting nearly equal disk and slot areas.
"""
from functools import lru_cache
import math
import numpy as np


def _cross(a, b):
    return float(a[0]*b[1]-a[1]*b[0])


def _polygon_area(vertices):
    if len(vertices) < 3:
        return 0.
    return .5*sum(_cross(a, b) for a, b in zip(vertices, np.roll(vertices, -1, axis=0)))


def clip_halfplane(vertices, normal, bound):
    """Sutherland--Hodgman clipping to normal.dot(x)<=bound."""
    v = np.asarray(vertices, dtype=float)
    if len(v) == 0:
        return np.empty((0, 2))
    normal = np.asarray(normal, dtype=float)
    out = []
    previous = v[-1]
    previous_distance = float(previous@normal-bound)
    for current in v:
        distance = float(current@normal-bound)
        if (distance <= 0) != (previous_distance <= 0):
            fraction = previous_distance/(previous_distance-distance)
            out.append(previous+fraction*(current-previous))
        if distance <= 0:
            out.append(current)
        previous, previous_distance = current, distance
    return np.array(out, dtype=float).reshape((-1, 2))


def circle_polygon_area(vertices, radius, diagnostics=None):
    """Area of a counterclockwise convex polygon intersected with a disk.

    The disk center is the coordinate origin. Topological full/empty cases
    are resolved geometrically before evaluating any alternating arc sum.
    """
    v = np.asarray(vertices, dtype=float)
    if len(v) < 3:
        return 0.
    if radius <= 0 or not np.isfinite(radius) or not np.all(np.isfinite(v)):
        raise ValueError('Require a positive radius and finite polygon')
    r2 = radius*radius
    inside = np.sum(v*v, axis=1) <= r2
    area = _polygon_area(v)
    if area < -64*np.finfo(float).eps:
        raise ValueError('Require a counterclockwise polygon')
    if np.all(inside):
        cleaned = max(area, 0.)
        if diagnostics is not None and cleaned != area:
            diagnostics['area_cleanup_count'] += 1
            diagnostics['maximum_area_cleanup'] = max(diagnostics['maximum_area_cleanup'], abs(cleaned-area))
            diagnostics['area_cleanup_signed_change'] += cleaned-area
        return cleaned
    origin_inside, closest2 = True, math.inf
    for a, b in zip(v, np.roll(v, -1, axis=0)):
        d = b-a
        length2 = float(d@d)
        if length2 == 0:
            continue
        origin_inside &= _cross(d, -a) >= 0
        t = min(1., max(0., -float(a@d)/length2))
        closest2 = min(closest2, float((a+t*d)@(a+t*d)))
    if not np.any(inside) and closest2 >= r2:
        return math.pi*r2 if origin_inside else 0.
    total = 0.
    for a, b in zip(v, np.roll(v, -1, axis=0)):
        d = b-a
        aa = float(d@d)
        if aa == 0:
            continue
        bb, cc = 2*float(a@d), float(a@a)-r2
        discriminant = bb*bb-4*aa*cc
        cuts = [0., 1.]
        if discriminant > 0:
            root = math.sqrt(discriminant)
            cuts += [t for t in ((-bb-root)/(2*aa), (-bb+root)/(2*aa)) if 0 < t < 1]
        cuts.sort()
        for left, right in zip(cuts[:-1], cuts[1:]):
            p, q = a+left*d, a+right*d
            middle = .5*(p+q)
            if float(middle@middle) <= r2:
                total += .5*_cross(p, q)
            else:
                total += .5*r2*math.atan2(_cross(p, q), float(p@q))
    # Only geometric roundoff is removed here, never a transported state.
    tolerance = 128*np.finfo(float).eps*max(r2, abs(area))
    if not -tolerance <= total <= min(area, math.pi*r2)+tolerance:
        raise ArithmeticError('Circle-polygon area lies outside geometric bounds')
    cleaned = min(max(total, 0.), max(0., min(area, math.pi*r2)))
    if diagnostics is not None and cleaned != total:
        diagnostics['area_cleanup_count'] += 1
        diagnostics['maximum_area_cleanup'] = max(diagnostics['maximum_area_cleanup'], abs(cleaned-total))
        diagnostics['area_cleanup_signed_change'] += cleaned-total
    return cleaned


def total_area(radius=.15, slot_width=.05, slot_offset=.1):
    """Closed total area for a lower-open slot ending above the disk center."""
    half = slot_width/2
    if not (0 < half < radius and 0 <= slot_offset <= math.sqrt(radius*radius-half*half)):
        raise ValueError('Require the fixed upper slot end inside the disk')
    removed = (2*half*slot_offset+half*math.sqrt(radius*radius-half*half)
               +radius*radius*math.asin(half/radius))
    return math.pi*radius*radius-removed


def centroid(angle=0., rotation_center=(.5, .5), shape_center=(.5, .75),
             radius=.15, slot_width=.05, slot_top=.85):
    """True continuum centroid from closed area and first moments.

    The missing lower-open slot has local first y-moment
    halfwidth*(slot_offset**2-radius**2)+halfwidth**3/3. The whole disk
    has zero local first moments. This is not a cell-center quadrature.
    """
    half, offset = slot_width/2, slot_top-shape_center[1]
    area = total_area(radius, slot_width, offset)
    local_y = (half*(radius*radius-offset*offset)-half**3/3)/area
    delta = np.array(shape_center)-np.array(rotation_center)+np.array((0., local_y))
    c, s = math.cos(angle), math.sin(angle)
    return np.array(rotation_center)+np.array((c*delta[0]-s*delta[1],
                                               s*delta[0]+c*delta[1]))


def inverse_points(x, y, angle=0., rotation_center=(.5, .5)):
    """Physical points mapped back by an exact rigid rotation."""
    c, s = math.cos(angle), math.sin(angle)
    dx, dy = np.asarray(x)-rotation_center[0], np.asarray(y)-rotation_center[1]
    return rotation_center[0]+c*dx+s*dy, rotation_center[1]-s*dx+c*dy


def indicator(x, y, angle=0., rotation_center=(.5, .5), shape_center=(.5, .75),
              radius=.15, slot_width=.05, slot_top=.85):
    x0, y0 = inverse_points(x, y, angle, rotation_center)
    disk = (x0-shape_center[0])**2+(y0-shape_center[1])**2 < radius*radius
    slot = (abs(x0-shape_center[0]) < slot_width/2) & (y0 < slot_top)
    return np.asarray(disk & ~slot, dtype=float)


@lru_cache(maxsize=24)
def _cell_averages_cached(edge_tuple, angle, rotation_center, shape_center,
                          radius, slot_width, slot_top):
    edges = np.array(edge_tuple)
    n = len(edges)-1
    xl, yl = np.meshgrid(edges[:-1], edges[:-1])
    xr, yr = np.meshgrid(edges[1:], edges[1:])
    x = np.stack((xl, xr, xr, xl), axis=-1)
    y = np.stack((yl, yl, yr, yr), axis=-1)
    x0, y0 = inverse_points(x, y, angle, rotation_center)
    local = np.stack((x0-shape_center[0], y0-shape_center[1]), axis=-1)
    r2, half, top = radius*radius, slot_width/2, slot_top-shape_center[1]
    c, s = math.cos(angle), math.sin(angle)
    dx, dy = np.array(shape_center)-np.array(rotation_center)
    cx, cy = np.array(rotation_center)+np.array((c*dx-s*dy, s*dx+c*dy))
    nearest_x = np.maximum(np.maximum(xl-cx, cx-xr), 0.)
    nearest_y = np.maximum(np.maximum(yl-cy, cy-yr), 0.)
    outside = nearest_x**2+nearest_y**2 >= r2
    full_disk = np.max(np.sum(local*local, axis=-1), axis=-1) <= r2
    minimum, maximum = local.min(axis=-2), local.max(axis=-2)
    no_slot = (maximum[..., 0] <= -half) | (minimum[..., 0] >= half) | (minimum[..., 1] >= top)
    full_slot = (minimum[..., 0] >= -half) & (maximum[..., 0] <= half) & (maximum[..., 1] <= top)
    values = np.zeros((n, n))
    values[full_disk & no_slot] = 1.
    mixed = ~outside & ~full_slot & ~(full_disk & no_slot)
    widths = np.diff(edges)
    diagnostics = {'area_cleanup_count': 0, 'maximum_area_cleanup': 0., 'area_cleanup_signed_change': 0.,
                   'fraction_cleanup_count': 0, 'maximum_fraction_cleanup': 0.,
                   'fraction_cleanup_signed_area': 0.,
                   'maximum_raw_fraction_lower_excess': 0., 'maximum_raw_fraction_upper_excess': 0.,
                   'fraction_roundoff_band': 2e-12,
                   'mixed_cells': int(np.count_nonzero(mixed)),
                   'scope': 'Analytic geometric integration only; never PDE-state clipping.'}
    for j, i in np.argwhere(mixed):
        polygon = local[j, i]
        if no_slot[j, i]:
            area = circle_polygon_area(polygon, radius, diagnostics)
        else:
            # Disjoint left, right, and upper-center pieces of disk minus slot.
            left = clip_halfplane(polygon, (1., 0.), -half)
            right = clip_halfplane(polygon, (-1., 0.), -half)
            upper = clip_halfplane(polygon, (-1., 0.), half)
            upper = clip_halfplane(upper, (1., 0.), half)
            upper = clip_halfplane(upper, (0., -1.), -top)
            area = sum(circle_polygon_area(piece, radius, diagnostics) for piece in (left, right, upper))
        fraction = area/(widths[i]*widths[j])
        diagnostics['maximum_raw_fraction_lower_excess'] = max(diagnostics['maximum_raw_fraction_lower_excess'], -fraction)
        diagnostics['maximum_raw_fraction_upper_excess'] = max(diagnostics['maximum_raw_fraction_upper_excess'], fraction-1)
        if not -2e-12 <= fraction <= 1+2e-12:
            raise ArithmeticError('Geometric cell fraction is outside [0,1]')
        cleaned = min(1., max(0., fraction))
        if cleaned != fraction:
            diagnostics['fraction_cleanup_count'] += 1
            diagnostics['maximum_fraction_cleanup'] = max(diagnostics['maximum_fraction_cleanup'], abs(cleaned-fraction))
            diagnostics['fraction_cleanup_signed_area'] += (cleaned-fraction)*widths[i]*widths[j]
        values[j, i] = cleaned
    values.setflags(write=False)
    diagnostics['represented_area'] = float(np.sum(values*np.outer(widths, widths)))
    diagnostics['represented_area_before_fraction_cleanup'] = diagnostics['represented_area']-diagnostics['fraction_cleanup_signed_area']
    diagnostics['represented_area_before_any_cleanup'] = diagnostics['represented_area_before_fraction_cleanup']-diagnostics['area_cleanup_signed_change']
    return values, diagnostics


def cell_averages(edges, angle=0., rotation_center=(.5, .5), shape_center=(.5, .75),
                  radius=.15, slot_width=.05, slot_top=.85):
    """Return q[j,i] conservative cell averages, including arbitrary orientation.

    All coordinates are dimensionless. ``slot_top`` is an unrotated absolute
    y-coordinate. Translate it together with shape_center for a center probe.
    The final tiny geometric bound cleanup concerns analytic integration
    roundoff only. No PDE state is clipped by this module.
    """
    edges = np.asarray(edges, dtype=float)
    args = [angle, *rotation_center, *shape_center, radius, slot_width, slot_top]
    if (edges.ndim != 1 or len(edges) < 2 or not np.all(np.isfinite(edges))
            or np.any(np.diff(edges) <= 0) or not all(np.isfinite(v) for v in args)
            or radius <= 0 or not 0 < slot_width < 2*radius):
        raise ValueError('Require finite increasing edges and valid fixed geometry')
    values, _ = _cell_averages_cached(tuple(edges), float(angle), tuple(rotation_center),
                                     tuple(shape_center), radius, slot_width, slot_top)
    return values.copy()


def cell_average_diagnostics(edges, angle=0., rotation_center=(.5, .5), shape_center=(.5, .75),
                             radius=.15, slot_width=.05, slot_top=.85):
    """Actual analytic-integration roundoff handling, separately from evolution."""
    cell_averages(edges, angle, rotation_center, shape_center, radius, slot_width, slot_top)
    _, diagnostics = _cell_averages_cached(tuple(np.asarray(edges, dtype=float)), float(angle),
                                           tuple(rotation_center), tuple(shape_center),
                                           radius, slot_width, slot_top)
    return dict(diagnostics)
