# 水素型原子の動径固有値問題 / Hydrogenic radial eigenproblems

https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/

## 日本語

[公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#hydrogenic) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#hydrogenic-atoms)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

#### 水素型原子：解析解と格子収束

共通実行例 · 問題の式

$$
\left[-\frac12\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{2r^2}-\frac Zr\right]u_{n\ell}=E_{n\ell}u_{n\ell}
$$

$$
E_n^{\rm ref}=-\frac{Z^2}{2n^2},\qquad Z\in\{1,2\}
$$

原子単位の1電子・定常動径問題。計算は有限半径箱の零Dirichlet境界を使い、無限領域の水素型解析解と比較する。一般多電子・分子・周期系の解法を意味しない。

### 厳密解・参照解

水素型原子の解析的な固有エネルギー・軌道と比較し、有限半径打切りと格子誤差を分けます。既存の固定入力・保存結果を参照します。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

#### [水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja)

解析解 · 同じ問題の参照

E_n=-Z^2/(2n^2) hartree; normalized hydrogenic radial functions on r>=0

非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

#### [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u;\quad \Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2};\quad \int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

#### 水素型原子：解析解と格子収束

E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。

- [E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n1-l0.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l0.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l1.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n3-l2.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n1-l0.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l0.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l1.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n3-l2.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja)

共通実行例

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。

非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。

[コード / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
python -m pytest -q
```

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

#### [code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_hydrogenic_refinement_and_normalization`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

作業フォルダ：quantum-atoms-2026-11-21/

```sh
python -m pytest -q test_atomic_radial.py -k test_hydrogenic_refinement_and_normalization
```

## English

[Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#hydrogenic-atoms-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

#### Hydrogenic atoms: analytic references and grid refinement

Common execution example · Problem definition

$$
\left[-\frac12\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{2r^2}-\frac Zr\right]u_{n\ell}=E_{n\ell}u_{n\ell}
$$

$$
E_n^{\rm ref}=-\frac{Z^2}{2n^2},\qquad Z\in\{1,2\}
$$

One-electron stationary radial problem in atomic units. A finite radial box with zero Dirichlet boundaries is compared with infinite-domain hydrogenic analytic references; not a general many-electron, molecular or periodic solver.

### Exact and reference solutions

Compare with analytic hydrogenic eigenenergies/orbitals and separate finite-radius truncation from mesh error using existing fixed inputs and stored results. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

#### [Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en)

Analytic reference · Reference for the same problem

E_n=-Z^2/(2n^2) hartree; normalized hydrogenic radial functions on r>=0

Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh.

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

#### [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-measurements)

Finite-grid numerical reference · Reference for the same problem

E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u;\quad \Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2};\quad \int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

#### Hydrogenic atoms: analytic references and grid refinement

E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.

- [E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n1-l0.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l0.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l1.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n3-l2.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n1-l0.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l0.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l1.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n3-l2.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en)

Common execution example

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.

Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh.

[Code / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
python -m pytest -q
```

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

#### [code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_hydrogenic_refinement_and_normalization`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Working directory: quantum-atoms-2026-11-21/

```sh
python -m pytest -q test_atomic_radial.py -k test_hydrogenic_refinement_and_normalization
```
