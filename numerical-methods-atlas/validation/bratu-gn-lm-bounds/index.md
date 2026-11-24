# GN・LMと有界最小二乗のBratu比較

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-algorithm)

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。


**問題の図**

![GN・LMと有界最小二乗のBratu比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-validation)

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

- [Bratu逆最小二乗の独立Thomas局所参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja) (`bratu-gn-lm-bounds`; 同じ問題の参照 · 有限格子の数値参照)

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。
## 前提・単位・境界

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。

**編集上の補足**

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

## 採用した計算法

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

## 比較・検証

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

## 確認の限界

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 17,
    "completed_fits": 17,
    "expected_fits": 17,
    "forward_evaluations": 234,
    "maximum_stationarity_inf": 9.69771818404297e-10,
    "reference_scope": "independent Thomas state/Jacobian; shared local TRF optimizer; no global optimum proof"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-objective-reference": true,
    "fit-0-data-rank": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-objective-reference": true,
    "fit-1-data-rank": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-objective-reference": true,
    "fit-2-data-rank": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-objective-reference": true,
    "fit-3-data-rank": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-objective-reference": true,
    "fit-4-data-rank": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-objective-reference": true,
    "fit-5-data-rank": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-objective-reference": true,
    "fit-6-data-rank": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-objective-reference": true,
    "fit-7-data-rank": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-objective-reference": true,
    "fit-8-data-rank": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-objective-reference": true,
    "fit-9-data-rank": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-objective-reference": true,
    "fit-10-data-rank": true,
    "fit-10-feasible": true,
    "fit-10-active-constraint": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-objective-reference": true,
    "fit-11-data-rank": true,
    "fit-11-feasible": true,
    "fit-11-active-constraint": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-objective-reference": true,
    "fit-12-data-rank": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-objective-reference": true,
    "fit-13-data-rank": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-objective-reference": true,
    "fit-14-data-rank": true,
    "fit-14-feasible": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-objective-reference": true,
    "fit-15-data-rank": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-objective-reference": true,
    "fit-16-data-rank": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/index.json

![保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Bratu comparisons of GN, LM and bounded least squares

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-algorithm)

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.


**Problem figure**

![Bratu comparisons of GN, LM and bounded least squares: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-validation)

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

- [Independent Thomas-based local references for Bratu inverse least squares](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en) (`bratu-gn-lm-bounds`; Same-problem reference · Finite-grid numerical reference)

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.
## Assumptions, units and boundaries

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.

**Editorial clarification**

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

## Adopted numerical method

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

## References and validation

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

## Limits

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

## Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 17,
    "completed_fits": 17,
    "expected_fits": 17,
    "forward_evaluations": 234,
    "maximum_stationarity_inf": 9.69771818404297e-10,
    "reference_scope": "independent Thomas state/Jacobian; shared local TRF optimizer; no global optimum proof"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-objective-reference": true,
    "fit-0-data-rank": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-objective-reference": true,
    "fit-1-data-rank": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-objective-reference": true,
    "fit-2-data-rank": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-objective-reference": true,
    "fit-3-data-rank": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-objective-reference": true,
    "fit-4-data-rank": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-objective-reference": true,
    "fit-5-data-rank": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-objective-reference": true,
    "fit-6-data-rank": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-objective-reference": true,
    "fit-7-data-rank": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-objective-reference": true,
    "fit-8-data-rank": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-objective-reference": true,
    "fit-9-data-rank": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-objective-reference": true,
    "fit-10-data-rank": true,
    "fit-10-feasible": true,
    "fit-10-active-constraint": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-objective-reference": true,
    "fit-11-data-rank": true,
    "fit-11-feasible": true,
    "fit-11-active-constraint": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-objective-reference": true,
    "fit-12-data-rank": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-objective-reference": true,
    "fit-13-data-rank": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-objective-reference": true,
    "fit-14-data-rank": true,
    "fit-14-feasible": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-objective-reference": true,
    "fit-15-data-rank": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-objective-reference": true,
    "fit-16-data-rank": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/index.json

![Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
