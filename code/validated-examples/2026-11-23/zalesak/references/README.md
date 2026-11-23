# Independent geometric reference

The primary normalized shape definition is the **Firedrake official DG advection demo**, lines73–79: disk center(0.5,0.75), radius0.15, slot0.475<x<0.525 andy<0.85, within[0,1]². Its velocity is(0.5−y,x−0.5), giving period2π.

This supplement isolates the slotted-cylinder indicator in[0,1] and uses conservative finite volumes with periodic face fluxes. The official demo instead combines the cylinder with a bell and cone, adds background1, usesDQ1 finite elements and prescribes inflow1. It cites LeVeque(1996). The historical Zalesak(1979) publisher record and abstract were checked, but its full original test definition was not accessible. No exact reproduction of either original algorithm, grid or boundary condition is claimed. No Firedrake, Clawpack or ExactPack software is run or copied.

For rotation center`c`, angle`θ=angle0+ωt`, and original indicator`χ₀`, the continuous solution is

`q(x,t)=χ₀(c+R(−θ)(x−c))`.

The finite-volume reference is the integral of this indicator over each cell, divided by cell area. It is **not** the value at the cell center or a rasterized mask. A full turn returns the original cell means; quarter turns additionally check the direction and actual path, which a return-only test cannot establish.

`geometry.py` transforms the four cell vertices into the unrotated shape frame. It partitions disk-minus-slot into disjoint left, right and upper-center convex pieces, clips the polygon by half-planes, and integrates each polygon–circle intersection analytically. Each directed edge is split at circle crossings. Green's theorem yields a triangle contribution inside the circle and a circular-sector contribution outside. Full/empty configurations are resolved geometrically before arc summation.

Let`r`be the disk radius,`h=slot_width/2`and`a=slot_top−shape_center_y`. For the fixed upper slot end inside the disk,

`A=πr²−[2ha+h√(r²−h²)+r²asin(h/r)]`.

The local first moment of the remaining shape is`Mx=0`, `My=h(r²−a²)−h³/3`. Divide by`A`, translate to the shape center, and rigidly rotate to obtain the **true continuum centroid**. Weighting cell means by cell-center coordinates only approximates this continuum centroid and has its own discretization error; those two quantities are kept separate.

`qualify_reference.qualify()` contains eight checks fixed before scientific execution:

1. Analytic polygon partitions sum to the closed area on geometry grids32/64/128/256, an oblique orientation, a quarter turn and a half-cell translation. The32-grid reference check from the original attempt is retained even though the revised PDE family uses64/128/256.
2. Twelve fixed cut-cell fractions agree with independent vertical-section integration by SciPy1.14.1`quad`.
3. Whole-shape adaptive quadrature agrees with the closed area.
4. Independently integrated true first moments agree with the closed centroid at three orientations.
5. Full-turn conservative cell means return.
6. A quarter turn matches the correctly oriented array rotation.
7. Fraction roundoff cleanup stays within its declared2e−12 dimensionless band.
8. Dimensional area cleanup stays within128 machine-epsilon timesradius².

The independent quadrature uses circular vertical intervals and three linear slot inequalities. It shares no polygon clipping, Green/sector primitive, finite-volume flux or rasterization with the analytic-area implementation. Its break points include line/circle intersections, and the requested tolerances and reported quadrature errors are retained. Numerical agreement is evidence for these fixed geometries, not an interval-arithmetic proof for all inputs.

Geometric floating-point cleanup is recorded separately from PDE evolution: counts, maximum raw lower/upper excess, signed area changes, and represented area before/after cleanup are saved. Only the analytic initializer/reference has these tiny bound restorations. The PDE evolves its raw states without clipping or retry, with a separately declared5e−13 stage roundoff band.

The exact support stays within radius0.4 of the rotation center and away from the periodic seams, also for the fixed translation probe. The globally periodic velocity extension has tangential jumps at seams; it is not a smooth periodic solid-body field. Coarse-grid numerical tails can reach the seams, so a fixed physical boundary-band diagnostic is saved.

Source roles and actual inspection scope are in[citations.json](citations.json)and[source-review.json](source-review.json). The mathematical evaluator and qualification code are new standalone source under the supplement's MIT code license. No third-party article PDF or program source is redistributed.
