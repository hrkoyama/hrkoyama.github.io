# 乾燥床へのRitter破堤流 / Ritter dam break onto a dry bed

https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/

## 日本語

[実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/#dry-bed-dam-break) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#dry-bed-dam-break)

### 方程式・問題の定義

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、800/1600/3200セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。

#### [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja)

$$
h_t+(hu)_x=0
$$

$$
(hu)_t+(hu^2+gh^2/2)_x=0
$$

$$
u_t-fv=-g\eta_x,\quad v_t+fu=-g\eta_y
$$

$$
\eta_t+H(u_x+v_y)=0
$$

前2式は平坦床・摩擦なしの1次元系。後2行は水深Hまわりの線形回転系。非線形流れのテストと、回転系のFourier記号の検証を区別します。

#### 乾いた河床のダム破壊：実際のwetting/drying

補助実行例 · 実行例の定義・検証式

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

### 厳密解・参照解

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。

#### [Ritter乾燥床破堤：g9.81の専用セル平均参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-measurements)

解析解 · 同じ問題の参照

cL=sqrt(g*hL); h=(2*cL-(x-x0)/t)^2/(9*g), u=2*((x-x0)/t+cL)/3 inside fan; hR=0 beyond x0+2*cL*t.

平坦・摩擦なしの[-10,10]m、堰x0=0、hL1m/hR0、初速0、g9.81、t.5s。左波頭−sqrt(g)tと真の乾燥前縁2sqrt(g)tで分割して保存量(h,hu)をセル平均します。固定水深.001mの等値線も区別します。旧参照カードと重力・領域・時刻の異なる専用入力で、旧値は変更しません。

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

#### [浅水／乾床への膨張波](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dry-bed)

解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

#### 乾いた河床のダム破壊：実際のwetting/drying

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja)

### 計算法

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja)

補助実行例

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、1600/3200/6400セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。 第3回は108/109判定が合格し、最細の前線誤差.27415>.25mで不合格でした。第4回は同じ領域のRitter格子だけを1600/3200/6400に細分化します。相対水深L1は領域内参照質量で正規化し、領域変更を比べるため絶対L1も保存します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)

## English

[Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/#dry-bed-dam-break) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#dry-bed-dam-break-en)

### Equations and problem definitions

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,800/1600/3200 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.

#### [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en)

$$
h_t+(hu)_x=0
$$

$$
(hu)_t+(hu^2+gh^2/2)_x=0
$$

$$
u_t-fv=-g\eta_x,\quad v_t+fu=-g\eta_y
$$

$$
\eta_t+H(u_x+v_y)=0
$$

The first two equations are 1D flat-bed, frictionless flow; the remaining lines are the linear rotating system about depth H. Distinguish nonlinear flow tests from rotating-system Fourier-symbol checks.

#### Dry-bed dam break: actual wetting and dry states

Supplementary execution example · Example definition or validation formula

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

### Exact and reference solutions

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m.

#### [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-measurements)

Analytic reference · Reference for the same problem

cL=sqrt(g*hL); h=(2*cL-(x-x0)/t)^2/(9*g), u=2*((x-x0)/t+cL)/3 inside fan; hR=0 beyond x0+2*cL*t.

Flat frictionless[-10,10]m, dam x00,hL1m/hR0,zero initial velocity,g9.81,t.5s. Split conserved(h,hu) cell means at the rarefaction head−sqrt(g)t and genuine dry front2sqrt(g)t. Separately track the fixed depth.001m contour. These dedicated gravity/domain/time inputs differ from the historical card, whose values remain unchanged.

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

#### [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dry-bed)

Analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

#### Dry-bed dam break: actual wetting and dry states

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en)

### Numerical methods

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en)

Supplementary execution example

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged. Revision3 passed108/109 gates but failed the .27415m>.25m contour criterion. Revision4 refines only Ritter grids to1600/3200/6400. Relative depth L1 is normalized by domain reference mass; absolute L1 is also retained because the domain changed between revisions1 and2.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)
