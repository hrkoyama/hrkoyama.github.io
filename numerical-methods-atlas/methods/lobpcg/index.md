# Generalized eigenpairs with SciPy LOBPCG / SciPy LOBPCGによる一般化固有値比較

Status: educational-example

Actual SciPy 1.14.1 LOBPCG computes the lowest three consistent-mass P1 string modes, compared with an original M-inner-product Krylov method, generalized LAPACK and closed discrete spectra.

整合質量P1弦の最低3モードを実SciPy1.14.1 LOBPCGで解き、自作M内積Krylov・一般化LAPACK・独立離散スペクトルと比較します。

LOBPCG is implemented by SciPy, not authored here. This example covers a small 1D string; it does not expose unreturned internal histories or guarantee general clustered-spectrum or performance behavior.

Other names: 局所最適ブロック前処理共役勾配法, Locally Optimal Block Preconditioned Conjugate Gradient

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/



- Reference: https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html — Selected discussion of SPD B, LinearOperator, preconditioner M, histories, the 5k > n fallback and the rod example was read. This is an actual library comparison; the full Knyazev 2001 paper was not newly read.
- Reference: https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py — Selected adapter and initial B-orthonormalization exception handling was read. The component binds the hash of the actual installed source.

## Small fixed-input validation supplements

Actual SciPy 1.14.1 LOBPCG computes the lowest three consistent-mass P1 string modes, compared with an original M-inner-product Krylov method, generalized LAPACK and closed discrete spectra.

整合質量P1弦の最低3モードを実SciPy1.14.1 LOBPCGで解き、自作M内積Krylov・一般化LAPACK・独立離散スペクトルと比較します。

- Consistent-mass FEM string eigenpairs: https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json

Common execution records: [{"id": "fem-mass-eigen", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [固定端弦の固有値と整合質量FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja) (`dirichlet-string-eigenproblem`; fem-mass-eigen)

#### 問題の図 (`method-problems-ja`)

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

- [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。


#### 厳密解・参照解 (`method-references-ja`)

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#references-ja) (`fem-mass-eigen`)

- [P1整合質量弦：閉離散固有値と連続体固有値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja) (`fem-mass-eigen`; 同じ問題の参照; 解析参照)

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

[既存の参照図](/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 整合質量FEM弦の一般化固有値 (`fem-mass-eigen`)

[整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

整合質量P1弦の最低3モードを実SciPy1.14.1 LOBPCGで解き、自作M内積Krylov・一般化LAPACK・独立離散スペクトルと比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Fixed-end string eigenvalues and consistent-mass FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en) (`dirichlet-string-eigenproblem`; fem-mass-eigen)

#### Problem figures (`method-problems-en`)

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

- [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) (`fem-mass-eigen`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.


#### Exact / reference solutions (`method-references-en`)

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#references-en) (`fem-mass-eigen`)

- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en) (`fem-mass-eigen`; Same-problem reference; Analytic reference)

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

[Existing reference profile](/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Consistent-mass FEM string eigenpairs (`fem-mass-eigen`)

[Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Actual SciPy 1.14.1 LOBPCG computes the lowest three consistent-mass P1 string modes, compared with an original M-inner-product Krylov method, generalized LAPACK and closed discrete spectra.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### Package tests

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
