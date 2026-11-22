# Particle-in-cell / PIC / Particle-in-Cell（PIC）

Status: educational-example

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

Finite amplitude and finite particles leave an error floor. Nonlinear instabilities, Landau damping, collisions, electromagnetic/relativistic PIC and open particle boundaries are unvalidated.

Other names: PIC法, particle in cell, 粒子セル法, 粒子インセル法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/pic/



- Reference: https://doi.org/10.1063/1.1706638 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1201/9780367806934 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

- Cold-plasma oscillation with electrostatic CIC PIC: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "pic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; cold-plasma-pic)

#### 問題の図 (`method-problems-ja`)

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

- [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) (`pic`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。


#### 厳密解・参照解 (`method-references-ja`)

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) (`cold-plasma-pic`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pic/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### CIC静電PICの冷たいプラズマ振動 (`pic`)

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

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

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; cold-plasma-pic)

#### Problem figures (`method-problems-en`)

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

- [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) (`pic`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.


#### Exact / reference solutions (`method-references-en`)

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) (`cold-plasma-pic`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/pic/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Cold-plasma oscillation with electrostatic CIC PIC (`pic`)

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

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
