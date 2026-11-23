# Neutral slabs: corrected3P and genuine2P references

Freeze rectangular boxes and the nonperiodic-z branch; compare the Yeh–Berkowitz correction with a genuine2P reference including self and zero modes.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Neutral rectangular slab: genuine2P reference and YB

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.

**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)
- [Slab electrostatics and 2D-periodic Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=en) (`slab-ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-algorithm)

Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

- [Coulomb electrostatics with mixed periodic boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en) (`coulomb-electrostatics`)

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.


**Problem figure**

![Neutral rectangular slab: genuine2P reference and YB: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) (`neutral-slab-yb`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-validation)

Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.

- [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en) (`neutral-slab-yb`; Same-problem reference · Semi-analytic reference)

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.
### Assumptions, units and boundaries

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

**Editorial clarification**

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

### Adopted numerical method

Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

### References and validation

Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.

### Limits

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_energy": -4.45950558164492,
    "maximum_reference_force": 5.484895963941495,
    "dipole_z": 0.33999999999999997,
    "finest_energy_error": 4.618527782440651e-14,
    "finest_force_error": 1.0009770790020411e-12
  },
  "checks": {
    "reference splitting energy": true,
    "reference splitting force": true,
    "reference cutoff energy": true,
    "reference cutoff force": true,
    "z1.5-a3 finite saved fields": true,
    "z1.5-a3 neutral net force": true,
    "z1.5-a4 finite saved fields": true,
    "z1.5-a4 neutral net force": true,
    "z3-a3 finite saved fields": true,
    "z3-a3 neutral net force": true,
    "z3-a4 finite saved fields": true,
    "z3-a4 neutral net force": true,
    "z6-a3 finite saved fields": true,
    "z6-a3 neutral net force": true,
    "z6-a4 finite saved fields": true,
    "z6-a4 neutral net force": true,
    "z1.5 alpha energy": true,
    "z1.5 alpha force": true,
    "z3 alpha energy": true,
    "z3 alpha force": true,
    "z6 alpha energy": true,
    "z6 alpha force": true,
    "z6-a3 finest energy": true,
    "z6-a3 finest force": true,
    "z6-a3 correction improves energy": true,
    "z6-a3 correction improves force": true,
    "z6-a4 finest energy": true,
    "z6-a4 finest force": true,
    "z6-a4 correction improves energy": true,
    "z6-a4 correction improves force": true,
    "neutral translation energy": true,
    "neutral translation force": true,
    "production energy gradient h1e-05": true,
    "reference energy gradient h1e-05": true,
    "production energy gradient h5e-06": true,
    "reference energy gradient h5e-06": true,
    "omitted zero mode is detected": true,
    "far-z potential step": true,
    "far-z zero field": true,
    "source permutation energy": true,
    "source permutation force": true,
    "charged cell rejected": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/index.json

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

Validation figure from actual saved fixed-input calculation arrays.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Fast and spectrally accurate Ewald summation for2-periodic electrostatic systems. https://arxiv.org/pdf/1109.1667; review_level=primary-selected-equations
Eq4 and AppendixA Eq41/zero-mode inspected; rendered selected pages requested. No full-paper audit or spectral-PME implementation claimed.

- Ewald summation for systems with slab geometry. https://doi.org/10.1063/1.479595; review_level=bibliography-original-unaccessed
Original publisher full text unavailable; no original-text review claimed. Neutral correction independently derived and checked against official LAMMPS implementation/documentation.

- LAMMPS slab Ewald documentation and neutral correction. https://docs.lammps.org/kspace_modify.html; review_level=official-selected-docs-and-formulas
Slab geometry restrictions and official Ewald::slabcorr neutral formula inspected. No LAMMPS code copied or executed; mutable stable source is contextual, not a numerical dependency.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
