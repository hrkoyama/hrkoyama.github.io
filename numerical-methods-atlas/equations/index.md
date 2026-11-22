# 方程式・モデル / Equations and models

https://hrkoyama.github.io/numerical-methods-atlas/equations/

## 日本語

### 線形移流

ID: `linear-advection` · local-example

$$
\partial_t u+a\,\partial_xu=0
$$

一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/)

#### 関連するテスト問題の図とコード

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [実行・検証：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。


##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [非対称移流拡散離散系の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja) (`sparse-advection-diffusion`)

![保存済み非対称離散系の真の残差履歴。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#code-ja)

定常の離散移流拡散行列です。リンク先は移流項と拡散項の基礎であり、各単独式がこの行列問題全体を表すわけではありません。

固定入力実行例は未登録です。



### 熱・拡散方程式

ID: `heat` · local-example

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/)

#### 関連するテスト問題の図とコード

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [非対称移流拡散離散系の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja) (`sparse-advection-diffusion`)

![保存済み非対称離散系の真の残差履歴。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#code-ja)

定常の離散移流拡散行列です。リンク先は移流項と拡散項の基礎であり、各単独式がこの行列問題全体を表すわけではありません。

固定入力実行例は未登録です。

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

![周期Fourierモードの線形反応拡散。16/32/64格子の連続解誤差と、固定格子での半離散厳密解に対する時間誤差を分けた保存収束図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

線形反応拡散u_t=D u_xx+r u（公開入力はD=0.1、r=0.1）です。熱方程式へのリンクは拡散部分で、反応項を含む固有値r-Dk²で比較します。

- [実行・検証：反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`) · [コードZIP：反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。




### Poisson・Laplace方程式

ID: `poisson-laplace` · local-example

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/)

#### 関連するテスト問題の図とコード

##### [1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

![保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

- [実行・検証：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`) · [コードZIP：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。


##### [1次元Poisson・純Neumann境界](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja) (`poisson-1d-neumann`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-neumann.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [1次元Poisson・Dirichlet/Neumann混合境界](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja) (`poisson-1d-mixed`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-mixed.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [1次元Poisson・Robin境界の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja) (`poisson-1d-robin`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja) (`poisson-2d-broad`)

![保存済みの広帯域ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [2次元Poisson・局在ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja) (`poisson-2d-localized`)

![保存済み局在ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [実行・検証：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP：2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

- [実行・検証：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja) (`sa-amg`) · [コードZIP：行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

この実行例の範囲：正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。


##### [2次元Poisson・一様ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja) (`poisson-2d-uniform`)

![保存済み一様ソースPoisson問題のマルチグリッド残差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [2次元Poisson・乱数ソースの離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja) (`poisson-2d-random`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [3次元周期Poisson・Fourier製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja) (`poisson-3d-periodic`)

![保存済み3次元周期Poisson解の3断面。3次元流体計算ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [1次元周期Poisson・擬似時間による定常解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja) (`poisson-1d-periodic`)

![保存済み擬似時間定常解の誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) (`periodic-particles`)

![共有図の周期PM部分。孤立ツリーの比較は別問題です。](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#code-ja)

- [実行・検証：周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) (`periodic-particles`) · [コードZIP：周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。


##### [孤立FFTと非周期直接畳み込み](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=ja) (`isolated-convolution`)

![境界核の共有図。このカードは「孤立畳み込み」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=ja#code-ja)

重力Poisson方程式の孤立境界に対応する密度場の畳み込み問題です。粒子の軟化二体力や全方向周期Poissonの例とは区別し、この図ではゼロ埋めFFTと同じ離散核の非周期直接畳み込みを照合します。

固定入力実行例は未登録です。

##### [一様平面スラブの重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja) (`uniform-slab`)

![境界核の共有図。このカードは「一様平面スラブ」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja#code-ja)

水平周期・鉛直孤立の重力Poisson問題で、一様平板の零水平モードを扱います。下のPoisson代表式に対し、ここでの右辺は4πGρです。全方向周期境界や軟化粒子系とは区別します。

固定入力実行例は未登録です。

##### [正弦波状薄層の重力](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja) (`sinusoidal-sheet`)

![境界核の共有図。このカードは「正弦薄層」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja#code-ja)

水平周期・鉛直孤立の重力Poisson問題で、面密度の非零水平モードと零モードを扱います。Poisson代表式の右辺は4πGρです。全方向周期場や軟化粒子の二体力とは区別します。

固定入力実行例は未登録です。

##### [中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

![中性立方セルの非対称8点電荷。Ewaldの実空間・逆空間打切りに対する力の差を保存値から表示。smooth PMEの格子・Bスプライン次数比較は同じ問題の補助例へ接続。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

リンクは静電Poisson/Laplace場です。中性周期Coulomb電荷のEwald/PME問題であり、重力の質量・符号・境界を流用しません。

- [実行・検証：中性周期セルのEwald和と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja) (`ewald`) · [コードZIP：中性周期セルのEwald和と独立theta積分](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

- [実行・検証：Bスプラインsmooth PMEの格子・次数収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja) (`spme`) · [コードZIP：Bスプラインsmooth PMEの格子・次数収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。


##### [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) (`logarithmic-particles`)

![固定seedの128粒子、2次元自由空間の対数核。FMMの展開次数2/4/8/12を独立した全対直接和と比べたポテンシャル・電場誤差の保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#code-ja)

2次元Poisson/Laplaceの対数Green核を用いる粒子和です。3次元軟化重力1/rモデルとは区別します。

- [実行・検証：2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja) (`fmm`) · [コードZIP：2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。


##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

Poissonへのリンクは自己無撞着な静電場の部分です。粒子の運動・CIC補間を結合したPIC全体の式が一覧に揃っているわけではありません。

- [実行・検証：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) (`pic`) · [コードZIP：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。




### 非粘性Burgers方程式

ID: `burgers` · local-example

$$
\partial_tu+\partial_x(u^2/2)=0
$$

非線形のスカラー保存則。衝撃波と膨張波を比較する。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/equation-gallery/)

#### 関連するテスト問題の図とコード

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja) (`burgers-shock`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja) (`burgers-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#code-ja)

固定入力実行例は未登録です。



### LWR交通流モデル

ID: `traffic` · local-example

$$
\partial_t\rho+\partial_x[\rho(1-\rho)]=0
$$

無次元化した代表流束。渋滞の上流伝播と希薄化を調べる。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/equation-gallery/)

#### 関連するテスト問題の図とコード

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja) (`traffic-jam`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja) (`traffic-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#code-ja)

固定入力実行例は未登録です。



### 圧縮性Euler方程式

ID: `euler` · local-example

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)

#### 関連するテスト問題の図とコード

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

- [実行・検証：Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja) (`sod`) · [コードZIP：Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。


##### [Lax衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=ja) (`lax`)

![共有図の左パネル：Lax衝撃波管。右は別のエントロピー波収束計算。](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

- [実行・検証：Shu–Osher：特性WENO-Zと高解像度参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja) (`shu-osher`) · [コードZIP：Shu–Osher：特性WENO-Zと高解像度参照](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：[-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。

- [実行・検証：Shu–Osher：独立参照と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja) (`shu-independent`) · [コードZIP：Shu–Osher：独立参照と格子収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

この実行例の範囲：衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。


##### [1次元Eulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja) (`entropy-1d`)

![保存済みの1次元エントロピー波の密度誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [移動接触不連続](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja) (`moving-contact`)

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [1次元の強い圧力ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja) (`strong-shock`)

![完了したPPM計算の保存密度。停止した他の変種とは区別しています。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![保存済み2次元Double Mach反射の最終フレーム。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/double-mach/frame-080.webp)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![保存済みMach 3前向きステップの計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/step-m3-mc.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja) (`entropy-2d`)

![保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [円柱前面の弓形衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja) (`cylinder-forebody`)

![保存済み円柱前面の密度比較。有限時刻の結果で、定常収束の認定ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja) (`odd-even`)

![保存済み定常平面衝撃波のodd–even診断。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

![保存したKEEP移動渦の最終フレーム。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/keep-vortex/frame-080.webp)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

固定入力実行例は未登録です。



### 浅水方程式

ID: `shallow-water` · local-example

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

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/geophysical-grids/)

#### 関連するテスト問題の図とコード

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

固定入力実行例は未登録です。



### 等温流体方程式

ID: `isothermal` · local-example

$$
\rho_t+(\rho u)_x=0
$$

$$
(\rho u)_t+(\rho u^2+c_s^2\rho)_x=0
$$

一定の等温音速cₛを用いる1次元の代表形。密度ジャンプの参照解へ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)

#### 関連するテスト問題の図とコード

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

固定入力実行例は未登録です。



### 理想MHD

ID: `mhd` · local-example

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/)

#### 関連するテスト問題の図とコード

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

- [実行・検証：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja) (`ct-glm-independent`) · [コードZIP：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

この実行例の範囲：同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

- [実行・検証：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja) (`ct-glm-ot-convergence`) · [コードZIP：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

この実行例の範囲：同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。


##### [Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) (`brio-wu`)

![保存済みBrio–Wu衝撃波管の比較図。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#code-ja)

- [実行・検証：Brio–Wu：HLLDと保存的に粗視化した数値参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja) (`brio-wu`) · [コードZIP：Brio–Wu：HLLDと保存的に粗視化した数値参照](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。

- [実行・検証：Brio–Wu：別実装HLLDとの照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja) (`brio-independent`) · [コードZIP：Brio–Wu：別実装HLLDとの照合](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

この実行例の範囲：公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。


##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

![保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) (`advected-magnetostatic-equilibrium`)

![非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#code-ja)

周期単位正方形・γ=5/3・μ0=1の平面理想MHDを扱います。構成した磁気静力学平衡を一定速度で移流する厳密解で、外力による製造解や標準円偏光Alfvén波とは異なります。GLMの補助方程式と具体的な保存変数セル平均は、実行例の式・入力・コードを参照してください。

- [実行・検証：CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja) (`ct-glm-smooth-convergence`) · [コードZIP：CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

この実行例の範囲：非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。




### 非圧縮Navier–Stokes

ID: `navier-stokes` · local-example

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。公開例は周期2次元MAC格子の射影法とTaylor–Green渦です。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)

#### 関連するテスト問題の図とコード

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

- [実行・検証：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。


##### [周期せん断波の粘性減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja) (`lbm-shear`)

![保存済みせん断波振幅と粘性減衰の参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja)

格子BGKが計算モデル、非圧縮Navier–Stokesは低Mach数で比較する巨視的な減衰モデルです。

固定入力実行例は未登録です。

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja) (`channel-poiseuille`)

![保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja)

格子BGK・体積力・半格子壁を使う計算と、巨視的な定常非圧縮流路解を結びます。

固定入力実行例は未登録です。



### 等温格子BGK

ID: `bgk` · local-example

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/)

#### 関連するテスト問題の図とコード

##### [周期せん断波の粘性減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja) (`lbm-shear`)

![保存済みせん断波振幅と粘性減衰の参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja)

格子BGKが計算モデル、非圧縮Navier–Stokesは低Mach数で比較する巨視的な減衰モデルです。

固定入力実行例は未登録です。

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja) (`channel-poiseuille`)

![保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja)

格子BGK・体積力・半格子壁を使う計算と、巨視的な定常非圧縮流路解を結びます。

固定入力実行例は未登録です。



### Hamilton系・振動子

ID: `hamiltonian` · local-example

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)

#### 関連するテスト問題の図とコード

##### [調和振動子（複素ODE表示も統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja) (`harmonic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#code-ja)

- [実行・検証：調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja) (`harmonic-oscillator`) · [コードZIP：調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。


##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja) (`quartic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

![調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

Hamilton系へのリンクは調和ポテンシャルの力学部分です。計算には摩擦・雑音またはCSVRの温度浴が追加されます。

- [実行・検証：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja) (`langevin-harmonic`) · [コードZIP：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

- [実行・検証：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja) (`csvr-langevin-harmonic`) · [コードZIP：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。


##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

![弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

Hamilton系へのリンクは非調和ポテンシャルの力学部分です。確率温度浴を加えたCSVR・Langevinの分布検証を行います。

- [実行・検証：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja) (`csvr-langevin-quartic`) · [コードZIP：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。




### 重力粒子モデル

ID: `particle-gravity` · local-example

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)

#### 関連するテスト問題の図とコード

##### [3次元周期Poisson・Fourier製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja) (`poisson-3d-periodic`)

![保存済み3次元周期Poisson解の3断面。3次元流体計算ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [孤立粒子群の軟化重力（ツリー・直接和）](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja) (`isolated-particles`)

![保存済みツリー力と直接和の相対誤差。開き角・展開次数を比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja#code-ja)

- [実行・検証：Barnes–Hut：192粒子と直接和の比較](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja) (`barnes-hut`) · [コードZIP：Barnes–Hut：192粒子と直接和の比較](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

この実行例の範囲：孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。


##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) (`periodic-particles`)

![共有図の周期PM部分。孤立ツリーの比較は別問題です。](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#code-ja)

- [実行・検証：周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) (`periodic-particles`) · [コードZIP：周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。




### Bratu非線形境界値問題

ID: `bratu` · local-example

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/)

#### 関連するテスト問題の図とコード

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

- [実行・検証：1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja) (`bratu`) · [コードZIP：1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：−u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。




### 補助的な双曲型拡散系

ID: `hyperbolic-diffusion` · local-example

$$
\partial_\tau u-\nu\partial_xp=f
$$

$$
\partial_\tau p-T_r^{-1}\partial_xu=-p/T_r
$$

τは擬似時間、Trは緩和時間。定常でp=uₓ、−νuₓₓ=fを回復します。物理時間の熱拡散とは区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/hyperbolic-diffusion/)

#### 関連するテスト問題の図とコード

##### [1次元周期Poisson・擬似時間による定常解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja) (`poisson-1d-periodic`)

![保存済み擬似時間定常解の誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja#code-ja)

固定入力実行例は未登録です。



### 特殊相対論的流体（SRHD）

ID: `srhd` · reading

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

c=1、平坦なCartesian時空での理想流体の代表形。状態方程式と原始変数の回復が必要です。アトラスでは文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#what-changes-from-the-existing-euler-examples)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 一般相対論的流体（GRHD）

ID: `grhd` · reading

$$
\nabla_\mu(\rho_0u^\mu)=0,\qquad\nabla_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p g^{\mu\nu}
$$

c=G=1、計量符号(−,+,+,+)の理想流体。背景計量を固定する場合と、Einstein方程式も解く場合を区別します。文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#19721998-from-curved-background-flows-to-conservative-hrsc)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 一般相対論的MHD（GRMHD）

ID: `grmhd` · reading

$$
\nabla_\mu(\rho_0u^\mu)=0
$$

$$
\nabla_\mu(T_{\rm fluid}^{\mu\nu}+T_{\rm EM}^{\mu\nu})=0
$$

$$
\nabla_\mu{}^*F^{\mu\nu}=0,\qquad F^{\mu\nu}u_\nu=0
$$

理想電気伝導の代表形。物質と電磁場の応力エネルギー、磁場制約、計量を組み合わせます。状態方程式・時空の扱いを含む完全系は解説先へ。文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#19992006-magnetic-constraints-and-dynamical-spacetime)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 相対論的放射モーメント・M1

ID: `m1-radiation` · reading

$$
\nabla_\mu T^{\mu\nu}=G^\nu,\qquad\nabla_\mu R^{\mu\nu}=-G^\nu
$$

$$
P^{ij}=D_{\rm M1}^{ij}(E,\boldsymbol F)\,E
$$

Gνを物質が受け取る四元力と定義した模式形。Rは放射の応力エネルギー、Pは放射圧テンソル。M1は角度モーメントの閉包で、放射分布全体を厳密に解くものではありません。文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#2013-onward-radiation-and-microphysics-add-stiff-systems)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 因果的な相対論的粘性流体

ID: `causal-viscous` · reading

$$
\nabla_\mu T^{\mu\nu}=0,\qquad T^{\mu\nu}=T_{\rm ideal}^{\mu\nu}+\Pi\Delta^{\mu\nu}+\pi^{\mu\nu}
$$

$$
\tau_\pi D\pi^{\langle\mu\nu\rangle}+\pi^{\mu\nu}=\pi_{\rm NS}^{\mu\nu}+\cdots
$$

下段はIsrael–Stewart型の緩和を示す模式式で、完全な構成則ではありません。追加緩和変数を使わないBDNKなどの一階理論と区別します。因果性の条件は理論・状態方程式に依存し、文献解説のみです。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#a-parallel-19792019-branch-causal-viscous-fluid-theory)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### ロジスティック個体群増殖

ID: `bio-logistic` · local-example

$$
\dot N=rN(1-N/K)
$$

収容力Kを持つ密度依存の連続時間増殖モデル。離散ロジスティック写像とは区別します。 限定した実行例：無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#01-1838-logistic-population-growth)

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

#### 関連するテスト問題の図とコード

##### [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja) (`logistic-growth`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#code-ja)

- [実行・検証：ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja) (`logistic-growth`) · [コードZIP：ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

この実行例の範囲：無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。




### Michaelis–Mentenと完全酵素反応系

ID: `bio-enzyme` · reading

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#02-1913-michaelismenten-and-full-enzyme-kinetics)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Lotka–Volterra捕食・被食

ID: `bio-lotka-volterra` · reading

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#03-1920-lotkavolterra-predatorprey)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### McKendrick年齢構造個体群

ID: `bio-age-structure` · reading

$$
\partial_t n+\partial_a n=-\mu(a)n
$$

$$
n(0,t)=\int_0^\infty b(a)n(a,t)\,da
$$

年齢aに沿う輸送と死亡、新生個体の非局所な更新境界を持つモデルです。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#04-1926-mckendrick-age-structured-population)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### SIR・SEIR区画モデル

ID: `bio-sir` · local-example

$$
\dot s=-\beta si
$$

$$
\dot i=\beta si-\gamma i
$$

$$
\dot r=\gamma i
$$

$$
s+i+r=1
$$

閉じた一様混合集団の規格化SIR系。SEIRは曝露区画を追加します。人数と割合ではβの定義が異なります。 限定した実行例：閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#05-1927-sir-and-seir-compartment-models)

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

#### 関連するテスト問題の図とコード

##### [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja) (`sir-epidemic`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#code-ja)

- [実行・検証：SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja) (`sir-epidemic`) · [コードZIP：SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

この実行例の範囲：閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。




### Fisher–KPP侵入前線

ID: `bio-fisher-kpp` · reading

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#06-1937-fisherkpp-invasion-front)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Monod増殖とケモスタット

ID: `bio-monod` · reading

$$
\mu(S)=\mu_{\max}\frac{S}{K_S+S}
$$

$$
\dot X=(\mu(S)-d)X
$$

$$
\dot S=d(S_{in}-S)-\mu(S)X/Y
$$

基質S、菌体X、収率Y、希釈率dの代表形。d=0の閉鎖バッチとケモスタットを区別します。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#07-1949-monod-growth-and-chemostat)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Hodgkin–Huxley膜動態

ID: `bio-hodgkin-huxley` · reading

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#08-1952-hodgkinhuxley-membrane-dynamics)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Turing反応拡散の枠組み

ID: `bio-turing` · local-example

$$
u_t=D_u\Delta u+f(u,v)
$$

$$
v_t=D_v\Delta v+g(u,v)
$$

2成分反応拡散の枠組み。f・gは個別に指定する必要があり、模様の画像だけでTuring機構とは判定できません。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#09-1952-turing-reactiondiffusion-framework)

a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。

#### 関連するテスト問題の図とコード

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [実行・検証：Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`) · [コードZIP：Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

- [実行・検証：Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) (`schnakenberg-nonlinear`) · [コードZIP：Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

この実行例の範囲：t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

- [実行・検証：Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) (`schnakenberg-pattern`) · [コードZIP：Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

この実行例の範囲：t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。




### FitzHugh–Nagumoの興奮と回復

ID: `bio-fitzhugh-nagumo` · local-example

$$
v_t=D\Delta v+v-v^3/3-w+I
$$

$$
w_t=\epsilon(v+a-bw)
$$

高速の興奮と低速の回復を結ぶ規格化した代表形。係数・符号・空間拡張には複数の規約があります。 限定した実行例：公開実行例はD=0の空間なしの縮約ODEです。FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#10-1961-fitzhughnagumo-excitation-and-recovery)

FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

#### 関連するテスト問題の図とコード

##### [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`)

![無次元の2変数FHN型ODEにt=10〜20の電流パルス。DOP853参照とRK4の興奮・回復、刻み0.1/0.05/0.025の収束と全出力点の差を保存結果から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#code-ja)

公開固定入力は空間拡散を含まない2変数ODEの極限です。一般の伝播PDEを検証したという意味ではありません。

- [実行・検証：FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`) · [コードZIP：FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。




### Keller–Segel走化性

ID: `bio-keller-segel` · reading

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#11-1970-kellersegel-chemotaxis)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Gierer–Meinhardt活性化・抑制

ID: `bio-gierer-meinhardt` · reading

$$
a_t=D_a\Delta a+\rho a^2/h-\mu a+\sigma_a
$$

$$
h_t=D_h\Delta h+\rho_h a^2-\nu h
$$

短距離活性化・長距離抑制の簡略代表形。飽和項や基礎生成項には複数の変種があります。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#12-1972-gierermeinhardt-activatorinhibitor)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 流体・弾性構造と埋め込み境界

ID: `bio-immersed-boundary` · reading

$$
\rho(\boldsymbol u_t+\boldsymbol u\cdot\nabla\boldsymbol u)=-\nabla p+\mu\Delta\boldsymbol u+\boldsymbol f
$$

$$
\nabla\cdot\boldsymbol u=0
$$

$$
\boldsymbol X_t=\boldsymbol u(\boldsymbol X,t)
$$

流体と変形構造の結合の入口。構造の力・構成則が別途必要で、既存の非圧縮ソルバーだけで実装済みとはなりません。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#13-1972-fluidelastic-structure-and-immersed-boundaries)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 化学マスター方程式とGillespie SSA

ID: `bio-chemical-master` · reading

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#14-1977-chemical-master-equation-and-gillespie-ssa)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Mackey–Glass遅延生理フィードバック

ID: `bio-mackey-glass` · reading

$$
\dot x(t)=\frac{\beta x(t-\tau)}{1+x(t-\tau)^p}-\gamma x(t)
$$

遅延を持つフィードバックODE。初期値1点だけでなく、遅延区間の履歴関数が必要です。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#15-1977-mackeyglass-delayed-physiological-feedback)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### レプリケータ進化ゲーム動態

ID: `bio-replicator` · reading

$$
\dot x_i=x_i[(A\boldsymbol x)_i-\boldsymbol x^TA\boldsymbol x]
$$

$$
x_i\geq0
$$

$$
\sum_i x_i=1
$$

利得行列Aに対する戦略割合の動態。定常点と進化的安定戦略の同一視はしません。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#16-1978-replicator-evolutionary-game-dynamics)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Schnakenberg反応拡散

ID: `bio-schnakenberg` · local-example

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。

#### 関連するテスト問題の図とコード

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [実行・検証：Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`) · [コードZIP：Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

- [実行・検証：Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) (`schnakenberg-nonlinear`) · [コードZIP：Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

この実行例の範囲：t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

- [実行・検証：Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) (`schnakenberg-pattern`) · [コードZIP：Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

この実行例の範囲：t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。




### Shigesada–Kawasaki–Teramoto交差拡散

ID: `bio-skt` · reading

$$
u_t=\Delta[(d_1+\alpha_{11}u+\alpha_{12}v)u]+u(a_1-b_1u-c_1v)
$$

$$
v_t=\Delta[(d_2+\alpha_{21}u+\alpha_{22}v)v]+v(a_2-b_2u-c_2v)
$$

自己拡散・交差拡散と競争を含む系。表示は環境ポテンシャルを省いた一様環境での縮約形です。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#18-1979-shigesadakawasakiteramoto-cross-diffusion)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Gray–Scott空間自己触媒反応

ID: `bio-gray-scott` · reading

$$
u_t=D_u\Delta u-uv^2+F(1-u)
$$

$$
v_t=D_v\Delta v+uv^2-(F+k)v
$$

流入・除去を持つ自己触媒反応拡散。斑点分裂の画像だけで細胞分裂や線形Turing不安定性とは判定しません。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#19-1983-grayscott-spatial-autocatalysis)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Aliev–Panfilov心筋興奮

ID: `bio-cardiac` · reading

$$
u_t=D\Delta u-ku(u-a)(u-1)-uv
$$

$$
v_t=\left(\epsilon_0+\frac{\mu_1v}{u+\mu_2}\right)[-v-ku(u-b-1)]
$$

心筋波の興奮・回復を表す現象論的な2変数モデル。単・双領域の組織モデルは追加の構成を要します。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#20-1996-alievpanfilov-cardiac-excitation)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### Repressilator mRNA・タンパク質回路

ID: `bio-repressilator` · reading

$$
\dot m_i=\frac{\alpha}{1+p_{i-1}^n}+\alpha_0-m_i
$$

$$
\dot p_i=\beta(m_i-p_i)
$$

$$
i=1,2,3\ \text{cyclic}
$$

3遺伝子の環状抑制。mRNAとタンパク質を残す6変数形で、振動の有無はパラメータに依存します。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#21-2000-repressilator-mrnaprotein-network)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 遺伝子トグルスイッチ

ID: `bio-toggle` · reading

$$
\dot u=\frac{\alpha_1}{1+v^p}-u
$$

$$
\dot v=\frac{\alpha_2}{1+u^q}-v
$$

相互抑制による規格化した2変数遺伝子スイッチ。任意のHill指数・生成率で双安定になるとは限りません。 文献解説のみ。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#22-2000-genetic-toggle-switch)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 電子の定常Schrödinger方程式

ID: `stationary-schrodinger` · local-example

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子多体固有値問題。核間反発は電子Hamiltonianの外に加える。実行例は1電子の孤立水素型原子に限定。一般の多電子直接解法は未実装。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#schrodinger)

#### 関連するテスト問題の図とコード

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja)

- [実行・検証：水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`) · [コードZIP：水素型原子：解析解と格子収束](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。


##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [実行・検証：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

この実行例の範囲：孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。




### 閉殻Hartree–Fock方程式

ID: `hartree-fock-model` · local-example

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

閉殻RHFの占有空間軌道の式。一般に非局所な交換を含む。実行例は球対称1s² Heの局所還元に限定し、一般の分子・多電子のFock行列構築は未実装。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-fock)

#### 関連するテスト問題の図とコード

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [実行・検証：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。


##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [実行・検証：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

この実行例の範囲：孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。




### 局所Kohn–Sham DFT

ID: `kohn-sham-model` · local-example

$$
E[n]=T_s[n]+\int v_{\rm ext}n\,d\mathbf r+E_H[n]+E_{\rm xc}[n]+E_{NN}
$$

$$
[-\tfrac12\nabla^2+v_{\rm ext}+v_H+v_{\rm xc}]\phi_i=\varepsilon_i\phi_i
$$

$$
n(\mathbf r)=\sum_i f_i|\phi_i(\mathbf r)|^2,\quad \int n\,d\mathbf r=N,\quad v_{\rm xc}=\frac{\delta E_{\rm xc}}{\delta n}
$$

密度汎関数の局所KS代表形。実行例は球対称He・スピン非偏極Dirac交換のみLDA。相関・GGA・hybrid・一般化KS・周期系は未実装。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#kohn-sham-dft)

#### 関連するテスト問題の図とコード

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [実行・検証：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。


##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) (`periodic-he-dft`)

![固定Heセルの周期LDA：Γ点とkメッシュ、Gaussian軌道基底・FFT格子・SCFを分離。DFTK平面波参照の打切り収束と差も表示。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#code-ja)

- [実行・検証：周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja) (`periodic-he-dft`) · [コードZIP：周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

この実行例の範囲：固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。


##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

![非対称He₂の解析力をエネルギー有限差分とDFTK参照で比較。力のk点・基底・FFT・SCF収束とBOMDの局所接続確認。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

- [実行・検証：周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja) (`periodic-he-forces`) · [コードZIP：周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

この実行例の範囲：非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。




### 時間依存Kohn–Sham方程式

ID: `time-dependent-kohn-sham` · reading

$$
i\partial_t\phi_i(\mathbf r,t)=[-\tfrac12\nabla^2+v_s[n](\mathbf r,t)]\phi_i(\mathbf r,t)
$$

局所時間依存KSの代表形。初期状態、交換相関の記憶効果、断熱近似を区別する。実時間と線形応答の専用実装は未公開。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#tddft)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



## English

### Linear advection

ID: `linear-advection` · local-example

$$
\partial_t u+a\,\partial_xu=0
$$

Transport at constant speed a: translation, numerical diffusion and stability.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)

#### Related test problem figures and code

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [Run and validate: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.


##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Nonsymmetric advection-diffusion discrete manufactured system](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en) (`sparse-advection-diffusion`)

![Stored true-residual histories of the nonsymmetric discrete system.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#code-en)

This is a steady discrete advection-diffusion matrix. Linked entries explain its transport and diffusion components; neither alone represents the complete matrix problem.

No fixed-input execution example is registered.



### Heat / diffusion equation

ID: `heat` · local-example

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)

#### Related test problem figures and code

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Nonsymmetric advection-diffusion discrete manufactured system](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en) (`sparse-advection-diffusion`)

![Stored true-residual histories of the nonsymmetric discrete system.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#code-en)

This is a steady discrete advection-diffusion matrix. Linked entries explain its transport and diffusion components; neither alone represents the complete matrix problem.

No fixed-input execution example is registered.

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`)

![Stored linear periodic Fourier reaction–diffusion refinement separates continuum errors on 16/32/64 grids from temporal errors against a fixed-grid semidiscrete exact solution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#code-en)

Linear reaction-diffusion u_t=D u_xx+r u, with published D=0.1 and r=0.1. The heat link covers diffusion; compare using the eigenvalue r-Dk² including reaction.

- [Run and validate: Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`) · [Code ZIP: Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.




### Poisson / Laplace equations

ID: `poisson-laplace` · local-example

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)

#### Related test problem figures and code

##### [1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

![Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

- [Run and validate: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`) · [Code ZIP: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.


##### [1D Poisson / pure Neumann boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=en) (`poisson-1d-neumann`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-neumann.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=en#code-en)

No fixed-input execution example is registered.

##### [1D Poisson / mixed Dirichlet-Neumann boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=en) (`poisson-1d-mixed`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-mixed.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=en#code-en)

No fixed-input execution example is registered.

##### [1D Poisson / Robin manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=en) (`poisson-1d-robin`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=en#code-en)

No fixed-input execution example is registered.

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en) (`poisson-2d-broad`)

![Stored broad smooth forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#code-en)

No fixed-input execution example is registered.

##### [2D Poisson / localized source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en) (`poisson-2d-localized`)

![Stored localized forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#code-en)

No fixed-input execution example is registered.

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [Run and validate: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP: 2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

- [Run and validate: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en) (`sa-amg`) · [Code ZIP: Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Scope of this execution example: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.


##### [2D Poisson / uniform source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en) (`poisson-2d-uniform`)

![Stored multigrid residual history for uniform-source Poisson.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en#code-en)

No fixed-input execution example is registered.

##### [2D Poisson / random-source discrete residual](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en) (`poisson-2d-random`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#code-en)

No fixed-input execution example is registered.

##### [3D periodic Poisson / Fourier manufactured solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en) (`poisson-3d-periodic`)

![Three stored slices of a 3D periodic Poisson solution, not 3D fluid evolution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en#code-en)

No fixed-input execution example is registered.

##### [1D periodic Poisson / pseudo-time steady solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=en) (`poisson-1d-periodic`)

![Stored error refinement of the pseudo-time steady solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) (`periodic-particles`)

![Periodic-PM part of a shared figure; isolated-tree comparisons are a separate problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#code-en)

- [Run and validate: Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) (`periodic-particles`) · [Code ZIP: Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.


##### [Isolated FFT versus direct nonperiodic convolution](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=en) (`isolated-convolution`)

![Shared boundary-kernel figure; this card links specifically to isolated-convolution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=en#code-en)

A density-field convolution for the gravitational Poisson equation with isolated boundaries, distinct from softened particle-pair forces or fully periodic Poisson examples. This visual compares zero-padded FFT with nonperiodic direct convolution using the same discrete kernel.

No fixed-input execution example is registered.

##### [Uniform plane-slab gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en) (`uniform-slab`)

![Shared boundary-kernel figure; this card links specifically to uniform-slab.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en#code-en)

A gravitational Poisson problem periodic horizontally and isolated vertically, using the zero horizontal mode of a uniform slab. The right-hand side of the representative Poisson equation below is 4πGρ here; fully periodic boundaries and softened particle systems are different cases.

No fixed-input execution example is registered.

##### [Sinusoidal sheet gravity](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en) (`sinusoidal-sheet`)

![Shared boundary-kernel figure; this card links specifically to sinusoidal-sheet.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en#code-en)

A gravitational Poisson problem periodic horizontally and isolated vertically, combining nonzero and zero horizontal modes of a sheet density. The Poisson right-hand side is 4πGρ; this differs from fully periodic fields or softened particle-pair forces.

No fixed-input execution example is registered.

##### [Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

![Asymmetric eight-charge neutral cubic cell: saved force differences over Ewald real/reciprocal cutoffs. The same problem links to a smooth-PME mesh/B-spline-order supplement.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

The link is the electrostatic Poisson/Laplace field. This is neutral periodic Coulomb Ewald/PME, not an interchange of gravitational masses, signs or boundaries.

- [Run and validate: Neutral-cell Ewald sums and an independent theta integral](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en) (`ewald`) · [Code ZIP: Neutral-cell Ewald sums and an independent theta integral](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

- [Run and validate: Mesh/order convergence of B-spline smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en) (`spme`) · [Code ZIP: Mesh/order convergence of B-spline smooth PME](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.


##### [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

![Stored potential/field errors for 128 fixed-seed particles with a 2D free-space log kernel: FMM orders 2/4/8/12 versus a separate all-pairs sum.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

A particle sum with the logarithmic Green kernel of 2D Poisson/Laplace, distinct from softened 3D 1/r gravity.

- [Run and validate: 2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en) (`fmm`) · [Code ZIP: 2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.


##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

Poisson identifies the self-consistent electrostatic field; the registry does not list the complete coupled particle-motion/CIC PIC system.

- [Run and validate: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) (`pic`) · [Code ZIP: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.




### Inviscid Burgers equation

ID: `burgers` · local-example

$$
\partial_tu+\partial_x(u^2/2)=0
$$

A nonlinear scalar conservation law: compare shocks and rarefactions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/equation-gallery/)

#### Related test problem figures and code

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en) (`burgers-shock`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en) (`burgers-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#code-en)

No fixed-input execution example is registered.



### LWR traffic model

ID: `traffic` · local-example

$$
\partial_t\rho+\partial_x[\rho(1-\rho)]=0
$$

A representative nondimensional flux: upstream jams and clearing fans.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/equation-gallery/)

#### Related test problem figures and code

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en) (`traffic-jam`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en) (`traffic-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#code-en)

No fixed-input execution example is registered.



### Compressible Euler equations

ID: `euler` · local-example

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)

#### Related test problem figures and code

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

- [Run and validate: Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en) (`sod`) · [Code ZIP: Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.


##### [Lax shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=en) (`lax`)

![Shared figure, left: Lax shock tube. Right: a separate entropy-wave refinement study.](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

- [Run and validate: Shu–Osher: characteristic WENO-Z and a numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en) (`shu-osher`) · [Code ZIP: Shu–Osher: characteristic WENO-Z and a numerical reference](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.

- [Run and validate: Shu–Osher: independent reference and mesh refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en) (`shu-independent`) · [Code ZIP: Shu–Osher: independent reference and mesh refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Scope of this execution example: Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.


##### [One-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en) (`entropy-1d`)

![Stored density-error refinement for a 1D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Moving contact discontinuity](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en) (`moving-contact`)

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#code-en)

No fixed-input execution example is registered.

##### [One-dimensional strong pressure jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en) (`strong-shock`)

![Stored density from a completed PPM run, distinct from variants that stopped.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Stored final frame of 2D Double Mach reflection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/double-mach/frame-080.webp)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

No fixed-input execution example is registered.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Stored computed field for the Mach-3 forward-facing step.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/step-m3-mc.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en) (`entropy-2d`)

![Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Cylinder-forebody bow shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en) (`cylinder-forebody`)

![Stored finite-time forebody density comparison; not steady-state certification.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en) (`odd-even`)

![Stored odd–even diagnostic for a stationary planar shock.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

![Stored final frame of the KEEP moving vortex.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/keep-vortex/frame-080.webp)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

No fixed-input execution example is registered.



### Shallow-water equations

ID: `shallow-water` · local-example

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

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/geophysical-grids/)

#### Related test problem figures and code

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution example is registered.



### Isothermal flow equations

ID: `isothermal` · local-example

$$
\rho_t+(\rho u)_x=0
$$

$$
(\rho u)_t+(\rho u^2+c_s^2\rho)_x=0
$$

A one-dimensional form with constant isothermal sound speed cₛ. Follow the density-jump reference solution.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)

#### Related test problem figures and code

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

No fixed-input execution example is registered.



### Ideal magnetohydrodynamics

ID: `mhd` · local-example

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/)

#### Related test problem figures and code

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

- [Run and validate: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en) (`ct-glm-independent`) · [Code ZIP: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Scope of this execution example: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

- [Run and validate: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en) (`ct-glm-ot-convergence`) · [Code ZIP: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Scope of this execution example: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.


##### [Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) (`brio-wu`)

![Stored Brio–Wu shock-tube comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#code-en)

- [Run and validate: Brio–Wu: HLLD and a conservatively restricted numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en) (`brio-wu`) · [Code ZIP: Brio–Wu: HLLD and a conservatively restricted numerical reference](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.

- [Run and validate: Brio–Wu against an independent HLLD implementation](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en) (`brio-independent`) · [Code ZIP: Brio–Wu against an independent HLLD implementation](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Scope of this execution example: Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.


##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

![Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

No fixed-input execution example is registered.

##### [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) (`advected-magnetostatic-equilibrium`)

![Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#code-en)

Planar ideal MHD on a periodic unit square with gamma=5/3 and mu0=1. The exact solution translates a constructed magnetostatic equilibrium at constant velocity; it is neither a forced manufactured solution nor the standard circularly polarized Alfvén wave. The execution example supplies the GLM auxiliary equation and explicit conserved cell averages.

- [Run and validate: CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en) (`ct-glm-smooth-convergence`) · [Code ZIP: CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Scope of this execution example: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.




### Incompressible Navier–Stokes

ID: `navier-stokes` · local-example

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

A representative constant-density, constant-viscosity form. Public examples use periodic 2D MAC projection and a Taylor–Green vortex.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/)

#### Related test problem figures and code

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

- [Run and validate: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.


##### [Viscous decay of a periodic shear wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en) (`lbm-shear`)

![Stored shear amplitudes and viscous-decay reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#code-en)

Lattice BGK is the computed model; incompressible Navier–Stokes supplies the low-Mach macroscopic decay comparison.

No fixed-input execution example is registered.

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en) (`channel-poiseuille`)

![Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en)

Links the lattice-BGK/body-force/halfway-wall calculation to its macroscopic steady incompressible channel solution.

No fixed-input execution example is registered.



### Isothermal lattice BGK

ID: `bgk` · local-example

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/)

#### Related test problem figures and code

##### [Viscous decay of a periodic shear wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en) (`lbm-shear`)

![Stored shear amplitudes and viscous-decay reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#code-en)

Lattice BGK is the computed model; incompressible Navier–Stokes supplies the low-Mach macroscopic decay comparison.

No fixed-input execution example is registered.

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en) (`channel-poiseuille`)

![Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en)

Links the lattice-BGK/body-force/halfway-wall calculation to its macroscopic steady incompressible channel solution.

No fixed-input execution example is registered.



### Hamiltonian systems and oscillators

ID: `hamiltonian` · local-example

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)

#### Related test problem figures and code

##### [Harmonic oscillator, including complex-ODE form](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en) (`harmonic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#code-en)

- [Run and validate: Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en) (`harmonic-oscillator`) · [Code ZIP: Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.


##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en) (`quartic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

![Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

The Hamiltonian link identifies the harmonic mechanical part; the calculations add friction/noise or a CSVR heat bath.

- [Run and validate: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en) (`langevin-harmonic`) · [Code ZIP: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

- [Run and validate: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en) (`csvr-langevin-harmonic`) · [Code ZIP: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.


##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

![Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

The Hamiltonian link identifies the anharmonic mechanical part; validation concerns distributions with added stochastic CSVR/Langevin heat baths.

- [Run and validate: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en) (`csvr-langevin-quartic`) · [Code ZIP: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.




### Gravitational particle model

ID: `particle-gravity` · local-example

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)

#### Related test problem figures and code

##### [3D periodic Poisson / Fourier manufactured solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en) (`poisson-3d-periodic`)

![Three stored slices of a 3D periodic Poisson solution, not 3D fluid evolution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Isolated softened particle gravity: tree versus direct sum](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en) (`isolated-particles`)

![Stored relative tree/direct-sum force errors versus opening angle and expansion order.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en#code-en)

- [Run and validate: Barnes–Hut: 192 particles against direct summation](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en) (`barnes-hut`) · [Code ZIP: Barnes–Hut: 192 particles against direct summation](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Scope of this execution example: Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.


##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) (`periodic-particles`)

![Periodic-PM part of a shared figure; isolated-tree comparisons are a separate problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#code-en)

- [Run and validate: Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) (`periodic-particles`) · [Code ZIP: Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.




### Bratu nonlinear boundary-value problem

ID: `bratu` · local-example

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)

#### Related test problem figures and code

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

- [Run and validate: 1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en) (`bratu`) · [Code ZIP: 1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.




### Auxiliary hyperbolic diffusion system

ID: `hyperbolic-diffusion` · local-example

$$
\partial_\tau u-\nu\partial_xp=f
$$

$$
\partial_\tau p-T_r^{-1}\partial_xu=-p/T_r
$$

τ is pseudo-time and Tr a relaxation time. At steady state p=uₓ and −νuₓₓ=f are recovered; this is distinct from physical-time heat diffusion.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/hyperbolic-diffusion/)

#### Related test problem figures and code

##### [1D periodic Poisson / pseudo-time steady solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=en) (`poisson-1d-periodic`)

![Stored error refinement of the pseudo-time steady solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=en#code-en)

No fixed-input execution example is registered.



### Special-relativistic hydrodynamics (SRHD)

ID: `srhd` · reading

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

Representative ideal fluid in flat Cartesian spacetime, c=1. An equation of state and primitive recovery are required. Atlas coverage is literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#what-changes-from-the-existing-euler-examples)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### General-relativistic hydrodynamics (GRHD)

ID: `grhd` · reading

$$
\nabla_\mu(\rho_0u^\mu)=0,\qquad\nabla_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p g^{\mu\nu}
$$

Ideal fluid with c=G=1 and signature (−,+,+,+). Distinguish prescribed geometry from an evolved Einstein system. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#19721998-from-curved-background-flows-to-conservative-hrsc)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### General-relativistic MHD (GRMHD)

ID: `grmhd` · reading

$$
\nabla_\mu(\rho_0u^\mu)=0
$$

$$
\nabla_\mu(T_{\rm fluid}^{\mu\nu}+T_{\rm EM}^{\mu\nu})=0
$$

$$
\nabla_\mu{}^*F^{\mu\nu}=0,\qquad F^{\mu\nu}u_\nu=0
$$

Representative ideal-conductivity form combining matter/EM stress-energy, magnetic constraints and geometry. Consult the chapter for closure and spacetime choices. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#19992006-magnetic-constraints-and-dynamical-spacetime)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Relativistic radiation moments / M1

ID: `m1-radiation` · reading

$$
\nabla_\mu T^{\mu\nu}=G^\nu,\qquad\nabla_\mu R^{\mu\nu}=-G^\nu
$$

$$
P^{ij}=D_{\rm M1}^{ij}(E,\boldsymbol F)\,E
$$

Schematic moment system defining Gν as the four-force received by matter. R is radiation stress-energy and P the radiation-pressure tensor. M1 closes angular moments rather than exactly resolving the full distribution. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#2013-onward-radiation-and-microphysics-add-stiff-systems)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Causal relativistic viscous fluid

ID: `causal-viscous` · reading

$$
\nabla_\mu T^{\mu\nu}=0,\qquad T^{\mu\nu}=T_{\rm ideal}^{\mu\nu}+\Pi\Delta^{\mu\nu}+\pi^{\mu\nu}
$$

$$
\tau_\pi D\pi^{\langle\mu\nu\rangle}+\pi^{\mu\nu}=\pi_{\rm NS}^{\mu\nu}+\cdots
$$

The second line only sketches Israel–Stewart-type relaxation; it is not a complete constitutive law. Distinguish first-order approaches such as BDNK without extra relaxation variables. Causality depends on the theory and equation of state. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#a-parallel-19792019-branch-causal-viscous-fluid-theory)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Logistic population growth

ID: `bio-logistic` · local-example

$$
\dot N=rN(1-N/K)
$$

Density-limited growth with carrying capacity K. It is the simplest biological ODE baseline. The linked original is the later 1847 memoir; the 1838 note itself was not audited. The differential equation is not the discrete logistic map. Scoped executed example: One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#01-1838-logistic-population-growth)

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

#### Related test problem figures and code

##### [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en) (`logistic-growth`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#code-en)

- [Run and validate: Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en) (`logistic-growth`) · [Code ZIP: Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Scope of this execution example: One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.




### Michaelis–Menten and full enzyme kinetics

ID: `bio-enzyme` · reading

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#02-1913-michaelismenten-and-full-enzyme-kinetics)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Lotka–Volterra predator–prey

ID: `bio-lotka-volterra` · reading

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

Coupled prey growth and predation; a phase-plane and long-time integration test.  Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#03-1920-lotkavolterra-predatorprey)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### McKendrick age-structured population

ID: `bio-age-structure` · reading

$$
\partial_t n+\partial_a n=-\mu(a)n
$$

$$
n(0,t)=\int_0^\infty b(a)n(a,t)\,da
$$

Individuals move through age a at unit speed; newborns enter through a nonlocal renewal boundary. This is the classical age-transport form; the later von Foerster lineage is acknowledged without treating its date as the first appearance. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#04-1926-mckendrick-age-structured-population)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### SIR and SEIR compartment models

ID: `bio-sir` · local-example

$$
\dot s=-\beta si
$$

$$
\dot i=\beta si-\gamma i
$$

$$
\dot r=\gamma i
$$

$$
s+i+r=1
$$

Closed, well-mixed normalized population fractions. SEIR adds an exposed compartment and a progression rate. The original general epidemic framework is broader than this SIR specialization. Population-count and fraction conventions give different β definitions. Scoped executed example: Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#05-1927-sir-and-seir-compartment-models)

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

#### Related test problem figures and code

##### [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en) (`sir-epidemic`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#code-en)

- [Run and validate: SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en) (`sir-epidemic`) · [Code ZIP: SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Scope of this execution example: Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.




### Fisher–KPP invasion front

ID: `bio-fisher-kpp` · reading

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#06-1937-fisherkpp-invasion-front)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Monod growth and chemostat

ID: `bio-monod` · reading

$$
\mu(S)=\mu_{\max}\frac{S}{K_S+S}
$$

$$
\dot X=(\mu(S)-d)X
$$

$$
\dot S=d(S_{in}-S)-\mu(S)X/Y
$$

Nutrient-limited biomass X, substrate S, yield Y and chemostat dilution d; d=0 gives a closed batch model. This writes one constant-yield extension of saturation growth, not a universal metabolic model. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#07-1949-monod-growth-and-chemostat)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Hodgkin–Huxley membrane dynamics

ID: `bio-hodgkin-huxley` · reading

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#08-1952-hodgkinhuxley-membrane-dynamics)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Turing reaction–diffusion framework

ID: `bio-turing` · local-example

$$
u_t=D_u\Delta u+f(u,v)
$$

$$
v_t=D_v\Delta v+g(u,v)
$$

A framework for diffusion-driven pattern onset around a homogeneous reaction equilibrium, not a unique choice of f and g. A spot image or unequal diffusion coefficients alone do not establish a Turing mechanism. Boundary conditions determine the available modes. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#09-1952-turing-reactiondiffusion-framework)

A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.

#### Related test problem figures and code

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Run and validate: Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) (`turing-schnakenberg`) · [Code ZIP: Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

- [Run and validate: Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) (`schnakenberg-nonlinear`) · [Code ZIP: Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Scope of this execution example: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

- [Run and validate: Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) (`schnakenberg-pattern`) · [Code ZIP: Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Scope of this execution example: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.




### FitzHugh–Nagumo excitation and recovery

ID: `bio-fitzhugh-nagumo` · local-example

$$
v_t=D\Delta v+v-v^3/3-w+I
$$

$$
w_t=\epsilon(v+a-bw)
$$

A normalized fast excitation/slow recovery model for pulses, refractoriness and spiral waves when extended in space. This is a common normalized variant; cubic coefficients, recovery signs and nondimensionalization differ between formulations. Scoped executed example: The executed case has D=0 and no spatial coordinate. Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#10-1961-fitzhughnagumo-excitation-and-recovery)

Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

#### Related test problem figures and code

##### [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`)

![A dimensionless two-variable FHN-type ODE with a t=10..20 current pulse: stored RK4/DOP853 excitation and recovery, steps 0.1/0.05/0.025 and all-output-time differences.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#code-en)

The published fixed input is the two-variable ODE limit without spatial diffusion; it does not validate the general propagation PDE.

- [Run and validate: FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`) · [Code ZIP: FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.




### Keller–Segel chemotaxis

ID: `bio-keller-segel` · reading

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#11-1970-kellersegel-chemotaxis)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Gierer–Meinhardt activator–inhibitor

ID: `bio-gierer-meinhardt` · reading

$$
a_t=D_a\Delta a+\rho a^2/h-\mu a+\sigma_a
$$

$$
h_t=D_h\Delta h+\rho_h a^2-\nu h
$$

A representative simplified short-range activation/long-range inhibition model. Source densities, saturation and baseline production vary across the model family. This simplified formula is not a verbatim transcription of every original variant. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#12-1972-gierermeinhardt-activatorinhibitor)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Fluid–elastic structure and immersed boundaries

ID: `bio-immersed-boundary` · reading

$$
\rho(\boldsymbol u_t+\boldsymbol u\cdot\nabla\boldsymbol u)=-\nabla p+\mu\Delta\boldsymbol u+\boldsymbol f
$$

$$
\nabla\cdot\boldsymbol u=0
$$

$$
\boldsymbol X_t=\boldsymbol u(\boldsymbol X,t)
$$

Fluid coupled to a deformable structure; biological examples include valves and membranes, once a force/constitutive law is supplied. Immersed boundary is a numerical coupling method, not itself a closed biological constitutive equation. The existing periodic MAC solver does not implement this coupling. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#13-1972-fluidelastic-structure-and-immersed-boundaries)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Chemical master equation and Gillespie SSA

ID: `bio-chemical-master` · reading

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#14-1977-chemical-master-equation-and-gillespie-ssa)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Mackey–Glass delayed physiological feedback

ID: `bio-mackey-glass` · reading

$$
\dot x(t)=\frac{\beta x(t-\tau)}{1+x(t-\tau)^p}-\gamma x(t)
$$

Delayed feedback in a normalized physiological control model; delay can change stability and oscillatory behavior. A scalar initial value alone is insufficient. The delayed ODE is distinct from a spatial reaction–diffusion model. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#15-1977-mackeyglass-delayed-physiological-feedback)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Replicator evolutionary game dynamics

ID: `bio-replicator` · reading

$$
\dot x_i=x_i[(A\boldsymbol x)_i-\boldsymbol x^TA\boldsymbol x]
$$

$$
x_i\geq0
$$

$$
\sum_i x_i=1
$$

Strategy fractions reproduce according to relative payoff in a specified matrix game. No universal Lyapunov function or equivalence of fixed point and evolutionarily stable strategy is assumed. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#16-1978-replicator-evolutionary-game-dynamics)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Schnakenberg reaction–diffusion

ID: `bio-schnakenberg` · local-example

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.

#### Related test problem figures and code

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Run and validate: Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) (`turing-schnakenberg`) · [Code ZIP: Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

- [Run and validate: Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) (`schnakenberg-nonlinear`) · [Code ZIP: Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Scope of this execution example: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

- [Run and validate: Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) (`schnakenberg-pattern`) · [Code ZIP: Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Scope of this execution example: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.




### Shigesada–Kawasaki–Teramoto cross-diffusion

ID: `bio-skt` · reading

$$
u_t=\Delta[(d_1+\alpha_{11}u+\alpha_{12}v)u]+u(a_1-b_1u-c_1v)
$$

$$
v_t=\Delta[(d_2+\alpha_{21}u+\alpha_{22}v)v]+v(a_2-b_2u-c_2v)
$$

Competition with density-dependent self- and cross-dispersal can produce spatial segregation. The displayed homogeneous-environment reduction omits the original environmental-potential terms. It is not equivalent to two independent scalar diffusion equations. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#18-1979-shigesadakawasakiteramoto-cross-diffusion)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Gray–Scott spatial autocatalysis

ID: `bio-gray-scott` · reading

$$
u_t=D_u\Delta u-uv^2+F(1-u)
$$

$$
v_t=D_v\Delta v+uv^2-(F+k)v
$$

A chemical feed/decay model whose spatial extension supports diverse spot and wave patterns. 1983 is the well-mixed CSTR source; Pearson 1993 is the spatial pattern reference. Spot division does not by itself demonstrate cell division or a linear Turing instability. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#19-1983-grayscott-spatial-autocatalysis)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Aliev–Panfilov cardiac excitation

ID: `bio-cardiac` · reading

$$
u_t=D\Delta u-ku(u-a)(u-1)-uv
$$

$$
v_t=\left(\epsilon_0+\frac{\mu_1v}{u+\mu_2}\right)[-v-ku(u-b-1)]
$$

A reduced phenomenological excitation/recovery model for cardiac waves and restitution. Monodomain/bidomain tissue models add conductivity tensors and, for bidomain, an extracellular elliptic constraint. They are not automatically included by this two-variable model. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#20-1996-alievpanfilov-cardiac-excitation)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Repressilator mRNA–protein network

ID: `bio-repressilator` · reading

$$
\dot m_i=\frac{\alpha}{1+p_{i-1}^n}+\alpha_0-m_i
$$

$$
\dot p_i=\beta(m_i-p_i)
$$

$$
i=1,2,3\ \text{cyclic}
$$

Three repressing genes form a cyclic network; retaining mRNA and protein gives six state variables. The six-variable form is distinct from a reduced three-protein oscillator; oscillations are parameter-dependent. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#21-2000-repressilator-mrnaprotein-network)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Genetic toggle switch

ID: `bio-toggle` · reading

$$
\dot u=\frac{\alpha_1}{1+v^p}-u
$$

$$
\dot v=\frac{\alpha_2}{1+u^q}-v
$$

Mutual repression produces a possible bistable genetic switch in a normalized model. Bistability is not guaranteed for arbitrary Hill exponents or production rates. Induction, mRNA dynamics and noise are additional model choices. Literature-only.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#22-2000-genetic-toggle-switch)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Stationary electronic Schrödinger equation

ID: `stationary-schrodinger` · local-example

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#schrodinger)

#### Related test problem figures and code

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en)

- [Run and validate: Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`) · [Code ZIP: Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.


##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Run and validate: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Scope of this execution example: Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.




### Closed-shell Hartree–Fock equations

ID: `hartree-fock-model` · local-example

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

Closed-shell RHF spatial-orbital equations, generally with nonlocal exchange. Runnable code is restricted to the spherical 1s² helium local reduction; general molecular/many-electron Fock-matrix construction is not implemented.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-fock)

#### Related test problem figures and code

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Run and validate: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.


##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Run and validate: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Scope of this execution example: Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.




### Local Kohn–Sham DFT

ID: `kohn-sham-model` · local-example

$$
E[n]=T_s[n]+\int v_{\rm ext}n\,d\mathbf r+E_H[n]+E_{\rm xc}[n]+E_{NN}
$$

$$
[-\tfrac12\nabla^2+v_{\rm ext}+v_H+v_{\rm xc}]\phi_i=\varepsilon_i\phi_i
$$

$$
n(\mathbf r)=\sum_i f_i|\phi_i(\mathbf r)|^2,\quad \int n\,d\mathbf r=N,\quad v_{\rm xc}=\frac{\delta E_{\rm xc}}{\delta n}
$$

Representative local KS equations. Runnable code covers spherical-helium spin-unpolarized Dirac exchange-only LDA. Correlation, GGA, hybrids, generalized KS and periodic systems are not implemented.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#kohn-sham-dft)

#### Related test problem figures and code

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Run and validate: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.


##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) (`periodic-he-dft`)

![Periodic LDA for fixed He: separate Gamma/k sampling, Gaussian orbital basis, FFT grid and SCF. Includes independently converged DFTK plane-wave reference differences.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#code-en)

- [Run and validate: Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en) (`periodic-he-dft`) · [Code ZIP: Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

Scope of this execution example: Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.


##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

![Asymmetric-He₂ analytic forces versus energy finite differences and DFTK reference. Force k-point, basis, FFT and SCF refinement, plus a local BOMD interface check.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

- [Run and validate: Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en) (`periodic-he-forces`) · [Code ZIP: Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

Scope of this execution example: Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.




### Time-dependent Kohn–Sham equations

ID: `time-dependent-kohn-sham` · reading

$$
i\partial_t\phi_i(\mathbf r,t)=[-\tfrac12\nabla^2+v_s[n](\mathbf r,t)]\phi_i(\mathbf r,t)
$$

Representative local time-dependent KS equations. Distinguish initial-state dependence, exchange-correlation memory and adiabatic approximations. No dedicated real-time or response implementation is published.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#tddft)

#### Related test problem figures and code

No associated test problem is registered for this entry.
