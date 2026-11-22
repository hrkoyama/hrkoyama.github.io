# Particles, electrostatics, kinetic and radiative transport

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Ewald summation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Particle mesh Ewald / PME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Smooth particle mesh Ewald / SPME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Ewald summation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en>)
- [Particle mesh Ewald / PME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en>)
- [Smooth particle mesh Ewald / SPME](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en>)
- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)
- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. The link is the electrostatic Poisson/Laplace field. This is neutral periodic Coulomb Ewald/PME, not an interchange of gravitational masses, signs or boundaries.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. A particle sum with the logarithmic Green kernel of 2D Poisson/Laplace, distinct from softened 3D 1/r gravity.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Poisson identifies the self-consistent electrostatic field; the registry does not list the complete coupled particle-motion/CIC PIC system.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-algorithm>)

  Combine an erfc-screened image sum, Gaussian-damped reciprocal structure factors and the self correction. Differentiate each term and check all 24 force components against central energy differences.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-algorithm>)

  Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-algorithm>)

  Implement leaf P2M, upward M2M, interaction-list M2L, downward L2L, local-polynomial evaluation and near-field P2P. Record translation and near-pair counts; this is not a Barnes–Hut traversal relabeled as FMM.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-algorithm>)

  Combine CIC deposition and matching field gathering, a mean-zero spectral Poisson solve and velocity Verlet. Set the field Nyquist mode to zero for a real skew-adjoint spectral derivative.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-algorithm>)

  Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-algorithm>)

  Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

## Problem figures

- [Neutral periodic charges: Ewald and smooth PME](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png
- [2D logarithmic FMM with M2M, M2L and L2L](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png
- [Cold-plasma oscillation with electrostatic CIC PIC](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](<https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png
- [Discrete-ordinate radiation transport through an absorbing slab](<https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png
- [Neutral-cell Ewald sums and an independent theta integral](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png
- [Mesh/order convergence of B-spline smooth PME](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png
- [2D logarithmic FMM with M2M, M2L and L2L](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png
- [Cold-plasma oscillation with electrostatic CIC PIC](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png
- [Discrete-ordinate radiation transport through an absorbing slab](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png

## Exact / reference solutions

- [Neutral periodic charges: Ewald and smooth PME — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#references-en>)

  Check converged Ewald sums for identical neutral periodic charges/conventions, force finite differences and cutoff/mesh refinement. Boundaries and interactions differ from isolated gravitational direct sums. The companion compares energy and every force for the same neutral eight-charge cubic tin-foil cell against a separately implemented theta integral and its own refinement. SPME uses B-spline energy gradients; original Lagrange PME and exact momentum conservation are not claimed.
- [2D logarithmic FMM with M2M, M2L and L2L — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#references-en>)

  Use direct summation with the same 2D logarithmic kernel and particles to check expansion order, hierarchical translations and force error. Do not reuse a 3D 1/r reference. The companion uses Cartesian direct sums and analytic configurations as separate references, varying expansion order and tree depth independently. It guarantees neither monotonic error with depth nor accuracy/complexity for a 3D Coulomb kernel.
- [Cold-plasma oscillation with electrostatic CIC PIC — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en>)

  Compare with linear cold-plasma displacement cos(t); check charge compatibility, Poisson residual, self force, and separate grid/timestep series. This is not an exact reference for general nonlinear PIC trajectories. The companion retains stationary background ions and separates charge, momentum and particle/field-energy diagnostics from trajectory error. Its reference is small-amplitude linear theory, supplying no evidence for thermal Landau damping or electromagnetic PIC.
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#references-en>)

  Check momentum/energy conservation, anisotropy relaxation and distribution moments for the homogeneous collision component. Finite-particle equilibrium is microcanonical; Maxwell/Gamma distributions are large-N standards. This does not validate an exact solution of the full spatial Boltzmann equation. The companion derives finite-particle moments on a fixed-momentum/energy sphere and compares independent projected-Gaussian samples across seeds. Collision rounds are not physical time, and the correspondence does not extend to spatial hard-sphere transport.
- [Discrete-ordinate radiation transport through an absorbing slab — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#references-en>)

  Compare discrete ordinates with analytic directional exponential attenuation through a purely absorbing slab with specified inflow. This differs from relativistic M1 moment closure. The companion retains analytic rays and a continuum-angle reference, separating fixed-ordinate spatial error, exact-ray angular error and inflow/outflow/volume-absorption balance. It does not extend to scattering or multidimensional closures.
- [Neutral-cell Ewald sums and an independent theta integral — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-validation>)

  Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.
- [Mesh/order convergence of B-spline smooth PME — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-validation>)

  Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.
- [2D logarithmic FMM with M2M, M2L and L2L — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-validation>)

  For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.
- [Cold-plasma oscillation with electrostatic CIC PIC — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-validation>)

  Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-validation>)

  Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.
- [Discrete-ordinate radiation transport through an absorbing slab — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-validation>)

  With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

## Code and validation

- [Neutral-cell Ewald sums and an independent theta integral](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en>)
  availability: run

  Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.
- [Mesh/order convergence of B-spline smooth PME](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en>)
  availability: run

  A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.
- [Ewald: asymmetric-cell energies and forces versus independent theta integration](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en>)
  availability: run

  Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.
- [SPME: mesh, interpolation order, mesh phase and conservation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en>)
  availability: run

  Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.
- [2D logarithmic FMM with M2M, M2L and L2L](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en>)
  availability: run

  Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.
- [FMM: direct and analytic references, order and tree depth](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en>)
  availability: run

  Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.
- [Cold-plasma oscillation with electrostatic CIC PIC](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en>)
  availability: run

  Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.
- [PIC: mesh/time convergence, invariants and particle noise](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en>)
  availability: run

  Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en>)
  availability: run

  Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.
- [DSMC collision component: finite-N equilibrium, invariants and statistical error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en>)
  availability: run

  Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.
- [Discrete-ordinate radiation transport through an absorbing slab](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en>)
  availability: run

  Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.
- [Radiation transport: space/angle convergence and photon statistics](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en>)
  availability: run

  Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.
