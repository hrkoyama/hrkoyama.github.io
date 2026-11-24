# 対称不定値鞍点系とSchur前処理

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

**使用手法**

- [対称不定値系の教育用MINRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja) (`minres`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-algorithm)

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`)

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。


**問題の図**

![対称不定値鞍点系とSchur前処理：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-validation)

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja) (`symmetric-saddle-minres`; 同じ問題の参照 · 有限格子の数値参照)

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。
## 前提・単位・境界

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。

**編集上の補足**

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

## 採用した計算法

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

## 比較・検証

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

## 確認の限界

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_original_relative_residual": 2.340278567268362e-13,
    "max_relative_reference_error": 4.2310885906326075e-10,
    "max_iterations": 29,
    "max_condition_infinity_estimate": 5682.080194251278
  },
  "checks": {
    "n12/ideal-Schur-three-point-spectrum": true,
    "saddle-12-none-minres/finite": true,
    "saddle-12-none-minres/same-true-residual": true,
    "saddle-12-none-minres/independent-reference": true,
    "saddle-12-none-minres/basis-orthogonality": true,
    "saddle-12-none-minres/symmetric-congruence": true,
    "saddle-12-none-minres/fixed-dimension-budget": true,
    "saddle-12-none-gmres/finite": true,
    "saddle-12-none-gmres/same-true-residual": true,
    "saddle-12-none-gmres/independent-reference": true,
    "saddle-12-none-gmres/basis-orthogonality": true,
    "saddle-12-none-gmres/symmetric-congruence": true,
    "saddle-12-none-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/finite": true,
    "saddle-12-exact-Schur-minres/same-true-residual": true,
    "saddle-12-exact-Schur-minres/independent-reference": true,
    "saddle-12-exact-Schur-minres/basis-orthogonality": true,
    "saddle-12-exact-Schur-minres/symmetric-congruence": true,
    "saddle-12-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-12-exact-Schur-gmres/finite": true,
    "saddle-12-exact-Schur-gmres/same-true-residual": true,
    "saddle-12-exact-Schur-gmres/independent-reference": true,
    "saddle-12-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-12-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-12-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-gmres/ideal-three-step-control": true,
    "n24/ideal-Schur-three-point-spectrum": true,
    "saddle-24-none-minres/finite": true,
    "saddle-24-none-minres/same-true-residual": true,
    "saddle-24-none-minres/independent-reference": true,
    "saddle-24-none-minres/basis-orthogonality": true,
    "saddle-24-none-minres/symmetric-congruence": true,
    "saddle-24-none-minres/fixed-dimension-budget": true,
    "saddle-24-none-gmres/finite": true,
    "saddle-24-none-gmres/same-true-residual": true,
    "saddle-24-none-gmres/independent-reference": true,
    "saddle-24-none-gmres/basis-orthogonality": true,
    "saddle-24-none-gmres/symmetric-congruence": true,
    "saddle-24-none-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/finite": true,
    "saddle-24-exact-Schur-minres/same-true-residual": true,
    "saddle-24-exact-Schur-minres/independent-reference": true,
    "saddle-24-exact-Schur-minres/basis-orthogonality": true,
    "saddle-24-exact-Schur-minres/symmetric-congruence": true,
    "saddle-24-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-24-exact-Schur-gmres/finite": true,
    "saddle-24-exact-Schur-gmres/same-true-residual": true,
    "saddle-24-exact-Schur-gmres/independent-reference": true,
    "saddle-24-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-24-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-24-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-gmres/ideal-three-step-control": true,
    "CG/explicit-negative-curvature-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/index.json

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

速度サイズ24の固定例で使う、保存した35×35鞍点行列。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Paige and Saunders: Stanford SOL MINRES. https://web.stanford.edu/group/SOL/software/minres/; review_level=selected-author-official-documentation
Selected discussion of symmetric indefinite systems, SPD preconditioners and the original residual was read. The original 1975 paper was not read. This stored-basis Lanczos least-squares variant is not a copy of the production short recurrence.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Symmetric saddle systems and Schur preconditioning

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

**Methods used**

- [Educational MINRES for symmetric-indefinite systems](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en) (`minres`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-algorithm)

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`)

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.


**Problem figure**

![Symmetric saddle systems and Schur preconditioning: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-validation)

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en) (`symmetric-saddle-minres`; Same-problem reference · Finite-grid numerical reference)

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.
## Assumptions, units and boundaries

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.

**Editorial clarification**

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

## Adopted numerical method

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

## References and validation

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

## Limits

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_original_relative_residual": 2.340278567268362e-13,
    "max_relative_reference_error": 4.2310885906326075e-10,
    "max_iterations": 29,
    "max_condition_infinity_estimate": 5682.080194251278
  },
  "checks": {
    "n12/ideal-Schur-three-point-spectrum": true,
    "saddle-12-none-minres/finite": true,
    "saddle-12-none-minres/same-true-residual": true,
    "saddle-12-none-minres/independent-reference": true,
    "saddle-12-none-minres/basis-orthogonality": true,
    "saddle-12-none-minres/symmetric-congruence": true,
    "saddle-12-none-minres/fixed-dimension-budget": true,
    "saddle-12-none-gmres/finite": true,
    "saddle-12-none-gmres/same-true-residual": true,
    "saddle-12-none-gmres/independent-reference": true,
    "saddle-12-none-gmres/basis-orthogonality": true,
    "saddle-12-none-gmres/symmetric-congruence": true,
    "saddle-12-none-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/finite": true,
    "saddle-12-exact-Schur-minres/same-true-residual": true,
    "saddle-12-exact-Schur-minres/independent-reference": true,
    "saddle-12-exact-Schur-minres/basis-orthogonality": true,
    "saddle-12-exact-Schur-minres/symmetric-congruence": true,
    "saddle-12-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-12-exact-Schur-gmres/finite": true,
    "saddle-12-exact-Schur-gmres/same-true-residual": true,
    "saddle-12-exact-Schur-gmres/independent-reference": true,
    "saddle-12-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-12-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-12-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-gmres/ideal-three-step-control": true,
    "n24/ideal-Schur-three-point-spectrum": true,
    "saddle-24-none-minres/finite": true,
    "saddle-24-none-minres/same-true-residual": true,
    "saddle-24-none-minres/independent-reference": true,
    "saddle-24-none-minres/basis-orthogonality": true,
    "saddle-24-none-minres/symmetric-congruence": true,
    "saddle-24-none-minres/fixed-dimension-budget": true,
    "saddle-24-none-gmres/finite": true,
    "saddle-24-none-gmres/same-true-residual": true,
    "saddle-24-none-gmres/independent-reference": true,
    "saddle-24-none-gmres/basis-orthogonality": true,
    "saddle-24-none-gmres/symmetric-congruence": true,
    "saddle-24-none-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/finite": true,
    "saddle-24-exact-Schur-minres/same-true-residual": true,
    "saddle-24-exact-Schur-minres/independent-reference": true,
    "saddle-24-exact-Schur-minres/basis-orthogonality": true,
    "saddle-24-exact-Schur-minres/symmetric-congruence": true,
    "saddle-24-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-24-exact-Schur-gmres/finite": true,
    "saddle-24-exact-Schur-gmres/same-true-residual": true,
    "saddle-24-exact-Schur-gmres/independent-reference": true,
    "saddle-24-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-24-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-24-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-gmres/ideal-three-step-control": true,
    "CG/explicit-negative-curvature-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/index.json

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

The saved 35 x 35 saddle matrix for velocity size 24.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Paige and Saunders: Stanford SOL MINRES. https://web.stanford.edu/group/SOL/software/minres/; review_level=selected-author-official-documentation
Selected discussion of symmetric indefinite systems, SPD preconditioners and the original residual was read. The original 1975 paper was not read. This stored-basis Lanczos least-squares variant is not a copy of the production short recurrence.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
