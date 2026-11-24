# 同じ初期値から線探索と信頼領域を比べる

原残差・scaled meritと全試行の記録から、根・非根停留・上限終了を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 同じ難しい初期値に対する線探索と信頼領域

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

**使用手法**

- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)
- [小固定系のdogleg信頼領域法](https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=ja) (`dogleg-trust-region`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-algorithm)

原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。


**問題の図**

![同じ難しい初期値に対する線探索と信頼領域：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-validation)

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [同一初期値の大域化：解析対照と離散Bratu修正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja) (`globalization-difficult-starts`; 同じ問題の参照 · 有限格子の数値参照)

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。
### 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

### 採用した計算法

原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

### 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

### 確認の限界

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_required_unscaled_residual": 9.581336599939344e-11,
    "max_required_state_or_correction_error": 1.1079606960955801e-10,
    "max_model_ledger_defect": 1.1920928955078125e-07,
    "total_residual_evaluations": 322,
    "rejected_trials": 37
  },
  "checks": {
    "rosenbrock-unit-minus-full-newton/finite_saved_history": true,
    "rosenbrock-unit-minus-full-newton/original_residual_recomputed": true,
    "rosenbrock-unit-minus-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-full-newton/method_step_ledger": true,
    "rosenbrock-unit-minus-full-newton/work_caps": true,
    "rosenbrock-unit-minus-full-newton/termination_category": true,
    "rosenbrock-unit-minus-armijo-newton/finite_saved_history": true,
    "rosenbrock-unit-minus-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-unit-minus-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-armijo-newton/method_step_ledger": true,
    "rosenbrock-unit-minus-armijo-newton/work_caps": true,
    "rosenbrock-unit-minus-armijo-newton/termination_category": true,
    "rosenbrock-unit-minus-armijo-newton/original_root_residual": true,
    "rosenbrock-unit-minus-armijo-newton/independent_state_or_correction_error": true,
    "rosenbrock-unit-minus-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-unit-minus-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-unit-minus-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-unit-minus-dogleg-trust-region/work_caps": true,
    "rosenbrock-unit-minus-dogleg-trust-region/termination_category": true,
    "rosenbrock-unit-minus-dogleg-trust-region/original_root_residual": true,
    "rosenbrock-unit-minus-dogleg-trust-region/independent_state_or_correction_error": true,
    "rosenbrock-unit-zero-full-newton/finite_saved_history": true,
    "rosenbrock-unit-zero-full-newton/original_residual_recomputed": true,
    "rosenbrock-unit-zero-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-full-newton/method_step_ledger": true,
    "rosenbrock-unit-zero-full-newton/work_caps": true,
    "rosenbrock-unit-zero-full-newton/termination_category": true,
    "rosenbrock-unit-zero-armijo-newton/finite_saved_history": true,
    "rosenbrock-unit-zero-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-unit-zero-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-armijo-newton/method_step_ledger": true,
    "rosenbrock-unit-zero-armijo-newton/work_caps": true,
    "rosenbrock-unit-zero-armijo-newton/termination_category": true,
    "rosenbrock-unit-zero-armijo-newton/original_root_residual": true,
    "rosenbrock-unit-zero-armijo-newton/independent_state_or_correction_error": true,
    "rosenbrock-unit-zero-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-unit-zero-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-unit-zero-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-unit-zero-dogleg-trust-region/work_caps": true,
    "rosenbrock-unit-zero-dogleg-trust-region/termination_category": true,
    "rosenbrock-unit-zero-dogleg-trust-region/original_root_residual": true,
    "rosenbrock-unit-zero-dogleg-trust-region/independent_state_or_correction_error": true,
    "rosenbrock-left-scaled-minus-full-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-full-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-full-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-full-newton/work_caps": true,
    "rosenbrock-left-scaled-minus-full-newton/termination_category": true,
    "rosenbrock-left-scaled-minus-armijo-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-armijo-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-armijo-newton/work_caps": true,
    "rosenbrock-left-scaled-minus-armijo-newton/termination_category": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/work_caps": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/termination_category": true,
    "rosenbrock-left-scaled-zero-full-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-full-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-full-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-full-newton/work_caps": true,
    "rosenbrock-left-scaled-zero-full-newton/termination_category": true,
    "rosenbrock-left-scaled-zero-armijo-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-armijo-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-armijo-newton/work_caps": true,
    "rosenbrock-left-scaled-zero-armijo-newton/termination_category": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/work_caps": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/termination_category": true,
    "bratu-amp0-full-newton/finite_saved_history": true,
    "bratu-amp0-full-newton/original_residual_recomputed": true,
    "bratu-amp0-full-newton/scaled_merit_recomputed": true,
    "bratu-amp0-full-newton/method_step_ledger": true,
    "bratu-amp0-full-newton/work_caps": true,
    "bratu-amp0-full-newton/termination_category": true,
    "bratu-amp0-armijo-newton/finite_saved_history": true,
    "bratu-amp0-armijo-newton/original_residual_recomputed": true,
    "bratu-amp0-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp0-armijo-newton/method_step_ledger": true,
    "bratu-amp0-armijo-newton/work_caps": true,
    "bratu-amp0-armijo-newton/termination_category": true,
    "bratu-amp0-armijo-newton/original_root_residual": true,
    "bratu-amp0-armijo-newton/independent_state_or_correction_error": true,
    "bratu-amp0-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp0-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp0-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp0-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp0-dogleg-trust-region/work_caps": true,
    "bratu-amp0-dogleg-trust-region/termination_category": true,
    "bratu-amp0-dogleg-trust-region/original_root_residual": true,
    "bratu-amp0-dogleg-trust-region/independent_state_or_correction_error": true,
    "bratu-amp4-full-newton/finite_saved_history": true,
    "bratu-amp4-full-newton/original_residual_recomputed": true,
    "bratu-amp4-full-newton/scaled_merit_recomputed": true,
    "bratu-amp4-full-newton/method_step_ledger": true,
    "bratu-amp4-full-newton/work_caps": true,
    "bratu-amp4-full-newton/termination_category": true,
    "bratu-amp4-armijo-newton/finite_saved_history": true,
    "bratu-amp4-armijo-newton/original_residual_recomputed": true,
    "bratu-amp4-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp4-armijo-newton/method_step_ledger": true,
    "bratu-amp4-armijo-newton/work_caps": true,
    "bratu-amp4-armijo-newton/termination_category": true,
    "bratu-amp4-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp4-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp4-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp4-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp4-dogleg-trust-region/work_caps": true,
    "bratu-amp4-dogleg-trust-region/termination_category": true,
    "bratu-amp8-full-newton/finite_saved_history": true,
    "bratu-amp8-full-newton/original_residual_recomputed": true,
    "bratu-amp8-full-newton/scaled_merit_recomputed": true,
    "bratu-amp8-full-newton/method_step_ledger": true,
    "bratu-amp8-full-newton/work_caps": true,
    "bratu-amp8-full-newton/termination_category": true,
    "bratu-amp8-armijo-newton/finite_saved_history": true,
    "bratu-amp8-armijo-newton/original_residual_recomputed": true,
    "bratu-amp8-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp8-armijo-newton/method_step_ledger": true,
    "bratu-amp8-armijo-newton/work_caps": true,
    "bratu-amp8-armijo-newton/termination_category": true,
    "bratu-amp8-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp8-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp8-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp8-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp8-dogleg-trust-region/work_caps": true,
    "bratu-amp8-dogleg-trust-region/termination_category": true,
    "stationary-armijo-newton/stationary_nonroot_status": true,
    "stationary-armijo-newton/not_false_root": true,
    "stationary-dogleg-trust-region/stationary_nonroot_status": true,
    "stationary-dogleg-trust-region/not_false_root": true,
    "domain/rejected_before_exp_evaluation": true,
    "domain/finite_candidate_retained": true,
    "exact24_main_records": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/index.json

![同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- PETSc developers (n.d.). SNES: Nonlinear Solvers [accessed 2026-11-24]. https://petsc.org/release/manual/snes/; review_level=official-documentation-selected-sections
Read nonlinear solver categories, stopping/domain-error distinctions and selected line-search/trust-region descriptions. Our fixed Euclidean dogleg and Delta0=1 are independently specified; not asserted to reproduce PETSc defaults. Unread: MINPACK original report/paper, PETSc solver implementation source, Full manual outside named sections. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
