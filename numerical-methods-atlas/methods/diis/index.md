# Pulay / DIIS acceleration / Pulay / DIIS加速

Status: reading-only

Use iteration history to accelerate SCF and related sequences.

反復履歴を利用してSCF等の収束を加速する。

Introductory bilingual reading, representative equations and primary references are available. No dedicated implementation or numerical verification result is provided yet. Extrapolation guarantees neither convergence nor monotonic energy decrease. Investigate initial-state dependence and unstable stationary solutions even when a residual appears small.

Other names: Pulay, DIIS, プーレイ

Comparison notes: Extrapolation guarantees neither convergence nor monotonic energy decrease. Investigate initial-state dependence and unstable stationary solutions even when a residual appears small.

外挿は収束やエネルギーの単調減少を保証しません。残差が見かけ上小さい場合、初期値依存や停留解の不安定性も確認します。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#diis
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#diis



- Reference: https://doi.org/10.1016/0009-2614(80)80396-4 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/diis/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
