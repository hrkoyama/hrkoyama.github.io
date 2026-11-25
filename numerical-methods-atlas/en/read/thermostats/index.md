# Thermostats: temperature control and distributions

Compare fluctuations, ergodicity and time correlations as well as mean temperature, from Nosé–Hoover and velocity rescaling to stochastic and momentum-conserving methods.

Retain the earlier two-method comparison of Langevin and CSVR. Preserve the earlier one-degree-of-freedom harmonic Langevin/BAOAB case. A separate edition compares both baths with the same OBABO splitting for a nondegenerate two-degree harmonic system and a two-degree anharmonic system with quartic coefficient lambda=0.2, and checks the standalone CSVR kinetic-energy kernel. A separate fixed two-mode release contrasts direct rescaling, Berendsen, Nosé–Hoover and NHC3 while retaining unmet or unresolved original goals. The remaining six methods are planned.

## Define the controlled temperature

With kinetic energy K and f active degrees of freedom, the kinetic temperature is T = 2 K / (f k_B). Count constraints and removed center-of-mass motion consistently, and separate thermal motion from streaming. State whether rotational degrees of freedom are included.

## Equal mean temperature does not imply equal distributions

For f independent momentum degrees of freedom with classical quadratic kinetic energy, canonical equilibrium gives 2 K/(k_B T₀) a chi-square distribution with f degrees of freedom. Its mean K is f k_B T₀/2 and variance is f(k_B T₀)²/2. Direct rescaling v ← √(T₀/T) v fixes K immediately after application, removing these fluctuations. CSVR instead uses a stochastic factor to generate fluctuations.

## Separate sampling from dynamics

An invariant distribution does not ensure adequate finite-time exploration. Even correct equilibrium sampling can coexist with friction- or collision-induced changes in velocity autocorrelations and diffusion. Assess integration error, heat-bath coupling time and random-seed dependence.

## CSVR and Langevin: shared canonical targets, distinct correlations

The new comparison is limited to small classical systems. CSVR and Langevin use matched OBABO splitting, degrees of freedom, temperature, potential and observation times. Distribution, fluctuations and correlations are separate diagnostics. The earlier BAOAB harmonic results remain in their original release.

### The stochastic CSVR update and its sign

CSVR evolves the total kinetic energy stochastically and scales all momenta together. The implementation uses the 2007 kinetic-energy SDE and exact propagator, with the signed factor in the 2008 paper. Here h denotes a thermostat substep.

The same Gaussian R determines energy and sign. Momentum flips matter for a few degrees of freedom. Draw S directly from a chi-square law with f−1 degrees, with S=0 at f=1; this avoids the Gamma-construction typo identified by the original author.

$$
dK=\frac{\bar K-K}{\tau}\,dt+2\sqrt{\frac{K\bar K}{f\tau}}\,dW
$$

$$
c=e^{-h/\tau},\quad a=\frac{(1-c)\bar K}{f},\quad K^+=\left(\sqrt{cK}+\sqrt a\,R\right)^2+aS,\quad R\sim N(0,1),\quad S\sim\chi^2_{f-1}
$$

$$
\alpha=\operatorname{sign}\!\left(\sqrt{cK}+\sqrt a\,R\right)\sqrt{K^+/K},\qquad p_i^+=\alpha p_i
$$

### Compare with the same splitting

Both new methods use O(Δt/2)–B(Δt/2)–A(Δt)–B(Δt/2)–O(Δt/2) for MD step Δt: A moves coordinates, B applies forces and O is the thermostat. The CSVR formula uses bath substep h=Δt/2. They share a velocity-Verlet core and differ in the bath updates.

Set τ=(2γ)⁻¹ to match kinetic-energy relaxation for the force-free bath. This τ is not the friction time γ⁻¹. At f=1, signed CSVR has the Langevin transition law; a paired-noise check tests the implementation.

The earlier BAOAB example uses a different B–A–O–A–B splitting. Its release and independent linear reference remain unchanged; the new OBABO references and errors do not replace them.

$$
\tau=(2\gamma)^{-1},\qquad p^+=e^{-\gamma h}p+\sqrt{m k_B T_0(1-e^{-2\gamma h})}\,R_{\rm phys}\quad(f=1)
$$

### Three separate questions: distribution, fluctuation and correlation

Both methods share the static canonical target. Check momentum, kinetic energy and instantaneous-temperature distributions, means and variances. Position references are analytic for harmonic systems and use separate quadrature for the anharmonic case. Matching the mean temperature alone does not check fluctuations.

Dynamic correlations depend on the method and coupling time. Measure position q, momentum p, kinetic energy K and total energy H without requiring agreement between methods. For harmonic Langevin, distinguish the continuous matrix exponential from the OBABO discrete stationary covariance/propagator. Other full-system correlations are measured with uncertainty and timestep dependence.

The exact ρK(t)=exp(−t/τ) reference applies only to the isolated bath. Full harmonic or anharmonic motion exchanges K and U, so that expression is not used as its correlation target.

CDF errors are maxima over predeclared checkpoints: five position/energy points and, for the conditional bath, three quantile points. They are not Kolmogorov–Smirnov suprema over the whole distribution. Full-system correlations use canonical-reference centering and normalization, so finite-step zero-lag values need not equal one exactly.

$$
K=\sum_{i=1}^{f}\frac{p_i^2}{2m_i},\quad \bar K=\frac{f k_B T_0}{2},\quad T_{\rm inst}=\frac{2K}{f k_B}
$$

$$
\frac{2K}{k_B T_0}\sim\chi_f^2,\quad \operatorname{Var}K=\frac{f(k_B T_0)^2}{2},\quad \operatorname{Var}T_{\rm inst}=\frac{2T_0^2}{f}
$$

$$
C_X(t)=\langle(X(t)-\langle X\rangle)(X(0)-\langle X\rangle)\rangle,\qquad \rho_X(t)=C_X(t)/C_X(0)
$$

$$
\mathbb E[K^+\mid K]=cK+fa,\quad\operatorname{Var}(K^+\mid K)=2fa^2+4acK,\quad \rho_K(t)=e^{-t/\tau}\ \text{(bath only)}
$$

### Sampling limits and implementation boundaries

Preservation from a canonical initial ensemble and relaxation from temperature-perturbed starts are distinct checks. Use independent replicas, fixed seeds and finite observation windows; separate sampling uncertainty from timestep and coupling effects. These small tests do not guarantee mixing from arbitrary starts. Correlation standard errors use the spread of products across independent replicas at each lag; they are not uncertainties of a single-trajectory time average or an effective-sample-size estimate. No independent dynamical reference is claimed for the anharmonic full-system correlations, which are not presented as having zero error.

A common scaling factor does not directly randomize momentum direction. A correct K distribution cannot rule out restricted sampling from invariant conditions such as zero total momentum in a symmetric system, or from invariant subspaces. The adopted degrees of freedom include no added constraints or removed center-of-mass mode.

For a positive bath step, at K=0 the direction is undefined, so this implementation rejects global rescaling explicitly. It does not inject an arbitrary direction as an undocumented algorithm. Nonfinite or nonphysical parameters are also checked.

## Validated scope and next checks

Three new cases separate the exact isolated-bath law, a few-degree harmonic system and a weakly anharmonic system. Each entry exposes fixed inputs, measurements, errors/uncertainty, criteria, code, tests, ZIP and independent-extraction receipt. The earlier BAOAB example is separate evidence. These CSVR comparisons are not evidence for other algorithms. A separate fixed-input release contrasts four deterministic schemes and retains unmet/unresolved original goals; six other schemes remain planned.

## Sources and review scope

For CSVR, the kinetic-energy equations/appendix in the 2007 author manuscript, signed update in the 2008 manuscript and author correction were checked. The adopted small classical examples are validated by separate references, quadrature and actual reruns. They do not reproduce the original Lennard–Jones or TIP4P-water experiments. This CSVR source audit is not transferred to other algorithms. Four deterministic schemes have a separate limited release; the remaining six schemes are comparative reading and primary-source entry points. Individual original-paper curation for Gaussian isokinetic remains open.

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1
- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1
- Giovanni Bussi (2026). Algorithms: stochastic velocity rescaling, author correction note. https://sites.google.com/site/giovannibussi/Research/algorithms

## NH,chains,weak coupling and fixed-speed contrasts

Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas.

Separately test physical reversal,Hext derivative,phi1,local weak-coupling inverses and noninjective rescaling. Retain four distributions,fluctuations,signed correlations and unresolved DKW precision at time20.

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.

## Execution and validation entries

### Langevin thermostat: canonical distributions, timestep bias and correlation

Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

### Exact CSVR bath: conditional laws, fluctuations and kinetic correlation

A bath diagnostic, not another independent physical problem. Correct K sampling does not thermalize momentum directions by global scaling alone. The bath-only exp(−t/tau) identity is not a full-MD kinetic ACF. Statistical decisions apply to fixed seeds/budgets, not general mixing guarantees.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

### CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes

Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

### Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

### A two-state BO / CP-type model with a short nuclear thermostat coupling

Long first-principles NVE and general electronic/nuclear thermostat equilibration remain deferred. No material prediction, multi-orbital CPMD or canonical/ergodic sampling certificate.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

### NH,chains,weak coupling and fixed-speed contrasts

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json

### Constraints,centre-of-mass removal and canonical statistics

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json
