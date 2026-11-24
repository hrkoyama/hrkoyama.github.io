# Adaptive SDIRK2 / step doubling / 適応SDIRK2／ステップ倍分割

Status: educational-example

Read about Adaptive SDIRK2 / step doubling, follow the original references and inspect related educational code and checks. Additional fixed examples: Robertson kinetics: initial stiffness and actual error, Van der Pol: an early stiffness transition. See each release for assumptions and checked scope.

「適応SDIRK2／ステップ倍分割」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：Robertson反応系の初期剛性と実誤差、van der Polの短時間剛性遷移。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. The preceding limitations describe earlier editions. This additional release: Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

Other names: ステップ倍分割法, step doubling, 適応SDIRK2, adaptive SDIRK2

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py

- Reference: https://doi.org/10.1137/0714068 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/S0168-9274(97)00056-1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional fixed examples: Robertson kinetics: initial stiffness and actual error, Van der Pol: an early stiffness transition. See each release for assumptions and checked scope. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

追加固定例：Robertson反応系の初期剛性と実誤差、van der Polの短時間剛性遷移。条件と検証範囲は各配布版で確認してください。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

- Robertson kinetics: initial stiffness and actual error: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/
- Van der Pol: an early stiffness transition: https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

Common execution records: [{"id": "robertson-stiff-kinetics", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "van-der-pol-stiff-transition", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`; robertson-stiff-kinetics)
- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`; robertson-stiff-kinetics)
- [van der Pol振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja) (`van-der-pol`; van-der-pol-stiff-transition)

#### 問題の図 (`method-problems-ja`)

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`)

![保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#code-ja)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。


#### 厳密解・参照解 (`method-references-ja`)

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) (`robertson-stiff-kinetics`)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照; 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements)

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照; 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements)

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) (`van-der-pol-stiff-transition`)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja) (`van-der-pol-stiff-transition`; 同じ問題の参照; 有限格子の数値参照)

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

[既存の参照図](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Robertson反応系の初期剛性と実誤差 (`robertson-stiff-kinetics`)

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

##### van der Polの短時間剛性遷移 (`van-der-pol-stiff-transition`)

[van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`; robertson-stiff-kinetics)
- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`; robertson-stiff-kinetics)
- [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en) (`van-der-pol`; van-der-pol-stiff-transition)

#### Problem figures (`method-problems-en`)

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.


#### Exact / reference solutions (`method-references-en`)

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) (`robertson-stiff-kinetics`)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference; Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-measurements)

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference; Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-measurements)

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) (`van-der-pol-stiff-transition`)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en) (`van-der-pol-stiff-transition`; Same-problem reference; Finite-grid numerical reference)

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Robertson kinetics: initial stiffness and actual error (`robertson-stiff-kinetics`)

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

##### Van der Pol: an early stiffness transition (`van-der-pol-stiff-transition`)

[Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
