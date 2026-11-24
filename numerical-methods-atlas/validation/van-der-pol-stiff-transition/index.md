# van der Polの短時間剛性遷移

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
## 前提・単位・境界

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

**編集上の補足**

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

## 比較・検証

資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。

## 確認の限界

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

## 元の数値目標と未達の結果

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

## 保存実測値と判定

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

- scikit-sundae official van der Pol example [accessed 2026-11-24]. https://scikit-sundae.readthedocs.io/en/stable/examples/van_der_pol.html; review_level=official-project-example-selected-equations
公式binding例の2階/1階系と初期値を確認。採用μ=1/100,T=2は独自の軽量範囲で、原著やμ1000全周期の再現ではありません。

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
固定版の手法/API・局所許容誤差・終了状態を選択確認。独立原著の全編監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Van der Pol: an early stiffness transition

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

**Methods used**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) (`bdf2`)
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-algorithm)

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

- [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en) (`van-der-pol`)

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.


**Problem figure**

![Van der Pol: an early stiffness transition: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-validation)

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en) (`van-der-pol-stiff-transition`; Same-problem reference · Finite-grid numerical reference)

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.
## Assumptions, units and boundaries

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

**Editorial clarification**

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

## References and validation

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

## Limits

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

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

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/index.json

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded.

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

- scikit-sundae official van der Pol example [accessed 2026-11-24]. https://scikit-sundae.readthedocs.io/en/stable/examples/van_der_pol.html; review_level=official-project-example-selected-equations
Read the equations and initial state in the official binding example. Our mu = 1 and 100, T = 2 inputs are an authored early-transient scope, not an original-paper or full mu = 1000 cycle reproduction.

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
Read selected fixed-version method, API, local-tolerance and termination sections. This is not a full audit of the original research papers.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
