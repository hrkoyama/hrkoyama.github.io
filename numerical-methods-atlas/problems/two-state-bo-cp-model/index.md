# 2準位模型のBO/CP型連成と短い核熱浴 / A two-state BO / CP-type model with a short nuclear thermostat coupling

https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/

## 日本語

[電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/#two-state-bo-cp-ou) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#two-state-bo-cp-model)

### 方程式・問題の定義

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

#### [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja)

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

#### 2準位模型のBO/CP型連成と短い核熱浴

補助実行例 · 実行例の定義・検証式

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

### 厳密解・参照解

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

#### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-measurements)

半解析解 · 同じ問題の参照

H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T;\quad E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2};\quad M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta);\quad V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

#### 2準位模型のBO/CP型連成と短い核熱浴

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja)

### 計算法

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

- [Born–Oppenheimer分子動力学（BOMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [カー–パリネロ法（CPMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja)

補助実行例

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

短い自作教育模型です。第一原理・長いNVE・一般CPMD・正準平衡・エルゴード性の成功は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

## English

[Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/#two-state-bo-cp-ou) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#two-state-bo-cp-model-en)

### Equations and problem definitions

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

#### [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en)

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

#### A two-state BO / CP-type model with a short nuclear thermostat coupling

Supplementary execution example · Example definition or validation formula

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

### Exact and reference solutions

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

#### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-measurements)

Semi-analytic reference · Reference for the same problem

H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T;\quad E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2};\quad M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta);\quad V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

#### A two-state BO / CP-type model with a short nuclear thermostat coupling

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en)

### Numerical methods

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

- [Born–Oppenheimer molecular dynamics / BOMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Car–Parrinello molecular dynamics / CPMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en)

Supplementary execution example

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Long first-principles NVE and general electronic/nuclear thermostat equilibration remain deferred. No material prediction, multi-orbital CPMD or canonical/ergodic sampling certificate.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
