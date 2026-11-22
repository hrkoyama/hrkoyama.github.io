# Continuous finite elements: from weak form to sparse assembly

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
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

  Use sin(πx)sin(πy) on the unit square to check finite-difference and continuous-P1 FEM mesh errors, plus the supplemental AMG example's discrete reference. The added amg-conditioning case uses known algebraic solutions for conditioning/residual diagnostics and has no physical-problem binding. Its results are not borrowed as evidence for this Poisson problem’s mesh accuracy or independent reference.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson: CG, multigrid and P1 FEM — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en#poisson-2d-sine-en-validation>)

  CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

## Code and validation

- [2D Poisson: CG, multigrid and P1 FEM](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en>)
  availability: run

  Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.
- [Matrix-based AMG: distinguish residual and solution error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en>)
  availability: run

  Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.
- [Continuous P1 Galerkin FEM — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
