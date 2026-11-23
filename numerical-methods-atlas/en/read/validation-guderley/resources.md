# Guderley converging shock: lightweight spherical-radial verification

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-guderley/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  A scoped spherical-shell example with piecewise-constant HLL finite-volume fluxes, shell areas/volumes, the geometric pressure source and physical-time Heun updates.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  A scoped spherical-shell example with piecewise-constant HLL finite-volume fluxes, shell areas/volumes, the geometric pressure source and physical-time Heun updates.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Spherical-radial ideal-gas Euler flow, evolving density, radial momentum and total energy with shell-volume weighting and separately integrating the radial-momentum geometric source.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-algorithm>)

  First-order spherical finite volumes use face area4pi*r^2 and shell volume4pi*delta(r^3)/3. Shared HLL flux divergence plus the radial-momentum pressure source p_i*delta(A)/V is advanced by Heun at CFL0.4. The center is reflecting with zero face area; the outer similarity state is evaluated at both actual RK times. All three conserved budgets integrate the actual boundary flux and geometric source using the same Heun weights. There are no state floors, pressure repairs or hidden step retries.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Guderley converging shock](<https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion-preview.png
- [Guderley converging shock: lightweight spherical-radial verification](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion.png

## Exact / reference solutions

- [Guderley converging shock — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#references-en>)

  The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Numerical eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make this a semi-analytic reference, not closed-form exact cell means. Distinguish the ExactPack-based evaluator from the finite-volume PDE calculation; this is not a comparison between independent similarity implementations. Collapse at the origin, the reflected branch and general equations of state are outside this example.
- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=1.4, with unshocked upstream rho0=1, u=p=0. Lazarus time t in [-1,-0.85] excludes collapse at 0; r in [0,0.75], Rs(t)=0.6*(-t)^alpha and alpha=1/lambda. The initial field already contains the similarity shock and is not zero pressure throughout the domain. Lambda is computed by the pinned ExactPack eigenvalue routine, and the same pinned source supplies the pre-collapse similarity ODE. Shells are split at the shock and conserved states are Gauss16 volume averaged, checked against Gauss32; pressure is p(Ubar). This is not closed-form exact cell means or an independent semi-analytic implementation: it is a dense-output adapter to ExactPack. The figure is a 2D central-section display of 1D radial data, not a 2D Cartesian or post-collapse computation. The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Numerical eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make this a semi-analytic reference, not closed-form exact cell means. Distinguish the ExactPack-based evaluator from the finite-volume PDE calculation; this is not a comparison between independent similarity implementations. Collapse at the origin, the reflected branch and general equations of state are outside this example.
- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=1.4, with unshocked upstream rho0=1, u=p=0. Lazarus time t in [-1,-0.85] excludes collapse at 0; r in [0,0.75], Rs(t)=0.6*(-t)^alpha and alpha=1/lambda. The initial field already contains the similarity shock and is not zero pressure throughout the domain. Lambda is computed by the pinned ExactPack eigenvalue routine, and the same pinned source supplies the pre-collapse similarity ODE. Shells are split at the shock and conserved states are Gauss16 volume averaged, checked against Gauss32; pressure is p(Ubar). This is not closed-form exact cell means or an independent semi-analytic implementation: it is a dense-output adapter to ExactPack. The figure is a 2D central-section display of 1D radial data, not a 2D Cartesian or post-collapse computation.
- [Guderley converging shock: lightweight spherical-radial verification — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-validation>)

  The33 unit checks and55 gates over three refinements were fixed before execution and passed with warnings treated as errors. Checks cover the zero-sound-speed cold HLL branch, geometric static-pressure balance, shared-flux budgets, actual two-stage boundary times and raw failed-stage retention. Full-volume L1 is shown alongside the predetermined r>=0.8*Rs shock/nonzero-flow region, so cold inner gas does not hide active errors. Maximum density/pressure differences and the saved shock trajectory remain visible. The semi-analytic reference uses the pinned LANL ExactPack eigenvalue routine and ODE through a cached pre-collapse-only adapter. It is not an independently reimplemented similarity ODE; the separately implemented finite-volume Euler evolution is compared against that reference. Full-volume density L1 is0.02345/0.01339/0.007722 and pressure L1 is0.03277/0.01743/0.009477. Density L1 in the predetermined r>=0.8*Rs region also decreases:0.02414/0.01378/0.007948. The finest measured shock radius is0.530273 against similarity0.533989, about2.54 cells apart. The maximum scaled three-component budget residual is8.85e-16. Minimum internal energy and sound-speed-only roundoff guard evaluations are both0. The smooth-reference Euler finite-difference residual is8.24e-9 and finite-offset moving-jump residual4.40e-8. All three runs including the similarity eigenvalue calculation took about44.6 seconds on the original Mac.
- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=1.4, with unshocked upstream rho0=1, u=p=0. Lazarus time t in [-1,-0.85] excludes collapse at 0; r in [0,0.75], Rs(t)=0.6*(-t)^alpha and alpha=1/lambda. The initial field already contains the similarity shock and is not zero pressure throughout the domain. Lambda is computed by the pinned ExactPack eigenvalue routine, and the same pinned source supplies the pre-collapse similarity ODE. Shells are split at the shock and conserved states are Gauss16 volume averaged, checked against Gauss32; pressure is p(Ubar). This is not closed-form exact cell means or an independent semi-analytic implementation: it is a dense-output adapter to ExactPack. The figure is a 2D central-section display of 1D radial data, not a 2D Cartesian or post-collapse computation. The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Numerical eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make this a semi-analytic reference, not closed-form exact cell means. Distinguish the ExactPack-based evaluator from the finite-volume PDE calculation; this is not a comparison between independent similarity implementations. Collapse at the origin, the reflected branch and general equations of state are outside this example.

## Code and validation

- [Guderley converging shock: lightweight spherical-radial verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en>)
  availability: run

  An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.
