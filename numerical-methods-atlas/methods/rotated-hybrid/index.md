# Rotated-hybrid Riemann solver / 回転ハイブリッド・リーマンソルバー

Status: educational-example

Construct directional dissipation using a velocity-jump frame. Distinguish Ren (2003), Nishikawa–Kitamura (2008) and related Roe–Nishikawa et al. (2005) research, and state the scope of the published HLLE/Roe experiment.

速度差に合わせた方向と直交方向で散逸を組む回転ハイブリッド法。Ren（2003）、西川–北村（2008）、Roe・西川ら（2005）の関連研究を区別し、公開HLLE/Roe実験の範囲を明示します。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: rotated Riemann solver, rotated hybrid Riemann solver, 回転リーマンソルバー, rotated-hybrid solver

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/rotated-hybrid/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/rotated-hybrid/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py

- Reference: https://doi.org/10.1016/s0045-7930(02)00114-7 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1016/j.jcp.2007.11.003 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.2514/6.2005-4872 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1016/0021-9991(81)90128-5 — Method-specific source; see the detailed reading for source role and actual review depth.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rotated-hybrid/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; cylinder-forebody)

#### 問題の図 (`method-problems-ja`)

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja) (`cylinder-forebody`)

![保存済み円柱前面の密度比較。有限時刻の結果で、定常収束の認定ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja) (`cylinder-forebody`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/rotated-hybrid/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Educational directional HLLE/Roe construction; not the optimized Rotated-RHLL dissipation formula in Nishikawa–Kitamura (2008). Other chapter flux modules are separate methods.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_shock_expansion.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; cylinder-forebody)

#### Problem figures (`method-problems-en`)

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en) (`cylinder-forebody`)

![Stored finite-time forebody density comparison; not steady-state certification.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

Flux comparisons stored for the body-fitted bow shock. The rotated entry is the educational directional HLLE/Roe experiment, not completed validation of optimized Rotated-RHLL.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#references-en) (`cylinder-forebody`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/rotated-hybrid/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Educational directional HLLE/Roe construction; not the optimized Rotated-RHLL dissipation formula in Nishikawa–Kitamura (2008). Other chapter flux modules are separate methods.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_shock_expansion.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_shock_expansion.py
```
