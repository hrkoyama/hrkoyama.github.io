# Variable Eddington factors and tensors: closing moments with angular transport

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Variable Eddington factor (1D VEF)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en>)
- [Variable Eddington tensor (VET)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en>)

## Equations

- [Static grey VEF/VET moment closure](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en>)

  c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries.

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Variable Eddington factor: a periodic 1D scattering-source control](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en>)
  availability: run

  Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.
- [Variable Eddington tensor: a periodic 2D nonparallel-source control](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en>)
  availability: run

  Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.
- [Variable Eddington factor (1D VEF) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Variable Eddington tensor (VET) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
