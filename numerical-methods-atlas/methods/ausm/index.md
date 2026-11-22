# AUSM-family flux splitting / AUSM系列の流束分割

Status: educational-example

Read about AUSM-family flux splitting, follow the original references and inspect related educational code and checks.

「AUSM系列の流束分割」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: AUSM法, AUSM流束, advection upstream splitting method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py

- Reference: https://doi.org/10.1016/0021-9991(84)90143-8 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/1410.4194 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.1996.0256 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2005.09.020 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2007.11.003 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; strong-shock, cylinder-forebody, odd-even)

#### 問題の図 (`method-problems-ja`)

##### [1次元の強い圧力ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja) (`strong-shock`)

![完了したPPM計算の保存密度。停止した他の変種とは区別しています。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#code-ja)

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


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元の強い圧力ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#references-ja) (`strong-shock`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja) (`cylinder-forebody`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) (`odd-even`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/ausm.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_shock_expansion.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; strong-shock, cylinder-forebody, odd-even)

#### Problem figures (`method-problems-en`)

##### [One-dimensional strong pressure jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en) (`strong-shock`)

![Stored density from a completed PPM run, distinct from variants that stopped.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#code-en)

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


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional strong pressure jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#references-en) (`strong-shock`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#references-en) (`cylinder-forebody`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) (`odd-even`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/ausm.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_shock_expansion.py
```
