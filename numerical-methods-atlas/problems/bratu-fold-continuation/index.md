# 擬似弧長継続でBratuのfoldを越える / Crossing the Bratu fold with pseudo-arclength continuation

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/

## 日本語

[保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-bratu-continuation-jfnk/#bratu-fold-continuation) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu-fold-continuation)

### 方程式・問題の定義

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 擬似弧長継続でBratuのfoldを越える

補助実行例 · 実行例の定義・検証式

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

### 厳密解・参照解

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

#### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-measurements)

解析解 · 同じ問題の参照

u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)

同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

#### 擬似弧長継続でBratuのfoldを越える

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja)

### 計算法

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

- [重み付き擬似弧長継続](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja)

補助実行例

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

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

[Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-bratu-continuation-jfnk/#bratu-fold-continuation) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-fold-continuation-en)

### Equations and problem definitions

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Crossing the Bratu fold with pseudo-arclength continuation

Supplementary execution example · Example definition or validation formula

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

### Exact and reference solutions

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

#### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-measurements)

Analytic reference · Reference for the same problem

u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)

Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

#### Crossing the Bratu fold with pseudo-arclength continuation

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en)

### Numerical methods

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

- [Weighted pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en)

Supplementary execution example

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
