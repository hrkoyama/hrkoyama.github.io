# Corner singularities, curved coordinates and Neumann/Robin boundaries

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/

Resources explicitly registered to the methods, problems and executions of this chapter. Actually solve singular L-corner P1 FEM, annular variable-viscosity vector Q1 PDE, pure-Neumann compatibility/mean-gauge and mixed-Robin manufactured problems.

## Methods

- [Q1 FEM for scalar diffusion and mapped vector BVPs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en>)
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)

  Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.
- [Q1 FEM for scalar diffusion and mapped vector BVPs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en>)

  Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

  Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.
- [Variable-viscosity vector stress boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en>)

  Linear stress-divergence BVP coupling two Cartesian components. Q1 basis functions in polar coordinates use the exact curved Jacobian and include variable-mu gradients and shear. There is no pressure,incompressibility constraint or advective term. 1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.
- [Variable-viscosity vector stress boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en>)

  Linear stress-divergence BVP coupling two Cartesian components. Q1 basis functions in polar coordinates use the exact curved Jacobian and include variable-mu gradients and shear. There is no pressure,incompressibility constraint or advective term.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-algorithm>)

  Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-algorithm>)

  Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-algorithm>)

  Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-algorithm>)

  Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

## Problem figures

- [L-corner P1 FEM: grading and separate mesh distortion](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png
- [Annular variable-viscosity vector PDE MMS](<https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png
- [Pure Neumann compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png
- [2D mixed Robin MMS and boundary flux](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png
- [L-corner P1 FEM: grading and separate mesh distortion](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png
- [Annular variable-viscosity vector PDE MMS](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png
- [Pure Neumann compatibility and mean gauge](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png
- [2D mixed Robin MMS and boundary flux](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png

## Exact / reference solutions

- [L-corner P1 FEM: grading and separate mesh distortion — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#references-en>)

  Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.
- [L-corner singularity: harmonic field and separate smooth MMS](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. Integrate the analytic corner field and gradient over elements, comparing uniform and a-priori graded meshes at matched DOFs. A separate unit-square sine MMS on regular/warped meshes separates singularity from distortion. No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
- [Annular variable-viscosity vector PDE MMS — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#references-en>)

  Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).
- [Annular vector-viscous MMS: force qualified by independent stress differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution 1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. Derive stress/force from the Cartesian vector field with s=x²+y²,A=(s-1)(4-s), then qualify force by separate Cartesian stress finite differentiation. Also check independent integrated body force(756pi/5,0). A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
- [Pure Neumann compatibility and mean gauge — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#references-en>)

  Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.
- [Pure Neumann: analytic field, compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. Use point DOFs for u=cos(2pi*x)cos(2pi*y),f=8pi²u and zero outward normal flux. Distinguish means0/.25 and explicitly reject incompatible source+1 rather than projecting it away. A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
- [2D mixed Robin MMS and boundary flux — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#references-en>)

  Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.
- [Mixed Robin: 2D analytic field and independent normal flux](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. Use f=5pi²cos(pi*x)cos(2pi*y),outward Neumann±1 on x walls and analytic alpha*u+beta*dn(u)=g on y walls. Distinguish algebraic boundary-relation residual from analytic physical-normal-flux error. The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.
- [L-corner singularity: harmonic field and separate smooth MMS](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en>)
  reference_kind: analytic

  Analytic reference L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. Integrate the analytic corner field and gradient over elements, comparing uniform and a-priori graded meshes at matched DOFs. A separate unit-square sine MMS on regular/warped meshes separates singularity from distortion.
- [Annular vector-viscous MMS: force qualified by independent stress differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en>)
  reference_kind: manufactured

  Manufactured solution 1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. Derive stress/force from the Cartesian vector field with s=x²+y²,A=(s-1)(4-s), then qualify force by separate Cartesian stress finite differentiation. Also check independent integrated body force(756pi/5,0).
- [Pure Neumann: analytic field, compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en>)
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. Use point DOFs for u=cos(2pi*x)cos(2pi*y),f=8pi²u and zero outward normal flux. Distinguish means0/.25 and explicitly reject incompatible source+1 rather than projecting it away.
- [Mixed Robin: 2D analytic field and independent normal flux](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en>)
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. Use f=5pi²cos(pi*x)cos(2pi*y),outward Neumann±1 on x walls and analytic alpha*u+beta*dn(u)=g on y walls. Distinguish algebraic boundary-relation residual from analytic physical-normal-flux error.
- [L-corner P1 FEM: grading and separate mesh distortion — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-validation>)

  Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.
- [L-corner singularity: harmonic field and separate smooth MMS](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. Integrate the analytic corner field and gradient over elements, comparing uniform and a-priori graded meshes at matched DOFs. A separate unit-square sine MMS on regular/warped meshes separates singularity from distortion. No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
- [Annular variable-viscosity vector PDE MMS — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-validation>)

  Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).
- [Annular vector-viscous MMS: force qualified by independent stress differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution 1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. Derive stress/force from the Cartesian vector field with s=x²+y²,A=(s-1)(4-s), then qualify force by separate Cartesian stress finite differentiation. Also check independent integrated body force(756pi/5,0). A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
- [Pure Neumann compatibility and mean gauge — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-validation>)

  Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.
- [Pure Neumann: analytic field, compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. Use point DOFs for u=cos(2pi*x)cos(2pi*y),f=8pi²u and zero outward normal flux. Distinguish means0/.25 and explicitly reject incompatible source+1 rather than projecting it away. A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
- [2D mixed Robin MMS and boundary flux — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-validation>)

  Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.
- [Mixed Robin: 2D analytic field and independent normal flux](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. Use f=5pi²cos(pi*x)cos(2pi*y),outward Neumann±1 on x walls and analytic alpha*u+beta*dn(u)=g on y walls. Distinguish algebraic boundary-relation residual from analytic physical-normal-flux error. The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

## Code and validation

- [Annular variable-viscosity vector PDE MMS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en>)
  availability: run

  Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en>)
  availability: run

  Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.
- [L-corner P1 FEM: grading and separate mesh distortion](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en>)
  availability: run

  Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.
- [Pure Neumann compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en>)
  availability: run

  Solve singular2D Poisson with compatibility/gauge and reject incompatible source.
- [2D mixed Robin MMS and boundary flux](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en>)
  availability: run

  Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.
- [Q1 FEM for scalar diffusion and mapped vector BVPs — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
