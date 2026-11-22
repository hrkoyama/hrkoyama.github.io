# MAC pressure projection / MAC圧力射影法

Status: educational-example

Read about MAC pressure projection, follow the original references and inspect related educational code and checks.

「MAC圧力射影法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: 射影法, 圧力射影法, projection method, MAC projection, pressure projection

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/incompressible.py

- Reference: https://doi.org/10.1090/S0025-5718-1968-0242392-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Common execution records: [{"id": "taylor-green", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#taylor-green-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#taylor-green-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`; taylor-green)

#### 問題の図 (`method-problems-ja`)

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

- [周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja) (`taylor-green`)

- [粘性流／2次元Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja) (`taylor-green`; 関連モデルの参照; 解析参照)

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=taylor-green)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 周期Taylor–Green渦：速度・散逸・発散 (`taylor-green`)

[周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/incompressible.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/incompressible.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`; taylor-green)

#### Problem figures (`method-problems-en`)

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

- [Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en) (`taylor-green`)

- [Viscous flow / 2D Taylor–Green](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en) (`taylor-green`; Related-model reference; Analytic reference)

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=taylor-green)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Periodic Taylor–Green vortex: velocity, decay and divergence (`taylor-green`)

[Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/incompressible.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/incompressible.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
