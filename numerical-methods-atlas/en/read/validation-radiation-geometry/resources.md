# 2D shadows,beams and M1 closure

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/

Resources explicitly registered to the methods, problems and executions of this chapter. Compute absorber shadows and opposing beams with discrete ordinates and M1, separately checking the closed M1 PDE with a manufactured solution.

## Methods

- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

## Equations

- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa. Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.
- [Static grey M1 moments in flat spacetime](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en>)

  c=1,2D space with full3D pressure including Pzz. Separate isotropic/vacuum branches,closed-PDE MMS and beam defects against angular transport; no relativistic-fluid claim. Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.
- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa. Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.
- [Static grey M1 moments in flat spacetime](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en>)

  c=1,2D space with full3D pressure including Pzz. Separate isotropic/vacuum branches,closed-PDE MMS and beam defects against angular transport; no relativistic-fluid claim. Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.
- [Static grey M1 moments in flat spacetime](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en>)

  c=1,2D space with full3D pressure including Pzz. Separate isotropic/vacuum branches,closed-PDE MMS and beam defects against angular transport; no relativistic-fluid claim.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-algorithm>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.
- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-algorithm>)

  Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

## Problem figures

- [Two-dimensional absorber shadow and M1 transport](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png
- [Opposing beams and information loss in the M1 closure](<https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png
- [Two-dimensional absorber shadow and M1 transport](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png
- [Opposing beams and information loss in the M1 closure](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png

## Exact / reference solutions

- [Two-dimensional absorber shadow and M1 transport — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en>)

  The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.
- [Circular-absorber characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
- [Opposing beams and information loss in the M1 closure — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en>)

  The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.
- [Counterpropagating packet characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
- [Circular-absorber characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en>)
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution.
- [Counterpropagating packet characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en>)
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution.
- [Two-dimensional absorber shadow and M1 transport — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-validation>)

  The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.
- [Circular-absorber characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
- [Opposing beams and information loss in the M1 closure — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-validation>)

  The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.
- [Counterpropagating packet characteristic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference 2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

## Code and validation

- [Two-dimensional absorber shadow and M1 transport](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en>)
  availability: run

  Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.
- [Opposing beams and information loss in the M1 closure](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en>)
  availability: run

  Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.
