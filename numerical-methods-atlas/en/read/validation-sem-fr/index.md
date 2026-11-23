# Spectral elements and FR: small comparisons with existing FEM/DG

Compare2D SEM Poisson and1D periodic FR advection with the existing P1 FEM/modal DG under matched equations, boundaries and analytic fields. Separate h/p refinement, continuous error, residuals, conservation and time error from any external Nek/PyFR execution.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## 2D spectral-element Poisson: P1 FEM comparison and h/p refinement

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

**Methods used**

- [Spectral element method (SEM)](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en) (`spectral-element`)
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-algorithm)

C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.


**Problem figure**

![2D spectral-element Poisson: P1 FEM comparison and h/p refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-validation)

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
### Assumptions, units and boundaries

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

### Adopted numerical method

C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

### References and validation

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

### Limits

One smooth fixed problem only. Meshes, quadrature and algebraic solvers differ: no speed, complexity or universal-accuracy ranking. The diagonal GLL quadrature mass is not the exactly integrated mass of every product. No curved mesh, singular solution, incompressible flow or Nek5000/nekRS run.

### Stored measurements and decisions

```json
{
  "metrics": {
    "sem_h_l2_order": 3.0396439861149207,
    "sem_h_h1_order": 2.010636067947865,
    "p1_h_l2_order": 1.9744920294804964,
    "p1_h_h1_order": 0.9891011038360976,
    "p_refinement_l2_reduction": 311080.7699512155,
    "p6_l2_error": 3.7801651652951424e-07,
    "same_dof_free_unknowns": 225,
    "sem_finest_l2_error": 0.0002486410968007461,
    "p1_finest_l2_error": 0.005377435009938097,
    "same_dof_l2_ratio_sem_over_p1": 0.046237861794931924,
    "maximum_relative_residual": 3.1814596822002824e-12
  },
  "checks": {
    "sem_h_l2_convergence": true,
    "sem_h_h1_convergence": true,
    "p1_h_l2_convergence": true,
    "p1_h_h1_convergence": true,
    "p_refinement_monotone": true,
    "p_refinement_resolved": true,
    "equal_free_dofs": true,
    "same_dof_error_comparison": true,
    "linear_residuals": true,
    "zero_dirichlet_boundary": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/index.json

![Saved actual2D SEM field and nodal error. Continuous error norms use separate Gauss integration.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d-preview.png)

Saved actual2D SEM field and nodal error. Continuous error norms use separate Gauss integration.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

### Sources and review scope

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://nek5000.github.io/NekDoc/references.html; review_level=metadata
  Bibliographic identity from the official Nek5000 reference list; publisher full text was not retrieved. No original-paper audit/reproduction. This example is a Legendre GLL variant.
- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html; review_level=full-text
  Official Theory and FAQ: element-local polynomials, GLL/GL nodes and C0 continuity. No installation, execution or full-code audit of Nek5000.
- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/; review_level=full-text
  Official project overview: SEM, CPU/GPU nekRS and its relationship to Nek5000. No external solver installation, execution or performance comparison.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 1D periodic FR advection: Radau correction and published DG comparison

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

**Methods used**

- [Flux reconstruction (FR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en) (`flux-reconstruction`)
- [Discontinuous Galerkin / Legendre](https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en) (`dg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-algorithm)

p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.


**Problem figure**

![1D periodic FR advection: Radau correction and published DG comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-validation)

Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference · Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference · Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference · Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
### Assumptions, units and boundaries

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

### Adopted numerical method

p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

### References and validation

Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.

### Limits

DG correspondence is for these Radau/Gauss choices, a constant linear flux and affine elements. No all-FR/all-DG equivalence, nonlinear flux, shock, limiter or multidimensional FR claim. Distinguish coupled h/dt refinement from the exponential spatial result; the exponential is not an independent spatial PDE solver. PyFR itself is not run.

### Stored measurements and decisions

```json
{
  "metrics": {
    "p1_l2_order": 1.9917679206568963,
    "p1_exponential_l2_order": 1.991760641915898,
    "p2_l2_order": 2.999596193727679,
    "p2_exponential_l2_order": 2.9995943579113864,
    "finest_l2_error": 2.6116268430230035e-05,
    "maximum_fr_vs_published_dg": 3.9968028886505635e-15,
    "maximum_stage_mass_drift": 3.552713678800501e-15,
    "maximum_step_energy_increase": 0.0,
    "maximum_scaled_courant": 0.15,
    "finest_rk3_time_error": 9.442398008716171e-09,
    "halved_cfl_time_error": 1.1816779053955014e-09,
    "time_error_halving_ratio": 0.12514595384612126,
    "actual_transport_l2_change": 0.9999999629484513
  },
  "checks": {
    "p1_l2_convergence": true,
    "p2_l2_convergence": true,
    "semidiscrete_spatial_convergence": true,
    "finest_analytic_error": true,
    "published_dg_agreement": true,
    "periodic_stage_mass": true,
    "nonincreasing_step_energy": true,
    "scaled_courant_bound": true,
    "time_error_control": true,
    "nontrivial_translation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/index.json

![Saved FR initial/final field and analytic nodal error; actual transport atT=.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection-preview.png)

Saved FR initial/final field and analytic nodal error; actual transport atT=.25.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

### Sources and review scope

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=metadata
  Original 2007 title/author/AIAA number checked in the author's 2014 NASA report, printed p.27. The original AIAA text was not retrieved; correction formulas use the separately cited 2014 report.
- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=full-text
  Selected original NASA passages: abstract, differential form/interface correction, printed pp.19–21 equations(6.2)–(6.13) for Radau/DG, and p.27 bibliography. No full-report audit or nonlinear experiment reproduction.
- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/; review_level=full-text
  Official overview: FR spatial discretization, unstructured meshes and CPU/GPU platforms. PyFR is not installed, invoked or validated by this small Python example.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
