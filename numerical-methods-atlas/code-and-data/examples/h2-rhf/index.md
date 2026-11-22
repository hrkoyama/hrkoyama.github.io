# H₂ molecular RHF: independent reference, SCF and s-basis refinement / H₂分子RHF：独立参照・SCF・s型基底拡大

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: h2-rhf

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-h2.json

## ja

孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

### scope

孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

### assumptions

固定核・一重項の制限HF、1空間軌道の二重占有。自作Gaussian積分と別実装PySCFで同じ幾何・基底を使用。

### units

原子単位系：核間距離bohr、全エネルギーhartree。重なり行列・電子数・密度行列の規格化は入力と解説に記載。

### boundaries

孤立有限分子、Gaussian関数による全空間積分。周期境界や有限箱を使用しない。

### Input and run

Input: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json
Input SHA-256: 28bb38cda99ac89fb43e8dd85f3b38126d7684293c14762debe7b5453fa57daf
ZIP: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip
Run from: molecular-hf-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv

### Numerical acceptance

- numerical-flags / 固定入力の全数値判定: /checks; all values = true
- input-provenance / 入力ハッシュ: /input_sha256; value = 28bb38cda99ac89fb43e8dd85f3b38126d7684293c14762debe7b5453fa57daf
- max_reference_energy_error / max_reference_energy_error（定義・単位は解説）: /metrics/max_reference_energy_error; value ≤ 1e-09
- max_scf_commutator / max_scf_commutator（定義・単位は解説）: /metrics/max_scf_commutator; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error（定義・単位は解説）: /metrics/max_orthogonality_error; value ≤ 1e-09
- max_electron_count_error / max_electron_count_error（定義・単位は解説）: /metrics/max_electron_count_error; value ≤ 1e-09
- max_energy_consistency_error / max_energy_consistency_error（定義・単位は解説）: /metrics/max_energy_consistency_error; value ≤ 1e-09
- max_idempotency_error / max_idempotency_error（定義・単位は解説）: /metrics/max_idempotency_error; value ≤ 1e-08
- basis_energy_increase_max / basis_energy_increase_max（定義・単位は解説）: /metrics/basis_energy_increase_max; value ≤ 1e-08
- last_basis_energy_change_max / last_basis_energy_change_max（定義・単位は解説）: /metrics/last_basis_energy_change_max; value ≤ 0.001
- last_two_basis_changes_max / last_two_basis_changes_max（定義・単位は解説）: /metrics/last_two_basis_changes_max; value ≤ 0.001
- scf_tolerance_energy_error_max / scf_tolerance_energy_error_max（定義・単位は解説）: /metrics/scf_tolerance_energy_error_max; value ≤ 1e-06

### Failure and scope

最大反復・特異な重なり・不適切入力は失敗として扱う。SCF停止と基底公差、物理近似の妥当性を区別する。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/h2-hf/

### References

- 教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json
- 原法・独立参照の文献。確認深度は解説に明記。: https://doi.org/10.1098/rspa.1950.0036
- 原法・独立参照の文献。確認深度は解説に明記。: https://doi.org/10.1103/RevModPhys.23.69
- 原法・独立参照の文献。確認深度は解説に明記。: https://doi.org/10.1063/5.0006074

Code license: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

### scope

Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

### assumptions

Fixed nuclei, singlet restricted HF, one doubly occupied spatial orbital. Original Gaussian integrals and independent PySCF use identical geometries and bases.

### units

Atomic units: distances in bohr and total energies in hartree. Overlap, electron count and density normalization are specified in inputs/reading.

### boundaries

Isolated finite molecule with whole-space Gaussian integrals; no periodic boundary or finite box.

### Input and run

Input: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json
Input SHA-256: 28bb38cda99ac89fb43e8dd85f3b38126d7684293c14762debe7b5453fa57daf
ZIP: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip
Run from: molecular-hf-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv
- scf.csv (csv): https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv

### Numerical acceptance

- numerical-flags / All fixed-input numerical checks: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = 28bb38cda99ac89fb43e8dd85f3b38126d7684293c14762debe7b5453fa57daf
- max_reference_energy_error / max_reference_energy_error (definitions/units in reading): /metrics/max_reference_energy_error; value ≤ 1e-09
- max_scf_commutator / max_scf_commutator (definitions/units in reading): /metrics/max_scf_commutator; value ≤ 1e-08
- max_orthogonality_error / max_orthogonality_error (definitions/units in reading): /metrics/max_orthogonality_error; value ≤ 1e-09
- max_electron_count_error / max_electron_count_error (definitions/units in reading): /metrics/max_electron_count_error; value ≤ 1e-09
- max_energy_consistency_error / max_energy_consistency_error (definitions/units in reading): /metrics/max_energy_consistency_error; value ≤ 1e-09
- max_idempotency_error / max_idempotency_error (definitions/units in reading): /metrics/max_idempotency_error; value ≤ 1e-08
- basis_energy_increase_max / basis_energy_increase_max (definitions/units in reading): /metrics/basis_energy_increase_max; value ≤ 1e-08
- last_basis_energy_change_max / last_basis_energy_change_max (definitions/units in reading): /metrics/last_basis_energy_change_max; value ≤ 0.001
- last_two_basis_changes_max / last_two_basis_changes_max (definitions/units in reading): /metrics/last_two_basis_changes_max; value ≤ 0.001
- scf_tolerance_energy_error_max / scf_tolerance_energy_error_max (definitions/units in reading): /metrics/scf_tolerance_energy_error_max; value ≤ 1e-06

### Failure and scope

Iteration limits, singular overlap and invalid inputs fail explicitly. SCF stopping, basis tolerance and physical adequacy remain distinct.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/h2-hf/

### References

- Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json
- Primary formulation/reference publication; review depth stated in reading.: https://doi.org/10.1098/rspa.1950.0036
- Primary formulation/reference publication; review depth stated in reading.: https://doi.org/10.1103/RevModPhys.23.69
- Primary formulation/reference publication; review depth stated in reading.: https://doi.org/10.1063/5.0006074

Code license: https://hrkoyama.github.io/code/molecular-hf/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
