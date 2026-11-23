# Spectral elements: high-order finite elements and 2D Poisson

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/spectral-element/

Resources explicitly registered to the methods, problems and executions of this chapter. Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software.

## Methods

- [Spectral element method (SEM)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en>)
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)
- [Discontinuous Galerkin / Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en>)

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-algorithm>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

## Problem figures

- [2D Poisson / single sine mode, including FEM](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png
- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png

## Exact / reference solutions

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  reference_kind: manufactured

  Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [2D Poisson / single sine mode, including FEM — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Use sin(πx)sin(πy) on the unit square to check finite-difference and continuous-P1 FEM mesh errors, plus the supplemental AMG example's discrete reference. The added amg-conditioning case uses known algebraic solutions for conditioning/residual diagnostics and has no physical-problem binding. Its results are not borrowed as evidence for this Poisson problem’s mesh accuracy or independent reference. Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  relation: same-problem
  reference_kind: manufactured

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM. Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-validation>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  relation: same-problem
  reference_kind: manufactured

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM. Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

## Code and validation

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en>)
  availability: run

  Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.
- [Spectral element method (SEM) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
