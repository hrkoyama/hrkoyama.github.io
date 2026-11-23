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

## Small fixed-input validation supplements

The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional1D scalar transport on nonuniform moving cells uses actual upwind flux with positive physical-minus-face speed; not Euler fluid or remapping.

追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加は非一様な移動セルの1Dスカラー輸送で、正の物理速度−面速度を用いる実際の相対上流流束です。Euler流体やremap法ではありません。

- Zalesak-type 2D rotation: conservation, bounds and shape error: https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/result.json

- ALE scalar transport on genuinely nonuniform moving cells: https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json

Common execution records: [{"id": "advection-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#advection-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#advection-sine-en"}}, {"id": "zalesak-rotation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ale-nonuniform-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine, advection-square)
- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`; zalesak)
- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`; ale-nonuniform-transport)

#### 問題の図 (`method-problems-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

![実際の2次元スカラー輸送の最細格子の保存セル平均。全\[0,1\]²のうちx∈\[.28,.72\], y∈\[.53,.97\]の円盤周辺を拡大し、一回転後の一次風上とminmod MUSCLを幾何学的な参照セル平均と比較します。切り欠きの数値拡散を残した図で、FCT法やEuler流体の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

- [Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) (`zalesak-rotation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

- [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) (`advection-sine`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照; 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

[既存の参照図](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements)

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照; 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

[既存の参照図](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) (`advection-square`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) (`zalesak`)

- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja) (`zalesak-rotation`; 同じ問題の参照; 解析参照)

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

[既存の参照図](/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-measurements)

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) (`ale-nonuniform-transport`)

- [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja) (`ale-nonuniform-transport`; 同じ問題の参照; 解析参照)

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

[既存の参照図](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-measurements)

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

##### Zalesak型2D回転輸送：保存・有界性・形状誤差 (`zalesak-rotation`)

[Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### 非一様移動格子で実際に運ぶALEスカラー (`ale-nonuniform-transport`)

[非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加は非一様な移動セルの1Dスカラー輸送で、正の物理速度−面速度を用いる実際の相対上流流束です。Euler流体やremap法ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-sine, advection-square)
- [Two-dimensional rotational advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en) (`rotational-advection`; zalesak)
- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`; ale-nonuniform-transport)

#### Problem figures (`method-problems-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

Methods used by the stored square-wave CIP and limiter comparisons.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

![Saved cell means on the finest grid of actual two-dimensional scalar transport. Zoom x in\[.28,.72\],y in\[.53,.97\] from the full unit square and compare donor-cell upwinding and minmod MUSCL after one revolution against geometric reference cell means. Slot diffusion remains visible; this is not an FCT algorithm or Euler-flow calculation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

- [Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) (`zalesak-rotation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

- [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) (`advection-sine`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference; Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

[Existing reference profile](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements)

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference; Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

[Existing reference profile](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) (`advection-square`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) (`zalesak`)

- [Zalesak-type slotted disk: rigid rotation and geometric cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en) (`zalesak-rotation`; Same-problem reference; Analytic reference)

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

[Existing reference profile](/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-measurements)

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) (`ale-nonuniform-transport`)

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference; Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

[Existing reference profile](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-measurements)

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

##### Zalesak-type 2D rotation: conservation, bounds and shape error (`zalesak-rotation`)

[Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### ALE scalar transport on genuinely nonuniform moving cells (`ale-nonuniform-transport`)

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional1D scalar transport on nonuniform moving cells uses actual upwind flux with positive physical-minus-face speed; not Euler fluid or remapping.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```
