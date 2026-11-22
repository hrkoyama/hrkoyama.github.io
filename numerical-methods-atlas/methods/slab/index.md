# Horizontal-periodic slab Green-function FFT / 水平周期スラブGreen関数FFT

Status: educational-example

Read about Horizontal-periodic slab Green-function FFT, follow the original references and inspect related educational code and checks.

「水平周期スラブGreen関数FFT」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: slab gravity, スラブ重力, slab Green function, 水平周期境界の重力, 水平周期スラブ境界

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/gravity_boundaries.py

- Reference: https://doi.org/10.1201/9780367806934 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1088/0004-637X/693/2/1316 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/0812.1846 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; uniform-slab, sinusoidal-sheet)

#### 問題の図 (`method-problems-ja`)

##### [一様平面スラブの重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja) (`uniform-slab`)

![境界核の共有図。このカードは「一様平面スラブ」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [正弦波状薄層の重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja) (`sinusoidal-sheet`)

![境界核の共有図。このカードは「正弦薄層」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [一様平面スラブの重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja#references-ja) (`uniform-slab`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [正弦波状薄層の重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja#references-ja) (`sinusoidal-sheet`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/gravity_boundaries.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_gravity_boundaries.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; uniform-slab, sinusoidal-sheet)

#### Problem figures (`method-problems-en`)

##### [Uniform plane-slab gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en) (`uniform-slab`)

![Shared boundary-kernel figure; this card links specifically to uniform-slab.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Sinusoidal sheet gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en) (`sinusoidal-sheet`)

![Shared boundary-kernel figure; this card links specifically to sinusoidal-sheet.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Uniform plane-slab gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en#references-en) (`uniform-slab`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Sinusoidal sheet gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en#references-en) (`sinusoidal-sheet`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/gravity_boundaries.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_gravity_boundaries.py
```
