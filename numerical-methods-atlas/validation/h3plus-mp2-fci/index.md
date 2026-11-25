# 3中心H3+の小RHF/MP2/FCI模型

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

**使用手法**

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [MP2摂動論](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja) (`mp2`)
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) (`configuration-interaction`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-algorithm)

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。


**問題の図**

![3中心H3+の小RHF/MP2/FCI模型：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-validation)

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja) (`h3plus-mp2-fci`; 同じ問題の参照 · 有限格子の数値参照)

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。
## 前提・単位・境界

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

**編集上の補足**

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

## 採用した計算法

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

## 比較・検証

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

## 確認の限界

一般分子DFT・CC・一般多参照法は未実装です。MP2は変分的でなく、外部独立エンジンの新参照値も生成しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "99 operator assembly": 4.440892098500626e-16,
    "99 FCI residual": 2.0196960871277348e-16,
    "99 singlet spatial symmetry": 1.821725679363684e-16,
    "99 MP2 determinant perturbation oracle": 0.0,
    "99 MP2 minimum denominator": 2.27228160503523,
    "99 FCI <= RHF": -0.02394188636845218,
    "99 RHF electron count": 0.0,
    "99 RHF SCF residual": 4.7552933164260536e-12
  },
  "checks": {
    "99 operator assembly": true,
    "99 FCI residual": true,
    "99 singlet spatial symmetry": true,
    "99 MP2 determinant perturbation oracle": true,
    "99 MP2 minimum denominator": true,
    "99 FCI <= RHF": true,
    "99 RHF electron count": true,
    "99 RHF SCF residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/index.json

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

- PySCF Second-order Moller-Plesset perturbation theory [accessed 2026-11-25]. https://pyscf.org/user/mp.html; review_level=selected-official-documentation
公式MP2文書の導入、全/相関エネルギーとスピンの規約を選択閲読。新しい外部エンジン参照は生成しません。

- PySCF official mp2 module source [accessed 2026-11-25]. https://pyscf.org/_modules/pyscf/mp/mp2.html; review_level=selected-official-documentation
公式mp2ソースのkernel53–87行とenergy167–178行で分母・直接/交換項を確認。規約の参照でありコードのコピーや新PySCF参照生成ではありません。

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
公式CI文書の導入とFCIのスピン区分・行列式の例を選択閲読。章全体や実装全体の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# A tiny three-center H3+ RHF / MP2 / FCI example

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

**Methods used**

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [MP2 perturbation theory](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en) (`mp2`)
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) (`configuration-interaction`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-algorithm)

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.


**Problem figure**

![A tiny three-center H3+ RHF / MP2 / FCI example: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-validation)

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en) (`h3plus-mp2-fci`; Same-problem reference · Finite-grid numerical reference)

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.
## Assumptions, units and boundaries

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

**Editorial clarification**

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

## Adopted numerical method

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

## References and validation

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

## Limits

General molecular DFT, CC, large bases and general multireference methods remain unimplemented. Independent operator assembly is not an independent external chemistry-engine scalar reference.

## Stored measurements and decisions

```json
{
  "metrics": {
    "99 operator assembly": 4.440892098500626e-16,
    "99 FCI residual": 2.0196960871277348e-16,
    "99 singlet spatial symmetry": 1.821725679363684e-16,
    "99 MP2 determinant perturbation oracle": 0.0,
    "99 MP2 minimum denominator": 2.27228160503523,
    "99 FCI <= RHF": -0.02394188636845218,
    "99 RHF electron count": 0.0,
    "99 RHF SCF residual": 4.7552933164260536e-12
  },
  "checks": {
    "99 operator assembly": true,
    "99 FCI residual": true,
    "99 singlet spatial symmetry": true,
    "99 MP2 determinant perturbation oracle": true,
    "99 MP2 minimum denominator": true,
    "99 FCI <= RHF": true,
    "99 RHF electron count": true,
    "99 RHF SCF residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/index.json

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

- PySCF Second-order Moller-Plesset perturbation theory [accessed 2026-11-25]. https://pyscf.org/user/mp.html; review_level=selected-official-documentation
Introduction/total vs correlation energy/spin symmetry selected passages.

- PySCF official mp2 module source [accessed 2026-11-25]. https://pyscf.org/_modules/pyscf/mp/mp2.html; review_level=selected-official-documentation
Selected kernel lines53–87 and energy lines167–178: canonical occupied/virtual denominators and direct/exchange contractions. Source read for convention; code not copied into this packet and no fresh PySCF reference.

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
Introduction and FCI/spin-sector examples: all determinants within a finite symmetry sector, diagonalization, Nalpha/Nbeta. Not full chapter or full package source.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
