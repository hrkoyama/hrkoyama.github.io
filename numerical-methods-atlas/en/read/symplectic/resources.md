# Symplectic integration: a canonical map, not an exact energy promise

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Symplectic Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)
- [Yoshida fourth-order composition](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=en>)
- [Symplectic Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Yoshida fourth-order composition](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-harmonic-oscillator-en>)

  Unit mass/frequency, t=20, velocity Verlet with 200/400/800 steps. Reversibility or symplecticity does not imply exact conservation of the original energy.

## Problem figures

- [Nonlinear quartic-potential oscillator](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png
- [Harmonic oscillator: Verlet phase error and energy](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en>)

  A representative problem figure; its grid, time and initial data may differ from this fixed input.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png

## Exact / reference solutions

- [Nonlinear quartic-potential oscillator — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en>)

  Compare conserved energy and long-time numerical trajectories/map properties in the nonlinear potential. The stored figure is not labeled a closed-form exact trajectory.
- [Harmonic oscillator: Verlet phase error and energy — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en#harmonic-oscillator-en-validation>)

  CSV aligns numerical/analytic q,p and energy on the finest time grid. Observed order uses endpoint-state errors; energy deviation uses all recorded times.

## Code and validation

- [Harmonic oscillator: Verlet phase error and energy](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en>)
  availability: run

  Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.
- [Symplectic Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Velocity Verlet / particle leapfrog — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Yoshida fourth-order composition — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
