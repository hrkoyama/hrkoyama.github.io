# Independent fluid/MHD comparisons and CT/GLM

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)
- [GLM divergence cleaning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en>)
- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-algorithm>)

  Reuse the published first-order Rusanov/forward-Euler solvers: shared corner-EMF discrete curl for CT and cell-centered hyperbolic/parabolic GLM cleaning. Independent Athena++ uses HLLD, PLM and RK2.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-algorithm>)

  Atlas uses MC reconstruction and SSPRK2; the independent C++ reference uses HLLD, PLM and RK3. Implementations differ while sharing the HLLD flux family.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-algorithm>)

  Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-algorithm>)

  Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

## Problem figures

- [Orszag–Tang: CT, GLM and independent Athena++](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png
- [Brio–Wu against an independent HLLD implementation](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png
- [Shu–Osher: independent reference and mesh refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png
- [GLM longitudinal mode: analytic damping](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png

## Exact / reference solutions

- [Orszag–Tang: CT, GLM and independent Athena++ — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-validation>)

  Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.
- [Brio–Wu against an independent HLLD implementation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-validation>)

  Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.
- [Shu–Osher: independent reference and mesh refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-validation>)

  Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.
- [GLM longitudinal mode: analytic damping — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-validation>)

  Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

## Code and validation

- [Orszag–Tang: CT, GLM and independent Athena++](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en>)
  availability: run

  Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.
- [Brio–Wu against an independent HLLD implementation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en>)
  availability: run

  Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.
- [Shu–Osher: independent reference and mesh refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en>)
  availability: run

  Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.
- [GLM longitudinal mode: analytic damping](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en>)
  availability: run

  Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution.
