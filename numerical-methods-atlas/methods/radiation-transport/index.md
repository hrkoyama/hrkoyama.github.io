# Radiation transport and moment methods / 放射輸送・モーメント法

Status: educational-example

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

Other names: 放射輸送法, radiative transfer, radiation transport, 放射モーメント法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/



- Reference: https://doi.org/10.1016/0022-4073(84)90112-2 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

- Discrete-ordinate radiation transport through an absorbing slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "radiation-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) (`absorbing-slab`)

![光学的厚さ0.7の純吸収平板。32〜512セルのBeer–Lambert参照への空間誤差と、厳密セル内伝播を使う4〜32方向の角度誤差を分けた保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#code-ja)

- [純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja) (`radiation-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#references-ja) (`absorbing-slab`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 純吸収平板の離散座標放射輸送 (`radiation-transport`)

[純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

![Pure-absorption slab of optical depth 0.7: stored 32–512-cell spatial errors versus Beer–Lambert and a separate 4–32-ordinate angular sweep using exact cell propagation.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

- [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en) (`radiation-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.


#### Exact / reference solutions (`method-references-en`)

##### [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#references-en) (`absorbing-slab`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Discrete-ordinate radiation transport through an absorbing slab (`radiation-transport`)

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)

###### Package tests

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
