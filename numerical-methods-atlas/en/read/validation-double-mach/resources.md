# Double Mach reflection: lightweight grid verification

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-double-mach/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Godunov-type finite volumes](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en>)

  Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Compressible Euler with the same Mach10 data and gamma1.4 is evolved over the full rectangle[0,4]×[0,1].
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-algorithm>)

  The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Double Mach reflection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png
- [Double Mach reflection: lightweight grid verification](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png

## Exact / reference solutions

- [Double Mach reflection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en>)

  Preserve the previously published coarse HLL view and add comparison with a saved reference from a separate finite-volume implementation. The reference is itself a finite-grid numerical solution, not an exact full-field solution or error bound.
- [Double Mach reflection: saved independent finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow on [0,4] × [0,1], with gamma = 1.4, a Mach-10 incident shock at 60 degrees, initial shock foot x = 1/6 and final time T = 0.2. The saved reference uses a separately written, unsplit primitive MUSCL/HLL/Heun finite-volume code on 256 × 64 and 512 × 128 cells. Its generalized-minmod slope parameter is theta = 1.5 (MC-type, rather than canonical MC with theta = 2). The primary and reference codes share the HLL flux family and Heun time-integration equations, while their spatial reconstruction and implementations are separate. Conservative restriction produces comparison cell means. Previously executed source, data and receipts are reused from the immutable RKDG2D kit; no reference PDE, Athena or LAVA was executed anew for this addition. Reference grid differences indicate finite-resolution sensitivity, not rigorous error bounds. This is not an analytic 2D solution or a convergence test for the thin wall jet and vortex pattern. The incident discontinuity is classified at cell centers, rather than initialized from exact cut-cell averages. Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.
- [Double Mach reflection: saved independent finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow on [0,4] × [0,1], with gamma = 1.4, a Mach-10 incident shock at 60 degrees, initial shock foot x = 1/6 and final time T = 0.2. The saved reference uses a separately written, unsplit primitive MUSCL/HLL/Heun finite-volume code on 256 × 64 and 512 × 128 cells. Its generalized-minmod slope parameter is theta = 1.5 (MC-type, rather than canonical MC with theta = 2). The primary and reference codes share the HLL flux family and Heun time-integration equations, while their spatial reconstruction and implementations are separate. Conservative restriction produces comparison cell means. Previously executed source, data and receipts are reused from the immutable RKDG2D kit; no reference PDE, Athena or LAVA was executed anew for this addition. Reference grid differences indicate finite-resolution sensitivity, not rigorous error bounds. This is not an analytic 2D solution or a convergence test for the thin wall jet and vortex pattern. The incident discontinuity is classified at cell centers, rather than initialized from exact cut-cell averages.
- [Double Mach reflection: lightweight grid verification — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-validation>)

  The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.
- [Double Mach reflection: saved independent finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow on [0,4] × [0,1], with gamma = 1.4, a Mach-10 incident shock at 60 degrees, initial shock foot x = 1/6 and final time T = 0.2. The saved reference uses a separately written, unsplit primitive MUSCL/HLL/Heun finite-volume code on 256 × 64 and 512 × 128 cells. Its generalized-minmod slope parameter is theta = 1.5 (MC-type, rather than canonical MC with theta = 2). The primary and reference codes share the HLL flux family and Heun time-integration equations, while their spatial reconstruction and implementations are separate. Conservative restriction produces comparison cell means. Previously executed source, data and receipts are reused from the immutable RKDG2D kit; no reference PDE, Athena or LAVA was executed anew for this addition. Reference grid differences indicate finite-resolution sensitivity, not rigorous error bounds. This is not an analytic 2D solution or a convergence test for the thin wall jet and vortex pattern. The incident discontinuity is classified at cell centers, rather than initialized from exact cut-cell averages. Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

## Code and validation

- [Double Mach reflection: lightweight grid verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en>)
  availability: run

  Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.
