# Spectral element method (SEM) / スペクトル要素法（SEM）

Status: educational-example

Continuous Galerkin elements with high-order local polynomials and GLL quadrature. A small2D Poisson example compares h/p refinement with the existing P1 FEM; related implementations include Nek5000 and nekRS.

要素内の高次多項式とGLL求積を用いる連続Galerkin型の方法。2D Poissonのh/p収束と既存P1 FEMを軽量例で比較する。Nek5000・nekRSを関連実装として紹介。

One smooth fixed problem only. Meshes, quadrature and algebraic solvers differ: no speed, complexity or universal-accuracy ranking. The diagonal GLL quadrature mass is not the exactly integrated mass of every product. No curved mesh, singular solution, incompressible flow or Nek5000/nekRS run.

Other names: SEM, スペクトル要素, スペクトルエレメント法, spectral element, spectral-element method, spectral element method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spectral-element/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/spectral-element/



- Reference: https://nek5000.github.io/NekDoc/references.html — Bibliographic identity from the official Nek5000 reference list; publisher full text was not retrieved. No original-paper audit/reproduction. This example is a Legendre GLL variant.
- Reference: https://nek5000.github.io/NekDoc/theory.html — Official Theory and FAQ: element-local polynomials, GLL/GL nodes and C0 continuity. No installation, execution or full-code audit of Nek5000.
- Reference: https://nek5000.github.io/ — Official project overview: SEM, CPU/GPU nekRS and its relationship to Nek5000. No external solver installation, execution or performance comparison.

## Small fixed-input validation supplements

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

- 2D spectral-element Poisson: P1 FEM comparison and h/p refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json

Common execution records: [{"id": "sem-poisson-2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-sine)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) (`poisson-2d-sine`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照; 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[既存の参照図](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spectral-element/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較 (`sem-poisson-2d`)

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)
- [/code/validated-examples/2026-11-23/sem-fr/fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-sine)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) (`poisson-2d-sine`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference; Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Existing reference profile](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/spectral-element/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 2D spectral-element Poisson: P1 FEM comparison and h/p refinement (`sem-poisson-2d`)

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

###### Related source

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)
- [/code/validated-examples/2026-11-23/sem-fr/fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py)

###### Package tests

- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
