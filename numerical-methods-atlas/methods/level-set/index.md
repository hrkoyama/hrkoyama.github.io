# Level-set method / レベルセット法

Status: educational-example

Represent an interface by phi=0 and evolve advection or normal motion through Hamilton–Jacobi equations. Dedicated ENO2/Heun examples validate 2D circle translation and off-center rigid rotation, measuring area error and redistancing effects.

界面をφ=0で表し、Hamilton–Jacobi型の方程式で移流・法線運動を扱う。専用の2D円の平行移動・偏心剛体回転をENO2＋Heunで検証し、面積誤差と再初期化の影響を比較する。

VOF/CLSVOF comparisons describe formulations and conditions. No VOF implementation, performance ranking, curvature-flow, two-phase-flow or topology-change validation is claimed.

Other names: level set, level-set method, levelset, レベルセット, レベル・セット法, 界面捕獲, 符号付き距離関数

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/



- Reference: https://doi.org/10.1016/0021-9991(88)90002-2 — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- Reference: https://doi.org/10.1016/0021-9991(81)90145-5 — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- Reference: https://doi.org/10.1137/S1064827596298245 — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- Reference: https://doi.org/10.1006/jcph.2000.6537 — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.

## Small fixed-input validation supplements

Prescribed circle translation and off-center full rotation only: 2D ENO2/Heun,32²/64²/128²,T1, optional redistancing, five common observations and anN64 CFL-halving sensitivity.

与えた速度による円の平行移動・偏心1周回転。2D ENO2/Heun、32²/64²/128²、T1、再初期化あり/なし、5共通時刻とN64の刻み半減だけを検証。

- 2D level-set circle translation: interface, area and redistancing: https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/
- 2D rigid rotation of an off-center level-set circle: https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json

Common execution records: [{"id": "level-set-translation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "level-set-rotation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja) (`level-set-advection`; level-set-circle)

#### 問題の図 (`method-problems-ja`)

##### [レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

![実際の128²レベルセット場から抽出した円のゼロ等値線。左は平行移動、右は偏心円の一周回転。解析界面と移流単独・単純な再初期化ありを比較します。VOF計算ではなく、面積保存を補正していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

専用の2D ENO2／Heunレベルセット移流。任意選択の単純なGodunov再初期化による面積変化も保存し、VOF実装を割り当てません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

- [レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) (`level-set-translation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

- [偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) (`level-set-rotation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。


#### 厳密解・参照解 (`method-references-ja`)

##### [レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#references-ja) (`level-set-circle`)

- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja) (`level-set-translation`; 同じ問題の参照; 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/level-set-translation/?lang=ja)

- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja) (`level-set-rotation`; 同じ問題の参照; 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/level-set-rotation/?lang=ja)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### レベルセット円の2D平行移動：界面・面積・再初期化 (`level-set-translation`)

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

##### 偏心したレベルセット円の2D剛体回転 (`level-set-rotation`)

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

与えた速度による円の平行移動・偏心1周回転。2D ENO2/Heun、32²/64²/128²、T1、再初期化あり/なし、5共通時刻とN64の刻み半減だけを検証。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en) (`level-set-advection`; level-set-circle)

#### Problem figures (`method-problems-en`)

##### [Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

![Zero contours extracted from actual128² level-set fields: translation(left) and an off-center full rotation(right). Compare analytic interfaces against advection alone and simple redistancing. This is not a VOF calculation, and no area correction is applied.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

Dedicated2D ENO2/Heun level-set advection. Optional simple Godunov redistancing retains measured area changes; no VOF implementation is assigned.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

- [2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) (`level-set-translation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

- [2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) (`level-set-rotation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.


#### Exact / reference solutions (`method-references-en`)

##### [Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#references-en) (`level-set-circle`)

- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en) (`level-set-translation`; Same-problem reference; Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

[Existing reference profile](/numerical-methods-atlas/validation/level-set-translation/?lang=en)

- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en) (`level-set-rotation`; Same-problem reference; Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

[Existing reference profile](/numerical-methods-atlas/validation/level-set-rotation/?lang=en)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 2D level-set circle translation: interface, area and redistancing (`level-set-translation`)

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

##### 2D rigid rotation of an off-center level-set circle (`level-set-rotation`)

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Prescribed circle translation and off-center full rotation only: 2D ENO2/Heun,32²/64²/128²,T1, optional redistancing, five common observations and anN64 CFL-halving sensitivity.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

###### Related source

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)

###### Package tests

- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
