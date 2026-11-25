# Periodic-He KS-LDA: Gamma, k meshes, basis and SCF / 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: periodic-he-dft

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

**使用手法**

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) (`electronic-bases`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja) (`xc-functionals`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)
- [周期電子状態とk点](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja) (`k-point`)

**方程式**

[この実行例の近似式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-periodic-he-dft-ja)

3次元周期・固定HeセルのKS-LDA。BZ積分メッシュとバンド経路、数値収束と物理近似を区別。

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)
$$

$$
n(\mathbf r)=2\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k}|\psi_{n\mathbf k}(\mathbf r)|^2
$$

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

**問題の図**

![固定Heセルの周期LDA：Γ点とkメッシュ、Gaussian軌道基底・FFT格子・SCFを分離。DFTK平面波参照の打切り収束と差も表示。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) (`periodic-he-dft`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja#periodic-he-dft-ja-validation)

別実行のDFTK平面波KS-LDA。Γ／2³で同一モデルを比較し、平面波打切り収束を保存。異なる有限軌道基底のため機械精度一致は要求しない。

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。


### scope

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

### assumptions

固定中性セル・2電子閉殻、整数占有。Γ中心の分率k座標と一様重みを保存。同一のGTH係数・Libxc汎関数で独立DFTKと比較し、エネルギー原点のフィットはしない。

### units

原子単位系：距離bohr、エネルギーhartree／基本セル、波数は逆bohr。分率k座標は逆格子基底での値。

### boundaries

3次元Bloch周期境界。セル内He 1原子、価電子2、点電荷イオンのEwald項を含む中性セル。

### Input and run

Input: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json
Input SHA-256: d8558a1e6dec13e2c2246d82d387223bf8bbe4d151e41ef3afb993ddbbafea84
ZIP: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip
Run from: periodic-dft-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/scf.csv

### Numerical acceptance

- numerical-flags / 固定入力の全数値判定: /checks; all values = true
- input-provenance / 入力SHA-256: /input_sha256; value = d8558a1e6dec13e2c2246d82d387223bf8bbe4d151e41ef3afb993ddbbafea84
- kpoint_last_change / kpoint_last_change（定義・単位は解説）: /metrics/kpoint_last_change; value ≤ 0.001
- basis_last_change / basis_last_change（定義・単位は解説）: /metrics/basis_last_change; value ≤ 0.001
- auxiliary_last_change / auxiliary_last_change（定義・単位は解説）: /metrics/auxiliary_last_change; value ≤ 0.0001
- scf_last_change / scf_last_change（定義・単位は解説）: /metrics/scf_last_change; value ≤ 1e-07
- max_reference_energy_error / max_reference_energy_error（定義・単位は解説）: /metrics/max_reference_energy_error; value ≤ 0.001
- max_tight_scf_commutator / max_tight_scf_commutator（定義・単位は解説）: /metrics/max_tight_scf_commutator; value ≤ 1e-05
- max_electron_count_error / max_electron_count_error（定義・単位は解説）: /metrics/max_electron_count_error; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error（定義・単位は解説）: /metrics/max_orthogonality_error; value ≤ 1e-08
- max_energy_reconstruction_error / max_energy_reconstruction_error（定義・単位は解説）: /metrics/max_energy_reconstruction_error; value ≤ 1e-08
- min_sampled_ks_gap / min_sampled_ks_gap（定義・単位は解説）: /metrics/min_sampled_ks_gap; value ≥ 0.1
- max_overlap_condition / max_overlap_condition（定義・単位は解説）: /metrics/max_overlap_condition; value ≤ 10000000000.0

### Failure and scope

不正入力・重なり行列の悪条件・SCF未収束・公差不達を明示して失敗。低い残差だけでk点／基底収束や物理モデルを保証しない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/

### References

- 別実行のDFTK平面波KS-LDA。Γ／2³で同一モデルを比較し、平面波打切り収束を保存。異なる有限軌道基底のため機械精度一致は要求しない。: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.1007/BF01339455
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.1103/PhysRevB.13.5188
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.1103/PhysRevB.54.1703
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.1139/p80-159
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.1063/5.0006074
- 原法・独立実装の文献。確認深度は解説に明記。: https://doi.org/10.21105/jcon.00069

Code license: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作ドライバー・検証コードはMIT。PySCF・DFTK・LibxcとGTH／Gaussian基底データはそれぞれの条件を保持。入力・数値・図・本文は個別条件。本台帳は一括許諾を追加しません。

## en

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

**Methods used**

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) (`electronic-bases`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en) (`xc-functionals`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)
- [Periodic electronic structure and k-point sampling](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en) (`k-point`)

**Equations**

[This example’s approximation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-periodic-he-dft-en)

KS-LDA for a fixed 3D periodic He cell. BZ integration meshes differ from band paths; numerical convergence differs from physical-model accuracy.

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)
$$

$$
n(\mathbf r)=2\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k}|\psi_{n\mathbf k}(\mathbf r)|^2
$$

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

**Problem figure**

![Periodic LDA for fixed He: separate Gamma/k sampling, Gaussian orbital basis, FFT grid and SCF. Includes independently converged DFTK plane-wave reference differences.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) (`periodic-he-dft`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en#periodic-he-dft-en-validation)

Separately executed DFTK plane-wave KS-LDA at Gamma and 2³ for the same model, with cutoff convergence saved. Different finite orbital bases are compared within a stated tolerance, without machine-precision claims.

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.


### scope

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

### assumptions

Fixed neutral two-electron closed-shell cell with integer occupations. Explicit Gamma-centered fractional k coordinates and equal weights. Independent DFTK uses identical GTH coefficients and Libxc functionals; no fitted energy shifts.

### units

Atomic units: distances in bohr, energies in hartree per primitive cell and wavevectors in inverse bohr. Fractional k coordinates use reciprocal-lattice units.

### boundaries

Three-dimensional Bloch periodic boundaries. One He atom and two valence electrons per neutral primitive cell, including the ionic Ewald term.

### Input and run

Input: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json
Input SHA-256: d8558a1e6dec13e2c2246d82d387223bf8bbe4d151e41ef3afb993ddbbafea84
ZIP: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip
Run from: periodic-dft-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/scf.csv

### Numerical acceptance

- numerical-flags / All fixed-input numerical checks: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = d8558a1e6dec13e2c2246d82d387223bf8bbe4d151e41ef3afb993ddbbafea84
- kpoint_last_change / kpoint_last_change (definitions and units in reading): /metrics/kpoint_last_change; value ≤ 0.001
- basis_last_change / basis_last_change (definitions and units in reading): /metrics/basis_last_change; value ≤ 0.001
- auxiliary_last_change / auxiliary_last_change (definitions and units in reading): /metrics/auxiliary_last_change; value ≤ 0.0001
- scf_last_change / scf_last_change (definitions and units in reading): /metrics/scf_last_change; value ≤ 1e-07
- max_reference_energy_error / max_reference_energy_error (definitions and units in reading): /metrics/max_reference_energy_error; value ≤ 0.001
- max_tight_scf_commutator / max_tight_scf_commutator (definitions and units in reading): /metrics/max_tight_scf_commutator; value ≤ 1e-05
- max_electron_count_error / max_electron_count_error (definitions and units in reading): /metrics/max_electron_count_error; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error (definitions and units in reading): /metrics/max_orthogonality_error; value ≤ 1e-08
- max_energy_reconstruction_error / max_energy_reconstruction_error (definitions and units in reading): /metrics/max_energy_reconstruction_error; value ≤ 1e-08
- min_sampled_ks_gap / min_sampled_ks_gap (definitions and units in reading): /metrics/min_sampled_ks_gap; value ≥ 0.1
- max_overlap_condition / max_overlap_condition (definitions and units in reading): /metrics/max_overlap_condition; value ≤ 10000000000.0

### Failure and scope

Invalid inputs, excessive overlap conditioning, SCF nonconvergence and missed tolerances fail explicitly. Small residuals alone do not establish k/basis convergence or physical-model accuracy.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/

### References

- Separately executed DFTK plane-wave KS-LDA at Gamma and 2³ for the same model, with cutoff convergence saved. Different finite orbital bases are compared within a stated tolerance, without machine-precision claims.: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.1007/BF01339455
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.1103/PhysRevB.13.5188
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.1103/PhysRevB.54.1703
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.1139/p80-159
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.1063/5.0006074
- Primary formulation or independent implementation; reading states review depth.: https://doi.org/10.21105/jcon.00069

Code license: https://hrkoyama.github.io/code/periodic-dft/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original driver and validation code is MIT. PySCF, DFTK, Libxc and GTH/Gaussian basis data retain their own terms. Inputs, numerical data, figures and prose retain item-specific terms; this registry adds no blanket permission.
