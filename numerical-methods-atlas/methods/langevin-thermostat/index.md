# Langevin thermostat / Langevinサーモスタット

Status: educational-example

Langevin thermostat: canonical distributions, timestep bias and correlation: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

Langevin温度制御：正準分布・刻み偏り・時間相関: 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

Langevin thermostat: canonical distributions, timestep bias and correlation: Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

Other names: ランジュバン, ランジュヴァン, friction and noise

Comparison notes: Friction changes dynamical correlations and diffusion. Finite-step sampling errors must be assessed together with the integration scheme.

摩擦は実時間の相関・拡散に影響する。有限刻みでの標本化誤差は積分法と刻み幅も含めて調べる。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1103/PhysRevE.75.056707 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://docs.lammps.org/fix_langevin.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

## Small fixed-input validation supplements

Langevin thermostat: canonical distributions, timestep bias and correlation: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

Langevin温度制御：正準分布・刻み偏り・時間相関: 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

- Langevin thermostat: canonical distributions, timestep bias and correlation: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/
- Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json

Common execution records: [{"id": "langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-quartic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
