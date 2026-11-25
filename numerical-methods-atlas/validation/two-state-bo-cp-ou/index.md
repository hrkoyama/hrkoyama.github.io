# 2準位模型のBO/CP型連成と短い核熱浴

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

**使用手法**

- [Born–Oppenheimer分子動力学（BOMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja) (`born-oppenheimer-md`)
- [カー–パリネロ法（CPMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja) (`car-parrinello-md`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-algorithm)

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

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

- [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja) (`two-state-bo-cp-model`)

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。


**問題の図**

![2準位模型のBO/CP型連成と短い核熱浴：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-validation)

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja) (`two-state-bo-cp-ou`; 同じ問題の参照 · 半解析参照)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。
## 前提・単位・境界

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

**編集上の補足**

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

## 採用した計算法

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

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

## 比較・検証

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

## 確認の限界

短い自作教育模型です。第一原理・長いNVE・一般CPMD・正準平衡・エルゴード性の成功は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "95 bo-0 NVE extended energy drift": 4.54374582403716e-08,
    "95 bo-1 NVE extended energy drift": 1.135934568630148e-08,
    "95 bo-2 NVE extended energy drift": 2.8398352558411943e-09,
    "95 cp-mu004-0 NVE extended energy drift": 4.543430420778094e-08,
    "95 cp-mu004-1 NVE extended energy drift": 1.1358568974273453e-08,
    "95 cp-mu004-2 NVE extended energy drift": 2.839641743968002e-09,
    "95 cp-mu001 NVE extended energy drift": 2.8397284523862254e-09,
    "95 bo finest RK4 state comparison": 5.443721431889809e-09,
    "95 cp-mu004 finest RK4 state comparison": 9.898870595217574e-08,
    "95 bo fixed RK4 companion sensitivity": 2.5547594848822963e-15,
    "95 cp-mu004 fixed RK4 companion sensitivity": 1.2252872249276024e-15,
    "95 OU extended energy minus measured heat": 4.47292801061816e-09,
    "95 OU conditional temperature variance identity": 0.0,
    "95 normalized orbital": 2.220446049250313e-16
  },
  "checks": {
    "95 bo-0 NVE extended energy drift": true,
    "95 bo-1 NVE extended energy drift": true,
    "95 bo-2 NVE extended energy drift": true,
    "95 cp-mu004-0 NVE extended energy drift": true,
    "95 cp-mu004-1 NVE extended energy drift": true,
    "95 cp-mu004-2 NVE extended energy drift": true,
    "95 cp-mu001 NVE extended energy drift": true,
    "95 bo finest RK4 state comparison": true,
    "95 cp-mu004 finest RK4 state comparison": true,
    "95 bo fixed RK4 companion sensitivity": true,
    "95 cp-mu004 fixed RK4 companion sensitivity": true,
    "95 OU extended energy minus measured heat": true,
    "95 OU conditional temperature variance identity": true,
    "95 normalized orbital": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/index.json

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

- Unified Approach for Molecular Dynamics and Density-Functional Theory [accessed 2026-11-25]. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471; review_level=abstract-and-metadata
出版社の題名・著者・日付・DOIと抄録のみ。PDF本文・式は今回読んでおらず、Si計算やこの自作模型を原論文から再現したとは主張しません。

- Quantum ESPRESSO cp.x input description [accessed 2026-11-25]. https://www.quantum-espresso.org/Doc/INPUT_CP.html; review_level=selected-official-documentation
公式cp.xのemass・直交化の選択箇所のみ。この無次元電子角の架空質量を同じ物理規約へ読み替えません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# A two-state BO / CP-type model with a short nuclear thermostat coupling

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

**Methods used**

- [Born–Oppenheimer molecular dynamics / BOMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en) (`born-oppenheimer-md`)
- [Car–Parrinello molecular dynamics / CPMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en) (`car-parrinello-md`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-algorithm)

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

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

- [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en) (`two-state-bo-cp-model`)

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.


**Problem figure**

![A two-state BO / CP-type model with a short nuclear thermostat coupling: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-validation)

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en) (`two-state-bo-cp-ou`; Same-problem reference · Semi-analytic reference)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.
## Assumptions, units and boundaries

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

**Editorial clarification**

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

## Adopted numerical method

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

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

## References and validation

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

## Limits

Long first-principles NVE and general electronic/nuclear thermostat equilibration remain deferred. No material prediction, multi-orbital CPMD or canonical/ergodic sampling certificate.

## Stored measurements and decisions

```json
{
  "metrics": {
    "95 bo-0 NVE extended energy drift": 4.54374582403716e-08,
    "95 bo-1 NVE extended energy drift": 1.135934568630148e-08,
    "95 bo-2 NVE extended energy drift": 2.8398352558411943e-09,
    "95 cp-mu004-0 NVE extended energy drift": 4.543430420778094e-08,
    "95 cp-mu004-1 NVE extended energy drift": 1.1358568974273453e-08,
    "95 cp-mu004-2 NVE extended energy drift": 2.839641743968002e-09,
    "95 cp-mu001 NVE extended energy drift": 2.8397284523862254e-09,
    "95 bo finest RK4 state comparison": 5.443721431889809e-09,
    "95 cp-mu004 finest RK4 state comparison": 9.898870595217574e-08,
    "95 bo fixed RK4 companion sensitivity": 2.5547594848822963e-15,
    "95 cp-mu004 fixed RK4 companion sensitivity": 1.2252872249276024e-15,
    "95 OU extended energy minus measured heat": 4.47292801061816e-09,
    "95 OU conditional temperature variance identity": 0.0,
    "95 normalized orbital": 2.220446049250313e-16
  },
  "checks": {
    "95 bo-0 NVE extended energy drift": true,
    "95 bo-1 NVE extended energy drift": true,
    "95 bo-2 NVE extended energy drift": true,
    "95 cp-mu004-0 NVE extended energy drift": true,
    "95 cp-mu004-1 NVE extended energy drift": true,
    "95 cp-mu004-2 NVE extended energy drift": true,
    "95 cp-mu001 NVE extended energy drift": true,
    "95 bo finest RK4 state comparison": true,
    "95 cp-mu004 finest RK4 state comparison": true,
    "95 bo fixed RK4 companion sensitivity": true,
    "95 cp-mu004 fixed RK4 companion sensitivity": true,
    "95 OU extended energy minus measured heat": true,
    "95 OU conditional temperature variance identity": true,
    "95 normalized orbital": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/index.json

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

- Unified Approach for Molecular Dynamics and Density-Functional Theory [accessed 2026-11-25]. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471; review_level=abstract-and-metadata
Publisher title/authors/date/DOI and abstract only. Full PDF/equations not read; this is not a reproduction of the silicon calculation.

- Quantum ESPRESSO cp.x input description [accessed 2026-11-25]. https://www.quantum-espresso.org/Doc/INPUT_CP.html; review_level=selected-official-documentation
Selected emass/orthogonalization and CP context. Its physical mass conventions are not silently assigned to the authored dimensionless angle mass.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
