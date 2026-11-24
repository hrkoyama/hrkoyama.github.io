# Long-time grazing PML in a dispersive medium

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-grazing/

Resources explicitly registered to the methods, problems and executions of this chapter. Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

## Methods

- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)

  Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)

  Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

  Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.
- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

## Equations

- [Passive Lorentz–Ohmic Maxwell fields](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en>)

  A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation. Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-algorithm>)

  Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.
- [Passive Lorentz–Ohmic Maxwell fields](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en>)

  A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation.

## Problem figures

- [Long-time grazing PML in a dispersive medium](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png
- [Long-time grazing PML in a dispersive medium](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png

## Exact / reference solutions

- [Long-time grazing PML in a dispersive medium — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#references-en>)

  Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.
- [Isolated same-grid reference for a long grazing dispersive packet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference The homogeneous Lorentz medium continues through the PML: epsilon_inf = 1, delta_epsilon = 0.2, omega_0 = 12, gamma = 0 or 0.005. An Ez-polarized finite-kx Gaussian has carrier omega = 6 and central phase angle 80 degrees. Joint grid/layer refinement uses peaks 6/9/12 on 512/768/1024 cells; the normal control uses 6 and damped fine companion 12. Final time is 700. The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.
- [Isolated same-grid reference for a long grazing dispersive packet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference The homogeneous Lorentz medium continues through the PML: epsilon_inf = 1, delta_epsilon = 0.2, omega_0 = 12, gamma = 0 or 0.005. An Ez-polarized finite-kx Gaussian has carrier omega = 6 and central phase angle 80 degrees. Joint grid/layer refinement uses peaks 6/9/12 on 512/768/1024 cells; the normal control uses 6 and damped fine companion 12. Final time is 700.
- [Long-time grazing PML in a dispersive medium — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-validation>)

  Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.
- [Isolated same-grid reference for a long grazing dispersive packet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference The homogeneous Lorentz medium continues through the PML: epsilon_inf = 1, delta_epsilon = 0.2, omega_0 = 12, gamma = 0 or 0.005. An Ez-polarized finite-kx Gaussian has carrier omega = 6 and central phase angle 80 degrees. Joint grid/layer refinement uses peaks 6/9/12 on 512/768/1024 cells; the normal control uses 6 and damped fine companion 12. Final time is 700. The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

## Code and validation

- [Long-time grazing PML in a dispersive medium](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en>)
  availability: run

  Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.
