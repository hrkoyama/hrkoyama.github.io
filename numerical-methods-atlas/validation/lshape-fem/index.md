# L字領域P1特異解：graded格子と歪みの分離

再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。

**使用手法**

- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-algorithm)

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。


**問題の図**

![L字領域P1特異解：graded格子と歪みの分離：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) (`lshape-fem`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-validation)

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

- [L字角の特異解：調和場と別の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja) (`lshape-fem`; 同じ問題の参照 · 解析参照)

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。
## 前提・単位・境界

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。

**編集上の補足**

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

## 採用した計算法

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

## 比較・検証

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

## 確認の限界

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 32,
    "dofs": 961,
    "l2": 0.00134735733393484,
    "h1": 0.10884489368256302,
    "quadrature_relative_gap": 1.40015698331148e-14,
    "minimum_area": 0.00047869957157375606,
    "minimum_angle_degrees": 43.597518748367705,
    "maximum_aspect": 2.084333006036921,
    "condition_one_norm_estimate": 627.0284248525954,
    "residual": 1.6514567491299204e-15,
    "boundary_error": 0.0,
    "symmetry": 0.0
  },
  "checks": {
    "uniform-n8 residual": true,
    "uniform-n8 boundary_error": true,
    "uniform-n8 symmetry": true,
    "uniform-n8 quadrature_relative_gap": true,
    "uniform-n8 positive geometry": true,
    "uniform-n16 residual": true,
    "uniform-n16 boundary_error": true,
    "uniform-n16 symmetry": true,
    "uniform-n16 quadrature_relative_gap": true,
    "uniform-n16 positive geometry": true,
    "uniform-n32 residual": true,
    "uniform-n32 boundary_error": true,
    "uniform-n32 symmetry": true,
    "uniform-n32 quadrature_relative_gap": true,
    "uniform-n32 positive geometry": true,
    "graded-n8 residual": true,
    "graded-n8 boundary_error": true,
    "graded-n8 symmetry": true,
    "graded-n8 quadrature_relative_gap": true,
    "graded-n8 positive geometry": true,
    "graded-n16 residual": true,
    "graded-n16 boundary_error": true,
    "graded-n16 symmetry": true,
    "graded-n16 quadrature_relative_gap": true,
    "graded-n16 positive geometry": true,
    "graded-n32 residual": true,
    "graded-n32 boundary_error": true,
    "graded-n32 symmetry": true,
    "graded-n32 quadrature_relative_gap": true,
    "graded-n32 positive geometry": true,
    "square-n8 residual": true,
    "square-n8 boundary_error": true,
    "square-n8 symmetry": true,
    "square-n8 quadrature_relative_gap": true,
    "square-n8 positive geometry": true,
    "square-n16 residual": true,
    "square-n16 boundary_error": true,
    "square-n16 symmetry": true,
    "square-n16 quadrature_relative_gap": true,
    "square-n16 positive geometry": true,
    "square-n32 residual": true,
    "square-n32 boundary_error": true,
    "square-n32 symmetry": true,
    "square-n32 quadrature_relative_gap": true,
    "square-n32 positive geometry": true,
    "warped-n8 residual": true,
    "warped-n8 boundary_error": true,
    "warped-n8 symmetry": true,
    "warped-n8 quadrature_relative_gap": true,
    "warped-n8 positive geometry": true,
    "warped-n16 residual": true,
    "warped-n16 boundary_error": true,
    "warped-n16 symmetry": true,
    "warped-n16 quadrature_relative_gap": true,
    "warped-n16 positive geometry": true,
    "warped-n32 residual": true,
    "warped-n32 boundary_error": true,
    "warped-n32 symmetry": true,
    "warped-n32 quadrature_relative_gap": true,
    "warped-n32 positive geometry": true,
    "uniform l2 refinement 1": true,
    "uniform l2 refinement 2": true,
    "uniform h1 refinement 1": true,
    "uniform h1 refinement 2": true,
    "graded l2 refinement 1": true,
    "graded l2 refinement 2": true,
    "graded h1 refinement 1": true,
    "graded h1 refinement 2": true,
    "square l2 refinement 1": true,
    "square l2 refinement 2": true,
    "square h1 refinement 1": true,
    "square h1 refinement 2": true,
    "warped l2 refinement 1": true,
    "warped l2 refinement 2": true,
    "warped h1 refinement 1": true,
    "warped h1 refinement 2": true,
    "matched unknown counts": true,
    "finest graded/uniform H1": true,
    "finest graded H1": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## 出典と確認範囲

- Long Chen (n.d.). Introduction to Adaptive Finite Element Methods. https://lyc102.github.io/ifem/afem/; review_level=selected-official-tutorial-equations
Author documentation: L-shaped harmonic r^(2/3)sin(2theta/3) field and non-quasiuniform refinement motivation inspected. No MATLAB code copied or run; our removed quadrant/angle convention is explicitly defined.

- Joachim Schöberl (n.d.). Interactive FEM: graded meshes around vertex singularities. https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html; review_level=selected-author-teaching-section
Section24.4 weighted regularity and graded meshes inspected. Our fixed max-norm radial map is independently constructed; no general AMR implementation or universal optimality theorem claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# L-corner P1 FEM: grading and separate mesh distortion

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.

**Methods used**

- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-algorithm)

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.


**Problem figure**

![L-corner P1 FEM: grading and separate mesh distortion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-validation)

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

- [L-corner singularity: harmonic field and separate smooth MMS](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en) (`lshape-fem`; Same-problem reference · Analytic reference)

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
## Assumptions, units and boundaries

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.

**Editorial clarification**

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

## Adopted numerical method

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

## References and validation

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

## Limits

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 32,
    "dofs": 961,
    "l2": 0.00134735733393484,
    "h1": 0.10884489368256302,
    "quadrature_relative_gap": 1.40015698331148e-14,
    "minimum_area": 0.00047869957157375606,
    "minimum_angle_degrees": 43.597518748367705,
    "maximum_aspect": 2.084333006036921,
    "condition_one_norm_estimate": 627.0284248525954,
    "residual": 1.6514567491299204e-15,
    "boundary_error": 0.0,
    "symmetry": 0.0
  },
  "checks": {
    "uniform-n8 residual": true,
    "uniform-n8 boundary_error": true,
    "uniform-n8 symmetry": true,
    "uniform-n8 quadrature_relative_gap": true,
    "uniform-n8 positive geometry": true,
    "uniform-n16 residual": true,
    "uniform-n16 boundary_error": true,
    "uniform-n16 symmetry": true,
    "uniform-n16 quadrature_relative_gap": true,
    "uniform-n16 positive geometry": true,
    "uniform-n32 residual": true,
    "uniform-n32 boundary_error": true,
    "uniform-n32 symmetry": true,
    "uniform-n32 quadrature_relative_gap": true,
    "uniform-n32 positive geometry": true,
    "graded-n8 residual": true,
    "graded-n8 boundary_error": true,
    "graded-n8 symmetry": true,
    "graded-n8 quadrature_relative_gap": true,
    "graded-n8 positive geometry": true,
    "graded-n16 residual": true,
    "graded-n16 boundary_error": true,
    "graded-n16 symmetry": true,
    "graded-n16 quadrature_relative_gap": true,
    "graded-n16 positive geometry": true,
    "graded-n32 residual": true,
    "graded-n32 boundary_error": true,
    "graded-n32 symmetry": true,
    "graded-n32 quadrature_relative_gap": true,
    "graded-n32 positive geometry": true,
    "square-n8 residual": true,
    "square-n8 boundary_error": true,
    "square-n8 symmetry": true,
    "square-n8 quadrature_relative_gap": true,
    "square-n8 positive geometry": true,
    "square-n16 residual": true,
    "square-n16 boundary_error": true,
    "square-n16 symmetry": true,
    "square-n16 quadrature_relative_gap": true,
    "square-n16 positive geometry": true,
    "square-n32 residual": true,
    "square-n32 boundary_error": true,
    "square-n32 symmetry": true,
    "square-n32 quadrature_relative_gap": true,
    "square-n32 positive geometry": true,
    "warped-n8 residual": true,
    "warped-n8 boundary_error": true,
    "warped-n8 symmetry": true,
    "warped-n8 quadrature_relative_gap": true,
    "warped-n8 positive geometry": true,
    "warped-n16 residual": true,
    "warped-n16 boundary_error": true,
    "warped-n16 symmetry": true,
    "warped-n16 quadrature_relative_gap": true,
    "warped-n16 positive geometry": true,
    "warped-n32 residual": true,
    "warped-n32 boundary_error": true,
    "warped-n32 symmetry": true,
    "warped-n32 quadrature_relative_gap": true,
    "warped-n32 positive geometry": true,
    "uniform l2 refinement 1": true,
    "uniform l2 refinement 2": true,
    "uniform h1 refinement 1": true,
    "uniform h1 refinement 2": true,
    "graded l2 refinement 1": true,
    "graded l2 refinement 2": true,
    "graded h1 refinement 1": true,
    "graded h1 refinement 2": true,
    "square l2 refinement 1": true,
    "square l2 refinement 2": true,
    "square h1 refinement 1": true,
    "square h1 refinement 2": true,
    "warped l2 refinement 1": true,
    "warped l2 refinement 2": true,
    "warped h1 refinement 1": true,
    "warped h1 refinement 2": true,
    "matched unknown counts": true,
    "finest graded/uniform H1": true,
    "finest graded H1": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## Sources and review scope

- Long Chen (n.d.). Introduction to Adaptive Finite Element Methods. https://lyc102.github.io/ifem/afem/; review_level=selected-official-tutorial-equations
Author documentation: L-shaped harmonic r^(2/3)sin(2theta/3) field and non-quasiuniform refinement motivation inspected. No MATLAB code copied or run; our removed quadrant/angle convention is explicitly defined.

- Joachim Schöberl (n.d.). Interactive FEM: graded meshes around vertex singularities. https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html; review_level=selected-author-teaching-section
Section24.4 weighted regularity and graded meshes inspected. Our fixed max-norm radial map is independently constructed; no general AMR implementation or universal optimality theorem claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
