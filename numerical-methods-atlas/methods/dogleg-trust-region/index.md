# Dogleg trust regions for fixed small systems / 小固定系のdogleg信頼領域法

Status: educational-example

Fixed small nonlinear systems separate the original residual from a left-scaled merit and check a Euclidean Cauchy–Gauss–Newton dogleg with every rejected trial retained.

固定した小非線形系で、原残差と左スケールmeritを分け、Euclidean Cauchy–Gauss–Newton doglegと全拒否試行を検証します。

Only six required-root controls and declared diagnostic starts are covered. No exact optimal trust-region subproblem, all-start guarantee, PETSc implementation equivalence or large-scale performance is claimed.

Other names: 信頼領域, dogleg, ドッグレッグ, trust region, Cauchy Gauss Newton

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-globalization-controls/#globalization-difficult-starts
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-globalization-controls/#globalization-difficult-starts



- Reference: https://petsc.org/release/manual/snes/ — The source owner records this selected reading: Read nonlinear solver categories, stopping/domain-error distinctions and selected line-search/trust-region descriptions. Our fixed Euclidean dogleg and Delta0=1 are independently specified; not asserted to reproduce PETSc defaults. Unread: MINPACK original report/paper, PETSc solver implementation source, Full manual outside named sections. Publication year is not established; display n.d. Access date is separate.

## Small fixed-input validation supplements

Fixed small nonlinear systems separate the original residual from a left-scaled merit and check a Euclidean Cauchy–Gauss–Newton dogleg with every rejected trial retained.

固定した小非線形系で、原残差と左スケールmeritを分け、Euclidean Cauchy–Gauss–Newton doglegと全拒否試行を検証します。

- Line search and trust regions from the same difficult starts: https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json

Common execution records: [{"id": "globalization-difficult-starts", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Separately qualify larger sparse systems, other fixed radii/scales and broader nonlinear models with new inputs and references; no all-start convergence guarantee is claimed.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`; globalization-difficult-starts)
- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; globalization-difficult-starts)

#### 問題の図 (`method-problems-ja`)

##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`)

![同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#code-ja)

- [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。


#### 厳密解・参照解 (`method-references-ja`)

##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#references-ja) (`globalization-difficult-starts`)

- [同一初期値の大域化：解析対照と離散Bratu修正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja) (`globalization-difficult-starts`; 同じ問題の参照; 有限格子の数値参照)

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

[既存の参照図](/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-globalization-controls/#globalization-difficult-starts)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 同じ難しい初期値に対する線探索と信頼領域 (`globalization-difficult-starts`)

[同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した小非線形系で、原残差と左スケールmeritを分け、Euclidean Cauchy–Gauss–Newton doglegと全拒否試行を検証します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/experiments.py)
- [/code/validated-examples/2026-11-24/globalization-controls/globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/globalization.py)
- [/code/validated-examples/2026-11-24/globalization-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/problems.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/problems.py)
- [/code/validated-examples/2026-11-24/globalization-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/references.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`; globalization-difficult-starts)
- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; globalization-difficult-starts)

#### Problem figures (`method-problems-en`)

##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`)

![Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#code-en)

- [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.


#### Exact / reference solutions (`method-references-en`)

##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#references-en) (`globalization-difficult-starts`)

- [Globalization from identical starts: analytic controls and discrete Bratu corrections](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en) (`globalization-difficult-starts`; Same-problem reference; Finite-grid numerical reference)

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

[Existing reference profile](/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-globalization-controls/#globalization-difficult-starts)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Line search and trust regions from the same difficult starts (`globalization-difficult-starts`)

[Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Fixed small nonlinear systems separate the original residual from a left-scaled merit and check a Euclidean Cauchy–Gauss–Newton dogleg with every rejected trial retained.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/experiments.py)
- [/code/validated-examples/2026-11-24/globalization-controls/globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/globalization.py)
- [/code/validated-examples/2026-11-24/globalization-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/problems.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/problems.py)
- [/code/validated-examples/2026-11-24/globalization-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/references.py)

###### Package tests

- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
