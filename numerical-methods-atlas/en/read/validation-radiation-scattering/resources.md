# Isotropically scattering slabs and continuum-angle references

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-scattering/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare discrete ordinates in an isotropically scattering slab with an independent continuous-angle integral-equation reference.

## Methods

- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

## Equations

- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa. Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-algorithm>)

  Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.
- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.

## Problem figures

- [Isotropic scattering in a finite slab](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png
- [Isotropic scattering in a finite slab](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png

## Exact / reference solutions

- [Isotropic scattering in a finite slab — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#references-en>)

  Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.
- [Isotropically scattering slab: continuous-angle Fredholm flux reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Plane-parallel steady optical-depth slab, unit incoming radiance on the left,vacuum incoming on the right,isotropic single-scattering albedo. Incoming hemispherical flux pi; signed-angle J=.5*integral I. Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.
- [Isotropically scattering slab: continuous-angle Fredholm flux reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Plane-parallel steady optical-depth slab, unit incoming radiance on the left,vacuum incoming on the right,isotropic single-scattering albedo. Incoming hemispherical flux pi; signed-angle J=.5*integral I.
- [Isotropic scattering in a finite slab — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-validation>)

  Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.
- [Isotropically scattering slab: continuous-angle Fredholm flux reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Plane-parallel steady optical-depth slab, unit incoming radiance on the left,vacuum incoming on the right,isotropic single-scattering albedo. Incoming hemispherical flux pi; signed-angle J=.5*integral I. Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

## Code and validation

- [Isotropic scattering in a finite slab](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en>)
  availability: run

  Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.
