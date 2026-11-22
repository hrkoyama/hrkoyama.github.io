# Symplectic Euler / シンプレクティックEuler法

Status: educational-example

Read about Symplectic Euler, follow the original references and inspect related educational code and checks.

「シンプレクティックEuler法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: symplectic Euler法, symplectic Euler method, シンプレクティックオイラー法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1016/0375-9601(90)90092-3 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1017/S0962492902000144 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; quartic-oscillator)

#### 問題の図 (`method-problems-ja`)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja) (`quartic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) (`quartic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; quartic-oscillator)

#### Problem figures (`method-problems-en`)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en) (`quartic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) (`quartic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_hamiltonian.py
```
