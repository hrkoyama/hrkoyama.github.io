# H/Heの式・密度・固定参照カード

既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)
- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-algorithm)

pとn、軌道固有値と全エネルギーを区別し、既存の式と3保存行を照合します。

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。


**問題の図**

![H/Heの式・密度・固定参照カード：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-validation)

選択3行は各40基底関数です。保存値・電子数・出典を照合し、新SCFは実行しません。

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
## 前提・単位・境界

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

**編集上の補足**

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

## 採用した計算法

pとn、軌道固有値と全エネルギーを区別し、既存の式と3保存行を照合します。

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

## 比較・検証

選択3行は各40基底関数です。保存値・電子数・出典を照合し、新SCFは実行しません。

## 確認の限界

有限基底HFや交換のみLDAを相関込みの厳密Heとは呼びません。独立参照の再生成は0回です。

## 保存実測値と判定

```json
{
  "metrics": {
    "96 selected saved row count": 0.0,
    "96 saved energy literal 0": 0.0,
    "96 basis functions 0": 0.0,
    "96 saved electron count 0": 1.7763568394002505e-15,
    "96 saved energy literal 1": 0.0,
    "96 basis functions 1": 0.0,
    "96 saved electron count 1": 3.1086244689504383e-15,
    "96 saved energy literal 2": 0.0,
    "96 basis functions 2": 0.0,
    "96 saved electron count 2": 3.1086244689504383e-15
  },
  "checks": {
    "96 selected saved row count": true,
    "96 saved energy literal 0": true,
    "96 basis functions 0": true,
    "96 saved electron count 0": true,
    "96 saved energy literal 1": true,
    "96 basis functions 1": true,
    "96 saved electron count 1": true,
    "96 saved energy literal 2": true,
    "96 basis functions 2": true,
    "96 saved electron count 2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/index.json

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

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
同一作業内の選択閲読：式7–8、13–15、24–35と近傍のHO/Coulomb・規格化・測度。章全体・出典書籍の通読ではありません。

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Hydrogenic formulas and immutable finite-basis helium reference cards

Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)
- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-algorithm)

Audit existing formulas and three stored energy rows; distinguish radial from volume density and orbital from total energy.

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.


**Problem figure**

![Hydrogenic formulas and immutable finite-basis helium reference cards: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-validation)

Each of three saved rows uses40 uncontracted functions. Check exact values and electron counts without rerunning SCF or independent references.

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
## Assumptions, units and boundaries

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

**Editorial clarification**

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

## Adopted numerical method

Audit existing formulas and three stored energy rows; distinguish radial from volume density and orbital from total energy.

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

## References and validation

Each of three saved rows uses40 uncontracted functions. Check exact values and electron counts without rerunning SCF or independent references.

## Limits

No new SCF, external-reference regeneration, complete-basis or correlated-exact helium claim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "96 selected saved row count": 0.0,
    "96 saved energy literal 0": 0.0,
    "96 basis functions 0": 0.0,
    "96 saved electron count 0": 1.7763568394002505e-15,
    "96 saved energy literal 1": 0.0,
    "96 basis functions 1": 0.0,
    "96 saved electron count 1": 3.1086244689504383e-15,
    "96 saved energy literal 2": 0.0,
    "96 basis functions 2": 0.0,
    "96 saved electron count 2": 3.1086244689504383e-15
  },
  "checks": {
    "96 selected saved row count": true,
    "96 saved energy literal 0": true,
    "96 basis functions 0": true,
    "96 saved electron count 0": true,
    "96 saved energy literal 1": true,
    "96 basis functions 1": true,
    "96 saved electron count 1": true,
    "96 saved energy literal 2": true,
    "96 basis functions 2": true,
    "96 saved electron count 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/index.json

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

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
Earlier same-session R3 selected E7–8,E13–15,E24–35; oscillator/Coulomb normalization and measure. Full chapter/books not audited.

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
