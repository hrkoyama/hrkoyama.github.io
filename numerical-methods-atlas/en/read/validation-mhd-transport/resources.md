# Independent MHD transport, waves and compression comparisons

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-transport/

Resources explicitly registered to the methods, problems and executions of this chapter. Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments.

## Methods

- [HLLD MHD Riemann solver](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [Constrained transport / CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-algorithm>)

  Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.
- [Ideal magnetohydrodynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en>)

  Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-algorithm>)

  Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-algorithm>)

  Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

## Problem figures

- [Circular Alfven wave: full-state refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png
- [Magnetic loop: independent 2D reference and refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png
- [Late Orszag-Tang: independent reference and compression structure](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png
- [Circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png
- [Magnetic field-loop advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png
- [Orszag–Tang vortex (CT/GLM/error variants merged)](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp

## Exact / reference solutions

- [Circular Alfven wave: analytic full-state conserved cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en>)
  reference_kind: analytic

  Analytic reference gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure. Apply sinc(h) to transverse magnetic fields and momenta, retaining E=.66, and qualify against independent Gauss16 quadrature. The x-t picture shows one spatial dimension and saved times, not oblique2D propagation.
- [Magnetic loop: pinned independent Athena++ final-field reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs. Execute the unchanged official generator at pinned commit1395e2f…; qualify Ny64/128 and finest-grid half-CFL sensitivity. Compare final conserved fields only after conservative restriction.
- [Late Orszag-Tang: independent finite-grid density/pressure reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model. Run official Athena++ at128²/256² and finest-grid half CFL to T.2. Conservatively restrict final conserved variables before computing pressure; pressure is not averaged separately.
- [Circular Alfven wave: full-state refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-validation>)

  Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.
- [Circular Alfven wave: analytic full-state conserved cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure. Apply sinc(h) to transverse magnetic fields and momenta, retaining E=.66, and qualify against independent Gauss16 quadrature. The x-t picture shows one spatial dimension and saved times, not oblique2D propagation. gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.
- [Magnetic loop: independent 2D reference and refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-validation>)

  Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.
- [Magnetic loop: pinned independent Athena++ final-field reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs. Execute the unchanged official generator at pinned commit1395e2f…; qualify Ny64/128 and finest-grid half-CFL sensitivity. Compare final conserved fields only after conservative restriction. Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.
- [Late Orszag-Tang: independent reference and compression structure — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-validation>)

  Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.
- [Late Orszag-Tang: independent finite-grid density/pressure reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model. Run official Athena++ at128²/256² and finest-grid half CFL to T.2. Conservatively restrict final conserved variables before computing pressure; pressure is not averaged separately. gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
- [Circularly polarized Alfvén wave — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Evaluate the analytic circularly polarized Alfvén wave using conserved cell averages, including its constant total energy. Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.
- [Circular Alfven wave: analytic full-state conserved cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en>)
  relation: related-model
  reference_kind: analytic

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Analytic reference gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure. Apply sinc(h) to transverse magnetic fields and momenta, retaining E=.66, and qualify against independent Gauss16 quadrature. The x-t picture shows one spatial dimension and saved times, not oblique2D propagation. gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.
- [Magnetic field-loop advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Check return error against the initial weak-field loop, magnetic energy and layout-specific divergence after one transit. No exact solution is claimed for arbitrary finite-strength MHD loops. Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.
- [Magnetic loop: pinned independent Athena++ final-field reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en>)
  relation: related-model
  reference_kind: numerical-reference

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Finite-grid numerical reference Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs. Execute the unchanged official generator at pinned commit1395e2f…; qualify Ny64/128 and finest-grid half-CFL sensitivity. Compare final conserved fields only after conservative restriction. Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.
- [Orszag–Tang vortex (CT/GLM/error variants merged) — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en>)

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Check conservation, divergence appropriate to each discrete layout, and separately run Athena++ numerical references. These are not exact solutions of the nonlinear MHD problem. Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.
- [Late Orszag-Tang: independent finite-grid density/pressure reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en>)
  relation: related-model
  reference_kind: numerical-reference

  Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments. Finite-grid numerical reference gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model. Run official Athena++ at128²/256² and finest-grid half CFL to T.2. Conservatively restrict final conserved variables before computing pressure; pressure is not averaged separately. gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

## Code and validation

- [Circular Alfven wave: full-state refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en>)
  availability: run

  Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.
- [Magnetic loop: independent 2D reference and refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en>)
  availability: run

  Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.
- [Late Orszag-Tang: independent reference and compression structure](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en>)
  availability: run

  Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.
