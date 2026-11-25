# Langevin thermostat / Langevinサーモスタット

Status: educational-example

Langevin thermostat: canonical distributions, timestep bias and correlation: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

Langevin温度制御：正準分布・刻み偏り・時間相関: 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

Langevin thermostat: canonical distributions, timestep bias and correlation: Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

Other names: ランジュバン, ランジュヴァン, friction and noise

Comparison notes: Friction changes dynamical correlations and diffusion. Finite-step sampling errors must be assessed together with the integration scheme.

摩擦は実時間の相関・拡散に影響する。有限刻みでの標本化誤差は積分法と刻み幅も含めて調べる。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1103/PhysRevE.75.056707 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://docs.lammps.org/fix_langevin.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

## Small fixed-input validation supplements

Langevin thermostat: canonical distributions, timestep bias and correlation: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

Langevin温度制御：正準分布・刻み偏り・時間相関: 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

- Langevin thermostat: canonical distributions, timestep bias and correlation: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/
- Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json

- A two-state BO / CP-type model with a short nuclear thermostat coupling: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

- Constraints,centre-of-mass removal and canonical statistics: https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json

Common execution records: [{"id": "langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-harmonic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "csvr-langevin-quartic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "two-state-bo-cp-ou", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "projected-canonical-dof", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; langevin-harmonic, thermostatted-quartic)
- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`; langevin-harmonic)
- [2モードの決定論的温度浴](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-mode-thermostat-model-ja) (`finite-mode-thermostat-model`; thermostatted-quartic)
- [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja) (`two-state-bo-cp-model`; two-state-bo-cp-model)
- [固定線形拘束の正準運動量](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#projected-canonical-model-ja) (`projected-canonical-model`; projected-canonical-dof)

#### 問題の図 (`method-problems-ja`)

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

![調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

- [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja) (`langevin-harmonic`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja) (`csvr-langevin-harmonic`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

![弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

- [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja) (`csvr-langevin-quartic`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

![電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) (`two-state-bo-cp-ou`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

##### [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja) (`projected-canonical-dof`)

![有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。 固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#code-ja)

- [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja) (`projected-canonical-dof`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja) (`langevin-harmonic`)

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照; 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[既存の参照図](/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-measurements)

##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja) (`thermostatted-quartic`)

- [NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja) (`deterministic-thermostat-contrasts`; 同じ問題の参照; 半解析参照)

同じ2モード四次系と調和対照。決定論的浴の短時間・有限標本比較。

[既存の参照図](/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-measurements)

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) (`two-state-bo-cp-model`)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja) (`two-state-bo-cp-ou`; 同じ問題の参照; 半解析参照)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

[既存の参照図](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-measurements)

##### [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#references-ja) (`projected-canonical-dof`)

- [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja) (`projected-canonical-dof`; 同じ問題の参照; 半解析参照)

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

[既存の参照図](/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Langevin温度制御：正準分布・刻み偏り・時間相関 (`langevin-harmonic`)

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

##### CSVRとLangevin：調和2自由度の分布・揺らぎ・相関 (`csvr-langevin-harmonic`)

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

##### 非調和CSVRとLangevin：Boltzmann求積との分布比較 (`csvr-langevin-quartic`)

[非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

##### 2準位模型のBO/CP型連成と短い核熱浴 (`two-state-bo-cp-ou`)

[2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

##### 拘束・重心除去と正準統計 (`projected-canonical-dof`)

[拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Langevin温度制御：正準分布・刻み偏り・時間相関: 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。 CSVRとLangevin：調和2自由度の分布・揺らぎ・相関: 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。 非調和CSVRとLangevin：Boltzmann求積との分布比較: 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; langevin-harmonic, thermostatted-quartic)
- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`; langevin-harmonic)
- [Two-mode deterministic thermostat model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-mode-thermostat-model-en) (`finite-mode-thermostat-model`; thermostatted-quartic)
- [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en) (`two-state-bo-cp-model`; two-state-bo-cp-model)
- [Canonical momentum under fixed linear constraints](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#projected-canonical-model-en) (`projected-canonical-model`; projected-canonical-dof)

#### Problem figures (`method-problems-en`)

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

![Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

- [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en) (`langevin-harmonic`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en) (`csvr-langevin-harmonic`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

![Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en) (`csvr-langevin-quartic`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

![Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) (`two-state-bo-cp-ou`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

##### [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en) (`projected-canonical-dof`)

![Separate effectiveDOF,momentum covariance,transient distributions and time correlations. These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#code-en)

- [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en) (`projected-canonical-dof`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

Separate effectiveDOF,momentum covariance,transient distributions and time correlations.


#### Exact / reference solutions (`method-references-en`)

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en) (`langevin-harmonic`)

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference; Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[Existing reference profile](/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-measurements)

##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en) (`thermostatted-quartic`)

- [NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en) (`deterministic-thermostat-contrasts`; Same-problem reference; Semi-analytic reference)

Same two-mode quartic system plus a harmonic control; short-time and finite-sample deterministic-bath comparisons.

[Existing reference profile](/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-measurements)

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) (`two-state-bo-cp-model`)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en) (`two-state-bo-cp-ou`; Same-problem reference; Semi-analytic reference)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

[Existing reference profile](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-measurements)

##### [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#references-en) (`projected-canonical-dof`)

- [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-projected-canonical-dof-en) (`projected-canonical-dof`; Same-problem reference; Semi-analytic reference)

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

[Existing reference profile](/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Langevin thermostat: canonical distributions, timestep bias and correlation (`langevin-harmonic`)

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

##### CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes (`csvr-langevin-harmonic`)

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

##### Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature (`csvr-langevin-quartic`)

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

##### A two-state BO / CP-type model with a short nuclear thermostat coupling (`two-state-bo-cp-ou`)

[A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

##### Constraints,centre-of-mass removal and canonical statistics (`projected-canonical-dof`)

[Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

Separate effectiveDOF,momentum covariance,transient distributions and time correlations.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Langevin thermostat: canonical distributions, timestep bias and correlation: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations. CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations. Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py)

###### Package tests

- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
