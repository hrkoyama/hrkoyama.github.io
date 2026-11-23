# CSVR and Langevin: distributions, fluctuations and correlations

Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Exact CSVR bath: conditional laws, fluctuations and kinetic correlation

Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-algorithm)

Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-validation)

Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

kB=1, T=1.3, tau=0.5, h=0.2, 65536 independent replicas. Test three initial energies at each of three degree counts. No Hamiltonian force, positions, constraints or center-of-mass removal.

### Adopted numerical method

Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

### References and validation

Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.

### Limits

A bath diagnostic, not another independent physical problem. Correct K sampling does not thermalize momentum directions by global scaling alone. The bath-only exp(−t/tau) identity is not a full-MD kinetic ACF. Statistical decisions apply to fixed seeds/budgets, not general mixing guarantees.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_conditional_mean_z": 1.3654493943919508,
    "maximum_conditional_variance_relative_error": 0.01524939112434133,
    "maximum_cdf_error": 0.0039733886718749944,
    "maximum_stationary_mean_relative_error": 0.014118871247168655,
    "maximum_stationary_variance_relative_error": 0.029724570745614808,
    "maximum_kinetic_acf_error": 0.011721962477943104,
    "noiseless_variance_fraction": 2.0403637334495363e-09
  },
  "checks": {
    "conditional_mean": true,
    "conditional_variance": true,
    "transition_and_stationary_cdf": true,
    "stationary_mean": true,
    "stationary_fluctuations": true,
    "kinetic_correlation": true,
    "noiseless_control_loses_fluctuations": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
Checked theory II.1–II.3 and the exact kinetic-energy propagator in Appendix A of the author manuscript arXiv:0803.4060v1 (posted 2008 for the 2007 article). The SISSA publisher PDF was unavailable. Original molecular applications are not reproduced. Direct chi-square sampling avoids copying the gamma-generation typo later noted by the author.

- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
Checked sections I–II, finite-step update Eq. (8), the sign of alpha in Eq. (9) using the same Gaussian, the Nf=1 Langevin limit and tau=1/(2 gamma). The original long Lennard-Jones transport calculations are not reproduced.

- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
Checked the author’s official note identifying a typo in the 2007 paper’s gamma-based generation of Gaussian-square sums. Year is access year. This is an original implementation, not a reproduction of the downloadable code.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-algorithm)

Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-validation)

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

m=kB=T=1, omega=(1,1.7), Nf=2. tau=0.25/1, h=0.1/0.05. Evolve 8192 canonically initialized replicas and a separate 4096-replica ensemble with q,p scaled by 1.4 to t=20. Correlation lags are 0/0.5/1/2/4.

### Adopted numerical method

Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

### References and validation

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

### Limits

Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_canonical_cdf": 0.015625,
    "maximum_canonical_mean": 0.013405172680857502,
    "maximum_canonical_variance": 0.05977288750654294,
    "maximum_heated_cdf": 0.01733397470983844,
    "maximum_heated_mean": 0.026796700361769732,
    "maximum_heated_variance": 0.11505796375558419,
    "maximum_acf_standard_error": 0.03519420852454281,
    "maximum_langevin_acf_absolute_error": 0.05177769481005279,
    "maximum_langevin_acf_z": 2.526881902370831,
    "quadrature_refinement_error": 4.440892098500626e-16,
    "minimum_shadow_bias_order": 2.0078530846410816,
    "maximum_shadow_covariance_error": 2.4424906541753444e-15,
    "finest_shadow_position_bias": 0.0006261309490266931
  },
  "checks": {
    "canonical_position_momentum_energy_cdfs": true,
    "canonical_energy_means": true,
    "canonical_energy_fluctuations": true,
    "heated_start_cdfs": true,
    "heated_start_energy_means": true,
    "heated_start_energy_fluctuations": true,
    "quadrature_reference_refined": true,
    "independent_replica_correlation_uncertainty": true,
    "langevin_independent_discrete_correlation": true,
    "shadow_covariance_identity": true,
    "deterministic_second_order_bias": true,
    "finest_shadow_bias": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
Checked theory II.1–II.3 and the exact kinetic-energy propagator in Appendix A of the author manuscript arXiv:0803.4060v1 (posted 2008 for the 2007 article). The SISSA publisher PDF was unavailable. Original molecular applications are not reproduced. Direct chi-square sampling avoids copying the gamma-generation typo later noted by the author.

- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
Checked sections I–II, finite-step update Eq. (8), the sign of alpha in Eq. (9) using the same Gaussian, the Nf=1 Langevin limit and tau=1/(2 gamma). The original long Lennard-Jones transport calculations are not reproduced.

- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
Checked the author’s official note identifying a typo in the 2007 paper’s gamma-based generation of Gaussian-square sums. Year is access year. This is an original implementation, not a reproduction of the downloadable code.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-algorithm)

Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-validation)

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

m=kB=T=1, omega=(1,1.7), lambda=0.2, U=sum(omega²q²/2+lambda q⁴/4). Use 8192 canonical and 4096 heated replicas, t=20, tau=0.25/1, h=0.1/0.05, lags 0/0.5/1/2/4.

### Adopted numerical method

Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

### References and validation

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

### Limits

A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_canonical_cdf": 0.009973613306457074,
    "maximum_canonical_mean": 0.02768676262778527,
    "maximum_canonical_variance": 0.06550451883072274,
    "maximum_heated_cdf": 0.02028342990986376,
    "maximum_heated_mean": 0.037081739382698875,
    "maximum_heated_variance": 0.08740949912634027,
    "maximum_acf_standard_error": 0.033097037653465056,
    "quadrature_refinement_error": 2.1561918917001321e-13
  },
  "checks": {
    "canonical_position_momentum_energy_cdfs": true,
    "canonical_energy_means": true,
    "canonical_energy_fluctuations": true,
    "heated_start_cdfs": true,
    "heated_start_energy_means": true,
    "heated_start_energy_fluctuations": true,
    "quadrature_reference_refined": true,
    "independent_replica_correlation_uncertainty": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
Checked theory II.1–II.3 and the exact kinetic-energy propagator in Appendix A of the author manuscript arXiv:0803.4060v1 (posted 2008 for the 2007 article). The SISSA publisher PDF was unavailable. Original molecular applications are not reproduced. Direct chi-square sampling avoids copying the gamma-generation typo later noted by the author.

- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
Checked sections I–II, finite-step update Eq. (8), the sign of alpha in Eq. (9) using the same Gaussian, the Nf=1 Langevin limit and tau=1/(2 gamma). The original long Lennard-Jones transport calculations are not reproduced.

- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
Checked the author’s official note identifying a typo in the 2007 paper’s gamma-based generation of Gaussian-square sums. Year is access year. This is an original implementation, not a reproduction of the downloadable code.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
