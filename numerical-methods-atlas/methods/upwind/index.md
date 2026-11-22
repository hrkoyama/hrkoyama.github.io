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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine, advection-square)

#### 問題の図 (`method-problems-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) (`advection-sine`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) (`advection-square`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 周期正弦波の線形移流：風上法と解析解 (`advection-sine`)

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-sine, advection-square)

#### Problem figures (`method-problems-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

Methods used by the stored square-wave CIP and limiter comparisons.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) (`advection-sine`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) (`advection-square`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Periodic sine advection: upwind and analytic transport (`advection-sine`)

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```
