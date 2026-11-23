# Slab electrostatics and 2D-periodic Ewald / スラブ静電場と2次元周期Ewald

Status: educational-example

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series. Additional fixed examples: Neutral rectangular slab: genuine2P reference and YB. See each release for assumptions and checked scope.

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。 追加固定例：中性長方形スラブ：真2P参照とYB補正。条件と検証範囲は各配布版で確認してください。

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected. Additional fixed examples: Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

Other names: 2D periodic Ewald, 2次元周期Ewald, slab Ewald, スラブEwald法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/slab-ewald/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/slab-ewald/



- Reference: https://doi.org/10.1063/1.479595 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1002/andp.19213690304 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Additional fixed examples: Neutral rectangular slab: genuine2P reference and YB. See each release for assumptions and checked scope.

追加固定例：中性長方形スラブ：真2P参照とYB補正。条件と検証範囲は各配布版で確認してください。

- Neutral rectangular slab: genuine2P reference and YB: https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json

Common execution records: [{"id": "neutral-slab-yb", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en"}, "kind": "dedicated-supplement"}]

Next: The fixed neutral slab is verified. Validate new conditions,references and criteria separately when extending it.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Coulomb静電場と混合周期境界](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja) (`coulomb-electrostatics`; neutral-slab-yb)

#### 問題の図 (`method-problems-ja`)

##### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#code-ja)

- [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。


#### 厳密解・参照解 (`method-references-ja`)

##### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#references-ja) (`neutral-slab-yb`)

- [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja) (`neutral-slab-yb`; 同じ問題の参照; 半解析参照)

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

[既存の参照図](/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/slab-ewald/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 中性長方形スラブ：真2P参照とYB補正 (`neutral-slab-yb`)

[中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：中性長方形スラブ：真2P参照とYB補正。条件と検証範囲は各配布版で確認してください。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-23/slab-ewald/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/run.py)
- [/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py)
- [/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py)
- [/code/validated-examples/2026-11-23/slab-ewald/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/experiments.py)
- [/code/validated-examples/2026-11-23/slab-ewald/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/protocol.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-23/slab-ewald/test_slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/test_slab.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Coulomb electrostatics with mixed periodic boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en) (`coulomb-electrostatics`; neutral-slab-yb)

#### Problem figures (`method-problems-en`)

##### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) (`neutral-slab-yb`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#code-en)

- [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en) (`neutral-slab-yb`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.


#### Exact / reference solutions (`method-references-en`)

##### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#references-en) (`neutral-slab-yb`)

- [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en) (`neutral-slab-yb`; Same-problem reference; Semi-analytic reference)

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

[Existing reference profile](/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/slab-ewald/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Neutral rectangular slab: genuine2P reference and YB (`neutral-slab-yb`)

[Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Neutral rectangular slab: genuine2P reference and YB. See each release for assumptions and checked scope.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

###### Related source

- [/code/validated-examples/2026-11-23/slab-ewald/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/run.py)
- [/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py)
- [/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py)
- [/code/validated-examples/2026-11-23/slab-ewald/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/experiments.py)
- [/code/validated-examples/2026-11-23/slab-ewald/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/protocol.py)

###### Package tests

- [/code/validated-examples/2026-11-23/slab-ewald/test_slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/test_slab.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
