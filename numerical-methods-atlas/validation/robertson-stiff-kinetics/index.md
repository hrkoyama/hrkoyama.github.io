# Robertson反応系の初期剛性と実誤差

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

**使用手法**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja) (`bdf2`)
- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) (`sdirk2`)
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) (`step-doubling`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-algorithm)

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`)

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。


**問題の図**

![Robertson反応系の初期剛性と実誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-validation)

22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照 · 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照 · 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
## 前提・単位・境界

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。

**編集上の補足**

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

## 比較・検証

22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。

## 確認の限界

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_sampled_weighted_error": 0.04388888512603525,
    "factorizations": 11711,
    "linear_solves": 23896,
    "factor_reuses": 12185,
    "accuracy_scope": "Fixed reference observation times only; all-step positivity/conservation separately tested. Stage residual norm is weightedLinf; adaptive estimator norm is RMS."
  },
  "checks": {
    "robertson-bdf2-512:complete-finite": true,
    "robertson-bdf2-512:true-stage-residual": true,
    "robertson-bdf2-512:mass": true,
    "robertson-bdf2-512:accepted-positivity": true,
    "robertson-bdf2-1024:complete-finite": true,
    "robertson-bdf2-1024:true-stage-residual": true,
    "robertson-bdf2-1024:mass": true,
    "robertson-bdf2-1024:accepted-positivity": true,
    "robertson-bdf2-2048:complete-finite": true,
    "robertson-bdf2-2048:true-stage-residual": true,
    "robertson-bdf2-2048:mass": true,
    "robertson-bdf2-2048:accepted-positivity": true,
    "robertson-sdirk2-512:complete-finite": true,
    "robertson-sdirk2-512:true-stage-residual": true,
    "robertson-sdirk2-512:mass": true,
    "robertson-sdirk2-512:accepted-positivity": true,
    "robertson-sdirk2-1024:complete-finite": true,
    "robertson-sdirk2-1024:true-stage-residual": true,
    "robertson-sdirk2-1024:mass": true,
    "robertson-sdirk2-1024:accepted-positivity": true,
    "robertson-sdirk2-2048:complete-finite": true,
    "robertson-sdirk2-2048:true-stage-residual": true,
    "robertson-sdirk2-2048:mass": true,
    "robertson-sdirk2-2048:accepted-positivity": true,
    "robertson-sdirk-doubling-loose:complete-finite": true,
    "robertson-sdirk-doubling-loose:true-stage-residual": true,
    "robertson-sdirk-doubling-loose:mass": true,
    "robertson-sdirk-doubling-loose:accepted-positivity": true,
    "robertson-sdirk-doubling-tight:complete-finite": true,
    "robertson-sdirk-doubling-tight:true-stage-residual": true,
    "robertson-sdirk-doubling-tight:mass": true,
    "robertson-sdirk-doubling-tight:accepted-positivity": true,
    "robertson-bdf2:finest-accuracy": true,
    "robertson-bdf2:refinement": true,
    "robertson-sdirk2:finest-accuracy": true,
    "robertson-sdirk2:refinement": true,
    "robertson-adaptive-loose:accuracy": true,
    "robertson-adaptive-tight:accuracy": true,
    "robertson-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/index.json

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Official SUNDIALS cvRoberts_dns model definition [accessed 2026-11-24]. https://raw.githubusercontent.com/LLNL/sundials/main/examples/cvode/serial/cvRoberts_dns.c; review_level=official-source-selected-functions
観測mainのモデル式・初期値・Jacobianを選択閲読。今回T=.4のみで、原論文全文・4e10の長時間計算や既存数値表の再現ではありません。

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
固定版の手法/API・局所許容誤差・終了状態を選択確認。独立原著の全編監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Robertson kinetics: initial stiffness and actual error

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

**Methods used**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) (`bdf2`)
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-algorithm)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result.

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`)

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.


**Problem figure**

![Robertson kinetics: initial stiffness and actual error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-validation)

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference · Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference · Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
## Assumptions, units and boundaries

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.

**Editorial clarification**

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result.

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

## References and validation

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.

## Limits

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_sampled_weighted_error": 0.04388888512603525,
    "factorizations": 11711,
    "linear_solves": 23896,
    "factor_reuses": 12185,
    "accuracy_scope": "Fixed reference observation times only; all-step positivity/conservation separately tested. Stage residual norm is weightedLinf; adaptive estimator norm is RMS."
  },
  "checks": {
    "robertson-bdf2-512:complete-finite": true,
    "robertson-bdf2-512:true-stage-residual": true,
    "robertson-bdf2-512:mass": true,
    "robertson-bdf2-512:accepted-positivity": true,
    "robertson-bdf2-1024:complete-finite": true,
    "robertson-bdf2-1024:true-stage-residual": true,
    "robertson-bdf2-1024:mass": true,
    "robertson-bdf2-1024:accepted-positivity": true,
    "robertson-bdf2-2048:complete-finite": true,
    "robertson-bdf2-2048:true-stage-residual": true,
    "robertson-bdf2-2048:mass": true,
    "robertson-bdf2-2048:accepted-positivity": true,
    "robertson-sdirk2-512:complete-finite": true,
    "robertson-sdirk2-512:true-stage-residual": true,
    "robertson-sdirk2-512:mass": true,
    "robertson-sdirk2-512:accepted-positivity": true,
    "robertson-sdirk2-1024:complete-finite": true,
    "robertson-sdirk2-1024:true-stage-residual": true,
    "robertson-sdirk2-1024:mass": true,
    "robertson-sdirk2-1024:accepted-positivity": true,
    "robertson-sdirk2-2048:complete-finite": true,
    "robertson-sdirk2-2048:true-stage-residual": true,
    "robertson-sdirk2-2048:mass": true,
    "robertson-sdirk2-2048:accepted-positivity": true,
    "robertson-sdirk-doubling-loose:complete-finite": true,
    "robertson-sdirk-doubling-loose:true-stage-residual": true,
    "robertson-sdirk-doubling-loose:mass": true,
    "robertson-sdirk-doubling-loose:accepted-positivity": true,
    "robertson-sdirk-doubling-tight:complete-finite": true,
    "robertson-sdirk-doubling-tight:true-stage-residual": true,
    "robertson-sdirk-doubling-tight:mass": true,
    "robertson-sdirk-doubling-tight:accepted-positivity": true,
    "robertson-bdf2:finest-accuracy": true,
    "robertson-bdf2:refinement": true,
    "robertson-sdirk2:finest-accuracy": true,
    "robertson-sdirk2:refinement": true,
    "robertson-adaptive-loose:accuracy": true,
    "robertson-adaptive-tight:accuracy": true,
    "robertson-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/index.json

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Official SUNDIALS cvRoberts_dns model definition [accessed 2026-11-24]. https://raw.githubusercontent.com/LLNL/sundials/main/examples/cvode/serial/cvRoberts_dns.c; review_level=official-source-selected-functions
Read the model, initial values and Jacobian in selected official source sections. The observed main URL is not an immutable release pin. Our T = 0.4 scope does not reproduce the original paper, the long 4e10 benchmark or its numerical tables.

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
Read selected fixed-version method, API, local-tolerance and termination sections. This is not a full audit of the original research papers.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
