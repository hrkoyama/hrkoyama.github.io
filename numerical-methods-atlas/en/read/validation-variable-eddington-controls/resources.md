# Lightweight variable Eddington factor and tensor checks

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-variable-eddington-controls/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Variable Eddington factor (1D VEF)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en>)

  Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
- [Variable Eddington tensor (VET)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en>)

  Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.
- [Variable Eddington factor (1D VEF)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en>)
- [Variable Eddington tensor (VET)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en>)

## Equations

- [Static grey VEF/VET moment closure](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en>)

  c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Static grey VEF/VET moment closure](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en>)

  c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-algorithm>)

  At each iteration solve formal Fourier transport with q+ss E_LO, extract f=Kxx/E_HO, and solve finite-difference moment equations using shared conservative faces. The primary closure never receives the analytic reference.
- [Static grey VEF/VET moment closure](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en>)

  c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-algorithm>)

  Iterate formal Fourier angular transport, D=K_HO/E_HO, and an independent finite-difference moment solve. Include both Dxy cross derivatives in shared face fluxes and check local/global discrete budgets.

## Problem figures

- [Variable Eddington factor: a periodic 1D scattering-source control](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png
- [Variable Eddington tensor: a periodic 2D nonparallel-source control](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png
- [Variable Eddington factor: a periodic 1D scattering-source control](<https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png
- [Variable Eddington tensor: a periodic 2D nonparallel-source control](<https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png

## Exact / reference solutions

- [Variable Eddington factor: a periodic 1D scattering-source control — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#references-en>)

  The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
- [Authored continuum Fourier response for periodic 1D VEF](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu. Positive prescribed isotropic source; physical angle space remains S2. The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
- [Variable Eddington tensor: a periodic 2D nonparallel-source control — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#references-en>)

  The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.
- [Authored continuum Fourier response for periodic 2D VET](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained. Positive prescribed isotropic source; physical angle space remains S2. The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.
- [Authored continuum Fourier response for periodic 1D VEF](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en>)
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu. Positive prescribed isotropic source; physical angle space remains S2.
- [Authored continuum Fourier response for periodic 2D VET](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en>)
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained. Positive prescribed isotropic source; physical angle space remains S2.
- [Variable Eddington factor: a periodic 1D scattering-source control — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-validation>)

  Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.
- [Authored continuum Fourier response for periodic 1D VEF](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu. Positive prescribed isotropic source; physical angle space remains S2. The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
- [Variable Eddington tensor: a periodic 2D nonparallel-source control — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-validation>)

  Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.
- [Authored continuum Fourier response for periodic 2D VET](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained. Positive prescribed isotropic source; physical angle space remains S2. The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

## Code and validation

- [Variable Eddington factor: a periodic 1D scattering-source control](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en>)
  availability: run

  Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.
- [Variable Eddington tensor: a periodic 2D nonparallel-source control](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en>)
  availability: run

  Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.
