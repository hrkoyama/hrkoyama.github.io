# 3平面波の非局所projectorと有限温度占有

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-algorithm)

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

- [3平面波・非局所核と平均Fermi占有](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja) (`finite-projector-fermi-model`)

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。


**問題の図**

![3平面波の非局所projectorと有限温度占有：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) (`finite-projector-fermi`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-validation)

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja) (`periodic-projector-occupations`; 同じ問題の参照 · 半解析参照)

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。
## 前提・単位・境界

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

**編集上の補足**

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

## 採用した計算法

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

## 比較・検証

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

## 確認の限界

元素に合わせたノルム保存擬ポテンシャルではありません。実金属、自己無撞着Hartree/XC、一般材料や長時間MDは未検証です。

## 保存実測値と判定

```json
{
  "metrics": {
    "101 Hermiticity 0": 3.58464566598299e-18,
    "101 residual 0": 2.751670084160633e-16,
    "101 independent cubic 0": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 0": 0.0,
    "101 Hermiticity 1": 3.58464566598299e-18,
    "101 residual 1": 2.7503882064100795e-16,
    "101 independent cubic 1": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 1": 0.0,
    "101 fixed electron number": 6.661338147750939e-16,
    "101 lower occupation": 4.6784131873466673e-05,
    "101 upper occupation": 1.4444120001743874,
    "101 nonnegative entropy": 1.4360712457901055,
    "101 finest free-energy force difference": 1.721169318180671e-10
  },
  "checks": {
    "101 Hermiticity 0": true,
    "101 residual 0": true,
    "101 independent cubic 0": true,
    "101 fixed-case cubic clamp activation 0": true,
    "101 Hermiticity 1": true,
    "101 residual 1": true,
    "101 independent cubic 1": true,
    "101 fixed-case cubic clamp activation 1": true,
    "101 fixed electron number": true,
    "101 lower occupation": true,
    "101 upper occupation": true,
    "101 nonnegative entropy": true,
    "101 finest free-energy force difference": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/index.json

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

- DFTK periodic problems and plane-wave discretisations [accessed 2026-11-25]. https://docs.dftk.org/stable/guide/periodic_problems/; review_level=selected-official-documentation
公式周期問題ガイドのBloch・周期演算子・平面波の選択箇所。物質の数値計算は再現していません。

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
公式文書の分離形・ノルム保存・GTH形式と近似の導入。自作rank-one核を元素適合のノルム保存ポテンシャルと呼びません。

- DFTK Temperature and metallic systems [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/metallic_systems/; review_level=selected-official-documentation
公式金属例のFermi温度・部分占有・Entropy項・高速例の未収束警告のみ。Mg計算や新k/基底/カットオフ走査は行いません。

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
NumPy2.0公式の引数、昇順固有値、規格化した固有ベクトル、Hermitian三角格納、LinAlgError、LAPACKの説明を選択閲読。全LAPACK実装・誤差証明の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# A three-wave periodic projector and Fermi-occupation model

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-algorithm)

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

- [Three-wave nonlocal kernel and mean Fermi occupations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en) (`finite-projector-fermi-model`)

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.


**Problem figure**

![A three-wave periodic projector and Fermi-occupation model: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) (`finite-projector-fermi`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-validation)

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en) (`periodic-projector-occupations`; Same-problem reference · Semi-analytic reference)

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.
## Assumptions, units and boundaries

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

**Editorial clarification**

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

## Adopted numerical method

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

## References and validation

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

## Limits

The authored rank-one kernel is not an element-fitted norm-conserving pseudopotential. No self-consistent Hartree/XC, real metal, general material or long-time MD success.

## Stored measurements and decisions

```json
{
  "metrics": {
    "101 Hermiticity 0": 3.58464566598299e-18,
    "101 residual 0": 2.751670084160633e-16,
    "101 independent cubic 0": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 0": 0.0,
    "101 Hermiticity 1": 3.58464566598299e-18,
    "101 residual 1": 2.7503882064100795e-16,
    "101 independent cubic 1": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 1": 0.0,
    "101 fixed electron number": 6.661338147750939e-16,
    "101 lower occupation": 4.6784131873466673e-05,
    "101 upper occupation": 1.4444120001743874,
    "101 nonnegative entropy": 1.4360712457901055,
    "101 finest free-energy force difference": 1.721169318180671e-10
  },
  "checks": {
    "101 Hermiticity 0": true,
    "101 residual 0": true,
    "101 independent cubic 0": true,
    "101 fixed-case cubic clamp activation 0": true,
    "101 Hermiticity 1": true,
    "101 residual 1": true,
    "101 independent cubic 1": true,
    "101 fixed-case cubic clamp activation 1": true,
    "101 fixed electron number": true,
    "101 lower occupation": true,
    "101 upper occupation": true,
    "101 nonnegative entropy": true,
    "101 finest free-energy force difference": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/index.json

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

- DFTK periodic problems and plane-wave discretisations [accessed 2026-11-25]. https://docs.dftk.org/stable/guide/periodic_problems/; review_level=selected-official-documentation
Selected displayed Bloch/periodic operator/plane-wave basis context; no material calculations reproduced.

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
Official separable Kleinman-Bylander/norm-conserving/GTH formats and approximation limits introduction. Our rank-one kernel is authored and is not an element-fitted norm-conserving potential.

- DFTK Temperature and metallic systems [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/metallic_systems/; review_level=selected-official-documentation
Selected Fermi-Dirac smearing temperature, partial occupations, explicit unconverged fast-example warning and energy Entropy term. No magnesium run, no new k/basis/cutoff scans.

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
Signature, Hermitian lower-triangle handling, all ascending eigenvalues/normalized columns, LinAlgError and LAPACK syevd/heevd notes.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
