# CT and GLM: matched controls, independent checks and grid/time convergence

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-convergence/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)

  CT and GLM are explicitly bound by the ct-glm-smooth-convergence release example. Matching LLF coefficients and time steps still compares whole discretizations with different magnetic placement, corner EMF averaging and normal-field handling. This solenoidal physical example is distinct from active-cleaning measurements in the separate nonphysical constraint control.
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)

  CT and GLM are explicitly bound by the ct-glm-smooth-convergence release example. Matching LLF coefficients and time steps still compares whole discretizations with different magnetic placement, corner EMF averaging and normal-field handling. This solenoidal physical example is distinct from active-cleaning measurements in the separate nonphysical constraint control.
- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)

## Equations

- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests. Planar ideal MHD on a periodic unit square with gamma=5/3 and mu0=1. The exact solution translates a constructed magnetostatic equilibrium at constant velocity; it is neither a forced manufactured solution nor the standard circularly polarized Alfvén wave. The execution example supplies the GLM auxiliary equation and explicit conserved cell averages.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-algorithm>)

  Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-algorithm>)

  Primary runs use fixed alpha=ch=3 Rusanov/forward Euler and grid-independent GLM kappa2. Independent C++ Athena++ uses HLLD/PLM/RK2/upwind CT. Continuous initial fields agree; Athena’s face/primitive discretization is not identical.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-algorithm>)

  Use the same fully coupled MHD code. With y-invariance andBy=vy=0, the GLM Bx/psi subsystem decouples from fluid feedback, allowing a separately constructed2x2 discrete Fourier symbol and forward-Euler matrix power. Compare kappa2/0 at identical dt and LLF viscosity, separating B/psi phase exchange from physical damping.

## Problem figures

- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png
- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png
- [Orszag–Tang: matched CT/GLM and converged independent references](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png
- [Initial-constraint preservation by CT and active GLM cleaning: nonphysical control](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png

## Exact / reference solutions

- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#references-en>)

  Compare spatial errors against conserved cell averages of the constructed exact solution. Independent DOP853 integration of the same fixed spatial RHS checks temporal error and is not a separate spatial solver. The existing 18-case reference-solution library has no card for this constructed solution, so use the bound example’s equations, results and source rather than borrowing another problem’s reference card.
- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-validation>)

  Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.
- [Orszag–Tang: matched CT/GLM and converged independent references — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-validation>)

  Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.
- [Initial-constraint preservation by CT and active GLM cleaning: nonphysical control — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-validation>)

  Check preservation of the initial CT defect, nonzero GLM psi, independent FE agreement for bothBx/psi, positive density/pressure, and conserved physical E/mass. Test the kappa2/0 ratio of auxiliary wave energy W=mean(Bx²+psi²/ch²), separating FE, semidiscrete-exponential and continuum-Fourier references.

## Code and validation

- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en>)
  availability: run

  Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.
- [Orszag–Tang: matched CT/GLM and converged independent references](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en>)
  availability: run

  Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.
- [Initial-constraint preservation by CT and active GLM cleaning: nonphysical control](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en>)
  availability: run

  Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.
