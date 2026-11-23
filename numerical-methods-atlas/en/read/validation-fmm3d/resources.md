# 3D1/r kernels: expansions,trees and force checks

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-fmm3d/

Resources explicitly registered to the methods, problems and executions of this chapter. Check nonzero final contributions through actual3D M2M,M2L,L2L paths and unique interaction ownership.

## Methods

- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)

  Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.
- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)

## Equations

- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-algorithm>)

  Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

## Problem figures

- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png
- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png

## Exact / reference solutions

- [Actual3D1/r FMM: multilevel translations, force and ownership — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#references-en>)

  Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.
- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3. Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.
- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.
- [Actual3D1/r FMM: multilevel translations, force and ownership — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-validation>)

  Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.
- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3. Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

## Code and validation

- [Actual3D1/r FMM: multilevel translations, force and ownership](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en>)
  availability: run

  Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.
