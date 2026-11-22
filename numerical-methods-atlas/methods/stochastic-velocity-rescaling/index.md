# Stochastic velocity rescaling (CSVR) / 確率的速度リスケーリング（CSVR）

Status: educational-example

Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関: 自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: A bath diagnostic, not another independent physical problem. Correct K sampling does not thermalize momentum directions by global scaling alone. The bath-only exp(−t/tau) identity is not a full-MD kinetic ACF. Statistical decisions apply to fixed seeds/budgets, not general mixing guarantees. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

Other names: CSVR, Bussi–Donadio–Parrinello, Bussi thermostat, v-rescale, canonical velocity rescaling, 確率的速度スケーリング

Comparison notes: Assess equilibrium distributions separately from real-time dynamics. State the coupling time, integration step and degree-of-freedom count.

分布の正しさと実時間の運動の再現を別々に調べる。結合時間・積分刻み・自由度数を明記する。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1063/1.2408420 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://arxiv.org/abs/0803.4060 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

## Small fixed-input validation supplements

Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関: 自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

- Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/
- CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/
- Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json

Common execution records: [{"id": "csvr-kinetic-kernel", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-quartic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
