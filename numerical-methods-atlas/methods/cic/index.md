# Cloud-in-cell assignment and interpolation / Cloud-in-cellの割当てと補間

Status: educational-example

Read about Cloud-in-cell assignment and interpolation, follow the original references and inspect related educational code and checks.

「Cloud-in-cellの割当てと補間」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: CIC法, cloud in cell

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py

- Reference: https://doi.org/10.1038/324446a0 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(87)90140-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/astro-ph/0505010 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Common execution records: [{"id": "periodic-particles", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-particles-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-particles-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`; periodic-particles)
- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; periodic-particles)

#### 問題の図 (`method-problems-ja`)

##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) (`periodic-particles`)

![共有図の周期PM部分。孤立ツリーの比較は別問題です。](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#code-ja)

- [周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) (`periodic-particles`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#references-ja) (`periodic-particles`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 周期PM粒子群：質量・内力・格子場 (`periodic-particles`)

[周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_particle_gravity.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`; periodic-particles)
- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; periodic-particles)

#### Problem figures (`method-problems-en`)

##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) (`periodic-particles`)

![Periodic-PM part of a shared figure; isolated-tree comparisons are a separate problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#code-en)

- [Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) (`periodic-particles`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#references-en) (`periodic-particles`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Periodic PM particles: mass, internal force and mesh field (`periodic-particles`)

[Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_particle_gravity.py
```
