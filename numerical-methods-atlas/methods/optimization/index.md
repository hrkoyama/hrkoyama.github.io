# Gradient and quasi-Newton optimization / 勾配法・準Newton法

Status: educational-example

Fit Bratu coefficients from synthetic observations and verify two-parameter adjoint gradients, regularization bias, data-sensitivity singular values and nonidentifiable observations.

Bratuの合成観測から係数を推定し、2パラメータの随伴勾配、正則化の偏り、観測感度の特異値と識別不能例を検証する。

Educational tests use small smooth lower-branch Bratu problems and fixed synthetic observations. They cover two spatial coefficients, Tikhonov regularization, local data-sensitivity SVD, rank loss with central observations and reflection ambiguity. Prior selection through regularization does not add observational information. Real data, high-dimensional function estimation, global uniqueness, statistical confidence intervals and quasi-Newton methods generally are outside scope.

Other names: 数値最適化, 勾配降下法, 準Newton法, 準ニュートン法, gradient descent, quasi Newton, Bratu, λ推定, パラメータ推定, 逆問題, inverse problem, parameter identification, projected gradient, Armijo, 複数パラメータ推定, 正則化, 識別可能性, Tikhonov regularization, identifiability, singular values, multi-parameter inverse problem

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/



- Reference: https://doi.org/10.1093/comjnl/13.3.317 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.2140/pjm.1966.16.1 — Original sufficient-decrease and backtracking construction; the detailed chapter distinguishes the local projected implementation from the original theorem.
- Reference: https://www.imm.dtu.dk/~pcha/Regutools/RTv4manual.pdf — Author official manual; the detailed chapter records the selected SVD and standard-form Tikhonov/nonzero-prior passages consulted. The local Bratu implementation is independent of the MATLAB toolbox.

Bratu inverse supplement: bounded projected adjoint-gradient fitting of one scalar parameter from fixed synthetic observations. Same-model consistency, continuous-observation grid bias and fixed-noise shifts are separate checks.

- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/scripts/build_bratu_inverse.py

- Tests: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/tests/test_bratu_inverse.py

Download: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/bratu-inverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/docs/figures/bratu-inverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_inverse.py
python scripts/build_bratu_inverse.py
```

Multi-parameter Bratu inverse supplement: two spatial coefficients, adjoint fitting, Tikhonov regularization and data-only SVD identifiability diagnostics. Regularization does not add observational information.

- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py

- Tests: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py

Download: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```

Next: Separate validation for data-driven regularization selection, many coefficients, real data and more general optimization methods.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu)

#### 問題の図 (`method-problems-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Primary immutable two-parameter spatial-coefficient Bratu supplement with adjoint fitting, Tikhonov regularization and data-only SVD identifiability checks. The previous scalar inverse supplement remains available as scalar_inverse_release; neither edition establishes general inverse-problem validity.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)

###### 関連ソース

- [/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-multinverse/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py)
- [/code/bratu-multinverse/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py)
- [/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py)

###### 配布版のテスト

- [/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Primary immutable two-parameter spatial-coefficient Bratu supplement with adjoint fitting, Tikhonov regularization and data-only SVD identifiability checks. The previous scalar inverse supplement remains available as scalar_inverse_release; neither edition establishes general inverse-problem validity.

[Related code edition / ZIP](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)

###### Related source

- [/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-multinverse/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py)
- [/code/bratu-multinverse/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py)
- [/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py)

###### Package tests

- [/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```
