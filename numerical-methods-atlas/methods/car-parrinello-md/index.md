# Car–Parrinello molecular dynamics / CPMD / カー–パリネロ法（CPMD）

Status: educational-example

Assign fictitious inertia to orbitals and propagate an orthonormality-constrained extended system with the nuclei.

電子軌道に仮想質量を与え、直交制約付きの拡張系で核と同時に進める。

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

Other names: CPMD, Car Parrinello, Car–Parrinello, Car Parrinello MD, カー・パリネロ法, カーパリネロ法, 第一原理分子動力学

Comparison notes: Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md



- Reference: https://doi.org/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.

## Small fixed-input validation supplements

Restricted fixed examples: A two-state BO / CP-type model with a short nuclear thermostat coupling. Saved-reference audits are not new electronic calculations.

固定した小規模例に限定：2準位模型のBO/CP型連成と短い核熱浴。保存参照監査は新しい電子計算ではありません。

- A two-state BO / CP-type model with a short nuclear thermostat coupling: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "two-state-bo-cp-ou", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain these fixed educational examples; broader extensions require a separately specified need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja) (`two-state-bo-cp-model`; two-state-bo-cp-model)

#### 問題の図 (`method-problems-ja`)

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

![電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) (`two-state-bo-cp-ou`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) (`two-state-bo-cp-model`)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja) (`two-state-bo-cp-ou`; 同じ問題の参照; 半解析参照)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

[既存の参照図](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 2準位模型のBO/CP型連成と短い核熱浴 (`two-state-bo-cp-ou`)

[2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した小規模例に限定：2準位模型のBO/CP型連成と短い核熱浴。保存参照監査は新しい電子計算ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en) (`two-state-bo-cp-model`; two-state-bo-cp-model)

#### Problem figures (`method-problems-en`)

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

![Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) (`two-state-bo-cp-ou`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.


#### Exact / reference solutions (`method-references-en`)

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) (`two-state-bo-cp-model`)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en) (`two-state-bo-cp-ou`; Same-problem reference; Semi-analytic reference)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

[Existing reference profile](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### A two-state BO / CP-type model with a short nuclear thermostat coupling (`two-state-bo-cp-ou`)

[A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Restricted fixed examples: A two-state BO / CP-type model with a short nuclear thermostat coupling. Saved-reference audits are not new electronic calculations.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### Package tests

- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
