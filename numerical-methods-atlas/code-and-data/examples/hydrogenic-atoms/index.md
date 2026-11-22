# Hydrogenic atoms: analytic references and grid refinement / 水素型原子：解析解と格子収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: hydrogenic-atoms

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

Z=1,2の指定された束縛状態について、エネルギー・動径波動関数・格子収束を解析参照と比べる。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-hydrogenic-atoms-ja)

原子単位の1電子・定常動径問題。計算は有限半径箱の零Dirichlet境界を使い、無限領域の水素型解析解と比較する。一般多電子・分子・周期系の解法を意味しない。

$$
\left[-\frac12\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{2r^2}-\frac Zr\right]u_{n\ell}=E_{n\ell}u_{n\ell}
$$

$$
E_n^{\rm ref}=-\frac{Z^2}{2n^2},\qquad Z\in\{1,2\}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

**問題の図**

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja#hydrogenic-atoms-ja-validation)

E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。


### scope

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。

### assumptions

非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。

### units

原子単位系：エネルギーhartree、距離bohr。

### boundaries

孤立系、u(0)=u(r_max)=0。主計算r_max=60 bohr。H 1sの領域打切り依存は別に検査。

### Input and run

Input: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
Input SHA-256: 8680ad9e5b04b5689b52849c71d849ddb98f9ecc9bea851a0f09d2ee2fcc6237
ZIP: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip
Run from: quantum-atoms-2026-11-21

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
```

### Outputs

- results.json (json): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json
- profiles/hydrogenic-z1-n1-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n1-l0.csv
- profiles/hydrogenic-z1-n2-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l0.csv
- profiles/hydrogenic-z1-n2-l1.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l1.csv
- profiles/hydrogenic-z1-n3-l2.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n3-l2.csv
- profiles/hydrogenic-z2-n1-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n1-l0.csv
- profiles/hydrogenic-z2-n2-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l0.csv
- profiles/hydrogenic-z2-n2-l1.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l1.csv
- profiles/hydrogenic-z2-n3-l2.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n3-l2.csv

### Numerical acceptance

- normalization / 動径軌道の規格化: /hydrogenic/refinement; field=norm; |value − 1| ≤ 1e-12
- eigen-residual / 全固有値問題の残差: /hydrogenic/refinement; field=eigen_residual; value ≤ 1e-07 hartree
- analytic-energy-fine-grid / 最細格子の解析解との差: /hydrogenic/refinement; where={"dr": 0.01}; field=energy_error; value ≤ 0.00021 hartree
- energy-refinement / 格子細分による誤差低減: /checks/hydrogenic_exact_energy_errors_reduce; value = true

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#hydrogenic

### References

- E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。: https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic
- 原法の文献：Schrödinger, E. (1926), Quantisierung als Eigenwertproblem: https://doi.org/10.1002/andp.19263840404

Code license: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare energy, radial wavefunctions and grid refinement with analytic references for the specified Z=1,2 bound states.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-hydrogenic-atoms-en)

One-electron stationary radial problem in atomic units. A finite radial box with zero Dirichlet boundaries is compared with infinite-domain hydrogenic analytic references; not a general many-electron, molecular or periodic solver.

$$
\left[-\frac12\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{2r^2}-\frac Zr\right]u_{n\ell}=E_{n\ell}u_{n\ell}
$$

$$
E_n^{\rm ref}=-\frac{Z^2}{2n^2},\qquad Z\in\{1,2\}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

**Problem figure**

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en#hydrogenic-atoms-en-validation)

E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.


### scope

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.

### assumptions

Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh.

### units

Atomic units: energy in hartree, distance in bohr.

### boundaries

Isolated boundaries, u(0)=u(r_max)=0. Main domain r_max=60 bohr; hydrogen 1s has a separate box-truncation study.

### Input and run

Input: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
Input SHA-256: 8680ad9e5b04b5689b52849c71d849ddb98f9ecc9bea851a0f09d2ee2fcc6237
ZIP: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip
Run from: quantum-atoms-2026-11-21

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
```

### Outputs

- results.json (json): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json
- profiles/hydrogenic-z1-n1-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n1-l0.csv
- profiles/hydrogenic-z1-n2-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l0.csv
- profiles/hydrogenic-z1-n2-l1.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n2-l1.csv
- profiles/hydrogenic-z1-n3-l2.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z1-n3-l2.csv
- profiles/hydrogenic-z2-n1-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n1-l0.csv
- profiles/hydrogenic-z2-n2-l0.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l0.csv
- profiles/hydrogenic-z2-n2-l1.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n2-l1.csv
- profiles/hydrogenic-z2-n3-l2.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/hydrogenic-z2-n3-l2.csv

### Numerical acceptance

- normalization / Reduced-orbital normalization: /hydrogenic/refinement; field=norm; |value − 1| ≤ 1e-12
- eigen-residual / All eigenpair residuals: /hydrogenic/refinement; field=eigen_residual; value ≤ 1e-07 hartree
- analytic-energy-fine-grid / Finest-grid analytic energy errors: /hydrogenic/refinement; where={"dr": 0.01}; field=energy_error; value ≤ 0.00021 hartree
- energy-refinement / Energy-error reduction under refinement: /checks/hydrogenic_exact_energy_errors_reduce; value = true

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic

### References

- E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.: https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic
- Original method publication: Schrödinger, E. (1926), Quantisierung als Eigenwertproblem: https://doi.org/10.1002/andp.19263840404

Code license: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
