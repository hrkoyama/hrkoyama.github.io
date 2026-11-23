"""Independent analytic-geometry checks; no PDE or image rasterization."""
import math
import numpy as np
from scipy.integrate import quad
from . import geometry as g


def _quad_moments(rect, angle=0., rotation_center=(.5, .5), shape_center=(.5, .75),
                  radius=.15, slot_width=.05, slot_top=.85):
    """Independent vertical slicing and adaptive 1D integration.

    At fixed physical x, intersect the circular y-interval with the cell and
    the three linear slot constraints. This shares no polygon clipping,
    sector integrals, or rasterization with geometry.cell_averages.
    """
    left, right, bottom, top = rect
    c, s = math.cos(angle), math.sin(angle)
    delta = np.array(shape_center)-np.array(rotation_center)
    cx, cy = np.array(rotation_center)+np.array((c*delta[0]-s*delta[1], s*delta[0]+c*delta[1]))
    half, offset = slot_width/2, slot_top-shape_center[1]
    lines = [(s, c, half), (-s, -c, half), (c, -s, offset)]
    start, finish = max(left, cx-radius), min(right, cx+radius)
    if finish <= start:
        return np.zeros(3), 0.
    breaks = [start, finish, cx]
    for yy in [bottom, top]:
        distance = radius*radius-(yy-cy)**2
        if distance >= 0:
            root = math.sqrt(distance)
            breaks += [cx-root, cx+root]
    # Intersections among slot lines and with the cell's horizontal edges.
    for a, b, bound in lines:
        if abs(b) > 1e-14:
            for yy in [bottom, top]:breaks.append(cx+(bound-a*(yy-cy))/b)
        if abs(b) <= 1e-14:
            continue
    for i, (a, b, bound) in enumerate(lines):
        for aa, bb, other in lines[i+1:]:
            determinant = b*aa-bb*a
            if abs(determinant) > 1e-14:
                xx = (bound*aa-other*a)/determinant
                breaks.append(cx+xx)
        # Parametric intersections of each straight slot boundary and disk.
        # a*y+b*x=bound in coordinates relative to the rotated disk center.
        norm2 = a*a+b*b
        distance2 = bound*bound/norm2
        if distance2 <= radius*radius:
            foot = np.array((b, a))*bound/norm2
            tangent = np.array((-a, b))/math.sqrt(norm2)
            extent = math.sqrt(radius*radius-distance2)
            breaks += [cx+foot[0]-extent*tangent[0], cx+foot[0]+extent*tangent[0]]
    breaks = sorted(set(x for x in breaks if start < x < finish))
    def lengths(x):
        extent = math.sqrt(max(0., radius*radius-(x-cx)**2))
        lo, hi = max(bottom, cy-extent), min(top, cy+extent)
        if hi <= lo:
            return 0., 0.
        slow, shigh = lo, hi
        for a, b, bound in lines:
            remaining = bound-b*(x-cx)
            if abs(a) < 1e-14:
                if remaining < 0:
                    slow, shigh = 1., 0.;break
            elif a > 0:
                shigh = min(shigh, cy+remaining/a)
            else:
                slow = max(slow, cy+remaining/a)
        slot_length = max(0., shigh-slow)
        slot_moment = .5*(shigh*shigh-slow*slow) if shigh > slow else 0.
        return hi-lo-slot_length, .5*(hi*hi-lo*lo)-slot_moment
    values, errors = [], []
    for component in range(3):
        def integrand(x):
            length, y_moment = lengths(x)
            return length if component == 0 else x*length if component == 1 else y_moment
        absolute_target = min(2e-14, 1e-13*(right-left)*(top-bottom))
        value, error = quad(integrand, start, finish, points=breaks,
                            epsabs=absolute_target, epsrel=2e-13, limit=160)
        values.append(value);errors.append(error)
    return np.array(values), max(errors)


def qualify():
    """Eight predeclared checks; thresholds are independent of PDE outcomes."""
    checks, metrics = {}, {}
    expected = g.total_area()
    area_errors, guard_rows = [], []
    for n, angle, shift in [(32, 0., 0.), (64, 0., 0.), (128, 0., 0.), (256, 0., 0.),
                             (64, math.pi/4, 0.), (64, math.pi/2, 0.), (64, 0., .5/64)]:
        edges = np.linspace(0., 1., n+1)
        kwargs = dict(angle=angle, rotation_center=(.5+shift, .5+shift),
                      shape_center=(.5+shift, .75+shift), slot_top=.85+shift)
        q = g.cell_averages(edges, **kwargs)
        area_errors.append(abs(float(np.sum(q))/n**2-expected))
        guard_rows.append({'n': n, 'angle': angle, 'shift': shift,
                           **g.cell_average_diagnostics(edges, **kwargs)})
    metrics['closed_total_area'] = expected
    metrics['maximum_partition_total_area_error'] = max(area_errors)
    checks['analytic circle partitions conserve closed total area'] = max(area_errors) <= 3e-12

    cuts = [(0., 31, 38), (0., 31, 54), (0., 41, 48), (0., 31, 57),
            (0., 40, 52), (0., 32, 48), (math.pi/4, 30, 43),
            (math.pi/4, 20, 52), (math.pi/4, 17, 48),
            (math.pi/4, 15, 46), (math.pi/4, 14, 39), (math.pi/4, 20, 43)]
    edges = np.linspace(0., 1., 65)
    spot_rows = []
    for angle, i, j in cuts:
        exact = g.cell_averages(edges, angle=angle)[j, i]
        moments, error = _quad_moments((edges[i], edges[i+1], edges[j], edges[j+1]), angle)
        independent = moments[0]*64**2
        spot_rows.append({'angle': angle, 'i': i, 'j': j,
                          'analytic_fraction': float(exact), 'quad_fraction': float(independent),
                          'absolute_difference': abs(float(exact-independent)),
                          'quad_reported_absolute_error': error})
    metrics['cut_cells'] = spot_rows
    metrics['maximum_independent_cut_cell_difference'] = max(x['absolute_difference'] for x in spot_rows)
    checks['twelve fixed cut cells agree with independent vertical quadrature'] = metrics['maximum_independent_cut_cell_difference'] <= 3e-12

    continuum_rows = []
    for angle in [0., math.pi/4, math.pi/2]:
        moments, error = _quad_moments((0., 1., 0., 1.), angle)
        centroid = moments[1:]/moments[0]
        continuum_rows.append({'angle': angle, 'quad_area': float(moments[0]),
                               'quad_centroid': centroid.tolist(),
                               'analytic_centroid': g.centroid(angle=angle).tolist(),
                               'area_difference': abs(float(moments[0]-expected)),
                               'centroid_maximum_difference': float(abs(centroid-g.centroid(angle=angle)).max()),
                               'quad_reported_absolute_error': error})
    metrics['continuum_moments'] = continuum_rows
    checks['independent whole-area quadrature agrees with closed area'] = max(x['area_difference'] for x in continuum_rows) <= 3e-12
    checks['true analytic centroid agrees with independent first moments'] = max(x['centroid_maximum_difference'] for x in continuum_rows) <= 3e-12

    initial = g.cell_averages(edges)
    full = g.cell_averages(edges, angle=2*math.pi)
    quarter = g.cell_averages(edges, angle=math.pi/2)
    metrics['full_turn_maximum_cell_mean_difference'] = float(abs(initial-full).max())
    metrics['quarter_turn_maximum_array_rotation_difference'] = float(abs(quarter-np.rot90(initial, -1)).max())
    checks['full-turn geometric cell means return'] = metrics['full_turn_maximum_cell_mean_difference'] <= 3e-12
    checks['quarter-turn geometry has the correct counterclockwise orientation'] = metrics['quarter_turn_maximum_array_rotation_difference'] <= 3e-12

    metrics['geometry_roundoff_diagnostics'] = guard_rows
    checks['geometric fraction roundoff cleanup remains within its separate band'] = all(x['maximum_fraction_cleanup'] <= 2e-12 for x in guard_rows)
    checks['analytic area cleanup remains within its dimensional floating-point band'] = all(x['maximum_area_cleanup'] <= 128*np.finfo(float).eps*.15**2 for x in guard_rows)
    return {'checks': checks, 'metrics': metrics,
            'scope': 'Independent analytic geometry qualification, not a PDE solver. True first moments are distinct from cell-center centroid quadrature. No Firedrake software was executed.'}
