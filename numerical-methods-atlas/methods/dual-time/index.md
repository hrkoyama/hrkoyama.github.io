# Dual time stepping / 二重時間積分

Status: educational-example

Read about Dual time stepping, follow the original references and inspect related educational code and checks.

「二重時間積分」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: dual time stepping, デュアルタイムステッピング, 二重時間積分法, 二重時間法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/roe_properties.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py

- Reference: https://doi.org/10.1016/0021-9991(87)90084-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.2514/6.1991-1596 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(81)90128-5 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1137/0725021 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(91)90211-3 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2007.11.003 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/dual-time/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

この手法に対応付けられたテスト問題の図は未登録です。

#### 厳密解・参照解 (`method-references-ja`)

この手法の問題図に結び付く参照資料は未登録です。
##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/roe_properties.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/roe_properties.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_priority.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_priority.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_shock_priority.py tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

No test-problem figure is registered for this method.

#### Exact / reference solutions (`method-references-en`)

No reference context is registered for this method’s problem figures.
##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/roe_properties.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/roe_properties.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_priority.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_priority.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_shock_priority.py tests/test_numerics.py
```
