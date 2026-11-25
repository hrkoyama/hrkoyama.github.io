# 保存周期Heエネルギー・力の参照台帳

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

**使用手法**

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-algorithm)

保存エネルギー差分・解析力・Gaussian/PW比較の算術を再照合します。

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。


**問題の図**

![保存周期Heエネルギー・力の参照台帳：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-validation)

元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。
## 前提・単位・境界

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。

**編集上の補足**

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

## 採用した計算法

保存エネルギー差分・解析力・Gaussian/PW比較の算術を再照合します。

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

## 比較・検証

元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。

## 確認の限界

新電子計算や基底・k点・cutoff走査は0回です。局所Heの成功を非局所擬ポテンシャルへ拡張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "100 saved FD arithmetic 0": 0.0,
    "100 unchanged FD science bound 0": 8.486369273974503e-09,
    "100 saved FD arithmetic 1": 0.0,
    "100 unchanged FD science bound 1": 1.4108486323660685e-08,
    "100 saved FD arithmetic 2": 0.0,
    "100 unchanged FD science bound 2": 2.1580722472935854e-08,
    "100 saved FD arithmetic 3": 0.0,
    "100 unchanged FD science bound 3": 1.1233197302895626e-08,
    "100 saved FD arithmetic 4": 0.0,
    "100 unchanged FD science bound 4": 1.818304432021911e-08,
    "100 saved FD arithmetic 5": 0.0,
    "100 unchanged FD science bound 5": 2.3223412720652092e-08,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": 7.28156560618684e-05,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": 7.395629375217538e-05,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": 7.538249895754426e-05,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": 0.00017168416810697806
  },
  "checks": {
    "100 saved FD arithmetic 0": true,
    "100 unchanged FD science bound 0": true,
    "100 saved FD arithmetic 1": true,
    "100 unchanged FD science bound 1": true,
    "100 saved FD arithmetic 2": true,
    "100 unchanged FD science bound 2": true,
    "100 saved FD arithmetic 3": true,
    "100 unchanged FD science bound 3": true,
    "100 saved FD arithmetic 4": true,
    "100 unchanged FD science bound 4": true,
    "100 saved FD arithmetic 5": true,
    "100 unchanged FD science bound 5": true,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/index.json

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

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
公式文書の分離形・ノルム保存・GTH形式と近似の導入。自作rank-one核を元素適合のノルム保存ポテンシャルと呼びません。

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Immutable periodic-helium energy and force reference audit

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

**Methods used**

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-algorithm)

Audit arithmetic of saved energy differences, analytic forces and Gaussian/PW comparisons under the original bounds.

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.


**Problem figure**

![Immutable periodic-helium energy and force reference audit: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-validation)

Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.
## Assumptions, units and boundaries

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.

**Editorial clarification**

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

## Adopted numerical method

Audit arithmetic of saved energy differences, analytic forces and Gaussian/PW comparisons under the original bounds.

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

## References and validation

Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.

## Limits

No new SCF/DFTK/PySCF run, no basis/k/cutoff scans; preserve all old values and criteria. The He GTH is local-only, so its saved success does not test nonlocal projectors.

## Stored measurements and decisions

```json
{
  "metrics": {
    "100 saved FD arithmetic 0": 0.0,
    "100 unchanged FD science bound 0": 8.486369273974503e-09,
    "100 saved FD arithmetic 1": 0.0,
    "100 unchanged FD science bound 1": 1.4108486323660685e-08,
    "100 saved FD arithmetic 2": 0.0,
    "100 unchanged FD science bound 2": 2.1580722472935854e-08,
    "100 saved FD arithmetic 3": 0.0,
    "100 unchanged FD science bound 3": 1.1233197302895626e-08,
    "100 saved FD arithmetic 4": 0.0,
    "100 unchanged FD science bound 4": 1.818304432021911e-08,
    "100 saved FD arithmetic 5": 0.0,
    "100 unchanged FD science bound 5": 2.3223412720652092e-08,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": 7.28156560618684e-05,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": 7.395629375217538e-05,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": 7.538249895754426e-05,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": 0.00017168416810697806
  },
  "checks": {
    "100 saved FD arithmetic 0": true,
    "100 unchanged FD science bound 0": true,
    "100 saved FD arithmetic 1": true,
    "100 unchanged FD science bound 1": true,
    "100 saved FD arithmetic 2": true,
    "100 unchanged FD science bound 2": true,
    "100 saved FD arithmetic 3": true,
    "100 unchanged FD science bound 3": true,
    "100 saved FD arithmetic 4": true,
    "100 unchanged FD science bound 4": true,
    "100 saved FD arithmetic 5": true,
    "100 unchanged FD science bound 5": true,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/index.json

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

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
Official separable Kleinman-Bylander/norm-conserving/GTH formats and approximation limits introduction. Our rank-one kernel is authored and is not an element-fitted norm-conserving potential.

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
