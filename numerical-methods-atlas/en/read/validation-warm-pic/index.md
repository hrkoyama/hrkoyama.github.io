# Warm PIC: Landau damping and two-stream instability

Compare self-consistent weighted full-f PIC with independently formulated dielectric dispersion and linear Volterra IVPs.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Warm PIC linear Landau damping

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-algorithm)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.


**Problem figure**

![Warm PIC linear Landau damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en) (`thermal-landau-damping`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
### Assumptions, units and boundaries

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

**Editorial clarification**

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

### Adopted numerical method

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

### References and validation

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

### Limits

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

### Stored measurements and decisions

```json
{
  "metrics": {
    "mean_rate": -0.15488075370071888,
    "seed_standard_error": 1.4514731389084198e-05,
    "conditional_t95_lower": -0.15492694605400026,
    "conditional_t95_upper": -0.1548345613474375,
    "dielectric_rate": -0.15335946690960467,
    "volterra_fixed_window_rate": -0.1536475740216858,
    "root_window_relative_bias": 0.0018786392381694443,
    "mean_linear_curve_relative_rms": 0.02092398393973105,
    "three_noise_to_minimum_envelope": 5.222378053852797e-12,
    "mesh_rate_fraction": 0.005387063405092717,
    "time-half_rate_fraction": 9.14827746356337e-05,
    "velocity_rate_fraction": 0.0001972171817183033,
    "amplitude-half_rate_fraction": 0.0009187020274627366,
    "amplitude_scaled_curve_gap": 0.004375529905721923,
    "mean_frequency": 1.4127212133462208,
    "frequency_seed_se": 3.853831828103487e-05,
    "dielectric_frequency": 1.4156618886045371,
    "spatial_strata_rate_fraction": 6.62744989007398e-05,
    "spatial_strata_scaled_curve_gap": 0.001153705277393216
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "ten declared Landau full-f calculations": true,
    "thermal-landau-damping-seed33001 all fields and histories finite": true,
    "thermal-landau-damping-seed33001 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33001 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33001 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33001 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33001 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33002 all fields and histories finite": true,
    "thermal-landau-damping-seed33002 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33002 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33002 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33002 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33002 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33003 all fields and histories finite": true,
    "thermal-landau-damping-seed33003 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33003 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33003 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33003 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33003 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33004 all fields and histories finite": true,
    "thermal-landau-damping-seed33004 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33004 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33004 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33004 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33004 resolved fixed-window rate fit": true,
    "thermal-landau-damping-mesh all fields and histories finite": true,
    "thermal-landau-damping-mesh fixed time and five snapshots": true,
    "thermal-landau-damping-mesh charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-mesh positive full-f weights without repair": true,
    "thermal-landau-damping-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-mesh resolved fixed-window rate fit": true,
    "thermal-landau-damping-time-half all fields and histories finite": true,
    "thermal-landau-damping-time-half fixed time and five snapshots": true,
    "thermal-landau-damping-time-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-time-half positive full-f weights without repair": true,
    "thermal-landau-damping-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-time-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-velocity all fields and histories finite": true,
    "thermal-landau-damping-velocity fixed time and five snapshots": true,
    "thermal-landau-damping-velocity charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-velocity positive full-f weights without repair": true,
    "thermal-landau-damping-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-velocity resolved fixed-window rate fit": true,
    "thermal-landau-damping-amplitude-half all fields and histories finite": true,
    "thermal-landau-damping-amplitude-half fixed time and five snapshots": true,
    "thermal-landau-damping-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-amplitude-half positive full-f weights without repair": true,
    "thermal-landau-damping-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-amplitude-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-noise all fields and histories finite": true,
    "thermal-landau-damping-noise fixed time and five snapshots": true,
    "thermal-landau-damping-noise charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-noise positive full-f weights without repair": true,
    "thermal-landau-damping-noise joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata all fields and histories finite": true,
    "thermal-landau-damping-spatial-strata fixed time and five snapshots": true,
    "thermal-landau-damping-spatial-strata charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-spatial-strata positive full-f weights without repair": true,
    "thermal-landau-damping-spatial-strata joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata resolved fixed-window rate fit": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true,
    "mean frequency versus dielectric pole": true,
    "spatial-strata separate rate sensitivity": true,
    "spatial-strata scaled field sensitivity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/index.json

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
Selected original equations and diagnostic limitations inspected; independently derived continuum references are evaluated here.

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
Official Z definition inspected; no PlasmaPy execution.

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
Pinned official quadrature definition read; initialization only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Warm PIC two-stream initial growth

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-algorithm)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.


**Problem figure**

![Warm PIC two-stream initial growth: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en) (`thermal-two-stream`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
### Assumptions, units and boundaries

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.

**Editorial clarification**

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

### Adopted numerical method

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

### References and validation

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

### Limits

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

### Stored measurements and decisions

```json
{
  "metrics": {
    "mean_rate": 0.27311134290987144,
    "seed_standard_error": 0.00015934759074193113,
    "conditional_t95_lower": 0.27260422775845883,
    "conditional_t95_upper": 0.27361845806128404,
    "dielectric_rate": 0.2845096862049824,
    "volterra_fixed_window_rate": 0.27367842777159807,
    "root_window_relative_bias": 0.03806991100324323,
    "mean_linear_curve_relative_rms": 0.02389414539434425,
    "three_noise_to_minimum_envelope": 5.21270074929847e-09,
    "mesh_rate_fraction": 0.002014175281809955,
    "time-half_rate_fraction": 0.0017066353745795366,
    "velocity_rate_fraction": 0.0012636985750053421,
    "amplitude-half_rate_fraction": 9.699235024311375e-05,
    "amplitude_scaled_curve_gap": 0.0009509378138530034
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "thermal-two-stream-seed34001 all fields and histories finite": true,
    "thermal-two-stream-seed34001 fixed time and five snapshots": true,
    "thermal-two-stream-seed34001 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34001 positive full-f weights without repair": true,
    "thermal-two-stream-seed34001 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34001 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34002 all fields and histories finite": true,
    "thermal-two-stream-seed34002 fixed time and five snapshots": true,
    "thermal-two-stream-seed34002 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34002 positive full-f weights without repair": true,
    "thermal-two-stream-seed34002 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34002 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34003 all fields and histories finite": true,
    "thermal-two-stream-seed34003 fixed time and five snapshots": true,
    "thermal-two-stream-seed34003 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34003 positive full-f weights without repair": true,
    "thermal-two-stream-seed34003 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34003 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34004 all fields and histories finite": true,
    "thermal-two-stream-seed34004 fixed time and five snapshots": true,
    "thermal-two-stream-seed34004 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34004 positive full-f weights without repair": true,
    "thermal-two-stream-seed34004 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34004 resolved fixed-window rate fit": true,
    "thermal-two-stream-mesh all fields and histories finite": true,
    "thermal-two-stream-mesh fixed time and five snapshots": true,
    "thermal-two-stream-mesh charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-mesh positive full-f weights without repair": true,
    "thermal-two-stream-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-mesh resolved fixed-window rate fit": true,
    "thermal-two-stream-time-half all fields and histories finite": true,
    "thermal-two-stream-time-half fixed time and five snapshots": true,
    "thermal-two-stream-time-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-time-half positive full-f weights without repair": true,
    "thermal-two-stream-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-time-half resolved fixed-window rate fit": true,
    "thermal-two-stream-velocity all fields and histories finite": true,
    "thermal-two-stream-velocity fixed time and five snapshots": true,
    "thermal-two-stream-velocity charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-velocity positive full-f weights without repair": true,
    "thermal-two-stream-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-velocity resolved fixed-window rate fit": true,
    "thermal-two-stream-amplitude-half all fields and histories finite": true,
    "thermal-two-stream-amplitude-half fixed time and five snapshots": true,
    "thermal-two-stream-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-amplitude-half positive full-f weights without repair": true,
    "thermal-two-stream-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-amplitude-half resolved fixed-window rate fit": true,
    "thermal-two-stream-noise all fields and histories finite": true,
    "thermal-two-stream-noise fixed time and five snapshots": true,
    "thermal-two-stream-noise charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-noise positive full-f weights without repair": true,
    "thermal-two-stream-noise joint load and Gaussian quadrature qualified": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/index.json

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over[12,20].

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
Selected original equations and diagnostic limitations inspected; independently derived continuum references are evaluated here.

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
Official Z definition inspected; no PlasmaPy execution.

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
Pinned official quadrature definition read; initialization only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
