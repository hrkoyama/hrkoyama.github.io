# Robertson保存制約DAEと公式IDA保存値

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

**使用手法**

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) (`dae`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-algorithm)

解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`)

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`)

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。


**問題の図**

![Robertson保存制約DAEと公式IDA保存値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-validation)

元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照 · 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照 · 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
## 前提・単位・境界

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

**編集上の補足**

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

## 比較・検証

元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。

## 確認の限界

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:refinement": false,
    "residual_dae:finest-reference-error": false,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:refinement": false,
    "full_ode:finest-reference-error": false,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true
  },
  "original_target_summary": {
    "met": 35,
    "total": 39,
    "all_met": false,
    "acceptance_sha256": "de0c9378204b8b08610318f41d98efb95cc2c31048a6b593707197635a0cba96"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "robertson-residual_dae-r1:nonnegative": 0.0,
    "robertson-residual_dae-r1:nonlinear-residual": 1.0710574122841998e-12,
    "robertson-residual_dae-r1:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r2:nonnegative": 0.0,
    "robertson-residual_dae-r2:nonlinear-residual": 1.9804734758359423e-12,
    "robertson-residual_dae-r2:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r4:nonnegative": 0.0,
    "robertson-residual_dae-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-residual_dae-r4:mass": 2.220446049250313e-16,
    "residual_dae:refinement": [
      1.0816554513576002,
      1.7211244337110214
    ],
    "residual_dae:finest-reference-error": 0.007755772186054176,
    "residual_dae:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.98496998732485e-06
      ],
      [
        2.8469832178190657e-05,
        3.4259947900275225e-09,
        3.737975817291739e-05
      ]
    ],
    "robertson-full_ode-r1:nonnegative": 0.0,
    "robertson-full_ode-r1:nonlinear-residual": 1.0707354074153451e-12,
    "robertson-full_ode-r1:mass": 4.440892098500626e-16,
    "robertson-full_ode-r2:nonnegative": 0.0,
    "robertson-full_ode-r2:nonlinear-residual": 1.980642882425393e-12,
    "robertson-full_ode-r2:mass": 1.5543122344752192e-15,
    "robertson-full_ode-r4:nonnegative": 0.0,
    "robertson-full_ode-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-full_ode-r4:mass": 8.881784197001252e-16,
    "full_ode:refinement": [
      1.0816554513576304,
      1.72112443371103
    ],
    "full_ode:finest-reference-error": 0.007755772186054176,
    "full_ode:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.9849699872138277e-06
      ],
      [
        2.8469832178079635e-05,
        3.4259947900546275e-09,
        3.737975817323658e-05
      ]
    ],
    "ODE-DAE-r1": 8.131516293641283e-16,
    "ODE-DAE-r2": 2.100641709190665e-15,
    "ODE-DAE-r4": 8.809142651444724e-16,
    "finest_scaled_error_DAE": 0.007755772186054176,
    "finest_scaled_error_ODE": 0.007755772186054176,
    "reference_solver_counters": [
      {
        "id": "reference-radau-loose",
        "method": "Radau",
        "nfev": 4291,
        "njev": 43,
        "nlu": 166,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-radau-tight",
        "method": "Radau",
        "nfev": 12141,
        "njev": 9,
        "nlu": 124,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-bdf-tight",
        "method": "BDF",
        "nfev": 1593,
        "njev": 3,
        "nlu": 110,
        "status": 0,
        "observations": 1537
      }
    ],
    "IDA_new_executions": 0,
    "original_targets_met": 35,
    "original_targets_total": 39
  },
  "checks": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true,
    "verification:original-target-inventory": true,
    "verification:all-original-decisions-recomputed": true,
    "verification:measured-records-match-saved-arrays": true,
    "verification:frozen-original-input-and-acceptance": true,
    "verification:independent-reference-integrity": true,
    "verification:actual-target-summary": true,
    "verification:retained-first-attempt-history": true,
    "verification:only-declared-study-goals-are-nonmandatory": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/index.json

![Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-preview.png)

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SUNDIALS v7.1.1 idaRoberts_dns example [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c; review_level=official-source-selected-functions
Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.

- Stored official v7.1.1 IDA Robertson output [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out; review_level=official-stored-output-selected-rows
Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Robertson conservation DAE and stored official IDA values

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-algorithm)

Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`)

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`)

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.


**Problem figure**

![Robertson conservation DAE and stored official IDA values: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-validation)

Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference · Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference · Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
## Assumptions, units and boundaries

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

**Editorial clarification**

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

## References and validation

Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

## Limits

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:refinement": false,
    "residual_dae:finest-reference-error": false,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:refinement": false,
    "full_ode:finest-reference-error": false,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true
  },
  "original_target_summary": {
    "met": 35,
    "total": 39,
    "all_met": false,
    "acceptance_sha256": "de0c9378204b8b08610318f41d98efb95cc2c31048a6b593707197635a0cba96"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "robertson-residual_dae-r1:nonnegative": 0.0,
    "robertson-residual_dae-r1:nonlinear-residual": 1.0710574122841998e-12,
    "robertson-residual_dae-r1:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r2:nonnegative": 0.0,
    "robertson-residual_dae-r2:nonlinear-residual": 1.9804734758359423e-12,
    "robertson-residual_dae-r2:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r4:nonnegative": 0.0,
    "robertson-residual_dae-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-residual_dae-r4:mass": 2.220446049250313e-16,
    "residual_dae:refinement": [
      1.0816554513576002,
      1.7211244337110214
    ],
    "residual_dae:finest-reference-error": 0.007755772186054176,
    "residual_dae:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.98496998732485e-06
      ],
      [
        2.8469832178190657e-05,
        3.4259947900275225e-09,
        3.737975817291739e-05
      ]
    ],
    "robertson-full_ode-r1:nonnegative": 0.0,
    "robertson-full_ode-r1:nonlinear-residual": 1.0707354074153451e-12,
    "robertson-full_ode-r1:mass": 4.440892098500626e-16,
    "robertson-full_ode-r2:nonnegative": 0.0,
    "robertson-full_ode-r2:nonlinear-residual": 1.980642882425393e-12,
    "robertson-full_ode-r2:mass": 1.5543122344752192e-15,
    "robertson-full_ode-r4:nonnegative": 0.0,
    "robertson-full_ode-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-full_ode-r4:mass": 8.881784197001252e-16,
    "full_ode:refinement": [
      1.0816554513576304,
      1.72112443371103
    ],
    "full_ode:finest-reference-error": 0.007755772186054176,
    "full_ode:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.9849699872138277e-06
      ],
      [
        2.8469832178079635e-05,
        3.4259947900546275e-09,
        3.737975817323658e-05
      ]
    ],
    "ODE-DAE-r1": 8.131516293641283e-16,
    "ODE-DAE-r2": 2.100641709190665e-15,
    "ODE-DAE-r4": 8.809142651444724e-16,
    "finest_scaled_error_DAE": 0.007755772186054176,
    "finest_scaled_error_ODE": 0.007755772186054176,
    "reference_solver_counters": [
      {
        "id": "reference-radau-loose",
        "method": "Radau",
        "nfev": 4291,
        "njev": 43,
        "nlu": 166,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-radau-tight",
        "method": "Radau",
        "nfev": 12141,
        "njev": 9,
        "nlu": 124,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-bdf-tight",
        "method": "BDF",
        "nfev": 1593,
        "njev": 3,
        "nlu": 110,
        "status": 0,
        "observations": 1537
      }
    ],
    "IDA_new_executions": 0,
    "original_targets_met": 35,
    "original_targets_total": 39
  },
  "checks": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true,
    "verification:original-target-inventory": true,
    "verification:all-original-decisions-recomputed": true,
    "verification:measured-records-match-saved-arrays": true,
    "verification:frozen-original-input-and-acceptance": true,
    "verification:independent-reference-integrity": true,
    "verification:actual-target-summary": true,
    "verification:retained-first-attempt-history": true,
    "verification:only-declared-study-goals-are-nonmandatory": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/index.json

![Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-preview.png)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SUNDIALS v7.1.1 idaRoberts_dns example [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c; review_level=official-source-selected-functions
Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.

- Stored official v7.1.1 IDA Robertson output [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out; review_level=official-stored-output-selected-rows
Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
