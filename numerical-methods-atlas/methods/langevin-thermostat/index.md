# Langevin thermostat / Langevinサーモスタット

Status: educational-example

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.

Other names: ランジュバン, ランジュヴァン, friction and noise

Comparison notes: Friction changes dynamical correlations and diffusion. Finite-step sampling errors must be assessed together with the integration scheme.

摩擦は実時間の相関・拡散に影響する。有限刻みでの標本化誤差は積分法と刻み幅も含めて調べる。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1103/PhysRevE.75.056707 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://docs.lammps.org/fix_langevin.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

## Small fixed-input validation supplement

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

- Langevin thermostat: canonical distributions, timestep bias and correlation: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

Common execution records: [{"id": "langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
