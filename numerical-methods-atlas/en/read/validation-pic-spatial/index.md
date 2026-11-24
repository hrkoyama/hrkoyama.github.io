# PIC checks against independent spatial kernels

Update the field at every kick using independent CIC and explicit DFT kernels; state the shared temporal algorithm.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Independently coded PIC spatial pipeline

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-algorithm)

The independent path owns scalar deposition, explicit complex DFT sums and scalar gathering; it imports no primary spatial routines. Mathematical CIC, Nyquist convention, velocity-Verlet and initial arrays are intentionally shared.

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.


**Problem figure**

![Independently coded PIC spatial pipeline: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-validation)

19pytest and58/58fixed gates passed. Compare six pairs=twelve self-consistent trajectories at all13states; maximum differences:x8.88e-16,v3.33e-16,E8.33e-16,rho2.89e-15. Shared pytest+main.392s. Initial small pytest retained17/18with a periodic-index failure; integer wrapping was corrected before the first fixed main batch.

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference · Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
### Assumptions, units and boundaries

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

**Editorial clarification**

Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit.

### Adopted numerical method

The independent path owns scalar deposition, explicit complex DFT sums and scalar gathering; it imports no primary spatial routines. Mathematical CIC, Nyquist convention, velocity-Verlet and initial arrays are intentionally shared.

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

### References and validation

19pytest and58/58fixed gates passed. Compare six pairs=twelve self-consistent trajectories at all13states; maximum differences:x8.88e-16,v3.33e-16,E8.33e-16,rho2.89e-15. Shared pytest+main.392s. Initial small pytest retained17/18with a periodic-index failure; integer wrapping was corrected before the first fixed main batch.

### Limits

Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit.

### Stored measurements and decisions

```json
{
  "metrics": {
    "comparison_pairs": 6,
    "separate_trajectories": 12,
    "saved_states_per_trajectory": 13,
    "maximum_position_discrepancy": 8.881784197001252e-16,
    "maximum_velocity_discrepancy": 3.3306690738754696e-16,
    "maximum_field_discrepancy": 8.326672684688674e-16,
    "maximum_charge_discrepancy": 2.886579864025407e-15
  },
  "checks": {
    "primary analytic charge field electron-sign fixture": true,
    "independent analytic charge field electron-sign fixture": true,
    "deliberate wrong electron sign is detected": true,
    "odd-grid force": true,
    "odd-grid field": true,
    "odd-grid charge": true,
    "positive-weight force": true,
    "positive-weight field": true,
    "positive-weight charge": true,
    "n8-seed35001 all saved arrays finite": true,
    "n8-seed35001 all-step position": true,
    "n8-seed35001 all-step velocity": true,
    "n8-seed35001 all-step field": true,
    "n8-seed35001 all-step charge": true,
    "n8-seed35001 independent charge conservation": true,
    "n8-seed35001 independent momentum conservation": true,
    "n8-seed35001 own fields at every fixed kick": true,
    "n8-seed35002 all saved arrays finite": true,
    "n8-seed35002 all-step position": true,
    "n8-seed35002 all-step velocity": true,
    "n8-seed35002 all-step field": true,
    "n8-seed35002 all-step charge": true,
    "n8-seed35002 independent charge conservation": true,
    "n8-seed35002 independent momentum conservation": true,
    "n8-seed35002 own fields at every fixed kick": true,
    "n16-seed35001 all saved arrays finite": true,
    "n16-seed35001 all-step position": true,
    "n16-seed35001 all-step velocity": true,
    "n16-seed35001 all-step field": true,
    "n16-seed35001 all-step charge": true,
    "n16-seed35001 independent charge conservation": true,
    "n16-seed35001 independent momentum conservation": true,
    "n16-seed35001 own fields at every fixed kick": true,
    "n16-seed35002 all saved arrays finite": true,
    "n16-seed35002 all-step position": true,
    "n16-seed35002 all-step velocity": true,
    "n16-seed35002 all-step field": true,
    "n16-seed35002 all-step charge": true,
    "n16-seed35002 independent charge conservation": true,
    "n16-seed35002 independent momentum conservation": true,
    "n16-seed35002 own fields at every fixed kick": true,
    "n32-seed35001 all saved arrays finite": true,
    "n32-seed35001 all-step position": true,
    "n32-seed35001 all-step velocity": true,
    "n32-seed35001 all-step field": true,
    "n32-seed35001 all-step charge": true,
    "n32-seed35001 independent charge conservation": true,
    "n32-seed35001 independent momentum conservation": true,
    "n32-seed35001 own fields at every fixed kick": true,
    "n32-seed35002 all saved arrays finite": true,
    "n32-seed35002 all-step position": true,
    "n32-seed35002 all-step velocity": true,
    "n32-seed35002 all-step field": true,
    "n32-seed35002 all-step charge": true,
    "n32-seed35002 independent charge conservation": true,
    "n32-seed35002 independent momentum conservation": true,
    "n32-seed35002 own fields at every fixed kick": true,
    "six paired comparisons equal twelve separate trajectories": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/index.json

![Actual saved phase space from one of twelve evolutions; color is the self-consistent velocity increment.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial-preview.png)

Actual saved phase space from one of twelve evolutions; color is the self-consistent velocity increment.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme [accessed 2026-11-23]. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
Selected original equations and diagnostic limitations inspected; independently derived continuum references are evaluated here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
