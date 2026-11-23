# Mean-preserving positive-state scaling / 平均を保つ正値状態スケーリング

Status: educational-example

Read about Mean-preserving positive-state scaling, follow the original references and inspect related educational code and checks.

「平均を保つ正値状態スケーリング」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

Distinguish the earlier standalone helper checks from the new scoped one-dimensional MUSCL/Lax–Friedrichs/SSPRK(3,3) update. Its stage positivity is checked under the stated CFL/wave-speed conditions and fixed inputs, without certifying all existing Euler, WENO, DG or MHD updates.

Other names: 正値性スケーリング, 正値性保持スケーリング, positive state scaling, mean preserving scaling

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced-limiters/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced-limiters/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py

- Reference: https://doi.org/10.1090/S0025-5718-1989-0983311-4 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2010.08.016 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity.

追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。

- Euler double rarefaction: positivity at every stage: https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json

Common execution records: [{"id": "euler-double-rarefaction-positivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; double-rarefaction)

#### 問題の図 (`method-problems-ja`)

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

従来のGodunov／HLLEプレビューと、追加のMUSCL・Lax–Friedrichs・平均保存スケーリング・SSPRK(3,3)固定入力は別の実行例です。段階正値性の条件は追加版の説明・契約・全段ログに限定します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

- [Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) (`euler-double-rarefaction-positivity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) (`double-rarefaction`)

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced-limiters/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Euler二重膨張波：段階ごとの正値性 (`euler-double-rarefaction-positivity`)

[Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_limiters.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; double-rarefaction)

#### Problem figures (`method-problems-en`)

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

The earlier Godunov/HLLE preview and the new MUSCL/Lax–Friedrichs/mean-preserving-scaling/SSPRK(3,3) run are separate execution records. Stage-positivity conditions are scoped to the additional release, its contract and all-stage diagnostics.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

- [Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) (`euler-double-rarefaction-positivity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.


#### Exact / reference solutions (`method-references-en`)

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) (`double-rarefaction`)

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference; Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced-limiters/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Euler double rarefaction: positivity at every stage (`euler-double-rarefaction-positivity`)

[Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_limiters.py
```
