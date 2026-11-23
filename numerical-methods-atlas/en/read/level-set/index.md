# Level sets: moving interfaces and comparison with VOF

Level sets: moving interfaces and comparison with VOF

A level set embeds a curve or surface as the zero contour of a grid function and evolves that function. It connects transport, Hamilton–Jacobi equations and interface geometry, with a representation that naturally accommodates merging and splitting. Start with the equations, then inspect small reproducible two-dimensional circle motions.

Represent the interface by phi=0


$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi0\;\text{outside}
$$
Here the interior is negative and the exterior positive. Function values are neither fluid density nor volume fraction. A monotone transformation retaining the zero set leaves the interface unchanged while changing gradients and numerical behavior. Some sources reverse the sign; normals and normal speeds must use the same convention.

An interface transported by a velocity


$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$
Differentiate the condition that phi is constant along a trajectory moving with velocity u to obtain the transport equation. Prescribed-velocity interface transport differs from solving coupled two-phase velocities and pressure. Upwind differences, ENO/WENO and time integration discretize this equation; they are choices in addition to the interface representation.

Normals, curvature and normal motion


$$
\phi_t+V_n\|\nabla\phi\|=0,\qquad\mathbf{n}=\frac{\nabla\phi}{\|\nabla\phi\|},\quad\kappa=\nabla\cdot\mathbf{n}
$$

$$
\phi(\mathbf{x})=\operatorname{sgn}(\phi)\operatorname{dist}(\mathbf{x},\Gamma),\qquad\|\nabla\phi\|=1\quad\text{where differentiable}
$$
With a negative interior the normal points outward; the two-dimensional circle has kappa=1/r in this convention. A prescribed normal speed gives a Hamilton–Jacobi equation. A signed distance has unit gradient where differentiable; circle centers and points with nonunique nearest interfaces need not be smooth. Diagnostics therefore focus on a band near the interface; curvature-driven motion is explained but not executed here.

What redistancing repairs and can change


$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad\psi(\mathbf{x},0)=\phi_0(\mathbf{x}),\quad S_\epsilon(z)=\frac{z}{\sqrt{z^2+\epsilon^2}}
$$
General advection need not retain a distance function. An auxiliary pseudo-time tau equation can restore distance quality without advancing physical time t. Preserving an ideal zero set does not guarantee an interpolated discrete interface stays fixed. The example uses first-order Godunov iterations with sign frozen per call; it is not the constrained higher-order Sussman–Fatemi scheme, and no position or area improvement is assumed.

VOF: geometry and a volume balance


$$
F_K=\frac1{|K|}\int_K H(-\phi)\,d\mathbf{x},\quad0\le F_K\le1,\qquad\nabla\cdot\mathbf{u}=0:\quad F_t+\nabla\cdot(F\mathbf{u})=0
$$

$$
F_K^{n+1}=F_K^n-\frac{\Delta t}{|K|}\sum_{f\subset\partial K}|f|\widehat{\mathcal F}_{K,f},\quad\sum_K|K|F_K^{n+1}=\sum_K|K|F_K^n-\text{boundary flux}
$$
Comparison of formulations, conservation and implementation scopeAspectLevel setVOFStored quantitySigned function phi; interface phi=0Cell fluid-volume fraction FGeometryNormals/curvature from derivatives of phiInterface reconstruction and geometry from fractionsConservationOrdinary transport/redistancing does not guarantee enclosed volumeConservative shared face fluxes provide a volume balanceNumerical issuesDistance distortion; interface/volume driftCheck bounds, reconstruction and curvature separatelyCombinationCLSVOF couples distance-like geometry and conservative fractionsThe particular coupling needs its own consistency/error checksThis additionCircle advection/rotation examples and22 testsConceptual comparison; no VOF numerical experimentFor a prescribed incompressible velocity, volume fractions admit conservative transport. Cancellation of shared interior face fluxes gives a global balance with boundary fluxes. Bounds0Small 2D examples: translation and off-center rotation


$$
\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-r,\quad \mathbf{c}_{\rm tr}(t)=\mathbf{c}_0+t\mathbf{v},\quad\mathbf{c}_{\rm rot}(t)=\mathbf{x}_c+R(\omega t)(\mathbf{c}_0-\mathbf{x}_c)
$$
Radius.15 on the unit square, T=1. Translation starts at(.3,.35) with velocity(.2,.1). Rotation carries a circle centered at(.68,.5) once about(.5,.5), at angular speed2pi. ENO2 one-sided differences and Heun RK2 use32²/64²/128² grids and Courant numberBoth cases compare advection alone against five redistancing pseudo-steps every.1 physical time. Observe0/.25/.5/.75/1; the rotation checks intermediate displacement as well as full-turn return.

[](/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)Finest-grid contours from saved2D fields: black analytic final interface, orange advection only, dashed teal redistancing, dotted gray initial interface.What the error measurements mean


$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\big|\|\mathbf{z}-\mathbf{c}(t)\|-r\big|,\quad p_{\rm obs}=\log_2\!\left(E_\Gamma(h)/E_\Gamma(h/2)\right)
$$
Z_h contains linearly interpolated grid-edge zero crossings; E_Gamma is the maximum radial error at these samples, not a continuous-interface Hausdorff distance. Geometric area clips linear phi on triangles and compares against pi*r², retaining initial geometric bias. Coupled grid/time refinement of advection alone observes about1.90 for translation and2.02 for rotation. SeparateN64 CFL-halving sensitivity is recorded; this is not a proof of pure spatial order.

Finest-grid worst relative area error changes about0.22% to0.93% for translation and1.06% to2.02% for rotation, from advection alone to redistancing. The simple redistancing increases error in these fixed runs. Distance-gradient quality, zero-interface accuracy and enclosed-volume balance are distinct diagnostics.

Scope and related reading

This release transports circles in prescribed velocities. It does not validate topology changes, curvature flow, surface tension or two-phase flow, nor benchmark VOF performance. Downloads retain analytic reference formulas, full2D final fields, intermediate interface samples, CSV, input hashes, all decisions and each redistancing area change. The existing Zalesak slotted-disk material is a separate conservative scalar-transport example; its code is not relabeled as a VOF implementation.

[Zalesak-type conservative2D rotational transport](/numerical-methods-atlas/en/read/validation-zalesak/) · [ENO/WENO](/numerical-methods-atlas/en/read/benchmarks/)

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### 2D level-set circle translation: interface, area and redistancing

Fixed-target computation

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

[Input, results and acceptance](/numerical-methods-atlas/validation/level-set-translation/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-level-set/#level-set-translation) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py) · [Code level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py) · [Code geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py) · [Tests test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py) · [ZIP](/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [Results](/code/validated-examples/2026-11-23/level-set/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-23/level-set/verification.json)

### 2D rigid rotation of an off-center level-set circle

Fixed-target computation

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

[Input, results and acceptance](/numerical-methods-atlas/validation/level-set-rotation/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-level-set/#level-set-rotation) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py) · [Code level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py) · [Code geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py) · [Tests test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py) · [ZIP](/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [Results](/code/validated-examples/2026-11-23/level-set/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-23/level-set/verification.json)

## Publication scope

The level-set implementation is limited to educational2D circle translation/rotation; VOF has comparison reading only. The dedicated ZIP is independently extracted and its22 tests and every fixed input rerun. The common22 examples, historical releases and existing success records are preserved.

## Sources

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://doi.org/10.1016/0021-9991(88)90002-2
- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://doi.org/10.1016/0021-9991(81)90145-5
- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://doi.org/10.1137/S1064827596298245
- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://doi.org/10.1006/jcph.2000.6537
