# Rusanov / local Lax–Friedrichs flux / Rusanov／局所Lax–Friedrichs流束

Status: educational-example

Read about Rusanov / local Lax–Friedrichs flux, follow the original references and inspect related educational code and checks.

「Rusanov／局所Lax–Friedrichs流束」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

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

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

- Noh shocks: zero-pressure planar and cylindrical flow: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/result.json

Common execution records: [{"id": "noh-shock", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; noh)

#### 問題の図 (`method-problems-ja`)

##### [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![内向きに収束する流れが、外向きに進む衝撃波を作ります。円筒対称の1次元有限体積密度を回転表示し、厳密なセル平均と比較します。独立した2次元Euler計算ではありません。初期圧力ゼロ、γ=5/3、512セル、t=0.6。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

新しい専用配布版は区分定数Rusanov流束とSSPRK2/Heunを使用します。旧Eulerモジュールを圧力床で変更したものではなく、半径方向の面応力を用いる独自の整合的一次源項を検証します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。


#### 厳密解・参照解 (`method-references-ja`)

##### [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) (`noh`)

- [Nohの冷たい流入衝撃波：平面・円筒対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照; 解析参照)

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

[既存の参照図](/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Noh衝撃波：初期圧力ゼロの平面・円筒対称計算 (`noh-shock`)

[Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json)

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23-r3/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/run.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/plot_noh.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23-r3/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/test_noh.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; noh)

#### Problem figures (`method-problems-en`)

##### [Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Inward converging flow generates an outward moving shock. Revolved density from a 1D cylindrical-radial finite-volume calculation, compared with exact cell means. This is not an independent 2D Euler calculation. Zero initial pressure, gamma=5/3, 512 cells, t=0.6.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

The new dedicated edition uses piecewise-constant Rusanov flux with SSPRK2/Heun. It does not alter the older Euler module with a pressure floor; it checks an original consistent first-order radial face-stress source.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

- [Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.


#### Exact / reference solutions (`method-references-en`)

##### [Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) (`noh`)

- [Noh cold-inflow shock: planar and cylindrical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference; Analytic reference)

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

[Existing reference profile](/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Noh shocks: zero-pressure planar and cylindrical flow (`noh-shock`)

[Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json)

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23-r3/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/run.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/plot_noh.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23-r3/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/test_noh.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_numerics.py
```
