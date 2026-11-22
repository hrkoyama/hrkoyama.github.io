# MCMC, temperature control and biological models

Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Gaussian-target MCMC: distribution, autocorrelation and ESS

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

### Assumptions, units and boundaries

One dimensionless variable and symmetric Gaussian random-walk width1.5. Spawn 32 separate PCG64 streams from a fixed master seed; retain 8192 samples per chain after 1024 burn-in steps.

### Adopted numerical method

Use a log-acceptance Metropolis update. Pool FFT within-chain autocovariances and obtain mean-observable ESS from Geyer initial-positive pairs starting at gamma0+gamma1. Also report classical split-Rhat.

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

### References and validation

Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.

### Limits

Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate.

### Stored measurements and decisions

```json
{
  "metrics": {
    "mean_error": 0.010631777843262634,
    "variance_error": 0.002245617179238435,
    "cdf_max_error": 0.0032519421134648008,
    "acceptance": 0.5894775390625,
    "tau": 5.380318100624768,
    "ess": 48722.769750279185,
    "split_rhat": 1.0004379739161546,
    "acf_lag1": 0.6804539280760109,
    "ar1_exact_tau": 9.000000000000002,
    "ar1_series_tau_error": 1.7763568394002505e-15,
    "ar1_empirical_tau_relative_error": 0.012439210859068739,
    "budget_mean_rmse_ratio": 2.949230534359497
  },
  "checks": {
    "finite": true,
    "mean": true,
    "variance": true,
    "cdf": true,
    "split_rhat": true,
    "ess": true,
    "acceptance": true,
    "ar1_exact_sequence": true,
    "ar1_sampling_diagnostic": true,
    "sample_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
  Publisher bibliography and abstract checked. Cited for symmetric-proposal Metropolis acceptance; no reproduction of the original hard-sphere experiment is claimed.
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
  Bibliography, summary and opening excerpt of the original paper hosted by a university checked; the publisher DOI could not be opened. This example uses symmetric Gaussian proposals and does not implement a general asymmetric proposal ratio.
- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://projecteuclid.org/journals/statistical-science/volume-7/issue-4/Practical-Markov-Chain-Monte-Carlo/10.1214/ss/1177011137.full; review_level=publisher-abstract-and-selected-original-section
  Publisher-side abstract/metadata and returned original-paper excerpts on initial-positive sequences and AR(1), from a university-hosted copy, checked. No full-text audit or convergence certificate for arbitrary chains is claimed.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Langevin thermostat: canonical distributions, timestep bias and correlation

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

### Assumptions, units and boundaries

Mass, Boltzmann constant, frequency, friction and temperature are one. Use 32768 replicas, burn time 20, steps 0.4/0.2/0.1 and correlation lag 2; require h*omega<2.

### Adopted numerical method

Compose force B and drift A half steps with exact OU noise O in B-A-O-A-B order. Record covariance, three CDFs, energy mean/variance and position correlation.

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

### References and validation

Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.

### Limits

Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_covariance_sampling_error": 0.010793938239005096,
    "maximum_correlation_sampling_error": 0.007859497657203701,
    "maximum_lyapunov_residual": 1.1102230246251565e-16,
    "maximum_burn_transient_covariance_error": 3.9116795872649285e-09,
    "minimum_covariance_bias_order": 1.9999999999999882,
    "finest_covariance_bias": 0.0024999999999999467,
    "energy_cdf_error": 0.004375986814703525,
    "position_cdf_error": 0.005928788756380088,
    "momentum_cdf_error": 0.0068938107115509295,
    "energy_mean_error": 0.009281722112660762,
    "energy_variance_error": 0.03054847700744423
  },
  "checks": {
    "finite": true,
    "stationary_reference": true,
    "burn_transient": true,
    "covariance_sampling": true,
    "correlation_sampling": true,
    "bias_refinement": true,
    "finest_bias": true,
    "canonical_energy_cdf": true,
    "canonical_position_cdf": true,
    "canonical_momentum_cdf": true,
    "canonical_energy_mean": true,
    "canonical_energy_variance": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- B. Leimkuhler and C. Matthews (2013). Rational Construction of Stochastic Numerical Methods for Molecular Sampling. https://arxiv.org/abs/1203.5428; review_level=author-manuscript-selected-appendix
  Author manuscript abstract, Langevin equation and BAOAB update in the appendix (printed page 22) checked. The original long molecular runs and general-system superconvergence are not reproduced here.
- The SciPy community (2024). SciPy1.14.1 solve_discrete_lyapunov reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.solve_discrete_lyapunov.html; review_level=official-api-documentation
  Official equation AXA^H-X+Q=0, signs and output specification checked.
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Reaction-diffusion: separate second-order space and fourth-order time

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

### Assumptions, units and boundaries

Periodic[0,2pi), D=0.1,r=0.1, initial cos(2x), final t=2. Use grids 16/32/64 and a separate fixed-grid timestep sequence 0.5/0.25/0.125.

### Adopted numerical method

Advance original periodic second-centered differences with RK4. The spatial sequence uses one small time step; the temporal sequence fixes the spatial operator.

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

### References and validation

Measure spatial order against r-Dk² and temporal order against r-4Dsin²(kdx/2)/dx². Both are independent analytic references, rather than a finer-grid run of the same solver.

### Limits

Only a linear, periodic, smooth single mode is verified. Nonlinear Fisher fronts, complex boundaries, spatial ecosystems and general reaction networks remain outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_finest_error": 0.0014105590121191725,
    "spatial_minimum_order": 1.9995467358065582,
    "temporal_finest_error": 4.109141582553377e-09,
    "temporal_minimum_order": 4.0421093675761
  },
  "checks": {
    "space_error": true,
    "space_order": true,
    "time_error": true,
    "time_order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Turing instability: linear growth and small-amplitude patterns

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

### Assumptions, units and boundaries

Dimensionless a=0.1,b=0.9, equilibrium(1,0.9), diffusivities(0.01,1), periodic k=2 and initial amplitude1e-4. Restrict runs to linear t=1 and nonlinear t=4.

### Adopted numerical method

Advance the linearized and short nonlinear PDEs using original centered differences/RK4. Record mode amplitudes/growth on three grids, minimum concentrations and early-pattern amplification.

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

### References and validation

Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.

### Limits

One near-equilibrium onset experiment. No claim reproduces original-paper parameters/experiments, mature patterns, wavenumber selection from random noise or biological calibration.

### Stored measurements and decisions

```json
{
  "metrics": {
    "homogeneous_max_real_eigenvalue": -0.10000000000000003,
    "continuum_mode_growth_rate": 0.42841126979143596,
    "linear_finest_relative_error": 0.00024726924944451685,
    "linear_minimum_spatial_order": 2.000750498056138,
    "linear_finest_growth_rate_error": 7.301377900481576e-05,
    "nonlinear_minimum_concentration": 0.8998159771334997,
    "nonlinear_early_linear_relative_error": 0.00016918909911058558,
    "pattern_amplitude_growth": 5.535462628423193
  },
  "checks": {
    "homogeneous_stable": true,
    "diffusion_mode_unstable": true,
    "linear_space_error": true,
    "linear_space_order": true,
    "growth_rate": true,
    "nonlinear_finite_positive": true,
    "early_linear_agreement": true,
    "growing_spatial_pattern": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012; review_level=publisher-archive-and-original-first-page-metadata
  Royal Society manuscript-review archive and bibliography on the original first page hosted by a university checked. Publisher text returned 403. Historical source for diffusion-driven instability, distinct from this adopted Schnakenberg example.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliographic-metadata
  PubMed bibliography and DOI checked (no abstract). Cited for the reaction-system family; a=0.1,b=0.9 and this spatial experiment are adopted educational inputs, not a transcription of the original experiment.
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

### Assumptions, units and boundaries

Dimensionless a=0.7,b=0.8,tau=12.5. Start at resting equilibrium for I=0, apply I=0.8 only during t=10..20 and integrate to t=80. No calibration to physiological physical units.

### Adopted numerical method

Use original RK4 with steps 0.1/0.05/0.025, splitting time intervals exactly at pulse discontinuities. At output spacing 0.1, measure the peak and distance from rest.

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

### References and validation

Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

### Limits

Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_tolerance_difference": 1.673639005161931e-10,
    "finest_max_error": 6.469538016418142e-08,
    "minimum_temporal_order": 4.06818366368244,
    "peak_v": 2.099845449002621,
    "peak_v_error": 2.613303262677391e-08,
    "peak_time_error": 0.0,
    "recovery_distance": 2.3590633279280127e-05
  },
  "checks": {
    "reference_tolerance": true,
    "solution_error": true,
    "time_order": true,
    "excitation": true,
    "peak_voltage": true,
    "peak_time": true,
    "recovery": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- R. FitzHugh (1961). Impulses and Physiological States in Theoretical Models of Nerve Membrane. https://pubmed.ncbi.nlm.nih.gov/19431309/; review_level=official-abstract-and-metadata
  Original-paper abstract and bibliography in PubMed checked. Supports the two-variable excitable/refractory reduction; no full HH or measured membrane-voltage reproduction is claimed.
- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). An Active Pulse Transmission Line Simulating Nerve Axon. https://ieeexplore.ieee.org/abstract/document/4066548; review_level=publisher-abstract-and-metadata
  IEEE publisher abstract, volume, pages and DOI checked. Historical source for reduced excitation and its circuit analogue; no spatial transmission-line or hardware-experiment reproduction is claimed.
- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-api-documentation
  Official DOP853, dense output, tolerance and success specifications checked. Implementation documentation for the separate numerical reference.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
