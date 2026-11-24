# 小型FNOの問題単位検証

同じ重みで32/64点・未見関数・OODを分けて評価します。

**使用手法**

- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) (`pinn-operators`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-algorithm)

入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。


**問題の図**

![小型FNOの問題単位検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-validation)

全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照 · 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja) (`fno-periodic-heat`; 関連モデルの参照 · 解析参照)

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。
## 前提・単位・境界

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

**編集上の補足**

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。 旧熱拡散primaryを保持し、今回の[0,2π)・問題単位データ族・νとTは別入力として示します。

## 採用した計算法

入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

## 比較・検証

全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

## 確認の限界

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seed-8501:optimizer-converged": false,
    "seed-8501:ID-N32-relative": true,
    "seed-8501:ID-N64-relative": true,
    "seed-8501:norm-control-absolute": true,
    "seed-8502:optimizer-converged": false,
    "seed-8502:ID-N32-relative": true,
    "seed-8502:ID-N64-relative": true,
    "seed-8502:norm-control-absolute": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 8,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "models": 2,
    "parameters_per_model": 93,
    "whole_problem_IDs": 46,
    "prediction_rows": 116,
    "nonlinear_dealiasing": "none",
    "restriction_discrepancy_scope": "Native-grid nonlinear/alias sensitivity, not continuum error"
  },
  "checks": {
    "seed-8501:finite-parameters": true,
    "seed-8501:optimizer-return-status": true,
    "seed-8501:actual-work": true,
    "seed-8501:relative-NA": true,
    "seed-8502:finite-parameters": true,
    "seed-8502:optimizer-return-status": true,
    "seed-8502:actual-work": true,
    "seed-8502:relative-NA": true,
    "disjoint-whole-problem-IDs": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/index.json

![同じ重みで32/64点・未見関数・OODを分けて評価します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat-preview.png)

同じ重みで32/64点・未見関数・OODを分けて評価します。 保存値だけを描画します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Fourier Neural Operator for Parametric Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/html/2010.08895v3; review_level=selected-primary-body
Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Tiny FNO on held-out heat problems

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

**Methods used**

- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) (`pinn-operators`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-algorithm)

Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.


**Problem figure**

![Tiny FNO on held-out heat problems: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-validation)

Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference · Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en) (`fno-periodic-heat`; Related-model reference · Analytic reference)

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.
## Assumptions, units and boundaries

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

**Editorial clarification**

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination. The old heat primary remains. This [0,2pi) whole-problem family, diffusivities and final time are separate fixed inputs.

## Adopted numerical method

Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

## References and validation

Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

## Limits

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seed-8501:optimizer-converged": false,
    "seed-8501:ID-N32-relative": true,
    "seed-8501:ID-N64-relative": true,
    "seed-8501:norm-control-absolute": true,
    "seed-8502:optimizer-converged": false,
    "seed-8502:ID-N32-relative": true,
    "seed-8502:ID-N64-relative": true,
    "seed-8502:norm-control-absolute": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 8,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "models": 2,
    "parameters_per_model": 93,
    "whole_problem_IDs": 46,
    "prediction_rows": 116,
    "nonlinear_dealiasing": "none",
    "restriction_discrepancy_scope": "Native-grid nonlinear/alias sensitivity, not continuum error"
  },
  "checks": {
    "seed-8501:finite-parameters": true,
    "seed-8501:optimizer-return-status": true,
    "seed-8501:actual-work": true,
    "seed-8501:relative-NA": true,
    "seed-8502:finite-parameters": true,
    "seed-8502:optimizer-return-status": true,
    "seed-8502:actual-work": true,
    "seed-8502:relative-NA": true,
    "disjoint-whole-problem-IDs": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/index.json

![Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat-preview.png)

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs. This figure reads saved data only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Fourier Neural Operator for Parametric Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/html/2010.08895v3; review_level=selected-primary-body
Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
