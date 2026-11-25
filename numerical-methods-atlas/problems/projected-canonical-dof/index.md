# 拘束・重心除去と正準統計 / Constraints,centre-of-mass removal and canonical statistics

https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/

## 日本語

[有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。 固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostat-constraint-controls/#projected-canonical-dof) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#projected-canonical-dof)

### 方程式・問題の定義

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

#### [固定線形拘束の正準運動量](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#projected-canonical-model-ja)

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

#### 拘束・重心除去と正準統計

補助実行例 · 実行例の定義・検証式

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。

### 厳密解・参照解

Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。

#### [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-measurements)

半解析解 · 同じ問題の参照

Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C);\quad \mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)

共通の調和ポテンシャル中の1次元3粒子で質量1/2/3、kBT=1。無拘束・COM・COM相対・冗長行の等価拘束で有効自由度3/2/1/1、各1,024標本を比較します。固定線形拘束Cq=0、CM⁻¹p=0を用い、冗長行は同じ接空間上で比較します。

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

#### 拘束・重心除去と正準統計

Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja)

### 計算法

質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja)

補助実行例

有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)

## English

[Separate effectiveDOF,momentum covariance,transient distributions and time correlations. These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostat-constraint-controls/#projected-canonical-dof) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#projected-canonical-dof-en)

### Equations and problem definitions

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.

#### [Canonical momentum under fixed linear constraints](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#projected-canonical-model-en)

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

#### Constraints,centre-of-mass removal and canonical statistics

Supplementary execution example · Example definition or validation formula

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

Separate effectiveDOF,momentum covariance,transient distributions and time correlations.

### Exact and reference solutions

Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.

#### [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-measurements)

Semi-analytic reference · Reference for the same problem

Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C);\quad \mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas. Dimensionless; masses 1/2/3 and kBT=1. Fixed linear constraints Cq=0 and CM⁻¹p=0; redundant rows are compared on the same tangent space.

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

#### Constraints,centre-of-mass removal and canonical statistics

Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en)

### Numerical methods

Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.

- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en)

Supplementary execution example

Separate effectiveDOF,momentum covariance,transient distributions and time correlations.

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)
