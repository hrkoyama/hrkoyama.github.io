# Upwind finite differences / 風上差分（upwind）

Status: educational-example

A first-order baseline for one-dimensional constant-speed transport using the upstream value. The released periodic forward-Euler example exposes flow direction, the CFL restriction and numerical diffusion.

流れの上流側の値を用い、1次元の一定速度輸送を1次精度で進める基準法。公開例は周期格子の前進Euler更新で、風向きとCFL条件、数値拡散の関係を比較できる。

First order in both space and time and generally diffusive for waves and contacts. The explicit periodic update is unstable for |C|>1. This constant-speed scalar example establishes no conservation or stability guarantee for variable-coefficient, nonlinear-system or multidimensional extensions.

Other names: 風上差分, 風上差分法, 風上法, upwind scheme, upwind differencing


## 条件と確認範囲 (ja)

problem: 一定速度で運ばれるスカラー分布の時間発展。

variant: advection.pyの符号対応1次風上差分。difference_stepは前進Euler、finite_differenceは周期空間微分を提供する。

use_when:
- 一定速度の周期移流で、安定性と数値拡散を分けて学ぶ。
- 高次法の比較用に簡単で単調な基準更新が必要で、|C|≤1を満たせる。

avoid_when:
- 小さな拡散で細部を長時間保つ必要がある。
- 変速度の保存則や非周期境界を追加処理なしで解きたい。

assumptions [specified]:
- 対象はq_t+a q_x=0、一定の実速度a、一様格子である。
- 公開の完全離散更新difference_stepは前進Eulerで、C=a Δt/Δxの符号に応じて後退差分と前進差分を切り替える。
- この線形周期更新の安定性・単調性には|C|≤1を用いる。finite_difference単独は空間演算子であり時間積分法を指定しない。
速度符号による分岐と更新式を確認。

units [specified]:
qの単位は任意だが一貫させる。xは長さ、tは時間、aは長さ/時間で、C=a Δt/Δxは無次元。公開の周期ベンチマークは無次元化されている。
コードのCとdxの関係から単位を明示。

boundary_conditions [specified]:
np.rollによる周期境界。流入・流出や壁境界を扱うにはゴースト値の実装が別途必要で、現在の周期演算子をそのまま転用しない。
差分関数はnp.rollを用いる。

limitations [specified]:
空間・時間とも1次精度で、一般に波形や接触面を拡散させる。|C|>1ではこの陽的更新の安定性は保たれない。一定速度のスカラー例だけから、変係数・非線形系や多次元での保存性・安定性は保証しない。
増幅率関数と既存テストの対象範囲に限定。

Review: advection.pyのfinite_difference・difference_step・amplificationとtest_numerics.pyの離散Fourierモード、周期平均保存、差分方向・次数の既存テストを読んだ。今回の再実行はしていない。

Not checked:
- 今回の数値再実行、非周期境界、変係数輸送の検証。
- Courant–Isaacson–Rees原報の本文との逐式照合。

Evidence:
- finite_difference; difference_step; amplification: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py
- test_amplification_matches_actual_discrete_mode; test_periodic_difference_conserves_mean; test_spatial_stencil_direction_and_orders: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [formulation / primary-research] Courant, Isaacson & Rees (1952). On the solution of nonlinear hyperbolic differential equations by finite differences. — https://doi.org/10.1002/cpa.3160050303
  風上差分に関係する歴史的な一次文献。今回は書誌を確認し、本サイトのスカラー更新式との対応や安定条件はコードから記述する。
  metadata (2026-11-22); Publisher title, authors, year, volume and pages; full text unavailable.; https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160050303

## Conditions and review scope (en)

problem: Time evolution of a scalar distribution transported at constant speed.

variant: Sign-aware first-order upstream differencing in advection.py: forward Euler in difference_step and a periodic spatial derivative in finite_difference.

use_when:
- Study stability and numerical diffusion for constant-speed periodic advection.
- Use a simple monotone baseline for comparison with higher-order methods when |C|≤1 can be enforced.

avoid_when:
- Long-time preservation of fine features with little numerical diffusion is essential.
- Variable-speed conservation laws or nonperiodic boundaries are required without additional treatment.

assumptions [specified]:
- The problem is q_t+a q_x=0 with constant real a on a uniform grid.
- The fully discrete difference_step uses forward Euler and switches between backward and forward differences according to the sign of C=a Δt/Δx.
- For this linear periodic update, use |C|≤1 for stability and monotonicity. finite_difference alone is a spatial operator and does not specify a time integrator.
The sign branches and update formula were inspected.

units [specified]:
q may have any consistent unit; x is length, t is time, and a is length/time. C=a Δt/Δx is dimensionless. Released periodic benchmarks are nondimensional.
Units follow from the Courant number and grid spacing.

boundary_conditions [specified]:
Periodic boundaries are imposed with np.roll. Inflow, outflow and wall boundaries require a separate ghost-state implementation.
The difference functions use np.roll.

limitations [specified]:
First order in both space and time and generally diffusive for waves and contacts. The explicit periodic update is unstable for |C|>1. This constant-speed scalar example establishes no conservation or stability guarantee for variable-coefficient, nonlinear-system or multidimensional extensions.
Claims are limited to the amplification function and existing test coverage.

Review: Inspected finite_difference, difference_step and amplification in advection.py, plus existing discrete-Fourier-mode, periodic-mean and stencil-direction/order tests in test_numerics.py. No rerun was performed.

Not checked:
- No numerical rerun, nonperiodic-boundary validation or variable-coefficient transport validation.
- No equation-by-equation comparison with the Courant–Isaacson–Rees full text.

Evidence:
- finite_difference; difference_step; amplification: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py
- test_amplification_matches_actual_discrete_mode; test_periodic_difference_conserves_mean; test_spatial_stencil_direction_and_orders: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [formulation / primary-research] Courant, Isaacson & Rees (1952). On the solution of nonlinear hyperbolic differential equations by finite differences. — https://doi.org/10.1002/cpa.3160050303
  Historical primary source associated with upstream differencing. The local scalar specialization and stability condition are established from code inspection.
  metadata (2026-11-22); Publisher title, authors, year, volume and pages; full text unavailable.; https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160050303


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1002/cpa.3160050303 — Historical upstream-differencing lineage. Only bibliographic metadata were checked; the scalar update and CFL statement here come from the atlas code.

Common execution records: [{"id": "advection-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#advection-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#advection-sine-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
