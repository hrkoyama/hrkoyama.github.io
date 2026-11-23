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

固定入力実行例は未登録です。



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

この項目に対応付けられたテスト問題は未登録です。



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

No fixed-input execution example is registered.



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

No associated test problem is registered for this entry.



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
