# Monotonized central / MC / 単調中心勾配制限／MC

Status: educational-example

Read about Monotonized central / MC, follow the original references and inspect related educational code and checks.

「単調中心勾配制限／MC」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: MC制限関数, MC limiter, monotonized central limiter, 単調中心制限関数

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py

- Reference: https://doi.org/10.1137/0721062 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-square)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; nasa-wedge, forward-step, entropy-2d)

#### 問題の図 (`method-problems-ja`)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja) (`entropy-2d`)

![保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) (`advection-square`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) (`nasa-wedge`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) (`forward-step`)

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照; 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements)

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) (`entropy-2d`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/tvd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_limiters.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-square)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; nasa-wedge, forward-step, entropy-2d)

#### Problem figures (`method-problems-en`)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

Methods used by the stored square-wave CIP and limiter comparisons.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en) (`entropy-2d`)

![Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) (`advection-square`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) (`nasa-wedge`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) (`forward-step`)

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference; Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements)

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) (`entropy-2d`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/tvd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_limiters.py
```
