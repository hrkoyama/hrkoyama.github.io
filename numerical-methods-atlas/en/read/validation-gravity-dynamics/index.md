# Gravitational trajectories: Kepler and softened finite particles

Distinguish exact Kepler trajectories from short-time finite-particle references using the identical softened ODE.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Unsoftened Kepler two-body time error

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-algorithm)

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.


**Problem figure**

![Unsoftened Kepler two-body time error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-validation)

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference · Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en) (`kepler-eccentricity`; Same-problem reference · Semi-analytic reference)

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.
### Assumptions, units and boundaries

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

**Editorial clarification**

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

### Adopted numerical method

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

### References and validation

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

### Limits

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_position_error": 0.0016120499258598436,
    "finest_energy_drift": 0.00017450491925918854,
    "period": 6.283185307179586
  },
  "checks": {
    "s128 finite synchronized fields": true,
    "s128 fixed final time": true,
    "s128 positive pair separation": true,
    "s128 momentum_drift": true,
    "s128 angular_drift": true,
    "s128 com_drift": true,
    "s128 Kepler root residual": true,
    "s128 independent final pair force": true,
    "s256 finite synchronized fields": true,
    "s256 fixed final time": true,
    "s256 positive pair separation": true,
    "s256 momentum_drift": true,
    "s256 angular_drift": true,
    "s256 com_drift": true,
    "s256 Kepler root residual": true,
    "s256 independent final pair force": true,
    "s512 finite synchronized fields": true,
    "s512 fixed final time": true,
    "s512 positive pair separation": true,
    "s512 momentum_drift": true,
    "s512 angular_drift": true,
    "s512 com_drift": true,
    "s512 Kepler root residual": true,
    "s512 independent final pair force": true,
    "analytic reference energy identity": true,
    "analytic reference angular identity": true,
    "analytic reference COM identity": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest Kepler position": true,
    "finest Kepler energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/index.json

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

Validation figure from actual saved fixed-input calculation arrays.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- JPL Keplerian-element formulas. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=official-selected-kepler-equation
Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Short-time32body dynamics from a cold Plummer-density sample

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)
- [Barnes–Hut octree](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en) (`barnes-hut`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-algorithm)

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.


**Problem figure**

![Short-time32body dynamics from a cold Plummer-density sample: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-validation)

Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en) (`gravity-plummer-short`; Same-problem reference · Finite-grid numerical reference)

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.
### Assumptions, units and boundaries

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

**Editorial clarification**

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

### Adopted numerical method

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

### References and validation

Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.

### Limits

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_tolerance_gap": 1.3339329640871256e-12,
    "finest_direct_error": 8.032388866139367e-09,
    "finest_energy_drift": 8.566574106443163e-09,
    "theta035_trajectory": 5.672453506265489e-07,
    "asymmetric_net_force": 2.3712429943822043e-05
  },
  "checks": {
    "independent ODE tolerance qualification": true,
    "independent reference energy": true,
    "independent reference momentum": true,
    "independent reference angular momentum": true,
    "antipodal initial COM": true,
    "direct-s20 finite synchronized fields": true,
    "direct-s20 fixed final time": true,
    "direct-s20 positive pair separation": true,
    "direct-s20 momentum_drift": true,
    "direct-s20 angular_drift": true,
    "direct-s20 com_drift": true,
    "direct-s40 finite synchronized fields": true,
    "direct-s40 fixed final time": true,
    "direct-s40 positive pair separation": true,
    "direct-s40 momentum_drift": true,
    "direct-s40 angular_drift": true,
    "direct-s40 com_drift": true,
    "direct-s80 finite synchronized fields": true,
    "direct-s80 fixed final time": true,
    "direct-s80 positive pair separation": true,
    "direct-s80 momentum_drift": true,
    "direct-s80 angular_drift": true,
    "direct-s80 com_drift": true,
    "theta0 finite synchronized fields": true,
    "theta0 fixed final time": true,
    "theta0 positive pair separation": true,
    "theta0 momentum_drift": true,
    "theta0 angular_drift": true,
    "theta0 com_drift": true,
    "theta0 trajectory reproduces direct": true,
    "theta0 same-position force identity": true,
    "theta0.35 finite synchronized fields": true,
    "theta0.35 fixed final time": true,
    "theta0.35 positive pair separation": true,
    "theta.35 trajectory error": true,
    "theta.35 same-position force error": true,
    "theta0.6 finite synchronized fields": true,
    "theta0.6 fixed final time": true,
    "theta0.6 positive pair separation": true,
    "theta.6 actual accepted nodes": true,
    "theta.6 same-position force error": true,
    "direct time refinement 1": true,
    "direct time refinement 2": true,
    "finest direct state error": true,
    "finest direct energy": true,
    "asymmetric diagnostics finite": true,
    "asymmetric tree approximation exercised": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/index.json

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

Validation figure from actual saved fixed-input calculation arrays.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- On the Problem of Distribution in Globular Star Clusters. https://academic.oup.com/mnras/article/71/5/460/972150; review_level=bibliography-only-original-unaccessed
Bibliography inherited from prior scoped source review; original full text not read. The finite32-body cold initial condition is density-derived, not an equilibrium Plummer DF or exact continuum flow.

- galpy official Plummer potential definition. https://docs.galpy.org/en/v1.11.0/reference/potentialplummer.html; review_level=official-potential-definition
Official potential normalization read in preparatory source review. No galpy execution; density scale1 and pair softening.05 are distinct parameters.

- SciPy1.14.1 solve_ivp. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-method-api
DOP853 order8, tolerance and t_eval semantics inspected; same softened finite-N ODE with independent scalar pair force. Not an exact analytic N-body solution.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
