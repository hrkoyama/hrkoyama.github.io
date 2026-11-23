# Euler reconstruction: PPM, characteristics, WENO-Z and AUSM

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Euler characteristic reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=en>)
- [FD WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en>)
- [FD WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Limited PPM reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [FD WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Euler characteristic reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Monotonized central / MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-shu-osher-en>)

  Initial jump at x=−4; see the fixed input for the left state. Compares characteristic finite-difference WENO5-Z point values. The 800-point reference is neither exact nor an independent solver.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Shu–Osher shock/entropy interaction](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png
- [Moving contact discontinuity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png
- [Smooth two-dimensional Euler entropy wave](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png

## Exact / reference solutions

- [Shu–Osher shock/entropy interaction — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#references-en>)

  Distinguish the stored high-resolution WENO-Z numerical reference from the separately distributed independent Athena++ reference. Neither is claimed as an exact solution of this shock–density-wave interaction.
- [Moving contact discontinuity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#references-en>)

  The standard is analytic translation of a periodic contact discontinuity at constant pressure and velocity. The complete Sod wave pattern is not a substitute.
- [Smooth two-dimensional Euler entropy wave — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en>)

  Check analytic conserved cell averages and mesh refinement for the 2D periodic sine-density wave with velocity (0.7,0.3) and constant pressure.
- [Shu–Osher: characteristic WENO-Z and a numerical reference — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en#shu-osher-en-validation>)

  Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.

## Code and validation

- [WENO-JS/Z: fixed critical-point and epsilon comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en>)
  availability: run

  Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.
- [Shu–Osher: characteristic WENO-Z and a numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en>)
  availability: run

  Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.
- [Shu–Osher: independent reference and mesh refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en>)
  availability: run

  Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.
- [Euler characteristic reconstruction — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [FD WENO5-Z — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Smooth two-dimensional Euler entropy wave — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
