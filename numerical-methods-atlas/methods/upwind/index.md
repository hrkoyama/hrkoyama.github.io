# Upwind finite differences / 風上差分（upwind）

Status: educational-example

A first-order baseline for one-dimensional constant-speed transport using the upstream value. The released periodic forward-Euler example exposes flow direction, the CFL restriction and numerical diffusion. Additional fixed examples: Isotropic scattering in a finite slab. See each release for assumptions and checked scope. Additional fixed examples: Su–Olson transport with an independently published analytical table. See each release for assumptions and checked scope. Additional fixed examples: Two-dimensional absorber shadow and M1 transport, Opposing beams and information loss in the M1 closure. See each release for assumptions and checked scope.

流れの上流側の値を用い、1次元の一定速度輸送を1次精度で進める基準法。公開例は周期格子の前進Euler更新で、風向きとCFL条件、数値拡散の関係を比較できる。 追加固定例：等方散乱平板の反射・透過・吸収。条件と検証範囲は各配布版で確認してください。 追加固定例：Su–Olson1997角度輸送の独立公開表比較。条件と検証範囲は各配布版で確認してください。 追加固定例：2D吸収影と保存的M1輸送、2D反向beamとM1閉包の情報損失。条件と検証範囲は各配布版で確認してください。

First order in both space and time and generally diffusive for waves and contacts. The explicit periodic update is unstable for |C|>1. This constant-speed scalar example establishes no conservation or stability guarantee for variable-coefficient, nonlinear-system or multidimensional extensions. Additional fixed examples: Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound. Additional fixed examples: No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator. Additional fixed examples: Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

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
空間・時間とも1次精度で、一般に波形や接触面を拡散させる。|C|>1ではこの陽的更新の安定性は保たれない。一定速度のスカラー例だけから、変係数・非線形系や多次元での保存性・安定性は保証しない。 今回の追加固定例：有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。 今回の追加固定例：原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。 今回の追加固定例：6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。 6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
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
First order in both space and time and generally diffusive for waves and contacts. The explicit periodic update is unstable for |C|>1. This constant-speed scalar example establishes no conservation or stability guarantee for variable-coefficient, nonlinear-system or multidimensional extensions. Additional fixed examples: Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound. Additional fixed examples: No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator. Additional fixed examples: Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
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

- Isotropic scattering in a finite slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json

- Su–Olson transport with an independently published analytical table: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json

- Two-dimensional absorber shadow and M1 transport: https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/
- Opposing beams and information loss in the M1 closure: https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json

Common execution records: [{"id": "advection-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#advection-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#advection-sine-en"}}, {"id": "zalesak-rotation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ale-nonuniform-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "isotropic-scattering-slab", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "su-olson-transport1997", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "shadow-absorber2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "opposing-beams2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine, advection-square)
- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`; zalesak)
- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`; ale-nonuniform-transport)
- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`; isotropic-scattering-slab, su-olson-transport1997, shadow-absorber2d, opposing-beams2d)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; su-olson-transport1997)
- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

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

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

- [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

- [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

- [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

- [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) (`opposing-beams2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。


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

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#references-ja) (`isotropic-scattering-slab`)

- [等方散乱平板：連続角Fredholm流束参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja) (`isotropic-scattering-slab`; 同じ問題の参照; 半解析参照)

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

[既存の参照図](/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-measurements)

##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#references-ja) (`su-olson-transport1997`)

- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja) (`su-olson-transport1997`; 同じ問題の参照; 有限格子の数値参照)

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

[既存の参照図](/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-measurements)

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja) (`shadow-absorber2d`)

- [円形吸収体の特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja) (`shadow-absorber2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-measurements)

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja) (`opposing-beams2d`)

- [反向伝播packetの特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja) (`opposing-beams2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-measurements)

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

##### 等方散乱平板の反射・透過・吸収 (`isotropic-scattering-slab`)

[等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

##### Su–Olson1997角度輸送の独立公開表比較 (`su-olson-transport1997`)

[Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。

##### 2D吸収影と保存的M1輸送 (`shadow-absorber2d`)

[2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。

##### 2D反向beamとM1閉包の情報損失 (`opposing-beams2d`)

[2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。

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
- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)

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
- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`; isotropic-scattering-slab, su-olson-transport1997, shadow-absorber2d, opposing-beams2d)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; su-olson-transport1997)
- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

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

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

- [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

- [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) (`su-olson-transport1997`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

- [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) (`shadow-absorber2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

- [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) (`opposing-beams2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.


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

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#references-en) (`isotropic-scattering-slab`)

- [Isotropically scattering slab: continuous-angle Fredholm flux reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en) (`isotropic-scattering-slab`; Same-problem reference; Semi-analytic reference)

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

[Existing reference profile](/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-measurements)

##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#references-en) (`su-olson-transport1997`)

- [Su–Olson transport: primary2023author-provided analytical benchmark data](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en) (`su-olson-transport1997`; Same-problem reference; Finite-grid numerical reference)

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

[Existing reference profile](/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-measurements)

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en) (`shadow-absorber2d`)

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-measurements)

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en) (`opposing-beams2d`)

- [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en) (`opposing-beams2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-measurements)

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

##### Isotropic scattering in a finite slab (`isotropic-scattering-slab`)

[Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

##### Su–Olson transport with an independently published analytical table (`su-olson-transport1997`)

[Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

##### Two-dimensional absorber shadow and M1 transport (`shadow-absorber2d`)

[Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

##### Opposing beams and information loss in the M1 closure (`opposing-beams2d`)

[Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.

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
- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```
