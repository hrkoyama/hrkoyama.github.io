# Mie scattering width of a two-dimensional dielectric cylinder

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Mie scattering width of a two-dimensional dielectric cylinder

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

**Methods used**

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) (`fdtd`)
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) (`leapfrog`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-algorithm)

Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

- [Linear Maxwell fields in vacuum and dielectrics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-en) (`maxwell`)

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.


**Problem figure**

![Mie scattering width of a two-dimensional dielectric cylinder: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en) (`cylinder-mie2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-validation)

Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.

- [Exterior series and scattering width of a dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cylinder-mie2d-en) (`cylinder-mie2d`; Same-problem reference · Analytic reference)

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.
### Assumptions, units and boundaries

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.

**Editorial clarification**

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials. The central white region is a diagnostic mask at r<0.4, distinct from the physical cylinder radius0.25.

### Adopted numerical method

Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

### References and validation

Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.

### Limits

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_and_control_runs": 5,
    "spatial_dimensions": 2,
    "geometry": "Explicitnodalstaircase,noorderclaim",
    "scattering_is_power_integral": true,
    "reference": "IndependentordinarycylindricalJ/H1,notspherical",
    "gallery_source": 145,
    "finest_scattering_width": 0.9571725126288017,
    "independent_scattering_width": 0.9778618212649008,
    "finest_width_relative_error": 0.02115770161610031,
    "finest_exterior_field_relative_error": 0.030278686279997306,
    "complete_run_phasor_linearity": 0.0
  },
  "checks": {
    "reference-and-new-components-qualified": true,
    "cylinder-ppw12/finite": true,
    "cylinder-ppw12/outward-scattering-power": true,
    "cylinder-ppw12/closed-contour-sensitivity": true,
    "cylinder-ppw12/fixed-window-sensitivity": true,
    "cylinder-ppw18/finite": true,
    "cylinder-ppw18/outward-scattering-power": true,
    "cylinder-ppw18/closed-contour-sensitivity": true,
    "cylinder-ppw18/fixed-window-sensitivity": true,
    "cylinder-ppw24/finite": true,
    "cylinder-ppw24/outward-scattering-power": true,
    "cylinder-ppw24/closed-contour-sensitivity": true,
    "cylinder-ppw24/fixed-window-sensitivity": true,
    "finest-scattering-width": true,
    "finest-exterior-scattered-field": true,
    "coarse-to-finest-improvement": true,
    "complete-run-phasor-linearity": true,
    "complete-run-power-quadratic": true,
    "zero-contrast-stored-snapshot-fields": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/index.json

![Real part of the actual saved scattered electric phasor on the finest two-dimensional grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

Real part of the actual saved scattered electric phasor on the finest two-dimensional grid.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Ansys Optics (n.d.). Mie scattering 2D [accessed 2026-11-24]. https://optics.ansys.com/hc/en-us/articles/360042703373-Mie-scattering-2D; review_level=primary-official-documentation-selected-example
Read the complete substantive benchmark description: two-dimensional dielectric cylinder, TFSF, angular far field and lossless cross sections. Did not read the associated simulation files, theory table or cited book; no external numerical data imported. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.

- NIST DLMF. Bessel and Hankel Wronskians, section10.5 (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/10.5; review_level=primary-official-mathematical-identity
Read section 10.5, especially equation 10.5.3 for the ordinary J/Hankel1 Wronskian; version 1.2.8. Cylinder boundary algebra is independently derived here. The year 2026 denotes DLMF version 1.2.8, released on 2026-09-15, not its initial publication year. Accessed on 2026-11-24.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
