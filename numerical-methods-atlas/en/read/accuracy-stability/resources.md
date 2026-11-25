# A-stability, L-stability and error norms

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/accuracy-stability/

Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.

## Methods

- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.
- [Crank–Nicolson](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings.

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-stiff-cosine-en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings. Temporal initial-value problems using the existing two-stage SDIRK2. Main case: t=1 and 1000/2000/4000 steps. These example formulas are separate from the 46-model inventory, not new heat-PDE or general stiff-system entries.

## Problem figures

- [Stiff cosine-tracking ODE: SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings. A representative problem figure; its grid, time and initial data may differ from this fixed input.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png

## Exact / reference solutions

- [Stiff cosine-tracking ODE: SDIRK2 — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en#stiff-cosine-en-validation>)

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings. CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.
- [Stiff cosine-tracking ODE: SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-stiff-cosine-exact-en>)
  relation: same-problem
  reference_kind: analytic

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings. Analytic reference rate=1000; 1000/2000/4000 steps give rate*h=1,0.5,0.25. Uses fixed gamma=1-1/sqrt(2) and the existing Newton stage solver. Separate decay: y'=-1e8*y, y(0)=1, h=1. No adaptive stepping. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

## Code and validation

- [Stiff cosine-tracking ODE: SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en>)
  availability: run

  Links to the time integrators compared in the chapter and a related SDIRK2 stiff cosine-tracking ODE. Errors, stage residuals and step refinement for stiff-cosine validate that fixed input; they are neither a general A/L-stability proof nor a matched verification of every listed method. Error norms and stability retain their different meanings. Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.
