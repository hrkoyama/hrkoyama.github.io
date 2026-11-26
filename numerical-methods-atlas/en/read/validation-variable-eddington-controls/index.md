# Lightweight variable Eddington factor and tensor checks

Iterate angular transport and a separate moment solve for periodic problems with a positive isotropic source, separating analytic-reference errors, balance, and spatial and angular effects.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Variable Eddington factor: a periodic 1D scattering-source control

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

**Methods used**

- [Variable Eddington factor (1D VEF)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en) (`variable-eddington-factor`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-algorithm)

At each iteration solve formal Fourier transport with q+ss E_LO, extract f=Kxx/E_HO, and solve finite-difference moment equations using shared conservative faces. The primary closure never receives the analytic reference.

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`)

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu.


**Problem figure**

![Variable Eddington factor: a periodic 1D scattering-source control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-validation)

Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.

- [Authored continuum Fourier response for periodic 1D VEF](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en) (`vef-fourier-scattering1d`; Same-problem reference · Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
### Assumptions, units and boundaries

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu.

**Editorial clarification**

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

### Adopted numerical method

At each iteration solve formal Fourier transport with q+ss E_LO, extract f=Kxx/E_HO, and solve finite-difference moment equations using shared conservative faces. The primary closure never receives the analytic reference.

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

### References and validation

Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.

### Limits

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 3.0084362898696935e-05,
    "finest_face_H_relative_rms_error": 0.0001843336208869165,
    "finest_mode_complex_relative_error": 0.00046313206947184505,
    "finest_D_component_max_abs_error": 2.562663219352057e-06,
    "E_error_refinement_ratio": 0.2575572363841145,
    "face_H_error_refinement_ratio": 0.25786212296040795,
    "HO_LO_gap_refinement_ratio": 0.2575572378802047,
    "angle_probe_E_relative_rms_difference": 7.903639960737542e-15,
    "angle_probe_D_max_abs_difference": 7.216449660063518e-15,
    "finest_nonconstant_f_span": 0.019387902446938998,
    "finest_max_abs_Dxy": 0.0,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/index.json

![Saved point/face errors, spatial refinement, a separate angular probe and iteration history. The constant source is a separate control.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d-diagnostics.png)

Saved point/face errors, spatial refinement, a separate angular probe and iteration history. The constant source is a separate control.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations [accessed 2026-11-26]. https://academic.oup.com/mnras/article/149/1/65/2604466; review_level=primary-publisher-abstract-and-bibliography
Publisher title/authors/date/DOI and abstract. Establishes historical variable-factor iteration and grey example. Unread limit: Original scannedPDF fetch failed; original equations, full tests and non-LTE calculations are unread and must not be claimed reproduced.

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Unread limit: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.

- A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers [accessed 2026-11-26]. https://arxiv.org/pdf/2111.12255; review_level=selected-primary-method-scope
Introduction PDFpp1–3 on independent HO/LO discretizations, finite-mesh moment differences and conservation; no numerical tables adopted. Unread limit: No claim of reproducing high-orderDG, preconditioner performance or large-mesh studies.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Variable Eddington tensor: a periodic 2D nonparallel-source control

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

**Methods used**

- [Variable Eddington tensor (VET)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en) (`variable-eddington-tensor`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-algorithm)

Iterate formal Fourier angular transport, D=K_HO/E_HO, and an independent finite-difference moment solve. Include both Dxy cross derivatives in shared face fluxes and check local/global discrete budgets.

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`)

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained.


**Problem figure**

![Variable Eddington tensor: a periodic 2D nonparallel-source control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-validation)

Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.

- [Authored continuum Fourier response for periodic 2D VET](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en) (`vet-fourier-source2d`; Same-problem reference · Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.
### Assumptions, units and boundaries

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained.

**Editorial clarification**

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

### Adopted numerical method

Iterate formal Fourier angular transport, D=K_HO/E_HO, and an independent finite-difference moment solve. Include both Dxy cross derivatives in shared face fluxes and check local/global discrete budgets.

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

### References and validation

Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.

### Limits

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 0.00012228131179061114,
    "finest_face_H_relative_rms_error": 0.0010738390026674726,
    "finest_mode_complex_relative_error": 0.0017983436413314031,
    "finest_D_component_max_abs_error": 1.0250275895629102e-05,
    "E_error_refinement_ratio": 0.2655289724016241,
    "face_H_error_refinement_ratio": 0.26613409578253794,
    "HO_LO_gap_refinement_ratio": 0.2657021024383582,
    "angle_probe_E_relative_rms_difference": 2.3900276798110385e-07,
    "angle_probe_D_max_abs_difference": 2.4197709053153105e-07,
    "finest_nonconstant_f_span": 0.022629325122685784,
    "finest_max_abs_Dxy": 0.0052432003949135775,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/index.json

![Saved face-flux errors, Dzz, spatial/angular comparisons and iteration residuals. The full3x3 tensor is retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d-diagnostics.png)

Saved face-flux errors, Dzz, spatial/angular comparisons and iteration residuals. The full3x3 tensor is retained.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2223; review_level=selected-primary-equations-and-test-description
Section3.1 algorithmStep1; Section3.4 PDFp8, equations22–23 and discussion; Section6.5 shadow-test scope description read. Unread limit: Not a reproduction of Athena, mixed-frameRHD, gas coupling, shocks or the paper shadow/cloud-ablation test.

- A Radiation Transfer Solver for Athena using Short Characteristics [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2222; review_level=selected-primary-equations
Equations8–16 source/opacity/moment conventions, Section3.2 angular quadrature Eq17–19 and two-stream warning; Section3.3 Eq20 formal solution and Section3.5 boundary scope read. Unread limit: Proposed Fourier formal solver is not their short-characteristics/interpolation algorithm. No multifrequency, ALI, stellar atmosphere or timing reproduction claim.

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Unread limit: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.

- A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method [accessed 2026-11-26]. https://arxiv.org/pdf/1306.0010; review_level=selected-primary-equations
Section2.3 PDFp5, equations11–17: localM1 tensor, trace/covariance constraints and chi(reducedflux). Introduction distinction from formalVET also read. Unread limit: No Hyperion/RHD solver or reduced-light-speed/timing validation. InstitutionalPDF endpoint returned401; arXiv original-author copy was read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
