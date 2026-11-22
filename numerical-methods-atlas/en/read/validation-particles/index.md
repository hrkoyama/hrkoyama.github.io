# Particles, electrostatics, kinetic and radiative transport

Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Neutral-cell Ewald sums and an independent theta integral

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-algorithm)

Combine an erfc-screened image sum, Gaussian-damped reciprocal structure factors and the self correction. Differentiate each term and check all 24 force components against central energy differences.

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Neutral-cell Ewald sums and an independent theta integral: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-validation)

Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Cubic cell, zero total charge, Coulomb constant one and conducting/tin-foil boundary. An asymmetric eight-charge case is distinct from the eight-ion NaCl reference cell.

### Adopted numerical method

Combine an erfc-screened image sum, Gaussian-damped reciprocal structure factors and the self correction. Differentiate each term and check all 24 force components against central energy differences.

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

### References and validation

Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.

### Limits

No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

### Stored measurements and decisions

```json
{
  "metrics": {
    "madelung_constant": 1.7475645946331826,
    "theta_reference": 1.7475645946331821,
    "theta_quadrature_error": 1.27151293921409e-13,
    "real_cutoff_force_last_change": 0.0,
    "madelung_error": 4.440892098500626e-16,
    "splitting_energy_difference": 5.329070518200751e-15,
    "splitting_force_difference": 3.8191672047105385e-14,
    "finite_difference_error": 1.7360424209300618e-09,
    "cutoff_force_last_change": 0.0,
    "net_force": 1.1546319456101628e-14
  },
  "checks": {
    "madelung_error": true,
    "splitting_energy_difference": true,
    "splitting_force_difference": true,
    "finite_difference_error": true,
    "cutoff_force_last_change": true,
    "net_force": true,
    "nonzero_forces": true,
    "real_cutoff_refines": true,
    "theta_reference_error_bound": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  Publisher metadata and original section headings checked; no full-text audit claimed.
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Official Jacobi-theta lattice-parameter transformations checked; year denotes access year.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Mesh/order convergence of B-spline smooth PME

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

**Methods used**

- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) (`pme`)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) (`spme`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-algorithm)

Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Mesh/order convergence of B-spline smooth PME: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-validation)

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

The neutral cubic cell and real-space term match the Ewald example. The adopted PME-family variant uses Essmann-type B-splines, distinct from Darden’s original Lagrange interpolation.

### Adopted numerical method

Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

### References and validation

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

### Limits

Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "force_error": 7.855116843202836e-06,
    "energy_error": 8.183940956030256e-07,
    "finest_to_coarsest_force_ratio": 0.0062278365701822136,
    "charge_error": 2.1871393585115584e-14,
    "finite_difference_error": 2.6557447796449196e-08,
    "net_force": 1.919342197087559e-05
  },
  "checks": {
    "force_error": true,
    "energy_error": true,
    "finest_to_coarsest_force_ratio": true,
    "charge_error": true,
    "finite_difference_error": true,
    "both_orders_refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  Original PDF opening and abstract checked; historical original PME is distinguished from the implemented B-spline variant.
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  Original PDF abstract and selected spline/structure-factor, FFT and analytic-gradient material checked; not a reproduction of every paper benchmark.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2D logarithmic FMM with M2M, M2L and L2L

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-algorithm)

Implement leaf P2M, upward M2M, interaction-list M2L, downward L2L, local-polynomial evaluation and near-field P2P. Record translation and near-pair counts; this is not a Barnes–Hut traversal relabeled as FMM.

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![2D logarithmic FMM with M2M, M2L and L2L: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-validation)

For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Particles lie in a unit-square bounding box, not a physical wall boundary. The kernel is phi=−sum(q log r), with field −grad(phi); self terms are excluded and no periodic images are used.

### Adopted numerical method

Implement leaf P2M, upward M2M, interaction-list M2L, downward L2L, local-polynomial evaluation and near-field P2P. Record translation and near-pair counts; this is not a Barnes–Hut traversal relabeled as FMM.

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

### References and validation

For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.

### Limits

No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation.

### Stored measurements and decisions

```json
{
  "metrics": {
    "potential_max_error": 5.953093840105339e-07,
    "field_max_error": 6.36492158818669e-05,
    "finest_to_coarsest_ratio": 3.419465787735687e-05
  },
  "checks": {
    "potential_max_error": true,
    "field_max_error": true,
    "finest_to_coarsest_ratio": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_field_is_subset": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  Institution-hosted reprint consulted for the log kernel, moments, three translations and up/down passes; 1997 reprint distinguished from 1987 original.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Cold-plasma oscillation with electrostatic CIC PIC

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-algorithm)

Combine CIC deposition and matching field gathering, a mean-zero spectral Poisson solve and velocity Verlet. Set the field Nyquist mode to zero for a real skew-adjoint spectral derivative.

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Cold-plasma oscillation with electrostatic CIC PIC: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-validation)

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Dimensionless length 2pi, electron charge/mass −1, stationary ion density one and plasma frequency one. A quiet start receives a small sinusoidal displacement of amplitude 0.001.

### Adopted numerical method

Combine CIC deposition and matching field gathering, a mean-zero spectral Poisson solve and velocity Verlet. Set the field Nyquist mode to zero for a real skew-adjoint spectral derivative.

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

### References and validation

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

### Limits

Finite amplitude and finite particles leave an error floor. Nonlinear instabilities, Landau damping, collisions, electromagnetic/relativistic PIC and open particle boundaries are unvalidated.

### Stored measurements and decisions

```json
{
  "metrics": {
    "mode_error": 0.0008867237363958114,
    "time_mode_error": 0.0004385575782555884,
    "charge_error": 1.743934249004316e-16,
    "poisson_residual": 1.0587911840678754e-22,
    "self_force": 3.3306690738754696e-16,
    "grid_refinement_ratio": 0.05753235309401034,
    "time_refinement_ratio": 0.014260976320524699
  },
  "checks": {
    "mode_error": true,
    "charge_error": true,
    "poisson_residual": true,
    "self_force": true,
    "time_error": true,
    "grid_refines": true,
    "time_refines": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  Publisher preview bibliography, introduction and contents checked; historical source for CIC/cold plasma, not a full-book audit.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-algorithm)

Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Conservation and Maxwell relaxation in a homogeneous DSMC collision component: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-validation)

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Homogeneous, equal masses, isotropic scattering and constant collision rate. Each round randomly matches every particle once. Two initial beams at ±sqrt(3) give target temperature one. Each seed has zero total momentum and fixed total energy: its finite-N equilibrium is microcanonical, while Maxwell/Gamma are large-N references.

### Adopted numerical method

Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

### References and validation

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

### Limits

This is an educational DSMC collision component. No spatial streaming, collision cells, speed-dependent hard-sphere selection, measured transport coefficients/flow fields or every-seed guarantee. Bird’s original hard-sphere conditions are not reproduced.

### Stored measurements and decisions

```json
{
  "metrics": {
    "momentum_error": 1.2923689896027213e-16,
    "energy_error": 2.9605947323337516e-16,
    "variance_error": 0.008371767231336591,
    "fourth_moment_error": 0.06631754023150327,
    "energy_cdf_ks": 0.0017215082600027798,
    "anisotropy_error": 0.011017100788060268,
    "finest_particle_count": 8192,
    "seeds": 16
  },
  "checks": {
    "momentum_error": true,
    "energy_error": true,
    "variance_error": true,
    "fourth_moment_error": true,
    "energy_cdf_ks": true,
    "anisotropy_error": true,
    "sampling_uncertainty_decreases": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
  Official Sandia DSMC commemorative document and DOI metadata checked; publisher text unavailable and the original hard-sphere model is not claimed as reproduced.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Discrete-ordinate radiation transport through an absorbing slab

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-algorithm)

Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Discrete-ordinate radiation transport through an absorbing slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-validation)

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

A uniform slab of optical depth 0.7 receives unit intensity over the positive hemisphere, with zero reverse inflow, scattering and emission.

### Adopted numerical method

Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

### References and validation

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

### Limits

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

### Stored measurements and decisions

```json
{
  "metrics": {
    "ray_max_error": 0.012314628761692092,
    "spatial_flux_error": 0.0011230547235325794,
    "angular_flux_error": 4.558353694505968e-12,
    "balance_error": 9.769962616701378e-15,
    "refinement_ratio": 0.06309366514102617
  },
  "checks": {
    "ray_max_error": true,
    "spatial_flux_error": true,
    "angular_flux_error": true,
    "balance_error": true,
    "refinement_ratio": true,
    "positive_bounded_intensity": true,
    "angular_refines": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
  Publisher HTML bibliography, abstract and base transfer equation checked; cited as discrete-ordinate background, not full DISORT implementation.
- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
  Official integral representation of the generalized exponential integral checked; year denotes access year.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
