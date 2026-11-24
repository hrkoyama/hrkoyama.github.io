# 整合質量FEM弦の一般化固有値 / Consistent-mass FEM string eigenpairs

https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/

## 日本語

[内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#fem-mass-eigen) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#fem-mass-eigen)

### 方程式・問題の定義

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。

#### [固定端弦の固有値と整合質量FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja)

$$
-T\phi^{\prime\prime}=\rho\lambda\phi,\quad 0<x<1
$$

$$
\phi(0)=\phi(1)=0,\quad T=\rho=1
$$

$$
\lambda_j=(j\pi)^2
$$

$$
\lambda_{j,h}=\frac{6(1-\cos\theta_j)}{h^2(2+\cos\theta_j)},\quad\theta_j=\frac{j\pi}{n+1}
$$

単位弦の定常振動形の固有値問題です。整合質量P1の代数固有値誤差と連続体への離散化誤差を分けます。時間発展を実行した例ではありません。

#### 整合質量FEM弦の一般化固有値

補助実行例 · 実行例の定義・検証式

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

### 厳密解・参照解

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

#### [P1整合質量弦：閉離散固有値と連続体固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-measurements)

解析解 · 同じ問題の参照

Kx=lambda_h Mx; lambda_j,h=6*(1-cos(theta_j))/(h^2*(2+cos(theta_j))),theta_j=j*pi/(n+1); lambda_j=(j*pi)^2,phi_j(x)=sin(j*pi*x)

長さ・張力・密度1、両端Dirichlet0、内部15/31/63点、最低3固有対。閉離散固有値とgeneralized dense LAPACKを比較し、連続(jπ)²への誤差を別に調べます。表示ベクトルは保存した数値解で、符号は任意です。

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

#### 整合質量FEM弦の一般化固有値

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja)

### 計算法

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SciPy LOBPCGによる一般化固有値比較](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja)

補助実行例

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

## English

[The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#fem-mass-eigen) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#fem-mass-eigen-en)

### Equations and problem definitions

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.

#### [Fixed-end string eigenvalues and consistent-mass FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en)

$$
-T\phi^{\prime\prime}=\rho\lambda\phi,\quad 0<x<1
$$

$$
\phi(0)=\phi(1)=0,\quad T=\rho=1
$$

$$
\lambda_j=(j\pi)^2
$$

$$
\lambda_{j,h}=\frac{6(1-\cos\theta_j)}{h^2(2+\cos\theta_j)},\quad\theta_j=\frac{j\pi}{n+1}
$$

A unit-string normal-mode eigenproblem separates consistent-mass P1 algebraic error from continuum discretization error. No time evolution is performed.

#### Consistent-mass FEM string eigenpairs

Supplementary execution example · Example definition or validation formula

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

### Exact and reference solutions

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

#### [Consistent-mass P1 string: closed discrete and continuum eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-measurements)

Analytic reference · Reference for the same problem

Kx=lambda_h Mx; lambda_j,h=6*(1-cos(theta_j))/(h^2*(2+cos(theta_j))),theta_j=j*pi/(n+1); lambda_j=(j*pi)^2,phi_j(x)=sin(j*pi*x)

Unit length, tension and density, homogeneous Dirichlet endpoints, 15/31/63 interior nodes, and the lowest three eigenpairs. Compare closed discrete eigenvalues with generalized dense LAPACK, then measure error relative to (j*pi)^2 separately. Displayed vectors are saved numerical modes with arbitrary sign.

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

#### Consistent-mass FEM string eigenpairs

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en)

### Numerical methods

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Generalized eigenpairs with SciPy LOBPCG](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en)

Supplementary execution example

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
