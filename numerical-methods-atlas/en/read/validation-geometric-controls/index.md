# Geometric integration of constraints, orbits and multiple frequencies

Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## SHAKE and RATTLE: constraints and momentum ownership

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.

**Methods used**

- [SHAKE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=en) (`shake`)
- [RATTLE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=en) (`rattle`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-algorithm)

Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`)

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.


**Problem figure**

![SHAKE and RATTLE: constraints and momentum ownership: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-validation)

A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference · Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference · Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
### Assumptions, units and boundaries

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

**Editorial clarification**

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

### References and validation

A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

### Limits

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

### Stored measurements and decisions

```json
{
  "metrics": {
    "rattle_observed_orders": [
      2.0002044529735445,
      2.0000564458078465
    ],
    "shake_observed_orders": [
      2.000077432739235,
      2.0000041345609065
    ],
    "reduced_map_probes": [
      {
        "state": [
          0.7,
          0.0
        ],
        "symplectic_defect": 3.424459604772778e-10,
        "FD_difference": 1.7850310118916468e-10
      },
      {
        "state": [
          0.3,
          0.2
        ],
        "symplectic_defect": 3.746203347532173e-11,
        "FD_difference": 1.8735013540549517e-10
      },
      {
        "state": [
          -0.4,
          -0.3
        ],
        "symplectic_defect": 1.2937362292575472e-10,
        "FD_difference": 2.7755575615628914e-10
      }
    ],
    "evolution_count": 10,
    "centered_SHAKE_not_RATTLE_tangent": true,
    "maximum_constraint": 3.811062576630775e-12
  },
  "checks": {
    "rattle-tight-2500-finite": true,
    "rattle-tight-2500-completed": true,
    "rattle-tight-2500-constraint": true,
    "rattle-tight-2500-state": true,
    "rattle-tight-2500-energy": true,
    "rattle-tight-2500-solver": true,
    "rattle-tight-2500-tangent": true,
    "rattle-tight-5000-finite": true,
    "rattle-tight-5000-completed": true,
    "rattle-tight-5000-constraint": true,
    "rattle-tight-5000-state": true,
    "rattle-tight-5000-energy": true,
    "rattle-tight-5000-solver": true,
    "rattle-tight-5000-tangent": true,
    "rattle-tight-10000-finite": true,
    "rattle-tight-10000-completed": true,
    "rattle-tight-10000-constraint": true,
    "rattle-tight-10000-state": true,
    "rattle-tight-10000-energy": true,
    "rattle-tight-10000-solver": true,
    "rattle-tight-10000-tangent": true,
    "rattle-loose-2500-finite": true,
    "rattle-loose-2500-completed": true,
    "rattle-loose-2500-constraint": true,
    "rattle-loose-2500-state": true,
    "rattle-loose-2500-energy": true,
    "rattle-loose-2500-solver": true,
    "rattle-loose-2500-tangent": true,
    "rattle-reverse-finite": true,
    "rattle-reverse-steps": true,
    "rattle-reverse-recovery": true,
    "shake-tight-2500-finite": true,
    "shake-tight-2500-completed": true,
    "shake-tight-2500-constraint": true,
    "shake-tight-2500-state": true,
    "shake-tight-2500-energy": true,
    "shake-tight-2500-solver": true,
    "shake-tight-2500-finite-C-identity": true,
    "shake-tight-2500-centered-tangency": true,
    "shake-tight-5000-finite": true,
    "shake-tight-5000-completed": true,
    "shake-tight-5000-constraint": true,
    "shake-tight-5000-state": true,
    "shake-tight-5000-energy": true,
    "shake-tight-5000-solver": true,
    "shake-tight-5000-finite-C-identity": true,
    "shake-tight-5000-centered-tangency": true,
    "shake-tight-10000-finite": true,
    "shake-tight-10000-completed": true,
    "shake-tight-10000-constraint": true,
    "shake-tight-10000-state": true,
    "shake-tight-10000-energy": true,
    "shake-tight-10000-solver": true,
    "shake-tight-10000-finite-C-identity": true,
    "shake-tight-10000-centered-tangency": true,
    "shake-loose-2500-finite": true,
    "shake-loose-2500-completed": true,
    "shake-loose-2500-constraint": true,
    "shake-loose-2500-state": true,
    "shake-loose-2500-energy": true,
    "shake-loose-2500-solver": true,
    "shake-loose-2500-finite-C-identity": true,
    "shake-loose-2500-centered-tangency": true,
    "shake-reverse-finite": true,
    "shake-reverse-steps": true,
    "shake-reverse-recovery": true,
    "rattle-state-order": true,
    "shake-state-order": true,
    "reduced-map-0-symplectic-proxy": true,
    "reduced-map-0-FD-consistency": true,
    "reduced-map-1-symplectic-proxy": true,
    "reduced-map-1-FD-consistency": true,
    "reduced-map-2-symplectic-proxy": true,
    "reduced-map-2-FD-consistency": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/index.json

![Saved reduced phase portraits at h=0.01. SHAKE uses interior centered momentum; RATTLE uses full-time tangent momentum.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum-preview.png)

Saved reduced phase portraits at h=0.01. SHAKE uses interior centered momentum; RATTLE uses full-time tangent momentum.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Solving Differential Equations on Manifolds [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly-sde-mani.pdf; review_level=selected-primary-scope
Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed.

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- DLMF22.4: Periods, Poles, and Zeros (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/22.4; review_level=selected-primary-scope
Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Kepler eccentricity and time-step controls

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-algorithm)

Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

- [Kepler two-body problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kepler-two-body-en) (`kepler-two-body`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.


**Problem figure**

![Kepler eccentricity and time-step controls: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-validation)

An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference · Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en) (`kepler-eccentricity`; Same-problem reference · Semi-analytic reference)

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.
### Assumptions, units and boundaries

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

**Editorial clarification**

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

### References and validation

An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

### Limits

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

### Stored measurements and decisions

```json
{
  "metrics": {
    "e0.1_orders": [
      1.9999876782390122,
      1.9999962905452664
    ],
    "e0.7_orders": [
      1.987542094585538,
      2.000215589787777
    ],
    "evolution_count": 16,
    "variable_map_symplecticity_measured": false,
    "max_state_error": 0.39849708597264355
  },
  "checks": {
    "e0p1-fixed-512-finite": true,
    "e0p1-fixed-512-time": true,
    "e0p1-fixed-512-radius": true,
    "e0p1-fixed-512-angular": true,
    "e0p1-fixed-512-energy": true,
    "e0p1-fixed-512-reference": true,
    "e0p1-fixed-1024-finite": true,
    "e0p1-fixed-1024-time": true,
    "e0p1-fixed-1024-radius": true,
    "e0p1-fixed-1024-angular": true,
    "e0p1-fixed-1024-energy": true,
    "e0p1-fixed-1024-reference": true,
    "e0p1-fixed-2048-finite": true,
    "e0p1-fixed-2048-time": true,
    "e0p1-fixed-2048-radius": true,
    "e0p1-fixed-2048-angular": true,
    "e0p1-fixed-2048-energy": true,
    "e0p1-fixed-2048-reference": true,
    "e0p1-fixed-long-finite": true,
    "e0p1-fixed-long-time": true,
    "e0p1-fixed-long-radius": true,
    "e0p1-fixed-long-angular": true,
    "e0p1-fixed-long-energy": true,
    "e0p1-fixed-long-reference": true,
    "e0p1-fixed-long-periapsis-count": true,
    "e0p1-fixed-long-periapsis-time": true,
    "e0p1-variable-long-finite": true,
    "e0p1-variable-long-time": true,
    "e0p1-variable-long-radius": true,
    "e0p1-variable-long-angular": true,
    "e0p1-variable-long-energy": true,
    "e0p1-variable-long-reference": true,
    "e0p1-variable-long-periapsis-count": true,
    "e0p1-variable-long-periapsis-time": true,
    "e0p1-reverse-fixed-finite": true,
    "e0p1-reverse-fixed-schedule": true,
    "e0p1-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-replay-finite": true,
    "e0p1-reverse-variable-replay-schedule": true,
    "e0p1-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-regenerated-finite": true,
    "e0p1-reverse-variable-regenerated-schedule": true,
    "e0p1-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0p7-fixed-512-finite": true,
    "e0p7-fixed-512-time": true,
    "e0p7-fixed-512-radius": true,
    "e0p7-fixed-512-angular": true,
    "e0p7-fixed-512-energy": true,
    "e0p7-fixed-512-reference": true,
    "e0p7-fixed-1024-finite": true,
    "e0p7-fixed-1024-time": true,
    "e0p7-fixed-1024-radius": true,
    "e0p7-fixed-1024-angular": true,
    "e0p7-fixed-1024-energy": true,
    "e0p7-fixed-1024-reference": true,
    "e0p7-fixed-2048-finite": true,
    "e0p7-fixed-2048-time": true,
    "e0p7-fixed-2048-radius": true,
    "e0p7-fixed-2048-angular": true,
    "e0p7-fixed-2048-energy": true,
    "e0p7-fixed-2048-reference": true,
    "e0p7-fixed-long-finite": true,
    "e0p7-fixed-long-time": true,
    "e0p7-fixed-long-radius": true,
    "e0p7-fixed-long-angular": true,
    "e0p7-fixed-long-energy": true,
    "e0p7-fixed-long-reference": true,
    "e0p7-fixed-long-periapsis-count": true,
    "e0p7-fixed-long-periapsis-time": true,
    "e0p7-variable-long-finite": true,
    "e0p7-variable-long-time": true,
    "e0p7-variable-long-radius": true,
    "e0p7-variable-long-angular": true,
    "e0p7-variable-long-energy": true,
    "e0p7-variable-long-reference": true,
    "e0p7-variable-long-periapsis-count": true,
    "e0p7-variable-long-periapsis-time": true,
    "e0p7-reverse-fixed-finite": true,
    "e0p7-reverse-fixed-schedule": true,
    "e0p7-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-replay-finite": true,
    "e0p7-reverse-variable-replay-schedule": true,
    "e0p7-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-regenerated-finite": true,
    "e0p7-reverse-variable-regenerated-schedule": true,
    "e0p7-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0.1-fine-state": true,
    "e0.1-state-order": true,
    "e0.1-fine-energy": true,
    "e0.7-fine-state": true,
    "e0.7-state-order": true,
    "e0.7-fine-energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/index.json

![Saved ten-period fixed-step and variable-step orbits at e=0.7, shown with equal physical aspect and an unsoftened central force.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity-preview.png)

Saved ten-period fixed-step and variable-step orbits at e=0.7, shown with equal physical aspect and an unsoftened central force.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- Approximate Positions of the Planets [accessed 2026-11-24]. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=selected-primary-scope
Official JPL page, selected steps3–4 and Kepler equation. Only the eccentric-anomaly equation and elliptic coordinate transformation are used; no planetary coefficient tables, fitted ephemeris accuracy or Horizons calculation is claimed. Publication date was not verified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Coupled frequencies and finite-window resonance

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-algorithm)

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

- [Coupled two-frequency harmonic oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en) (`coupled-harmonic-oscillators`)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.


**Problem figure**

![Coupled frequencies and finite-window resonance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-validation)

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en) (`multifrequency-resonance`; Same-problem reference · Semi-analytic reference)

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.
### Assumptions, units and boundaries

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

**Editorial clarification**

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

### References and validation

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

### Limits

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

### Stored measurements and decisions

```json
{
  "metrics": {
    "verlet_observed_orders": [
      2.0006335257949495,
      2.0004237164828513
    ],
    "impulse_observed_orders": [
      2.000688773919643,
      2.0001158542645605
    ],
    "evolution_count": 18,
    "probe_steps": 64,
    "ideal_pi_separate_from_actual_float": true,
    "maximum_frozen_map_relative_error": 2.432468376162801e-15
  },
  "checks": {
    "w10-verlet-1p0-finite-cap": true,
    "w10-verlet-1p0-completed": true,
    "w10-verlet-1p0-discrete-reference": true,
    "w10-verlet-1p0-roundoff": true,
    "w10-verlet-1p0-symplectic": true,
    "w10-verlet-1p0-classification": true,
    "w10-verlet-1p8-finite-cap": true,
    "w10-verlet-1p8-completed": true,
    "w10-verlet-1p8-discrete-reference": true,
    "w10-verlet-1p8-roundoff": true,
    "w10-verlet-1p8-symplectic": true,
    "w10-verlet-1p8-classification": true,
    "w10-verlet-2p2-finite-cap": true,
    "w10-verlet-2p2-completed": true,
    "w10-verlet-2p2-discrete-reference": true,
    "w10-verlet-2p2-roundoff": true,
    "w10-verlet-2p2-symplectic": true,
    "w10-verlet-2p2-classification": true,
    "w10-impulse-0p9-finite-cap": true,
    "w10-impulse-0p9-completed": true,
    "w10-impulse-0p9-discrete-reference": true,
    "w10-impulse-0p9-roundoff": true,
    "w10-impulse-0p9-symplectic": true,
    "w10-impulse-0p9-classification": true,
    "w10-impulse-1p0-finite-cap": true,
    "w10-impulse-1p0-completed": true,
    "w10-impulse-1p0-discrete-reference": true,
    "w10-impulse-1p0-roundoff": true,
    "w10-impulse-1p0-symplectic": true,
    "w10-impulse-1p0-classification": true,
    "w10-impulse-1p1-finite-cap": true,
    "w10-impulse-1p1-completed": true,
    "w10-impulse-1p1-discrete-reference": true,
    "w10-impulse-1p1-roundoff": true,
    "w10-impulse-1p1-symplectic": true,
    "w10-impulse-1p1-classification": true,
    "w20-verlet-1p0-finite-cap": true,
    "w20-verlet-1p0-completed": true,
    "w20-verlet-1p0-discrete-reference": true,
    "w20-verlet-1p0-roundoff": true,
    "w20-verlet-1p0-symplectic": true,
    "w20-verlet-1p0-classification": true,
    "w20-verlet-1p8-finite-cap": true,
    "w20-verlet-1p8-completed": true,
    "w20-verlet-1p8-discrete-reference": true,
    "w20-verlet-1p8-roundoff": true,
    "w20-verlet-1p8-symplectic": true,
    "w20-verlet-1p8-classification": true,
    "w20-verlet-2p2-finite-cap": true,
    "w20-verlet-2p2-completed": true,
    "w20-verlet-2p2-discrete-reference": true,
    "w20-verlet-2p2-roundoff": true,
    "w20-verlet-2p2-symplectic": true,
    "w20-verlet-2p2-classification": true,
    "w20-impulse-0p9-finite-cap": true,
    "w20-impulse-0p9-completed": true,
    "w20-impulse-0p9-discrete-reference": true,
    "w20-impulse-0p9-roundoff": true,
    "w20-impulse-0p9-symplectic": true,
    "w20-impulse-0p9-classification": true,
    "w20-impulse-1p0-finite-cap": true,
    "w20-impulse-1p0-completed": true,
    "w20-impulse-1p0-discrete-reference": true,
    "w20-impulse-1p0-roundoff": true,
    "w20-impulse-1p0-symplectic": true,
    "w20-impulse-1p0-classification": true,
    "w20-impulse-1p1-finite-cap": true,
    "w20-impulse-1p1-completed": true,
    "w20-impulse-1p1-discrete-reference": true,
    "w20-impulse-1p1-roundoff": true,
    "w20-impulse-1p1-symplectic": true,
    "w20-impulse-1p1-classification": true,
    "w10-verlet-accuracy-500-finite": true,
    "w10-verlet-accuracy-500-completed": true,
    "w10-verlet-accuracy-500-state": true,
    "w10-verlet-accuracy-500-energy": true,
    "w10-verlet-accuracy-500-mode": true,
    "w10-verlet-accuracy-500-discrete-reference": true,
    "w10-verlet-accuracy-1000-finite": true,
    "w10-verlet-accuracy-1000-completed": true,
    "w10-verlet-accuracy-1000-state": true,
    "w10-verlet-accuracy-1000-energy": true,
    "w10-verlet-accuracy-1000-mode": true,
    "w10-verlet-accuracy-1000-discrete-reference": true,
    "w10-verlet-accuracy-2000-finite": true,
    "w10-verlet-accuracy-2000-completed": true,
    "w10-verlet-accuracy-2000-state": true,
    "w10-verlet-accuracy-2000-energy": true,
    "w10-verlet-accuracy-2000-mode": true,
    "w10-verlet-accuracy-2000-discrete-reference": true,
    "w10-impulse-accuracy-500-finite": true,
    "w10-impulse-accuracy-500-completed": true,
    "w10-impulse-accuracy-500-state": true,
    "w10-impulse-accuracy-500-energy": true,
    "w10-impulse-accuracy-500-mode": true,
    "w10-impulse-accuracy-500-discrete-reference": true,
    "w10-impulse-accuracy-1000-finite": true,
    "w10-impulse-accuracy-1000-completed": true,
    "w10-impulse-accuracy-1000-state": true,
    "w10-impulse-accuracy-1000-energy": true,
    "w10-impulse-accuracy-1000-mode": true,
    "w10-impulse-accuracy-1000-discrete-reference": true,
    "w10-impulse-accuracy-2000-finite": true,
    "w10-impulse-accuracy-2000-completed": true,
    "w10-impulse-accuracy-2000-state": true,
    "w10-impulse-accuracy-2000-energy": true,
    "w10-impulse-accuracy-2000-mode": true,
    "w10-impulse-accuracy-2000-discrete-reference": true,
    "verlet-state-order": true,
    "verlet-fine-state": true,
    "verlet-fine-relative-H": true,
    "verlet-fine-coordinate-energy": true,
    "impulse-state-order": true,
    "impulse-fine-state": true,
    "impulse-fine-relative-H": true,
    "impulse-fine-coordinate-energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/index.json

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
