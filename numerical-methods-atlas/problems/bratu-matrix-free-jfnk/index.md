# 解析・中央差分・方向ADによるJacobian不要Newton–Krylov / Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/

## 日本語

[保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-bratu-continuation-jfnk/#bratu-matrix-free-jfnk) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu-matrix-free-jfnk)

### 方程式・問題の定義

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov

補助実行例 · 実行例の定義・検証式

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

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

### 厳密解・参照解

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

#### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-measurements)

解析解 · 同じ問題の参照

u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)

同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

#### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja)

### 計算法

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

- [Jacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja)

補助実行例

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)

## English

[Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-bratu-continuation-jfnk/#bratu-matrix-free-jfnk) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-matrix-free-jfnk-en)

### Equations and problem definitions

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

Supplementary execution example · Example definition or validation formula

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

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

### Exact and reference solutions

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

#### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-measurements)

Analytic reference · Reference for the same problem

u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)

Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

#### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en)

### Numerical methods

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

- [Jacobian-free Newton-Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en)

Supplementary execution example

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
