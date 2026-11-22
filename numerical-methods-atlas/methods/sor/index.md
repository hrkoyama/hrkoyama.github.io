# Successive over-relaxation / SOR / 逐次過緩和法／SOR

Status: educational-example

Read about Successive over-relaxation / SOR, follow the original references and inspect related educational code and checks.

「逐次過緩和法／SOR」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: SOR法, 逐次過緩和, 過緩和法, successive over relaxation

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py

- Reference: https://doi.org/10.1017/S0305004100023197 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1090/S0025-5718-1977-0431719-X — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1137/1.9780898719505 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja) (`poisson-2d-broad`)

![保存済みの広帯域ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元Poisson・局在ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja) (`poisson-2d-localized`)

![保存済み局在ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#references-ja) (`poisson-2d-broad`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

同じPoisson製造解の考え方ですが、カードは1次元単一正弦、こちらは2次元の滑らかな複合ソースです。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

##### [2次元Poisson・局在ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#references-ja) (`poisson-2d-localized`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en) (`poisson-2d-broad`)

![Stored broad smooth forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [2D Poisson / localized source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en) (`poisson-2d-localized`)

![Stored localized forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#references-en) (`poisson-2d-broad`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

Both use manufactured Poisson solutions, but the card is a 1D single sine while this test uses a smooth composite 2D source.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

##### [2D Poisson / localized source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#references-en) (`poisson-2d-localized`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```
