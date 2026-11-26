# Rusanov / local Lax–Friedrichs flux / Rusanov／局所Lax–Friedrichs流束

Status: educational-example

Read about Rusanov / local Lax–Friedrichs flux, follow the original references and inspect related educational code and checks. Additional fixed examples: Two-dimensional absorber shadow and M1 transport, Opposing beams and information loss in the M1 closure. See each release for assumptions and checked scope.

「Rusanov／局所Lax–Friedrichs流束」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：2D吸収影と保存的M1輸送、2D反向beamとM1閉包の情報損失。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

Other names: Rusanov法, Rusanov flux, 局所Lax-Friedrichs法, local Lax Friedrichs flux, LLF, ルサノフ法, ルサノフ流束

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(89)90222-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(91)90211-3 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1017/CBO9780511791253 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately.

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。

- Noh shocks: zero-pressure planar, cylindrical and spherical flow: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json

- Noh problem: an actual 2D Cartesian Euler calculation: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/result.json

- Sedov–Taylor point blast: lightweight spherical-radial validation: https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/result.json

- Two-dimensional absorber shadow and M1 transport: https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/
- Opposing beams and information loss in the M1 closure: https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json

- Saltzman-type skew-grid piston: 2D Euler and ALE: https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json

Common execution records: [{"id": "noh-shock", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "noh-cartesian-2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "sedov-blast", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "shadow-absorber2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "opposing-beams2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "saltzman-ale-piston", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; noh, sedov, saltzman-ale-piston)
- [静止媒質の灰色輻射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`; shadow-absorber2d, opposing-beams2d)
- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

#### 問題の図 (`method-problems-ja`)

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![実際の2次元Cartesian Euler計算の密度場。正方形全域128²セル、初期圧力ゼロ、γ=5/3、t=.6。白破線は厳密衝撃円。軸・対角方向の差と原点過熱を残し、1D半径例にも辿れます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

- [Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) (`noh-cartesian-2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。

##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

![1次元球対称Eulerの保存済み半径密度を中心断面に表示。γ=5/3、E=ρ0=1、p0=0、t=.05、512球殻、有限投入半径.03。半解析的な点源参照との違いと衝撃層の誤差を残した図で、実2D Cartesian計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

区分定数のRusanov有限体積流束とSSPRK2/Heunを使う限定した球半径例です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

- [Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) (`sedov-blast`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

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

##### [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`)

![2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#code-ja)

- [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。


#### 厳密解・参照解 (`method-references-ja`)

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) (`noh`)

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照; 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

[既存の参照図](/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#references-ja) (`sedov`)

- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja) (`sedov`; 同じ問題の参照; 半解析参照)

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-measurements)

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja) (`shadow-absorber2d`)

- [円形吸収体の特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja) (`shadow-absorber2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-measurements)

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja) (`opposing-beams2d`)

- [反向伝播packetの特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja) (`opposing-beams2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-measurements)

##### [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#references-ja) (`saltzman-ale-piston`)

- [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja) (`saltzman-ale-piston`; 同じ問題の参照; 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。

[既存の参照図](/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算 (`noh-shock`)

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

##### Noh問題：実際の2次元Cartesian Euler計算 (`noh-cartesian-2d`)

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json)

正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。

##### Sedov–Taylor点爆発：球対称の軽量検証 (`sedov-blast`)

[Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json)

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

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

##### Saltzman型の歪み格子ピストン：2次元EulerとALE (`saltzman-ale-piston`)

[Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py)
- [/code/validated-examples/2026-11-23-r2/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/run.py)
- [/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py)
- [/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; noh, sedov, saltzman-ale-piston)
- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`; shadow-absorber2d, opposing-beams2d)
- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

#### Problem figures (`method-problems-en`)

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Density from an actual2D Cartesian Euler computation:full square128²,p0=0,gamma5/3,t=.6. White dashed circle is the exact shock. Axis/diagonal differences and origin heating remain visible, with links to earlier1D radial examples.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

- [Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) (`noh-cartesian-2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

![A central-section view of saved one-dimensional spherical-radial Euler density:gamma5/3,E=rho0=1,p0=0,t=.05,512 shells and finite deposition radius.03. Point-source reference differences and shock errors remain visible; this is not an actual2D Cartesian computation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

A scoped spherical-radial example using piecewise-constant Rusanov finite-volume fluxes and SSPRK2/Heun.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

- [Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) (`sedov-blast`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

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

##### [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`)

![Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#code-en)

- [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.


#### Exact / reference solutions (`method-references-en`)

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) (`noh`)

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference; Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

[Existing reference profile](/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#references-en) (`sedov`)

- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en) (`sedov`; Same-problem reference; Semi-analytic reference)

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

[Existing reference profile](/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-measurements)

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en) (`shadow-absorber2d`)

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-measurements)

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en) (`opposing-beams2d`)

- [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en) (`opposing-beams2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-measurements)

##### [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#references-en) (`saltzman-ale-piston`)

- [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en) (`saltzman-ale-piston`; Same-problem reference; Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.

[Existing reference profile](/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Noh shocks: zero-pressure planar, cylindrical and spherical flow (`noh-shock`)

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

##### Noh problem: an actual 2D Cartesian Euler calculation (`noh-cartesian-2d`)

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json)

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

##### Sedov–Taylor point blast: lightweight spherical-radial validation (`sedov-blast`)

[Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json)

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

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

##### Saltzman-type skew-grid piston: 2D Euler and ALE (`saltzman-ale-piston`)

[Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py)
- [/code/validated-examples/2026-11-23-r2/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/run.py)
- [/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py)
- [/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_numerics.py
```
