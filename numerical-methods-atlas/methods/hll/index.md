# HLL / HLL

Status: educational-example

Read about HLL, follow the original references and inspect related educational code and checks.

「HLL」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: HLL法, HLL流束, HLLリーマンソルバー, Harten-Lax-van Leer

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

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`; dam-break)
- [等温流体方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#isothermal-ja) (`isothermal`; isothermal-jump)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; double-mach, nasa-wedge, forward-step, entropy-2d, odd-even)

#### 問題の図 (`method-problems-ja`)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![保存済み2次元Double Mach反射の最終フレーム。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/double-mach/frame-080.webp)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![保存済みMach 3前向きステップの計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/step-m3-mc.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja) (`entropy-2d`)

![保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja) (`odd-even`)

![保存済み定常平面衝撃波のodd–even診断。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) (`dam-break`)

- [浅水流／水深が正のダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dam-break-ja) (`swe-dam-break`; 関連モデルの参照; 半解析参照)

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break)

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) (`isothermal-jump`)

- [等温流／密度跳躍](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isothermal-jump-ja) (`isothermal-jump`; 関連モデルの参照; 半解析参照)

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump)

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) (`double-mach`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) (`nasa-wedge`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) (`forward-step`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) (`entropy-2d`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) (`odd-even`)

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

- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`; dam-break)
- [Isothermal flow equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#isothermal-en) (`isothermal`; isothermal-jump)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; double-mach, nasa-wedge, forward-step, entropy-2d, odd-even)

#### Problem figures (`method-problems-en`)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Stored final frame of 2D Double Mach reflection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/double-mach/frame-080.webp)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Stored computed field for the Mach-3 forward-facing step.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/step-m3-mc.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en) (`entropy-2d`)

![Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en) (`odd-even`)

![Stored odd–even diagnostic for a stationary planar shock.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

Fluxes and Roe acoustic entropy smoothing used in the stored normal-shock diagnostic. The pressure-sensor blend is not identified as Rotated-RHLL.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) (`dam-break`)

- [Shallow water / wet dam break](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dam-break-en) (`swe-dam-break`; Related-model reference; Semi-analytic reference)

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break)

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) (`isothermal-jump`)

- [Isothermal / density jump](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isothermal-jump-en) (`isothermal-jump`; Related-model reference; Semi-analytic reference)

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump)

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) (`double-mach`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) (`nasa-wedge`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) (`forward-step`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) (`entropy-2d`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) (`odd-even`)

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
