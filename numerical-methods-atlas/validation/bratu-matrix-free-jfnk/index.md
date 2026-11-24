# 解析・中央差分・方向ADによるJacobian不要Newton–Krylov

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

**使用手法**

- [Jacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja) (`jacobian-free-newton-krylov`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)
- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) (`automatic-differentiation`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-algorithm)

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。


**問題の図**

![解析・中央差分・方向ADによるJacobian不要Newton–Krylov：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-validation)

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja) (`bratu-matrix-free-jfnk`; 同じ問題の参照 · 解析参照)

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。
## 前提・単位・境界

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。

**編集上の補足**

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

## 採用した計算法

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

## 比較・検証

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

## 確認の限界

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "mode_gap_max": 4.884981308350689e-15,
    "qualification_AD_relative": 1.1692887409033045e-17,
    "qualification_FD_relative": 8.651069407676375e-11,
    "reasons": [
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual"
    ],
    "evaluation_scope": "Actualsolverevaluations;analyticlinear-forcingvalidationcountedseparately.NoPETScorassemblednonlinearJacobianusedbyJFNK."
  },
  "checks": {
    "nonzero Jv reference": true,
    "AD Jv exact": true,
    "AD primal exact": true,
    "central FD Jv": true,
    "zero Jv branch": true,
    "0/nonlinear converged": true,
    "0/finite states": true,
    "0/discrete residual": true,
    "0/continuous branch error": true,
    "0/analytic verified forcing": true,
    "0/declared eta": true,
    "0/evaluation count ledger": true,
    "0/bounded Krylov storage": true,
    "0/accepted Armijo steps": true,
    "1/nonlinear converged": true,
    "1/finite states": true,
    "1/discrete residual": true,
    "1/continuous branch error": true,
    "1/analytic verified forcing": true,
    "1/declared eta": true,
    "1/evaluation count ledger": true,
    "1/bounded Krylov storage": true,
    "1/accepted Armijo steps": true,
    "2/nonlinear converged": true,
    "2/finite states": true,
    "2/discrete residual": true,
    "2/continuous branch error": true,
    "2/analytic verified forcing": true,
    "2/declared eta": true,
    "2/evaluation count ledger": true,
    "2/bounded Krylov storage": true,
    "2/accepted Armijo steps": true,
    "3/nonlinear converged": true,
    "3/finite states": true,
    "3/discrete residual": true,
    "3/continuous branch error": true,
    "3/analytic verified forcing": true,
    "3/declared eta": true,
    "3/evaluation count ledger": true,
    "3/bounded Krylov storage": true,
    "3/accepted Armijo steps": true,
    "4/nonlinear converged": true,
    "4/finite states": true,
    "4/discrete residual": true,
    "4/continuous branch error": true,
    "4/analytic verified forcing": true,
    "4/declared eta": true,
    "4/evaluation count ledger": true,
    "4/bounded Krylov storage": true,
    "4/accepted Armijo steps": true,
    "5/nonlinear converged": true,
    "5/finite states": true,
    "5/discrete residual": true,
    "5/continuous branch error": true,
    "5/analytic verified forcing": true,
    "5/declared eta": true,
    "5/evaluation count ledger": true,
    "5/bounded Krylov storage": true,
    "5/accepted Armijo steps": true,
    "6/nonlinear converged": true,
    "6/finite states": true,
    "6/discrete residual": true,
    "6/continuous branch error": true,
    "6/analytic verified forcing": true,
    "6/declared eta": true,
    "6/evaluation count ledger": true,
    "6/bounded Krylov storage": true,
    "6/accepted Armijo steps": true,
    "7/nonlinear converged": true,
    "7/finite states": true,
    "7/discrete residual": true,
    "7/continuous branch error": true,
    "7/analytic verified forcing": true,
    "7/declared eta": true,
    "7/evaluation count ledger": true,
    "7/bounded Krylov storage": true,
    "7/accepted Armijo steps": true,
    "8/nonlinear converged": true,
    "8/finite states": true,
    "8/discrete residual": true,
    "8/continuous branch error": true,
    "8/analytic verified forcing": true,
    "8/declared eta": true,
    "8/evaluation count ledger": true,
    "8/bounded Krylov storage": true,
    "8/accepted Armijo steps": true,
    "9/nonlinear converged": true,
    "9/finite states": true,
    "9/discrete residual": true,
    "9/continuous branch error": true,
    "9/analytic verified forcing": true,
    "9/declared eta": true,
    "9/evaluation count ledger": true,
    "9/bounded Krylov storage": true,
    "9/accepted Armijo steps": true,
    "10/nonlinear converged": true,
    "10/finite states": true,
    "10/discrete residual": true,
    "10/continuous branch error": true,
    "10/analytic verified forcing": true,
    "10/declared eta": true,
    "10/evaluation count ledger": true,
    "10/bounded Krylov storage": true,
    "10/accepted Armijo steps": true,
    "11/nonlinear converged": true,
    "11/finite states": true,
    "11/discrete residual": true,
    "11/continuous branch error": true,
    "11/analytic verified forcing": true,
    "11/declared eta": true,
    "11/evaluation count ledger": true,
    "11/bounded Krylov storage": true,
    "11/accepted Armijo steps": true,
    "12/nonlinear converged": true,
    "12/finite states": true,
    "12/discrete residual": true,
    "12/continuous branch error": true,
    "12/analytic verified forcing": true,
    "12/declared eta": true,
    "12/evaluation count ledger": true,
    "12/bounded Krylov storage": true,
    "12/accepted Armijo steps": true,
    "mode agreement N63 lower": true,
    "mode agreement N63 upper": true,
    "mode agreement N127 lower": true,
    "mode agreement N127 upper": true,
    "finest exact branches": true,
    "all mode errors refine": true,
    "constant forcing companion matches": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/index.json

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- D.A.Knoll,D.E.Keyes (2004). Jacobian-free Newton-Krylov methods: a survey of approaches and applications. https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf; review_level=primary-selected-PDF-text-via-course-mirror
原著のJv・差分刻み・inexact forcing・前処理の選択部分を講義ミラー配送から読解。中央差分と固定clamp付き比率則は明示的な実装選択です。

- S. C. Eisenstat and H. F. Walker (1996). Choosing the Forcing Terms in an Inexact Newton Method. https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf; review_level=primary-selected-PDF-text
著者公開の原著PDFからAlgorithm IN、Choice 2と実用的safeguardの選択部分を確認。本文全体・全証明・性能表の監査ではありません。

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
著者教材のBratu解析族と二枝・丸めた臨界値を確認。変数は採用thetaの2倍で、別導出とDecimal80で資格。1914原著は未読です。

- PETSc developers (2026). PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length. https://petsc.org/release/manual/snes/; review_level=official-selected-documentation
公式3.26.1文書の関連節のみ確認。PETScを使用・実行した成功値は借用せず、二次arc制約と採用超平面を区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

**Methods used**

- [Jacobian-free Newton-Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en) (`jacobian-free-newton-krylov`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)
- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-algorithm)

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.


**Problem figure**

![Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-validation)

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en) (`bratu-matrix-free-jfnk`; Same-problem reference · Analytic reference)

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.
## Assumptions, units and boundaries

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.

**Editorial clarification**

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

## Adopted numerical method

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

## References and validation

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

## Limits

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

## Stored measurements and decisions

```json
{
  "metrics": {
    "mode_gap_max": 4.884981308350689e-15,
    "qualification_AD_relative": 1.1692887409033045e-17,
    "qualification_FD_relative": 8.651069407676375e-11,
    "reasons": [
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual"
    ],
    "evaluation_scope": "Actualsolverevaluations;analyticlinear-forcingvalidationcountedseparately.NoPETScorassemblednonlinearJacobianusedbyJFNK."
  },
  "checks": {
    "nonzero Jv reference": true,
    "AD Jv exact": true,
    "AD primal exact": true,
    "central FD Jv": true,
    "zero Jv branch": true,
    "0/nonlinear converged": true,
    "0/finite states": true,
    "0/discrete residual": true,
    "0/continuous branch error": true,
    "0/analytic verified forcing": true,
    "0/declared eta": true,
    "0/evaluation count ledger": true,
    "0/bounded Krylov storage": true,
    "0/accepted Armijo steps": true,
    "1/nonlinear converged": true,
    "1/finite states": true,
    "1/discrete residual": true,
    "1/continuous branch error": true,
    "1/analytic verified forcing": true,
    "1/declared eta": true,
    "1/evaluation count ledger": true,
    "1/bounded Krylov storage": true,
    "1/accepted Armijo steps": true,
    "2/nonlinear converged": true,
    "2/finite states": true,
    "2/discrete residual": true,
    "2/continuous branch error": true,
    "2/analytic verified forcing": true,
    "2/declared eta": true,
    "2/evaluation count ledger": true,
    "2/bounded Krylov storage": true,
    "2/accepted Armijo steps": true,
    "3/nonlinear converged": true,
    "3/finite states": true,
    "3/discrete residual": true,
    "3/continuous branch error": true,
    "3/analytic verified forcing": true,
    "3/declared eta": true,
    "3/evaluation count ledger": true,
    "3/bounded Krylov storage": true,
    "3/accepted Armijo steps": true,
    "4/nonlinear converged": true,
    "4/finite states": true,
    "4/discrete residual": true,
    "4/continuous branch error": true,
    "4/analytic verified forcing": true,
    "4/declared eta": true,
    "4/evaluation count ledger": true,
    "4/bounded Krylov storage": true,
    "4/accepted Armijo steps": true,
    "5/nonlinear converged": true,
    "5/finite states": true,
    "5/discrete residual": true,
    "5/continuous branch error": true,
    "5/analytic verified forcing": true,
    "5/declared eta": true,
    "5/evaluation count ledger": true,
    "5/bounded Krylov storage": true,
    "5/accepted Armijo steps": true,
    "6/nonlinear converged": true,
    "6/finite states": true,
    "6/discrete residual": true,
    "6/continuous branch error": true,
    "6/analytic verified forcing": true,
    "6/declared eta": true,
    "6/evaluation count ledger": true,
    "6/bounded Krylov storage": true,
    "6/accepted Armijo steps": true,
    "7/nonlinear converged": true,
    "7/finite states": true,
    "7/discrete residual": true,
    "7/continuous branch error": true,
    "7/analytic verified forcing": true,
    "7/declared eta": true,
    "7/evaluation count ledger": true,
    "7/bounded Krylov storage": true,
    "7/accepted Armijo steps": true,
    "8/nonlinear converged": true,
    "8/finite states": true,
    "8/discrete residual": true,
    "8/continuous branch error": true,
    "8/analytic verified forcing": true,
    "8/declared eta": true,
    "8/evaluation count ledger": true,
    "8/bounded Krylov storage": true,
    "8/accepted Armijo steps": true,
    "9/nonlinear converged": true,
    "9/finite states": true,
    "9/discrete residual": true,
    "9/continuous branch error": true,
    "9/analytic verified forcing": true,
    "9/declared eta": true,
    "9/evaluation count ledger": true,
    "9/bounded Krylov storage": true,
    "9/accepted Armijo steps": true,
    "10/nonlinear converged": true,
    "10/finite states": true,
    "10/discrete residual": true,
    "10/continuous branch error": true,
    "10/analytic verified forcing": true,
    "10/declared eta": true,
    "10/evaluation count ledger": true,
    "10/bounded Krylov storage": true,
    "10/accepted Armijo steps": true,
    "11/nonlinear converged": true,
    "11/finite states": true,
    "11/discrete residual": true,
    "11/continuous branch error": true,
    "11/analytic verified forcing": true,
    "11/declared eta": true,
    "11/evaluation count ledger": true,
    "11/bounded Krylov storage": true,
    "11/accepted Armijo steps": true,
    "12/nonlinear converged": true,
    "12/finite states": true,
    "12/discrete residual": true,
    "12/continuous branch error": true,
    "12/analytic verified forcing": true,
    "12/declared eta": true,
    "12/evaluation count ledger": true,
    "12/bounded Krylov storage": true,
    "12/accepted Armijo steps": true,
    "mode agreement N63 lower": true,
    "mode agreement N63 upper": true,
    "mode agreement N127 lower": true,
    "mode agreement N127 upper": true,
    "finest exact branches": true,
    "all mode errors refine": true,
    "constant forcing companion matches": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/index.json

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- D.A.Knoll,D.E.Keyes (2004). Jacobian-free Newton-Krylov methods: a survey of approaches and applications. https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf; review_level=primary-selected-PDF-text-via-course-mirror
Selected primary Jv,FDscale,inexactforcing andpreconditioning sections readvia disclosedcourse mirror; centralFD/cappedrule areexplicitimplementation choices.

- S. C. Eisenstat and H. F. Walker (1996). Choosing the Forcing Terms in an Inexact Newton Method. https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf; review_level=primary-selected-PDF-text
Read selected Algorithm IN, Choice 2 and safeguard passages from the author-hosted original; not a full proof or performance-table audit.

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
Read author exercise exactfamily/twobranches/roundedcritical; itsparameter istwiceourtheta. Independentderivation/Decimal80qualification;1914originalunread.

- PETSc developers (2026). PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length. https://petsc.org/release/manual/snes/; review_level=official-selected-documentation
Selected official3.26.1sections only; noPETSc execution orborrowed result. Distinguish itsquadraticarcconstraint fromourhyperplane.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
