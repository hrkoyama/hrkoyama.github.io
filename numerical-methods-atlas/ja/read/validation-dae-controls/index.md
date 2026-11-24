# DAEの初期化・保存則・拘束ドリフト

整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## index-1 DAEの整合初期化と離散残差

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

**使用手法**

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) (`dae`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-algorithm)

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`)

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。


**問題の図**

![index-1 DAEの整合初期化と離散残差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-validation)

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja) (`index1-dae-consistent-initialization`; 同じ問題の参照 · 製造解)

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。
### 前提・単位・境界

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

**編集上の補足**

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

### 比較・検証

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

### 確認の限界

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference:three-independent-discrete-roots": 3.5860203695392556e-14,
    "initialize-0.5:root": 0.0,
    "initialize-2:root": 2.220446049250313e-16,
    "index1-BE-16:step-residual": 9.536815781530095e-14,
    "index1-BE-16:constraint": 9.536815781530095e-14,
    "index1-BE-16:MMS-bound": 0.017655667991177793,
    "index1-BE-32:step-residual": 1.5543122344752192e-15,
    "index1-BE-32:constraint": 4.440892098500626e-16,
    "index1-BE-32:MMS-bound": 0.00889059915166246,
    "index1-BE-64:step-residual": 3.552713678800501e-15,
    "index1-BE-64:constraint": 3.3306690738754696e-16,
    "index1-BE-64:MMS-bound": 0.0044611112911168704,
    "first-order-refinement": [
      0.989778852631791,
      0.9948775084516599
    ],
    "finest_max_state_error": 0.0044611112911168704,
    "observed_orders": [
      0.989778852631791,
      0.9948775084516599
    ],
    "one_step_reference_errors": [
      3.5860203695392556e-14,
      1.1102230246251565e-16,
      1.1102230246251565e-16
    ],
    "original_targets_met": 30,
    "original_targets_total": 30
  },
  "checks": {
    "reference:MMS-0": true,
    "reference:MMS-1": true,
    "reference:MMS-2": true,
    "reference:nonexpansive-positive-region": true,
    "reference:initial-differentiated-constraint": true,
    "reference:three-positive-branch-brackets": true,
    "reference:three-independent-discrete-roots": true,
    "initialize-0.5:root": true,
    "initialize-0.5:algebraic-residual": true,
    "initialize-2:root": true,
    "initialize-2:algebraic-residual": true,
    "initialize-0:expected-singular-status": true,
    "index1-BE-16:finite": true,
    "index1-BE-16:positive": true,
    "index1-BE-16:step-residual": true,
    "index1-BE-16:constraint": true,
    "index1-BE-16:MMS-bound": true,
    "index1-BE-32:finite": true,
    "index1-BE-32:positive": true,
    "index1-BE-32:step-residual": true,
    "index1-BE-32:constraint": true,
    "index1-BE-32:MMS-bound": true,
    "index1-BE-64:finite": true,
    "index1-BE-64:positive": true,
    "index1-BE-64:step-residual": true,
    "index1-BE-64:constraint": true,
    "index1-BE-64:MMS-bound": true,
    "first-order-refinement": true,
    "initial-F-and-hidden-constraint": true,
    "six-record-identities": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/index.json

![既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。

### 取得・実行

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

### 出典と確認範囲

- SUNDIALS v7.1.1 IDA mathematics, section 5.2 [accessed 2026-11-24]. https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html; review_level=official-documentation-selected-equations
Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Robertson保存制約DAEと公式IDA保存値

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
### 前提・単位・境界

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

**編集上の補足**

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

### 比較・検証

元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。

### 確認の限界

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

### 元の数値目標と未達の結果

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

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- SUNDIALS v7.1.1 idaRoberts_dns example [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c; review_level=official-source-selected-functions
Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.

- Stored official v7.1.1 IDA Robertson output [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out; review_level=official-stored-output-selected-rows
Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 振り子の指数低減・拘束ドリフト・明示安定化

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

**使用手法**

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) (`dae`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-algorithm)

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。


**問題の図**

![振り子の指数低減・拘束ドリフト・明示安定化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-validation)

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照 · 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照 · 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
### 前提・単位・境界

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

**編集上の補足**

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

### 比較・検証

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。

### 確認の限界

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "pendulum-consistent-underlying-2000:state": 1.6288695170452172e-08,
    "pendulum-consistent-underlying-2000:energy": 1.1849681791353817e-08,
    "pendulum-consistent-stabilized-2000:state": 2.182399358452436e-09,
    "pendulum-consistent-stabilized-2000:energy": 1.2245648939313014e-10,
    "pendulum-radial-underlying-2000:C-law": 1.0557027235041927e-08,
    "pendulum-radial-underlying-2000:D-law": 1.037474827401963e-09,
    "pendulum-radial-underlying-2000:work-ledger": 4.06214124837323e-11,
    "pendulum-radial-stabilized-2000:C-law": 1.058986416895176e-10,
    "pendulum-radial-stabilized-2000:D-law": 1.113360997362714e-10,
    "pendulum-radial-stabilized-2000:work-ledger": 1.2632772794691789e-09,
    "underlying-consistent-fourth-order": [
      3.997663875510909,
      3.999093883138539
    ],
    "visible-unstabilized-drift": 0.019999989442972765,
    "stabilized-drift-ratio": 8.89400134498285e-10,
    "finest_consistent_state_error": 1.6288695170452172e-08,
    "observed_orders": [
      3.997663875510909,
      3.999093883138539
    ],
    "stabilized_to_unstabilized_drift_ratio": 8.89400134498285e-10,
    "reference_solver_counters": [
      {
        "id": "angular-reference-0",
        "method": "DOP853",
        "nfev": 1373,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      },
      {
        "id": "angular-reference-1",
        "method": "DOP853",
        "nfev": 2273,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      }
    ],
    "original_targets_met": 45,
    "original_targets_total": 45
  },
  "checks": {
    "reference:Jacobi-angular-agreement": true,
    "reference:angular-tolerance-agreement": true,
    "reference:Jacobi-initial": true,
    "reference:Jacobi-invariants": true,
    "reference:AGM-K": true,
    "reference:Decimal-remainder-qualification": true,
    "reference:constraint-identity-False": true,
    "reference:constraint-work-False": true,
    "reference:constraint-identity-True": true,
    "reference:constraint-work-True": true,
    "default-consistency-rejection": true,
    "pendulum-consistent-underlying-500:finite": true,
    "pendulum-consistent-underlying-500:radius": true,
    "pendulum-consistent-underlying-1000:finite": true,
    "pendulum-consistent-underlying-1000:radius": true,
    "pendulum-consistent-underlying-2000:finite": true,
    "pendulum-consistent-underlying-2000:radius": true,
    "pendulum-consistent-underlying-2000:state": true,
    "pendulum-consistent-underlying-2000:energy": true,
    "pendulum-consistent-stabilized-2000:finite": true,
    "pendulum-consistent-stabilized-2000:radius": true,
    "pendulum-consistent-stabilized-2000:state": true,
    "pendulum-consistent-stabilized-2000:energy": true,
    "pendulum-radial-underlying-500:finite": true,
    "pendulum-radial-underlying-500:radius": true,
    "pendulum-radial-underlying-1000:finite": true,
    "pendulum-radial-underlying-1000:radius": true,
    "pendulum-radial-underlying-2000:finite": true,
    "pendulum-radial-underlying-2000:radius": true,
    "pendulum-radial-underlying-2000:C-law": true,
    "pendulum-radial-underlying-2000:D-law": true,
    "pendulum-radial-underlying-2000:work-ledger": true,
    "pendulum-radial-stabilized-500:finite": true,
    "pendulum-radial-stabilized-500:radius": true,
    "pendulum-radial-stabilized-1000:finite": true,
    "pendulum-radial-stabilized-1000:radius": true,
    "pendulum-radial-stabilized-2000:finite": true,
    "pendulum-radial-stabilized-2000:radius": true,
    "pendulum-radial-stabilized-2000:C-law": true,
    "pendulum-radial-stabilized-2000:D-law": true,
    "pendulum-radial-stabilized-2000:work-ledger": true,
    "underlying-consistent-fourth-order": true,
    "visible-unstabilized-drift": true,
    "stabilized-drift-ratio": true,
    "eleven-record-identities": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/index.json

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。

### 取得・実行

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

### 出典と確認範囲

- NIST DLMF section22.19(i), pendulum [accessed 2026-11-24]. https://dlmf.nist.gov/22.19; review_level=official-reference-selected-equations
Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.

- NIST DLMF section19.8(i), arithmetic-geometric mean [accessed 2026-11-24]. https://dlmf.nist.gov/19.8; review_level=official-reference-selected-equations
Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
