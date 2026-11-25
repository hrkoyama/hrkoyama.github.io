# Biological reaction–diffusion: two-dimensional and boundary controls

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-space-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare a special-speed Fisher front, boundary-specific two-dimensional Schnakenberg transients and forced Keller–Segel cell averages and fluxes with independent references.

## Methods

- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

  Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.
- [Crank–Nicolson](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en>)

  Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

  Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

  Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

  Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)
- [Crank–Nicolson](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en>)
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

## Equations

- [Fisher–KPP invasion front](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en>)

  Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Not implementation of the entire model family. Fixed cases: Fisher–KPP: a special-speed exact front Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.
- [Schnakenberg reaction–diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en>)

  A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. The earlier 1D case alone makes no general pattern-selection, biological-calibration or fluid-coupling claim. Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.
- [Keller–Segel chemotaxis](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en>)

  Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Not implementation of the entire model family. Fixed cases: Keller–Segel: a manufactured coupled-flux solution On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.
- [Forced advective Keller–Segel manufactured problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en>)

  This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity. On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.
- [Forced advective Keller–Segel manufactured problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en>)

  This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-algorithm>)

  Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.
- [Fisher–KPP invasion front](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en>)

  Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Not implementation of the entire model family. Fixed cases: Fisher–KPP: a special-speed exact front
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-algorithm>)

  Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.
- [Schnakenberg reaction–diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en>)

  A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. The earlier 1D case alone makes no general pattern-selection, biological-calibration or fluid-coupling claim. Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-algorithm>)

  Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.
- [Keller–Segel chemotaxis](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en>)

  Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Not implementation of the entire model family. Fixed cases: Keller–Segel: a manufactured coupled-flux solution

## Problem figures

- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png
- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png

## Exact / reference solutions

- [Fisher–KPP: a special-speed exact front — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#references-en>)

  Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.
- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24. Dimensionless; diffusion coefficient and reaction rate equal 1. Separate exact-front and constant boundary experiments; retain finite-domain effects. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.
- [Schnakenberg:2D boundaries and initial modes — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#references-en>)

  Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions. Dimensionless square [0,2pi]², diffusion coefficients 0.01 and 1. Single/mixed Neumann modes and a single mode with equilibrium Dirichlet data. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.
- [Keller–Segel: a manufactured coupled-flux solution — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#references-en>)

  Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection. Dimensionless; manufactured-field coefficients and forcing are fixed in inputs.json. Manufactured forcing and boundary fluxes, with explicit ownership of interior faces and corners. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.
- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en>)
  reference_kind: analytic

  Analytic reference Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24. Dimensionless; diffusion coefficient and reaction rate equal 1. Separate exact-front and constant boundary experiments; retain finite-domain effects.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions. Dimensionless square [0,2pi]², diffusion coefficients 0.01 and 1. Single/mixed Neumann modes and a single mode with equilibrium Dirichlet data.
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en>)
  reference_kind: manufactured

  Manufactured solution On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection. Dimensionless; manufactured-field coefficients and forcing are fixed in inputs.json. Manufactured forcing and boundary fluxes, with explicit ownership of interior faces and corners.
- [Fisher–KPP: a special-speed exact front — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-validation>)

  Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.
- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24. Dimensionless; diffusion coefficient and reaction rate equal 1. Separate exact-front and constant boundary experiments; retain finite-domain effects. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.
- [Schnakenberg:2D boundaries and initial modes — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-validation>)

  Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions. Dimensionless square [0,2pi]², diffusion coefficients 0.01 and 1. Single/mixed Neumann modes and a single mode with equilibrium Dirichlet data. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.
- [Keller–Segel: a manufactured coupled-flux solution — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-validation>)

  Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection. Dimensionless; manufactured-field coefficients and forcing are fixed in inputs.json. Manufactured forcing and boundary fluxes, with explicit ownership of interior faces and corners. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

## Code and validation

- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en>)
  availability: run

  Separate profile, phase, grid, time and finite-boundary errors.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en>)
  availability: run

  Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en>)
  availability: run

  Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.
