# 離散fold近傍のBratu感度

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-algorithm)

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。


**問題の図**

![離散fold近傍のBratu感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

- [離散fold近傍のBratu shooting・接線・随伴参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja) (`bratu-fold-sensitivity`; 同じ問題の参照 · 有限格子の数値参照)

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
## 前提・単位・境界

内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。

**編集上の補足**

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

## 採用した計算法

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

## 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

## 確認の限界

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

## 保存実測値と判定

```json
{
  "metrics": {
    "principal_records": 6,
    "FD_state_solves": 36,
    "tight_target_policy": "1e-12 observational; exact returned candidate retained. Passing case does not imply target attained."
  },
  "checks": {
    "n31-point0-finite-state-branches": true,
    "n31-point0-strict-state-reference": true,
    "n31-point0-state-residuals": true,
    "n31-point0-below-discrete-fold": true,
    "n31-point0-strict-gradient-reference": true,
    "n31-point0-direct-duality": true,
    "n31-point0-GMRES-fixed-targets": true,
    "n31-point0-residual-identities": true,
    "n31-point0-FD-complete": true,
    "n31-point1-finite-state-branches": true,
    "n31-point1-strict-state-reference": true,
    "n31-point1-state-residuals": true,
    "n31-point1-below-discrete-fold": true,
    "n31-point1-strict-gradient-reference": true,
    "n31-point1-direct-duality": true,
    "n31-point1-GMRES-fixed-targets": true,
    "n31-point1-residual-identities": true,
    "n31-point1-FD-complete": true,
    "n31-point2-finite-state-branches": true,
    "n31-point2-strict-state-reference": true,
    "n31-point2-state-residuals": true,
    "n31-point2-below-discrete-fold": true,
    "n31-point2-strict-gradient-reference": true,
    "n31-point2-direct-duality": true,
    "n31-point2-GMRES-fixed-targets": true,
    "n31-point2-residual-identities": true,
    "n31-point2-FD-complete": true,
    "n63-point0-finite-state-branches": true,
    "n63-point0-strict-state-reference": true,
    "n63-point0-state-residuals": true,
    "n63-point0-below-discrete-fold": true,
    "n63-point0-strict-gradient-reference": true,
    "n63-point0-direct-duality": true,
    "n63-point0-GMRES-fixed-targets": true,
    "n63-point0-residual-identities": true,
    "n63-point0-FD-complete": true,
    "n63-point1-finite-state-branches": true,
    "n63-point1-strict-state-reference": true,
    "n63-point1-state-residuals": true,
    "n63-point1-below-discrete-fold": true,
    "n63-point1-strict-gradient-reference": true,
    "n63-point1-direct-duality": true,
    "n63-point1-GMRES-fixed-targets": true,
    "n63-point1-residual-identities": true,
    "n63-point1-FD-complete": true,
    "n63-point2-finite-state-branches": true,
    "n63-point2-strict-state-reference": true,
    "n63-point2-state-residuals": true,
    "n63-point2-below-discrete-fold": true,
    "n63-point2-strict-gradient-reference": true,
    "n63-point2-direct-duality": true,
    "n63-point2-GMRES-fixed-targets": true,
    "n63-point2-residual-identities": true,
    "n63-point2-FD-complete": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/index.json

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
math.sumprodの公式API選択箇所を確認。閲覧日は出版年ではなく、一般の正丸め保証ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Bratu sensitivity near the discrete fold

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-algorithm)

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.


**Problem figure**

![Bratu sensitivity near the discrete fold: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

- [Discrete Bratu shooting, tangent and adjoint references near a fold](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en) (`bratu-fold-sensitivity`; Same-problem reference · Finite-grid numerical reference)

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
## Assumptions, units and boundaries

31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.

**Editorial clarification**

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

## Adopted numerical method

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

## References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

## Limits

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

## Stored measurements and decisions

```json
{
  "metrics": {
    "principal_records": 6,
    "FD_state_solves": 36,
    "tight_target_policy": "1e-12 observational; exact returned candidate retained. Passing case does not imply target attained."
  },
  "checks": {
    "n31-point0-finite-state-branches": true,
    "n31-point0-strict-state-reference": true,
    "n31-point0-state-residuals": true,
    "n31-point0-below-discrete-fold": true,
    "n31-point0-strict-gradient-reference": true,
    "n31-point0-direct-duality": true,
    "n31-point0-GMRES-fixed-targets": true,
    "n31-point0-residual-identities": true,
    "n31-point0-FD-complete": true,
    "n31-point1-finite-state-branches": true,
    "n31-point1-strict-state-reference": true,
    "n31-point1-state-residuals": true,
    "n31-point1-below-discrete-fold": true,
    "n31-point1-strict-gradient-reference": true,
    "n31-point1-direct-duality": true,
    "n31-point1-GMRES-fixed-targets": true,
    "n31-point1-residual-identities": true,
    "n31-point1-FD-complete": true,
    "n31-point2-finite-state-branches": true,
    "n31-point2-strict-state-reference": true,
    "n31-point2-state-residuals": true,
    "n31-point2-below-discrete-fold": true,
    "n31-point2-strict-gradient-reference": true,
    "n31-point2-direct-duality": true,
    "n31-point2-GMRES-fixed-targets": true,
    "n31-point2-residual-identities": true,
    "n31-point2-FD-complete": true,
    "n63-point0-finite-state-branches": true,
    "n63-point0-strict-state-reference": true,
    "n63-point0-state-residuals": true,
    "n63-point0-below-discrete-fold": true,
    "n63-point0-strict-gradient-reference": true,
    "n63-point0-direct-duality": true,
    "n63-point0-GMRES-fixed-targets": true,
    "n63-point0-residual-identities": true,
    "n63-point0-FD-complete": true,
    "n63-point1-finite-state-branches": true,
    "n63-point1-strict-state-reference": true,
    "n63-point1-state-residuals": true,
    "n63-point1-below-discrete-fold": true,
    "n63-point1-strict-gradient-reference": true,
    "n63-point1-direct-duality": true,
    "n63-point1-GMRES-fixed-targets": true,
    "n63-point1-residual-identities": true,
    "n63-point1-FD-complete": true,
    "n63-point2-finite-state-branches": true,
    "n63-point2-strict-state-reference": true,
    "n63-point2-state-residuals": true,
    "n63-point2-below-discrete-fold": true,
    "n63-point2-strict-gradient-reference": true,
    "n63-point2-direct-duality": true,
    "n63-point2-GMRES-fixed-targets": true,
    "n63-point2-residual-identities": true,
    "n63-point2-FD-complete": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/index.json

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
Selectedofficial math.sumprod API read;accessdate is notpublicationyear,no globalcorrectrounding claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
