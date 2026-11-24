# 擬似弧長継続でBratuのfoldを越える

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

**使用手法**

- [重み付き擬似弧長継続](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja) (`pseudo-arclength-continuation`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-algorithm)

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。


**問題の図**

![擬似弧長継続でBratuのfoldを越える：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-validation)

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja) (`bratu-fold-continuation`; 同じ問題の参照 · 解析参照)

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。
## 前提・単位・境界

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。

**編集上の補足**

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

## 採用した計算法

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

## 比較・検証

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

## 確認の限界

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "fold_orders": [
      2.0003257002223824,
      2.000081417263765
    ],
    "intended_failure_reason": "line search exhausted",
    "discrete_nonexistence_bound": 3.6300955492983498,
    "matching": "Fullpathfamilycoordinatefrommidpointisexplicit;separatefixedlambda2rootsvalidatebothbrancheswithoutparameterfitting.",
    "reference_qualification_max_ODE": 6e-78
  },
  "checks": {
    "N31/finite complete branch": true,
    "N31/discrete residual": true,
    "N31/unit tangent": true,
    "N31/tangent equation": true,
    "N31/tangent orientation": true,
    "N31/turning tangent": true,
    "N31/lower and upper lambda2 neighborhoods": true,
    "N31/fold discrete equation": true,
    "N31/fold null equation": true,
    "N31/fold null normalization": true,
    "N31/fold sigma_min": true,
    "N31/simple fold parameter transversality": true,
    "N31/simple fold quadratic transversality": true,
    "N31/lower discrete root": true,
    "N31/upper discrete root": true,
    "N31/ordered distinct branches": true,
    "N31/nonzero reference fields": true,
    "N63/finite complete branch": true,
    "N63/discrete residual": true,
    "N63/unit tangent": true,
    "N63/tangent equation": true,
    "N63/tangent orientation": true,
    "N63/turning tangent": true,
    "N63/lower and upper lambda2 neighborhoods": true,
    "N63/fold discrete equation": true,
    "N63/fold null equation": true,
    "N63/fold null normalization": true,
    "N63/fold sigma_min": true,
    "N63/simple fold parameter transversality": true,
    "N63/simple fold quadratic transversality": true,
    "N63/lower discrete root": true,
    "N63/upper discrete root": true,
    "N63/ordered distinct branches": true,
    "N63/nonzero reference fields": true,
    "N127/finite complete branch": true,
    "N127/discrete residual": true,
    "N127/unit tangent": true,
    "N127/tangent equation": true,
    "N127/tangent orientation": true,
    "N127/turning tangent": true,
    "N127/lower and upper lambda2 neighborhoods": true,
    "N127/fold discrete equation": true,
    "N127/fold null equation": true,
    "N127/fold null normalization": true,
    "N127/fold sigma_min": true,
    "N127/simple fold parameter transversality": true,
    "N127/simple fold quadratic transversality": true,
    "N127/lower discrete root": true,
    "N127/upper discrete root": true,
    "N127/ordered distinct branches": true,
    "N127/nonzero reference fields": true,
    "Decimal80 continuum ODE": true,
    "Decimal80 zero endpoints": true,
    "reference fixed lambda": true,
    "reference fold printed anchor": true,
    "no-solution lambda4 proof bound": true,
    "lambda4 Newton reports failure": true,
    "lambda4 finite retained states": true,
    "lambda4 remains above tolerance": true,
    "finest full path shape": true,
    "finest family curve lambda": true,
    "finest continuous fold error": true,
    "fold first refinement order": true,
    "fold second refinement order": true,
    "finest lower exact solution": true,
    "finest upper exact solution": true,
    "both branch errors refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/index.json

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。

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

- K.I.Dickson,C.T.Kelley,I.C.F.Ipsen,I.G.Kevrekidis (2007). Condition Estimates for Pseudo-Arclength Continuation. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=primary-selected-PDF-text
原著PDFの選択部分2.2節の接線・正規化・超平面制約と単純foldの範囲を読解。全文・全証明の監査ではありません。

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
著者教材のBratu解析族と二枝・丸めた臨界値を確認。変数は採用thetaの2倍で、別導出とDecimal80で資格。1914原著は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Crossing the Bratu fold with pseudo-arclength continuation

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

**Methods used**

- [Weighted pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en) (`pseudo-arclength-continuation`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-algorithm)

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.


**Problem figure**

![Crossing the Bratu fold with pseudo-arclength continuation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-validation)

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en) (`bratu-fold-continuation`; Same-problem reference · Analytic reference)

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.
## Assumptions, units and boundaries

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.

**Editorial clarification**

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

## Adopted numerical method

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

## References and validation

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

## Limits

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "fold_orders": [
      2.0003257002223824,
      2.000081417263765
    ],
    "intended_failure_reason": "line search exhausted",
    "discrete_nonexistence_bound": 3.6300955492983498,
    "matching": "Fullpathfamilycoordinatefrommidpointisexplicit;separatefixedlambda2rootsvalidatebothbrancheswithoutparameterfitting.",
    "reference_qualification_max_ODE": 6e-78
  },
  "checks": {
    "N31/finite complete branch": true,
    "N31/discrete residual": true,
    "N31/unit tangent": true,
    "N31/tangent equation": true,
    "N31/tangent orientation": true,
    "N31/turning tangent": true,
    "N31/lower and upper lambda2 neighborhoods": true,
    "N31/fold discrete equation": true,
    "N31/fold null equation": true,
    "N31/fold null normalization": true,
    "N31/fold sigma_min": true,
    "N31/simple fold parameter transversality": true,
    "N31/simple fold quadratic transversality": true,
    "N31/lower discrete root": true,
    "N31/upper discrete root": true,
    "N31/ordered distinct branches": true,
    "N31/nonzero reference fields": true,
    "N63/finite complete branch": true,
    "N63/discrete residual": true,
    "N63/unit tangent": true,
    "N63/tangent equation": true,
    "N63/tangent orientation": true,
    "N63/turning tangent": true,
    "N63/lower and upper lambda2 neighborhoods": true,
    "N63/fold discrete equation": true,
    "N63/fold null equation": true,
    "N63/fold null normalization": true,
    "N63/fold sigma_min": true,
    "N63/simple fold parameter transversality": true,
    "N63/simple fold quadratic transversality": true,
    "N63/lower discrete root": true,
    "N63/upper discrete root": true,
    "N63/ordered distinct branches": true,
    "N63/nonzero reference fields": true,
    "N127/finite complete branch": true,
    "N127/discrete residual": true,
    "N127/unit tangent": true,
    "N127/tangent equation": true,
    "N127/tangent orientation": true,
    "N127/turning tangent": true,
    "N127/lower and upper lambda2 neighborhoods": true,
    "N127/fold discrete equation": true,
    "N127/fold null equation": true,
    "N127/fold null normalization": true,
    "N127/fold sigma_min": true,
    "N127/simple fold parameter transversality": true,
    "N127/simple fold quadratic transversality": true,
    "N127/lower discrete root": true,
    "N127/upper discrete root": true,
    "N127/ordered distinct branches": true,
    "N127/nonzero reference fields": true,
    "Decimal80 continuum ODE": true,
    "Decimal80 zero endpoints": true,
    "reference fixed lambda": true,
    "reference fold printed anchor": true,
    "no-solution lambda4 proof bound": true,
    "lambda4 Newton reports failure": true,
    "lambda4 finite retained states": true,
    "lambda4 remains above tolerance": true,
    "finest full path shape": true,
    "finest family curve lambda": true,
    "finest continuous fold error": true,
    "fold first refinement order": true,
    "fold second refinement order": true,
    "finest lower exact solution": true,
    "finest upper exact solution": true,
    "both branch errors refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/index.json

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.

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

- K.I.Dickson,C.T.Kelley,I.C.F.Ipsen,I.G.Kevrekidis (2007). Condition Estimates for Pseudo-Arclength Continuation. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=primary-selected-PDF-text
Read selected original sec2.2 tangent,normalization,hyperplane andsimple-fold scope; nofullproof audit.

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
Read author exercise exactfamily/twobranches/roundedcritical; itsparameter istwiceourtheta. Independentderivation/Decimal80qualification;1914originalunread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
