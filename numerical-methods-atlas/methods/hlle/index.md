# HLLE / Einfeldt wave speeds / HLLE／Einfeldt波速

Status: educational-example

Read about HLLE / Einfeldt wave speeds, follow the original references and inspect related educational code and checks.

「HLLE／Einfeldt波速」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: HLLE法, HLLE流束, Einfeldt, Einfeldt波速, HLLE solver, アインフェルト波速

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

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; strong-shock, double-rarefaction, cylinder-forebody, odd-even)
- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`; circular-alfven, magnetic-loop)

#### 問題の図 (`method-problems-ja`)

##### [1次元の強い圧力ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja) (`strong-shock`)

![完了したPPM計算の保存密度。停止した他の変種とは区別しています。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

従来のGodunov／HLLEプレビューと、追加のMUSCL・Lax–Friedrichs・平均保存スケーリング・SSPRK(3,3)固定入力は別の実行例です。段階正値性の条件は追加版の説明・契約・全段ログに限定します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja) (`cylinder-forebody`)

![保存済み円柱前面の密度比較。有限時刻の結果で、定常収束の認定ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja) (`odd-even`)

![保存済み定常平面衝撃波のodd–even診断。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

![保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元の強い圧力ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#references-ja) (`strong-shock`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) (`double-rarefaction`)

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction)

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja) (`cylinder-forebody`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) (`odd-even`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) (`circular-alfven`)

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照; 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

[既存の参照図](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-measurements)

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) (`magnetic-loop`)

- [磁場ループ：固定Athena++の独立終端参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja) (`magnetic-loop-independent`; 関連モデルの参照; 有限格子の数値参照)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-measurements)

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

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; strong-shock, double-rarefaction, cylinder-forebody, odd-even)
- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`; circular-alfven, magnetic-loop)

#### Problem figures (`method-problems-en`)

##### [One-dimensional strong pressure jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en) (`strong-shock`)

![Stored density from a completed PPM run, distinct from variants that stopped.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

The earlier Godunov/HLLE preview and the new MUSCL/Lax–Friedrichs/mean-preserving-scaling/SSPRK(3,3) run are separate execution records. Stage-positivity conditions are scoped to the additional release, its contract and all-stage diagnostics.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en) (`cylinder-forebody`)

![Stored finite-time forebody density comparison; not steady-state certification.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

Flux comparisons stored for the body-fitted bow shock. The rotated entry is the educational directional HLLE/Roe experiment, not completed validation of optimized Rotated-RHLL.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en) (`odd-even`)

![Stored odd–even diagnostic for a stationary planar shock.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

Fluxes and Roe acoustic entropy smoothing used in the stored normal-shock diagnostic. The pressure-sensor blend is not identified as Rotated-RHLL.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

![Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional strong pressure jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#references-en) (`strong-shock`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) (`double-rarefaction`)

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference; Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction)

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#references-en) (`cylinder-forebody`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) (`odd-even`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) (`circular-alfven`)

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference; Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

[Existing reference profile](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-measurements)

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) (`magnetic-loop`)

- [Magnetic loop: pinned independent Athena++ final-field reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en) (`magnetic-loop-independent`; Related-model reference; Finite-grid numerical reference)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.

[Existing reference profile](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-measurements)

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
