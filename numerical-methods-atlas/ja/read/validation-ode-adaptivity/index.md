# 硬いODE・RK45・境界分割

Robertsonとvan der Pol、RK45の補間・イベント、非同次境界の分割法を小さな固定入力で検証します。独立参照、局所推定と実誤差、時間誤差と空間誤差を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Robertson反応系の初期剛性と実誤差

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
### 前提・単位・境界

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。

**編集上の補足**

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

### 比較・検証

22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。

### 確認の限界

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Official SUNDIALS cvRoberts_dns model definition [accessed 2026-11-24]. https://raw.githubusercontent.com/LLNL/sundials/main/examples/cvode/serial/cvRoberts_dns.c; review_level=official-source-selected-functions
観測mainのモデル式・初期値・Jacobianを選択閲読。今回T=.4のみで、原論文全文・4e10の長時間計算や既存数値表の再現ではありません。

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
固定版の手法/API・局所許容誤差・終了状態を選択確認。独立原著の全編監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## van der Polの短時間剛性遷移

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

**使用手法**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja) (`bdf2`)
- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) (`sdirk2`)
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) (`step-doubling`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-algorithm)

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

- [van der Pol振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja) (`van-der-pol`)

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。


**問題の図**

![van der Polの短時間剛性遷移：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-validation)

資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja) (`van-der-pol-stiff-transition`; 同じ問題の参照 · 有限格子の数値参照)

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。
### 前提・単位・境界

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

**編集上の補足**

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

### 比較・検証

資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。

### 確認の限界

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "vdp-mu1-bdf2-256:complete-finite": true,
    "vdp-mu1-bdf2-256:true-stage-residual": true,
    "vdp-mu1-bdf2-256:bounded-state": true,
    "vdp-mu1-bdf2-512:complete-finite": true,
    "vdp-mu1-bdf2-512:true-stage-residual": true,
    "vdp-mu1-bdf2-512:bounded-state": true,
    "vdp-mu1-bdf2-1024:complete-finite": true,
    "vdp-mu1-bdf2-1024:true-stage-residual": true,
    "vdp-mu1-bdf2-1024:bounded-state": true,
    "vdp-mu1-sdirk2-256:complete-finite": true,
    "vdp-mu1-sdirk2-256:true-stage-residual": true,
    "vdp-mu1-sdirk2-256:bounded-state": true,
    "vdp-mu1-sdirk2-512:complete-finite": true,
    "vdp-mu1-sdirk2-512:true-stage-residual": true,
    "vdp-mu1-sdirk2-512:bounded-state": true,
    "vdp-mu1-sdirk2-1024:complete-finite": true,
    "vdp-mu1-sdirk2-1024:true-stage-residual": true,
    "vdp-mu1-sdirk2-1024:bounded-state": true,
    "vdp-mu1-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu1-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu1-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu1-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu100-bdf2-256:complete-finite": true,
    "vdp-mu100-bdf2-256:true-stage-residual": true,
    "vdp-mu100-bdf2-256:bounded-state": true,
    "vdp-mu100-bdf2-512:complete-finite": true,
    "vdp-mu100-bdf2-512:true-stage-residual": true,
    "vdp-mu100-bdf2-512:bounded-state": true,
    "vdp-mu100-bdf2-1024:complete-finite": true,
    "vdp-mu100-bdf2-1024:true-stage-residual": true,
    "vdp-mu100-bdf2-1024:bounded-state": true,
    "vdp-mu100-sdirk2-256:complete-finite": true,
    "vdp-mu100-sdirk2-256:true-stage-residual": true,
    "vdp-mu100-sdirk2-256:bounded-state": true,
    "vdp-mu100-sdirk2-512:complete-finite": true,
    "vdp-mu100-sdirk2-512:true-stage-residual": true,
    "vdp-mu100-sdirk2-512:bounded-state": true,
    "vdp-mu100-sdirk2-1024:complete-finite": true,
    "vdp-mu100-sdirk2-1024:true-stage-residual": true,
    "vdp-mu100-sdirk2-1024:bounded-state": true,
    "vdp-mu100-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu100-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu100-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu100-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu1-bdf2:finest-accuracy": true,
    "vdp-mu1-bdf2:refinement": true,
    "vdp-mu1-sdirk2:finest-accuracy": true,
    "vdp-mu1-sdirk2:refinement": true,
    "vdp-mu1-adaptive-loose:accuracy": true,
    "vdp-mu1-adaptive-tight:accuracy": false,
    "vdp-mu1-adaptive:actual-tolerance-response": true,
    "vdp-mu100-bdf2:finest-accuracy": true,
    "vdp-mu100-bdf2:refinement": true,
    "vdp-mu100-sdirk2:finest-accuracy": true,
    "vdp-mu100-sdirk2:refinement": true,
    "vdp-mu100-adaptive-loose:accuracy": true,
    "vdp-mu100-adaptive-tight:accuracy": true,
    "vdp-mu100-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true
  },
  "original_target_summary": {
    "met": 62,
    "total": 63,
    "all_met": false,
    "acceptance_sha256": "fd7e7cfe528d9844e2992e8ef96d6b33e482e8c5d2bc63a4d6955431168f6051"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_sampled_weighted_error": 0.0013539838869965851,
    "factorizations": 12376,
    "linear_solves": 20946,
    "factor_reuses": 8570,
    "accuracy_scope": "Fixed reference observation times only; all-step positivity/conservation separately tested. Stage residual norm is weightedLinf; adaptive estimator norm is RMS.",
    "original_mu1_tight_global_goal": 2e-05,
    "actual_mu1_tight_global_error": 4.535633779001458e-05,
    "original_mu1_tight_global_goal_met": false,
    "reporting_scope": "Current protocol verifies faithful reporting; it does not assert this original global accuracy goal was met."
  },
  "checks": {
    "vdp-mu1-bdf2-256:complete-finite": true,
    "vdp-mu1-bdf2-256:true-stage-residual": true,
    "vdp-mu1-bdf2-256:bounded-state": true,
    "vdp-mu1-bdf2-512:complete-finite": true,
    "vdp-mu1-bdf2-512:true-stage-residual": true,
    "vdp-mu1-bdf2-512:bounded-state": true,
    "vdp-mu1-bdf2-1024:complete-finite": true,
    "vdp-mu1-bdf2-1024:true-stage-residual": true,
    "vdp-mu1-bdf2-1024:bounded-state": true,
    "vdp-mu1-sdirk2-256:complete-finite": true,
    "vdp-mu1-sdirk2-256:true-stage-residual": true,
    "vdp-mu1-sdirk2-256:bounded-state": true,
    "vdp-mu1-sdirk2-512:complete-finite": true,
    "vdp-mu1-sdirk2-512:true-stage-residual": true,
    "vdp-mu1-sdirk2-512:bounded-state": true,
    "vdp-mu1-sdirk2-1024:complete-finite": true,
    "vdp-mu1-sdirk2-1024:true-stage-residual": true,
    "vdp-mu1-sdirk2-1024:bounded-state": true,
    "vdp-mu1-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu1-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu1-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu1-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu100-bdf2-256:complete-finite": true,
    "vdp-mu100-bdf2-256:true-stage-residual": true,
    "vdp-mu100-bdf2-256:bounded-state": true,
    "vdp-mu100-bdf2-512:complete-finite": true,
    "vdp-mu100-bdf2-512:true-stage-residual": true,
    "vdp-mu100-bdf2-512:bounded-state": true,
    "vdp-mu100-bdf2-1024:complete-finite": true,
    "vdp-mu100-bdf2-1024:true-stage-residual": true,
    "vdp-mu100-bdf2-1024:bounded-state": true,
    "vdp-mu100-sdirk2-256:complete-finite": true,
    "vdp-mu100-sdirk2-256:true-stage-residual": true,
    "vdp-mu100-sdirk2-256:bounded-state": true,
    "vdp-mu100-sdirk2-512:complete-finite": true,
    "vdp-mu100-sdirk2-512:true-stage-residual": true,
    "vdp-mu100-sdirk2-512:bounded-state": true,
    "vdp-mu100-sdirk2-1024:complete-finite": true,
    "vdp-mu100-sdirk2-1024:true-stage-residual": true,
    "vdp-mu100-sdirk2-1024:bounded-state": true,
    "vdp-mu100-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu100-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu100-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu100-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu1-bdf2:finest-accuracy": true,
    "vdp-mu1-bdf2:refinement": true,
    "vdp-mu1-sdirk2:finest-accuracy": true,
    "vdp-mu1-sdirk2:refinement": true,
    "vdp-mu1-adaptive-loose:accuracy": true,
    "vdp-mu1-adaptive:actual-tolerance-response": true,
    "vdp-mu100-bdf2:finest-accuracy": true,
    "vdp-mu100-bdf2:refinement": true,
    "vdp-mu100-sdirk2:finest-accuracy": true,
    "vdp-mu100-sdirk2:refinement": true,
    "vdp-mu100-adaptive-loose:accuracy": true,
    "vdp-mu100-adaptive-tight:accuracy": true,
    "vdp-mu100-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true,
    "vdp-mu1-adaptive-tight:original-goal-outcome-faithfully-reported": true,
    "vdp-mu1-adaptive-tight:accepted-local-controls-satisfied": true,
    "vdp-mu1-adaptive-tight:immutable-original-failure-bound": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/index.json

![保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。

### 取得・実行

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

### 出典と確認範囲

- scikit-sundae official van der Pol example [accessed 2026-11-24]. https://scikit-sundae.readthedocs.io/en/stable/examples/van_der_pol.html; review_level=official-project-example-selected-equations
公式binding例の2階/1階系と初期値を確認。採用μ=1/100,T=2は独自の軽量範囲で、原著やμ1000全周期の再現ではありません。

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
固定版の手法/API・局所許容誤差・終了状態を選択確認。独立原著の全編監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## RK45の埋込み推定・補間・イベント

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

**使用手法**

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-algorithm)

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`)

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。


**問題の図**

![RK45の埋込み推定・補間・イベント：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) (`rk45-dense-events`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-validation)

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja) (`rk45-dense-events`; 同じ問題の参照 · 解析参照)

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。
### 前提・単位・境界

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

**編集上の補足**

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

### 比較・検証

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

### 確認の限界

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_dense_error": 6.136827199998418e-05,
    "maximum_event_time_error": 1.4618863214188593e-05,
    "actual_RHS_evaluations": 2162,
    "rejected_trials": 40,
    "scope": "Analytic state/simple crossings; accepted-full endpoint versus terminal dense-root state distinct. No global guarantee inferred from localtol."
  },
  "checks": {
    "rk45-loose-hmax0.4:completion-and-work": true,
    "rk45-loose-hmax0.4:endpoint-error": true,
    "rk45-loose-hmax0.4:offmesh-error": true,
    "rk45-loose-hmax0.4:event-time-and-set": true,
    "rk45-loose-hmax0.4:event-residual": true,
    "rk45-loose-hmax0.1:completion-and-work": true,
    "rk45-loose-hmax0.1:endpoint-error": true,
    "rk45-loose-hmax0.1:offmesh-error": true,
    "rk45-loose-hmax0.1:event-time-and-set": true,
    "rk45-loose-hmax0.1:event-residual": true,
    "rk45-medium-hmax0.4:completion-and-work": true,
    "rk45-medium-hmax0.4:endpoint-error": true,
    "rk45-medium-hmax0.4:offmesh-error": true,
    "rk45-medium-hmax0.4:event-time-and-set": true,
    "rk45-medium-hmax0.4:event-residual": true,
    "rk45-medium-hmax0.1:completion-and-work": true,
    "rk45-medium-hmax0.1:endpoint-error": true,
    "rk45-medium-hmax0.1:offmesh-error": true,
    "rk45-medium-hmax0.1:event-time-and-set": true,
    "rk45-medium-hmax0.1:event-residual": true,
    "rk45-tight-hmax0.4:completion-and-work": true,
    "rk45-tight-hmax0.4:endpoint-error": true,
    "rk45-tight-hmax0.4:offmesh-error": true,
    "rk45-tight-hmax0.4:event-time-and-set": true,
    "rk45-tight-hmax0.4:event-residual": true,
    "rk45-tight-hmax0.1:completion-and-work": true,
    "rk45-tight-hmax0.1:endpoint-error": true,
    "rk45-tight-hmax0.1:offmesh-error": true,
    "rk45-tight-hmax0.1:event-time-and-set": true,
    "rk45-tight-hmax0.1:event-residual": true,
    "rk45-terminal-direction-1:completion-and-work": true,
    "rk45-terminal-direction-1:endpoint-error": true,
    "rk45-terminal-direction-1:offmesh-error": true,
    "rk45-terminal-direction-1:event-time-and-set": true,
    "rk45-terminal-direction-1:event-residual": true,
    "rk45-terminal-direction1:completion-and-work": true,
    "rk45-terminal-direction1:endpoint-error": true,
    "rk45-terminal-direction1:offmesh-error": true,
    "rk45-terminal-direction1:event-time-and-set": true,
    "rk45-terminal-direction1:event-residual": true,
    "hmax0.4:actual-tolerance-response": true,
    "hmax0.1:actual-tolerance-response": true,
    "rejected-trial-actually-exercised": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/index.json

![減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。

### 取得・実行

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

### 出典と確認範囲

- SciPy1.14.1 RK45 coefficient and dense-output source [accessed 2026-11-24]. https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py; review_level=official-release-source-selected-functions
C/A/B/E/P、段階・受理/棄却時FSAL更新、quartic補間を確認。原Dormand–Prince1980/Shampine1986論文は書誌参照のみで全文未読。係数由来のBSD通知を同梱。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Dirichlet境界でのStrang次数低下と補正

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

**使用手法**

- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)
- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) (`lie-trotter`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-algorithm)

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

- [非同次境界を持つ線形反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja) (`inhomogeneous-reaction-diffusion`)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。


**問題の図**

![Dirichlet境界でのStrang次数低下と補正：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-validation)

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

- [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja) (`strang-boundary-order-reduction`; 同じ問題の参照 · 半解析参照)

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。
### 前提・単位・境界

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

**編集上の補足**

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

### 採用した計算法

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

### 比較・検証

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

### 確認の限界

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

### 保存実測値と判定

```json
{
  "metrics": {
    "N127_finest_raw_temporal_error": 0.00011072277594093016,
    "N127_finest_corrected_temporal_error": 9.830520841802581e-08,
    "reference_spatial_order": 1.9999950873134633,
    "scope": "Actual1Dnonperiodicfields. TimevsSAME-FDoracle; spacevsanalyticcontinuum. Linearautonomousspecialization, fixed-regime order; no universal reduction/theorem reproduction."
  },
  "checks": {
    "boundary-n31-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-lie-8:actual-field-and-work": true,
    "boundary-n127-lie-8:boundary-compatibility-ledger": true,
    "boundary-n127-lie-16:actual-field-and-work": true,
    "boundary-n127-lie-16:boundary-compatibility-ledger": true,
    "boundary-n127-lie-32:actual-field-and-work": true,
    "boundary-n127-lie-32:boundary-compatibility-ledger": true,
    "boundary-n127-lie-64:actual-field-and-work": true,
    "boundary-n127-lie-64:boundary-compatibility-ledger": true,
    "n31:corrected-finest-accuracy": true,
    "n63:corrected-finest-accuracy": true,
    "n127:corrected-finest-accuracy": true,
    "strang-unmodified:fixed-regime-temporal-order": true,
    "strang-boundary-corrected:fixed-regime-temporal-order": true,
    "finest:boundary-correction-improves": true,
    "separate-reference-spatial-order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/index.json

![実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。

### 取得・実行

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

### 出典と確認範囲

- L. Einkemmer; A. Ostermann (2014). Overcoming order reduction in diffusion-reaction splitting. Part1: Dirichlet boundary conditions [accessed 2026-11-24]. https://arxiv.org/abs/1411.0465; review_level=primary-preprint-selected-sections
2014v1の§2/Algorithm2/定数境界例、§3.2の定理・仮定、1D例の選択抽出テキストを閲読。全証明・原PDF全画像の監査ではありません。今回線形特殊例で、原著の非線形数値表ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
