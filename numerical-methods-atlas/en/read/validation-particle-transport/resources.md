# Particles and transport: independent references, conservation and statistical error

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particle-transport/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Ewald summation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en>)
- [Particle mesh Ewald / PME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en>)
- [Smooth particle mesh Ewald / SPME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en>)
- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)
- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-algorithm>)

  Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-algorithm>)

  Use 16³/24³/40³ meshes, orders four/six and three translations relative to the mesh. Differentiate FFT reciprocal energy through assignment weights; real/self terms share the primary Ewald implementation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-algorithm>)

  Retain P2M/M2M/M2L/L2L and near P2P; compare orders 2/4/8/12 and depths two/three. References include independent Cartesian direct sums, a closed-form charge pair and regular-polygon radial/far-field identities.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-algorithm>)

  CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-algorithm>)

  Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-algorithm>)

  Use upstream finite volumes and Gauss-Legendre ordinates; exact exponential propagation removes spatial error in the angle series. Monte Carlo independently tracks survival/absorption using mu=sqrt(U) and exponential optical paths.

## Problem figures

- [Ewald: asymmetric-cell energies and forces versus independent theta integration](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png
- [SPME: mesh, interpolation order, mesh phase and conservation](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png
- [FMM: direct and analytic references, order and tree depth](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png
- [PIC: mesh/time convergence, invariants and particle noise](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png
- [DSMC collision component: finite-N equilibrium, invariants and statistical error](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png
- [Radiation transport: space/angle convergence and photon statistics](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png

## Exact / reference solutions

- [Ewald: asymmetric-cell energies and forces versus independent theta integration — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-validation>)

  Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.
- [SPME: mesh, interpolation order, mesh phase and conservation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-validation>)

  Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.
- [FMM: direct and analytic references, order and tree depth — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-validation>)

  Measure maximum absolute potential/field errors, actual far translations, rotation/translation differences and net charge-weighted force. Detect an inaccurate low-order control.
- [PIC: mesh/time convergence, invariants and particle noise — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-validation>)

  Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.
- [Independently coded PIC spatial pipeline](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories. Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
- [DSMC collision component: finite-N equilibrium, invariants and statistical error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-validation>)

  Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.
- [Radiation transport: space/angle convergence and photon statistics — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-validation>)

  Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

## Code and validation

- [Ewald: asymmetric-cell energies and forces versus independent theta integration](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en>)
  availability: run

  Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.
- [SPME: mesh, interpolation order, mesh phase and conservation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en>)
  availability: run

  Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.
- [FMM: direct and analytic references, order and tree depth](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en>)
  availability: run

  Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.
- [PIC: mesh/time convergence, invariants and particle noise](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en>)
  availability: run

  Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.
- [DSMC collision component: finite-N equilibrium, invariants and statistical error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en>)
  availability: run

  Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.
- [Radiation transport: space/angle convergence and photon statistics](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en>)
  availability: run

  Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.
