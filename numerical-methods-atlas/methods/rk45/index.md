# Dormand–Prince RK45 / Dormand–Prince RK45

Status: educational-example

Explicit time integration combines an embedded 5(4) error estimator, adaptive steps, a quartic continuous extension and directed events.

埋込み5(4)誤差推定と刻み制御、4次の連続拡張、向き付きイベントを組み合わせる陽的時間積分です。

No general guarantee is provided for stiff systems, tangential roots, multiple crossings per step or reset systems. Local tolerances are not global error bounds.

Other names: RK45, Dormand-Prince 5(4), DOPRI5, 埋込みRunge–Kutta

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/



- Reference: https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py — Read C, A, B, E, P, stage evaluation, accepted/rejected FSAL updates and quartic evaluation. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography. The adapted coefficient BSD notice is retained.

## Small fixed-input validation supplements

Additional fixed examples: RK45: embedded errors, dense output and events. See each release for assumptions and checked scope. There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

追加固定例：RK45の埋込み推定・補間・イベント。条件と検証範囲は各配布版で確認してください。 接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

- RK45: embedded errors, dense output and events: https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

Common execution records: [{"id": "rk45-dense-events", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`; rk45-dense-events)

#### 問題の図 (`method-problems-ja`)

##### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) (`rk45-dense-events`)

![減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#code-ja)

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja) (`rk45-dense-events`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#references-ja) (`rk45-dense-events`)

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja) (`rk45-dense-events`; 同じ問題の参照; 解析参照)

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

[既存の参照図](/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### RK45の埋込み推定・補間・イベント (`rk45-dense-events`)

[RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`; rk45-dense-events)

#### Problem figures (`method-problems-en`)

##### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) (`rk45-dense-events`)

![Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#code-en)

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en) (`rk45-dense-events`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.


#### Exact / reference solutions (`method-references-en`)

##### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#references-en) (`rk45-dense-events`)

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en) (`rk45-dense-events`; Same-problem reference; Analytic reference)

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

[Existing reference profile](/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### RK45: embedded errors, dense output and events (`rk45-dense-events`)

[RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)

###### Package tests

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
