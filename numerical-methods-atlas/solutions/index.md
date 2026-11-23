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




### Nohの冷たい流入衝撃波：平面・円筒対称

解析解 · 1次元

`s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.`

理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)と円筒対称の半径方向(d=2)の有限体積計算で、圧力の床は使いません。カラー図は1次元の半径方向解を回転表示したもので、Cartesianの2次元計算ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/#noh-shock)

- original-problem: [W. F. Noh (1987), Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux, JCP72,78–120](https://doi.org/10.1016/0021-9991(87)90074-X) — Original problem and wall-heating analysis. Publisher metadata/abstract checked; no claim of reproducing every original calculation.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Noh1987. The analytic evaluator is a reference, not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, exactpack/solvers/noh/noh1.py](https://github.com/lanl/ExactPack/blob/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/noh/noh1.py) — BSD-3-Clause. Actual evaluation is restricted to gamma=5/3,rho0=1,inward speed1. Source hashes, point/shell comparisons and parameter-limit control are saved in the Noh release.
#### 関連するテスト問題の図とコード

##### [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![内向きに収束する流れが、外向きに進む衝撃波を作ります。円筒対称の1次元有限体積密度を回転表示し、厳密なセル平均と比較します。独立した2次元Euler計算ではありません。初期圧力ゼロ、γ=5/3、512セル、t=0.6。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

同じ問題への対応

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

- [実行・検証：Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP：Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

この実行例の範囲：圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。




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




### Noh cold-inflow shock: planar and cylindrical symmetry

Analytic reference · 1D

`s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.`

Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1) and cylindrically symmetric radial (d=2) finite-volume calculations; no pressure floor. The radial color image is a revolved one-dimensional solution, not a two-dimensional Cartesian computation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/#noh-shock)

- original-problem: [W. F. Noh (1987), Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux, JCP72,78–120](https://doi.org/10.1016/0021-9991(87)90074-X) — Original problem and wall-heating analysis. Publisher metadata/abstract checked; no claim of reproducing every original calculation.
- reference-software-paper: [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](https://doi.org/10.1016/j.softx.2023.101560) — Cite the software paper separately from Noh1987. The analytic evaluator is a reference, not a numerical Euler solver.
- executed-reference-implementation: [LANL ExactPack, commit9bacc477eb791e959c9621e771fc7a725db755fa, exactpack/solvers/noh/noh1.py](https://github.com/lanl/ExactPack/blob/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/noh/noh1.py) — BSD-3-Clause. Actual evaluation is restricted to gamma=5/3,rho0=1,inward speed1. Source hashes, point/shell comparisons and parameter-limit control are saved in the Noh release.
#### Related test problem figures and code

##### [Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Inward converging flow generates an outward moving shock. Revolved density from a 1D cylindrical-radial finite-volume calculation, compared with exact cell means. This is not an independent 2D Euler calculation. Zero initial pressure, gamma=5/3, 512 cells, t=0.6.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

Same-problem link

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

- [Run and validate: Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP: Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip)

Scope of this execution example: A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.
