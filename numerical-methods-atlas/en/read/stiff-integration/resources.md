# Stiff integration: solve the stage, control the time error

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)
- [IMEX Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=en>)
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)

  Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.
- [IMEX Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=en>)

  Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.

## Equations

- [Robertson chemical kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en>)

  Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation.
- [Van der Pol oscillator](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en>)

  Compare work and error for fixed mu values over a short interval; this does not validate a full relaxation cycle.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-stiff-cosine-en>)

  Temporal initial-value problems using the existing two-stage SDIRK2. Main case: t=1 and 1000/2000/4000 steps. These example formulas are separate from the 46-model inventory, not new heat-PDE or general stiff-system entries.

## Problem figures

- [Stiff cosine-tracking ODE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png
- [Nonlinear nonautonomous ODE with rational exact solution](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png

## Exact / reference solutions

- [Stiff cosine-tracking ODE — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#references-en>)

  Check fixed/adaptive-step errors against cos t for y′=-1000(y-cos t)-sin t with y(0)=1.
- [Nonlinear nonautonomous ODE with rational exact solution — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en>)

  Check temporal refinement against the manufactured exact solution 1/(1+t) for y′=-y²+sin(t)[y-1/(1+t)], y(0)=1.
- [Stiff cosine-tracking ODE: SDIRK2 — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en#stiff-cosine-en-validation>)

  CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.

## Code and validation

- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en>)
  availability: run

  Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en>)
  availability: run

  Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.
- [Stiff cosine-tracking ODE: SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en>)
  availability: run

  Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.
- [BDF2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [L-stable SDIRK2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [IMEX Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Adaptive SDIRK2 / step doubling — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Stiff cosine-tracking ODE — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Nonlinear nonautonomous ODE with rational exact solution — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
