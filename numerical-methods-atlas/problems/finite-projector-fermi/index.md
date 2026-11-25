# 3平面波の非局所projectorと有限温度占有 / A three-wave periodic projector and Fermi-occupation model

https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/

## 日本語

[3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/#periodic-projector-occupations) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#finite-projector-fermi)

### 方程式・問題の定義

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

#### [3平面波・非局所核と平均Fermi占有](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja)

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

#### 3平面波の非局所projectorと有限温度占有

補助実行例 · 実行例の定義・検証式

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

### 厳密解・参照解

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

#### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-measurements)

半解析解 · 同じ問題の参照

H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R};\quad f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5;\quad F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

#### 3平面波の非局所projectorと有限温度占有

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja)

### 計算法

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja)

補助実行例

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

元素に合わせたノルム保存擬ポテンシャルではありません。実金属、自己無撞着Hartree/XC、一般材料や長時間MDは未検証です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

## English

[Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/#periodic-projector-occupations) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#finite-projector-fermi-en)

### Equations and problem definitions

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

#### [Three-wave nonlocal kernel and mean Fermi occupations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en)

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

#### A three-wave periodic projector and Fermi-occupation model

Supplementary execution example · Example definition or validation formula

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

### Exact and reference solutions

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

#### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-measurements)

Semi-analytic reference · Reference for the same problem

H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R};\quad f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5;\quad F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

#### A three-wave periodic projector and Fermi-occupation model

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en)

### Numerical methods

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en)

Supplementary execution example

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The authored rank-one kernel is not an element-fitted norm-conserving pseudopotential. No self-consistent Hartree/XC, real metal, general material or long-time MD success.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
