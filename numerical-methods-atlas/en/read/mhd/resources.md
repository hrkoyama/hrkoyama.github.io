# MHD: constrained transport and divergence cleaning

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)
- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)
- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [HLLE / Einfeldt wave speeds](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [HLLE / Einfeldt wave speeds](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

## Equations

- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-brio-wu-en>)

  [0,1], initial jump x=0.5, t=0.1. HLLD/MC/SSPRK2 is compared after conservative block averaging of the 512-cell result; this same-solver numerical reference is not an exact MHD solution.

## Problem figures

- [Orszag–Tang vortex (CT/GLM/error variants merged)](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp
- [Brio–Wu shock tube](<https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png
- [Circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png
- [Magnetic field-loop advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png

## Exact / reference solutions

- [Orszag–Tang vortex (CT/GLM/error variants merged) — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en>)

  Check conservation, divergence appropriate to each discrete layout, and separately run Athena++ numerical references. These are not exact solutions of the nonlinear MHD problem.
- [Brio–Wu shock tube — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#references-en>)

  Distinguish a finer-grid reference from the same code and an independent Athena++ reference. For coplanar γ=2 Brio–Wu, no exact solution or universal uniqueness is claimed.
- [Circularly polarized Alfvén wave — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en>)

  Evaluate the analytic circularly polarized Alfvén wave using conserved cell averages, including its constant total energy.
- [Magnetic field-loop advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en>)

  Check return error against the initial weak-field loop, magnetic energy and layout-specific divergence after one transit. No exact solution is claimed for arbitrary finite-strength MHD loops.
- [Brio–Wu: HLLD and a conservatively restricted numerical reference — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en#brio-wu-en-validation>)

  Restrict the 512-cell conserved variables by integer block averaging to 64/128 cells before converting to primitives. CSV pairs each 128-cell result with its corresponding restricted reference. Positivity, longitudinal-field error 10^-12, boundary-flux balance 10^-10 and empirical error decrease are separate checks; fallback counts remain visible.

## Code and validation

- [Orszag–Tang: CT, GLM and independent Athena++](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en>)
  availability: run

  Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.
- [Orszag–Tang: matched CT/GLM and converged independent references](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en>)
  availability: run

  Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.
- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en>)
  availability: run

  Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.
- [Brio–Wu: HLLD and a conservatively restricted numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en>)
  availability: run

  Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.
- [Brio–Wu against an independent HLLD implementation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en>)
  availability: run

  Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.
- [Constrained transport / CT — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [GLM divergence cleaning — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [HLLD MHD Riemann solver — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
