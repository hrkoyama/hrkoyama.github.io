# Gravitational trajectories: Kepler and softened finite particles

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/

Resources explicitly registered to the methods, problems and executions of this chapter. Distinguish exact Kepler trajectories from short-time finite-particle references using the identical softened ODE.

## Methods

- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.
- [Barnes–Hut octree](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en>)

  Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)
- [Barnes–Hut octree](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en>)

## Equations

- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-algorithm>)

  Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-algorithm>)

  Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

## Problem figures

- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png

## Exact / reference solutions

- [Unsoftened Kepler two-body time error — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#references-en>)

  Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- [Short-time32body dynamics from a cold Plummer-density sample — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#references-en>)

  Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening. Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en>)
  reference_kind: analytic

  Analytic reference G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.
- [Unsoftened Kepler two-body time error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-validation>)

  Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- [Short-time32body dynamics from a cold Plummer-density sample — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-validation>)

  Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening. Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

## Code and validation

- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en>)
  availability: run

  Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.
- [Short-time32body dynamics from a cold Plummer-density sample](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en>)
  availability: run

  Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.
