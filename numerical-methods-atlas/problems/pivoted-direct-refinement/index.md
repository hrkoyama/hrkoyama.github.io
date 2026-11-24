# 部分ピボットLU・Choleskyと反復改良 / Pivoted LU, Cholesky and iterative refinement

https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/

## 日本語

[保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#pivoted-direct-refinement) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#pivoted-direct-refinement)

### 方程式・問題の定義

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。

#### [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。

#### 部分ピボットLU・Choleskyと反復改良

補助実行例 · 実行例の定義・検証式

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。

### 厳密解・参照解

実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。

#### [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-measurements)

解析解 · 同じ問題の参照

x_ref=round_binary64(exact_Fraction_solve(A_binary64,b_binary64)); r=b-Ax; eta_inf=||r||inf/(||A||inf||x||inf+||b||inf)

固定4行列の実binary64 A,bをFractionへ厳密変換し、有理数消去の解を最後にbinary64へ変換。LAPACKは別比較であり共有数値基盤を含みます。任意の悪条件行列に対する前進精度保証ではありません。

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

#### 部分ピボットLU・Choleskyと反復改良

実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja)

### 計算法

手書き部分ピボットLU・下三角Cholesky・前後代入。

- [部分ピボットLUと混合精度反復改良](https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Cholesky分解と三角代入](https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja)

補助実行例

独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

## English

[The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#pivoted-direct-refinement) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#pivoted-direct-refinement-en)

### Equations and problem definitions

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.

#### [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.

#### Pivoted LU, Cholesky and iterative refinement

Supplementary execution example · Example definition or validation formula

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.

### Exact and reference solutions

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

#### [Pivoted LU and Cholesky: exact-rational references for actual binary input](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-measurements)

Analytic reference · Reference for the same problem

x_ref=round_binary64(exact_Fraction_solve(A_binary64,b_binary64)); r=b-Ax; eta_inf=||r||inf/(||A||inf||x||inf+||b||inf)

The four fixed matrices use the actual binary64 A and b, converted exactly to Fractions. Rational elimination is exact, followed by a final binary64 rounding. Separate LAPACK comparisons share some numerical infrastructure. This is not a forward-accuracy guarantee for arbitrary ill-conditioned matrices.

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

#### Pivoted LU, Cholesky and iterative refinement

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en)

### Numerical methods

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

- [Partial-pivot LU and mixed-precision refinement](https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Cholesky factorization and triangular solves](https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en)

Supplementary execution example

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
