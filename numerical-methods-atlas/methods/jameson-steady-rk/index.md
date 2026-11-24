# Jameson-type steady multistage Runge–Kutta / Jameson型の定常多段Runge–Kutta

Status: educational-example

A multistage iteration forms each stage from a fixed base state and advances pseudo-time to damp steady residuals.

基準状態から各段階を構成する多段反復で、擬似時間を進めて定常残差を減衰させます。

The chosen stability polynomial matches classical RK4 on linear problems, but this is not a fourth-order method for general nonlinear problems. Stable modes, a neutral control and an expanding control are distinguished.

Other names: Jameson multistage, steady Runge-Kutta, 定常多段RK

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/steady-runge-kutta/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/steady-runge-kutta/



- Reference: https://perform.readthedocs.io/en/latest/solver/timeschemes.html — Selected four-stage base-state recurrence. No full JST 1981 paper reading or compressible-flow implementation claim.

## Small fixed-input validation supplements

Additional fixed examples: Real-space mode damping with steady multistage RK. See each release for assumptions and checked scope. Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

追加固定例：定常多段RKの実空間モード減衰。条件と検証範囲は各配布版で確認してください。 固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

- Real-space mode damping with steady multistage RK: https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json

Common execution records: [{"id": "jameson-steady-linear-modes", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`; jameson-steady-linear-modes)
- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`; jameson-steady-linear-modes)

#### 問題の図 (`method-problems-ja`)

##### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`)

![周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#code-ja)

- [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。


#### 厳密解・参照解 (`method-references-ja`)

##### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#references-ja) (`jameson-steady-linear-modes`)

- [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-jameson-steady-linear-modes-ja) (`jameson-steady-linear-modes`; 同じ問題の参照; 解析参照)

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

[既存の参照図](/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/steady-runge-kutta/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 定常多段RKの実空間モード減衰 (`jameson-steady-linear-modes`)

[定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24/steady-rk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/run.py)
- [/code/validated-examples/2026-11-24/steady-rk/steady.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/steady.py)
- [/code/validated-examples/2026-11-24/steady-rk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/experiments.py)
- [/code/validated-examples/2026-11-24/steady-rk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/io_contract.py)
- [/code/validated-examples/2026-11-24/steady-rk/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/references.py)
- [/code/validated-examples/2026-11-24/steady-rk/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/reporting.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24/steady-rk/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/test_cases.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`; jameson-steady-linear-modes)
- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`; jameson-steady-linear-modes)

#### Problem figures (`method-problems-en`)

##### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`)

![Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#code-en)

- [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.


#### Exact / reference solutions (`method-references-en`)

##### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#references-en) (`jameson-steady-linear-modes`)

- [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-jameson-steady-linear-modes-en) (`jameson-steady-linear-modes`; Same-problem reference; Analytic reference)

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

[Existing reference profile](/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/steady-runge-kutta/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Real-space mode damping with steady multistage RK (`jameson-steady-linear-modes`)

[Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24/steady-rk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/run.py)
- [/code/validated-examples/2026-11-24/steady-rk/steady.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/steady.py)
- [/code/validated-examples/2026-11-24/steady-rk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/experiments.py)
- [/code/validated-examples/2026-11-24/steady-rk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/io_contract.py)
- [/code/validated-examples/2026-11-24/steady-rk/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/references.py)
- [/code/validated-examples/2026-11-24/steady-rk/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/reporting.py)

###### Package tests

- [/code/validated-examples/2026-11-24/steady-rk/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/test_cases.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
