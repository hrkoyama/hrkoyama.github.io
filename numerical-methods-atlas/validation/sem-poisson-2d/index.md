# スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

**使用手法**

- [スペクトル要素法（SEM）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja) (`spectral-element`)
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-algorithm)

SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。


**問題の図**

![スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-validation)

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
## 前提・単位・境界

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

## 採用した計算法

SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

## 比較・検証

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

## 確認の限界

滑らかな固定問題だけの結果。要素・求積・代数ソルバーが異なるので、速度・計算量・汎用的優位性の比較ではありません。GLLの対角求積質量は一般の積の厳密な質量行列ではない。曲線格子・特異解・非圧縮流体・Nek5000/nekRS本体は未実行。

## 保存実測値と判定

```json
{
  "metrics": {
    "sem_h_l2_order": 3.0396439861149207,
    "sem_h_h1_order": 2.010636067947865,
    "p1_h_l2_order": 1.9744920294804964,
    "p1_h_h1_order": 0.9891011038360976,
    "p_refinement_l2_reduction": 311080.7699512155,
    "p6_l2_error": 3.7801651652951424e-07,
    "same_dof_free_unknowns": 225,
    "sem_finest_l2_error": 0.0002486410968007461,
    "p1_finest_l2_error": 0.005377435009938097,
    "same_dof_l2_ratio_sem_over_p1": 0.046237861794931924,
    "maximum_relative_residual": 3.1814596822002824e-12
  },
  "checks": {
    "sem_h_l2_convergence": true,
    "sem_h_h1_convergence": true,
    "p1_h_l2_convergence": true,
    "p1_h_h1_convergence": true,
    "p_refinement_monotone": true,
    "p_refinement_resolved": true,
    "equal_free_dofs": true,
    "same_dof_error_comparison": true,
    "linear_residuals": true,
    "zero_dirichlet_boundary": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/index.json

![保存した2D SEM場と節点誤差。連続誤差ノルムは別のGauss積分で評価しています。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d-preview.png)

保存した2D SEM場と節点誤差。連続誤差ノルムは別のGauss積分で評価しています。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

## 出典と確認範囲

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://nek5000.github.io/NekDoc/references.html; review_level=metadata
Nek5000公式参考文献の題名・巻・頁・DOIを照合。出版社の原文は未取得で、原報全体の監査・数値再現とはしない。今回の実装はLegendre GLL変種。

- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html; review_level=full-text
公式TheoryとFAQの要素局所の多項式、GLL/GL点・C0連続性を確認。教育用Poissonの実装とNek5000の流体ソルバー全体を同一視しない。

- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/; review_level=full-text
公式プロジェクトのSEM、nekRSのCPU/GPU対応、Nek5000との関係を確認。外部ソルバーの導入・実行・性能比較は未実施。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# 2D spectral-element Poisson: P1 FEM comparison and h/p refinement

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

**Methods used**

- [Spectral element method (SEM)](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en) (`spectral-element`)
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-algorithm)

C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.


**Problem figure**

![2D spectral-element Poisson: P1 FEM comparison and h/p refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-validation)

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
## Assumptions, units and boundaries

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

## Adopted numerical method

C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

## References and validation

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

## Limits

One smooth fixed problem only. Meshes, quadrature and algebraic solvers differ: no speed, complexity or universal-accuracy ranking. The diagonal GLL quadrature mass is not the exactly integrated mass of every product. No curved mesh, singular solution, incompressible flow or Nek5000/nekRS run.

## Stored measurements and decisions

```json
{
  "metrics": {
    "sem_h_l2_order": 3.0396439861149207,
    "sem_h_h1_order": 2.010636067947865,
    "p1_h_l2_order": 1.9744920294804964,
    "p1_h_h1_order": 0.9891011038360976,
    "p_refinement_l2_reduction": 311080.7699512155,
    "p6_l2_error": 3.7801651652951424e-07,
    "same_dof_free_unknowns": 225,
    "sem_finest_l2_error": 0.0002486410968007461,
    "p1_finest_l2_error": 0.005377435009938097,
    "same_dof_l2_ratio_sem_over_p1": 0.046237861794931924,
    "maximum_relative_residual": 3.1814596822002824e-12
  },
  "checks": {
    "sem_h_l2_convergence": true,
    "sem_h_h1_convergence": true,
    "p1_h_l2_convergence": true,
    "p1_h_h1_convergence": true,
    "p_refinement_monotone": true,
    "p_refinement_resolved": true,
    "equal_free_dofs": true,
    "same_dof_error_comparison": true,
    "linear_residuals": true,
    "zero_dirichlet_boundary": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/index.json

![Saved actual2D SEM field and nodal error. Continuous error norms use separate Gauss integration.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d-preview.png)

Saved actual2D SEM field and nodal error. Continuous error norms use separate Gauss integration.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

## Sources and review scope

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://nek5000.github.io/NekDoc/references.html; review_level=metadata
Bibliographic identity from the official Nek5000 reference list; publisher full text was not retrieved. No original-paper audit/reproduction. This example is a Legendre GLL variant.

- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html; review_level=full-text
Official Theory and FAQ: element-local polynomials, GLL/GL nodes and C0 continuity. No installation, execution or full-code audit of Nek5000.

- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/; review_level=full-text
Official project overview: SEM, CPU/GPU nekRS and its relationship to Nek5000. No external solver installation, execution or performance comparison.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
