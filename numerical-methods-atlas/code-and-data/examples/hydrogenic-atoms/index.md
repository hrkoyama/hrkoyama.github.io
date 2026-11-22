# Hydrogenic atoms: analytic references and grid refinement / 水素型原子：解析解と格子収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: hydrogenic-atoms

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

Z=1,2の指定された束縛状態について、エネルギー・動径波動関数・格子収束を解析参照と比べる。

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
