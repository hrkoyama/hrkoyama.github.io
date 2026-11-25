# Gillespie direct stochastic simulation (SSA) / Gillespie直接確率シミュレーション（SSA）

Status: educational-example

Draw an exponential waiting time and a reaction channel from state-dependent propensities to generate a continuous-time reaction path. The fixed example is immigration–death.

状態ごとの反応propensityから指数待ち時間と反応種を抽選し、連続時間の反応軌道を生成します。固定例は移入–死亡反応です。

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

Other names: Gillespie SSA, direct method, chemical master equation, chemical reaction SSA, 確率反応シミュレーション

Comparison notes: Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/#immigration-death-ssa
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/#immigration-death-ssa



- Reference: https://doi.org/10.1021/j100540a008 — Selected original article pp2343–2345, section III A–C, equations8–21 and algorithm0–3, carried forward from documented 2026-11-24 reading. Remaining article and earlier1976 derivation unread.

## Small fixed-input validation supplements

Separate one displayed path from12,288fixed ensemble paths.

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

- Immigration–death SSA: exact transient laws: https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json

Common execution records: [{"id": "immigration-death-ssa", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain the fixed immigration–death inputs, references and acceptance contract, retaining unmet study goals.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [化学マスター方程式とGillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja) (`bio-chemical-master`; immigration-death-ssa)
- [移入–死亡反応と厳密過渡法則](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#immigration-death-model-ja) (`immigration-death-model`; immigration-death-ssa)

#### 問題の図 (`method-problems-ja`)

##### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`)

![1本の軌跡と12,288本の固定アンサンブルを分けて検証します。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#code-ja)

- [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#references-ja) (`immigration-death-ssa`)

- [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja) (`immigration-death-ssa`; 同じ問題の参照; 解析参照)

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

[既存の参照図](/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/#immigration-death-ssa)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 移入–死亡SSA：有限時刻の厳密分布 (`immigration-death-ssa`)

[移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Chemical master equation and Gillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en) (`bio-chemical-master`; immigration-death-ssa)
- [Immigration–death reaction and exact transient law](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en) (`immigration-death-model`; immigration-death-ssa)

#### Problem figures (`method-problems-en`)

##### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) (`immigration-death-ssa`)

![Separate one displayed path from12,288fixed ensemble paths. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#code-en)

- [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en) (`immigration-death-ssa`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

Separate one displayed path from12,288fixed ensemble paths.


#### Exact / reference solutions (`method-references-en`)

##### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#references-en) (`immigration-death-ssa`)

- [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en) (`immigration-death-ssa`; Same-problem reference; Analytic reference)

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

[Existing reference profile](/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/#immigration-death-ssa)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Immigration–death SSA: exact transient laws (`immigration-death-ssa`)

[Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

Separate one displayed path from12,288fixed ensemble paths.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Separate one displayed path from12,288fixed ensemble paths.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)

###### Package tests

- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
