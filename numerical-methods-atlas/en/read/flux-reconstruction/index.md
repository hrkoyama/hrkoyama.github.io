# Flux reconstruction: flux correction, DG and 1D periodic advection

Flux reconstruction: flux correction, DG and 1D periodic advection

Flux reconstruction (FR) builds high-order conservation-law discretizations by correcting a polynomial flux inside each element with shared interface fluxes. Elements exchange information through numerical fluxes rather than enforcing a continuous solution. The correction function is part of the method definition; the name FR alone specifies neither accuracy nor stability.

Separate solution points from numerical interface fluxes


$$
u_t+a u_x=0,\quad x\in[0,1),\quad u(x+1,t)=u(x,t),\quad u_*(x,t)=0.4+\sin(2\pi(x-at))
$$

$$
u_h(\xi)=\sum_{j=0}^{p}u_j\ell_j(\xi),\qquad f^D(\xi)=\sum_{j=0}^{p}f(u_j)\ell_j(\xi)
$$
Map each interval to ξ in [−1,1] and store values at p+1 solution points. Extrapolation to a face gives two traces from neighboring elements. For this constant-speed problem choose the left state when a>0 and the right state when aConnect face fluxes with correction functions


$$
f^C(\xi)=f^D(\xi)+(f_L^*-f_L^D)g_L(\xi)+(f_R^*-f_R^D)g_R(\xi)
$$

$$
g_L(-1)=1,\ g_L(1)=0,\qquad g_R(-1)=0,\ g_R(1)=1,\qquad\dot u_i=-\frac{2}{h}\partial_\xi f^C(\xi_i)
$$
Here fD is the element-local flux polynomial and f* is the shared numerical flux. Distribute their face differences using gL/gR so that the corrected flux matches f* at the endpoints. Differentiate it at the solution points to evolve the state. Distinguish these unknowns and flux corrections from the different reconstruction procedures in MUSCL/WENO.

A Radau choice that recovers DG


$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\qquad g_R=\frac12(P_p+P_{p+1})
$$

$$
M\dot{\mathbf u}=\frac{2}{h}\left[aD^TM\mathbf u-\mathbf t_R f_R^*+\mathbf t_L f_L^*\right],\qquad M=\operatorname{diag}(w_i)
$$
Use Gauss solution points and the displayed Radau corrections. M is the diagonal Gauss-weight matrix, tL/tR extrapolate to faces and D differentiates on the reference interval. For a constant linear flux on affine intervals, this FR formulation corresponds to nodal DG. Modal Legendre coefficients represent the same polynomial when initial projection, flux and time stepping match. Nonlinear flux aliasing, other quadratures and other corrections require separate conditions.

Comparison with the existing modal DG



Comparison with the existing modal DG

| Aspect | This FR | Published modal DG |
| --- | --- | --- |
| Unknowns | p+1 Gauss-point values | p+1 Legendre coefficients |
| Coupling | Radau corrections of face-flux differences | Weak-form volume and face fluxes |
| Initialization | Common Gauss L2 projection | Same projection rule |
| Time integration | SSPRK(3,3) | Same SSPRK(3,3) and timestep rule |
| Meaning of this comparison | Check a specified linear correspondence | Actually execute the existing implementation |
| Limits | Not all corrections or nonlinear FR | Not equivalence with every DG variant |

Small example: translate a sine by a quarter period

Initial 0.4+sin(2pi x), speed 1, T=.25; execute p=1/2 on 8/16/32 cells. Bundle byte-identical published DG modules and run each configuration. During h refinement enforce scaled Courant(2p+1)|a|dt/h[](/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)Saved initial/final fields and checks. DG differences and mass changes are displayed on axes at the scale of 10⁻¹⁵ roundoff.Separate conservation, dissipation and time error


$$
I_h=\sum_e\frac{h}{2}\sum_iw_iu_{e,i},\quad \frac{dI_h}{dt}=0,\qquad \frac{d}{dt}\frac12\|u_h\|_{L^2}^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$
Shared face fluxes cancel in the periodic mass balance. The semidiscrete quadratic energy dissipates with interface jumps under upwinding. This does not guarantee stability at arbitrary timesteps or nonlinear entropy stability. Also measure every RK stage’s mass and each completed step’s energy.


$$
\dot U=A_hU,\quad U_{\exp}(T)=\exp(TA_h)U(0),\quad E_t=\|U_{\rm RK3}(T)-U_{\exp}(T)\|_M
$$
Continuous L2 errors use additional Gauss points. Coupled h/dt observed orders are about 1.99 at p1 and 3.00 at p2. The maximum FR/published-DG difference is about 4.0e−15; maximum stage mass change is about 3.6e−15.

Compute an exponential action of the same spatial matrix as a separate time propagator. At p2/N32, RK3 time error is about 9.44e−9 and halves in timestep to 1.18e−9, a ratio about.125. This is not an independent spatial PDE solver. Preserve the initial dense-exponential warning and subsequent JSON scalar-type failure with their original source/input/results; fixes retain every numerical acceptance threshold.

Related implementation: PyFR and scope

[PyFR](https://www.pyfr.org/) is FR-based flow software supporting unstructured meshes and CPU/GPU execution. Follow its official overview and [source](https://github.com/PyFR/PyFR). This small Python example neither installs nor runs or benchmarks PyFR. Nonlinear fluxes, shocks, limiters, general correction families, curved meshes and multidimensional FR require separate verification.

[Existing discontinuous Galerkin method](/numerical-methods-atlas/methods/dg/?lang=en) · [Continuous spectral elements](/numerical-methods-atlas/en/read/spectral-element/)

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### 1D periodic FR advection: Radau correction and published DG comparison

Fixed-target computation

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

DG correspondence is for these Radau/Gauss choices, a constant linear flux and affine elements. No all-FR/all-DG equivalence, nonlinear flux, shock, limiter or multidimensional FR claim. Distinguish coupled h/dt refinement from the exponential spatial result; the exponential is not an independent spatial PDE solver. PyFR itself is not run.

[Input, results and acceptance](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-sem-fr/#fr-periodic-advection) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py) · [Code fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) · [Code polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py) · [Code advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py) · [Code riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py) · [Code equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py) · [Code limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py) · [Code sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) · [Code fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py) · [Code krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py) · [Tests test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py) · [ZIP](/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [Results](/code/validated-examples/2026-11-23/sem-fr/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-23/sem-fr/verification.json)

## Publication scope

Dedicated small code, fixed inputs, saved fields and decisions are published with25 tests rerun from an independently extracted ZIP. Related external software is introduced from official documentation, without claiming installation or execution.

## Sources

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://doi.org/10.2514/6.2007-4079
- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf
- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/
