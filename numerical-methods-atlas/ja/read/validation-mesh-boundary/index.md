# 角特異性・曲線座標・Neumann／Robin境界

L字特異解のP1 FEM、環状領域の可変粘性ベクトルQ1 PDE、純Neumannの互換条件・平均ゲージ、混合Robinの製造解を実際に解きます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## L字領域P1特異解：graded格子と歪みの分離

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
### 前提・単位・境界

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。

**編集上の補足**

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

### 採用した計算法

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

### 比較・検証

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

### 確認の限界

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Long Chen (n.d.). Introduction to Adaptive Finite Element Methods. https://lyc102.github.io/ifem/afem/; review_level=selected-official-tutorial-equations
Author documentation: L-shaped harmonic r^(2/3)sin(2theta/3) field and non-quasiuniform refinement motivation inspected. No MATLAB code copied or run; our removed quadrant/angle convention is explicitly defined.

- Joachim Schöberl (n.d.). Interactive FEM: graded meshes around vertex singularities. https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html; review_level=selected-author-teaching-section
Section24.4 weighted regularity and graded meshes inspected. Our fixed max-norm radial map is independently constructed; no general AMR implementation or universal optimality theorem claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 環状領域の可変粘性・真2DベクトルMMS

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。

**使用手法**

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) (`q1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-algorithm)

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [可変粘性のベクトル応力境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja) (`variable-viscosity-vector`)

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。


**問題の図**

![環状領域の可変粘性・真2DベクトルMMS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-validation)

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

- [環状粘性ベクトルMMS：独立応力微分で外力を確認](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja) (`annular-viscous-mms`; 同じ問題の参照 · 製造解)

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。
### 前提・単位・境界

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。

**編集上の補足**

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

### 採用した計算法

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

### 比較・検証

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

### 確認の限界

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 32,
    "theta_cells": 64,
    "dofs": 3968,
    "relative_l2": 0.0022683900910951296,
    "relative_strain_l2": 0.05188955686190023,
    "relative_traction_l2": 0.07266006943162176,
    "residual": 1.0857981180834031e-13,
    "boundary_error": 0.0,
    "area_error": 3.552713678800501e-15,
    "reaction_balance": 1.736671818881876e-15,
    "traction_flux_balance": 0.042495559851796386,
    "exact_flux_balance": 5.984756355647655e-16,
    "analytic_force_error": 8.394500285269018e-16,
    "work_identity": 3.851517252670248e-15,
    "symmetry": 3.552713678800501e-15
  },
  "checks": {
    "annulus-n8 residual": true,
    "annulus-n8 boundary_error": true,
    "annulus-n8 area_error": true,
    "annulus-n8 reaction_balance": true,
    "annulus-n8 exact_flux_balance": true,
    "annulus-n8 analytic_force_error": true,
    "annulus-n8 work_identity": true,
    "annulus-n8 symmetry": true,
    "annulus-n16 residual": true,
    "annulus-n16 boundary_error": true,
    "annulus-n16 area_error": true,
    "annulus-n16 reaction_balance": true,
    "annulus-n16 exact_flux_balance": true,
    "annulus-n16 analytic_force_error": true,
    "annulus-n16 work_identity": true,
    "annulus-n16 symmetry": true,
    "annulus-n32 residual": true,
    "annulus-n32 boundary_error": true,
    "annulus-n32 area_error": true,
    "annulus-n32 reaction_balance": true,
    "annulus-n32 exact_flux_balance": true,
    "annulus-n32 analytic_force_error": true,
    "annulus-n32 work_identity": true,
    "annulus-n32 symmetry": true,
    "relative_l2 refinement 1": true,
    "relative_l2 refinement 2": true,
    "relative_strain_l2 refinement 1": true,
    "relative_strain_l2 refinement 2": true,
    "relative_traction_l2 refinement 1": true,
    "relative_traction_l2 refinement 2": true,
    "traction_flux_balance refinement 1": true,
    "traction_flux_balance refinement 2": true,
    "finest relative_l2": true,
    "finest relative_strain_l2": true,
    "finest relative_traction_l2": true,
    "finest traction_flux_balance": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

### 取得・実行

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

### 出典と確認範囲

- MFEM developers (n.d.). Example2: Linear Elasticity. https://mfem.org/examples/; review_level=selected-official-equations
Example2 stress sigma=lambda div(u)I+mu(grad(u)+grad(u)^T), weak formulation and traction conventions inspected. Use lambda0 as a linear vector viscous BVP; manufactured fields are derived here. MFEM not executed or copied.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 純Neumannの互換条件と平均値ゲージ

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-algorithm)

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。


**問題の図**

![純Neumannの互換条件と平均値ゲージ：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-validation)

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

- [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja) (`poisson-neumann`; 同じ問題の参照 · 製造解)

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。
### 前提・単位・境界

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。

**編集上の補足**

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

### 採用した計算法

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

### 比較・検証

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

### 確認の限界

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.0004017888396835558,
    "linf": 0.0008016429562934801,
    "residual": 1.6410484082740595e-15,
    "compatibility": 1.474514954580286e-17,
    "mean_error": 7.160477722908953e-17,
    "nullspace_defect": 0.0,
    "solver_gap": 1.0436096431476471e-14,
    "lagrange_multiplier": -2.2436555307051445e-15,
    "boundary_residual": 0.0,
    "boundary_flux_error": 0.0,
    "flux_balance": 1.474514954580286e-17,
    "symmetry": 0.0,
    "gauge_shift_error": 3.774758283725532e-15
  },
  "checks": {
    "neumann-n16 residual": true,
    "neumann-n16 boundary_residual": true,
    "neumann-n16 flux_balance": true,
    "neumann-n16 symmetry": true,
    "neumann-n16 compatibility": true,
    "neumann-n16 mean_error": true,
    "neumann-n16 nullspace_defect": true,
    "neumann-n16 solver_gap": true,
    "neumann-n32 residual": true,
    "neumann-n32 boundary_residual": true,
    "neumann-n32 flux_balance": true,
    "neumann-n32 symmetry": true,
    "neumann-n32 compatibility": true,
    "neumann-n32 mean_error": true,
    "neumann-n32 nullspace_defect": true,
    "neumann-n32 solver_gap": true,
    "neumann-n64 residual": true,
    "neumann-n64 boundary_residual": true,
    "neumann-n64 flux_balance": true,
    "neumann-n64 symmetry": true,
    "neumann-n64 compatibility": true,
    "neumann-n64 mean_error": true,
    "neumann-n64 nullspace_defect": true,
    "neumann-n64 solver_gap": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "mean gauge shifts only constant": true,
    "incompatible source rejected without projection": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

### 取得・実行

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

### 出典と確認範囲

- PETSc developers (n.d.). KSP: Solving Singular Systems. https://petsc.org/main/manual/ksp/; review_level=selected-official-section
Solving Singular Systems: constant Neumann nullspace and RHS compatibility inspected. We reject physical incompatibility rather than projecting it away. PETSc is neither a dependency nor executed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2D混合Robinの製造解と境界流束

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-algorithm)

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。


**問題の図**

![2D混合Robinの製造解と境界流束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-validation)

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

- [混合Robin：2次元解析場と独立な法線流束](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja) (`poisson-robin`; 同じ問題の参照 · 製造解)

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。
### 前提・単位・境界

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。

**編集上の補足**

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

### 採用した計算法

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

### 比較・検証

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

### 確認の限界

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.00037706113250587296,
    "linf": 0.0008911573863470412,
    "residual": 5.729791641151394e-15,
    "compatibility": 3.9384615384615382,
    "mean_error": 0.0,
    "nullspace_defect": 0.0,
    "solver_gap": 0.0,
    "lagrange_multiplier": 0.0,
    "boundary_residual": 4.440892098500626e-16,
    "boundary_flux_error": 0.0006164157489298994,
    "flux_balance": 1.6335890973273592e-13,
    "symmetry": 0.0
  },
  "checks": {
    "robin-n16 residual": true,
    "robin-n16 boundary_residual": true,
    "robin-n16 flux_balance": true,
    "robin-n16 symmetry": true,
    "robin-n32 residual": true,
    "robin-n32 boundary_residual": true,
    "robin-n32 flux_balance": true,
    "robin-n32 symmetry": true,
    "robin-n64 residual": true,
    "robin-n64 boundary_residual": true,
    "robin-n64 flux_balance": true,
    "robin-n64 symmetry": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "boundary flux refinement 1": true,
    "boundary flux refinement 2": true,
    "finest boundary flux": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

### 取得・実行

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

### 出典と確認範囲

- MFEM developers (n.d.). Boundary Conditions: Robin boundary conditions. https://mfem.org/fem_bc/; review_level=selected-official-equations
Outward normal derivative and Robin weak boundary contribution inspected; Example27 source overview inspected. Our cell-centred face elimination/MMS is separately derived; no MFEM execution.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
