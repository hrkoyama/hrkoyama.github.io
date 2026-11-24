# 厳密解・参照解 / Exact and reference solutions

Source: https://hrkoyama.github.io/numerical-methods-atlas/assets/reference-solutions.json

SHA-256: `c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc`

## 日本語

### 移流／正弦波の平行移動

解析解 · 1次元

`u = 1 + 0.25 sin[2π(x−t)]`

単位区間の周期境界、一定移流速度1。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

関連モデルの問題

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

- [実行・検証：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

- [実行・検証：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

この実行例の範囲：同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

- [実行・検証：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) (`fr-periodic-advection`) · [コードZIP：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。


##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

関連モデルの問題

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

固定入力実行例は未登録です。



### 熱拡散／Fourierモードの減衰

解析解 · 1次元

`u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]`

単位区間の周期境界、拡散係数0.02。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

関連モデルの問題

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

関連モデルの問題

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

固定入力実行例は未登録です。

##### [周期せん断波の粘性減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja) (`lbm-shear`)

![保存済みせん断波振幅と粘性減衰の参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja)

関連モデルの問題

周期せん断速度の線形粘性減衰とスカラー熱モードは同型ですが、LBMの格子単位・波数・粘性と参照カードのν=0.02は異なります。

固定入力実行例は未登録です。



### Burgers／衝撃波

解析解 · 1次元

`u_t + (u²/2)_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-shock) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja) (`burgers-shock`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#code-ja)

関連モデルの問題

左右状態(1,0)、段差位置0.5、端点継続が一致します。点値とセル平均の評価は区別します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### Burgers／膨張波

解析解 · 1次元

`u_t + (u²/2)_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-fan) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja) (`burgers-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#code-ja)

関連モデルの問題

左右状態(0,1)、段差位置0.5、端点継続が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### 交通流／上流へ進む衝撃波

解析解 · 1次元

`rho_t + [rho(1−rho)]_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-jam) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja) (`traffic-jam`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#code-ja)

関連モデルの問題

流束ρ(1-ρ)、左右密度(0.3,0.9)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### 交通流／渋滞解消の膨張波

解析解 · 1次元

`rho_t + [rho(1−rho)]_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-fan) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja) (`traffic-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#code-ja)

関連モデルの問題

流束ρ(1-ρ)、左右密度(0.9,0.1)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### Euler／Sod問題

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-sod) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

関連モデルの問題

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [実行・検証：Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja) (`sod`) · [コードZIP：Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。




### Euler／Lax問題

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-lax) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [Lax衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=ja) (`lax`)

![共有図の左パネル：Lax衝撃波管。右は別のエントロピー波収束計算。](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=ja#code-ja)

関連モデルの問題

γ=1.4、左右(0.445,0.698,3.528)/(0.5,0,0.571)、[-5,5]、x0=0、t=1.3が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### Euler／二重膨張波

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

関連モデルの問題

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [実行・検証：Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) (`euler-double-rarefaction-positivity`) · [コードZIP：Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

この実行例の範囲：既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。




### Euler／生成される真空

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-vacuum) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 浅水流／水深が正のダム崩壊

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

関連モデルの問題

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### 浅水／乾床への膨張波

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dry-bed) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

関連モデルの問題

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

- [実行・検証：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`) · [コードZIP：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。




### 浅水／中央の乾燥領域

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-vacuum) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 等温流／密度跳躍

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

p = c_s² rho、一定の音速c_s。初期密度は厳密に正とし、真空状態とエネルギー方程式はありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

関連モデルの問題

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

固定入力実行例は未登録です。



### Poisson／正弦波の製造解

製造解 · 1次元

`u = sin(πx); −u_xx = f = π² sin(πx)`

両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

![保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

関連モデルの問題

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。

- [実行・検証：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`) · [コードZIP：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。


##### [1次元Poisson・純Neumann境界](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja) (`poisson-1d-neumann`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-neumann.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja#code-ja)

関連モデルの問題

参照カードはsin(πx)・零Dirichlet、こちらはf=-2・純Neumann・平均ゲージです。

固定入力実行例は未登録です。

##### [1次元Poisson・Dirichlet/Neumann混合境界](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja) (`poisson-1d-mixed`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-mixed.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja#code-ja)

関連モデルの問題

参照カードは零Dirichletの正弦解、こちらは混合境界の1+x²です。

固定入力実行例は未登録です。

##### [1次元Poisson・Robin境界の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja) (`poisson-1d-robin`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja#code-ja)

関連モデルの問題

参照カードは零Dirichletの正弦解、こちらはRobin境界のexp(x)です。

固定入力実行例は未登録です。

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja) (`poisson-2d-broad`)

![保存済みの広帯域ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#code-ja)

関連モデルの問題

同じPoisson製造解の考え方ですが、カードは1次元単一正弦、こちらは2次元の滑らかな複合ソースです。

固定入力実行例は未登録です。

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

関連モデルの問題

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [実行・検証：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

- [実行・検証：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja) (`sa-amg`) · [コードZIP：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

この実行例の範囲：正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

- [実行・検証：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。




### 粘性チャネル／Couette流

解析解 · 1次元

`u(y) = y`

十分に発達した平面定常チャネル。壁速度u(0)=0、u(1)=1、圧力勾配ゼロ。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=couette) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 粘性チャネル／Poiseuille流

解析解 · 1次元

`u(y) = G y(1−y)/(2ν); G=1, ν=0.1`

十分に発達した平面定常チャネル、no-slip、単位密度。−dp/dx=G、または体積力加速度G。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poiseuille) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja) (`channel-poiseuille`)

![保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja)

関連モデルの問題

放物線形は共通ですが、計算は格子幅ny・目標最大速度0.01に応じた体積力、カードは単位幅・G=1・ν=0.1です。

固定入力実行例は未登録です。



### 粘性流／2次元Taylor–Green渦

解析解 · 2次元

`(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4`

周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。

Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=taylor-green) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

#### 関連するテスト問題の図とコード

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

関連モデルの問題

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

- [実行・検証：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

- [実行・検証：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) (`lbm-taylor-green`) · [コードZIP：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

この実行例の範囲：周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。




### Nohの冷たい流入衝撃波：平面・円筒・球対称

解析解 · 1次元

`s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.`

理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。 別の実2D Cartesian版では[-.5,.5]²の32²/64²/128²格子、2成分運動量と両方向流束を使い、半径還元は行いません。密度参照は衝撃円で分割した64/128点の求積セル平均です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/#noh-shock)

- original-problem: [W. F. Noh (1987), Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux, JCP72,78–120](https://doi.org/10.1016/0021-9991(87)90074-X) — Original problem and wall-heating analysis. Publisher metadata/abstract checked; no claim of reproducing every original calculation.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Noh1987. The analytic evaluator is a reference, not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, exactpack/solvers/noh/noh1.py](https://github.com/lanl/ExactPack/blob/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/noh/noh1.py) — BSD-3-Clause. Actual evaluation is restricted to gamma=5/3,rho0=1,inward speed1. Source hashes, point/shell comparisons and parameter-limit control are saved in the Noh release.
#### 関連するテスト問題の図とコード

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![実際の2次元Cartesian Euler計算の密度場。正方形全域128²セル、初期圧力ゼロ、γ=5/3、t=.6。白破線は厳密衝撃円。軸・対角方向の差と原点過熱を残し、1D半径例にも辿れます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

同じ問題への対応

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

- [実行・検証：Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP：Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

この実行例の範囲：初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

- [実行・検証：Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) (`noh-cartesian-2d`) · [コードZIP：Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

この実行例の範囲：正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。




### Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解

半解析解 · 1次元

`R_s(t)=beta*(E0*t^2/rho0)^(1/5), beta≈1.15166641793; D=2*R_s/(5*t); rho=rho0*G(r/R_s), u=D*V(r/R_s), p=rho0*D^2*P(r/R_s).`

理想気体Eulerの球半径対称、γ=5/3、周囲密度1・圧力0、爆発エネルギー1、r∈[0,1]、t=0.05。自己相似参照は瞬間的な理想点源を表しますが、有限体積計算は半径0.03の内部へ投入し、同じ最細格子で半径0.015も比較します。参照は相似ODEの数値積分、小さな中心域の正則漸近形、衝撃位置で分割する球殻求積を含む半解析解であり、閉形式の厳密セル平均ではありません。ギャラリー図は1次元球半径データの中心断面で、2D Cartesian計算ではありません。固定投入半径での誤差には点源とのモデル差が含まれ、その傾きは純粋な空間収束次数ではなく、投入半径の変更も感度診断に留まります。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-sedov/#sedov-blast)

- original-similarity-theory: [G. I. Taylor (1950), The formation of a blast wave by a very intense explosion I. Theoretical discussion, Proceedings of the Royal Society A201(1065),159–174](https://doi.org/10.1098/rspa.1950.0049) — Original theoretical similarity assumptions, Euler reduction, strong-shock conditions, energy normalization and regular-center exponent checked in selected original pp159–167 via a university-hosted scan. Publisher access returned403; no full publisher-text review or PDF redistribution is claimed.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Taylor1950 and the selected pinned reference implementation. ExactPack evaluates a reference and is not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, selected Sedov evaluator](https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/sedov) — BSD-3-Clause. The selected unmodified pinned Sedov evaluator was actually run at npts6001/12001 with gamma=5/3,rho0=E0=1,t=.05,geometry3 and probes xi=.15,.25,.5,.75,.9,1.05. Source hashes, invocation and point values are archived. The upstream small-radius warning for density/internal energy is retained; the central region and shock jump are excluded from these point probes. This does not validate other ExactPack solvers or an independent PDE engine.
#### 関連するテスト問題の図とコード

##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

![1次元球対称Eulerの保存済み半径密度を中心断面に表示。γ=5/3、E=ρ0=1、p0=0、t=.05、512球殻、有限投入半径.03。半解析的な点源参照との違いと衝撃層の誤差を残した図で、実2D Cartesian計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

同じ問題への対応

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

- [実行・検証：Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) (`sedov-blast`) · [コードZIP：Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

この実行例の範囲：球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。




### Double Mach反射：保存済み独立有限格子数値参照

有限格子の数値参照 · 2次元

`partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| (conservative restriction of saved finite-grid data).`

領域[0,4]×[0,1]の2次元理想気体Euler、γ=1.4、Mach10・角度60度の入射衝撃波、初期の衝撃脚x=1/6、最終時刻T=.2。保存参照は別実装の非分割primitive MUSCL/HLL/Heun有限体積法（勾配制限はgeneralized minmodのθ=1.5、MC型であり標準MCのθ=2とは異なる）で、256×64と512×128セルです。主計算とHLLという流束族・Heun時間積分の数式を共有しますが、空間再構成と実装は別です。保存量を保つ制限で比較用セル平均を得ます。不変のRKDG2Dキットで以前に実行したソース・配列・記録を再利用し、今回の参照PDE・Athena・LAVAの新規実行ではありません。参照の格子差も有限分解能の感度指標で、厳密な誤差上界ではありません。厳密2D解でも細いwall jet・渦構造の収束検証でもありません。 入射不連続面の初期化はセル中心での状態判定であり、衝撃面で切られたセルの厳密平均からの初期化ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-double-mach/#double-mach-reflection)

- original-problem: [P. Woodward and P. Colella (1984), The numerical simulation of two-dimensional fluid flow with strong shocks, Journal of Computational Physics54(1),115–173](https://doi.org/10.1016/0021-9991(84)90142-6) — Publisher metadata/abstract and official NASA setup checked. No direct full-original-paper review is claimed.
- official-setup-cross-check: [NASA LAVA tutorial: Double Mach Reflection](https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/) — Official selected setup and boundary cross-check only; no LAVA execution or figure redistribution.
- executed-reference-implementation: [Previously executed independent FV-MUSCL/generalized-minmod(theta1.5)/HLL/Heun reference distributed with the RKDG2D agent kit,2026-11-23-r2](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip) — Selected sourceSHA256bc206f991594c6b011bb3cde50f104b8806a371df19af0464ff6b1a1d1cc39af; archiveSHA2566fa8d75c1f70281eb0a78363eb3323c5a9a1b006f01f49182c4827f4d5710a69. Reuse previously executed256×64 and512×128 arrays, source and records under MIT; no new reference PDE/Athena/LAVA execution. Reference has an adaptive retry capability, but the selected saved records report zero rejected steps.
#### 関連するテスト問題の図とコード

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

同じ問題への対応

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

- [実行・検証：Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja) (`double-mach-reflection`) · [コードZIP：Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

この実行例の範囲：既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。




### Mach 3前向きステップ：独立C++有限格子数値参照

有限格子の数値参照 · 2次元

`partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| on fluid cells (conservative restriction of a finite-grid reference).`

γ=1.4の2次元Euler流れ。[0,3]×[0,1]のうちx≥.6,y<.2は固体とし、初期・入口の(ρ,u,v,p)=(1.4,3,0,1)、上下と段差は滑り壁、右端はゼロ勾配、T=4です。参照は独立したC++17実装のprimitive MUSCL（一般化minmod θ1.5）/Davis HLL/HeunをCFL=.3、240×80・480×160で新規実行しました。境界に接する法線方向の傾きはゼロにし、再構築の傾き再調整はセル平均を変えません。Python主計算は区分定数HLL/Heunで、流束族・時間積分式は共有しますが実装と空間再構築は別です。角のエントロピー/エンタルピー補正、状態floor、刻み再試行はありません。角の数値エントロピー層が下流へ移流され得る無補正条件であり、補正付き原著PPM像の再現とは区別します。固体を除いた保存量を保守的に制限してから圧力を算出し、参照格子差・保存収支・局所診断を残します。有限格子の数値参照であり、厳密2次元解、誤差上界、細いすべり線や巻き上がりの収束証明ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-forward-step/#forward-step-m3)

- original-problem: [P. Woodward and P. Colella (1984), The numerical simulation of two-dimensional fluid flow with strong shocks, Journal of Computational Physics54(1),115–173](https://doi.org/10.1016/0021-9991(84)90142-6) — Original-problem bibliographic context; no direct full-original-paper review or reproduction of its corner-corrected PPM results is claimed.
- checked-setup-and-corner-caveat: [B. Cockburn and C.-W. Shu (1991), The P¹-RKDG Method for Two-Dimensional Euler Equations of Gas Dynamics, NASA CR187542 / ICASE91-32, Example2](https://ntrs.nasa.gov/api/citations/19910015505/downloads/19910015505.pdf) — Selected text of Example2 on printedpage7/PDFpage11 and Fig3 captions on printedpage8/PDFpage12 checked for Mach3 step geometry,initial/inflow state,T4 and the distinction between untreated and specially treated corners. No figure redistribution or RKDG execution. This publication deliberately uses the uncorrected corner.
- independent-reference-implementation: [Independent educational C++17 forward-step FV reference,2026-11-23](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp) — MIT. New primitive-MUSCL/generalized-minmod(theta1.5)/Davis-HLL/Heun runs on240×80 and480×160. Reference sourceSHA25666e523f5486179f2c79ac0ad21a35a11856e55a9101e03b8d3bca76cccbd5996; compiler/invocation and execution/quality receipts accompany the arrays. No external AMROC/Athena/LAVA execution.
#### 関連するテスト問題の図とコード

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

同じ問題への対応

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

- [実行・検証：Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja) (`forward-step-m3`) · [コードZIP：Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

この実行例の範囲：実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。




### 等エントロピー渦：低Mach比較に用いるEuler解析場

解析解 · 2次元

`a=beta exp((1-X²-Y²)/2)/(2pi); (u,v)=(1-aY,.5+aX); theta=1-(gamma-1)beta² exp(1-X²-Y²)/(8 gamma pi² p_inf); rho=theta^(1/(gamma-1)); p=p_inf theta^(gamma/(gamma-1)); p_inf=1.25/(1.4 M_inf²).`

全平面Eulerの移動等エントロピー渦を、γ=1.4、β=3、背景密度1、背景速度U=(1,.5)で定義します。背景Mach数Mに対してp∞=1.25/(1.4M²)とし、θ=1−(γ−1)β²exp(1−r²)/(8γπ²p∞)、ρ=θ^(1/(γ−1))、p=p∞θ^(γ/(γ−1))です。Uとともに動く座標を[-10,10]²へ折り返します。解析式は全平面の厳密なEuler解ですが、有限周期箱の継ぎ目にはゼロでないGaussianの裾があり、滑らかな周期トーラスの厳密解とは区別します。4保存量のセル平均をGauss8で求積しGauss16と照合した後、圧力・速度へ変換します。閉形式の厳密セル平均やprimitive変数の平均ではありません。低Mach固定例はM=.1/.01、T=.1。p∞=1で従来KEEPの場へ戻ります。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-low-mach/#low-mach-vortex)

- original-flux-preconditioning-method: [Fabian Miczek, Friedrich K. Röpke and Philipp V. F. Edelmann (2015), New numerical solver for flows at various Mach numbers](https://doi.org/10.1051/0004-6361/201425059) — Selected author-version equations and RK3 discussion were checked. This short isentropic-vortex application does not reproduce the paper’s Gresho or implicit-integration experiments.
- matrix-form-and-explicit-stability-analysis: [Wasilij Barsukow, Philipp V. F. Edelmann, Christian Klingenberg, Fabian Miczek and Friedrich K. Röpke (2017), A Numerical Scheme for the Compressible Low-Mach Number Regime of Ideal Fluid Dynamics](https://doi.org/10.1007/s10915-017-0372-4) — Checked the modified dissipation, primitive matrix and restrictive forward-Euler stability result. The present SSPRK33 Fourier/stage checks are separate fixed-input evidence, not a general nonlinear or SSP guarantee.
- analytic-vortex-definition-and-finite-periodic-box-qualification: [Seth C. Spiegel, H. T. Huynh and James R. DeBonis (2015), A Survey of the Isentropic Euler Vortex Problem using High-Order Methods](https://doi.org/10.2514/6.2015-2444) — Checked the generalized vortex and finite-periodic-boundary qualifications. The selected beta3, mean velocity(1,.5) and background Mach values are explicit adaptations, not NASA/FR execution or figure reuse.
#### 関連するテスト問題の図とコード

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

![M∞=.01、64²、T=.1の実際の2次元Euler計算。全\[-10,10\]²領域から中心\[-3,3\]²を拡大し、保存速度から差分で求めた渦度と背景流を引いた速度矢印で、MUSCL付き通常Roe／前処理Roeを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

同じ問題への対応

同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。

- [実行・検証：低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja) (`low-mach-vortex`) · [コードZIP：低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

この実行例の範囲：同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。




### Guderley収束衝撃波：固有値と球対称の半解析参照

半解析解 · 1次元

`R_s(t)=0.6*(-t)^alpha, alpha=1/lambda; x=t*(0.6/r)^lambda; rho=rho0*R(x), u=-r*V(x)/(lambda*t), p=rho*(-r*C(x)/(lambda*t))^2/gamma. For r<R_s:rho=rho0,u=p=0.`

理想気体Eulerの球半径対称、γ=1.4、未衝撃上流ρ0=1,u=p=0。Lazarus時間t∈[-1,-.85]、r∈[0,.75]、R_s(t)=.6(-t)^α、α=1/λです。原点収束t=0は区間外で、初期場の外側には衝撃後の相似状態があります。λは固定ExactPackの固有値探索と元stateの8点照合で求めた資格確認済みの保存値を通常追試で再利用し、相似ODE・Gauss16/32球殻求積・Euler計算は再実行します。固有値探索と元ソース点照合の再生成は別の明示コマンドです。衝撃で積分を分けた保存量の体積平均からpを求め、原始圧力の平均と区別します。閉形式の厳密セル平均や独立に実装した相似解とは呼びません。図は1D球半径結果の2D子午面表示で、2D Cartesianや反射後の計算ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-guderley/#guderley-implosion)

- historical-original-problem-attribution: [G. Guderley (1942), Starke kugelige und zylindrische Verdichtungsstöße in der Nähe des Kugelmittelpunktes bzw. der Zylinderachse, Luftfahrtforschung 19, 302 (first page)](https://raw.githubusercontent.com/lanl/ExactPack/9bacc477eb791e959c9621e771fc7a725db755fa/doc/source/references.rst) — Historical original-problem attribution. Author/year/volume/first page 302 were checked in the pinned ExactPack bibliography and the title in the Lazarus1981 publisher references. The original 1942 text was not inspected and is not claimed as the directly transcribed source of the present fields or measurements.
- semi-analytic-benchmark-and-two-eigenvalue-context: [Scott D. Ramsey, James R. Kamm and John H. Bolstad (2012), The Guderley problem revisited, International Journal of Computational Fluid Dynamics 26, 79–99](https://doi.org/10.1080/10618562.2011.647768) — The LANL record and abstract distinguish the convergence exponent from the reflected trajectory eigenvalue. This is not a claim to have read the entire paper or reproduced its PDE experiment; the present field is constructed using the pinned ExactPack source.
- similarity-coordinate-convention-and-tabulated-exponent: [Roger B. Lazarus (1981), Self-Similar Solutions for Converging Shocks and Collapsing Cavities, SIAM Journal on Numerical Analysis 18, 316–371](https://doi.org/10.1137/0718022) — Checked the publisher record/abstract and the explicitly attributed equations/table in ExactPack. The tabulated lambda 1.3943607838 is the value transcribed in that code, not an independent retranscription of the original table.
- critical-point-eigenvalue-formulation-used-by-ExactPack-eexp: [R. F. Chisnell (1998), An analytic description of converging shock waves, Journal of Fluid Mechanics 354, 357–375](https://doi.org/10.1017/S0022112097007775) — Checked the publisher record/abstract and the critical-point phase matching and equation 3.1 implementation in ExactPack eexp. The exponent is computed through that eigenvalue routine rather than fixed by dimensional analysis. The exponent was computed in the retained qualification; routine replay reuses the qualified value. Full eigenvalue shooting is an explicit separate regeneration step.
- ExactPack-software-reference: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX 24, 101560](https://doi.org/10.1016/j.softx.2023.101560) — Cites the ExactPack software paper and its Guderley solver listing. The paper version 1.7.5 is distinguished from the exact source commit used here, whose source, SHA receipts and BSD license are retained.
- actually-executed-semi-analytic-reference-source: [Los Alamos National Laboratory / ExactPack contributors (2025), ExactPack Guderley solver, pinned source](https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/guderley) — Inspected pinned eexp, the pre-collapse ODE/state, transcribed tables, official regression values and BSD 3 terms. This is not a claim to have run the complete ExactPack suite; actual reference execution is recorded separately. The selected exponent, pre-collapse ODE and eight original state probes were actually executed; qualification.json and pinned source/license hashes are archived with this release. The public Guderley class, reflected B solve and full ExactPack suite were not run. Routine replay reuses the recorded qualified lambda and freshly integrates the pinned pre-collapse ODE; it does not claim to repeat eexp shooting or the eight original-state probes by default. Their full regeneration is separately available.
#### 関連するテスト問題の図とコード

##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

![1次元球対称Eulerの保存済み半径密度を子午面に表示。γ=1.4、512球殻、r∈\[0,.75\]、R_s(−1)=.6、t=−.85。圧力ゼロの静止上流へ進む収束前の衝撃波を半解析参照と比較します。2D Cartesianや原点反射後の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

同じ問題への対応

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

- [実行・検証：Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) (`guderley-implosion`) · [コードZIP：Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

この実行例の範囲：冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。




### Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均

解析解 · 2次元

`q(x,t)=1_D(c+R(-t)(x-c)); qbar_K(t)=area(K intersect [c+R(t)(D-c)])/area(K), c=(0.5,0.5), T=2*pi. D=disk((0.5,0.75),0.15) minus {0.475<x<0.525,y<0.85}.`

単位正方形の2次元スカラー輸送です。速度(.5−y,x−.5)、角速度1、周期2π、中心(.5,.75)・半径.15の円盤から.475<x<.525かつy<.85のスロットを除き、内部1・外部0とします。公式Firedrake例の正規化した切り欠き円盤だけを取り出した変種で、bell・cone・背景値1・DG・流入境界は再現しません。周期有限体積の対向面では法線速度が一致します。連続解の台は境界から離れており、数値的な裾は別に測ります。参照は剛体回転の逆特性と円盤・多角形の解析的な面積積分によるセル平均で、点値を並べた画像や別PDE計算の細格子解ではありません。一回転後の連続形状への帰還と、位置・初期角度を変えた固定診断を区別します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-zalesak/#zalesak-rotation)

- historical-original-problem-attribution: [Steven T. Zalesak (1979), Fully multidimensional flux-corrected transport algorithms for fluids, Journal of Computational Physics 31, 335–362](https://doi.org/10.1016/0021-9991(79)90051-2) — Publisher bibliography and abstract checked. Direct full-text access was unavailable; no complete original-test transcription or FCT replication is claimed.
- official-setup-cross-check: [Firedrake project, DG advection demo: normalized slotted-cylinder geometry and rigid velocity](https://www.firedrakeproject.org/demos/DG_advection.py.html) — Inspected the official velocity, period and geometry definitions. This release isolates a 0–1 slotted disk and uses periodic finite volumes; the official bell/cone/background 1, DG scheme, inflow boundary and full Firedrake experiment are not reproduced or executed.
- official-demo-historical-context: [Randall J. LeVeque (1996), High-Resolution Conservative Algorithms for Advection in Incompressible Flow, SIAM Journal on Numerical Analysis 33, 627–665](https://doi.org/10.1137/0733033) — The official Firedrake demonstration attributes its rotating-body setup to this work. Its role here is contextual attribution, not a claim that the full paper or its numerical algorithm was implemented.
#### 関連するテスト問題の図とコード

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

![実際の2次元スカラー輸送の最細格子の保存セル平均。全\[0,1\]²のうちx∈\[.28,.72\], y∈\[.53,.97\]の円盤周辺を拡大し、一回転後の一次風上とminmod MUSCLを幾何学的な参照セル平均と比較します。切り欠きの数値拡散を残した図で、FCT法やEuler流体の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

同じ問題への対応

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

- [実行・検証：Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) (`zalesak-rotation`) · [コードZIP：Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

この実行例の範囲：スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。




### WENO臨界点：多項式セル平均と解析的周期輸送

解析解 · 1次元

`qbar_i=h^-1 integral_Ci q0(x-t)dx; q0=cos(2pi*x)+.1*sin(2pi*x)^3; local P=x+...+x^5, x²+x³+x⁴+x⁵, or x³+x⁴+x⁵.`

局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-weno-critical/#weno-critical-epsilon)

- Classical JS candidate/weight/indicator background; preprint finite-difference convention distinguished from this FV implementation: [Guang-Shan Jiang and Chi-Wang Shu (1996), Efficient Implementation of Weighted ENO Schemes](https://ntrs.nasa.gov/api/citations/19960007052/downloads/19960007052.pdf) — NASA-hosted ICASE95-73 preprint selected sections1–3: candidate Table1, optimal Table2, equations2.15–2.16 and3.1–3.9; text layer inspected, not full paper/numerical tables
- Original WENO-Z attribution and historical scope, not an actually inspected full-text formula source: [Rafael Borges, Monique Carmona, Bruno Costa and Wai Sun Don (2008), An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws](https://scholars.hkbu.edu.hk/en/publications/an-improved-weighted-essentially-non-oscillatory-scheme-for-hyper-2/) — Author-institution publication record and abstract inspected; publisher full text returned403; original full paper and numerical experiments not audited
- Actually inspected finite-volume cell-mean derivation of baseline JS/Z candidates, weights and power-two choice; embedded modifications excluded: [Bart S. van Lith, Jan H. M. ten Thije Boonkkamp and Wilbert L. IJzerman (2017), Embedded WENO: A design strategy to improve existing WENO schemes](https://pure.tue.nl/ws/portalfiles/portal/53481949/embedded_WENO.pdf) — Institution-hosted accepted manuscript section2 equations2–15 (PDF pages4–8) and selected section4.2 (PDF page22) text inspected; screenshot requests cache-missed; not a full-paper review
#### 関連するテスト問題の図とコード

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

関連モデルの問題

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

- [実行・検証：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

- [実行・検証：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

この実行例の範囲：同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

- [実行・検証：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) (`fr-periodic-advection`) · [コードZIP：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。




### 静止湖：表現した床の上の湿潤・露出平衡

解析解 · 1次元

`q_i=0; h_i=max(eta0-z_i,0); z_i=cellmean(z); eta0=.5 or .1.`

g9.81、[0,25]m、200セル。8<x<12の放物線床z=.2−.05(x−10)²をセルごとにGauss8で平均し、h_i=max(η₀−z_i,0)、q_i=0、η₀=.5/.1mを初期化します。静水再構成が保つのはこの表現した区分定数床の平衡であり、連続床上の水深平均をそのまま使う別問題ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/#swashes-topography)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
- original HR attribution: [E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004), A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows](https://epubs.siam.org/doi/abs/10.1137/S1064827503431090) — Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.
- directly inspected HR algebra: [E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016), Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system](https://arxiv.org/pdf/1409.3825) — arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.
#### 関連するテスト問題の図とコード

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

同じ問題への対応

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

- [実行・検証：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) (`swashes-topography`) · [コードZIP：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。




### SWASHES定常流：非射流Bernoulli根

半解析解 · 1次元

`q=4.42; h+z+q²/(2gh²)=2+q²/(8g); h>(q²/g)^(1/3).`

g9.81、[0,25]m、同じ放物線床、流量q4.42m²/s、下流h2m。h+z+q²/(2gh²)=2+q²/(8g)の非射流根を別の二分法で求め、セル平均求積を比較します。100/200/400セルのPDE計算は定常参照から初期化してt2まで進め、SWASHESの静止状態からの過渡計算そのものは再現しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/#swashes-topography)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
#### 関連するテスト問題の図とコード

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

同じ問題への対応

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

- [実行・検証：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) (`swashes-topography`) · [コードZIP：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。




### Ritter乾燥床破堤：g9.81の専用セル平均参照

解析解 · 1次元

`cL=sqrt(g*hL); h=(2*cL-(x-x0)/t)^2/(9*g), u=2*((x-x0)/t+cL)/3 inside fan; hR=0 beyond x0+2*cL*t.`

平坦・摩擦なしの[-10,10]m、堰x0=0、hL1m/hR0、初速0、g9.81、t.5s。左波頭−sqrt(g)tと真の乾燥前縁2sqrt(g)tで分割して保存量(h,hu)をセル平均します。固定水深.001mの等値線も区別します。旧参照カードと重力・領域・時刻の異なる専用入力で、旧値は変更しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/#dry-bed-dam-break)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
#### 関連するテスト問題の図とコード

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

同じ問題への対応

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

- [実行・検証：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`) · [コードZIP：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。




### Ghia Re100：原著の有限格子速度中心線

有限格子の数値参照 · 2次元

`u_ref(.5,y_j),v_ref(x_j,.5): original TablesI/II Re100; primary vortex(x,y)=(.6172,.7344): TableV.`

単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/#cavity-ghia-re100)

- primary-research-reference: [U. Ghia, K. N. Ghia and C. T. Shin (1982), High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method](https://www.sciencedirect.com/science/article/pii/0021999182900584) — Original PDF rendered and visually read:391–392 equations/Fig1;398–399 TablesI/II Re100 columns;408 TableV primary vortex. Publisher abstract/bibliography read; publisher PDF403. Original PDF obtained from recorded public mirror; no full-paper audit.
- actual-original-table-transcription-provenance: [Original Ghia TablesI/II andV transcription/source audit](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/source-review.json) — Original PDF selected printed391–392,398–399,408 visually inspected. PDF SHA2561d76e4636d24d0fad41c7bdb5ed383e9b224b0bfe3aa0317ce7dfc50619f2d93; public mirror is only its delivery location. Transcribed CSV accompanies the immutable release.
#### 関連するテスト問題の図とコード

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

同じ問題への対応

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

- [実行・検証：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) (`cavity-ghia-re100`) · [コードZIP：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

- [実行・検証：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) (`lbm-cavity-re100`) · [コードZIP：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

この実行例の範囲：4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。




### 壁面製造解：多項式速度と独立した圧力演算子

製造解 · 2次元

`psi*=8 f(x)f(y),f(z)=z²(1−z)²; s=u*omega*_x+v*omega*_y−nu*Delta omega*. Separate: p_op=x²+y²+sin(pi*x)sin(pi*y).`

単位正方形・ν.01・滑りなし、ψ*=8x²(1−x)²y²(1−y)²、u*=ψ*y、v*=−ψ*x、ω*=−Δψ*。連続の渦度式からs=u*ω*x+v*ω*y−νΔω*を構成し、独立の係数行列微分と照合します。PDE計算の壁渦度はキャビティと同じThom式で、厳密値を注入しません。p_op=x²+y²+sinπx sinπyの非零Dirichlet Poisson・勾配は別の演算子問題で、流れに結合した圧力やキャビティ圧力ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/#wall-manufactured)

- primary-research-reference: [Kambiz Salari and Patrick Knupp (2000), Code Verification by the Method of Manufactured Solutions](https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/) — Official Sandia/OSTI record and primary report printed12 at UNT read for MMS plus mesh refinement. No whole-report audit. Our quartic polynomial and pressure field are newly constructed.
#### 関連するテスト問題の図とコード

##### [非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

![実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

同じ問題への対応

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

- [実行・検証：非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja) (`wall-manufactured`) · [コードZIP：非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。




### レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照

解析解 · 2次元

`phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.3+0.2*t,0.35+0.1*t).`

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/)

- original-formulation-and-selected-reference-context: [S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations](https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf) — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- original-formulation-and-selected-reference-context: [C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries](https://www.sciencedirect.com/science/article/pii/0021999181901455) — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- original-formulation-and-selected-reference-context: [M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow](https://epubs.siam.org/doi/10.1137/S1064827596298245) — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- original-formulation-and-selected-reference-context: [M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows](https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf) — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.
#### 関連するテスト問題の図とコード

##### [レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

![実際の128²レベルセット場から抽出した円のゼロ等値線。左は平行移動、右は偏心円の一周回転。解析界面と移流単独・単純な再初期化ありを比較します。VOF計算ではなく、面積保存を補正していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

同じ問題への対応

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [実行・検証：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) (`level-set-translation`) · [コードZIP：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

- [実行・検証：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) (`level-set-rotation`) · [コードZIP：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。




### 偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照

解析解 · 2次元

`phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.5,0.5)+R(2*pi*t)(0.18,0).`

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/)

- original-formulation-and-selected-reference-context: [S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations](https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf) — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- original-formulation-and-selected-reference-context: [C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries](https://www.sciencedirect.com/science/article/pii/0021999181901455) — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- original-formulation-and-selected-reference-context: [M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow](https://epubs.siam.org/doi/10.1137/S1064827596298245) — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- original-formulation-and-selected-reference-context: [M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows](https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf) — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.
#### 関連するテスト問題の図とコード

##### [レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

![実際の128²レベルセット場から抽出した円のゼロ等値線。左は平行移動、右は偏心円の一周回転。解析界面と移流単独・単純な再初期化ありを比較します。VOF計算ではなく、面積保存を補正していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

同じ問題への対応

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [実行・検証：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) (`level-set-translation`) · [コードZIP：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

- [実行・検証：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) (`level-set-rotation`) · [コードZIP：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。




### 2D Poisson正弦製造解：SEMとP1 FEMの共通参照

製造解 · 2次元

`u(x,y)=sin(pi*x)*sin(pi*y); f=2*pi^2*u; grad u=(pi*cos(pi*x)*sin(pi*y),pi*sin(pi*x)*cos(pi*y)).`

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spectral-element/)

- executed-reference-implementation: [Atlas sem.py: sine value and gradient](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) — Locally chosen exact field evaluated in every fixed-input run; not an external Nek/PyFR execution.
#### 関連するテスト問題の図とコード

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

同じ問題への対応

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

- [実行・検証：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

- [実行・検証：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja) (`sa-amg`) · [コードZIP：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

この実行例の範囲：正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

- [実行・検証：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。




### FRとDGの周期正弦移流：平均0.4・T=.25の解析参照

解析解 · 1次元

`u(x,t)=0.4+sin(2*pi*(x-t)); speed1, period1, T=.25.`

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/flux-reconstruction/)

- executed-reference-implementation: [Atlas fr.py: analytic translation](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) — Locally chosen exact field evaluated in every fixed-input run; not an external Nek/PyFR execution.
#### 関連するテスト問題の図とコード

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

同じ問題への対応

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

- [実行・検証：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

- [実行・検証：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

この実行例の範囲：同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

- [実行・検証：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) (`fr-periodic-advection`) · [コードZIP：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。




### KH初期成長：独立した線形Fourier–Galerkin参照

有限格子の数値参照 · 2次元

`U=tanh(sin(y)/delta); omega_t=-U*omega_x-Uyy*psi_x+nu*Delta(omega); -Delta(psi)=omega; qhat(t)=exp(t*L_K)qhat(0).`

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。主計算は非線形2次元の点サンプルで、参照はkx=1の連続線形化IVPです。K24/40/56の切断を比較し、基底の微分は独立Fourier係数から評価します。鋭い界面の分散式を流用しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/#kh-initial-growth)

- selected-primary-reference-context: [Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012), A Well-Posed Kelvin-Helmholtz Instability Test and Comparison](https://arxiv.org/abs/1111.1764) — Read original sections1–3 on matching smooth finite-domain models and growth diagnostics; arXiv journal metadata checked. Our forced incompressible model is distinct.
#### 関連するテスト問題の図とコード

##### [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) (`kh-initial-growth`)

![保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#code-ja)

同じ問題への対応

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

- [実行・検証：KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja) (`kh-initial-growth`) · [コードZIP：KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

この実行例の範囲：実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。




### RT初期成長：Boussinesq二層の線形IVP参照

有限格子の数値参照 · 2次元

`b0=.02*tanh(sin(y)/delta); omega_t=nu*Delta(omega)+theta_x; theta_t=kappa*Delta(theta)+psi_x*b0prime; -Delta(psi)=omega.`

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。参照は同じ滑らかな基底のkx=1連続線形化をFourier–Galerkin K24/40/56で解きます。慣性密度は一定、浮力偏差θだけが鉛直力へ入り、周期二層の一方が不安定です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/#rt-initial-growth)

- selected-primary-reference-context: [Antonio Celani, Andrea Mazzino and Lara Vozella (2006), Rayleigh–Taylor turbulence in two dimensions](https://arxiv.org/abs/nlin/0510067) — Read original pp1–2 governing equations1–2 and doubly periodic Boussinesq setup. No original turbulent-run reproduction.
#### 関連するテスト問題の図とコード

##### [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) (`rt-initial-growth`)

![保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#code-ja)

同じ問題への対応

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

- [実行・検証：RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja) (`rt-initial-growth`) · [コードZIP：RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

この実行例の範囲：密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。




### 円偏波Alfvén波：全保存変数の解析セル平均

解析解 · 1次元

`sinc(h)=sin(pi*h)/(pi*h); theta=2*pi*(x-t); (Bybar,Bzbar)=.1*sinc(h)*(cos(theta),sin(theta)); (mybar,mzbar)=-(Bybar,Bzbar); rhobar=Bxbar=1; Ebar=.66.`

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。横磁場と横運動量にはsinc(h)を掛け、E=.66を保ちます。独立Gauss16求積と照合します。図のx–tは1次元空間と保存時刻であり、斜め2次元伝播ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-transport/#circular-alfven-refinement)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
#### 関連するテスト問題の図とコード

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

![保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

関連モデルの問題

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

- [実行・検証：円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) (`circular-alfven-refinement`) · [コードZIP：円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。




### 磁場ループ：固定Athena++の独立終端参照

有限格子の数値参照 · 2次元

`Az=.001*max(.3-sqrt(x*x+y*y),0); rho=p=1; v=(2,1,2); T=1; Uref_coarse=conservative_block_average(Uref_fine).`

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。未変更の公式生成器を固定コミット1395e2f…で実行し、Ny64/128と最細格子CFL半減で参照感度を確認します。比較は終端保存場のみで、保守的な粗視化後に評価します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-transport/#magnetic-loop-independent)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
#### 関連するテスト問題の図とコード

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

関連モデルの問題

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。

- [実行・検証：磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) (`magnetic-loop-independent`) · [コードZIP：磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。




### 後期Orszag–Tang：独立有限格子の密度・圧力参照

有限格子の数値参照 · 2次元

`rho0=25/(36*pi); p0=5/(12*pi); v=(sin(2*pi*y),-sin(2*pi*x),0); Az=(cos(4*pi*x)-2*cos(2*pi*y))/(4*pi*sqrt(4*pi)); T=.2.`

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-transport/#postshock-orszag-tang)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
- Historical attribution, not a reference table for this compressible ideal-MHD calculation: [Steven A. Orszag and Ching-Mao Tang (1979), Small-scale structure of two-dimensional magnetohydrodynamic turbulence](https://doi.org/10.1017/S002211207900210X) — Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
#### 関連するテスト問題の図とコード

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

関連モデルの問題

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

- [実行・検証：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja) (`ct-glm-independent`) · [コードZIP：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

この実行例の範囲：同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

- [実行・検証：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja) (`ct-glm-ot-convergence`) · [コードZIP：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

この実行例の範囲：同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

- [実行・検証：後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) (`postshock-orszag-tang`) · [コードZIP：後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。




### ALE：実際の移動セル上の解析積分と時間参照

解析解 · 1次元

`x(xi,t)=xi+.2*sin(2*pi*xi)*sin(2*pi*t)/(2*pi); m_i=integral_[x_i,x_(i+1)](1+.2*sin(2*pi*(x-.7*t)))dx.`

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。解析解q(x,t)=1+.2sin[2π(x−.7t)]を、主計算が保存した実際の面位置の間で積分します。解析面位置との幾何誤差を別記し、時間検査は同じFV ODEを二公差の独立DOP853で解きます。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/#ale-nonuniform-transport)

- selected-primary-reference-context: [Dennis L. Huff (1987), Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid](https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf) — NASA TM89890 grid-velocity and GCL discussion around equation11/printedp5 inspected. It attributes GCL to Thomas/Lombard. Original1979 paper not read; no airfoil algorithm or code reproduced. Our 1D scalar moving-volume/Heun derivation is independent.
#### 関連するテスト問題の図とコード

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

同じ問題への対応

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

- [実行・検証：非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`) · [コードZIP：非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

この実行例の範囲：質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。




### C-grid：連続Fourier解と離散記号の行列指数

解析解 · 2次元

`Q(t)=exp(t*L)Q0; ktilde=2*sin(k*h/2)/h; ltilde=2*sin(l*h/2)/h; C=cos(k*h/2)*cos(l*h/2); g=H=f=1.`

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。η₀=.01cos[2π(x+2y)]、u₀=v₀=0を、連続3×3 Fourier作用素と離散3×3記号の行列指数で別々に発展させます。主計算は実際の2次元staggered場を時間更新します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/#cgrid-rotating-wave)

- selected-primary-reference-context: [P. Korn and S. Danilov, Elementary dispersion analysis of some mimetic discretizations on triangular C-grids](https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf) — Governing linear equations, energy adjoints and AppendixB quadrilateral standard-C symbols/eq19–21 inspected. Use standard square C-grid only, not the paper triangular mimetic schemes. No global Williamson test or original code run.
#### 関連するテスト問題の図とコード

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

同じ問題への対応

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

- [実行・検証：2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`) · [コードZIP：2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

この実行例の範囲：実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。




### L字角の特異解：調和場と別の滑らかな製造解

解析解 · 2次元

`u=r^(2/3)*sin(2*theta/3); -Delta(u)=0; theta in[0,3*pi/2]; separate square MMS u=sin(pi*x)*sin(pi*y).`

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。角の解析解と勾配を要素求積し、一様格子と事前graded格子を同じ自由度で比べます。別の単位正方形でsin(πx)sin(πy)をregular/warped格子へ置き、特異性と歪みを分けます。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#lshape-fem)

- selected-primary-reference-context: [Long Chen, Introduction to Adaptive Finite Element Methods](https://lyc102.github.io/ifem/afem/) — Author documentation: L-shaped harmonic r^(2/3)sin(2theta/3) field and non-quasiuniform refinement motivation inspected. No MATLAB code copied or run; our removed quadrant/angle convention is explicitly defined.
- selected-primary-reference-context: [Joachim Schöberl, Interactive FEM: graded meshes around vertex singularities](https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html) — Section24.4 weighted regularity and graded meshes inspected. Our fixed max-norm radial map is independently constructed; no general AMR implementation or universal optimality theorem claimed.
#### 関連するテスト問題の図とコード

##### [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) (`lshape-fem`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#code-ja)

同じ問題への対応

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

- [実行・検証：L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja) (`lshape-fem`) · [コードZIP：L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。




### 環状粘性ベクトルMMS：独立応力微分で外力を確認

製造解 · 2次元

`s=x*x+y*y; A=(s-1)*(4-s); u=(A*(1+x*y),A*(x*x-y*y)/2); mu=1+.2*s; f=-div(2*mu*epsilon(u)).`

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。s=x²+y²、A=(s−1)(4−s)のCartesianベクトル場から応力と外力を解析的に導き、別のCartesian差分応力微分で確認します。体積外力の独立積分(756π/5,0)も照合します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#annular-viscous-mms)

- selected-primary-reference-context: [MFEM developers, Example2: Linear Elasticity](https://mfem.org/examples/) — Example2 stress sigma=lambda div(u)I+mu(grad(u)+grad(u)^T), weak formulation and traction conventions inspected. Use lambda0 as a linear vector viscous BVP; manufactured fields are derived here. MFEM not executed or copied.
#### 関連するテスト問題の図とコード

##### [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

同じ問題への対応

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

- [実行・検証：環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`) · [コードZIP：環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。




### 純Neumann：解析場・互換条件・平均値ゲージ

製造解 · 2次元

`u=cos(2*pi*x)*cos(2*pi*y)+mean; f=8*pi^2*cos(2*pi*x)*cos(2*pi*y); dn(u)=0; integral(f)=-integral_boundary(dn(u)).`

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。u=cos(2πx)cos(2πy)、f=8π²u、外向き法線流束0を点DOFで比較します。平均0と平均.25を分け、source+1の物理的不適合を投影で隠さず拒否します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#poisson-neumann)

- selected-primary-reference-context: [PETSc developers, KSP: Solving Singular Systems](https://petsc.org/main/manual/ksp/) — Solving Singular Systems: constant Neumann nullspace and RHS compatibility inspected. We reject physical incompatibility rather than projecting it away. PETSc is neither a dependency nor executed.
#### 関連するテスト問題の図とコード

##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

同じ問題への対応

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

- [実行・検証：純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) (`poisson-neumann`) · [コードZIP：純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。




### 混合Robin：2次元解析場と独立な法線流束

製造解 · 2次元

`u=cos(pi*x)*cos(2*pi*y)+x+y; -Delta(u)=5*pi^2*cos(pi*x)*cos(2*pi*y); alpha*u+beta*dn(u)=g.`

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。f=5π²cos(πx)cos(2πy)を使い、x壁は外向きNeumann±1、y壁はαu+β∂nu=gの解析値です。境界条件の代数残差と、解析的な物理法線流束の誤差を別々に測ります。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#poisson-robin)

- selected-primary-reference-context: [MFEM developers, Boundary Conditions: Robin boundary conditions](https://mfem.org/fem_bc/) — Outward normal derivative and Robin weak boundary contribution inspected; Example27 source overview inspected. Our cell-centred face elimination/MMS is separately derived; no MFEM execution.
#### 関連するテスト問題の図とコード

##### [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

同じ問題への対応

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

- [実行・検証：2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja) (`poisson-robin`) · [コードZIP：2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。




### 相対論的対称衝突：特殊化した二衝撃波Taub参照

半解析解 · 1次元

`h_b^2-h_a^2=(p_b-p_a)*(h_b/rho_b+h_a/rho_a); v0^2=(p_b-p_a)*(e_b-e_a)/((e_a+p_b)*(e_b+p_a)); shock positions=.5 +/- Vs*t.`

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。Taub断熱式と相対速度式の圧力根から静止した同一星状態と衝撃波速度を求め、保存変数の区分一定厳密場をセル積分します。接触面は退化し、一般三波Riemannソルバーではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/#srhd-collision)

- selected-primary-reference-context: [Luciano Rezzolla and Olindo Zanotti (2001), An Improved Exact Riemann Solver for Relativistic Hydrodynamics](https://arxiv.org/abs/gr-qc/0103005) — Original arxiv v2 read: sections2–4, equations2.3/2.4,3.1 and4.5; restricted two-shock specialization. No whole-paper or generic Riemann implementation audit.
- selected-primary-reference-context: [José A. Font (2008), Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity](https://link.springer.com/article/10.12942/lrr-2008-7) — Official article sections3.1–3.2, tensor49–51 and recovery68–69 actually read. Flat-spacetime use only; no whole-review or complete-GRMHD implementation audit.
#### 関連するテスト問題の図とコード

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

同じ問題への対応

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

- [実行・検証：SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) (`srhd-collision`) · [コードZIP：SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

この実行例の範囲：相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。




### SRMHD円偏波：有限振幅厳密族と独立テンソル積分

解析解 · 1次元

`K=rho*h+B0^2*(1+eta^2); vA^2=2*B0^2/(K+sqrt(K^2-4*eta^2*B0^4)); (By,Bz)=eta*B0*(cos(2*pi*(x-vA*t)),sin(2*pi*(x-vA*t))); (vy,vz)=-vA*(By,Bz)/B0.`

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。非線形Alfvén速度の閉じた式を使い、点の原始変数から独立なストレステンソルで保存量と流束を作り、Gauss積分と複素段階PDE残差で確認します。原著の2π周期を単位区間へ移しています。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/#srmhd-alfven)

- selected-primary-reference-context: [L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007), ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics](https://arxiv.org/abs/0704.3206) — University-hosted original journal PDF section4.1 equations82–85 read; original arxiv preprint pages9–10 rendered and visually inspected, including normalization and period. Publisher PDF403. No whole-paper or ECHO-algorithm reproduction claim.
- selected-primary-reference-context: [José A. Font (2008), Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity](https://link.springer.com/article/10.12942/lrr-2008-7) — Official article sections3.1–3.2, tensor49–51 and recovery68–69 actually read. Flat-spacetime use only; no whole-review or complete-GRMHD implementation audit.
#### 関連するテスト問題の図とコード

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

同じ問題への対応

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

- [実行・検証：SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) (`srmhd-alfven`) · [コードZIP：SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

この実行例の範囲：完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。




### 係数ジャンプ拡散：共有流束とMG・AMG

有限格子の数値参照 · 2次元

`-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}; T_f=|f|/(d_L/a_L+d_R/a_R)`

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。 非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/#checkerboard-diffusion)

- selected-official-formulation-context: [Two-point flux approximation](https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html) — Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.
- selected-official-formulation-context: [BoomerAMG: smoother options](https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html) — CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.
- publisher-abstract-only: [Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems](https://link.springer.com/article/10.1007/BF02238511) — Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.
#### 関連するテスト問題の図とコード

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

同じ問題への対応

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

- [実行・検証：係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`) · [コードZIP：係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

この実行例の範囲：不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。




### 回転異方性拡散：完全テンソルQ1とMG・AMG

製造解 · 2次元

`-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T; f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y`

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。 u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/#rotated-anisotropic-diffusion)

- selected-official-formulation-context: [Two-point flux approximation](https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html) — Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.
- selected-official-formulation-context: [BoomerAMG: smoother options](https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html) — CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.
- publisher-abstract-only: [Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems](https://link.springer.com/article/10.1007/BF02238511) — Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.
#### 関連するテスト問題の図とコード

##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

同じ問題への対応

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

- [実行・検証：回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`) · [コードZIP：回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

この実行例の範囲：非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。




### 中性長方形スラブ：真2P参照とYB補正

半解析解 · 3次元

`phi=real2P+nonzero_modes+zero_mode-2alpha*q/sqrt(pi); E=.5sum(q*phi); F=-q grad(phi); DeltaE=2pi*Mz^2/V; DeltaFz=-4pi*q*Mz/V.`

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。 参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-slab-ewald/#neutral-slab-yb)

- reference-formula-or-scoped-context: [Fast and spectrally accurate Ewald summation for2-periodic electrostatic systems](https://arxiv.org/pdf/1109.1667) — Eq4 and AppendixA Eq41/zero-mode inspected; rendered selected pages requested. No full-paper audit or spectral-PME implementation claimed.
- reference-formula-or-scoped-context: [Ewald summation for systems with slab geometry](https://doi.org/10.1063/1.479595) — Original publisher full text unavailable; no original-text review claimed. Neutral correction independently derived and checked against official LAMMPS implementation/documentation.
- reference-formula-or-scoped-context: [LAMMPS slab Ewald documentation and neutral correction](https://docs.lammps.org/kspace_modify.html) — Slab geometry restrictions and official Ewald::slabcorr neutral formula inspected. No LAMMPS code copied or executed; mutable stable source is contextual, not a numerical dependency.
#### 関連するテスト問題の図とコード

##### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#code-ja)

同じ問題への対応

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

- [実行・検証：中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`) · [コードZIP：中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

この実行例の範囲：4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。




### 真3D 1/r FMM：多段変換・力・適応所有権

有限格子の数値参照 · 3次元

`Phi_i=-sum_{j!=i}G*m_j/r_ij; a_i=-sum_{j!=i}G*m_j*(x_i-x_j)/r_ij^3; finite6axis source Phi(0)=-1/a.`

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。 有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-fmm3d/#fmm3d-inverse-r)

- reference-formula-or-scoped-context: [The black-box fast multipole method](https://mc.stanford.edu/cgi-bin/images/f/fa/Darve_bbfmm_2009.pdf) — Tensor interpolation Eq7 and multilevel stages sections2–3 inspected, printed8715–8717; compression is separate. Original uncompressed educational implementation here, no timing reproduction.
- reference-formula-or-scoped-context: [FMM3D mathematical definitions](https://fmm3d.readthedocs.io/en/latest/math.html) — Official potential+1/(4pi r), gradient and source-self convention inspected. Our gravitational kernel is-1/r; FMM3D is not installed or run.
#### 関連するテスト問題の図とコード

##### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#code-ja)

同じ問題への対応

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

- [実行・検証：真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`) · [コードZIP：真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

この実行例の範囲：非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。




### 無軟化Kepler二体の時間誤差

解析解 · 3次元

`E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).`

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/#gravity-kepler)

- reference-formula-or-scoped-context: [JPL Keplerian-element formulas](https://ssd.jpl.nasa.gov/planets/approx_pos.html) — Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.
- reference-formula-or-scoped-context: [Geometric numerical integration illustrated by the Störmer–Verlet method](https://doi.org/10.1017/S0962492902000144) — Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.
#### 関連するテスト問題の図とコード

##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

同じ問題への対応

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

- [実行・検証：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) (`gravity-kepler`) · [コードZIP：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。




### 冷たいPlummer密度由来32粒子の短時間力学

有限格子の数値参照 · 3次元

`a_i=-sum_{j!=i}G*m_j*r_ij/(r_ij^2+eps^2)^(3/2); U=-sum_{i<j}G*m_i*m_j/sqrt(r_ij^2+eps^2).`

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。 非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/#gravity-plummer-short)

- reference-formula-or-scoped-context: [On the Problem of Distribution in Globular Star Clusters](https://academic.oup.com/mnras/article/71/5/460/972150) — Bibliography inherited from prior scoped source review; original full text not read. The finite32-body cold initial condition is density-derived, not an equilibrium Plummer DF or exact continuum flow.
- reference-formula-or-scoped-context: [galpy official Plummer potential definition](https://docs.galpy.org/en/v1.11.0/reference/potentialplummer.html) — Official potential normalization read in preparatory source review. No galpy execution; density scale1 and pair softening.05 are distinct parameters.
- reference-formula-or-scoped-context: [SciPy1.14.1 solve_ivp](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html) — DOP853 order8, tolerance and t_eval semantics inspected; same softened finite-N ODE with independent scalar pair force. Not an exact analytic N-body solution.
- reference-formula-or-scoped-context: [Geometric numerical integration illustrated by the Störmer–Verlet method](https://doi.org/10.1017/S0962492902000144) — Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.
#### 関連するテスト問題の図とコード

##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

同じ問題への対応

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

- [実行・検証：冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`) · [コードZIP：冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。




### 温かいPICの線形Landau減衰

半解析解 · 1次元

`D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).`

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-warm-pic/#thermal-landau-damping)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
- selected-primary-context: [Plasma dispersion function: official API mathematics](https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html) — Read the displayed integral definition and Maxwellian dispersion role. PlasmaPy is not installed or executed; SciPy Faddeeva is used with an independently derived dielectric.
- selected-primary-context: [SciPy1.14.1 roots_hermitenorm](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html) — Read Gauss–Hermite normal quadrature definition, exp(-x²/2) weight and degree2n-1 polynomial exactness. Used only for positive full-f initial particle weights; no Hermite PDE time evolution.
#### 関連するテスト問題の図とコード

##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

![実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

同じ問題への対応

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

- [実行・検証：温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`) · [コードZIP：温かいPICの線形Landau減衰](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

この実行例の範囲：熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。




### 温かいPICの二流初期成長

半解析解 · 1次元

`D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).`

各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-warm-pic/#thermal-two-stream)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
- selected-primary-context: [Plasma dispersion function: official API mathematics](https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html) — Read the displayed integral definition and Maxwellian dispersion role. PlasmaPy is not installed or executed; SciPy Faddeeva is used with an independently derived dielectric.
- selected-primary-context: [SciPy1.14.1 roots_hermitenorm](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html) — Read Gauss–Hermite normal quadrature definition, exp(-x²/2) weight and degree2n-1 polynomial exactness. Used only for positive full-f initial particle weights; no Hermite PDE time evolution.
#### 関連するテスト問題の図とコード

##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

![実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓\[12,20\]とは分けます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

同じ問題への対応

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

- [実行・検証：温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) (`thermal-two-stream`) · [コードZIP：温かいPICの二流初期成長](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

この実行例の範囲：温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。




### PIC空間演算の独立実装照合

有限格子の数値参照 · 1次元

`rho=-.5cos(2x) => E=-.25sin(2x), electron a=+.25sin(2x); independent scalar CIC + dense DFT owns its self-consistent field every kick.`

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-pic-spatial/#pic-independent-spatial)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
#### 関連するテスト問題の図とコード

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

関連モデルの問題

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

- [実行・検証：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) (`pic`) · [コードZIP：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

- [実行・検証：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja) (`pic-conservation`) · [コードZIP：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

- [実行・検証：PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) (`pic-independent-spatial`) · [コードZIP：PIC空間演算の独立実装照合](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

この実行例の範囲：ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。




### 硬球DSMCの有限Kn Couette流

有限格子の数値参照 · 1次元

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-wall/#dsmc-couette)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### 関連するテスト問題の図とコード

##### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja) (`dsmc-couette`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#code-ja)

同じ問題への対応

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

- [実行・検証：硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja) (`dsmc-couette`) · [コードZIP：硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。




### 硬球DSMCの有限Kn Fourier熱伝導

有限格子の数値参照 · 1次元

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-wall/#dsmc-fourier)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### 関連するテスト問題の図とコード

##### [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) (`dsmc-fourier`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#code-ja)

同じ問題への対応

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

- [実行・検証：硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja) (`dsmc-fourier`) · [コードZIP：硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。




### 硬球DSMCのMach2平面衝撃波

有限格子の数値参照 · 1次元

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。 各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-shock/#dsmc-planar-shock)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### 関連するテスト問題の図とコード

##### [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#code-ja)

同じ問題への対応

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

- [実行・検証：硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`) · [コードZIP：硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。




### LBMのRe100キャビティ：実2D場とGhia中心線

有限格子の数値参照 · 2次元

`Ghia1982Re100 centerline tables and primary-vortex location; these are rounded numerical data,not an exact whole-field solution.`

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-cavity/#lbm-cavity-re100)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.
- case-method-or-independent-reference: [High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method](https://www.sciencedirect.com/science/article/pii/0021999182900584) — Exact-byte existing17-point Re100columns and prior original-PDF/rendered-page provenance rechecked. Current session did not reacquire the original PDF. Printed398-399TablesI/II and408TableV provenance retained.
#### 関連するテスト問題の図とコード

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

関連モデルの問題

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

- [実行・検証：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) (`cavity-ghia-re100`) · [コードZIP：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

- [実行・検証：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) (`lbm-cavity-re100`) · [コードZIP：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

この実行例の範囲：4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。




### LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度

解析解 · 2次元

`u=U sin(x)cos(y) exp(-2nu t), v=-U cos(x)sin(y) exp(-2nu t); p=U^2 exp(-4nu t)[cos(2x)+cos(2y)]/4.`

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-taylor-green/#lbm-taylor-green)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.
#### 関連するテスト問題の図とコード

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

関連モデルの問題

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

- [実行・検証：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

- [実行・検証：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) (`lbm-taylor-green`) · [コードZIP：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

この実行例の範囲：周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。




### 曲面LBMの環状Couette制御：速度・圧力・トルク

解析解 · 2次元

`u_theta=Ar+B/r; p=A^2r^2/2+2AB log(r)-B^2/(2r^2)+C; T_inner=-4pi rho nu B.`

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-annulus/#lbm-annular-couette-control)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Selected original sec3 printed410-414 via disclosed author-content mirror: Eq12/13/14 quadratic reflected-characteristic interpolation,moving-wall coefficient,Eq15 momentum exchange and compromised mass conservation. Generic Lagrange scalar oracle independently qualifies weights andsigns. No localPDF/rendered-symbol audit;2001BFLfulloriginal remains unread.
#### 関連するテスト問題の図とコード

##### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

同じ問題への対応

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

- [実行・検証：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`) · [コードZIP：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

この実行例の範囲：実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。




### 実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界

有限格子の数値参照 · 2次元

`Re=Umean D/nu=20; CD=2Fx/(rho Umean^2 D); CL=2Fy/(rho Umean^2 D); delta p=p(.15,.2)-p(.25,.2).`

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-curved-boundary/#lbm-cylinder-re20)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Selected original sec3 printed410-414 via disclosed author-content mirror: Eq12/13/14 quadratic reflected-characteristic interpolation,moving-wall coefficient,Eq15 momentum exchange and compromised mass conservation. Generic Lagrange scalar oracle independently qualifies weights andsigns. No localPDF/rendered-symbol audit;2001BFLfulloriginal remains unread.
- case-method-or-independent-reference: [Benchmark Computations of Laminar Flow Around a Cylinder](https://kent-and.github.io/mek4250/2021/SchaeferTurek1996.pdf) — Original chapter delivered by course mirror after official links404: printed3-4geometry/2D-1/force definitions,7protocol user-selected outlet,11-12Table3 estimated ranges. Not a full-paper or separate local rendered-symbol audit.
- case-method-or-independent-reference: [DFG flow around cylinder benchmark2D-1, Re20](https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark1_re20.html) — Actual geometry,do-nothingBC,mean-speed normalization,force/probe definitions and Nabh1998attribution read. Nabh original report not read; its precise values are contextual,not the adopted outlet truth.
- case-method-or-independent-reference: [Non-equilibrium extrapolation method for velocity and pressure boundary conditions in the lattice Boltzmann method](https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310) — Official primary abstract actually read: equilibrium/nonequilibrium split and adjacent-fluid extrapolation. Full primary equations unavailable; the adopted all-nine poststream density reservoir is independently derived and qualified,not labelled the exact author implementation.
#### 関連するテスト問題の図とコード

##### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

同じ問題への対応

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

- [実行・検証：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`) · [コードZIP：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

この実行例の範囲：標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。




### 等方散乱平板：連続角Fredholm流束参照

半解析解 · 1次元

`J(x)=.5*E2(x)+omega/2*integral_0^L E1(|x-y|)J(y)dy; R=2omega*integral J E2(x)dx; T=2E3(L)+2omega*integral J E2(L-x)dx; A=4(1-omega)*integral J dx.`

平行平板の定常な光学厚さ座標を用い、左の入射放射輝度は1、右の入射は真空、等方散乱の単一散乱アルベドを固定します。入射半球流束はπ、符号付き角度の平均はJ=(1/2)∫I dμです。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-scattering/#isotropic-scattering-slab)

- transfer-equation-and-boundary-convention: [Pharr,Jakob and Humphreys, Physically Based Rendering4e: The Equation of Transfer](https://www.pbr-book.org/4ed/Light_Transport_II_Volume_Rendering/The_Equation_of_Transfer) — Read selected transfer/source/finite-ray boundary section. The isotropic Fredholm normalization,independent exact-cell E1weights and flux derivations are documented in this packet; no DISORT reproduction or Monte Carlo claim.
#### 関連するテスト問題の図とコード

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

同じ問題への対応

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

- [実行・検証：等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`) · [コードZIP：等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

この実行例の範囲：正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。




### Su–Olson1996拡散：固定版の独立積分評価関数

半解析解 · 1次元

`epsilon*u_tau-u_xx=v-u; v_tau=u-v; u(0,tau)-2/sqrt(3)*u_x(0,tau)=1; u(infinity,tau)=0; epsilon*u+v is the capacity-weighted total.`

初期の放射・物質変数が0、ε=1の半無限Marshak拡散です。無次元評価関数を直接用い、物理単位の質量吸収係数ラッパーに起因する曖昧な規約は持ち込みません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/#su-olson-diffusion1996)

- original-problem: [B. Su and G. L. Olson (1996), Benchmark results for the non-equilibrium Marshak diffusion problem, JQSRT56(3),337–351](https://doi.org/10.1016/0022-4073(96)84524-9) — Publisher abstract and bibliographic metadata read; original full text/equations/tables unavailable and not directly checked. Diffusion is distinct from the1997transport problem.
- reference-software-paper: [J. Thrussell and J. M. Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Bibliographic software credit,recorded separately from Su–Olson1996 and the pinned executed source. Full software paper is not claimed read.
- executed-reference-implementation: [LANL ExactPack1.7.5, pinned SuOlson/Timmes evaluator](https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson) — All55documentation,41wrapper and348Timmes module lines read. Execute nondimensional usolution/vsolution serially; qualify selected original/tight integrals against sensitivity,PDE and Robin checks. No primary solver shares this evaluator. Full ExactPack/base/library audit is not claimed.
- reference-source-license: [LANL ExactPack pinned BSD-3-Clause license](https://github.com/lanl/ExactPack/blob/8718b61f281a9744ea7a3820c51800915e4636e9/LICENSE.txt) — Actual license text read and retained as exactpack-LICENSE.txt with redistributed inert source snapshots.
#### 関連するテスト問題の図とコード

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

同じ問題への対応

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

- [実行・検証：Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`) · [コードZIP：Su–Olson1996非平衡拡散](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

この実行例の範囲：実際の放射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。




### Su–Olson輸送：2023著者公開の独立解析ベンチマーク表

有限格子の数値参照 · 1次元

`epsilon*I_tau+mu*I_x+I=V+Q; V_tau=E-V; E=.5*integral_-1^1 I dmu; I=2U of Crilly2023Appendix4.1; conserved total epsilon*E+V. Separate periodic companion: epsilon*I_t+mu*I_x=kappa*(V-I), V_t=kappa*(E-V); F approximately -E_x/(3*kappa), (epsilon+1)*E_t approximately E_xx/(3*kappa). For h=2*pi/N, A_N=.1*sin(h/2)/(h/2), E_diff=V_diff=1+A_N*exp[-s/(3*(epsilon+1))]*cos(x), t=kappa*s.`

無限領域の対称1次元角度輸送と物質交換で、ε=1、弾性散乱なし、低温の零初期状態です。Q=1を|x|<0.5、0<τ<10に与えます。主計算は左反射・十分遠い右入射真空の半領域で、比較時刻は境界の影響前です。別の同条件比較用の周期セル平均制御は、物理座標x∈[0,2π)、c=ε=1、κ=4/8/16、N=128/512/2048、Q=0、初期I=V=1+0.1cos(x)、s=0/.0625/.125/.25に対するt=κsを用います。この制御は1997のsource駆動問題とは初期・境界・sourceが異なり、制御内のFV・連続角度参照・拡散比較に同じ入力を用います。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/#su-olson-transport1997)

- original-problem: [B. Su and G. L. Olson (1997), An analytical benchmark for non-equilibrium radiative transfer in an isotropically scattering medium, Annals of Nuclear Energy24(13),1035–1055](https://doi.org/10.1016/S0306-4549(96)00100-4) — Publisher abstract/metadata read only. Original full text,integral normalization and original numerical tables were not directly read or transcribed. The actual comparison is independently attributed to the selected2023author repository below.
- primary-author-model-normalization: [A. Crilly (2023), Learning closure relations using differentiable programming: an example in radiation transport](https://raw.githubusercontent.com/ml4physicalsciences/ml4physicalsciences.github.io/master/2023/files/NeurIPS_ML4PS_2023_16.pdf) — Actually read and visually verified PDFpage6 Appendix4.1 equations7–10: epsilon*d_tau U+mu*d_x U+U=V/2+Q/2,V_tau=W−V. With I=2U, E=W. epsilon1,x0=.5,source duration10; no direct original1997-table verification.
- qualified-independent-published-data: [A. Crilly RTClosureJAX pinned SuOlsonData analytical benchmark tables](https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData) — Pinned W/Vtransport data,coordinates,times and README actually read. Repository calls them analytical Su–Olson data; transcription versus regeneration is undocumented. They are not trained-closure/model predictions. Retain full15×7raw table; compare13points at tau.1,1,3.16228 with matching source/epsilon/units. Rounded five-decimal finite data,not a rigorous exact reference.
- reference-data-license: [RTClosureJAX pinned MIT license](https://github.com/aidancrilly/RTClosureJAX/blob/3e4f636299d62bc03f7118cfc884230c756f9d87/LICENSE) — Actual MIT license read and retained with the bundled raw table. No redistribution of the2023paper PDF is required by this packet.
- shared-exponential-action-API: [SciPy1.14.1 expm_multiply: matrix exponential action and trace preconditioning](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.expm_multiply.html) — Actually inspected installed1.14.1 source/API docstring and the versioned official API action/traceA section. Shared by the new FV-mode and continuum-reference propagators; mathematical action equivalence is not bit equivalence or independent-engine evidence. The linked algorithm papers were not read as part of this update.
- independent-reference-propagator-qualification: [SciPy1.14.1 solve_ivp: DOP853 and complex initial states](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html) — Read selected official API sections for complex initial states,DOP853 and fixed tolerances. Two separately written continuum derivatives are compared to the shared exponential action under frozen141checks. This is finite reference qualification,not a primary SSPRK2 order test or a rigorous bound; original DOP853 papers were not reviewed here.
#### 関連するテスト問題の図とコード

##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

同じ問題への対応

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

- [実行・検証：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`) · [コードZIP：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

この実行例の範囲：物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。




### 円形吸収体の特性線参照

解析解 · 2次元

`I(x,y,t)=I_in(y)*exp(-kappa*ell_circle(x,y))*1_(x<t); Pxx=E,Pyy=Pzz=0 for the+xray.`

2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-geometry/#shadow-absorber2d)

- closure-and-model-limitations: [J. Rosdahl etal. (2013), RAMSES-RT: Radiation hydrodynamics in the cosmological context](https://arxiv.org/html/1304.7126v2) — Read selectedSection2 equations12–14 and opposing-beam limitation text. The static grey equations here are neither GR nor reproductions of RAMSES astrophysical calculations. Original Levermore1984 full text was not read.
- qualified-M1-numerical-method-context: [A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method](https://arxiv.org/pdf/1306.0010) — Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound. Actual generalized directional LF core passed762component checks,then all166fixed geometry gates. The authored LFcone proof is separate from the paper;no general nonlinearRiemannfan bound is claimed.
#### 関連するテスト問題の図とコード

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

同じ問題への対応

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

- [実行・検証：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`) · [コードZIP：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。




### 反向伝播packetの特性線参照

解析解 · 2次元

`Iplus(x,y,t)=6G(x-t,y;.25); Iminus(x,y,t)=6G(x+t,y;.75); E=Gplus+Gminus,Fx=Gplus-Gminus,Fy=0; Pxx=E,Pyy=Pzz=0.`

2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-geometry/#opposing-beams2d)

- closure-and-model-limitations: [J. Rosdahl etal. (2013), RAMSES-RT: Radiation hydrodynamics in the cosmological context](https://arxiv.org/html/1304.7126v2) — Read selectedSection2 equations12–14 and opposing-beam limitation text. The static grey equations here are neither GR nor reproductions of RAMSES astrophysical calculations. Original Levermore1984 full text was not read.
- qualified-M1-numerical-method-context: [A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method](https://arxiv.org/pdf/1306.0010) — Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound. Actual generalized directional LF core passed762component checks,then all166fixed geometry gates. The authored LFcone proof is separate from the paper;no general nonlinearRiemannfan bound is claimed.
#### 関連するテスト問題の図とコード

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

同じ問題への対応

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

- [実行・検証：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) (`opposing-beams2d`) · [コードZIP：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。




### GBMのweak誤差とMonte Carlo標準誤差

解析解 · 1次元

`dX_t=\mu X_t\,dt+\sigma X_t\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \mathbb E[X_h(T)]=X_0(1+\mu h)^n`

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-accuracy/#gbm-weak-moments)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### 関連するテスト問題の図とコード

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

関連モデルの問題

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [実行・検証：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) (`gbm-sde`) · [コードZIP：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

この実行例の範囲：スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [実行・検証：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja) (`gbm-weak-moments`) · [コードZIP：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

- [実行・検証：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja) (`gbm-milstein-strong`) · [コードZIP：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。




### OUのweakモーメントと同時Brownian結合

解析解 · 1次元

`dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa`

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-accuracy/#ou-weak-moments)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### 関連するテスト問題の図とコード

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

![調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

関連モデルの問題

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [実行・検証：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja) (`langevin-harmonic`) · [コードZIP：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

- [実行・検証：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja) (`csvr-langevin-harmonic`) · [コードZIP：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

- [実行・検証：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja) (`ou-weak-moments`) · [コードZIP：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。




### 同じBrownian経路のMilstein・EM strong比較

解析解 · 1次元

`X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]; \mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]`

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-accuracy/#gbm-milstein-strong)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### 関連するテスト問題の図とコード

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

関連モデルの問題

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

- [実行・検証：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) (`gbm-sde`) · [コードZIP：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

この実行例の範囲：スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [実行・検証：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja) (`gbm-weak-moments`) · [コードZIP：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

- [実行・検証：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja) (`gbm-milstein-strong`) · [コードZIP：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。




### 正規稀少尾の通常importance sampling

解析解 · 1次元

`\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}; \mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)`

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/#normal-tail-importance)

- selected-primary-definition-or-diagnostic-algorithm: [Monte Carlo theory,methods and examples,Chapter9: importance sampling](https://artowen.su.domains/mc/Ch-var-is.pdf) — Selected author-chapter support,ordinary estimator,second moments and diagnostics were read during preparation. Current refetch returned403. No full-book or PERT experiment reproduction.
#### 関連するテスト問題の図とコード

##### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja) (`normal-tail-importance`)

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#code-ja)

同じ問題への対応

重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

- [実行・検証：正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja) (`normal-tail-importance`) · [コードZIP：正規稀少尾の通常importance sampling](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

この実行例の範囲：通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。




### 相関2変量Gaussianのjoint標的とMCSE

有限格子の数値参照 · 2次元

`\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]; \operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}`

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/#correlated-gaussian-mcmc)

- selected-primary-definition-or-diagnostic-algorithm: [Rank-normalization,folding,and localization: An improved R-hat for assessing convergence of MCMC](https://arxiv.org/pdf/1903.08008) — Read selected original rank/foldedRhat,ESS and corrected Blom equation. No multivariate global-convergence certificate.
- selected-primary-definition-or-diagnostic-algorithm: [ArviZ0.20.0 public diagnostics API and selected implementation](https://python.arviz.org/en/v0.20.0/api/generated/arviz.mcse.html) — Read official0.20.0 ESS/MCSE source and API. Cache640values from128same-data observable/prefix arrays of8fixed chainsets in a separate process. Independence is the diagnostic engine,not an independent sampler.
#### 関連するテスト問題の図とコード

##### [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja) (`correlated-gaussian-mcmc`)

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja#code-ja)

同じ問題への対応

診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。

- [実行・検証：相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja) (`correlated-gaussian-mcmc`) · [コードZIP：相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

この実行例の範囲：実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。




### 誘電体円柱の外部級数と散乱幅

解析解 · 2次元

`E_z^{\mathrm{sca}}=\sum_n i^n a_nH_n^{(1)}(kr)e^{in\theta},\quad\Sigma_{\mathrm{sca}}=4\sum_n|a_n|^2/k`

無損失無限円柱、Ez偏光、c=ε0=μ0=1、半径0.25、ε=2.25、真空波長1。解析場は厳密な円の外部だけです。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-cylinder/#cylinder-mie2d)

- selected-primary-documentation-or-authored-identity: [Mie scattering 2D](https://optics.ansys.com/hc/en-us/articles/360042703373-Mie-scattering-2D) — Read the complete substantive benchmark description: two-dimensional dielectric cylinder, TFSF, angular far field and lossless cross sections. Did not read the associated simulation files, theory table or cited book; no external numerical data imported. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- selected-primary-documentation-or-authored-identity: [Bessel and Hankel Wronskians, section10.5](https://dlmf.nist.gov/10.5) — Read section 10.5, especially equation 10.5.3 for the ordinary J/Hankel1 Wronskian; version 1.2.8. Cylinder boundary algebra is independently derived here. The year 2026 denotes DLMF version 1.2.8, released on 2026-09-15, not its initial publication year. Accessed on 2026-11-24.
#### 関連するテスト問題の図とコード

##### [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`)

![保存した最細格子の実2D散乱電場phasorの実部。 図の中央の白抜きは診断用のr<0.4のマスクで、物理円柱の半径0.25とは区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#code-ja)

同じ問題への対応

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

- [実行・検証：2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`) · [コードZIP：2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

この実行例の範囲：実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。




### 斜め入射の複素Fresnel係数とLorentz板の直接散逸

解析解 · 2次元

`\varepsilon(\omega)=\varepsilon_\infty+f/(\omega_0^2-\omega^2-i\gamma\omega)+i\sigma/\omega`

外側真空、ky=4、板[4,5]、ε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。s=Ezとp=Hzをω=5.1/6/6.9で比較します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-lorentz/#lorentz-oblique-sp)

- selected-primary-documentation-or-authored-identity: [Meep Materials documentation](https://meep.readthedocs.io/en/latest/Materials/) — Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
#### 関連するテスト問題の図とコード

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`)

![保存したp偏光の実電場をky=4の周期y方向へ再構成した場。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#code-ja)

同じ問題への対応

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

- [実行・検証：Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`) · [コードZIP：Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

この実行例の範囲：有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。




### 浅角度分散波束の長時間・同格子孤立境界参照

有限格子の数値参照 · 2次元

`\widehat U^n(k_x)=M(k_x,\Delta t)^n\widehat U^0(k_x),\quad K_y=2\sin(k_y\Delta y/2)/\Delta y`

均質Lorentz媒質はPML内まで連続し、ε∞=1、Δε=0.2、ω0=12、γ=0または0.005。Ez偏光の有限kx Gaussianはcarrierω=6、中心位相角80度。512/768/1024点とpeak6/9/12を同時細分化し、垂直対照は6、弱減衰細格子対照は12。最終時刻は700です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-grazing/#dispersive-grazing-pml)

- selected-primary-documentation-or-authored-identity: [Meep Materials documentation](https://meep.readthedocs.io/en/latest/Materials/) — Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- selected-primary-documentation-or-authored-identity: [Notes on Perfectly Matched Layers](https://arxiv.org/html/2108.05348v1) — Read sections 3.2–4.2, equations 7–8 and the time-domain ADE discussion, plus sections 5–7.2 on homogeneity, evanescent fields and grazing/discretization limitations. The served text is updated 2026-08-24. The trapezoidal filter is our derivation; no full original Berenger/Roden-Gedney paper review is claimed.
#### 関連するテスト問題の図とコード

##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`)

![保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#code-ja)

同じ問題への対応

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

- [実行・検証：分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`) · [コードZIP：分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

この実行例の範囲：80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。




### 部分ピボットLU/Cholesky：実二進入力の厳密有理数参照

解析解 · 有限次元の代数問題

`x_ref=round_binary64(exact_Fraction_solve(A_binary64,b_binary64)); r=b-Ax; eta_inf=||r||inf/(||A||inf||x||inf+||b||inf)`

固定4行列の実binary64 A,bをFractionへ厳密変換し、有理数消去の解を最後にbinary64へ変換。LAPACKは別比較であり共有数値基盤を含みます。任意の悪条件行列に対する前進精度保証ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#pivoted-direct-refinement)

- selected-official-documentation: [LAPACK Users Guide: Linear Equations](https://netlib.org/lapack/lug/node38.html) — Selected LU, Cholesky, conditioning and refinement paragraphs were read. This source uses mixed precision, unlike the selected same-precision RFS description.
#### 関連するテスト問題の図とコード

##### [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`)

![保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#code-ja)

同じ問題への対応

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

- [実行・検証：部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`) · [コードZIP：部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。




### 対称不定値鞍点系：独立dense解と理想Schurスペクトル

有限格子の数値参照 · 有限次元の代数問題

`S=B H^{-1} B^T; P=diag(H,S); spectrum(L^{-1} A L^{-T})={1,(1-sqrt(5))/2,(1+sqrt(5))/2}; x_ref=LAPACK_solve(A,b)`

A=[[H,Bᵀ],[B,0]]、速度サイズ12/24、圧力行数5/11の代数問題。SPD理想Schurは全行列を小さく直接構成し、元の真残差とdense参照解誤差を別に判定。実Stokes境界値問題ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#symmetric-saddle-minres)

- selected-author-documentation: [Paige and Saunders: MINRES author documentation](https://web.stanford.edu/group/SOL/software/minres/) — Selected symmetry, indefinite-system, SPD-preconditioning and original-residual discussion was read. The original 1975 paper was not newly read.
- selected-official-documentation: [LAPACK Users Guide: Linear Equations](https://netlib.org/lapack/lug/node38.html) — Selected LU, Cholesky, conditioning and refinement paragraphs were read. This source uses mixed precision, unlike the selected same-precision RFS description.
#### 関連するテスト問題の図とコード

##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

同じ問題への対応

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

- [実行・検証：対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`) · [コードZIP：対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。




### 再始動/shift-invert：固定離散行列の閉スペクトル

解析解 · 有限次元の代数問題

`lambda_j=4/h^2*sin(j*pi/(2*(n+1)))^2,n=31; mu=1/(lambda-sigma); lambda=sigma+1/mu`

31×31 Dirichlet三重対角行列、h=1/32、再始動長8/16、shiftなし/0/950。参照はこの有限行列の固有値であり、格子細分化による連続PDE収束を認証しません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#restarted-shift-invert)

- selected-official-documentation: [SLEPc EPS manual: projection and spectral transformations](https://slepc.upv.es/release/documentation/manual/eps.html) — Selected projection, restarting and generalized-problem discussion was read. No SLEPc execution or Krylov-Schur reproduction is claimed.
#### 関連するテスト問題の図とコード

##### [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`)

![固有値比較に使う、保存した31×31 Dirichlet Laplacian。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#code-ja)

同じ問題への対応

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

- [実行・検証：明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`) · [コードZIP：明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。




### P1整合質量弦：閉離散固有値と連続体固有値

解析解 · 1次元

`Kx=lambda_h Mx; lambda_j,h=6*(1-cos(theta_j))/(h^2*(2+cos(theta_j))),theta_j=j*pi/(n+1); lambda_j=(j*pi)^2,phi_j(x)=sin(j*pi*x)`

長さ・張力・密度1、両端Dirichlet0、内部15/31/63点、最低3固有対。閉離散固有値とgeneralized dense LAPACKを比較し、連続(jπ)²への誤差を別に調べます。表示ベクトルは保存した数値解で、符号は任意です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#fem-mass-eigen)

- selected-official-documentation: [SciPy 1.14.1 LOBPCG](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html) — Selected SPD B, operator, preconditioner M, history and rod-example discussion was read. This uses the maintained SciPy implementation, not an original LOBPCG implementation.
- selected-official-documentation: [SLEPc EPS manual: projection and spectral transformations](https://slepc.upv.es/release/documentation/manual/eps.html) — Selected projection, restarting and generalized-problem discussion was read. No SLEPc execution or Krylov-Schur reproduction is claimed.
#### 関連するテスト問題の図とコード

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

同じ問題への対応

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

- [実行・検証：整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`) · [コードZIP：整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。




### 擬似弧長継続でBratuのfoldを越える

解析解 · 1次元

`u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)`

同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-bratu-continuation-jfnk/#bratu-fold-continuation)

- algorithm-primary: [Condition Estimates for Pseudo-Arclength Continuation](https://ipsen.math.ncsu.edu/ps/sinum65438.pdf) — Section2.2, printedpp265–266, Eqs2.2–2.5; tangent null equation, unit Euclidean tangent, augmented system and tangent hyperplane. Weighted h-sum metric is the implementation’s stated discrete variation. No full condition-number proof or original paper numerical benchmark is borrowed.
- analytic-reference: [Finite differences for the1D Bratu problem,Problem8](https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html) — Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.
#### 関連するテスト問題の図とコード

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

同じ問題への対応

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

- [実行・検証：擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`) · [コードZIP：擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

この実行例の範囲：同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。




### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov

解析解 · 1次元

`u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)`

同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-bratu-continuation-jfnk/#bratu-matrix-free-jfnk)

- algorithm-primary: [Jacobian-free Newton-Krylov methods: a survey of approaches and applications](https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf) — Selectedsec2.3,2.3.1,2.3.2 and2.4.1, printedpp361–363: matrix-free Jv action, perturbation scaling, inexact forcing Eq16 and line-search globalization. Actual central difference denominator2h and eps_machine^(1/3) scaling are independently specified/qualified, not an attribution to a PETSc default. No whole41-page audit or paper solver result reuse.
- algorithm-primary: [Choosing the Forcing Terms in an Inexact Newton Method](https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf) — Section1 AlgorithmIN/Eq1.2; selectedsec2 Choice2/Eq2.6; practical-safeguard paragraphssec2.1, printedpp16,20,22–23. Core eta=gamma*(||F_k||/||F_{k-1}||)^alpha is Choice2-style. Our gamma.9/alpha1.5 with eta_initial.3 and fixed[.001,.5] clamp omits the paper’s previous-eta safeguard. This is a declared variant, not its complete safeguarded algorithm or an asymptotic convergence certification.
- analytic-reference: [Finite differences for the1D Bratu problem,Problem8](https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html) — Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.
- context-only: [PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length](https://petsc.org/release/manual/snes/) — Selected Inexact Newton-like Methods and beginning of Matrix-Free Methods, residual forcing inequality and matrix-free/preconditioner distinction. Context only. No PETSc installation/execution or borrowed numerical success. Our hyperplane continuation is not a claim to implement every SNES arc-length scheme.
#### 関連するテスト問題の図とコード

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

同じ問題への対応

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

- [実行・検証：解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`) · [コードZIP：解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

この実行例の範囲：非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。




## English

### Advection / sine translation

Analytic reference · 1D

`u = 1 + 0.25 sin[2π(x−t)]`

Periodic unit interval; constant advection speed 1.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

Related-model problem

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [Run and validate: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

- [Run and validate: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Scope of this execution example: Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

- [Run and validate: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) (`fr-periodic-advection`) · [Code ZIP: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.


##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

Related-model problem

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

No fixed-input execution example is registered.



### Heat / Fourier-mode decay

Analytic reference · 1D

`u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]`

Periodic unit interval; viscosity 0.02.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

Related-model problem

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

Related-model problem

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

No fixed-input execution example is registered.

##### [Viscous decay of a periodic shear wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en) (`lbm-shear`)

![Stored shear amplitudes and viscous-decay reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#code-en)

Related-model problem

Linear viscous shear decay and scalar heat modes have the same form, but LBM lattice units, wavenumber and viscosity differ from the card’s ν=0.02.

No fixed-input execution example is registered.



### Burgers / shock

Analytic reference · 1D

`u_t + (u²/2)_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-shock) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en) (`burgers-shock`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#code-en)

Related-model problem

States (1,0), jump position 0.5 and endpoint continuation match; distinguish point and cell-average evaluation. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Burgers / rarefaction

Analytic reference · 1D

`u_t + (u²/2)_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-fan) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en) (`burgers-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#code-en)

Related-model problem

States (0,1), jump position 0.5 and endpoint continuation match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Traffic / upstream shock

Analytic reference · 1D

`rho_t + [rho(1−rho)]_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-jam) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en) (`traffic-jam`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#code-en)

Related-model problem

Flux ρ(1-ρ), left/right densities (0.3,0.9) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Traffic / clearing fan

Analytic reference · 1D

`rho_t + [rho(1−rho)]_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-fan) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en) (`traffic-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#code-en)

Related-model problem

Flux ρ(1-ρ), left/right densities (0.9,0.1) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Euler / Sod

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-sod) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

Related-model problem

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Run and validate: Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en) (`sod`) · [Code ZIP: Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.




### Euler / Lax

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-lax) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Lax shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=en) (`lax`)

![Shared figure, left: Lax shock tube. Right: a separate entropy-wave refinement study.](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=en#code-en)

Related-model problem

γ=1.4, states (0.445,0.698,3.528)/(0.5,0,0.571), [-5,5], x0=0 and t=1.3 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Euler / double rarefaction

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

Related-model problem

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Run and validate: Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) (`euler-double-rarefaction-positivity`) · [Code ZIP: Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

Scope of this execution example: Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.




### Euler / generated vacuum

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-vacuum) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Shallow water / wet dam break

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

Related-model problem

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Shallow water / dry-bed fan

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dry-bed) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

Related-model problem

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

- [Run and validate: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`) · [Code ZIP: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.




### Shallow water / dry middle state

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-vacuum) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Isothermal / density jump

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

p = c_s² rho; constant c_s; strictly positive initial density; no vacuum state or energy equation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

Related-model problem

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

No fixed-input execution example is registered.



### Poisson / manufactured sine

Manufactured solution · 1D

`u = sin(πx); −u_xx = f = π² sin(πx)`

Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

![Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

Related-model problem

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.

- [Run and validate: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`) · [Code ZIP: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.


##### [1D Poisson / pure Neumann boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=en) (`poisson-1d-neumann`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-neumann.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=en#code-en)

Related-model problem

The card is sin(πx) with zero Dirichlet boundaries; this test uses f=-2, pure Neumann data and a mean gauge.

No fixed-input execution example is registered.

##### [1D Poisson / mixed Dirichlet-Neumann boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=en) (`poisson-1d-mixed`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-mixed.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=en#code-en)

Related-model problem

The card is a zero-Dirichlet sine solution; this test uses mixed boundaries and 1+x².

No fixed-input execution example is registered.

##### [1D Poisson / Robin manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=en) (`poisson-1d-robin`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=en#code-en)

Related-model problem

The card is a zero-Dirichlet sine solution; this test uses Robin boundaries and exp(x).

No fixed-input execution example is registered.

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en) (`poisson-2d-broad`)

![Stored broad smooth forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#code-en)

Related-model problem

Both use manufactured Poisson solutions, but the card is a 1D single sine while this test uses a smooth composite 2D source.

No fixed-input execution example is registered.

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

Related-model problem

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [Run and validate: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

- [Run and validate: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en) (`sa-amg`) · [Code ZIP: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Scope of this execution example: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

- [Run and validate: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.




### Viscous channel / Couette

Analytic reference · 1D

`u(y) = y`

Fully developed planar steady channel; walls u(0)=0,u(1)=1; zero pressure gradient.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=couette) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Viscous channel / Poiseuille

Analytic reference · 1D

`u(y) = G y(1−y)/(2ν); G=1, ν=0.1`

Fully developed planar steady channel, no slip, unit density; −dp/dx=G or body acceleration G.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poiseuille) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en) (`channel-poiseuille`)

![Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en)

Related-model problem

Both have parabolic profiles, but the computation uses lattice height ny and forcing for peak speed 0.01; the card uses unit width, G=1 and ν=0.1.

No fixed-input execution example is registered.



### Viscous flow / 2D Taylor–Green

Analytic reference · 2D

`(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4`

Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4.

Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=taylor-green) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

#### Related test problem figures and code

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

Related-model problem

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

- [Run and validate: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

- [Run and validate: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) (`lbm-taylor-green`) · [Code ZIP: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

Scope of this execution example: Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.




### Noh cold-inflow shock: planar, cylindrical and spherical symmetry

Analytic reference · 1D

`s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.`

Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation. A separate full-square2D Cartesian calculation uses [-.5,.5]^2 with32²/64²/128² cells, both momenta and no radial reduction. Its density-cell reference is shock-split quadrature, checked at orders64/128.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/#noh-shock)

- original-problem: [W. F. Noh (1987), Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux, JCP72,78–120](https://doi.org/10.1016/0021-9991(87)90074-X) — Original problem and wall-heating analysis. Publisher metadata/abstract checked; no claim of reproducing every original calculation.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Noh1987. The analytic evaluator is a reference, not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, exactpack/solvers/noh/noh1.py](https://github.com/lanl/ExactPack/blob/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/noh/noh1.py) — BSD-3-Clause. Actual evaluation is restricted to gamma=5/3,rho0=1,inward speed1. Source hashes, point/shell comparisons and parameter-limit control are saved in the Noh release.
#### Related test problem figures and code

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Density from an actual2D Cartesian Euler computation:full square128²,p0=0,gamma5/3,t=.6. White dashed circle is the exact shock. Axis/diagonal differences and origin heating remain visible, with links to earlier1D radial examples.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

Same-problem link

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

- [Run and validate: Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP: Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

Scope of this execution example: An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

- [Run and validate: Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) (`noh-cartesian-2d`) · [Code ZIP: Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

Scope of this execution example: A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.




### Sedov–Taylor point blast: energy-normalized spherical similarity solution

Semi-analytic reference · 1D

`R_s(t)=beta*(E0*t^2/rho0)^(1/5), beta≈1.15166641793; D=2*R_s/(5*t); rho=rho0*G(r/R_s), u=D*V(r/R_s), p=rho0*D^2*P(r/R_s).`

Ideal-gas Euler in spherical radial symmetry, gamma=5/3, ambient rho0=1 and p0=0, explosion energy E0=1, r in [0,1], t=0.05. The similarity reference describes ideal instantaneous point deposition. Finite-volume runs instead deposit energy inside radius 0.03, with a paired radius-0.015 sensitivity calculation. The reference uses a numerical similarity-ODE integration, a tiny-core regular asymptote and split shell quadrature; it is semi-analytic, not closed-form exact cell means. The gallery picture is a central section of one-dimensional spherical-radial data, not a two-dimensional Cartesian computation. Fixed-radius errors include point-source model discrepancy, so their refinement slope is not a pure spatial order; the paired-radius calculation is only a sensitivity diagnostic.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sedov/#sedov-blast)

- original-similarity-theory: [G. I. Taylor (1950), The formation of a blast wave by a very intense explosion I. Theoretical discussion, Proceedings of the Royal Society A201(1065),159–174](https://doi.org/10.1098/rspa.1950.0049) — Original theoretical similarity assumptions, Euler reduction, strong-shock conditions, energy normalization and regular-center exponent checked in selected original pp159–167 via a university-hosted scan. Publisher access returned403; no full publisher-text review or PDF redistribution is claimed.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Taylor1950 and the selected pinned reference implementation. ExactPack evaluates a reference and is not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, selected Sedov evaluator](https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/sedov) — BSD-3-Clause. The selected unmodified pinned Sedov evaluator was actually run at npts6001/12001 with gamma=5/3,rho0=E0=1,t=.05,geometry3 and probes xi=.15,.25,.5,.75,.9,1.05. Source hashes, invocation and point values are archived. The upstream small-radius warning for density/internal energy is retained; the central region and shock jump are excluded from these point probes. This does not validate other ExactPack solvers or an independent PDE engine.
#### Related test problem figures and code

##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

![A central-section view of saved one-dimensional spherical-radial Euler density:gamma5/3,E=rho0=1,p0=0,t=.05,512 shells and finite deposition radius.03. Point-source reference differences and shock errors remain visible; this is not an actual2D Cartesian computation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

Same-problem link

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

- [Run and validate: Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) (`sedov-blast`) · [Code ZIP: Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

Scope of this execution example: A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.




### Double Mach reflection: saved independent finite-grid numerical reference

Finite-grid numerical reference · 2D

`partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| (conservative restriction of saved finite-grid data).`

Two-dimensional ideal-gas Euler flow on [0,4] × [0,1], with gamma = 1.4, a Mach-10 incident shock at 60 degrees, initial shock foot x = 1/6 and final time T = 0.2. The saved reference uses a separately written, unsplit primitive MUSCL/HLL/Heun finite-volume code on 256 × 64 and 512 × 128 cells. Its generalized-minmod slope parameter is theta = 1.5 (MC-type, rather than canonical MC with theta = 2). The primary and reference codes share the HLL flux family and Heun time-integration equations, while their spatial reconstruction and implementations are separate. Conservative restriction produces comparison cell means. Previously executed source, data and receipts are reused from the immutable RKDG2D kit; no reference PDE, Athena or LAVA was executed anew for this addition. Reference grid differences indicate finite-resolution sensitivity, not rigorous error bounds. This is not an analytic 2D solution or a convergence test for the thin wall jet and vortex pattern. The incident discontinuity is classified at cell centers, rather than initialized from exact cut-cell averages.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-double-mach/#double-mach-reflection)

- original-problem: [P. Woodward and P. Colella (1984), The numerical simulation of two-dimensional fluid flow with strong shocks, Journal of Computational Physics54(1),115–173](https://doi.org/10.1016/0021-9991(84)90142-6) — Publisher metadata/abstract and official NASA setup checked. No direct full-original-paper review is claimed.
- official-setup-cross-check: [NASA LAVA tutorial: Double Mach Reflection](https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/) — Official selected setup and boundary cross-check only; no LAVA execution or figure redistribution.
- executed-reference-implementation: [Previously executed independent FV-MUSCL/generalized-minmod(theta1.5)/HLL/Heun reference distributed with the RKDG2D agent kit,2026-11-23-r2](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip) — Selected sourceSHA256bc206f991594c6b011bb3cde50f104b8806a371df19af0464ff6b1a1d1cc39af; archiveSHA2566fa8d75c1f70281eb0a78363eb3323c5a9a1b006f01f49182c4827f4d5710a69. Reuse previously executed256×64 and512×128 arrays, source and records under MIT; no new reference PDE/Athena/LAVA execution. Reference has an adaptive retry capability, but the selected saved records report zero rejected steps.
#### Related test problem figures and code

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

Same-problem link

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

- [Run and validate: Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en) (`double-mach-reflection`) · [Code ZIP: Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

Scope of this execution example: Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.




### Mach-3 forward-facing step: independent C++ finite-grid numerical reference

Finite-grid numerical reference · 2D

`partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| on fluid cells (conservative restriction of a finite-grid reference).`

Two-dimensional ideal-gas Euler flow with gamma=1.4 in [0,3]×[0,1] excluding the solid step x>=.6,y<.2. Uniform initial/inflow primitive state (rho,u,v,p)=(1.4,3,0,1), reflecting slip channel/step walls, right zero-gradient outflow and T=4. The reference is a separately written C++17 unsplit finite-volume implementation with primitive MUSCL generalized minmod(theta=1.5), Davis HLL flux and Heun/SSPRK2 at CFL=.3 on 240×80 and480×160 cells. Normal slopes touching walls/exterior boundaries are zero; reconstructed primitive slopes may be rescaled without altering cell means. The primary Python calculation uses piecewise-constant HLL plus Heun; flux family/time equations are shared, while implementation and spatial reconstruction are separate. No Woodward–Colella corner entropy/enthalpy reset, state floors or time-step retries are used. The uncorrected corner can produce an entropy layer that affects the downstream reflected shock/Mach stem. This is a finite-grid numerical reference, not an exact solution, rigorous error bound, replication of corner-corrected original PPM figures, or proof that fine slip lines/vortices are resolved.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-forward-step/#forward-step-m3)

- original-problem: [P. Woodward and P. Colella (1984), The numerical simulation of two-dimensional fluid flow with strong shocks, Journal of Computational Physics54(1),115–173](https://doi.org/10.1016/0021-9991(84)90142-6) — Original-problem bibliographic context; no direct full-original-paper review or reproduction of its corner-corrected PPM results is claimed.
- checked-setup-and-corner-caveat: [B. Cockburn and C.-W. Shu (1991), The P¹-RKDG Method for Two-Dimensional Euler Equations of Gas Dynamics, NASA CR187542 / ICASE91-32, Example2](https://ntrs.nasa.gov/api/citations/19910015505/downloads/19910015505.pdf) — Selected text of Example2 on printedpage7/PDFpage11 and Fig3 captions on printedpage8/PDFpage12 checked for Mach3 step geometry,initial/inflow state,T4 and the distinction between untreated and specially treated corners. No figure redistribution or RKDG execution. This publication deliberately uses the uncorrected corner.
- independent-reference-implementation: [Independent educational C++17 forward-step FV reference,2026-11-23](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp) — MIT. New primitive-MUSCL/generalized-minmod(theta1.5)/Davis-HLL/Heun runs on240×80 and480×160. Reference sourceSHA25666e523f5486179f2c79ac0ad21a35a11856e55a9101e03b8d3bca76cccbd5996; compiler/invocation and execution/quality receipts accompany the arrays. No external AMROC/Athena/LAVA execution.
#### Related test problem figures and code

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

Same-problem link

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

- [Run and validate: Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en) (`forward-step-m3`) · [Code ZIP: Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

Scope of this execution example: Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.




### Isentropic vortex: analytic Euler field for low-Mach comparisons

Analytic reference · 2D

`a=beta exp((1-X²-Y²)/2)/(2pi); (u,v)=(1-aY,.5+aX); theta=1-(gamma-1)beta² exp(1-X²-Y²)/(8 gamma pi² p_inf); rho=theta^(1/(gamma-1)); p=p_inf theta^(gamma/(gamma-1)); p_inf=1.25/(1.4 M_inf²).`

The translating whole-plane ideal-gas Euler vortex uses gamma=1.4, beta=3, far-field density1 and background velocity U=(1,.5). For background Mach number M, p_inf=1.25/(1.4*M^2); theta=1-(gamma-1)*beta^2*exp(1-r^2)/(8*gamma*pi^2*p_inf), rho=theta^(1/(gamma-1)), p=p_inf*theta^(gamma/(gamma-1)). Coordinates move with U and are wrapped in [-10,10]^2. The whole-plane field is analytic; the finite minimum-image periodic field retains nonzero Gaussian seam tails and is not a globally exact smooth torus solution. Tensor Gauss8 cell means of all conserved variables are checked against Gauss16, then primitive pressure and velocity are recovered from those means. These are numerical cell quadratures, not closed-form exact cell averages or means of primitive variables. The low-Mach fixed runs use M=.1/.01 and T=.1; the historical KEEP case is recovered by p_inf=1.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-low-mach/#low-mach-vortex)

- original-flux-preconditioning-method: [Fabian Miczek, Friedrich K. Röpke and Philipp V. F. Edelmann (2015), New numerical solver for flows at various Mach numbers](https://doi.org/10.1051/0004-6361/201425059) — Selected author-version equations and RK3 discussion were checked. This short isentropic-vortex application does not reproduce the paper’s Gresho or implicit-integration experiments.
- matrix-form-and-explicit-stability-analysis: [Wasilij Barsukow, Philipp V. F. Edelmann, Christian Klingenberg, Fabian Miczek and Friedrich K. Röpke (2017), A Numerical Scheme for the Compressible Low-Mach Number Regime of Ideal Fluid Dynamics](https://doi.org/10.1007/s10915-017-0372-4) — Checked the modified dissipation, primitive matrix and restrictive forward-Euler stability result. The present SSPRK33 Fourier/stage checks are separate fixed-input evidence, not a general nonlinear or SSP guarantee.
- analytic-vortex-definition-and-finite-periodic-box-qualification: [Seth C. Spiegel, H. T. Huynh and James R. DeBonis (2015), A Survey of the Isentropic Euler Vortex Problem using High-Order Methods](https://doi.org/10.2514/6.2015-2444) — Checked the generalized vortex and finite-periodic-boundary qualifications. The selected beta3, mean velocity(1,.5) and background Mach values are explicit adaptations, not NASA/FR execution or figure reuse.
#### Related test problem figures and code

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

![Actual 2D Euler evolution at M∞=.01, 64² and T=.1. A central \[-3,3\]² crop of the full \[-10,10\]² computation compares ordinary and preconditioned Roe with MUSCL. Vorticity is derived by finite differences of saved velocity; arrows show velocity minus the background flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

Same-problem link

Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.

- [Run and validate: Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en) (`low-mach-vortex`) · [Code ZIP: Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

Scope of this execution example: The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.




### Guderley converging shock: eigenvalue and spherical semi-analytic reference

Semi-analytic reference · 1D

`R_s(t)=0.6*(-t)^alpha, alpha=1/lambda; x=t*(0.6/r)^lambda; rho=rho0*R(x), u=-r*V(x)/(lambda*t), p=rho*(-r*C(x)/(lambda*t))^2/gamma. For r<R_s:rho=rho0,u=p=0.`

Ideal-gas Euler in spherical radial symmetry, gamma=1.4, with unshocked upstream rho0=1, u=p=0. Lazarus time t in [-1,-0.85] excludes collapse at 0; r in [0,0.75], Rs(t)=0.6*(-t)^alpha and alpha=1/lambda. The initial field already contains the shocked outer similarity state. Lambda was computed and qualified using pinned ExactPack eigenvalue shooting and eight original-state probes. Routine replay reuses that recorded lambda and freshly integrates the same pinned pre-collapse similarity ODE. Full eigenvalue and original-probe regeneration is a separate explicit command. Shells are split at the shock and conserved states are Gauss16 volume averaged, checked against Gauss32; pressure is p(Ubar). This is a dense-output adapter to ExactPack, not closed-form exact cell means or an independent similarity implementation. The figure maps 1D spherical-radial data onto a 2D meridional section, not 2D Cartesian or post-collapse evolution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-guderley/#guderley-implosion)

- historical-original-problem-attribution: [G. Guderley (1942), Starke kugelige und zylindrische Verdichtungsstöße in der Nähe des Kugelmittelpunktes bzw. der Zylinderachse, Luftfahrtforschung 19, 302 (first page)](https://raw.githubusercontent.com/lanl/ExactPack/9bacc477eb791e959c9621e771fc7a725db755fa/doc/source/references.rst) — Historical original-problem attribution. Author/year/volume/first page 302 were checked in the pinned ExactPack bibliography and the title in the Lazarus1981 publisher references. The original 1942 text was not inspected and is not claimed as the directly transcribed source of the present fields or measurements.
- semi-analytic-benchmark-and-two-eigenvalue-context: [Scott D. Ramsey, James R. Kamm and John H. Bolstad (2012), The Guderley problem revisited, International Journal of Computational Fluid Dynamics 26, 79–99](https://doi.org/10.1080/10618562.2011.647768) — The LANL record and abstract distinguish the convergence exponent from the reflected trajectory eigenvalue. This is not a claim to have read the entire paper or reproduced its PDE experiment; the present field is constructed using the pinned ExactPack source.
- similarity-coordinate-convention-and-tabulated-exponent: [Roger B. Lazarus (1981), Self-Similar Solutions for Converging Shocks and Collapsing Cavities, SIAM Journal on Numerical Analysis 18, 316–371](https://doi.org/10.1137/0718022) — Checked the publisher record/abstract and the explicitly attributed equations/table in ExactPack. The tabulated lambda 1.3943607838 is the value transcribed in that code, not an independent retranscription of the original table.
- critical-point-eigenvalue-formulation-used-by-ExactPack-eexp: [R. F. Chisnell (1998), An analytic description of converging shock waves, Journal of Fluid Mechanics 354, 357–375](https://doi.org/10.1017/S0022112097007775) — Checked the publisher record/abstract and the critical-point phase matching and equation 3.1 implementation in ExactPack eexp. The exponent is computed through that eigenvalue routine rather than fixed by dimensional analysis. The exponent was computed in the retained qualification; routine replay reuses the qualified value. Full eigenvalue shooting is an explicit separate regeneration step.
- ExactPack-software-reference: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX 24, 101560](https://doi.org/10.1016/j.softx.2023.101560) — Cites the ExactPack software paper and its Guderley solver listing. The paper version 1.7.5 is distinguished from the exact source commit used here, whose source, SHA receipts and BSD license are retained.
- actually-executed-semi-analytic-reference-source: [Los Alamos National Laboratory / ExactPack contributors (2025), ExactPack Guderley solver, pinned source](https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/guderley) — Inspected pinned eexp, the pre-collapse ODE/state, transcribed tables, official regression values and BSD 3 terms. This is not a claim to have run the complete ExactPack suite; actual reference execution is recorded separately. The selected exponent, pre-collapse ODE and eight original state probes were actually executed; qualification.json and pinned source/license hashes are archived with this release. The public Guderley class, reflected B solve and full ExactPack suite were not run. Routine replay reuses the recorded qualified lambda and freshly integrates the pinned pre-collapse ODE; it does not claim to repeat eexp shooting or the eight original-state probes by default. Their full regeneration is separately available.
#### Related test problem figures and code

##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

![A meridional-section display of saved one-dimensional spherical-radial Euler density: gamma=1.4, 512 shells, r in \[0,0.75\], Rs(-1)=0.6, t=-0.85. Compare the pre-collapse shock entering stationary zero-pressure upstream gas with a semi-analytic reference. This is not 2D Cartesian or post-collapse evolution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

Same-problem link

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

- [Run and validate: Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) (`guderley-implosion`) · [Code ZIP: Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

Scope of this execution example: An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.




### Zalesak-type slotted disk: rigid rotation and geometric cell means

Analytic reference · 2D

`q(x,t)=1_D(c+R(-t)(x-c)); qbar_K(t)=area(K intersect [c+R(t)(D-c)])/area(K), c=(0.5,0.5), T=2*pi. D=disk((0.5,0.75),0.15) minus {0.475<x<0.525,y<0.85}.`

Unit-square two-dimensional scalar transport with prescribed velocity (0.5-y,x-0.5), angular speed 1 and period2*pi. The baseline indicator is one inside the disk of radius 0.15 centered at (0.5,0.75), excluding 0.475<x<0.525 and y<0.85, and zero outside. This isolates the normalized slotted-cylinder component described in the official Firedrake setup; its bell, cone, background 1, DG discretization and inflow boundary are not copied. Periodic finite-volume normal velocities match on opposite faces; the compact exact body stays away from the boundary, while numerical tails are measured. Exact rigid characteristics and analytic disk/polygon intersection areas define the reference cell means, not rasterized point samples or a second numerical PDE solution. A full turn returns to the initial continuum shape; rotated/shifted variants are separate fixed diagnostics.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-zalesak/#zalesak-rotation)

- historical-original-problem-attribution: [Steven T. Zalesak (1979), Fully multidimensional flux-corrected transport algorithms for fluids, Journal of Computational Physics 31, 335–362](https://doi.org/10.1016/0021-9991(79)90051-2) — Publisher bibliography and abstract checked. Direct full-text access was unavailable; no complete original-test transcription or FCT replication is claimed.
- official-setup-cross-check: [Firedrake project, DG advection demo: normalized slotted-cylinder geometry and rigid velocity](https://www.firedrakeproject.org/demos/DG_advection.py.html) — Inspected the official velocity, period and geometry definitions. This release isolates a 0–1 slotted disk and uses periodic finite volumes; the official bell/cone/background 1, DG scheme, inflow boundary and full Firedrake experiment are not reproduced or executed.
- official-demo-historical-context: [Randall J. LeVeque (1996), High-Resolution Conservative Algorithms for Advection in Incompressible Flow, SIAM Journal on Numerical Analysis 33, 627–665](https://doi.org/10.1137/0733033) — The official Firedrake demonstration attributes its rotating-body setup to this work. Its role here is contextual attribution, not a claim that the full paper or its numerical algorithm was implemented.
#### Related test problem figures and code

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

![Saved cell means on the finest grid of actual two-dimensional scalar transport. Zoom x in\[.28,.72\],y in\[.53,.97\] from the full unit square and compare donor-cell upwinding and minmod MUSCL after one revolution against geometric reference cell means. Slot diffusion remains visible; this is not an FCT algorithm or Euler-flow calculation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

Same-problem link

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

- [Run and validate: Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) (`zalesak-rotation`) · [Code ZIP: Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

Scope of this execution example: Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.




### WENO critical points: polynomial cell means and analytic periodic transport

Analytic reference · 1D

`qbar_i=h^-1 integral_Ci q0(x-t)dx; q0=cos(2pi*x)+.1*sin(2pi*x)^3; local P=x+...+x^5, x²+x³+x⁴+x⁵, or x³+x⁴+x⁵.`

Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-weno-critical/#weno-critical-epsilon)

- Classical JS candidate/weight/indicator background; preprint finite-difference convention distinguished from this FV implementation: [Guang-Shan Jiang and Chi-Wang Shu (1996), Efficient Implementation of Weighted ENO Schemes](https://ntrs.nasa.gov/api/citations/19960007052/downloads/19960007052.pdf) — NASA-hosted ICASE95-73 preprint selected sections1–3: candidate Table1, optimal Table2, equations2.15–2.16 and3.1–3.9; text layer inspected, not full paper/numerical tables
- Original WENO-Z attribution and historical scope, not an actually inspected full-text formula source: [Rafael Borges, Monique Carmona, Bruno Costa and Wai Sun Don (2008), An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws](https://scholars.hkbu.edu.hk/en/publications/an-improved-weighted-essentially-non-oscillatory-scheme-for-hyper-2/) — Author-institution publication record and abstract inspected; publisher full text returned403; original full paper and numerical experiments not audited
- Actually inspected finite-volume cell-mean derivation of baseline JS/Z candidates, weights and power-two choice; embedded modifications excluded: [Bart S. van Lith, Jan H. M. ten Thije Boonkkamp and Wilbert L. IJzerman (2017), Embedded WENO: A design strategy to improve existing WENO schemes](https://pure.tue.nl/ws/portalfiles/portal/53481949/embedded_WENO.pdf) — Institution-hosted accepted manuscript section2 equations2–15 (PDF pages4–8) and selected section4.2 (PDF page22) text inspected; screenshot requests cache-missed; not a full-paper review
#### Related test problem figures and code

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

Related-model problem

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [Run and validate: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

- [Run and validate: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Scope of this execution example: Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

- [Run and validate: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) (`fr-periodic-advection`) · [Code ZIP: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.




### Lake at rest: wet and emerged equilibrium over represented bed

Analytic reference · 1D

`q_i=0; h_i=max(eta0-z_i,0); z_i=cellmean(z); eta0=.5 or .1.`

Use g9.81,[0,25]m and200cells. Represent z=.2−.05(x−10)² on8<x<12 by split Gauss8 cell means, initializing h_i=max(eta0−z_i,0),q_i0 with eta0=.5/.1m. Hydrostatic reconstruction preserves equilibrium over this represented piecewise-constant bed; this differs from directly averaging depth over the continuous bed.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/#swashes-topography)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
- original HR attribution: [E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004), A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows](https://epubs.siam.org/doi/abs/10.1137/S1064827503431090) — Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.
- directly inspected HR algebra: [E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016), Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system](https://arxiv.org/pdf/1409.3825) — arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.
#### Related test problem figures and code

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

Same-problem link

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

- [Run and validate: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) (`swashes-topography`) · [Code ZIP: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.




### SWASHES steady flow: subcritical Bernoulli root

Semi-analytic reference · 1D

`q=4.42; h+z+q²/(2gh²)=2+q²/(8g); h>(q²/g)^(1/3).`

Use g9.81,[0,25]m, the parabolic bed, discharge q4.42m²/s and downstream depth2m. Independently bisect the subcritical root of h+z+q²/(2gh²)=2+q²/(8g) and qualify cell quadrature. PDE runs on100/200/400cells start from the steady reference and advance to t2; they do not reproduce the original rest-to-steady transient.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/#swashes-topography)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
#### Related test problem figures and code

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

Same-problem link

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

- [Run and validate: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) (`swashes-topography`) · [Code ZIP: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.




### Ritter dry-bed dam break: dedicated g9.81 cell-mean reference

Analytic reference · 1D

`cL=sqrt(g*hL); h=(2*cL-(x-x0)/t)^2/(9*g), u=2*((x-x0)/t+cL)/3 inside fan; hR=0 beyond x0+2*cL*t.`

Flat frictionless[-10,10]m, dam x00,hL1m/hR0,zero initial velocity,g9.81,t.5s. Split conserved(h,hu) cell means at the rarefaction head−sqrt(g)t and genuine dry front2sqrt(g)t. Separately track the fixed depth.001m contour. These dedicated gravity/domain/time inputs differ from the historical card, whose values remain unchanged.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/#dry-bed-dam-break)

- analytic formulas and benchmark provenance: [O. Delestre et al. (2013), SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies](https://arxiv.org/pdf/1110.0288) — Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.
#### Related test problem figures and code

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

Same-problem link

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

- [Run and validate: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`) · [Code ZIP: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.




### Ghia Re100: original finite-grid velocity centerlines

Finite-grid numerical reference · 2D

`u_ref(.5,y_j),v_ref(x_j,.5): original TablesI/II Re100; primary vortex(x,y)=(.6172,.7344): TableV.`

Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/#cavity-ghia-re100)

- primary-research-reference: [U. Ghia, K. N. Ghia and C. T. Shin (1982), High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method](https://www.sciencedirect.com/science/article/pii/0021999182900584) — Original PDF rendered and visually read:391–392 equations/Fig1;398–399 TablesI/II Re100 columns;408 TableV primary vortex. Publisher abstract/bibliography read; publisher PDF403. Original PDF obtained from recorded public mirror; no full-paper audit.
- actual-original-table-transcription-provenance: [Original Ghia TablesI/II andV transcription/source audit](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/source-review.json) — Original PDF selected printed391–392,398–399,408 visually inspected. PDF SHA2561d76e4636d24d0fad41c7bdb5ed383e9b224b0bfe3aa0317ce7dfc50619f2d93; public mirror is only its delivery location. Transcribed CSV accompanies the immutable release.
#### Related test problem figures and code

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

Same-problem link

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

- [Run and validate: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) (`cavity-ghia-re100`) · [Code ZIP: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

- [Run and validate: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) (`lbm-cavity-re100`) · [Code ZIP: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

Scope of this execution example: Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.




### Wall manufactured solution: polynomial velocity and separate pressure operator

Manufactured solution · 2D

`psi*=8 f(x)f(y),f(z)=z²(1−z)²; s=u*omega*_x+v*omega*_y−nu*Delta omega*. Separate: p_op=x²+y²+sin(pi*x)sin(pi*y).`

Unit square,viscosity.01,no-slip,psi*=8x²(1−x)²y²(1−y)²,u*=psi*_y,v*=−psi*_x,omega*=−Delta psi*. Construct s=u*omega*_x+v*omega*_y−nu*Delta omega* from the continuous vorticity PDE, qualified by independent tensor-coefficient differentiation. PDE wall vorticity uses the same Thom closure as the cavity without exact injection. Nonzero-Dirichlet Poisson/gradient for p_op=x²+y²+sin(pi*x)sin(pi*y) is a separate operator problem, not coupled flow or cavity pressure.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/#wall-manufactured)

- primary-research-reference: [Kambiz Salari and Patrick Knupp (2000), Code Verification by the Method of Manufactured Solutions](https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/) — Official Sandia/OSTI record and primary report printed12 at UNT read for MMS plus mesh refinement. No whole-report audit. Our quartic polynomial and pressure field are newly constructed.
#### Related test problem figures and code

##### [Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

![Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

Same-problem link

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

- [Run and validate: Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en) (`wall-manufactured`) · [Code ZIP: Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.




### 2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference

Analytic reference · 2D

`phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.3+0.2*t,0.35+0.1*t).`

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)

- original-formulation-and-selected-reference-context: [S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations](https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf) — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- original-formulation-and-selected-reference-context: [C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries](https://www.sciencedirect.com/science/article/pii/0021999181901455) — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- original-formulation-and-selected-reference-context: [M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow](https://epubs.siam.org/doi/10.1137/S1064827596298245) — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- original-formulation-and-selected-reference-context: [M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows](https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf) — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.
#### Related test problem figures and code

##### [Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

![Zero contours extracted from actual128² level-set fields: translation(left) and an off-center full rotation(right). Compare analytic interfaces against advection alone and simple redistancing. This is not a VOF calculation, and no area correction is applied.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

Same-problem link

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [Run and validate: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) (`level-set-translation`) · [Code ZIP: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

- [Run and validate: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) (`level-set-rotation`) · [Code ZIP: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.




### 2D rigid rotation of an off-center level-set circle: analytic signed-distance reference

Analytic reference · 2D

`phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.5,0.5)+R(2*pi*t)(0.18,0).`

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)

- original-formulation-and-selected-reference-context: [S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations](https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf) — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- original-formulation-and-selected-reference-context: [C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries](https://www.sciencedirect.com/science/article/pii/0021999181901455) — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- original-formulation-and-selected-reference-context: [M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow](https://epubs.siam.org/doi/10.1137/S1064827596298245) — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- original-formulation-and-selected-reference-context: [M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows](https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf) — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.
#### Related test problem figures and code

##### [Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

![Zero contours extracted from actual128² level-set fields: translation(left) and an off-center full rotation(right). Compare analytic interfaces against advection alone and simple redistancing. This is not a VOF calculation, and no area correction is applied.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

Same-problem link

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [Run and validate: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) (`level-set-translation`) · [Code ZIP: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

- [Run and validate: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) (`level-set-rotation`) · [Code ZIP: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.




### 2D Poisson sine manufactured solution: shared SEM/P1 FEM reference

Manufactured solution · 2D

`u(x,y)=sin(pi*x)*sin(pi*y); f=2*pi^2*u; grad u=(pi*cos(pi*x)*sin(pi*y),pi*sin(pi*x)*cos(pi*y)).`

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/spectral-element/)

- executed-reference-implementation: [Atlas sem.py: sine value and gradient](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) — Locally chosen exact field evaluated in every fixed-input run; not an external Nek/PyFR execution.
#### Related test problem figures and code

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

Same-problem link

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

- [Run and validate: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

- [Run and validate: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en) (`sa-amg`) · [Code ZIP: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Scope of this execution example: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

- [Run and validate: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.




### FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25

Analytic reference · 1D

`u(x,t)=0.4+sin(2*pi*(x-t)); speed1, period1, T=.25.`

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/flux-reconstruction/)

- executed-reference-implementation: [Atlas fr.py: analytic translation](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) — Locally chosen exact field evaluated in every fixed-input run; not an external Nek/PyFR execution.
#### Related test problem figures and code

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

Same-problem link

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

- [Run and validate: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

- [Run and validate: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Scope of this execution example: Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

- [Run and validate: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) (`fr-periodic-advection`) · [Code ZIP: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.




### KH initial growth: independent linear Fourier-Galerkin reference

Finite-grid numerical reference · 2D

`U=tanh(sin(y)/delta); omega_t=-U*omega_x-Uyy*psi_x+nu*Delta(omega); -Delta(psi)=omega; qhat(t)=exp(t*L_K)qhat(0).`

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1. The nonlinear primary evolves actual2D point samples. The reference solves the continuous linearized IVP at kx1 with truncationsK24/40/56 and independently Fourier-differentiated base profiles; it does not substitute a sharp-interface dispersion formula.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/#kh-initial-growth)

- selected-primary-reference-context: [Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012), A Well-Posed Kelvin-Helmholtz Instability Test and Comparison](https://arxiv.org/abs/1111.1764) — Read original sections1–3 on matching smooth finite-domain models and growth diagnostics; arXiv journal metadata checked. Our forced incompressible model is distinct.
#### Related test problem figures and code

##### [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

![Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

Same-problem link

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

- [Run and validate: KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en) (`kh-initial-growth`) · [Code ZIP: KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Scope of this execution example: Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.




### RT initial growth: linear Boussinesq double-layer IVP reference

Finite-grid numerical reference · 2D

`b0=.02*tanh(sin(y)/delta); omega_t=nu*Delta(omega)+theta_x; theta_t=kappa*Delta(theta)+psi_x*b0prime; -Delta(psi)=omega.`

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler. The reference uses the same smooth base, kx1 continuous linearization and Fourier-Galerkin truncationsK24/40/56. Inertial density is constant; buoyancy perturbation theta supplies vertical forcing, with one unstable interface in the periodic double layer.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/#rt-initial-growth)

- selected-primary-reference-context: [Antonio Celani, Andrea Mazzino and Lara Vozella (2006), Rayleigh–Taylor turbulence in two dimensions](https://arxiv.org/abs/nlin/0510067) — Read original pp1–2 governing equations1–2 and doubly periodic Boussinesq setup. No original turbulent-run reproduction.
#### Related test problem figures and code

##### [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

![Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

Same-problem link

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

- [Run and validate: RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en) (`rt-initial-growth`) · [Code ZIP: RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Scope of this execution example: Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.




### Circular Alfven wave: analytic full-state conserved cell means

Analytic reference · 1D

`sinc(h)=sin(pi*h)/(pi*h); theta=2*pi*(x-t); (Bybar,Bzbar)=.1*sinc(h)*(cos(theta),sin(theta)); (mybar,mzbar)=-(Bybar,Bzbar); rhobar=Bxbar=1; Ebar=.66.`

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure. Apply sinc(h) to transverse magnetic fields and momenta, retaining E=.66, and qualify against independent Gauss16 quadrature. The x-t picture shows one spatial dimension and saved times, not oblique2D propagation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-transport/#circular-alfven-refinement)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
#### Related test problem figures and code

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

![Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

Related-model problem

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

- [Run and validate: Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) (`circular-alfven-refinement`) · [Code ZIP: Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.




### Magnetic loop: pinned independent Athena++ final-field reference

Finite-grid numerical reference · 2D

`Az=.001*max(.3-sqrt(x*x+y*y),0); rho=p=1; v=(2,1,2); T=1; Uref_coarse=conservative_block_average(Uref_fine).`

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs. Execute the unchanged official generator at pinned commit1395e2f…; qualify Ny64/128 and finest-grid half-CFL sensitivity. Compare final conserved fields only after conservative restriction.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-transport/#magnetic-loop-independent)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
#### Related test problem figures and code

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

Related-model problem

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.

- [Run and validate: Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) (`magnetic-loop-independent`) · [Code ZIP: Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.




### Late Orszag-Tang: independent finite-grid density/pressure reference

Finite-grid numerical reference · 2D

`rho0=25/(36*pi); p0=5/(12*pi); v=(sin(2*pi*y),-sin(2*pi*x),0); Az=(cos(4*pi*x)-2*cos(2*pi*y))/(4*pi*sqrt(4*pi)); T=.2.`

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model. Run official Athena++ at128²/256² and finest-grid half CFL to T.2. Conservatively restrict final conserved variables before computing pressure; pressure is not averaged separately.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-transport/#postshock-orszag-tang)

- Actually inspected independent engine and fixed initial conditions; finite-grid numerical reference only: [Athena++ collaboration (2026), Athena++ official field_loop and orszag_tang problem generators, pinned source](https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416) — Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
- Primary CT-contact, magnetic-loop and circular-polarization background; selected sections only: [Thomas A. Gardiner and James M. Stone (2005), An unsplit Godunov method for ideal MHD via constrained transport](https://arxiv.org/abs/astro-ph/0501557) — Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
- Original HLLD attribution; implementation inherited from previously validated Atlas source: [Takahiro Miyoshi and Kanya Kusano (2005), A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics](https://doi.org/10.1016/j.jcp.2005.02.017) — Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
- Historical attribution, not a reference table for this compressible ideal-MHD calculation: [Steven A. Orszag and Ching-Mao Tang (1979), Small-scale structure of two-dimensional magnetohydrodynamic turbulence](https://doi.org/10.1017/S002211207900210X) — Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
#### Related test problem figures and code

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

Related-model problem

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

- [Run and validate: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en) (`ct-glm-independent`) · [Code ZIP: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Scope of this execution example: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

- [Run and validate: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en) (`ct-glm-ot-convergence`) · [Code ZIP: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Scope of this execution example: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

- [Run and validate: Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) (`postshock-orszag-tang`) · [Code ZIP: Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.




### ALE: analytic moving-cell integrals and separate time reference

Analytic reference · 1D

`x(xi,t)=xi+.2*sin(2*pi*xi)*sin(2*pi*t)/(2*pi); m_i=integral_[x_i,x_(i+1)](1+.2*sin(2*pi*(x-.7*t)))dx.`

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. Integrate q(x,t)=1+.2sin[2pi(x-.7t)] between the actual saved primary faces. Separately record geometry error against analytic face positions. Time checks use independent DOP853 at two tolerances for the same FV ODE.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/#ale-nonuniform-transport)

- selected-primary-reference-context: [Dennis L. Huff (1987), Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid](https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf) — NASA TM89890 grid-velocity and GCL discussion around equation11/printedp5 inspected. It attributes GCL to Thomas/Lombard. Original1979 paper not read; no airfoil algorithm or code reproduced. Our 1D scalar moving-volume/Heun derivation is independent.
#### Related test problem figures and code

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

Same-problem link

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

- [Run and validate: ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`) · [Code ZIP: ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Scope of this execution example: Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.




### C-grid: continuous Fourier solution and discrete-symbol exponential

Analytic reference · 2D

`Q(t)=exp(t*L)Q0; ktilde=2*sin(k*h/2)/h; ltilde=2*sin(l*h/2)/h; C=cos(k*h/2)*cos(l*h/2); g=H=f=1.`

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Evolve eta0=.01cos[2pi(x+2y)],u0=v0=0 with separate continuous3x3 Fourier-operator and discrete3x3-symbol exponentials. The primary actually advances2D staggered fields.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/#cgrid-rotating-wave)

- selected-primary-reference-context: [P. Korn and S. Danilov, Elementary dispersion analysis of some mimetic discretizations on triangular C-grids](https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf) — Governing linear equations, energy adjoints and AppendixB quadrilateral standard-C symbols/eq19–21 inspected. Use standard square C-grid only, not the paper triangular mimetic schemes. No global Williamson test or original code run.
#### Related test problem figures and code

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

Same-problem link

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

- [Run and validate: Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`) · [Code ZIP: Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Scope of this execution example: Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.




### L-corner singularity: harmonic field and separate smooth MMS

Analytic reference · 2D

`u=r^(2/3)*sin(2*theta/3); -Delta(u)=0; theta in[0,3*pi/2]; separate square MMS u=sin(pi*x)*sin(pi*y).`

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. Integrate the analytic corner field and gradient over elements, comparing uniform and a-priori graded meshes at matched DOFs. A separate unit-square sine MMS on regular/warped meshes separates singularity from distortion.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#lshape-fem)

- selected-primary-reference-context: [Long Chen, Introduction to Adaptive Finite Element Methods](https://lyc102.github.io/ifem/afem/) — Author documentation: L-shaped harmonic r^(2/3)sin(2theta/3) field and non-quasiuniform refinement motivation inspected. No MATLAB code copied or run; our removed quadrant/angle convention is explicitly defined.
- selected-primary-reference-context: [Joachim Schöberl, Interactive FEM: graded meshes around vertex singularities](https://jschoeberl.github.io/iFEM/FEM/erroranalysis.html) — Section24.4 weighted regularity and graded meshes inspected. Our fixed max-norm radial map is independently constructed; no general AMR implementation or universal optimality theorem claimed.
#### Related test problem figures and code

##### [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

Same-problem link

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

- [Run and validate: L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en) (`lshape-fem`) · [Code ZIP: L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.




### Annular vector-viscous MMS: force qualified by independent stress differentiation

Manufactured solution · 2D

`s=x*x+y*y; A=(s-1)*(4-s); u=(A*(1+x*y),A*(x*x-y*y)/2); mu=1+.2*s; f=-div(2*mu*epsilon(u)).`

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. Derive stress/force from the Cartesian vector field with s=x²+y²,A=(s-1)(4-s), then qualify force by separate Cartesian stress finite differentiation. Also check independent integrated body force(756pi/5,0).

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#annular-viscous-mms)

- selected-primary-reference-context: [MFEM developers, Example2: Linear Elasticity](https://mfem.org/examples/) — Example2 stress sigma=lambda div(u)I+mu(grad(u)+grad(u)^T), weak formulation and traction conventions inspected. Use lambda0 as a linear vector viscous BVP; manufactured fields are derived here. MFEM not executed or copied.
#### Related test problem figures and code

##### [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

Same-problem link

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

- [Run and validate: Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en) (`annular-viscous-mms`) · [Code ZIP: Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.




### Pure Neumann: analytic field, compatibility and mean gauge

Manufactured solution · 2D

`u=cos(2*pi*x)*cos(2*pi*y)+mean; f=8*pi^2*cos(2*pi*x)*cos(2*pi*y); dn(u)=0; integral(f)=-integral_boundary(dn(u)).`

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. Use point DOFs for u=cos(2pi*x)cos(2pi*y),f=8pi²u and zero outward normal flux. Distinguish means0/.25 and explicitly reject incompatible source+1 rather than projecting it away.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#poisson-neumann)

- selected-primary-reference-context: [PETSc developers, KSP: Solving Singular Systems](https://petsc.org/main/manual/ksp/) — Solving Singular Systems: constant Neumann nullspace and RHS compatibility inspected. We reject physical incompatibility rather than projecting it away. PETSc is neither a dependency nor executed.
#### Related test problem figures and code

##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

Same-problem link

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

- [Run and validate: Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) (`poisson-neumann`) · [Code ZIP: Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Solve singular2D Poisson with compatibility/gauge and reject incompatible source.




### Mixed Robin: 2D analytic field and independent normal flux

Manufactured solution · 2D

`u=cos(pi*x)*cos(2*pi*y)+x+y; -Delta(u)=5*pi^2*cos(pi*x)*cos(2*pi*y); alpha*u+beta*dn(u)=g.`

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. Use f=5pi²cos(pi*x)cos(2pi*y),outward Neumann±1 on x walls and analytic alpha*u+beta*dn(u)=g on y walls. Distinguish algebraic boundary-relation residual from analytic physical-normal-flux error.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#poisson-robin)

- selected-primary-reference-context: [MFEM developers, Boundary Conditions: Robin boundary conditions](https://mfem.org/fem_bc/) — Outward normal derivative and Robin weak boundary contribution inspected; Example27 source overview inspected. Our cell-centred face elimination/MMS is separately derived; no MFEM execution.
#### Related test problem figures and code

##### [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

Same-problem link

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

- [Run and validate: 2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en) (`poisson-robin`) · [Code ZIP: 2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.




### Relativistic symmetric collision: specialized two-shock Taub reference

Semi-analytic reference · 1D

`h_b^2-h_a^2=(p_b-p_a)*(h_b/rho_b+h_a/rho_a); v0^2=(p_b-p_a)*(e_b-e_a)/((e_a+p_b)*(e_b+p_a)); shock positions=.5 +/- Vs*t.`

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints. Solve the pressure root from Taub adiabat and relative-velocity relations for the identical resting star states and shock speeds, then integrate the piecewise-constant exact conserved field over cells. The contact degenerates; this is not a general three-wave Riemann solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/#srhd-collision)

- selected-primary-reference-context: [Luciano Rezzolla and Olindo Zanotti (2001), An Improved Exact Riemann Solver for Relativistic Hydrodynamics](https://arxiv.org/abs/gr-qc/0103005) — Original arxiv v2 read: sections2–4, equations2.3/2.4,3.1 and4.5; restricted two-shock specialization. No whole-paper or generic Riemann implementation audit.
- selected-primary-reference-context: [José A. Font (2008), Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity](https://link.springer.com/article/10.12942/lrr-2008-7) — Official article sections3.1–3.2, tensor49–51 and recovery68–69 actually read. Flat-spacetime use only; no whole-review or complete-GRMHD implementation audit.
#### Related test problem figures and code

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

Same-problem link

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

- [Run and validate: SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) (`srhd-collision`) · [Code ZIP: SRHD symmetric two-shock collision](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Scope of this execution example: Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.




### SRMHD circular wave: finite-amplitude exact family and independent tensor integration

Analytic reference · 1D

`K=rho*h+B0^2*(1+eta^2); vA^2=2*B0^2/(K+sqrt(K^2-4*eta^2*B0^4)); (By,Bz)=eta*B0*(cos(2*pi*(x-vA*t)),sin(2*pi*(x-vA*t))); (vy,vz)=-vA*(By,Bz)/B0.`

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D. Use the closed nonlinear Alfven-speed formula. Independently form conserved quantities/fluxes from point primitives through the stress tensor; qualify Gauss integration and complex-step PDE residuals. Rescale the original2pi period to the unit interval.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/#srmhd-alfven)

- selected-primary-reference-context: [L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007), ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics](https://arxiv.org/abs/0704.3206) — University-hosted original journal PDF section4.1 equations82–85 read; original arxiv preprint pages9–10 rendered and visually inspected, including normalization and period. Publisher PDF403. No whole-paper or ECHO-algorithm reproduction claim.
- selected-primary-reference-context: [José A. Font (2008), Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity](https://link.springer.com/article/10.12942/lrr-2008-7) — Official article sections3.1–3.2, tensor49–51 and recovery68–69 actually read. Flat-spacetime use only; no whole-review or complete-GRMHD implementation audit.
#### Related test problem figures and code

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

Same-problem link

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

- [Run and validate: SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) (`srmhd-alfven`) · [Code ZIP: SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Scope of this execution example: Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.




### Checkerboard diffusion: shared flux, MG and AMG

Finite-grid numerical reference · 2D

`-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}; T_f=|f|/(d_L/a_L+d_R/a_R)`

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/#checkerboard-diffusion)

- selected-official-formulation-context: [Two-point flux approximation](https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html) — Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.
- selected-official-formulation-context: [BoomerAMG: smoother options](https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html) — CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.
- publisher-abstract-only: [Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems](https://link.springer.com/article/10.1007/BF02238511) — Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.
#### Related test problem figures and code

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

Same-problem link

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

- [Run and validate: Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`) · [Code ZIP: Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Scope of this execution example: Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.




### Rotated diffusion: full-tensor Q1, MG and AMG

Manufactured solution · 2D

`-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T; f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y`

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/#rotated-anisotropic-diffusion)

- selected-official-formulation-context: [Two-point flux approximation](https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html) — Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.
- selected-official-formulation-context: [BoomerAMG: smoother options](https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html) — CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.
- publisher-abstract-only: [Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems](https://link.springer.com/article/10.1007/BF02238511) — Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.
#### Related test problem figures and code

##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

Same-problem link

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

- [Run and validate: Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`) · [Code ZIP: Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Scope of this execution example: Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.




### Neutral rectangular slab: genuine2P reference and YB

Semi-analytic reference · 3D

`phi=real2P+nonzero_modes+zero_mode-2alpha*q/sqrt(pi); E=.5sum(q*phi); F=-q grad(phi); DeltaE=2pi*Mz^2/V; DeltaFz=-4pi*q*Mz/V.`

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-slab-ewald/#neutral-slab-yb)

- reference-formula-or-scoped-context: [Fast and spectrally accurate Ewald summation for2-periodic electrostatic systems](https://arxiv.org/pdf/1109.1667) — Eq4 and AppendixA Eq41/zero-mode inspected; rendered selected pages requested. No full-paper audit or spectral-PME implementation claimed.
- reference-formula-or-scoped-context: [Ewald summation for systems with slab geometry](https://doi.org/10.1063/1.479595) — Original publisher full text unavailable; no original-text review claimed. Neutral correction independently derived and checked against official LAMMPS implementation/documentation.
- reference-formula-or-scoped-context: [LAMMPS slab Ewald documentation and neutral correction](https://docs.lammps.org/kspace_modify.html) — Slab geometry restrictions and official Ewald::slabcorr neutral formula inspected. No LAMMPS code copied or executed; mutable stable source is contextual, not a numerical dependency.
#### Related test problem figures and code

##### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) (`neutral-slab-yb`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#code-en)

Same-problem link

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

- [Run and validate: Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en) (`neutral-slab-yb`) · [Code ZIP: Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

Scope of this execution example: Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.




### Actual3D1/r FMM: multilevel translations, force and ownership

Finite-grid numerical reference · 3D

`Phi_i=-sum_{j!=i}G*m_j/r_ij; a_i=-sum_{j!=i}G*m_j*(x_i-x_j)/r_ij^3; finite6axis source Phi(0)=-1/a.`

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-fmm3d/#fmm3d-inverse-r)

- reference-formula-or-scoped-context: [The black-box fast multipole method](https://mc.stanford.edu/cgi-bin/images/f/fa/Darve_bbfmm_2009.pdf) — Tensor interpolation Eq7 and multilevel stages sections2–3 inspected, printed8715–8717; compression is separate. Original uncompressed educational implementation here, no timing reproduction.
- reference-formula-or-scoped-context: [FMM3D mathematical definitions](https://fmm3d.readthedocs.io/en/latest/math.html) — Official potential+1/(4pi r), gradient and source-self convention inspected. Our gravitational kernel is-1/r; FMM3D is not installed or run.
#### Related test problem figures and code

##### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#code-en)

Same-problem link

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

- [Run and validate: Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`) · [Code ZIP: Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

Scope of this execution example: Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.




### Unsoftened Kepler two-body time error

Analytic reference · 3D

`E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).`

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/#gravity-kepler)

- reference-formula-or-scoped-context: [JPL Keplerian-element formulas](https://ssd.jpl.nasa.gov/planets/approx_pos.html) — Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.
- reference-formula-or-scoped-context: [Geometric numerical integration illustrated by the Störmer–Verlet method](https://doi.org/10.1017/S0962492902000144) — Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.
#### Related test problem figures and code

##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

Same-problem link

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

- [Run and validate: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) (`gravity-kepler`) · [Code ZIP: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.




### Short-time32body dynamics from a cold Plummer-density sample

Finite-grid numerical reference · 3D

`a_i=-sum_{j!=i}G*m_j*r_ij/(r_ij^2+eps^2)^(3/2); U=-sum_{i<j}G*m_i*m_j/sqrt(r_ij^2+eps^2).`

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/#gravity-plummer-short)

- reference-formula-or-scoped-context: [On the Problem of Distribution in Globular Star Clusters](https://academic.oup.com/mnras/article/71/5/460/972150) — Bibliography inherited from prior scoped source review; original full text not read. The finite32-body cold initial condition is density-derived, not an equilibrium Plummer DF or exact continuum flow.
- reference-formula-or-scoped-context: [galpy official Plummer potential definition](https://docs.galpy.org/en/v1.11.0/reference/potentialplummer.html) — Official potential normalization read in preparatory source review. No galpy execution; density scale1 and pair softening.05 are distinct parameters.
- reference-formula-or-scoped-context: [SciPy1.14.1 solve_ivp](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html) — DOP853 order8, tolerance and t_eval semantics inspected; same softened finite-N ODE with independent scalar pair force. Not an exact analytic N-body solution.
- reference-formula-or-scoped-context: [Geometric numerical integration illustrated by the Störmer–Verlet method](https://doi.org/10.1017/S0962492902000144) — Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.
#### Related test problem figures and code

##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

Same-problem link

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

- [Run and validate: Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) (`gravity-plummer-short`) · [Code ZIP: Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.




### Warm PIC linear Landau damping

Semi-analytic reference · 1D

`D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).`

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/#thermal-landau-damping)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
- selected-primary-context: [Plasma dispersion function: official API mathematics](https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html) — Read the displayed integral definition and Maxwellian dispersion role. PlasmaPy is not installed or executed; SciPy Faddeeva is used with an independently derived dielectric.
- selected-primary-context: [SciPy1.14.1 roots_hermitenorm](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html) — Read Gauss–Hermite normal quadrature definition, exp(-x²/2) weight and degree2n-1 polynomial exactness. Used only for positive full-f initial particle weights; no Hermite PDE time evolution.
#### Related test problem figures and code

##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

Same-problem link

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

- [Run and validate: Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) (`thermal-landau-damping`) · [Code ZIP: Warm PIC linear Landau damping](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Scope of this execution example: Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.




### Warm PIC two-stream initial growth

Semi-analytic reference · 1D

`D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).`

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/#thermal-two-stream)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
- selected-primary-context: [Plasma dispersion function: official API mathematics](https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html) — Read the displayed integral definition and Maxwellian dispersion role. PlasmaPy is not installed or executed; SciPy Faddeeva is used with an independently derived dielectric.
- selected-primary-context: [SciPy1.14.1 roots_hermitenorm](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html) — Read Gauss–Hermite normal quadrature definition, exp(-x²/2) weight and degree2n-1 polynomial exactness. Used only for positive full-f initial particle weights; no Hermite PDE time evolution.
#### Related test problem figures and code

##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

Same-problem link

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

- [Run and validate: Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) (`thermal-two-stream`) · [Code ZIP: Warm PIC two-stream initial growth](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Scope of this execution example: Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.




### Independently coded PIC spatial pipeline

Finite-grid numerical reference · 1D

`rho=-.5cos(2x) => E=-.25sin(2x), electron a=+.25sin(2x); independent scalar CIC + dense DFT owns its self-consistent field every kick.`

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-pic-spatial/#pic-independent-spatial)

- selected-primary-context: [On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme](https://arxiv.org/abs/1311.2098) — Read selected original arXiv v2 sections2 (normalized1D1V Vlasov–Poisson),4 and5.2/5.4 (recurrence/noise and linear-window distinction). No whole-paper review, copied reference table, or original-run reproduction. Our positive-weight quiet loading and two-stream inputs differ.
#### Related test problem figures and code

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

Related-model problem

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

- [Run and validate: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) (`pic`) · [Code ZIP: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

- [Run and validate: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en) (`pic-conservation`) · [Code ZIP: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

- [Run and validate: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) (`pic-independent-spatial`) · [Code ZIP: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

Scope of this execution example: Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.




### Finite-Kn hard-sphere Couette flow

Finite-grid numerical reference · 1D

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

H=2lambda0; diffuse Twalls1, tangential Uwalls+/-0.5; nonlinear viscous heating retained. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/#dsmc-couette)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### Related test problem figures and code

##### [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) (`dsmc-couette`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#code-en)

Same-problem link

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

- [Run and validate: Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en) (`dsmc-couette`) · [Code ZIP: Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.




### Finite-Kn hard-sphere Fourier heat conduction

Finite-grid numerical reference · 1D

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

H=2lambda0; diffuse Tleft1,Tright2; fixed walls; no continuum linear-temperature reference. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/#dsmc-fourier)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### Related test problem figures and code

##### [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

Same-problem link

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

- [Run and validate: Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en) (`dsmc-fourier`) · [Code ZIP: Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.




### Mach2 planar hard-sphere shock

Finite-grid numerical reference · 1D

`partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.`

Monatomic gamma5/3,M1=2, RH inflow/outflow reservoirs at x0/16. Reference lambda2/lambda1=7/16; no profile shifting or shock pinning. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-shock/#dsmc-planar-shock)

- executed-independent-reference-implementation: [SPARTA official source, pinned commit1ae18f3646e7c89f86e965f0f3c13fcc5f32e399, unmodified serial mac target](https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399) — Actual selected source read: collide_vss,update constants,cell moment/flux definitions and boundary commands. Source archive/license/hash/build and all native inputs/raw outputs retained persistently; public cache and reproduction instructions provided.
- collision-and-boundary-conventions: [SPARTA official collide/surf_collide/fix emit-face documentation](https://sparta.github.io/doc/collide.html) — Read selected HS/VSS parameter relations, physical collision candidates, diffuse wall and incoming flux conventions. Bird1994 original book was not read; no full-original-book verification claim.
#### Related test problem figures and code

##### [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#code-en)

Same-problem link

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

- [Run and validate: Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`) · [Code ZIP: Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.




### LBM Re100 cavity: actual2D fields and Ghia centerlines

Finite-grid numerical reference · 2D

`Ghia1982Re100 centerline tables and primary-vortex location; these are rounded numerical data,not an exact whole-field solution.`

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-cavity/#lbm-cavity-re100)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.
- case-method-or-independent-reference: [High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method](https://www.sciencedirect.com/science/article/pii/0021999182900584) — Exact-byte existing17-point Re100columns and prior original-PDF/rendered-page provenance rechecked. Current session did not reacquire the original PDF. Printed398-399TablesI/II and408TableV provenance retained.
#### Related test problem figures and code

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

Related-model problem

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

- [Run and validate: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) (`cavity-ghia-re100`) · [Code ZIP: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

- [Run and validate: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) (`lbm-cavity-re100`) · [Code ZIP: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

Scope of this execution example: Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.




### LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity

Analytic reference · 2D

`u=U sin(x)cos(y) exp(-2nu t), v=-U cos(x)sin(y) exp(-2nu t); p=U^2 exp(-4nu t)[cos(2x)+cos(2y)]/4.`

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-taylor-green/#lbm-taylor-green)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.
#### Related test problem figures and code

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

Related-model problem

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

- [Run and validate: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

- [Run and validate: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) (`lbm-taylor-green`) · [Code ZIP: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

Scope of this execution example: Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.




### Curved LBM annular Couette control: velocity,pressure andtorque

Analytic reference · 2D

`u_theta=Ar+B/r; p=A^2r^2/2+2AB log(r)-B^2/(2r^2)+C; T_inner=-4pi rho nu B.`

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-annulus/#lbm-annular-couette-control)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Selected original sec3 printed410-414 via disclosed author-content mirror: Eq12/13/14 quadratic reflected-characteristic interpolation,moving-wall coefficient,Eq15 momentum exchange and compromised mass conservation. Generic Lagrange scalar oracle independently qualifies weights andsigns. No localPDF/rendered-symbol audit;2001BFLfulloriginal remains unread.
#### Related test problem figures and code

##### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

Same-problem link

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

- [Run and validate: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`) · [Code ZIP: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

Scope of this execution example: Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.




### Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet

Finite-grid numerical reference · 2D

`Re=Umean D/nu=20; CD=2Fx/(rho Umean^2 D); CL=2Fy/(rho Umean^2 D); delta p=p(.15,.2)-p(.25,.2).`

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-curved-boundary/#lbm-cylinder-re20)

- case-method-or-independent-reference: [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](https://arxiv.org/abs/comp-gas/9611001) — Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- case-method-or-independent-reference: [Lattice Boltzmann method for moving boundaries](https://doi.org/10.1016/S0021-9991(02)00022-0) — Selected original sec3 printed410-414 via disclosed author-content mirror: Eq12/13/14 quadratic reflected-characteristic interpolation,moving-wall coefficient,Eq15 momentum exchange and compromised mass conservation. Generic Lagrange scalar oracle independently qualifies weights andsigns. No localPDF/rendered-symbol audit;2001BFLfulloriginal remains unread.
- case-method-or-independent-reference: [Benchmark Computations of Laminar Flow Around a Cylinder](https://kent-and.github.io/mek4250/2021/SchaeferTurek1996.pdf) — Original chapter delivered by course mirror after official links404: printed3-4geometry/2D-1/force definitions,7protocol user-selected outlet,11-12Table3 estimated ranges. Not a full-paper or separate local rendered-symbol audit.
- case-method-or-independent-reference: [DFG flow around cylinder benchmark2D-1, Re20](https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark1_re20.html) — Actual geometry,do-nothingBC,mean-speed normalization,force/probe definitions and Nabh1998attribution read. Nabh original report not read; its precise values are contextual,not the adopted outlet truth.
- case-method-or-independent-reference: [Non-equilibrium extrapolation method for velocity and pressure boundary conditions in the lattice Boltzmann method](https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310) — Official primary abstract actually read: equilibrium/nonequilibrium split and adjacent-fluid extrapolation. Full primary equations unavailable; the adopted all-nine poststream density reservoir is independently derived and qualified,not labelled the exact author implementation.
#### Related test problem figures and code

##### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

Same-problem link

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

- [Run and validate: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`) · [Code ZIP: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

Scope of this execution example: Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.




### Isotropically scattering slab: continuous-angle Fredholm flux reference

Semi-analytic reference · 1D

`J(x)=.5*E2(x)+omega/2*integral_0^L E1(|x-y|)J(y)dy; R=2omega*integral J E2(x)dx; T=2E3(L)+2omega*integral J E2(L-x)dx; A=4(1-omega)*integral J dx.`

Plane-parallel steady optical-depth slab, unit incoming radiance on the left,vacuum incoming on the right,isotropic single-scattering albedo. Incoming hemispherical flux pi; signed-angle J=.5*integral I.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-scattering/#isotropic-scattering-slab)

- transfer-equation-and-boundary-convention: [Pharr,Jakob and Humphreys, Physically Based Rendering4e: The Equation of Transfer](https://www.pbr-book.org/4ed/Light_Transport_II_Volume_Rendering/The_Equation_of_Transfer) — Read selected transfer/source/finite-ray boundary section. The isotropic Fredholm normalization,independent exact-cell E1weights and flux derivations are documented in this packet; no DISORT reproduction or Monte Carlo claim.
#### Related test problem figures and code

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

Same-problem link

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

- [Run and validate: Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`) · [Code ZIP: Isotropic scattering in a finite slab](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

Scope of this execution example: Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.




### Su–Olson1996 diffusion: pinned independent integral evaluator

Semi-analytic reference · 1D

`epsilon*u_tau-u_xx=v-u; v_tau=u-v; u(0,tau)-2/sqrt(3)*u_x(0,tau)=1; u(infinity,tau)=0; epsilon*u+v is the capacity-weighted total.`

Half-space Marshak diffusion with zero initial radiation/material variables and epsilon1. Direct dimensionless evaluator; no ambiguous physical mass-opacity wrapper convention.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/#su-olson-diffusion1996)

- original-problem: [B. Su and G. L. Olson (1996), Benchmark results for the non-equilibrium Marshak diffusion problem, JQSRT56(3),337–351](https://doi.org/10.1016/0022-4073(96)84524-9) — Publisher abstract and bibliographic metadata read; original full text/equations/tables unavailable and not directly checked. Diffusion is distinct from the1997transport problem.
- reference-software-paper: [J. Thrussell and J. M. Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Bibliographic software credit,recorded separately from Su–Olson1996 and the pinned executed source. Full software paper is not claimed read.
- executed-reference-implementation: [LANL ExactPack1.7.5, pinned SuOlson/Timmes evaluator](https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson) — All55documentation,41wrapper and348Timmes module lines read. Execute nondimensional usolution/vsolution serially; qualify selected original/tight integrals against sensitivity,PDE and Robin checks. No primary solver shares this evaluator. Full ExactPack/base/library audit is not claimed.
- reference-source-license: [LANL ExactPack pinned BSD-3-Clause license](https://github.com/lanl/ExactPack/blob/8718b61f281a9744ea7a3820c51800915e4636e9/LICENSE.txt) — Actual license text read and retained as exactpack-LICENSE.txt with redistributed inert source snapshots.
#### Related test problem figures and code

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

Same-problem link

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

- [Run and validate: Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`) · [Code ZIP: Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Scope of this execution example: Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.




### Su–Olson transport: primary2023author-provided analytical benchmark data

Finite-grid numerical reference · 1D

`epsilon*I_tau+mu*I_x+I=V+Q; V_tau=E-V; E=.5*integral_-1^1 I dmu; I=2U of Crilly2023Appendix4.1; conserved total epsilon*E+V. Separate periodic companion: epsilon*I_t+mu*I_x=kappa*(V-I), V_t=kappa*(E-V); F approximately -E_x/(3*kappa), (epsilon+1)*E_t approximately E_xx/(3*kappa). For h=2*pi/N, A_N=.1*sin(h/2)/(h/2), E_diff=V_diff=1+A_N*exp[-s/(3*(epsilon+1))]*cos(x), t=kappa*s.`

Infinite symmetric1D angular transport/material exchange,epsilon1,no elastic scattering,cold initial state. Source Q1 for |x|<.5 and0<tau<10. Primary half-domain uses reflecting left and distant incoming-vacuum right; comparison times precede boundary influence. A separate matched periodic cell-mean companion uses physical x in [0,2*pi), c=epsilon=1, kappa4/8/16, N128/512/2048, Q0, initial I=V=1+.1cos(x), and t=kappa*s for s=0,.0625,.125,.25. Its IC/BC/source differ from the source-driven1997 benchmark; the FV, continuum-angular and diffusion comparisons within this companion use matched inputs.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/#su-olson-transport1997)

- original-problem: [B. Su and G. L. Olson (1997), An analytical benchmark for non-equilibrium radiative transfer in an isotropically scattering medium, Annals of Nuclear Energy24(13),1035–1055](https://doi.org/10.1016/S0306-4549(96)00100-4) — Publisher abstract/metadata read only. Original full text,integral normalization and original numerical tables were not directly read or transcribed. The actual comparison is independently attributed to the selected2023author repository below.
- primary-author-model-normalization: [A. Crilly (2023), Learning closure relations using differentiable programming: an example in radiation transport](https://raw.githubusercontent.com/ml4physicalsciences/ml4physicalsciences.github.io/master/2023/files/NeurIPS_ML4PS_2023_16.pdf) — Actually read and visually verified PDFpage6 Appendix4.1 equations7–10: epsilon*d_tau U+mu*d_x U+U=V/2+Q/2,V_tau=W−V. With I=2U, E=W. epsilon1,x0=.5,source duration10; no direct original1997-table verification.
- qualified-independent-published-data: [A. Crilly RTClosureJAX pinned SuOlsonData analytical benchmark tables](https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData) — Pinned W/Vtransport data,coordinates,times and README actually read. Repository calls them analytical Su–Olson data; transcription versus regeneration is undocumented. They are not trained-closure/model predictions. Retain full15×7raw table; compare13points at tau.1,1,3.16228 with matching source/epsilon/units. Rounded five-decimal finite data,not a rigorous exact reference.
- reference-data-license: [RTClosureJAX pinned MIT license](https://github.com/aidancrilly/RTClosureJAX/blob/3e4f636299d62bc03f7118cfc884230c756f9d87/LICENSE) — Actual MIT license read and retained with the bundled raw table. No redistribution of the2023paper PDF is required by this packet.
- shared-exponential-action-API: [SciPy1.14.1 expm_multiply: matrix exponential action and trace preconditioning](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.expm_multiply.html) — Actually inspected installed1.14.1 source/API docstring and the versioned official API action/traceA section. Shared by the new FV-mode and continuum-reference propagators; mathematical action equivalence is not bit equivalence or independent-engine evidence. The linked algorithm papers were not read as part of this update.
- independent-reference-propagator-qualification: [SciPy1.14.1 solve_ivp: DOP853 and complex initial states](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html) — Read selected official API sections for complex initial states,DOP853 and fixed tolerances. Two separately written continuum derivatives are compared to the shared exponential action under frozen141checks. This is finite reference qualification,not a primary SSPRK2 order test or a rigorous bound; original DOP853 papers were not reviewed here.
#### Related test problem figures and code

##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

Same-problem link

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

- [Run and validate: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) (`su-olson-transport1997`) · [Code ZIP: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Scope of this execution example: Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.




### Circular-absorber characteristic reference

Analytic reference · 2D

`I(x,y,t)=I_in(y)*exp(-kappa*ell_circle(x,y))*1_(x<t); Pxx=E,Pyy=Pzz=0 for the+xray.`

2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/#shadow-absorber2d)

- closure-and-model-limitations: [J. Rosdahl etal. (2013), RAMSES-RT: Radiation hydrodynamics in the cosmological context](https://arxiv.org/html/1304.7126v2) — Read selectedSection2 equations12–14 and opposing-beam limitation text. The static grey equations here are neither GR nor reproductions of RAMSES astrophysical calculations. Original Levermore1984 full text was not read.
- qualified-M1-numerical-method-context: [A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method](https://arxiv.org/pdf/1306.0010) — Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound. Actual generalized directional LF core passed762component checks,then all166fixed geometry gates. The authored LFcone proof is separate from the paper;no general nonlinearRiemannfan bound is claimed.
#### Related test problem figures and code

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

Same-problem link

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

- [Run and validate: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) (`shadow-absorber2d`) · [Code ZIP: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.




### Counterpropagating packet characteristic reference

Analytic reference · 2D

`Iplus(x,y,t)=6G(x-t,y;.25); Iminus(x,y,t)=6G(x+t,y;.75); E=Gplus+Gminus,Fx=Gplus-Gminus,Fy=0; Pxx=E,Pyy=Pzz=0.`

2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/#opposing-beams2d)

- closure-and-model-limitations: [J. Rosdahl etal. (2013), RAMSES-RT: Radiation hydrodynamics in the cosmological context](https://arxiv.org/html/1304.7126v2) — Read selectedSection2 equations12–14 and opposing-beam limitation text. The static grey equations here are neither GR nor reproductions of RAMSES astrophysical calculations. Original Levermore1984 full text was not read.
- qualified-M1-numerical-method-context: [A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method](https://arxiv.org/pdf/1306.0010) — Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound. Actual generalized directional LF core passed762component checks,then all166fixed geometry gates. The authored LFcone proof is separate from the paper;no general nonlinearRiemannfan bound is claimed.
#### Related test problem figures and code

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

Same-problem link

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

- [Run and validate: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) (`opposing-beams2d`) · [Code ZIP: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.




### GBM weak bias and Monte Carlo error

Analytic reference · 1D

`dX_t=\mu X_t\,dt+\sigma X_t\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \mathbb E[X_h(T)]=X_0(1+\mu h)^n`

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/#gbm-weak-moments)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### Related test problem figures and code

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

Related-model problem

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Run and validate: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) (`gbm-sde`) · [Code ZIP: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Scope of this execution example: Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [Run and validate: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en) (`gbm-weak-moments`) · [Code ZIP: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

- [Run and validate: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en) (`gbm-milstein-strong`) · [Code ZIP: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.




### OU weak moments with joint Brownian coupling

Analytic reference · 1D

`dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa`

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/#ou-weak-moments)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### Related test problem figures and code

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

![Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

Related-model problem

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Run and validate: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en) (`langevin-harmonic`) · [Code ZIP: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

- [Run and validate: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en) (`csvr-langevin-harmonic`) · [Code ZIP: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

- [Run and validate: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en) (`ou-weak-moments`) · [Code ZIP: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.




### Milstein and EM on identical Brownian paths

Analytic reference · 1D

`X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]; \mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]`

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/#gbm-milstein-strong)

- selected-primary-definition-or-diagnostic-algorithm: [An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations](https://epubs.siam.org/doi/10.1137/S0036144500378302) — Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.
#### Related test problem figures and code

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

Related-model problem

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

- [Run and validate: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) (`gbm-sde`) · [Code ZIP: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Scope of this execution example: Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [Run and validate: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en) (`gbm-weak-moments`) · [Code ZIP: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

- [Run and validate: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en) (`gbm-milstein-strong`) · [Code ZIP: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.




### Ordinary importance sampling of a normal rare tail

Analytic reference · 1D

`\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}; \mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)`

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/#normal-tail-importance)

- selected-primary-definition-or-diagnostic-algorithm: [Monte Carlo theory,methods and examples,Chapter9: importance sampling](https://artowen.su.domains/mc/Ch-var-is.pdf) — Selected author-chapter support,ordinary estimator,second moments and diagnostics were read during preparation. Current refetch returned403. No full-book or PERT experiment reproduction.
#### Related test problem figures and code

##### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en) (`normal-tail-importance`)

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#code-en)

Same-problem link

Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

- [Run and validate: Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en) (`normal-tail-importance`) · [Code ZIP: Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

Scope of this execution example: Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.




### Joint target and MCSE for a correlated bivariate Gaussian

Finite-grid numerical reference · 2D

`\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]; \operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}`

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/#correlated-gaussian-mcmc)

- selected-primary-definition-or-diagnostic-algorithm: [Rank-normalization,folding,and localization: An improved R-hat for assessing convergence of MCMC](https://arxiv.org/pdf/1903.08008) — Read selected original rank/foldedRhat,ESS and corrected Blom equation. No multivariate global-convergence certificate.
- selected-primary-definition-or-diagnostic-algorithm: [ArviZ0.20.0 public diagnostics API and selected implementation](https://python.arviz.org/en/v0.20.0/api/generated/arviz.mcse.html) — Read official0.20.0 ESS/MCSE source and API. Cache640values from128same-data observable/prefix arrays of8fixed chainsets in a separate process. Independence is the diagnostic engine,not an independent sampler.
#### Related test problem figures and code

##### [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en) (`correlated-gaussian-mcmc`)

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en#code-en)

Same-problem link

Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.

- [Run and validate: Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en) (`correlated-gaussian-mcmc`) · [Code ZIP: Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

Scope of this execution example: Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.




### Exterior series and scattering width of a dielectric cylinder

Analytic reference · 2D

`E_z^{\mathrm{sca}}=\sum_n i^n a_nH_n^{(1)}(kr)e^{in\theta},\quad\Sigma_{\mathrm{sca}}=4\sum_n|a_n|^2/k`

Lossless infinite cylinder, Ez polarization, c = epsilon0 = mu0 = 1, radius 0.25, epsilon = 2.25 and vacuum wavelength 1. The analytical field is exterior to the exact circle.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-cylinder/#cylinder-mie2d)

- selected-primary-documentation-or-authored-identity: [Mie scattering 2D](https://optics.ansys.com/hc/en-us/articles/360042703373-Mie-scattering-2D) — Read the complete substantive benchmark description: two-dimensional dielectric cylinder, TFSF, angular far field and lossless cross sections. Did not read the associated simulation files, theory table or cited book; no external numerical data imported. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- selected-primary-documentation-or-authored-identity: [Bessel and Hankel Wronskians, section10.5](https://dlmf.nist.gov/10.5) — Read section 10.5, especially equation 10.5.3 for the ordinary J/Hankel1 Wronskian; version 1.2.8. Cylinder boundary algebra is independently derived here. The year 2026 denotes DLMF version 1.2.8, released on 2026-09-15, not its initial publication year. Accessed on 2026-11-24.
#### Related test problem figures and code

##### [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en) (`cylinder-mie2d`)

![Real part of the actual saved scattered electric phasor on the finest two-dimensional grid. The central white region is a diagnostic mask at r<0.4, distinct from the physical cylinder radius0.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#code-en)

Same-problem link

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

- [Run and validate: Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en) (`cylinder-mie2d`) · [Code ZIP: Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

Scope of this execution example: Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.




### Complex oblique Fresnel coefficients and direct Lorentz-slab loss

Analytic reference · 2D

`\varepsilon(\omega)=\varepsilon_\infty+f/(\omega_0^2-\omega^2-i\gamma\omega)+i\sigma/\omega`

Vacuum surroundings, ky = 4, slab [4, 5], epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Compare omega = 5.1/6/6.9 for both s = Ez and p = Hz.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-lorentz/#lorentz-oblique-sp)

- selected-primary-documentation-or-authored-identity: [Meep Materials documentation](https://meep.readthedocs.io/en/latest/Materials/) — Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
#### Related test problem figures and code

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`)

![Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#code-en)

Same-problem link

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

- [Run and validate: Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`) · [Code ZIP: Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

Scope of this execution example: Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.




### Isolated same-grid reference for a long grazing dispersive packet

Finite-grid numerical reference · 2D

`\widehat U^n(k_x)=M(k_x,\Delta t)^n\widehat U^0(k_x),\quad K_y=2\sin(k_y\Delta y/2)/\Delta y`

The homogeneous Lorentz medium continues through the PML: epsilon_inf = 1, delta_epsilon = 0.2, omega_0 = 12, gamma = 0 or 0.005. An Ez-polarized finite-kx Gaussian has carrier omega = 6 and central phase angle 80 degrees. Joint grid/layer refinement uses peaks 6/9/12 on 512/768/1024 cells; the normal control uses 6 and damped fine companion 12. Final time is 700.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-grazing/#dispersive-grazing-pml)

- selected-primary-documentation-or-authored-identity: [Meep Materials documentation](https://meep.readthedocs.io/en/latest/Materials/) — Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- selected-primary-documentation-or-authored-identity: [Notes on Perfectly Matched Layers](https://arxiv.org/html/2108.05348v1) — Read sections 3.2–4.2, equations 7–8 and the time-domain ADE discussion, plus sections 5–7.2 on homogeneity, evanescent fields and grazing/discretization limitations. The served text is updated 2026-08-24. The trapezoidal filter is our derivation; no full original Berenger/Roden-Gedney paper review is claimed.
#### Related test problem figures and code

##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`)

![Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#code-en)

Same-problem link

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

- [Run and validate: Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`) · [Code ZIP: Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

Scope of this execution example: Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.




### Pivoted LU and Cholesky: exact-rational references for actual binary input

Analytic reference · Finite-dimensional algebra

`x_ref=round_binary64(exact_Fraction_solve(A_binary64,b_binary64)); r=b-Ax; eta_inf=||r||inf/(||A||inf||x||inf+||b||inf)`

The four fixed matrices use the actual binary64 A and b, converted exactly to Fractions. Rational elimination is exact, followed by a final binary64 rounding. Separate LAPACK comparisons share some numerical infrastructure. This is not a forward-accuracy guarantee for arbitrary ill-conditioned matrices.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#pivoted-direct-refinement)

- selected-official-documentation: [LAPACK Users Guide: Linear Equations](https://netlib.org/lapack/lug/node38.html) — Selected LU, Cholesky, conditioning and refinement paragraphs were read. This source uses mixed precision, unlike the selected same-precision RFS description.
#### Related test problem figures and code

##### [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`)

![The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#code-en)

Same-problem link

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

- [Run and validate: Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`) · [Code ZIP: Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.




### Symmetric saddles: independent dense solutions and the ideal-Schur spectrum

Finite-grid numerical reference · Finite-dimensional algebra

`S=B H^{-1} B^T; P=diag(H,S); spectrum(L^{-1} A L^{-T})={1,(1-sqrt(5))/2,(1+sqrt(5))/2}; x_ref=LAPACK_solve(A,b)`

Algebraic saddles A=[[H,B^T],[B,0]] use velocity sizes 12 and 24 and pressure sizes 5 and 11. Explicit dense SPD ideal-Schur controls compare the original residual separately with dense-solution error. This is not a Stokes boundary-value PDE.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#symmetric-saddle-minres)

- selected-author-documentation: [Paige and Saunders: MINRES author documentation](https://web.stanford.edu/group/SOL/software/minres/) — Selected symmetry, indefinite-system, SPD-preconditioning and original-residual discussion was read. The original 1975 paper was not newly read.
- selected-official-documentation: [LAPACK Users Guide: Linear Equations](https://netlib.org/lapack/lug/node38.html) — Selected LU, Cholesky, conditioning and refinement paragraphs were read. This source uses mixed precision, unlike the selected same-precision RFS description.
#### Related test problem figures and code

##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

Same-problem link

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

- [Run and validate: Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`) · [Code ZIP: Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.




### Restarting and shift-invert: the closed spectrum of a fixed discrete matrix

Analytic reference · Finite-dimensional algebra

`lambda_j=4/h^2*sin(j*pi/(2*(n+1)))^2,n=31; mu=1/(lambda-sigma); lambda=sigma+1/mu`

A fixed 31 x 31 Dirichlet tridiagonal matrix with h=1/32, restart lengths 8 and 16, and shifts none/0/950. The references are eigenvalues of this finite matrix, not a continuum PDE grid-convergence study.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#restarted-shift-invert)

- selected-official-documentation: [SLEPc EPS manual: projection and spectral transformations](https://slepc.upv.es/release/documentation/manual/eps.html) — Selected projection, restarting and generalized-problem discussion was read. No SLEPc execution or Krylov-Schur reproduction is claimed.
#### Related test problem figures and code

##### [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) (`restarted-shift-invert`)

![The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#code-en)

Same-problem link

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

- [Run and validate: Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en) (`restarted-shift-invert`) · [Code ZIP: Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.




### Consistent-mass P1 string: closed discrete and continuum eigenvalues

Analytic reference · 1D

`Kx=lambda_h Mx; lambda_j,h=6*(1-cos(theta_j))/(h^2*(2+cos(theta_j))),theta_j=j*pi/(n+1); lambda_j=(j*pi)^2,phi_j(x)=sin(j*pi*x)`

Unit length, tension and density, homogeneous Dirichlet endpoints, 15/31/63 interior nodes, and the lowest three eigenpairs. Compare closed discrete eigenvalues with generalized dense LAPACK, then measure error relative to (j*pi)^2 separately. Displayed vectors are saved numerical modes with arbitrary sign.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#fem-mass-eigen)

- selected-official-documentation: [SciPy 1.14.1 LOBPCG](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html) — Selected SPD B, operator, preconditioner M, history and rod-example discussion was read. This uses the maintained SciPy implementation, not an original LOBPCG implementation.
- selected-official-documentation: [SLEPc EPS manual: projection and spectral transformations](https://slepc.upv.es/release/documentation/manual/eps.html) — Selected projection, restarting and generalized-problem discussion was read. No SLEPc execution or Krylov-Schur reproduction is claimed.
#### Related test problem figures and code

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

Same-problem link

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

- [Run and validate: Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) (`fem-mass-eigen`) · [Code ZIP: Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.




### Crossing the Bratu fold with pseudo-arclength continuation

Analytic reference · 1D

`u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)`

Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-bratu-continuation-jfnk/#bratu-fold-continuation)

- algorithm-primary: [Condition Estimates for Pseudo-Arclength Continuation](https://ipsen.math.ncsu.edu/ps/sinum65438.pdf) — Section2.2, printedpp265–266, Eqs2.2–2.5; tangent null equation, unit Euclidean tangent, augmented system and tangent hyperplane. Weighted h-sum metric is the implementation’s stated discrete variation. No full condition-number proof or original paper numerical benchmark is borrowed.
- analytic-reference: [Finite differences for the1D Bratu problem,Problem8](https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html) — Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.
#### Related test problem figures and code

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

Same-problem link

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

- [Run and validate: Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`) · [Code ZIP: Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Scope of this execution example: Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.




### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

Analytic reference · 1D

`u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)`

Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-bratu-continuation-jfnk/#bratu-matrix-free-jfnk)

- algorithm-primary: [Jacobian-free Newton-Krylov methods: a survey of approaches and applications](https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf) — Selectedsec2.3,2.3.1,2.3.2 and2.4.1, printedpp361–363: matrix-free Jv action, perturbation scaling, inexact forcing Eq16 and line-search globalization. Actual central difference denominator2h and eps_machine^(1/3) scaling are independently specified/qualified, not an attribution to a PETSc default. No whole41-page audit or paper solver result reuse.
- algorithm-primary: [Choosing the Forcing Terms in an Inexact Newton Method](https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf) — Section1 AlgorithmIN/Eq1.2; selectedsec2 Choice2/Eq2.6; practical-safeguard paragraphssec2.1, printedpp16,20,22–23. Core eta=gamma*(||F_k||/||F_{k-1}||)^alpha is Choice2-style. Our gamma.9/alpha1.5 with eta_initial.3 and fixed[.001,.5] clamp omits the paper’s previous-eta safeguard. This is a declared variant, not its complete safeguarded algorithm or an asymptotic convergence certification.
- analytic-reference: [Finite differences for the1D Bratu problem,Problem8](https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html) — Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.
- context-only: [PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length](https://petsc.org/release/manual/snes/) — Selected Inexact Newton-like Methods and beginning of Matrix-Free Methods, residual forcing inequality and matrix-free/preconditioner distinction. Context only. No PETSc installation/execution or borrowed numerical success. Our hyperplane continuation is not a claim to implement every SNES arc-length scheme.
#### Related test problem figures and code

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

Same-problem link

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

- [Run and validate: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`) · [Code ZIP: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Scope of this execution example: Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.
