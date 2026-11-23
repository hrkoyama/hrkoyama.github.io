# Level sets: moving interfaces and comparison with VOF

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/

Resources explicitly registered to the methods, problems and executions of this chapter. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

## Methods

- [Level-set method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en>)
- [Volume-of-fluid / VOF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/vof/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en>)
- [Level-set method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en>)

  Dedicated2D ENO2/Heun level-set advection. Optional simple Godunov redistancing retains measured area changes; no VOF implementation is assigned.

## Equations

- [Level-set interface advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en>)

  Nonconservative transport of an implicit zero-contour interface. Dedicated circle translation and rigid rotation distinguish this from VOF fraction transport. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [Level-set interface advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en>)

  Nonconservative transport of an implicit zero-contour interface. Dedicated circle translation and rigid rotation distinguish this from VOF fraction transport.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-algorithm>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-algorithm>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

## Problem figures

- [Advection of a level-set circle](<https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png
- [2D level-set circle translation: interface, area and redistancing](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png
- [2D rigid rotation of an off-center level-set circle](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png

## Exact / reference solutions

- [Advection of a level-set circle — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#references-en>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en>)
  reference_kind: analytic

  Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.
- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en>)
  reference_kind: analytic

  Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.
- [2D level-set circle translation: interface, area and redistancing — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-validation>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.
- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D rigid rotation of an off-center level-set circle — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-validation>)

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.
- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution. Analytic reference All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35. Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

## Code and validation

- [2D level-set circle translation: interface, area and redistancing](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en>)
  availability: run

  Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.
- [2D rigid rotation of an off-center level-set circle](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en>)
  availability: run

  Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.
- [Level-set method — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
