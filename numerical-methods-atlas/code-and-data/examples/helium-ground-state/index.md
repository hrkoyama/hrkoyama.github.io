# Helium: closed-shell HF and exchange-only LDA / He：閉殻HF・交換のみLDA

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: helium-ground-state

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

球対称1s²のHeをRHFと交換のみLDAで解き、SCF収束・エネルギー・電子数を独立な有限基底参照と照合する。

### scope

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

### assumptions

非相対論・無限質量の点核、2電子が単一1s空間軌道を二重占有。2次中心差分と線形密度混合。HF交換の局所還元はこの2電子問題に限定。

### units

原子単位系：エネルギーhartree、距離bohr。

### boundaries

球対称の孤立系、u(0)=u(r_max)=0。主計算r_max=16 bohr。格子幅と領域打切りを別々に検査。

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
- profiles/helium-hf.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-hf.csv
- profiles/helium-lda_x.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-lda_x.csv

### Numerical acceptance

- scf-convergence / 全格子のSCF収束: /helium/refinement; field=converged; value = true
- electron-count / 電子数: /helium/refinement; field=electron_count; |value − 2| ≤ 1e-12
- density-residual / 入力出力密度のL1残差: /helium/refinement; field=density_residual; value ≤ 1e-09
- orbital-residual / 出力密度での軌道残差: /helium/refinement; field=orbital_residual; value ≤ 1e-07 hartree
- energy-identity / エネルギー恒等式の誤差: /helium/refinement; field=energy_identity_error; value ≤ 1e-10 hartree
- independent-energy / h²外挿と独立参照の差（誤差の保証ではない）: /helium/independent_comparison; field=extrapolated_reference_difference; |value| ≤ 1e-08 hartree
- independent-density / 独立参照との密度L1差: /helium/independent_comparison; field=radial_density_l1_difference; value ≤ 5e-05
- iteration-limit-is-failure / 最大1反復は未収束と判定: /helium/expected_nonconvergence; field=converged; value = false
- failure-reason / 終了理由を保存: /helium/expected_nonconvergence; field=reason; value = max_iterations

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#helium

### References

- PySCF 2.11.0 / LibxcのGaussian基底参照。外挿値・有限格子値・参照を区別。参照scriptの再実行は今回の共通runnerの測定に含まない。: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- 原法の文献：Roothaan, C. C. J. (1951), New Developments in Molecular Orbital Theory: https://doi.org/10.1103/RevModPhys.23.69
- 原法の文献：Kohn, W.; Sham, L. J. (1965), Self-Consistent Equations Including Exchange and Correlation Effects: https://doi.org/10.1103/PhysRev.140.A1133
- 原法の文献：Dirac, P. A. M. (1930), Note on Exchange Phenomena in the Thomas Atom: https://doi.org/10.1017/S0305004100016108

Code license: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Solve spherical 1s² helium with RHF and exchange-only LDA; compare SCF convergence, energies and electron count with independent finite-basis references.

### scope

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

### assumptions

Nonrelativistic infinite-mass point nucleus, two electrons doubly occupying a single 1s spatial orbital. Second-order central differences and linear density mixing. Local HF exchange reduction is specific to this two-electron problem.

### units

Atomic units: energy in hartree, distance in bohr.

### boundaries

Spherical isolated system, u(0)=u(r_max)=0. Main domain r_max=16 bohr; mesh and box truncation are studied separately.

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
- profiles/helium-hf.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-hf.csv
- profiles/helium-lda_x.csv (csv): https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-lda_x.csv

### Numerical acceptance

- scf-convergence / SCF convergence on every mesh: /helium/refinement; field=converged; value = true
- electron-count / Electron number: /helium/refinement; field=electron_count; |value − 2| ≤ 1e-12
- density-residual / Input-output density L1 residual: /helium/refinement; field=density_residual; value ≤ 1e-09
- orbital-residual / Output-density orbital residual: /helium/refinement; field=orbital_residual; value ≤ 1e-07 hartree
- energy-identity / Energy-accounting identity error: /helium/refinement; field=energy_identity_error; value ≤ 1e-10 hartree
- independent-energy / h²-extrapolated difference from independent references, not a certified bound: /helium/independent_comparison; field=extrapolated_reference_difference; |value| ≤ 1e-08 hartree
- independent-density / Density L1 difference from independent references: /helium/independent_comparison; field=radial_density_l1_difference; value ≤ 5e-05
- iteration-limit-is-failure / One iteration is reported as unconverged: /helium/expected_nonconvergence; field=converged; value = false
- failure-reason / Save termination reason: /helium/expected_nonconvergence; field=reason; value = max_iterations

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#helium

### References

- PySCF 2.11.0 / Libxc finite-Gaussian references. Distinguish extrapolation, finite-grid values and references. Regenerating the independent reference is outside this measured runner.: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- Original method publication: Roothaan, C. C. J. (1951), New Developments in Molecular Orbital Theory: https://doi.org/10.1103/RevModPhys.23.69
- Original method publication: Kohn, W.; Sham, L. J. (1965), Self-Consistent Equations Including Exchange and Correlation Effects: https://doi.org/10.1103/PhysRev.140.A1133
- Original method publication: Dirac, P. A. M. (1930), Note on Exchange Phenomena in the Thomas Atom: https://doi.org/10.1017/S0305004100016108

Code license: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
