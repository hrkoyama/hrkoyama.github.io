# Scoped ALE piston, sphere transport and SPH/GSPH controls

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Five cases for four scoped extensions; not every original-paper setting or general accuracy qualification.

## Methods

- [Semi-Lagrangian transport: a limited prescribed sphere rotation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en>)
- [ALE uniform-state / geometric-conservation model](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en>)

  Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Semi-Lagrangian transport: a limited prescribed sphere rotation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en>)

  Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Godunov SPH / GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en>)

  GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [SPH kernel reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en>)

  GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [ALE uniform-state / geometric-conservation model](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en>)
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)
- [Godunov SPH / GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en>)
- [SPH kernel reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Prescribed scalar advection on a sphere](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en>)

  Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Axisymmetric spherical shallow-water subproblem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#spherical-shallow-water-en>)

  Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Prescribed scalar advection on a sphere](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en>)

  Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Axisymmetric spherical shallow-water subproblem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#spherical-shallow-water-en>)

  Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-algorithm>)

  Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-algorithm>)

  Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-algorithm>)

  NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-algorithm>)

  ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-algorithm>)

  Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

## Problem figures

- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png
- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png
- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png
- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png
- [Sod shock tube](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en>)

  Five cases for four scoped extensions; not every original-paper setting or general accuracy qualification. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png

## Exact / reference solutions

- [Saltzman-type skew-grid piston: 2D Euler and ALE — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#references-en>)

  Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report. Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Williamson-type spherical rotation: tilted axes and pole crossing — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#references-en>)

  Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core. Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Time evolution of axisymmetric spherical shallow-water balance — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en#references-en>)

  Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sphere-zonal-balance-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim. Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#references-en>)

  Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority. Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en>)
  reference_kind: analytic

  Analytic reference Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en>)
  reference_kind: analytic

  Analytic reference Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sphere-zonal-balance-en>)
  reference_kind: analytic

  Analytic reference Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en>)
  reference_kind: analytic

  Analytic reference GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [Saltzman-type skew-grid piston: 2D Euler and ALE — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-validation>)

  Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report. Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
- [Williamson-type spherical rotation: tilted axes and pole crossing — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-validation>)

  Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.
- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core. Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
- [Time evolution of axisymmetric spherical shallow-water balance — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-validation>)

  Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sphere-zonal-balance-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim. Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
- [Sod-type particle shock tube with Gaussian-convolution GSPH — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-validation>)

  Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.
- [Euler / Sod](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en>)
  relation: related-model
  reference_kind: semi-analytic

  Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity. γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim. Bind the fixed-input formula, reference, figure and executable code. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-validation>)

  Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority. Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
- [Sod shock tube — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#references-en>)

  Five cases for four scoped extensions; not every original-paper setting or general accuracy qualification. Use the semi-analytic Riemann solution for standard Sod data with γ=1.4. A matching problem does not imply identical point/cell-average sampling, grid or error norm.
- [Euler / Sod](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en>)
  relation: related-model
  reference_kind: semi-analytic

  Five cases for four scoped extensions; not every original-paper setting or general accuracy qualification. Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity. γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Five cases for four scoped extensions; not every original-paper setting or general accuracy qualification. Semi-analytic reference Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim. Bind the fixed-input formula, reference, figure and executable code. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.

## Code and validation

- [Williamson-type spherical rotation: tilted axes and pole crossing](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en>)
  availability: run

  Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en>)
  availability: run

  Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.
- [Time evolution of axisymmetric spherical shallow-water balance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en>)
  availability: run

  NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en>)
  availability: run

  Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.
- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en>)
  availability: run

  ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.
- [Semi-Lagrangian transport: a limited prescribed sphere rotation — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
