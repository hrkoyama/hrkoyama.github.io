# Oblique s/p incidence on a Lorentz-dispersive slab

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Oblique s/p incidence on a Lorentz-dispersive slab

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

**Methods used**

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) (`fdtd`)
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) (`leapfrog`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-algorithm)

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

- [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en) (`maxwell-lorentz`)

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.


**Problem figure**

![Oblique s/p incidence on a Lorentz-dispersive slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-validation)

Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.

- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en) (`lorentz-oblique-sp`; Same-problem reference · Analytic reference)

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.
### Assumptions, units and boundaries

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.

**Editorial clarification**

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.

### Adopted numerical method

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

### References and validation

Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.

### Limits

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_matched_pairs": 6,
    "completed_primary_and_vacuum_evolutions": 12,
    "spatial_dimensions": 2,
    "spatial_restriction": "Actual single-ky Yee evolution with both p electric ADE components.",
    "material_energy_included": true,
    "direct_absorption_not_defined_by_RT": true,
    "final_time": 60.0,
    "finite_window": "One final carrier period is checked; Gaussian tails remain noncompact.",
    "maximum_energy_budget_defect": 1.0729586483899446e-12,
    "maximum_vacuum_calibration_error": 2.7424705908990964e-13,
    "finest_complex_rt_errors": {
      "s": 0.011507167077779438,
      "p": 0.012023386314063115
    },
    "finest_RTA_errors": {
      "s": 0.004990411900537867,
      "p": 0.0022696015641971365
    }
  },
  "checks": {
    "fixed-reference-and-components-qualified": true,
    "lorentz-s-n960/finite": true,
    "lorentz-s-n960/closed-PEC-direct-work-budget": true,
    "lorentz-s-n960/vacuum-energy-budget": true,
    "lorentz-s-n960/nonnegative-material-work": true,
    "lorentz-s-n960/initial-slab-tail": true,
    "lorentz-s-n960/last-carrier-period-monitor-energy": true,
    "lorentz-s-n960/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n960/independent-direct-spectral-work-budget": true,
    "lorentz-s-n1920/finite": true,
    "lorentz-s-n1920/closed-PEC-direct-work-budget": true,
    "lorentz-s-n1920/vacuum-energy-budget": true,
    "lorentz-s-n1920/nonnegative-material-work": true,
    "lorentz-s-n1920/initial-slab-tail": true,
    "lorentz-s-n1920/last-carrier-period-monitor-energy": true,
    "lorentz-s-n1920/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n1920/independent-direct-spectral-work-budget": true,
    "lorentz-s-n3840/finite": true,
    "lorentz-s-n3840/closed-PEC-direct-work-budget": true,
    "lorentz-s-n3840/vacuum-energy-budget": true,
    "lorentz-s-n3840/nonnegative-material-work": true,
    "lorentz-s-n3840/initial-slab-tail": true,
    "lorentz-s-n3840/last-carrier-period-monitor-energy": true,
    "lorentz-s-n3840/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n3840/independent-direct-spectral-work-budget": true,
    "s/finest-complex-rt": true,
    "s/finest-RTA": true,
    "s/refinement-n1920": true,
    "s/refinement-n3840": true,
    "lorentz-p-n960/finite": true,
    "lorentz-p-n960/closed-PEC-direct-work-budget": true,
    "lorentz-p-n960/vacuum-energy-budget": true,
    "lorentz-p-n960/nonnegative-material-work": true,
    "lorentz-p-n960/initial-slab-tail": true,
    "lorentz-p-n960/last-carrier-period-monitor-energy": true,
    "lorentz-p-n960/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n960/independent-direct-spectral-work-budget": true,
    "lorentz-p-n1920/finite": true,
    "lorentz-p-n1920/closed-PEC-direct-work-budget": true,
    "lorentz-p-n1920/vacuum-energy-budget": true,
    "lorentz-p-n1920/nonnegative-material-work": true,
    "lorentz-p-n1920/initial-slab-tail": true,
    "lorentz-p-n1920/last-carrier-period-monitor-energy": true,
    "lorentz-p-n1920/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n1920/independent-direct-spectral-work-budget": true,
    "lorentz-p-n3840/finite": true,
    "lorentz-p-n3840/closed-PEC-direct-work-budget": true,
    "lorentz-p-n3840/vacuum-energy-budget": true,
    "lorentz-p-n3840/nonnegative-material-work": true,
    "lorentz-p-n3840/initial-slab-tail": true,
    "lorentz-p-n3840/last-carrier-period-monitor-energy": true,
    "lorentz-p-n3840/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n3840/independent-direct-spectral-work-budget": true,
    "p/finest-complex-rt": true,
    "p/finest-RTA": true,
    "p/refinement-n1920": true,
    "p/refinement-n3840": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/index.json

![Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Meep developers (n.d.). Meep Materials documentation [accessed 2026-11-24]. https://meep.readthedocs.io/en/latest/Materials/; review_level=primary-official-documentation-selected-sections
Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
