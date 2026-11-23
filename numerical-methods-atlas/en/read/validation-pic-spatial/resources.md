# PIC checks against independent spatial kernels

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-pic-spatial/

Resources explicitly registered to the methods, problems and executions of this chapter. Update the field at every kick using independent CIC and explicit DFT kernels; state the shared temporal algorithm.

## Methods

- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)
- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-algorithm>)

  The independent path owns scalar deposition, explicit complex DFT sums and scalar gathering; it imports no primary spatial routines. Mathematical CIC, Nyquist convention, velocity-Verlet and initial arrays are intentionally shared.
- [Electrostatic Vlasov–Poisson equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en>)

  1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope.

## Problem figures

- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png
- [Cold-plasma oscillation with electrostatic CIC PIC](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en>)

  Update the field at every kick using independent CIC and explicit DFT kernels; state the shared temporal algorithm. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png

## Exact / reference solutions

- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
- [Independently coded PIC spatial pipeline — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-validation>)

  19pytest and58/58fixed gates passed. Compare six pairs=twelve self-consistent trajectories at all13states; maximum differences:x8.88e-16,v3.33e-16,E8.33e-16,rho2.89e-15. Shared pytest+main.392s. Initial small pytest retained17/18with a periodic-index failure; integer wrapping was corrected before the first fixed main batch.
- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories. Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
- [Cold-plasma oscillation with electrostatic CIC PIC — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en>)

  Update the field at every kick using independent CIC and explicit DFT kernels; state the shared temporal algorithm. Compare with linear cold-plasma displacement cos(t); check charge compatibility, Poisson residual, self force, and separate grid/timestep series. This is not an exact reference for general nonlinear PIC trajectories. The companion retains stationary background ions and separates charge, momentum and particle/field-energy diagnostics from trajectory error. Its reference is small-amplitude linear theory, supplying no evidence for thermal Landau damping or electromagnetic PIC.
- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en>)
  relation: related-model
  reference_kind: numerical-reference

  Update the field at every kick using independent CIC and explicit DFT kernels; state the shared temporal algorithm. Finite-grid numerical reference Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories. Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

## Code and validation

- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en>)
  availability: run

  Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.
