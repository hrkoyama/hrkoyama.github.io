# Forward Euler / 前進Euler法

Status: educational-example

Read about Forward Euler, follow the original references and inspect related educational code and checks.

「前進Euler法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: 前進オイラー法, 陽的Euler法, 陽的オイラー法, explicit Euler, forward Euler method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front.

浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。

- SWASHES topographic flow: lakes and nonzero steady discharge: https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/
- Dry-bed dam break: actual wetting and dry states: https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json

Common execution records: [{"id": "swashes-topography", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dry-bed-dam-break", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; heat-periodic, heat-dirichlet)
- [地形源項付き浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja) (`shallow-water-bed`; swashes-topography)
- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`; dry-bed-dam-break)

#### 問題の図 (`method-problems-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja) (`nonlinear-exp-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja) (`nonlinear-rational-decay`)

![保存済み有理減衰ODEの時間刻み収束（代表3手法）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

- [SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) (`swashes-topography`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

- [乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) (`heat-periodic`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) (`heat-dirichlet`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) (`nonlinear-exp-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) (`nonlinear-rational-decay`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#references-ja) (`swashes-topography`)

- [静止湖：表現した床の上の湿潤・露出平衡](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja) (`lake-at-rest-bed`; 同じ問題の参照; 解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

[既存の参照図](/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

- [SWASHES定常流：非射流Bernoulli根](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja) (`swashes-bernoulli`; 同じ問題の参照; 半解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

[既存の参照図](/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#references-ja) (`dry-bed-dam-break`)

- [Ritter乾燥床破堤：g9.81の専用セル平均参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja) (`ritter-dry-bed`; 同じ問題の参照; 解析参照)

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

[既存の参照図](/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-measurements)

- [浅水／乾床への膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja) (`swe-dry-bed`; 関連モデルの参照; 解析参照)

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dry-bed)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### SWASHES地形流：静水と非零流量の定常解 (`swashes-topography`)

[SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

##### 乾いた河床のダム破壊：実際のwetting/drying (`dry-bed-dam-break`)

[乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; heat-periodic, heat-dirichlet)
- [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en) (`shallow-water-bed`; swashes-topography)
- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`; dry-bed-dam-break)

#### Problem figures (`method-problems-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en) (`nonlinear-exp-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en) (`nonlinear-rational-decay`)

![Stored time-refinement errors for rational decay, showing three methods.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

- [SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) (`swashes-topography`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

- [Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) (`heat-periodic`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) (`heat-dirichlet`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) (`nonlinear-exp-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) (`nonlinear-rational-decay`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#references-en) (`swashes-topography`)

- [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en) (`lake-at-rest-bed`; Same-problem reference; Analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

- [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en) (`swashes-bernoulli`; Same-problem reference; Semi-analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#references-en) (`dry-bed-dam-break`)

- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en) (`ritter-dry-bed`; Same-problem reference; Analytic reference)

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

[Existing reference profile](/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-measurements)

- [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en) (`swe-dry-bed`; Related-model reference; Analytic reference)

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dry-bed)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### SWASHES topographic flow: lakes and nonzero steady discharge (`swashes-topography`)

[SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

##### Dry-bed dam break: actual wetting and dry states (`dry-bed-dam-break`)

[Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
