# Corner singularities, curved coordinates and Neumann/Robin boundaries

Actually solve singular L-corner P1 FEM, annular variable-viscosity vector Q1 PDE, pure-Neumann compatibility/mean-gauge and mixed-Robin manufactured problems.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## L-corner P1 FEM: grading and separate mesh distortion

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.

**Methods used**

- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-algorithm)

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.


**Problem figure**

![L-corner P1 FEM: grading and separate mesh distortion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-validation)

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

- [L-corner singularity: harmonic field and separate smooth MMS](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en) (`lshape-fem`; Same-problem reference · Analytic reference)

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
### Assumptions, units and boundaries

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.

**Editorial clarification**

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

### Adopted numerical method

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

### References and validation

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

### Limits

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 32,
    "dofs": 961,
    "l2": 0.00134735733393484,
    "h1": 0.10884489368256302,
    "quadrature_relative_gap": 1.40015698331148e-14,
    "minimum_area": 0.00047869957157375606,
    "minimum_angle_degrees": 43.597518748367705,
    "maximum_aspect": 2.084333006036921,
    "condition_one_norm_estimate": 627.0284248525954,
    "residual": 1.6514567491299204e-15,
    "boundary_error": 0.0,
    "symmetry": 0.0
  },
  "checks": {
    "uniform-n8 residual": true,
    "uniform-n8 boundary_error": true,
    "uniform-n8 symmetry": true,
    "uniform-n8 quadrature_relative_gap": true,
    "uniform-n8 positive geometry": true,
    "uniform-n16 residual": true,
    "uniform-n16 boundary_error": true,
    "uniform-n16 symmetry": true,
    "uniform-n16 quadrature_relative_gap": true,
    "uniform-n16 positive geometry": true,
    "uniform-n32 residual": true,
    "uniform-n32 boundary_error": true,
    "uniform-n32 symmetry": true,
    "uniform-n32 quadrature_relative_gap": true,
    "uniform-n32 positive geometry": true,
    "graded-n8 residual": true,
    "graded-n8 boundary_error": true,
    "graded-n8 symmetry": true,
    "graded-n8 quadrature_relative_gap": true,
    "graded-n8 positive geometry": true,
    "graded-n16 residual": true,
    "graded-n16 boundary_error": true,
    "graded-n16 symmetry": true,
    "graded-n16 quadrature_relative_gap": true,
    "graded-n16 positive geometry": true,
    "graded-n32 residual": true,
    "graded-n32 boundary_error": true,
    "graded-n32 symmetry": true,
    "graded-n32 quadrature_relative_gap": true,
    "graded-n32 positive geometry": true,
    "square-n8 residual": true,
    "square-n8 boundary_error": true,
    "square-n8 symmetry": true,
    "square-n8 quadrature_relative_gap": true,
    "square-n8 positive geometry": true,
    "square-n16 residual": true,
    "square-n16 boundary_error": true,
    "square-n16 symmetry": true,
    "square-n16 quadrature_relative_gap": true,
    "square-n16 positive geometry": true,
    "square-n32 residual": true,
    "square-n32 boundary_error": true,
    "square-n32 symmetry": true,
    "square-n32 quadrature_relative_gap": true,
    "square-n32 positive geometry": true,
    "warped-n8 residual": true,
    "warped-n8 boundary_error": true,
    "warped-n8 symmetry": true,
    "warped-n8 quadrature_relative_gap": true,
    "warped-n8 positive geometry": true,
    "warped-n16 residual": true,
    "warped-n16 boundary_error": true,
    "warped-n16 symmetry": true,
    "warped-n16 quadrature_relative_gap": true,
    "warped-n16 positive geometry": true,
    "warped-n32 residual": true,
    "warped-n32 boundary_error": true,
    "warped-n32 symmetry": true,
    "warped-n32 quadrature_relative_gap": true,
    "warped-n32 positive geometry": true,
    "uniform l2 refinement 1": true,
    "uniform l2 refinement 2": true,
    "uniform h1 refinement 1": true,
    "uniform h1 refinement 2": true,
    "graded l2 refinement 1": true,
    "graded l2 refinement 2": true,
    "graded h1 refinement 1": true,
    "graded h1 refinement 2": true,
    "square l2 refinement 1": true,
    "square l2 refinement 2": true,
    "square h1 refinement 1": true,
    "square h1 refinement 2": true,
    "warped l2 refinement 1": true,
    "warped l2 refinement 2": true,
    "warped h1 refinement 1": true,
    "warped h1 refinement 2": true,
    "matched unknown counts": true,
    "finest graded/uniform H1": true,
    "finest graded H1": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

### Sources and review scope

- Long Chen (n.d.). Introduction to Adaptive Finite Element Methods. https://lyc102.github.io/ifem/afem/; review_level=selected-official-tutorial-equations
- Joachim Schöberl (n.d.). Interactive FEM: graded meshes around vertex singularities. https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html; review_level=selected-author-teaching-section

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Annular variable-viscosity vector PDE MMS

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.

**Methods used**

- [Q1 FEM for mapped-coordinate vector BVP](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-algorithm)

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [Variable-viscosity vector stress boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en) (`variable-viscosity-vector`)

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.


**Problem figure**

![Annular variable-viscosity vector PDE MMS: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-validation)

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

- [Annular vector-viscous MMS: force qualified by independent stress differentiation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en) (`annular-viscous-mms`; Same-problem reference · Manufactured solution)

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
### Assumptions, units and boundaries

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.

**Editorial clarification**

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

### Adopted numerical method

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

### References and validation

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

### Limits

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 32,
    "theta_cells": 64,
    "dofs": 3968,
    "relative_l2": 0.0022683900910951296,
    "relative_strain_l2": 0.05188955686190023,
    "relative_traction_l2": 0.07266006943162176,
    "residual": 1.0857981180834031e-13,
    "boundary_error": 0.0,
    "area_error": 3.552713678800501e-15,
    "reaction_balance": 1.736671818881876e-15,
    "traction_flux_balance": 0.042495559851796386,
    "exact_flux_balance": 5.984756355647655e-16,
    "analytic_force_error": 8.394500285269018e-16,
    "work_identity": 3.851517252670248e-15,
    "symmetry": 3.552713678800501e-15
  },
  "checks": {
    "annulus-n8 residual": true,
    "annulus-n8 boundary_error": true,
    "annulus-n8 area_error": true,
    "annulus-n8 reaction_balance": true,
    "annulus-n8 exact_flux_balance": true,
    "annulus-n8 analytic_force_error": true,
    "annulus-n8 work_identity": true,
    "annulus-n8 symmetry": true,
    "annulus-n16 residual": true,
    "annulus-n16 boundary_error": true,
    "annulus-n16 area_error": true,
    "annulus-n16 reaction_balance": true,
    "annulus-n16 exact_flux_balance": true,
    "annulus-n16 analytic_force_error": true,
    "annulus-n16 work_identity": true,
    "annulus-n16 symmetry": true,
    "annulus-n32 residual": true,
    "annulus-n32 boundary_error": true,
    "annulus-n32 area_error": true,
    "annulus-n32 reaction_balance": true,
    "annulus-n32 exact_flux_balance": true,
    "annulus-n32 analytic_force_error": true,
    "annulus-n32 work_identity": true,
    "annulus-n32 symmetry": true,
    "relative_l2 refinement 1": true,
    "relative_l2 refinement 2": true,
    "relative_strain_l2 refinement 1": true,
    "relative_strain_l2 refinement 2": true,
    "relative_traction_l2 refinement 1": true,
    "relative_traction_l2 refinement 2": true,
    "traction_flux_balance refinement 1": true,
    "traction_flux_balance refinement 2": true,
    "finest relative_l2": true,
    "finest relative_strain_l2": true,
    "finest relative_traction_l2": true,
    "finest traction_flux_balance": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

### Sources and review scope

- MFEM developers (n.d.). Example2: Linear Elasticity. https://mfem.org/examples/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Pure Neumann compatibility and mean gauge

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-algorithm)

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.


**Problem figure**

![Pure Neumann compatibility and mean gauge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-validation)

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

- [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en) (`poisson-neumann`; Same-problem reference · Manufactured solution)

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
### Assumptions, units and boundaries

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.

**Editorial clarification**

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

### Adopted numerical method

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

### References and validation

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

### Limits

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.0004017888396835558,
    "linf": 0.0008016429562934801,
    "residual": 1.6410484082740595e-15,
    "compatibility": 1.474514954580286e-17,
    "mean_error": 7.160477722908953e-17,
    "nullspace_defect": 0.0,
    "solver_gap": 1.0436096431476471e-14,
    "lagrange_multiplier": -2.2436555307051445e-15,
    "boundary_residual": 0.0,
    "boundary_flux_error": 0.0,
    "flux_balance": 1.474514954580286e-17,
    "symmetry": 0.0,
    "gauge_shift_error": 3.774758283725532e-15
  },
  "checks": {
    "neumann-n16 residual": true,
    "neumann-n16 boundary_residual": true,
    "neumann-n16 flux_balance": true,
    "neumann-n16 symmetry": true,
    "neumann-n16 compatibility": true,
    "neumann-n16 mean_error": true,
    "neumann-n16 nullspace_defect": true,
    "neumann-n16 solver_gap": true,
    "neumann-n32 residual": true,
    "neumann-n32 boundary_residual": true,
    "neumann-n32 flux_balance": true,
    "neumann-n32 symmetry": true,
    "neumann-n32 compatibility": true,
    "neumann-n32 mean_error": true,
    "neumann-n32 nullspace_defect": true,
    "neumann-n32 solver_gap": true,
    "neumann-n64 residual": true,
    "neumann-n64 boundary_residual": true,
    "neumann-n64 flux_balance": true,
    "neumann-n64 symmetry": true,
    "neumann-n64 compatibility": true,
    "neumann-n64 mean_error": true,
    "neumann-n64 nullspace_defect": true,
    "neumann-n64 solver_gap": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "mean gauge shifts only constant": true,
    "incompatible source rejected without projection": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

### Sources and review scope

- PETSc developers (n.d.). KSP: Solving Singular Systems. https://petsc.org/main/manual/ksp/; review_level=selected-official-section

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2D mixed Robin MMS and boundary flux

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-algorithm)

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.


**Problem figure**

![2D mixed Robin MMS and boundary flux: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-validation)

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

- [Mixed Robin: 2D analytic field and independent normal flux](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en) (`poisson-robin`; Same-problem reference · Manufactured solution)

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.
### Assumptions, units and boundaries

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.

**Editorial clarification**

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

### Adopted numerical method

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

### References and validation

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

### Limits

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.00037706113250587296,
    "linf": 0.0008911573863470412,
    "residual": 5.729791641151394e-15,
    "compatibility": 3.9384615384615382,
    "mean_error": 0.0,
    "nullspace_defect": 0.0,
    "solver_gap": 0.0,
    "lagrange_multiplier": 0.0,
    "boundary_residual": 4.440892098500626e-16,
    "boundary_flux_error": 0.0006164157489298994,
    "flux_balance": 1.6335890973273592e-13,
    "symmetry": 0.0
  },
  "checks": {
    "robin-n16 residual": true,
    "robin-n16 boundary_residual": true,
    "robin-n16 flux_balance": true,
    "robin-n16 symmetry": true,
    "robin-n32 residual": true,
    "robin-n32 boundary_residual": true,
    "robin-n32 flux_balance": true,
    "robin-n32 symmetry": true,
    "robin-n64 residual": true,
    "robin-n64 boundary_residual": true,
    "robin-n64 flux_balance": true,
    "robin-n64 symmetry": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "boundary flux refinement 1": true,
    "boundary flux refinement 2": true,
    "finest boundary flux": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

### Sources and review scope

- MFEM developers (n.d.). Boundary Conditions: Robin boundary conditions. https://mfem.org/fem_bc/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
