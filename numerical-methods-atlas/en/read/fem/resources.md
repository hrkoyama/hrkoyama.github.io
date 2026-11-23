# Continuous finite elements: from weak form to sparse assembly

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Spectral element method (SEM)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-poisson-2d-sine-en>)

  CG/MG use 15/31/63 interior nodes; P1 FEM uses 4/8/16 subdivisions. FEM value L2 and gradient H1-seminorm errors are evaluated inside elements. Single-mode CG iteration counts are not a general speed benchmark.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

## Problem figures

- [2D Poisson / single sine mode, including FEM](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png

## Exact / reference solutions

- [2D Poisson / single sine mode, including FEM — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en>)

  Use sin(πx)sin(πy) on the unit square to check finite-difference and continuous-P1 FEM mesh errors, plus the supplemental AMG example's discrete reference. The added amg-conditioning case uses known algebraic solutions for conditioning/residual diagnostics and has no physical-problem binding. Its results are not borrowed as evidence for this Poisson problem’s mesh accuracy or independent reference. Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM. Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [2D Poisson: CG, multigrid and P1 FEM — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en#poisson-2d-sine-en-validation>)

  CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM. Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

## Code and validation

- [2D Poisson: CG, multigrid and P1 FEM](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en>)
  availability: run

  Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.
- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en>)
  availability: run

  Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.
- [L-corner P1 FEM: grading and separate mesh distortion](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en>)
  availability: run

  Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.
- [Matrix-based AMG: distinguish residual and solution error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en>)
  availability: run

  Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.
- [Continuous P1 Galerkin FEM — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
