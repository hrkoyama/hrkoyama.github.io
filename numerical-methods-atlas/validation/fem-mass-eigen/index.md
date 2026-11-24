# 整合質量FEM弦の一般化固有値

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)
- [SciPy LOBPCGによる一般化固有値比較](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja) (`lobpcg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-algorithm)

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

- [固定端弦の固有値と整合質量FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja) (`dirichlet-string-eigenproblem`)

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。


**問題の図**

![整合質量FEM弦の一般化固有値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-validation)

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

- [P1整合質量弦：閉離散固有値と連続体固有値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja) (`fem-mass-eigen`; 同じ問題の参照 · 解析参照)

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。
## 前提・単位・境界

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。

**編集上の補足**

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

## 採用した計算法

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

## 比較・検証

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

## 確認の限界

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_generalized_residual": 1.94948028233657e-10,
    "max_M_orthogonality_defect": 1.1102230246251565e-15,
    "max_relative_reference_error": 1.5843735459579712e-13,
    "max_operator_vector_actions": 30,
    "max_preconditioner_vector_actions": 24
  },
  "checks": {
    "fem-15-mass-Krylov/finite": true,
    "fem-15-mass-Krylov/original-generalized-residual": true,
    "fem-15-mass-Krylov/M-orthogonality": true,
    "fem-15-mass-Krylov/independent-dense-reference": true,
    "fem-15-mass-Krylov/exact-discrete-spectrum": true,
    "fem-15-mass-Krylov/fixed-action-budget": true,
    "fem-15-SciPy-LOBPCG/finite": true,
    "fem-15-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-15-SciPy-LOBPCG/M-orthogonality": true,
    "fem-15-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-15-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-15-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-31-mass-Krylov/finite": true,
    "fem-31-mass-Krylov/original-generalized-residual": true,
    "fem-31-mass-Krylov/M-orthogonality": true,
    "fem-31-mass-Krylov/independent-dense-reference": true,
    "fem-31-mass-Krylov/exact-discrete-spectrum": true,
    "fem-31-mass-Krylov/fixed-action-budget": true,
    "fem-31-SciPy-LOBPCG/finite": true,
    "fem-31-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-31-SciPy-LOBPCG/M-orthogonality": true,
    "fem-31-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-31-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-31-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-63-mass-Krylov/finite": true,
    "fem-63-mass-Krylov/original-generalized-residual": true,
    "fem-63-mass-Krylov/M-orthogonality": true,
    "fem-63-mass-Krylov/independent-dense-reference": true,
    "fem-63-mass-Krylov/exact-discrete-spectrum": true,
    "fem-63-mass-Krylov/fixed-action-budget": true,
    "fem-63-SciPy-LOBPCG/finite": true,
    "fem-63-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-63-SciPy-LOBPCG/M-orthogonality": true,
    "fem-63-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-63-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-63-SciPy-LOBPCG/fixed-action-budget": true,
    "continuum/second-order-ratio-1": true,
    "continuum/second-order-ratio-2": true,
    "continuum/finest-three-eigenvalues": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/index.json

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

内部63点で計算した、M正規化された最低3モード。

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

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.

- SciPy 1.14.1 LOBPCG API. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html; review_level=selected-official-documentation
Selected discussion of SPD B, preconditioner M, the history tuple, the 3k eigensolve, the 5k > n fallback and the rod example was read. This maintained-library comparison shares reduced LAPACK primitives; LOBPCG is not independently authored here.

- SciPy 1.14.1 LOBPCG adapter and initial B-orthonormalization. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py; review_level=selected-official-source
Selected _makeMatMat, _b_orthonormalize and API lines were read. The installed pinned file is bound separately. No full reading of the original LOBPCG paper or byte equality between wheel and Web source formatting is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Consistent-mass FEM string eigenpairs

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)
- [Generalized eigenpairs with SciPy LOBPCG](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en) (`lobpcg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-algorithm)

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

- [Fixed-end string eigenvalues and consistent-mass FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en) (`dirichlet-string-eigenproblem`)

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.


**Problem figure**

![Consistent-mass FEM string eigenpairs: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-validation)

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en) (`fem-mass-eigen`; Same-problem reference · Analytic reference)

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.
## Assumptions, units and boundaries

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.

**Editorial clarification**

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

## Adopted numerical method

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

## References and validation

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

## Limits

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_generalized_residual": 1.94948028233657e-10,
    "max_M_orthogonality_defect": 1.1102230246251565e-15,
    "max_relative_reference_error": 1.5843735459579712e-13,
    "max_operator_vector_actions": 30,
    "max_preconditioner_vector_actions": 24
  },
  "checks": {
    "fem-15-mass-Krylov/finite": true,
    "fem-15-mass-Krylov/original-generalized-residual": true,
    "fem-15-mass-Krylov/M-orthogonality": true,
    "fem-15-mass-Krylov/independent-dense-reference": true,
    "fem-15-mass-Krylov/exact-discrete-spectrum": true,
    "fem-15-mass-Krylov/fixed-action-budget": true,
    "fem-15-SciPy-LOBPCG/finite": true,
    "fem-15-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-15-SciPy-LOBPCG/M-orthogonality": true,
    "fem-15-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-15-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-15-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-31-mass-Krylov/finite": true,
    "fem-31-mass-Krylov/original-generalized-residual": true,
    "fem-31-mass-Krylov/M-orthogonality": true,
    "fem-31-mass-Krylov/independent-dense-reference": true,
    "fem-31-mass-Krylov/exact-discrete-spectrum": true,
    "fem-31-mass-Krylov/fixed-action-budget": true,
    "fem-31-SciPy-LOBPCG/finite": true,
    "fem-31-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-31-SciPy-LOBPCG/M-orthogonality": true,
    "fem-31-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-31-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-31-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-63-mass-Krylov/finite": true,
    "fem-63-mass-Krylov/original-generalized-residual": true,
    "fem-63-mass-Krylov/M-orthogonality": true,
    "fem-63-mass-Krylov/independent-dense-reference": true,
    "fem-63-mass-Krylov/exact-discrete-spectrum": true,
    "fem-63-mass-Krylov/fixed-action-budget": true,
    "fem-63-SciPy-LOBPCG/finite": true,
    "fem-63-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-63-SciPy-LOBPCG/M-orthogonality": true,
    "fem-63-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-63-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-63-SciPy-LOBPCG/fixed-action-budget": true,
    "continuum/second-order-ratio-1": true,
    "continuum/second-order-ratio-2": true,
    "continuum/finest-three-eigenvalues": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/index.json

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

The first three M-normalized modes computed on the 63-node interior grid.

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

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.

- SciPy 1.14.1 LOBPCG API. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html; review_level=selected-official-documentation
Selected discussion of SPD B, preconditioner M, the history tuple, the 3k eigensolve, the 5k > n fallback and the rod example was read. This maintained-library comparison shares reduced LAPACK primitives; LOBPCG is not independently authored here.

- SciPy 1.14.1 LOBPCG adapter and initial B-orthonormalization. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py; review_level=selected-official-source
Selected _makeMatMat, _b_orthonormalize and API lines were read. The installed pinned file is bound separately. No full reading of the original LOBPCG paper or byte equality between wheel and Web source formatting is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
