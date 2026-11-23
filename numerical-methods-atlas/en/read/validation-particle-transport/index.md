# Particles and transport: independent references, conservation and statistical error

Extend existing periodic-force, FMM, PIC, collision and radiation problems in a separate release. Separate deterministic discretization, conservation, finite-particle bias and statistical error.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Ewald: asymmetric-cell energies and forces versus independent theta integration

Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-algorithm)

Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Ewald: asymmetric-cell energies and forces versus independent theta integration: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-validation)

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Coulomb constant one; unit cubic 3D periodic neutral cell with tin-foil boundary. The asymmetric configuration matches the earlier example; reference zero-mode and self conventions match the model.

**Editorial clarification**

Compare the asymmetric neutral cubic-cell energy and all 24 force components with a separately coded Gaussian/theta integral. Quadrature, truncation and upper-tail sensitivity apply to this fixed configuration.

### Adopted numerical method

Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

### References and validation

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

### Limits

One fixed neutral cubic cell. Upper-limit sensitivity is not a rigorous tail bound for arbitrary configurations. The theta reference is an independently formulated original implementation, not an external package or published numerical table. Charged/triclinic/slab cells, stress and long MD are outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_energy": -8.407406514350587,
    "reference_energy_refinement": 0.0,
    "reference_force_refinement": 1.7763568394002505e-15,
    "reference_tail_energy": 0.0,
    "reference_tail_force": 1.7763568394002505e-15,
    "reference_quadrature_estimate": 9.6957684120808e-13,
    "energy_error": 3.552713678800501e-15,
    "force_error": 1.2434497875801753e-14,
    "splitting_energy_spread": 3.552713678800501e-15,
    "splitting_force_spread": 7.105427357601002e-14,
    "real_refinement_ratio": 1.520413841404234e-14,
    "reciprocal_refinement_ratio": 4.647403985774097e-13,
    "translation_energy": 3.552713678800501e-15,
    "translation_force": 4.440892098500626e-15,
    "permutation_force": 1.7763568394002505e-15,
    "net_force": 2.842170943040401e-14,
    "gradient_error": 6.119158513229195e-10,
    "control_force_error": 0.8224115526909029
  },
  "checks": {
    "reference_energy_refinement": true,
    "reference_force_refinement": true,
    "reference_tail_energy": true,
    "reference_tail_force": true,
    "reference_quadrature_estimate": true,
    "energy_error": true,
    "force_error": true,
    "splitting_energy_spread": true,
    "splitting_force_spread": true,
    "translation_energy": true,
    "translation_force": true,
    "permutation_force": true,
    "net_force": true,
    "gradient_error": true,
    "real_refinement_ratio": true,
    "reciprocal_refinement_ratio": true,
    "truncation_control_detected": true,
    "asymmetric_forces_nonzero": true,
    "reference_quadrature_converged": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
Publisher metadata and original section headings checked; no full-text audit claimed.

- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
Official Jacobi-theta lattice-parameter transformations checked; year denotes access year.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SPME: mesh, interpolation order, mesh phase and conservation

Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.

**Methods used**

- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) (`pme`)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) (`spme`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-algorithm)

Use 16³/24³/40³ meshes, orders four/six and three translations relative to the mesh. Differentiate FFT reciprocal energy through assignment weights; real/self terms share the primary Ewald implementation.

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![SPME: mesh, interpolation order, mesh phase and conservation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-validation)

Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Same neutral periodic eight-charge cell, alpha=5.6 and three real-space image shells. This is Essmann-style SPME in the PME family, distinct from the original 1993 Lagrange interpolation.

**Editorial clarification**

Use the energy-gradient B-spline SPME variant of the PME family. Measure mesh-phase sensitivity and finite-mesh net force; do not claim exact momentum conservation or original Lagrange-PME reproduction.

### Adopted numerical method

Use 16³/24³/40³ meshes, orders four/six and three translations relative to the mesh. Differentiate FFT reciprocal energy through assignment weights; real/self terms share the primary Ewald implementation.

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

### References and validation

Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.

### Limits

Finite-mesh aliasing generally gives nonzero net force for this energy-gradient variant. No exact momentum conservation, arbitrary-configuration error bound, long MD, original PME or every SPME variant is certified.

### Stored measurements and decisions

```json
{
  "metrics": {
    "fine_energy_error": 8.630229899608821e-07,
    "fine_force_error": 7.855116843202836e-06,
    "force_refinement_ratio": 0.005861182985296622,
    "phase_energy_spread": 1.1496225127416437e-07,
    "phase_force_spread": 1.447734647719301e-05,
    "charge_error": 2.4202861936828413e-14,
    "fine_net_force": 1.919342197087559e-05,
    "maximum_net_force_all_meshes": 0.15409275755368146,
    "shared_ewald_energy_error": 0.0,
    "shared_ewald_force_error": 3.197442310920451e-14,
    "partition_error": 2.8199664825478976e-14,
    "partition_derivative_error": 3.268496584496461e-13,
    "gradient_error": 2.401151921738176e-08,
    "coarse_control_force_error": 0.03526113281182308
  },
  "checks": {
    "fine_energy_error": true,
    "fine_force_error": true,
    "force_refinement_ratio": true,
    "phase_energy_spread": true,
    "phase_force_spread": true,
    "charge_error": true,
    "partition_error": true,
    "partition_derivative_error": true,
    "gradient_error": true,
    "shared_ewald_energy_error": true,
    "shared_ewald_force_error": true,
    "fine_net_force": true,
    "coarse_control_detected": true,
    "both_orders_refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
Original PDF opening and abstract checked; historical original PME is distinguished from the implemented B-spline variant.

- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
Original PDF abstract and selected spline/structure-factor, FFT and analytic-gradient material checked; not a reproduction of every paper benchmark.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## FMM: direct and analytic references, order and tree depth

Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-algorithm)

Retain P2M/M2M/M2L/L2L and near P2P; compare orders 2/4/8/12 and depths two/three. References include independent Cartesian direct sums, a closed-form charge pair and regular-polygon radial/far-field identities.

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![FMM: direct and analytic references, order and tree depth: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-validation)

Measure maximum absolute potential/field errors, actual far translations, rotation/translation differences and net charge-weighted force. Detect an inaccurate low-order control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Free-space phi=−sum(q log r), excluding self terms. The unit square bounds the tree and is not a wall or periodic boundary; this is separate from a 3D Coulomb kernel.

**Editorial clarification**

Measure order, tree-depth and rotation/translation effects for the free-space 2D logarithmic kernel. Do not assume monotone depth improvement or generalize to 3D Coulomb kernels or optimal complexity.

### Adopted numerical method

Retain P2M/M2M/M2L/L2L and near P2P; compare orders 2/4/8/12 and depths two/three. References include independent Cartesian direct sums, a closed-form charge pair and regular-polygon radial/far-field identities.

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

### References and validation

Measure maximum absolute potential/field errors, actual far translations, rotation/translation differences and net charge-weighted force. Detect an inaccurate low-order control.

### Limits

Interaction repartition changes with depth, so fixed-order depth refinement is not assumed monotone. Target-wise expansions need not preserve exact action/reaction. No 3D, adaptive/periodic FMM or complexity-scaling claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "fine_potential_error": 1.6153974611299304e-06,
    "fine_field_error": 0.00013124381103546412,
    "order_refinement_ratio": 7.213976104507879e-05,
    "depth2_field_error": 0.00010463275822658602,
    "net_force_relative": 8.766244233276265e-08,
    "net_force_absolute": 0.00011622325026383606,
    "direct_net_force": 7.283063041541027e-14,
    "coarse_control_field_error": 1.8192992204874692,
    "translation_potential_error": 1.612941820106073e-06,
    "translation_field_error": 0.0004069109892306244,
    "rotation_potential_error": 1.614394697035948e-06,
    "rotation_field_error": 0.00015204244904776232,
    "analytic_direct_potential_error": 0.0,
    "analytic_direct_field_error": 0.0,
    "symmetric_field_error": 6.770015090751258e-06,
    "multipole_potential_error": 1.3839596135767351e-11,
    "multipole_field_error": 1.0251124393789723e-09
  },
  "checks": {
    "fine_potential_error": true,
    "fine_field_error": true,
    "order_refinement_ratio": true,
    "depth2_field_error": true,
    "translation_potential_error": true,
    "translation_field_error": true,
    "rotation_potential_error": true,
    "rotation_field_error": true,
    "net_force_relative": true,
    "analytic_direct_potential_error": true,
    "analytic_direct_field_error": true,
    "symmetric_field_error": true,
    "multipole_potential_error": true,
    "multipole_field_error": true,
    "coarse_control_detected": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_pairs_subset": true,
    "multipole_probe_has_far_translation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
Institution-hosted reprint consulted for the log kernel, moments, three translations and up/down passes; 1997 reprint distinguished from 1987 original.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## PIC: mesh/time convergence, invariants and particle noise

Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-algorithm)

CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![PIC: mesh/time convergence, invariants and particle noise: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-validation)

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference · Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
### Assumptions, units and boundaries

Length 2pi, stationary unit-density ions, electron q/m=−1, plasma frequency one, sinusoidal displacement 0.001 and final time 1.6. Mesh runs retain 2048 particles; time runs retain a 32-cell mesh and 256 particles. The particle weight is w=2pi/N and n is the grid count.

**Editorial clarification**

DOP853 integrates the same particle-grid RHS and is independent only as a time algorithm. Separate quiet-start refinement from random-load noise at time zero; do not claim exact energy conservation.

### Adopted numerical method

CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

### References and validation

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

### Limits

DOP853 is not an independent PIC spatial implementation. Distinguish charge/momentum preservation from approximate energy conservation. Initial-noise N scaling does not validate evolved warm plasmas. Landau damping, electromagnetic/relativistic PIC and collisions remain unvalidated.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_mesh_mode_error": 0.0012829885842868122,
    "minimum_mesh_error_ratio": 3.982691594959013,
    "minimum_time_order": 2.0012021519229015,
    "finest_time_mode_error": 0.0001650650068896753,
    "reference_sensitivity": 6.217248937900877e-12,
    "charge_error": 7.847704120519421e-16,
    "momentum_error": 6.812243160173109e-19,
    "resolved_gauss_error": 2.58493941422823e-26,
    "nyquist_charge": 2.725250580759564e-15,
    "relative_energy_drift": 0.00997018843320538,
    "minimum_shot_scaled_power": 0.9441284361820317,
    "maximum_shot_scaled_power": 1.3013624563118524,
    "minimum_shot_rms_reduction": 1.7035241144134314
  },
  "checks": {
    "continuum_reference": true,
    "mesh_convergence": true,
    "time_convergence": true,
    "independent_time_reference": true,
    "charge": true,
    "momentum": true,
    "resolved_gauss": true,
    "nyquist_charge": true,
    "measured_energy_drift": true,
    "shot_noise_power": true,
    "shot_noise_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
Publisher preview bibliography, introduction and contents checked; historical source for CIC/cold plasma, not a full-book audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## DSMC collision component: finite-N equilibrium, invariants and statistical error

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-algorithm)

Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![DSMC collision component: finite-N equilibrium, invariants and statistical error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-validation)

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Homogeneous equal-mass isotropic Maxwell collisions; N=16/64/256, 64 independent seeds, zero momentum and sum|v|²=3N. Start with two beams and run 24 collision rounds; rounds are not calibrated physical time.

**Editorial clarification**

Use the finite-N equilibrium beta law and independent sphere samples at fixed invariants. Account for particle correlation via independent-seed error; collision rounds are not calibrated time or hard-sphere transport.

### Adopted numerical method

Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

### References and validation

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

### Limits

Statistical diagnostics cover fixed 64-seed ensembles, not every seed. Conservation correlates particles within a seed; do not use IID KS p-values. No spatial streaming, collision cells, speed-dependent hard-sphere selection or transport coefficients.

### Stored measurements and decisions

```json
{
  "metrics": {
    "momentum_error": 2.983724378680108e-16,
    "relative_energy_error": 7.401486830834378e-16,
    "anisotropy_standard_errors": 1.6562460503431053,
    "cdf_standard_errors": 2.244491479985008,
    "independent_equilibrium_standard_errors": 1.7114389804398267,
    "fourth_standard_errors": 1.4292752287239299,
    "maximum_finite_n_maxwell_cdf_bias": 0.01377529224707158,
    "cdf_seed_standard_error_reduction": 3.996517498915623
  },
  "checks": {
    "momentum": true,
    "energy": true,
    "analytic_anisotropy": true,
    "exact_finite_n_cdf": true,
    "independent_equilibrium": true,
    "finite_n_fourth_moment": true,
    "finite_n_distinct_from_maxwell": true,
    "statistical_error_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
Official Sandia DSMC commemorative document and DOI metadata checked; publisher text unavailable and the original hard-sphere model is not claimed as reproduced.

- E. Scalas, A. T. Gabriel, E. Martin and G. Germano (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://arxiv.org/abs/1207.3505; review_level=primary-abstract-and-selected-theory; separate center-of-mass sphere derivation
Initial design reviewed the abstract; subsequent additional review consulted selected finite-system theory. Explicitly derive the zero-momentum sphere marginal here; no original molecular-dynamics data are reused.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Radiation transport: space/angle convergence and photon statistics

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-algorithm)

Use upstream finite volumes and Gauss-Legendre ordinates; exact exponential propagation removes spatial error in the angle series. Monte Carlo independently tracks survival/absorption using mu=sqrt(U) and exponential optical paths.

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Radiation transport: space/angle convergence and photon statistics: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-validation)

Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Steady uniform slab, optical depths .1/.7/3, unit incoming positive-hemisphere intensity, no reverse inflow/scattering/emission. Incoming photon directions for a flux estimator have density 2mu.

**Editorial clarification**

Separate space and angle errors for a pure-absorption slab, comparing characteristics, adaptive quadrature and photon survival. Finite-seed coverage is no all-seed guarantee; scattering and radiation hydrodynamics remain unvalidated.

### Adopted numerical method

Use upstream finite volumes and Gauss-Legendre ordinates; exact exponential propagation removes spatial error in the angle series. Monte Carlo independently tracks survival/absorption using mu=sqrt(U) and exponential optical paths.

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

### References and validation

Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

### Limits

Coverage is observed over finite fixed seeds; neither exactly 95% empirical coverage nor all-seed success is guaranteed. Keep deterministic quadrature error separate from statistical error. Multiple scattering, frequency dependence, thermal emission and radiation hydrodynamics are unvalidated.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_difference": 8.881784197001252e-16,
    "quad_reported_error": 4.357392576641327e-12,
    "minimum_spatial_order": 0.9856180164488282,
    "finest_spatial_flux_error": 0.0022447377157130965,
    "finest_angular_flux_error": 9.019895941264622e-12,
    "minimum_angular_reduction": 291718065.1011767,
    "balance_error": 7.771561172376096e-16,
    "minimum_intensity": 1.9515912759331092e-130,
    "maximum_intensity": 1.0,
    "mc_mean_standard_errors": 1.2889293439083243,
    "minimum_mc_rmse_ratio": 0.8350073934277391,
    "maximum_mc_rmse_ratio": 1.0858116678301433,
    "minimum_measured_coverage": 0.9375,
    "minimum_mc_rmse_reduction": 1.6796261124956355
  },
  "checks": {
    "independent_characteristic_reference": true,
    "reference_quadrature_error": true,
    "spatial_convergence": true,
    "spatial_accuracy": true,
    "angular_accuracy": true,
    "angular_convergence": true,
    "balance": true,
    "positivity": true,
    "mc_mean": true,
    "mc_binomial_error": true,
    "mc_coverage": true,
    "mc_statistical_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### Sources and review scope

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
Publisher HTML bibliography, abstract and base transfer equation checked; cited as discrete-ordinate background, not full DISORT implementation.

- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
Official integral representation of the generalized exponential integral checked; year denotes access year.

- SciPy developers (2024). SciPy 1.14.1: BinomTestResult.proportion_ci. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html; review_level=official-versioned-documentation
Official documentation confirms the exact Clopper–Pearson method and interval API. The 1934 publisher text was unavailable; no full-paper reading is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
