# Independent validation of nonlinear reaction–diffusion and pattern formation

Follow a 1D periodic Schnakenberg system from finite-amplitude transients to post-growth patterns. Compare with a separate numerical reference and distinguish grid, time-step and reference errors.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Finite-amplitude Schnakenberg transient: nonlinearity and independent reference

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-algorithm)

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-validation)

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

1D periodic x∈[0,2π), a=.1,b=.9,D=(.01,1). Common IC u=1+.08cos(2x)+.01cos(4x), v=.9−.03cos(2x)−.002cos(4x), restricted to a reflection-even, pi-periodic invariant subspace with a fixed origin.

**Editorial clarification**

Space refinement uses a separate Fourier–Galerkin/Radau reference; time refinement uses an independently integrated Radau solution of the same FD semidiscrete system, not an exact continuous-PDE solution. Splitting error masked spatial error in the first coarse-step pilot. Steps were refined while keeping the acceptance criteria; the original input and failed metrics remain in the release.

### Adopted numerical method

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

### References and validation

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

### Limits

A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations.

### Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_finest_linf": 0.0027896112809786544,
    "temporal_finest_linf": 0.0006354301179647415,
    "minimum_spatial_order": 1.950418112212569,
    "minimum_temporal_order": 1.9845197964375065,
    "reference_spatial_linf": 3.255173908200959e-13,
    "reference_tolerance_linf": 4.4497738826976274e-13,
    "reference_to_primary_error_ratio": 2.7620148525480325e-10,
    "temporal_contamination_ratio": 0.03590744607345364,
    "minimum_concentration": 0.22446801668493407,
    "minimum_newton_iterate": 0.22446801668493407,
    "maximum_midpoint_residual": 1.9676968388004923e-13,
    "maximum_reaction_balance_error": 1.6764367671839864e-14,
    "maximum_newton_iterations": 3,
    "nonlinear_relative_difference": 0.7973947672828199,
    "pattern_amplitude": 1.584854307174442,
    "higher_harmonic_ratio": 0.23973709295898224,
    "dominant_mode_u": 2,
    "mean_u": 1.0212843245725893,
    "mean_v": 0.7809100883890534
  },
  "checks": {
    "spatial_finest_linf": true,
    "temporal_finest_linf": true,
    "reference_spatial_linf": true,
    "reference_tolerance_linf": true,
    "reference_to_primary_error_ratio": true,
    "temporal_contamination_ratio": true,
    "maximum_midpoint_residual": true,
    "maximum_reaction_balance_error": true,
    "minimum_spatial_order": true,
    "minimum_temporal_order": true,
    "positive_without_clipping": true,
    "nonlinear_relative_difference": true,
    "pattern_amplitude": true,
    "higher_harmonic_ratio": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

### Sources and review scope

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://www.mit.edu/~kardar/research/seminars/EPB/Turing.pdf; review_level=original-paper-selected-sections
  Checked the university-hosted original scan, sections 6–7 (printed pp.46–50), ring formulation/linearization and bibliography. Distinct from the adopted coefficients, finite-amplitude reference and mature shape.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  Checked official PubMed bibliography/DOI and publisher-indexed abstract. Full text returned403. Historical source for the reaction family, not a claim to reproduce original coefficients or experiments.
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://epubs.siam.org/doi/pdf/10.1137/0705041; review_level=original-paper-selected-nonlinear-composition
  Checked original pp.510–512 for half-step composition and nonlinear second-order construction. This does not guarantee positivity or accuracy at arbitrary steps in the adopted model.
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=author-lecture-selected-midpoint-and-splitting
  Checked theorem3 and section5 of the author-hosted lecture for implicit-midpoint formula/order and symmetric splitting. Hamiltonian symplectic claims are not transferred to this chemical model.
- The SciPy community (2024). SciPy1.14.1 solve_ivp and Radau reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-api-specification
  Checked official Radau IIA order5, local rtol/atol scaling, analytic Jacobians and termination status. ODE tolerances do not certify global continuum-PDE accuracy.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-algorithm)

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-validation)

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

1D periodic x∈[0,2π), a=.1,b=.9,D=(.01,1). Common IC u=1+.08cos(2x)+.01cos(4x), v=.9−.03cos(2x)−.002cos(4x), restricted to a reflection-even, pi-periodic invariant subspace with a fixed origin.

**Editorial clarification**

Near-stationarity is a finite-time check of the high-accuracy Galerkin reference. A finite-step splitting fixed point need not solve the semidiscrete PDE’s steady equations, so the primary full-RHS residual is reported separately. A large difference from linearization indicates nonlinearity, not accuracy or stationarity. The selected reflection-even, pi-periodic subspace is the scope of the test.

### Adopted numerical method

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

### References and validation

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

### Limits

A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations. Near-saturation refers to the reference90→100 test window; it proves no exact steady state, nonlinear stability or long-term attractor. A huge late linearized difference diagnoses failure of linearization, not numerical error.

### Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_finest_linf": 0.0027421513094392225,
    "temporal_finest_linf": 0.0004451357306107795,
    "minimum_spatial_order": 2.0947550434887137,
    "minimum_temporal_order": 1.7547591906992372,
    "reference_spatial_linf": 5.154365823045737e-11,
    "reference_tolerance_linf": 1.496580637194711e-12,
    "reference_to_primary_error_ratio": 1.9342564607967953e-08,
    "temporal_contamination_ratio": 0.020832217157728455,
    "minimum_concentration": 0.11412754265070092,
    "minimum_newton_iterate": 0.11412754265070092,
    "maximum_midpoint_residual": 1.9676968388004923e-13,
    "maximum_reaction_balance_error": 7.109035582431034e-13,
    "maximum_newton_iterations": 3,
    "nonlinear_relative_difference": 1.1426000574491519e+21,
    "pattern_amplitude": 1.9621659199933201,
    "higher_harmonic_ratio": 0.32273224487596686,
    "dominant_mode_u": 2,
    "mean_u": 1.0000000000005342,
    "mean_v": 0.7497600594170122,
    "saturation_change": 5.0330260847886166e-08,
    "saturation_rhs": 1.8773358978485533e-09,
    "saturation_projected_rhs": 1.877346373585754e-09,
    "saturation_fd_rhs": 0.0011586974655886095,
    "saturation_amplitude_change": 2.517517927458357e-08
  },
  "checks": {
    "spatial_finest_linf": true,
    "temporal_finest_linf": true,
    "reference_spatial_linf": true,
    "reference_tolerance_linf": true,
    "reference_to_primary_error_ratio": true,
    "temporal_contamination_ratio": true,
    "maximum_midpoint_residual": true,
    "maximum_reaction_balance_error": true,
    "minimum_spatial_order": true,
    "minimum_temporal_order": true,
    "positive_without_clipping": true,
    "nonlinear_relative_difference": true,
    "pattern_amplitude": true,
    "higher_harmonic_ratio": true,
    "saturation_change": true,
    "saturation_rhs": true,
    "saturation_amplitude_change": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

### Sources and review scope

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://www.mit.edu/~kardar/research/seminars/EPB/Turing.pdf; review_level=original-paper-selected-sections
  Checked the university-hosted original scan, sections 6–7 (printed pp.46–50), ring formulation/linearization and bibliography. Distinct from the adopted coefficients, finite-amplitude reference and mature shape.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  Checked official PubMed bibliography/DOI and publisher-indexed abstract. Full text returned403. Historical source for the reaction family, not a claim to reproduce original coefficients or experiments.
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://epubs.siam.org/doi/pdf/10.1137/0705041; review_level=original-paper-selected-nonlinear-composition
  Checked original pp.510–512 for half-step composition and nonlinear second-order construction. This does not guarantee positivity or accuracy at arbitrary steps in the adopted model.
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=author-lecture-selected-midpoint-and-splitting
  Checked theorem3 and section5 of the author-hosted lecture for implicit-midpoint formula/order and symmetric splitting. Hamiltonian symplectic claims are not transferred to this chemical model.
- The SciPy community (2024). SciPy1.14.1 solve_ivp and Radau reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-api-specification
  Checked official Radau IIA order5, local rtol/atol scaling, analytic Jacobians and termination status. ODE tolerances do not certify global continuum-PDE accuracy.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
