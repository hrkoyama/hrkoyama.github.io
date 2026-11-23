# KH/RT initial growth and independent linear references

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare actual small-amplitude nonlinear2D runs with separately derived continuous Fourier–Galerkin linear IVPs. Separate finite-time growth, spatial, temporal and amplitude effects.

## Methods

- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Forced vorticity about a maintained shear layer](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en>)

  Explicit forcing maintains the analytic base shear; actual nonlinear2D dynamics evolve its perturbations. Pressure is eliminated. Distinguish this from sharp-interface infinite-domain or compressible KH dispersion. Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.
- [Boussinesq vorticity with active buoyancy](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en>)

  Inertial density is constant; density contrast enters buoyancy only. Forcing maintains the base profile. The curl of vertical buoyancy yields theta_x; this is a perturbation Boussinesq system rather than variable-density Euler. Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.
- [Forced vorticity about a maintained shear layer](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en>)

  Explicit forcing maintains the analytic base shear; actual nonlinear2D dynamics evolve its perturbations. Pressure is eliminated. Distinguish this from sharp-interface infinite-domain or compressible KH dispersion.
- [Boussinesq vorticity with active buoyancy](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en>)

  Inertial density is constant; density contrast enters buoyancy only. Forcing maintains the base profile. The curl of vertical buoyancy yields theta_x; this is a perturbation Boussinesq system rather than variable-density Euler.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-algorithm>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-algorithm>)

  Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

## Problem figures

- [KH initial growth in a smooth periodic shear layer](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png
- [RT initial growth in smooth Boussinesq double layers](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png
- [KH initial growth in a smooth periodic shear layer](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png
- [RT initial growth in smooth Boussinesq double layers](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png

## Exact / reference solutions

- [KH initial growth in a smooth periodic shear layer — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#references-en>)

  Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.
- [KH initial growth: independent linear Fourier-Galerkin reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1. The nonlinear primary evolves actual2D point samples. The reference solves the continuous linearized IVP at kx1 with truncationsK24/40/56 and independently Fourier-differentiated base profiles; it does not substitute a sharp-interface dispersion formula. Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
- [RT initial growth in smooth Boussinesq double layers — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#references-en>)

  Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.
- [RT initial growth: linear Boussinesq double-layer IVP reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler. The reference uses the same smooth base, kx1 continuous linearization and Fourier-Galerkin truncationsK24/40/56. Inertial density is constant; buoyancy perturbation theta supplies vertical forcing, with one unstable interface in the periodic double layer. Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
- [KH initial growth: independent linear Fourier-Galerkin reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1. The nonlinear primary evolves actual2D point samples. The reference solves the continuous linearized IVP at kx1 with truncationsK24/40/56 and independently Fourier-differentiated base profiles; it does not substitute a sharp-interface dispersion formula.
- [RT initial growth: linear Boussinesq double-layer IVP reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler. The reference uses the same smooth base, kx1 continuous linearization and Fourier-Galerkin truncationsK24/40/56. Inertial density is constant; buoyancy perturbation theta supplies vertical forcing, with one unstable interface in the periodic double layer.
- [KH initial growth in a smooth periodic shear layer — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-validation>)

  Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.
- [KH initial growth: independent linear Fourier-Galerkin reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1. The nonlinear primary evolves actual2D point samples. The reference solves the continuous linearized IVP at kx1 with truncationsK24/40/56 and independently Fourier-differentiated base profiles; it does not substitute a sharp-interface dispersion formula. Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
- [RT initial growth in smooth Boussinesq double layers — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-validation>)

  Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.
- [RT initial growth: linear Boussinesq double-layer IVP reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler. The reference uses the same smooth base, kx1 continuous linearization and Fourier-Galerkin truncationsK24/40/56. Inertial density is constant; buoyancy perturbation theta supplies vertical forcing, with one unstable interface in the periodic double layer. Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

## Code and validation

- [KH initial growth in a smooth periodic shear layer](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en>)
  availability: run

  Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.
- [RT initial growth in smooth Boussinesq double layers](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en>)
  availability: run

  Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.
