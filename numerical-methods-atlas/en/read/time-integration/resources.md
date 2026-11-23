# Time integration and leapfrog

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [Explicit midpoint RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en>)
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en>)
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

## Problem figures

- [Harmonic oscillator, including complex-ODE form](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png

## Exact / reference solutions

- [Harmonic oscillator, including complex-ODE form — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#references-en>)

  Compare with analytic sine/cosine trajectories, including complex-ODE form, and distinguish phase, energy and geometric map properties. No dedicated reference-library card is included.

## Code and validation

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
- [Noh problem: an actual 2D Cartesian Euler calculation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en>)
  availability: run

  A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.
- [Logistic growth: analytic solution and time refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en>)
  availability: run

  One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [SIR: independent DOP853 reference, conservation and convergence](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en>)
  availability: run

  Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.
- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en>)
  availability: run

  Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en>)
  availability: run

  Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en>)
  availability: run

  Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
- [Harmonic oscillator: Verlet phase error and energy](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en>)
  availability: run

  Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.
- [Forward Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Backward Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Heun / SSPRK(2,2) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Explicit midpoint RK2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Ralston RK2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Kutta RK3 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(3,3) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(4,3) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Classical RK4 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(5,4) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Implicit midpoint — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Two-step leapfrog — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
