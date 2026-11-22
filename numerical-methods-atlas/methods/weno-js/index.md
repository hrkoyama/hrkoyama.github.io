# WENO5-JS / WENO5-JS

Status: educational-example

Read about WENO5-JS, follow the original references and inspect related educational code and checks.

「WENO5-JS」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: WENO-JS, WENO5JS, WENO-JS法, WENO, WENO法, WENOスキーム, Jiang-Shu WENO

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(89)90222-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(91)90211-3 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1017/CBO9780511791253 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; entropy-1d, moving-contact)

#### 問題の図 (`method-problems-ja`)

##### [1次元Eulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja) (`entropy-1d`)

![保存済みの1次元エントロピー波の密度誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [移動接触不連続](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja) (`moving-contact`)

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Eulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja#references-ja) (`entropy-1d`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [移動接触不連続](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#references-ja) (`moving-contact`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; entropy-1d, moving-contact)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en) (`entropy-1d`)

![Stored density-error refinement for a 1D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Moving contact discontinuity](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en) (`moving-contact`)

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en#references-en) (`entropy-1d`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Moving contact discontinuity](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#references-en) (`moving-contact`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_numerics.py
```
