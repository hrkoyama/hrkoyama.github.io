# 最小基底H2のRHF/UHF/FCI・2固定幾何

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

**使用手法**

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) (`configuration-interaction`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-algorithm)

固定SCFでRHFと対称性を破ったUHFを求め、4x4二電子Hamiltonianを対角化します。

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

- [最小2電子模型のスピン非制限HF](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja) (`unrestricted-hartree-fock-model`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。


**問題の図**

![最小基底H2のRHF/UHF/FCI・2固定幾何：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-validation)

保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。

- [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja) (`h2-rhf-uhf-fci`; 同じ問題の参照 · 半解析参照)

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
## 前提・単位・境界

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

**編集上の補足**

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

## 採用した計算法

固定SCFでRHFと対称性を破ったUHFを求め、4x4二電子Hamiltonianを対角化します。

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

## 比較・検証

保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。

## 確認の限界

UHFはスピン混入を持ちます。2幾何だけで完全な解離曲線や連続空間の厳密解を保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "98 R1.4 saved PySCF RHF": 1.7319479184152442e-14,
    "98 R1.4 UHF analytic paired ansatz": 1.3322676295501878e-15,
    "98 R1.4 finite-basis FCI analytic": 4.440892098500626e-16,
    "98 R1.4 independent fermion assembly": 1.1102230246251565e-16,
    "98 R1.4 FCI residual": 1.510066572755813e-15,
    "98 R1.4 UHF <= RHF": 0.0,
    "98 R1.4 FCI <= UHF": -0.02056161860694994,
    "98 R1.4 RHF electron count": 1.3322676295501878e-15,
    "98 R1.4 RHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 RHF SCF residual": 4.739336526991705e-16,
    "98 R1.4 UHF electron count": 1.3322676295501878e-15,
    "98 R1.4 UHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 UHF SCF residual": 3.031599154361081e-11,
    "98 R3.0 saved PySCF RHF": 8.659739592076221e-15,
    "98 R3.0 UHF analytic paired ansatz": 0.0,
    "98 R3.0 finite-basis FCI analytic": 6.661338147750939e-16,
    "98 R3.0 independent fermion assembly": 1.1102230246251565e-16,
    "98 R3.0 FCI residual": 6.798699777552591e-16,
    "98 R3.0 UHF <= RHF": -0.06574294870227004,
    "98 R3.0 FCI <= UHF": -0.03413887592482623,
    "98 R3.0 RHF electron count": 8.881784197001252e-16,
    "98 R3.0 RHF orbital norm": 6.661338147750939e-16,
    "98 R3.0 RHF SCF residual": 1.0881821476711805e-16,
    "98 R3.0 UHF electron count": 4.440892098500626e-16,
    "98 R3.0 UHF orbital norm": 7.771561172376096e-16,
    "98 R3.0 UHF SCF residual": 1.610351596292876e-11,
    "98 stretched UHF energy lowering": 0.06574294870227004,
    "98 stretched UHF spin contamination": 0.7742403321308335
  },
  "checks": {
    "98 R1.4 saved PySCF RHF": true,
    "98 R1.4 UHF analytic paired ansatz": true,
    "98 R1.4 finite-basis FCI analytic": true,
    "98 R1.4 independent fermion assembly": true,
    "98 R1.4 FCI residual": true,
    "98 R1.4 UHF <= RHF": true,
    "98 R1.4 FCI <= UHF": true,
    "98 R1.4 RHF electron count": true,
    "98 R1.4 RHF orbital norm": true,
    "98 R1.4 RHF SCF residual": true,
    "98 R1.4 UHF electron count": true,
    "98 R1.4 UHF orbital norm": true,
    "98 R1.4 UHF SCF residual": true,
    "98 R3.0 saved PySCF RHF": true,
    "98 R3.0 UHF analytic paired ansatz": true,
    "98 R3.0 finite-basis FCI analytic": true,
    "98 R3.0 independent fermion assembly": true,
    "98 R3.0 FCI residual": true,
    "98 R3.0 UHF <= RHF": true,
    "98 R3.0 FCI <= UHF": true,
    "98 R3.0 RHF electron count": true,
    "98 R3.0 RHF orbital norm": true,
    "98 R3.0 RHF SCF residual": true,
    "98 R3.0 UHF electron count": true,
    "98 R3.0 UHF orbital norm": true,
    "98 R3.0 UHF SCF residual": true,
    "98 stretched UHF energy lowering": true,
    "98 stretched UHF spin contamination": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
公式CI文書の導入とFCIのスピン区分・行列式の例を選択閲読。章全体や実装全体の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

**Methods used**

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) (`configuration-interaction`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-algorithm)

Run fixed SCF and diagonalize the4x4 two-electron Hamiltonian using the unchanged explicit H STO-3G contraction.

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

- [Unrestricted HF in a minimal two-electron model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en) (`unrestricted-hartree-fock-model`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.


**Problem figure**

![Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-validation)

Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.

- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en) (`h2-rhf-uhf-fci`; Same-problem reference · Semi-analytic reference)

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
## Assumptions, units and boundaries

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

**Editorial clarification**

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

## Adopted numerical method

Run fixed SCF and diagonalize the4x4 two-electron Hamiltonian using the unchanged explicit H STO-3G contraction.

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

## References and validation

Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.

## Limits

Only two H2 geometries and two contracted s orbitals; no complete-basis dissociation curve. UHF is spin contaminated; FCI exactness is finite-basis only.

## Stored measurements and decisions

```json
{
  "metrics": {
    "98 R1.4 saved PySCF RHF": 1.7319479184152442e-14,
    "98 R1.4 UHF analytic paired ansatz": 1.3322676295501878e-15,
    "98 R1.4 finite-basis FCI analytic": 4.440892098500626e-16,
    "98 R1.4 independent fermion assembly": 1.1102230246251565e-16,
    "98 R1.4 FCI residual": 1.510066572755813e-15,
    "98 R1.4 UHF <= RHF": 0.0,
    "98 R1.4 FCI <= UHF": -0.02056161860694994,
    "98 R1.4 RHF electron count": 1.3322676295501878e-15,
    "98 R1.4 RHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 RHF SCF residual": 4.739336526991705e-16,
    "98 R1.4 UHF electron count": 1.3322676295501878e-15,
    "98 R1.4 UHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 UHF SCF residual": 3.031599154361081e-11,
    "98 R3.0 saved PySCF RHF": 8.659739592076221e-15,
    "98 R3.0 UHF analytic paired ansatz": 0.0,
    "98 R3.0 finite-basis FCI analytic": 6.661338147750939e-16,
    "98 R3.0 independent fermion assembly": 1.1102230246251565e-16,
    "98 R3.0 FCI residual": 6.798699777552591e-16,
    "98 R3.0 UHF <= RHF": -0.06574294870227004,
    "98 R3.0 FCI <= UHF": -0.03413887592482623,
    "98 R3.0 RHF electron count": 8.881784197001252e-16,
    "98 R3.0 RHF orbital norm": 6.661338147750939e-16,
    "98 R3.0 RHF SCF residual": 1.0881821476711805e-16,
    "98 R3.0 UHF electron count": 4.440892098500626e-16,
    "98 R3.0 UHF orbital norm": 7.771561172376096e-16,
    "98 R3.0 UHF SCF residual": 1.610351596292876e-11,
    "98 stretched UHF energy lowering": 0.06574294870227004,
    "98 stretched UHF spin contamination": 0.7742403321308335
  },
  "checks": {
    "98 R1.4 saved PySCF RHF": true,
    "98 R1.4 UHF analytic paired ansatz": true,
    "98 R1.4 finite-basis FCI analytic": true,
    "98 R1.4 independent fermion assembly": true,
    "98 R1.4 FCI residual": true,
    "98 R1.4 UHF <= RHF": true,
    "98 R1.4 FCI <= UHF": true,
    "98 R1.4 RHF electron count": true,
    "98 R1.4 RHF orbital norm": true,
    "98 R1.4 RHF SCF residual": true,
    "98 R1.4 UHF electron count": true,
    "98 R1.4 UHF orbital norm": true,
    "98 R1.4 UHF SCF residual": true,
    "98 R3.0 saved PySCF RHF": true,
    "98 R3.0 UHF analytic paired ansatz": true,
    "98 R3.0 finite-basis FCI analytic": true,
    "98 R3.0 independent fermion assembly": true,
    "98 R3.0 FCI residual": true,
    "98 R3.0 UHF <= RHF": true,
    "98 R3.0 FCI <= UHF": true,
    "98 R3.0 RHF electron count": true,
    "98 R3.0 RHF orbital norm": true,
    "98 R3.0 RHF SCF residual": true,
    "98 R3.0 UHF electron count": true,
    "98 R3.0 UHF orbital norm": true,
    "98 R3.0 UHF SCF residual": true,
    "98 stretched UHF energy lowering": true,
    "98 stretched UHF spin contamination": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
Introduction and FCI/spin-sector examples: all determinants within a finite symmetry sector, diagonalization, Nalpha/Nbeta. Not full chapter or full package source.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
