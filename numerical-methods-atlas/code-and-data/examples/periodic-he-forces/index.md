# Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface / 周期He₂の原子間力：解析力・有限差分・BOMD接続

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: periodic-he-forces

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

**使用手法**

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) (`electronic-bases`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja) (`xc-functionals`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)
- [周期電子状態とk点](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja) (`k-point`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-periodic-he-forces-ja)

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

$$
F_{I\alpha}=-\frac{\partial E_{\rm BO}}{\partial R_{I\alpha}}
$$

$$
F^{\rm FD}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

**問題の図**

![非対称He₂の解析力をエネルギー有限差分とDFTK参照で比較。力のk点・基底・FFT・SCF収束とBOMDの局所接続確認。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja#periodic-he-forces-ja-validation)

独立DFTK平面波計算：Γ／2³の解析力、8カットオフ設定、全6座標のエネルギー有限差分。共通Libxcと異なる有限基底の制約を明記。

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。


### scope

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

### assumptions

固定した非対称2原子Heセル（5 bohr立方、4価電子、非偏極・整数占有、局所GTH、LDA_X＋VWN5）。PySCFライブラリを使う検証ドライバー。物理的な平衡He物質や長時間MDではありません。

### units

原子単位：エネルギー hartree/cell、力 hartree/bohr、核座標 bohr、質量 電子質量、時間 原子時間。

### boundaries

3次元Bloch周期境界。中性セルにHe2原子・価電子4個。イオンEwald項を含む全エネルギーのCartesian微分。

### Input and run

Input: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json
Input SHA-256: d25fe56cf92f1486d9553ead5e7851db49fb3f319b7d32d7813278cc4103c097
ZIP: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip
Run from: periodic-forces-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/scf.csv
- finite-difference.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/finite-difference.csv

### Numerical acceptance

- numerical-flags / 固定入力の全数値判定: /checks; all values = true
- input-provenance / 固定入力のSHA-256: /input_sha256; value = d25fe56cf92f1486d9553ead5e7851db49fb3f319b7d32d7813278cc4103c097
- reference-provenance / 独立参照のSHA-256: /reference_sha256; value = f4beb96c3672066378e34ad756ea9a2b08aab10c5b16aae31537644b23303db7
- finite_difference_max_error / finite_difference_max_error（定義・単位は解説）: /metrics/finite_difference_max_error; value ≤ 2e-06
- finite_difference_scan_max_error / finite_difference_scan_max_error（定義・単位は解説）: /metrics/finite_difference_scan_max_error; value ≤ 1e-05
- max_electron_count_error / max_electron_count_error（定義・単位は解説）: /metrics/max_electron_count_error; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error（定義・単位は解説）: /metrics/max_orthogonality_error; value ≤ 1e-07
- max_energy_reconstruction_error / max_energy_reconstruction_error（定義・単位は解説）: /metrics/max_energy_reconstruction_error; value ≤ 1e-08
- min_sampled_ks_gap / min_sampled_ks_gap（定義・単位は解説）: /metrics/min_sampled_ks_gap; value ≥ 0.1
- max_overlap_condition / max_overlap_condition（定義・単位は解説）: /metrics/max_overlap_condition; value ≤ 100000000000.0
- finest_net_force / finest_net_force（定義・単位は解説）: /metrics/finest_net_force; value ≤ 1e-07
- bomd_position_step_difference / bomd_position_step_difference（定義・単位は解説）: /metrics/bomd_position_step_difference; value ≤ 1e-06
- kpoint_last_change / kpoint_last_change（定義・単位は解説）: /metrics/kpoint_last_change; value ≤ 0.001
- basis_last_change / basis_last_change（定義・単位は解説）: /metrics/basis_last_change; value ≤ 0.0001
- basis-k2_last_change / basis-k2_last_change（定義・単位は解説）: /metrics/basis-k2_last_change; value ≤ 0.0001
- auxiliary_last_change / auxiliary_last_change（定義・単位は解説）: /metrics/auxiliary_last_change; value ≤ 1e-05
- scf_last_change / scf_last_change（定義・単位は解説）: /metrics/scf_last_change; value ≤ 1e-06
- max_reference_force_error / max_reference_force_error（定義・単位は解説）: /metrics/max_reference_force_error; value ≤ 0.0002
- max_reference_energy_error / max_reference_energy_error（定義・単位は解説）: /metrics/max_reference_energy_error; value ≤ 0.0002
- max_tight_scf_commutator / max_tight_scf_commutator（定義・単位は解説）: /metrics/max_tight_scf_commutator; value ≤ 1e-06
- bomd_full_step_energy_defect / bomd_full_step_energy_defect（定義・単位は解説）: /metrics/bomd_full_step_energy_defect; value ≤ 1e-06
- bomd_two_half_steps_energy_defect / bomd_two_half_steps_energy_defect（定義・単位は解説）: /metrics/bomd_two_half_steps_energy_defect; value ≤ 1e-06
- reference_cutoff_force_change / reference_cutoff_force_change（定義・単位は解説）: /metrics/reference_cutoff_force_change; value ≤ 1e-05
- reference_finite_difference_max_error / reference_finite_difference_max_error（定義・単位は解説）: /metrics/reference_finite_difference_max_error; value ≤ 1e-05

### Failure and scope

不正モデル・非有限値・参照の改変・SCF未収束・力/収束公差不達を拒否。未収束の力をBOMDへ渡さない。短い刻み比較は長時間NVEを保証しない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-forces/

### References

- 独立DFTK平面波計算：Γ／2³の解析力、8カットオフ設定、全6座標のエネルギー有限差分。共通Libxcと異なる有限基底の制約を明記。: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/reference-dftk.json
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://doi.org/10.1139/p80-159
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://doi.org/10.1063/5.0006074
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://proceedings.juliacon.org/papers/10.21105/jcon.00069
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://journals.aps.org/pr/abstract/10.1103/PhysRev.56.340
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://www.tandfonline.com/doi/abs/10.1080/00268976900100941
- 原法・解析微分・独立実装の文献。確認範囲は解説に明記。: https://pubs.rsc.org/en/content/articlelanding/2005/cp/b509494a

Code license: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作ドライバー・検証コードはMIT。PySCF・DFTK・LibxcとGTH／Gaussian基底データはそれぞれの条件を保持。入力・数値・図・本文は個別条件。本台帳は一括許諾を追加しません。

## en

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

**Methods used**

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) (`electronic-bases`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en) (`xc-functionals`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)
- [Periodic electronic structure and k-point sampling](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en) (`k-point`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-periodic-he-forces-en)

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

$$
F_{I\alpha}=-\frac{\partial E_{\rm BO}}{\partial R_{I\alpha}}
$$

$$
F^{\rm FD}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

**Problem figure**

![Asymmetric-He₂ analytic forces versus energy finite differences and DFTK reference. Force k-point, basis, FFT and SCF refinement, plus a local BOMD interface check.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en#periodic-he-forces-en-validation)

Independent DFTK plane waves: Gamma/2³ analytic forces, eight cutoff settings and all-six-coordinate energy finite differences. State shared Libxc formulas and different finite-basis limits.

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.


### scope

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

### assumptions

Fixed asymmetric two-He cell (5-bohr cubic lattice, four valence electrons, unpolarized integer occupations, local GTH and LDA_X plus VWN5). A library-backed PySCF validation driver; not physical equilibrium helium or long-time MD.

### units

Atomic units: energy hartree/cell, force hartree/bohr, coordinates bohr, masses electron masses and atomic time.

### boundaries

Three-dimensional Bloch periodic boundaries. Two He atoms and four valence electrons per neutral cell. Cartesian derivatives of the total energy including ionic Ewald interactions.

### Input and run

Input: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json
Input SHA-256: d25fe56cf92f1486d9553ead5e7851db49fb3f319b7d32d7813278cc4103c097
ZIP: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip
Run from: periodic-forces-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/scf.csv
- finite-difference.csv (csv): https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/finite-difference.csv

### Numerical acceptance

- numerical-flags / All fixed-input numerical checks: /checks; all values = true
- input-provenance / Fixed-input SHA-256: /input_sha256; value = d25fe56cf92f1486d9553ead5e7851db49fb3f319b7d32d7813278cc4103c097
- reference-provenance / Independent-reference SHA-256: /reference_sha256; value = f4beb96c3672066378e34ad756ea9a2b08aab10c5b16aae31537644b23303db7
- finite_difference_max_error / finite_difference_max_error (definitions and units in reading): /metrics/finite_difference_max_error; value ≤ 2e-06
- finite_difference_scan_max_error / finite_difference_scan_max_error (definitions and units in reading): /metrics/finite_difference_scan_max_error; value ≤ 1e-05
- max_electron_count_error / max_electron_count_error (definitions and units in reading): /metrics/max_electron_count_error; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error (definitions and units in reading): /metrics/max_orthogonality_error; value ≤ 1e-07
- max_energy_reconstruction_error / max_energy_reconstruction_error (definitions and units in reading): /metrics/max_energy_reconstruction_error; value ≤ 1e-08
- min_sampled_ks_gap / min_sampled_ks_gap (definitions and units in reading): /metrics/min_sampled_ks_gap; value ≥ 0.1
- max_overlap_condition / max_overlap_condition (definitions and units in reading): /metrics/max_overlap_condition; value ≤ 100000000000.0
- finest_net_force / finest_net_force (definitions and units in reading): /metrics/finest_net_force; value ≤ 1e-07
- bomd_position_step_difference / bomd_position_step_difference (definitions and units in reading): /metrics/bomd_position_step_difference; value ≤ 1e-06
- kpoint_last_change / kpoint_last_change (definitions and units in reading): /metrics/kpoint_last_change; value ≤ 0.001
- basis_last_change / basis_last_change (definitions and units in reading): /metrics/basis_last_change; value ≤ 0.0001
- basis-k2_last_change / basis-k2_last_change (definitions and units in reading): /metrics/basis-k2_last_change; value ≤ 0.0001
- auxiliary_last_change / auxiliary_last_change (definitions and units in reading): /metrics/auxiliary_last_change; value ≤ 1e-05
- scf_last_change / scf_last_change (definitions and units in reading): /metrics/scf_last_change; value ≤ 1e-06
- max_reference_force_error / max_reference_force_error (definitions and units in reading): /metrics/max_reference_force_error; value ≤ 0.0002
- max_reference_energy_error / max_reference_energy_error (definitions and units in reading): /metrics/max_reference_energy_error; value ≤ 0.0002
- max_tight_scf_commutator / max_tight_scf_commutator (definitions and units in reading): /metrics/max_tight_scf_commutator; value ≤ 1e-06
- bomd_full_step_energy_defect / bomd_full_step_energy_defect (definitions and units in reading): /metrics/bomd_full_step_energy_defect; value ≤ 1e-06
- bomd_two_half_steps_energy_defect / bomd_two_half_steps_energy_defect (definitions and units in reading): /metrics/bomd_two_half_steps_energy_defect; value ≤ 1e-06
- reference_cutoff_force_change / reference_cutoff_force_change (definitions and units in reading): /metrics/reference_cutoff_force_change; value ≤ 1e-05
- reference_finite_difference_max_error / reference_finite_difference_max_error (definitions and units in reading): /metrics/reference_finite_difference_max_error; value ≤ 1e-05

### Failure and scope

Reject invalid models, nonfinite values, altered references, SCF nonconvergence and missed force/refinement criteria. Do not pass unconverged forces to BOMD. A short step comparison does not establish long-time NVE conservation.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-forces/

### References

- Independent DFTK plane waves: Gamma/2³ analytic forces, eight cutoff settings and all-six-coordinate energy finite differences. State shared Libxc formulas and different finite-basis limits.: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/reference-dftk.json
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://doi.org/10.1139/p80-159
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://doi.org/10.1063/5.0006074
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://proceedings.juliacon.org/papers/10.21105/jcon.00069
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://journals.aps.org/pr/abstract/10.1103/PhysRev.56.340
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://www.tandfonline.com/doi/abs/10.1080/00268976900100941
- Primary formulation, analytic differentiation or independent implementation; reading states review depth.: https://pubs.rsc.org/en/content/articlelanding/2005/cp/b509494a

Code license: https://hrkoyama.github.io/code/periodic-forces/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original driver and validation code is MIT. PySCF, DFTK, Libxc and GTH/Gaussian basis data retain their own terms. Inputs, numerical data, figures and prose retain item-specific terms; this registry adds no blanket permission.
