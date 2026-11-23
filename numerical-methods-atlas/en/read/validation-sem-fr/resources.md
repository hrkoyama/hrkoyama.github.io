# Spectral elements and FR: small comparisons with existing FEM/DG

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sem-fr/

Resources explicitly registered to the methods, problems and executions of this chapter. Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software.

## Methods

- [Spectral element method (SEM)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en>)
- [Continuous P1 Galerkin FEM](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en>)
- [Flux reconstruction (FR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en>)
- [Discontinuous Galerkin / Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-algorithm>)

  C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-algorithm>)

  p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability.

## Problem figures

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png
- [1D periodic FR advection: Radau correction and published DG comparison](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png
- [2D Poisson / single sine mode, including FEM](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png
- [Periodic sine-wave advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png

## Exact / reference solutions

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-validation>)

  Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM. Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [1D periodic FR advection: Radau correction and published DG comparison — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-validation>)

  Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en>)
  reference_kind: manufactured

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Manufactured solution Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
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
- [Periodic sine-wave advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example. Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## Code and validation

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en>)
  availability: run

  Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.
- [1D periodic FR advection: Radau correction and published DG comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en>)
  availability: run

  Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.
