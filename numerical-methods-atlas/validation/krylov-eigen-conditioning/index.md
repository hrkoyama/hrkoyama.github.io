# Krylov固有値：クラスター部分空間と非正規感度

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-algorithm)

全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Krylov固有値：クラスター部分空間と非正規感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-validation)

解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

対称行列の上位2固有値の間隔は1/.1/.01です。非正規行列は実浮動小数点の上三角行列でK=10/1000とし、対角が既知固有値です。浮動小数点の相似変換後に名目スペクトルを厳密真値とは呼びません。

**編集上の補足**

固有対残差、固有値・不変部分空間の誤差、スペクトルの間隔と非正規性を区別します。構成した感度対照を実際のKrylov反復の出力や万能な失敗例と同一視しません。

## 採用した計算法

全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

## 比較・検証

解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。

## 確認の限界

NumPyの射影コアとSciPyの密参照はLAPACK基盤を共有し得るため、全面的に独立なバックエンドとはしません。解析固有値と独立構成対照を併用します。再始動、内部固有値、大規模疎行列、普遍的な単調収束は対象外です。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_basis_orthogonality": 6.813979303412138e-16,
    "largest_eigenvalue_condition": 100000.00000500213,
    "constructed_small_residual": 2.4999999999688053e-08,
    "constructed_forward_error": 0.004999999999999893
  },
  "checks": {
    "gap1-analytic-spectrum": true,
    "gap1-resolved": true,
    "gap1-basis": true,
    "gap0.1-analytic-spectrum": true,
    "gap0.1-resolved": true,
    "gap0.1-basis": true,
    "gap0.01-analytic-spectrum": true,
    "gap0.01-resolved": true,
    "gap0.01-basis": true,
    "K10-condition": true,
    "K10-analytic-spectrum": true,
    "K10-resolved": true,
    "K10-basis": true,
    "K1000-condition": true,
    "K1000-analytic-spectrum": true,
    "K1000-resolved": true,
    "K1000-basis": true,
    "pseudoK1-literal-formula": true,
    "pseudoK10-literal-formula": true,
    "pseudoK1000-literal-formula": true,
    "small-residual-does-not-certify-forward-error": true,
    "short-dimension-has-residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html; review_level=official implementation documentation, error-bound overview and cluster/invariant-subspace distinction
非正規行列では小さな固有対残差と前進固有値誤差を同一視しません。固有値感度、個別固有ベクトル、固有値クラスターの不変部分空間を区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Krylov eigenvalues: cluster subspaces and nonnormal sensitivity

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-algorithm)

Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-validation)

Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Top symmetric gaps are1/.1/.01. Nonnormal matrices are actual floating-point upper-triangular inputs with K=10/1000 and known diagonal eigenvalues. Nominal spectra after floating-point similarity construction are not labelled exact truth.

**Editorial clarification**

Separate eigenpair residuals, eigenvalue/invariant-subspace errors, spectral gaps and nonnormality. A constructed sensitivity control is distinct from actual Krylov iteration output or a universal failure example.

## Adopted numerical method

Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

## References and validation

Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.

## Limits

NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_basis_orthogonality": 6.813979303412138e-16,
    "largest_eigenvalue_condition": 100000.00000500213,
    "constructed_small_residual": 2.4999999999688053e-08,
    "constructed_forward_error": 0.004999999999999893
  },
  "checks": {
    "gap1-analytic-spectrum": true,
    "gap1-resolved": true,
    "gap1-basis": true,
    "gap0.1-analytic-spectrum": true,
    "gap0.1-resolved": true,
    "gap0.1-basis": true,
    "gap0.01-analytic-spectrum": true,
    "gap0.01-resolved": true,
    "gap0.01-basis": true,
    "K10-condition": true,
    "K10-analytic-spectrum": true,
    "K10-resolved": true,
    "K10-basis": true,
    "K1000-condition": true,
    "K1000-analytic-spectrum": true,
    "K1000-resolved": true,
    "K1000-basis": true,
    "pseudoK1-literal-formula": true,
    "pseudoK10-literal-formula": true,
    "pseudoK1000-literal-formula": true,
    "small-residual-does-not-certify-forward-error": true,
    "short-dimension-has-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html; review_level=official implementation documentation, error-bound overview and cluster/invariant-subspace distinction
Do not equate a small eigenpair residual with small forward eigenvalue error for nonnormal matrices; distinguish eigenvalue sensitivity, individual vectors, and clustered invariant subspaces.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
