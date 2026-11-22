# CASSCF and multireference methods / CASSCF・多参照法

Status: reading-only

Map active spaces and systems beyond a single reference.

単一参照が不足する系と活性空間の選び方を整理する。

Introductory bilingual reading, representative equations and primary references are available. No dedicated implementation or numerical verification result is provided yet. Active-space dependence is distinct from grid error. Track orbital character across geometries rather than only orbital indices.

Other names: CAS, CASSCF, CASPT2, NEVPT2, 多参照法, 活性空間

Comparison notes: Active-space dependence is distinct from grid error. Track orbital character across geometries rather than only orbital indices.

活性空間依存を数値格子の誤差と混同しません。異なる核配置で活性軌道の性質が変わっていないかも追跡します。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#multireference
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#multireference



- Reference: https://doi.org/10.1016/0301-0104(80)80045-0 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/multireference/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
