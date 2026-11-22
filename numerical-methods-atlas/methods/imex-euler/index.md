# IMEX Euler / IMEX Euler

Status: educational-example

Read about IMEX Euler, follow the original references and inspect related educational code and checks.

「IMEX Euler」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: IMEX Euler法, IMEXオイラー法, implicit explicit Euler

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py

- Reference: https://doi.org/10.1137/0714068 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/S0168-9274(97)00056-1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja) (`nonlinear-rational-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) (`nonlinear-rational-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en) (`nonlinear-rational-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) (`nonlinear-rational-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
