# 雑音・モデル差と有限γ経路の正則化

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-algorithm)

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。


**問題の図**

![雑音・モデル差と有限γ経路の正則化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-validation)

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

- [有限γ経路と局所線形雑音伝播のBratu参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja) (`bratu-noise-regularization`; 同じ問題の参照 · 有限格子の数値参照)

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。
## 前提・単位・境界

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。

**編集上の補足**

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

## 採用した計算法

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

## 比較・検証

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

## 確認の限界

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

## 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 42,
    "completed_fits": 42,
    "expected_fits": 42,
    "independent_base_noise_vectors": 2,
    "coupled_gamma_paths": 8,
    "forward_evaluations": 339,
    "maximum_stationarity_inf": 2.8491609072034407e-10,
    "covariance_scope": "fixed-gamma Gauss–Newton local-linear-model plug-in; no selection-event covariance or coverage claim",
    "detailed_fit_records": "case67-all-fits.json"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-feasible": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-feasible": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-feasible": true,
    "path-0-complete": true,
    "path-0-selection": true,
    "path-0-covariance-eligibility-and-psd": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-feasible": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-feasible": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-feasible": true,
    "path-1-complete": true,
    "path-1-selection": true,
    "path-1-covariance-eligibility-and-psd": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-feasible": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-feasible": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-feasible": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-feasible": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-feasible": true,
    "path-2-complete": true,
    "path-2-selection": true,
    "path-2-covariance-eligibility-and-psd": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-feasible": true,
    "fit-17-complete": true,
    "fit-17-final-forward-residual": true,
    "fit-17-stationary": true,
    "fit-17-feasible": true,
    "fit-18-complete": true,
    "fit-18-final-forward-residual": true,
    "fit-18-stationary": true,
    "fit-18-feasible": true,
    "fit-19-complete": true,
    "fit-19-final-forward-residual": true,
    "fit-19-stationary": true,
    "fit-19-feasible": true,
    "path-3-complete": true,
    "path-3-selection": true,
    "path-3-covariance-eligibility-and-psd": true,
    "fit-20-complete": true,
    "fit-20-final-forward-residual": true,
    "fit-20-stationary": true,
    "fit-20-feasible": true,
    "fit-21-complete": true,
    "fit-21-final-forward-residual": true,
    "fit-21-stationary": true,
    "fit-21-feasible": true,
    "fit-22-complete": true,
    "fit-22-final-forward-residual": true,
    "fit-22-stationary": true,
    "fit-22-feasible": true,
    "fit-23-complete": true,
    "fit-23-final-forward-residual": true,
    "fit-23-stationary": true,
    "fit-23-feasible": true,
    "fit-24-complete": true,
    "fit-24-final-forward-residual": true,
    "fit-24-stationary": true,
    "fit-24-feasible": true,
    "path-4-complete": true,
    "path-4-selection": true,
    "path-4-covariance-eligibility-and-psd": true,
    "fit-25-complete": true,
    "fit-25-final-forward-residual": true,
    "fit-25-stationary": true,
    "fit-25-feasible": true,
    "fit-26-complete": true,
    "fit-26-final-forward-residual": true,
    "fit-26-stationary": true,
    "fit-26-feasible": true,
    "fit-27-complete": true,
    "fit-27-final-forward-residual": true,
    "fit-27-stationary": true,
    "fit-27-feasible": true,
    "fit-28-complete": true,
    "fit-28-final-forward-residual": true,
    "fit-28-stationary": true,
    "fit-28-feasible": true,
    "fit-29-complete": true,
    "fit-29-final-forward-residual": true,
    "fit-29-stationary": true,
    "fit-29-feasible": true,
    "path-5-complete": true,
    "path-5-selection": true,
    "path-5-covariance-eligibility-and-psd": true,
    "fit-30-complete": true,
    "fit-30-final-forward-residual": true,
    "fit-30-stationary": true,
    "fit-30-feasible": true,
    "fit-31-complete": true,
    "fit-31-final-forward-residual": true,
    "fit-31-stationary": true,
    "fit-31-feasible": true,
    "fit-32-complete": true,
    "fit-32-final-forward-residual": true,
    "fit-32-stationary": true,
    "fit-32-feasible": true,
    "fit-33-complete": true,
    "fit-33-final-forward-residual": true,
    "fit-33-stationary": true,
    "fit-33-feasible": true,
    "fit-34-complete": true,
    "fit-34-final-forward-residual": true,
    "fit-34-stationary": true,
    "fit-34-feasible": true,
    "path-6-complete": true,
    "path-6-selection": true,
    "path-6-covariance-eligibility-and-psd": true,
    "fit-35-complete": true,
    "fit-35-final-forward-residual": true,
    "fit-35-stationary": true,
    "fit-35-feasible": true,
    "fit-36-complete": true,
    "fit-36-final-forward-residual": true,
    "fit-36-stationary": true,
    "fit-36-feasible": true,
    "fit-37-complete": true,
    "fit-37-final-forward-residual": true,
    "fit-37-stationary": true,
    "fit-37-feasible": true,
    "fit-38-complete": true,
    "fit-38-final-forward-residual": true,
    "fit-38-stationary": true,
    "fit-38-feasible": true,
    "fit-39-complete": true,
    "fit-39-final-forward-residual": true,
    "fit-39-stationary": true,
    "fit-39-feasible": true,
    "path-7-complete": true,
    "path-7-selection": true,
    "path-7-covariance-eligibility-and-psd": true,
    "fit-40-complete": true,
    "fit-40-final-forward-residual": true,
    "fit-40-stationary": true,
    "fit-40-feasible": true,
    "fit-41-complete": true,
    "fit-41-final-forward-residual": true,
    "fit-41-stationary": true,
    "fit-41-feasible": true,
    "linear-control-covariance": true,
    "linear-control-bias": true,
    "linear-control-data-shift": true,
    "linear-control-symmetry": true,
    "linear-control-psd": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/index.json

![保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。

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

- Regularization Tools, Version 4.1 for Matlab 7.3 [accessed 2026-11-24]. https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf; review_level=selected-primary-scope
Official author manual: selected text around Section 2.5 and Section 2.9; physical pages 20 and 37 (printed 18 and 35) rendered locally and visually inspected. L-curve residual/solution norm tradeoff and discrepancy equation (2.61) were read. Four-point chord curvature here is a finite-list diagnostic, not the manual spline/corner algorithm, a theorem of optimal regularization or coverage. Original software (1994) and later article (2007) are separate bibliographic works and were not read.

- SciPy 1.14.1 curve_fit documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.curve_fit.html; review_level=selected-primary-scope
sigma/absolute_sigma and covariance interpretation sections. The penalized sandwich covariance in this study is derived independently; it is not presented as curve_fit output.

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Noise, model discrepancy and finite gamma paths

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-algorithm)

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.


**Problem figure**

![Noise, model discrepancy and finite gamma paths: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-validation)

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

- [Bratu references for finite gamma paths and local linear noise propagation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en) (`bratu-noise-regularization`; Same-problem reference · Finite-grid numerical reference)

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.
## Assumptions, units and boundaries

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.

**Editorial clarification**

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

## Adopted numerical method

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

## References and validation

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

## Limits

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

## Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 42,
    "completed_fits": 42,
    "expected_fits": 42,
    "independent_base_noise_vectors": 2,
    "coupled_gamma_paths": 8,
    "forward_evaluations": 339,
    "maximum_stationarity_inf": 2.8491609072034407e-10,
    "covariance_scope": "fixed-gamma Gauss–Newton local-linear-model plug-in; no selection-event covariance or coverage claim",
    "detailed_fit_records": "case67-all-fits.json"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-feasible": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-feasible": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-feasible": true,
    "path-0-complete": true,
    "path-0-selection": true,
    "path-0-covariance-eligibility-and-psd": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-feasible": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-feasible": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-feasible": true,
    "path-1-complete": true,
    "path-1-selection": true,
    "path-1-covariance-eligibility-and-psd": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-feasible": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-feasible": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-feasible": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-feasible": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-feasible": true,
    "path-2-complete": true,
    "path-2-selection": true,
    "path-2-covariance-eligibility-and-psd": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-feasible": true,
    "fit-17-complete": true,
    "fit-17-final-forward-residual": true,
    "fit-17-stationary": true,
    "fit-17-feasible": true,
    "fit-18-complete": true,
    "fit-18-final-forward-residual": true,
    "fit-18-stationary": true,
    "fit-18-feasible": true,
    "fit-19-complete": true,
    "fit-19-final-forward-residual": true,
    "fit-19-stationary": true,
    "fit-19-feasible": true,
    "path-3-complete": true,
    "path-3-selection": true,
    "path-3-covariance-eligibility-and-psd": true,
    "fit-20-complete": true,
    "fit-20-final-forward-residual": true,
    "fit-20-stationary": true,
    "fit-20-feasible": true,
    "fit-21-complete": true,
    "fit-21-final-forward-residual": true,
    "fit-21-stationary": true,
    "fit-21-feasible": true,
    "fit-22-complete": true,
    "fit-22-final-forward-residual": true,
    "fit-22-stationary": true,
    "fit-22-feasible": true,
    "fit-23-complete": true,
    "fit-23-final-forward-residual": true,
    "fit-23-stationary": true,
    "fit-23-feasible": true,
    "fit-24-complete": true,
    "fit-24-final-forward-residual": true,
    "fit-24-stationary": true,
    "fit-24-feasible": true,
    "path-4-complete": true,
    "path-4-selection": true,
    "path-4-covariance-eligibility-and-psd": true,
    "fit-25-complete": true,
    "fit-25-final-forward-residual": true,
    "fit-25-stationary": true,
    "fit-25-feasible": true,
    "fit-26-complete": true,
    "fit-26-final-forward-residual": true,
    "fit-26-stationary": true,
    "fit-26-feasible": true,
    "fit-27-complete": true,
    "fit-27-final-forward-residual": true,
    "fit-27-stationary": true,
    "fit-27-feasible": true,
    "fit-28-complete": true,
    "fit-28-final-forward-residual": true,
    "fit-28-stationary": true,
    "fit-28-feasible": true,
    "fit-29-complete": true,
    "fit-29-final-forward-residual": true,
    "fit-29-stationary": true,
    "fit-29-feasible": true,
    "path-5-complete": true,
    "path-5-selection": true,
    "path-5-covariance-eligibility-and-psd": true,
    "fit-30-complete": true,
    "fit-30-final-forward-residual": true,
    "fit-30-stationary": true,
    "fit-30-feasible": true,
    "fit-31-complete": true,
    "fit-31-final-forward-residual": true,
    "fit-31-stationary": true,
    "fit-31-feasible": true,
    "fit-32-complete": true,
    "fit-32-final-forward-residual": true,
    "fit-32-stationary": true,
    "fit-32-feasible": true,
    "fit-33-complete": true,
    "fit-33-final-forward-residual": true,
    "fit-33-stationary": true,
    "fit-33-feasible": true,
    "fit-34-complete": true,
    "fit-34-final-forward-residual": true,
    "fit-34-stationary": true,
    "fit-34-feasible": true,
    "path-6-complete": true,
    "path-6-selection": true,
    "path-6-covariance-eligibility-and-psd": true,
    "fit-35-complete": true,
    "fit-35-final-forward-residual": true,
    "fit-35-stationary": true,
    "fit-35-feasible": true,
    "fit-36-complete": true,
    "fit-36-final-forward-residual": true,
    "fit-36-stationary": true,
    "fit-36-feasible": true,
    "fit-37-complete": true,
    "fit-37-final-forward-residual": true,
    "fit-37-stationary": true,
    "fit-37-feasible": true,
    "fit-38-complete": true,
    "fit-38-final-forward-residual": true,
    "fit-38-stationary": true,
    "fit-38-feasible": true,
    "fit-39-complete": true,
    "fit-39-final-forward-residual": true,
    "fit-39-stationary": true,
    "fit-39-feasible": true,
    "path-7-complete": true,
    "path-7-selection": true,
    "path-7-covariance-eligibility-and-psd": true,
    "fit-40-complete": true,
    "fit-40-final-forward-residual": true,
    "fit-40-stationary": true,
    "fit-40-feasible": true,
    "fit-41-complete": true,
    "fit-41-final-forward-residual": true,
    "fit-41-stationary": true,
    "fit-41-feasible": true,
    "linear-control-covariance": true,
    "linear-control-bias": true,
    "linear-control-data-shift": true,
    "linear-control-symmetry": true,
    "linear-control-psd": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/index.json

![Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.

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

- Regularization Tools, Version 4.1 for Matlab 7.3 [accessed 2026-11-24]. https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf; review_level=selected-primary-scope
Official author manual: selected text around Section 2.5 and Section 2.9; physical pages 20 and 37 (printed 18 and 35) rendered locally and visually inspected. L-curve residual/solution norm tradeoff and discrepancy equation (2.61) were read. Four-point chord curvature here is a finite-list diagnostic, not the manual spline/corner algorithm, a theorem of optimal regularization or coverage. Original software (1994) and later article (2007) are separate bibliographic works and were not read.

- SciPy 1.14.1 curve_fit documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.curve_fit.html; review_level=selected-primary-scope
sigma/absolute_sigma and covariance interpretation sections. The penalized sandwich covariance in this study is derived independently; it is not presented as curve_fit output.

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
