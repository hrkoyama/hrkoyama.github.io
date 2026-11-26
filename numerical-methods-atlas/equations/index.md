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

既存の共通移流例を保持し、追加の有限体積WENO比較ではq₀=cos(2πx)+.1sin³(2πx)、[0,1]周期・速度1・T=1を使います。局所臨界多項式は別診断で、点値とセル平均や時間刻み誤差を区別します。

#### 関連するテスト問題の図とコード

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [実行・検証：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja) (`advection-sine`) · [コードZIP：周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

- [実行・検証：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP：WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

この実行例の範囲：同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

- [実行・検証：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) (`fr-periodic-advection`) · [コードZIP：FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。


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

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

- [実行・検証：小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja) (`fno-periodic-heat`) · [コードZIP：小型FNOの問題単位検証](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

この実行例の範囲：同じ重みで32/64点・未見関数・OODを分けて評価します。


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


##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

主検証は1997型の輻射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。

- [実行・検証：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`) · [コードZIP：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

この実行例の範囲：物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。


##### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`)

![時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#code-ja)

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。

- [実行・検証：時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`) · [コードZIP：時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

この実行例の範囲：後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。


##### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`)

![実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#code-ja)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

- [実行・検証：Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`) · [コードZIP：Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。




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

追加例はL字特異解と同じ自由度のgraded三角形、warped正方形、および純Neumannの適合条件・平均ゲージと混合Robin境界。旧Poisson例を保持し、残差と連続誤差を区別します。

#### 関連するテスト問題の図とコード

##### [1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

![保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

- [実行・検証：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`) · [コードZIP：1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。

- [実行・検証：1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja) (`pinn-poisson`) · [コードZIP：1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

この実行例の範囲：3固定seedの49パラメータPINNを解析解・FDと比較します。


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

- [実行・検証：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP：スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

この実行例の範囲：単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。


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

- [実行・検証：Ewald：非対称周期セルのエネルギー・力と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja) (`ewald-convergence`) · [コードZIP：Ewald：非対称周期セルのエネルギー・力と独立theta積分](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

- [実行・検証：SPME：格子・補間次数・格子位相と保存則](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja) (`spme-convergence`) · [コードZIP：SPME：格子・補間次数・格子位相と保存則](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。


##### [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) (`logarithmic-particles`)

![固定seedの128粒子、2次元自由空間の対数核。FMMの展開次数2/4/8/12を独立した全対直接和と比べたポテンシャル・電場誤差の保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#code-ja)

2次元Poisson/Laplaceの対数Green核を用いる粒子和です。3次元軟化重力1/rモデルとは区別します。

- [実行・検証：2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja) (`fmm`) · [コードZIP：2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

- [実行・検証：FMM：直接和・解析配置と展開次数・木の深さ](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja) (`fmm-convergence`) · [コードZIP：FMM：直接和・解析配置と展開次数・木の深さ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。


##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

Poissonへのリンクは自己無撞着な静電場の部分です。粒子の運動・CIC補間を結合したPIC全体の式が一覧に揃っているわけではありません。

- [実行・検証：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) (`pic`) · [コードZIP：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

- [実行・検証：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja) (`pic-conservation`) · [コードZIP：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

- [実行・検証：PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) (`pic-independent-spatial`) · [コードZIP：PIC空間演算の独立実装照合](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

この実行例の範囲：ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。


##### [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) (`lshape-fem`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#code-ja)

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。

- [実行・検証：L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja) (`lshape-fem`) · [コードZIP：L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。


##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。

- [実行・検証：純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) (`poisson-neumann`) · [コードZIP：純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。


##### [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。

- [実行・検証：2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja) (`poisson-robin`) · [コードZIP：2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。




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

- [実行・検証：Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja) (`gsph-sod`) · [コードZIP：Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

この実行例の範囲：Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。


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

- [実行・検証：Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) (`euler-double-rarefaction-positivity`) · [コードZIP：Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

この実行例の範囲：既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。


##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

同じMach10設定・γ=1.4の圧縮性Euler系を、長方形[0,4]×[0,1]の全域で更新します。

- [実行・検証：Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja) (`double-mach-reflection`) · [コードZIP：Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

この実行例の範囲：既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。


##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

γ=1.4、ρ=1.4、u=3、v=0、p=1の流入を、[0,3]×[0,1]から高さ.2・開始位置x=.6の段差を除いた2次元Euler系でT=4まで更新します。

- [実行・検証：Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja) (`forward-step-m3`) · [コードZIP：Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

この実行例の範囲：実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。


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

![M∞=.01、64²、T=.1の実際の2次元Euler計算。全\[-10,10\]²領域から中心\[-3,3\]²を拡大し、保存速度から差分で求めた渦度と背景流を引いた速度矢印で、MUSCL付き通常Roe／前処理Roeを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

- [実行・検証：低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja) (`low-mach-vortex`) · [コードZIP：低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

この実行例の範囲：同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。


##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![実際の2次元Cartesian Euler計算の密度場。正方形全域128²セル、初期圧力ゼロ、γ=5/3、t=.6。白破線は厳密衝撃円。軸・対角方向の差と原点過熱を残し、1D半径例にも辿れます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

1D平面・円筒・球の半径対称Euler系と、実際の2D Cartesian Euler系。2D版には幾何源・半径還元・対称境界がなく、全4辺の冷たい流入を与えます。

- [実行・検証：Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP：Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

この実行例の範囲：初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

- [実行・検証：Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) (`noh-cartesian-2d`) · [コードZIP：Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

この実行例の範囲：正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。


##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

![1次元球対称Eulerの保存済み半径密度を中心断面に表示。γ=5/3、E=ρ0=1、p0=0、t=.05、512球殻、有限投入半径.03。半解析的な点源参照との違いと衝撃層の誤差を残した図で、実2D Cartesian計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

無次元の球半径対称Euler系。1D半径方向の密度・運動量・全エネルギーを体積重み付きで発展させます。

- [実行・検証：Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) (`sedov-blast`) · [コードZIP：Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

この実行例の範囲：球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。


##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

![1次元球対称Eulerの保存済み半径密度を子午面に表示。γ=1.4、512球殻、r∈\[0,.75\]、R_s(−1)=.6、t=−.85。圧力ゼロの静止上流へ進む収束前の衝撃波を半解析参照と比較します。2D Cartesianや原点反射後の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

理想気体Eulerの球半径対称系。球殻体積を重みとして密度・半径運動量・全エネルギーを発展させ、半径運動量の幾何源を分けて積算します。

- [実行・検証：Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) (`guderley-implosion`) · [コードZIP：Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

この実行例の範囲：冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。


##### [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`)

![2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#code-ja)

- [実行・検証：Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`) · [コードZIP：Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

この実行例の範囲：2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。


##### [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`)

![規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#code-ja)

- [実行・検証：一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`) · [コードZIP：一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

この実行例の範囲：規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。




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

既存の湿潤1次元例と線形回転Fourier検査を保持します。追加Ritter例は平坦床・g9.81、[-10,10]、hL1/hR0、t.5の真の乾燥床です。地形源項付きの静止湖・Bernoulli流は別モデルshallow-water-bedへ案内します。

#### 関連するテスト問題の図とコード

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

固定入力実行例は未登録です。

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、800/1600/3200セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。

- [実行・検証：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`) · [コードZIP：乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。




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

従来のMHD例を保持。追加は全8量の1D整列円偏波と、実際の2D磁場ループ・衝撃波形成後Orszag–Tang。後二者の独立Athena参照は有限格子数値解であり、厳密解や任意問題の検証とはしません。

#### 関連するテスト問題の図とコード

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

- [実行・検証：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja) (`ct-glm-independent`) · [コードZIP：Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

この実行例の範囲：同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

- [実行・検証：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja) (`ct-glm-ot-convergence`) · [コードZIP：Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

この実行例の範囲：同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

- [実行・検証：後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) (`postshock-orszag-tang`) · [コードZIP：後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。


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

- [実行・検証：円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) (`circular-alfven-refinement`) · [コードZIP：円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。


##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

- [実行・検証：磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) (`magnetic-loop-independent`) · [コードZIP：磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

この実行例の範囲：実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。


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

一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)

既存の周期2D MAC射影・Taylor–Green例を保持し、追加の非周期Re100キャビティでは渦度・流れ関数法とThom壁条件を使います。速度中心線をGhia有限格子数値表と比較します。圧力を消去しているため、キャビティ圧力・圧力境界・MAC射影の追加検証とは表示しません。

#### 関連するテスト問題の図とコード

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

- [実行・検証：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

- [実行・検証：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) (`lbm-taylor-green`) · [コードZIP：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

この実行例の範囲：周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。


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

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

- [実行・検証：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) (`cavity-ghia-re100`) · [コードZIP：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

- [実行・検証：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) (`lbm-cavity-re100`) · [コードZIP：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

この実行例の範囲：4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。


##### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

- [実行・検証：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`) · [コードZIP：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

この実行例の範囲：実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。


##### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

- [実行・検証：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`) · [コードZIP：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

この実行例の範囲：標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。




### 等温格子BGK

ID: `bgk` · local-example

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/)

#### 関連するテスト問題の図とコード

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

- [実行・検証：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja) (`taylor-green`) · [コードZIP：周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

この実行例の範囲：既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

- [実行・検証：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) (`lbm-taylor-green`) · [コードZIP：LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

この実行例の範囲：周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。


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

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

- [実行・検証：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) (`cavity-ghia-re100`) · [コードZIP：Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

- [実行・検証：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) (`lbm-cavity-re100`) · [コードZIP：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

この実行例の範囲：4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。


##### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

- [実行・検証：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`) · [コードZIP：曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

この実行例の範囲：実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。


##### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

- [実行・検証：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`) · [コードZIP：LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

この実行例の範囲：標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。




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

- [実行・検証：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja) (`ou-weak-moments`) · [コードZIP：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。


##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

![弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

Hamilton系へのリンクは非調和ポテンシャルの力学部分です。確率温度浴を加えたCSVR・Langevinの分布検証を行います。

- [実行・検証：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja) (`csvr-langevin-quartic`) · [コードZIP：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

- [実行・検証：NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja) (`deterministic-thermostat-contrasts`) · [コードZIP：NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

この実行例の範囲：同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。


##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [実行・検証：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) (`gravity-kepler`) · [コードZIP：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

- [実行・検証：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja) (`kepler-eccentricity`) · [コードZIP：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。


##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

- [実行・検証：振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) (`high-index-pendulum`) · [コードZIP：振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

この実行例の範囲：位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

- [実行・検証：SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja) (`shake-rattle-pendulum`) · [コードZIP：SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。


##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

- [実行・検証：結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`) · [コードZIP：結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。




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


##### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#code-ja)

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。

- [実行・検証：真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`) · [コードZIP：真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

この実行例の範囲：非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。


##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [実行・検証：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) (`gravity-kepler`) · [コードZIP：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

- [実行・検証：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja) (`kepler-eccentricity`) · [コードZIP：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。


##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。

- [実行・検証：冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`) · [コードZIP：冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。




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


##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。

- [実行・検証：擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`) · [コードZIP：擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

この実行例の範囲：同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。


##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。

- [実行・検証：解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`) · [コードZIP：解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

この実行例の範囲：非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。


##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`)

![同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`) · [コードZIP：同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

この実行例の範囲：同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。


##### [独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja) (`reverse-vjp-duality`)

![独立矩形Jacobianと実際の逆微分誤差、固定wide写像の実測sweep数。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja) (`reverse-vjp-duality`) · [コードZIP：独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

この実行例の範囲：重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。


##### [HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja) (`hessian-vector-products`)

![保存HVPと独立参照、状態固定と陰関数全微分の二階曲率を区別した比較。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja) (`hessian-vector-products`) · [コードZIP：HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

この実行例の範囲：forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。


##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。

- [実行・検証：離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`) · [コードZIP：離散fold近傍のBratu感度](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

この実行例の範囲：離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。


##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。

- [実行・検証：分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`) · [コードZIP：分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

この実行例の範囲：2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。


##### [GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`)

![保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#code-ja)

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。

- [実行・検証：GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`) · [コードZIP：GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

この実行例の範囲：同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。


##### [雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`)

![保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#code-ja)

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。

- [実行・検証：雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`) · [コードZIP：雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

この実行例の範囲：2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。




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

ID: `srhd` · local-example

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

c=1、平坦なCartesian時空の理想流体。γ則EOSと原始変数回復を使う穏やかな対称二衝撃波の固定例を追加。一般三波Riemann解、極端なLorentz因子、一般相対論を検証したとはしません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/#what-changes-from-the-existing-euler-examples)

ρ1,p.1,v±.3,γ5/3、96/192/384セル、T.3、境界外挿。独立Taub解、圧力根SRHD回復/流束、保存量の境界収支と全段物理性を照合します。

#### 関連するテスト問題の図とコード

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。

- [実行・検証：SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) (`srhd-collision`) · [コードZIP：SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

この実行例の範囲：相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。




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



### 相対論的輻射モーメント・M1

ID: `m1-radiation` · reading

$$
\nabla_\mu T^{\mu\nu}=G^\nu,\qquad\nabla_\mu R^{\mu\nu}=-G^\nu
$$

$$
P^{ij}=D_{\rm M1}^{ij}(E,\boldsymbol F)\,E
$$

Gνを物質が受け取る四元力と定義した模式形。Rは輻射の応力エネルギー、Pは輻射圧テンソル。M1は角度モーメントの閉包で、輻射分布全体を厳密に解くものではありません。文献解説のみ。

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

ID: `bio-enzyme` · local-example

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 限定した実行例：2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#02-1913-michaelismenten-and-full-enzyme-kinetics)

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

#### 関連するテスト問題の図とコード

##### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) (`enzyme-qssa`)

![全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#code-ja)

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

- [実行・検証：酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja) (`enzyme-qssa`) · [コードZIP：酵素反応の保存と準定常近似](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

この実行例の範囲：全4状態と準定常近似を比較し、初期層と積分誤差を分けます。




### Lotka–Volterra捕食・被食

ID: `bio-lotka-volterra` · local-example

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 限定した実行例：1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#03-1920-lotkavolterra-predatorprey)

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

#### 関連するテスト問題の図とコード

##### [Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja) (`lotka-volterra`)

![正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja#code-ja)

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

- [実行・検証：Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja) (`lotka-volterra`) · [コードZIP：Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

この実行例の範囲：正の軌道を独立な対数座標参照と比較します。




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

ID: `bio-fisher-kpp` · local-example

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#06-1937-fisherkpp-invasion-front)

全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線

#### 関連するテスト問題の図とコード

##### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`)

![波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#code-ja)

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。

- [実行・検証：Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`) · [コードZIP：Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

この実行例の範囲：波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。




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

ID: `bio-hodgkin-huxley` · local-example

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#08-1952-hodgkinhuxley-membrane-dynamics)

全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火

#### 関連するテスト問題の図とコード

##### [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja) (`hodgkin-huxley-controls`)

![固定電位の解析ゲート解と、区分電流下の4状態系を照合します。 1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#code-ja)

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。

- [実行・検証：Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja) (`hodgkin-huxley-controls`) · [コードZIP：Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

この実行例の範囲：固定電位の解析ゲート解と、区分電流下の4状態系を照合します。




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

- [実行・検証：同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) (`reaction-diffusion-splitting`) · [コードZIP：同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

この実行例の範囲：32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。




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

ID: `bio-keller-segel` · local-example

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#11-1970-kellersegel-chemotaxis)

全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解

#### 関連するテスト問題の図とコード

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

![滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

- [実行・検証：Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`) · [コードZIP：Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

この実行例の範囲：滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。




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

ID: `bio-chemical-master` · local-example

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#14-1977-chemical-master-equation-and-gillespie-ssa)

全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布

#### 関連するテスト問題の図とコード

##### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`)

![1本の軌跡と12,288本の固定アンサンブルを分けて検証します。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#code-ja)

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

- [実行・検証：移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`) · [コードZIP：移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

この実行例の範囲：1本の軌跡と12,288本の固定アンサンブルを分けて検証します。




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

自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード

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

- [実行・検証：同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) (`reaction-diffusion-splitting`) · [コードZIP：同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

この実行例の範囲：32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。


##### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`)

![2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#code-ja)

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。

- [実行・検証：Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`) · [コードZIP：Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

この実行例の範囲：2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。




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

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#schrodinger)

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

#### 関連するテスト問題の図とコード

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja)

- [実行・検証：水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`) · [コードZIP：水素型原子：解析解と格子収束](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。


##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [実行・検証：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

- [実行・検証：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja) (`atomic-reference-cards`) · [コードZIP：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。


##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [実行・検証：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

この実行例の範囲：孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

- [実行・検証：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja) (`h2-rhf-uhf-fci`) · [コードZIP：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。


##### [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja) (`quantum-box-ho`)

![1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。 8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#code-ja)

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

- [実行・検証：1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja) (`quantum-box-ho`) · [コードZIP：1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。


##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

![固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

- [実行・検証：3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) (`h3plus-mp2-fci`) · [コードZIP：3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。




### 閉殻Hartree–Fock方程式

ID: `hartree-fock-model` · local-example

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-fock)

閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。

#### 関連するテスト問題の図とコード

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [実行・検証：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

- [実行・検証：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja) (`atomic-reference-cards`) · [コードZIP：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。


##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [実行・検証：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

この実行例の範囲：孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

- [実行・検証：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja) (`h2-rhf-uhf-fci`) · [コードZIP：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。


##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

![固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

- [実行・検証：3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) (`h3plus-mp2-fci`) · [コードZIP：3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。




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

密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#kohn-sham-dft)

#### 関連するテスト問題の図とコード

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [実行・検証：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP：He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

この実行例の範囲：Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

- [実行・検証：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja) (`atomic-reference-cards`) · [コードZIP：H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。


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

- [実行・検証：保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja) (`periodic-he-reference-cards`) · [コードZIP：保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。




### 時間依存Kohn–Sham方程式

ID: `time-dependent-kohn-sham` · reading

$$
i\partial_t\phi_i(\mathbf r,t)=[-\tfrac12\nabla^2+v_s[n](\mathbf r,t)]\phi_i(\mathbf r,t)
$$

局所時間依存KSの代表形。初期状態、交換相関の記憶効果、断熱近似を区別する。実時間と線形応答の専用実装は未公開。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#tddft)

#### 関連するテスト問題の図とコード

この項目に対応付けられたテスト問題は未登録です。



### 2次元の回転移流

ID: `rotational-advection` · local-example

$$
\partial_t q+\partial_x(aq)+\partial_y(bq)=0,\qquad a=-\omega(y-y_c),\quad b=\omega(x-x_c),\quad \partial_xa+\partial_yb=0
$$

与えた剛体回転速度でスカラーを運ぶ2次元保存則。連続場は一回転で戻り、保存量・有界性と切り欠きの形状誤差を調べます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-zalesak/)

単位正方形の周期境界、指定した非圧縮の剛体回転速度、0–1の切り欠き付き円盤を用いる2次元スカラー移流の固定例です。ドナーセル風上法とminmod制限付きMUSCL法をSSPRK(3,3)で進め、64²・128²・256²の一回転と64²の位置・角度変更を検証します。解析的な幾何学的セル平均を参照し、保存量、全記録段階の有界性、形状誤差を別々に評価します。FCT、Euler流体、任意の速度場への検証結果ではありません。

#### 関連するテスト問題の図とコード

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

![実際の2次元スカラー輸送の最細格子の保存セル平均。全\[0,1\]²のうちx∈\[.28,.72\], y∈\[.53,.97\]の円盤周辺を拡大し、一回転後の一次風上とminmod MUSCLを幾何学的な参照セル平均と比較します。切り欠きの数値拡散を残した図で、FCT法やEuler流体の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

与えた発散ゼロの回転速度に従うスカラー輸送で、Euler流体の発展ではありません。Zalesak型の円盤・スロットによる形状保持の問題を用いますが、ZalesakのFCTアルゴリズムそのものを実装した例ではありません。連続指示関数の点値と保存量の幾何学的セル平均を区別し、周期境界での数値的な裾も測ります。

- [実行・検証：Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) (`zalesak-rotation`) · [コードZIP：Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

この実行例の範囲：スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。




### 地形源項付き浅水方程式

ID: `shallow-water-bed` · local-example

$$
\partial_t h+\partial_xq=0
$$

$$
\partial_tq+\partial_x\!\left(q^2/h+gh^2/2\right)=-gh\,\partial_x z,\qquad q=hu
$$

$$
u=0,\qquad h_i=\max(\eta_0-z_i,0)
$$

摩擦・降雨なしの1次元Saint–Venant系。連続の地形と、保存平均から表現した区分定数の床を区別し、静水再構成の釣合いを確認します。 真の乾燥状態h=q=0では運動量の移流流束q²/hを0と定義します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/)

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

#### 関連するテスト問題の図とコード

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

- [実行・検証：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) (`swashes-topography`) · [コードZIP：SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

この実行例の範囲：水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。




### 外力付き非圧縮流と壁面製造解

ID: `forced-incompressible` · local-example

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\Delta\boldsymbol u+\boldsymbol f,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=(\nabla\times\boldsymbol f)_z,\quad-\Delta\psi=\omega,\quad(u,v)=(\psi_y,-\psi_x)
$$

$$
\psi_\star=8x^2(1-x)^2y^2(1-y)^2,\quad s=\boldsymbol u_\star\cdot\nabla\omega_\star-\nu\Delta\omega_\star
$$

$$
-\Delta p_{\mathrm{op},\star}=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p_{\mathrm{op},\star}=x^2+y^2+\sin(\pi x)\sin(\pi y)
$$

一定密度1の外力付き非圧縮系です。実際の流れは外力のcurlを使う渦度・流れ関数形で圧力を消去します。p_opは独立の非零Dirichlet Poisson・勾配演算子の製造問題で、流れと結合した圧力場やキャビティ圧力ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/)

単位正方形・ν=.01・17/33/65点。キャビティと同じThom壁条件で製造流れを解き、速度・流れ関数・壁剪断を比較します。圧力は別の製造演算子問題として評価します。

#### 関連するテスト問題の図とコード

##### [非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

![実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。

- [実行・検証：非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja) (`wall-manufactured`) · [コードZIP：非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

この実行例の範囲：キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。




### レベルセット界面の移流

ID: `level-set-advection` · local-example

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi<0\;\text{inside},\quad\phi>0\;\text{outside}
$$

$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$

ゼロ等値線で界面を表す非保存形の移流式。円の平行移動・剛体回転を検証し、VOFの体積率輸送と区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/)

与えた速度による円の平行移動・偏心1周回転。2D ENO2/Heun、32²/64²/128²、T1、再初期化あり/なし、5共通時刻とN64の刻み半減だけを検証。

#### 関連するテスト問題の図とコード

##### [レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

![実際の128²レベルセット場から抽出した円のゼロ等値線。左は平行移動、右は偏心円の一周回転。解析界面と移流単独・単純な再初期化ありを比較します。VOF計算ではなく、面積保存を補正していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [実行・検証：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja) (`level-set-translation`) · [コードZIP：レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

- [実行・検証：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) (`level-set-rotation`) · [コードZIP：偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

この実行例の範囲：中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。




### 維持されたせん断層の強制渦度系

ID: `forced-vorticity` · local-example

$$
-\Delta\psi=\omega,\qquad (u,v)=(\psi_y,-\psi_x)
$$

$$
\omega_t+U(y)\omega_x+U^{\prime\prime}(y)\psi_x+u\omega_x+v\omega_y=\nu\Delta\omega
$$

$$
U(y)=\tanh(\sin y/\delta),\qquad \Omega_{\mathrm{total}}=-U^{\prime}(y)+\omega
$$

解析的な基底せん断を明示的外力で維持し、微小摂動を実際の非線形2D渦度系で進めます。圧力は消去され、鋭い界面・無限領域・可圧縮KHの分散式とは区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/)

周期[0,2π]²、δ=.25、ν=.005、ε=1e−5、32²/64²/128²、T1の初期成長。独立Fourier–Galerkin線形IVPと、刻み・振幅変更を照合する限定例です。

#### 関連するテスト問題の図とコード

##### [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) (`kh-initial-growth`)

![保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#code-ja)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。

- [実行・検証：KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja) (`kh-initial-growth`) · [コードZIP：KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

この実行例の範囲：実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。




### 能動浮力を伴うBoussinesq渦度系

ID: `boussinesq-buoyancy` · local-example

$$
-\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x),\quad b=b_0(y)+\theta
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+\theta_x
$$

$$
\theta_t+u\theta_x+v\theta_y+v b_0^{\prime}=\kappa\Delta\theta,\qquad b_0=.02\tanh(\sin y/\delta)
$$

慣性密度を一定とし、密度差は浮力だけに残します。基底浮力を外力で維持した摂動形です。全浮力bの鉛直力のcurlがθxを与え、可変密度Euler系とは異なります。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/)

周期[0,2π]²、ν=κ=.005、δ=.25、ε=1e−5、32²/64²/128²、T2。滑らかな二層の初期成長を独立線形参照と比較し、RT乱流や鋭い密度界面を検証したとはしません。

#### 関連するテスト問題の図とコード

##### [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) (`rt-initial-growth`)

![保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#code-ja)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。

- [実行・検証：RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja) (`rt-initial-growth`) · [コードZIP：RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

この実行例の範囲：密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。




### 移動セル上のALEスカラー保存式

ID: `ale-scalar-transport` · local-example

$$
q_t+a q_x=0,\quad m_i(t)=\int_{x_{i-1/2}(t)}^{x_{i+1/2}(t)}q(x,t)\,dx
$$

$$
\dot m_i=-[(a-w)q]_{i-1/2}^{i+1/2},\qquad \dot V_i=w_{i+1/2}-w_{i-1/2}
$$

$$
x(\xi,t)=\xi+\frac{.2}{2\pi}\sin(2\pi\xi)\sin(2\pi t),\quad a=.7
$$

指定した非一様格子の面位置とセル質量を同じHeun段で更新し、幾何保存則と非一様な波の輸送を別々に評価します。Euler流体のLagrange/remap法ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/)

周期単位区間、q0=1+.2sin(2πx)、N40/80/160、T1。一定場GCLと固定Nの時間細分化も検査します。1D指定運動だけで、Saltzmanや一般移動メッシュ流体は対象外です。

#### 関連するテスト問題の図とコード

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。

- [実行・検証：非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`) · [コードZIP：非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

この実行例の範囲：質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。




### 線形回転浅水方程式

ID: `linear-rotating-shallow-water` · local-example

$$
\eta_t+H(u_x+v_y)=0,\qquad u_t-fv=-g\eta_x,\qquad v_t+fu=-g\eta_y
$$

$$
g=H=f=1,\quad \widetilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2)
$$

$$
\omega_h^2=f^2C^2+gH(\widetilde k^2+\widetilde l^2)
$$

平面f-planeの線形波を実際の2D staggered C-gridでRK4時間発展します。連続分散と離散記号の参照を分け、質量・エネルギー・慣性振動・離散定常釣合いを確認します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/)

周期単位正方形、モード(1,2)、高さ振幅.01、N16/32/64、T.5。独立時間系列を備えます。非線形浅水、球面・全球Williamson試験を実装したとはしません。

#### 関連するテスト問題の図とコード

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。

- [実行・検証：2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`) · [コードZIP：2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

この実行例の範囲：実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。




### 可変粘性のベクトル応力境界値問題

ID: `variable-viscosity-vector` · local-example

$$
-\nabla\cdot\boldsymbol\tau=\boldsymbol f,\quad \boldsymbol\tau=2\mu\boldsymbol\varepsilon(\boldsymbol u),\quad \boldsymbol\varepsilon(\boldsymbol u)=\tfrac12(\nabla\boldsymbol u+\nabla\boldsymbol u^T)
$$

$$
1<r<2,\quad \mu=1+r^2/5,\quad A=(r^2-1)(4-r^2),\quad \boldsymbol u_\star=A(1+xy,(x^2-y^2)/2)^T
$$

$$
\int_\Omega2\mu\,\boldsymbol\varepsilon(\boldsymbol u_h):\boldsymbol\varepsilon(\boldsymbol v_h)\,dA=\int_\Omega\boldsymbol f\cdot\boldsymbol v_h\,dA
$$

Cartesianの2成分を結合した線形応力発散BVPです。極座標内のQ1基底と正確な曲線Jacobianを使い、可変μの勾配と剪断応力を含みます。圧力・非圧縮拘束・対流項はありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/)

円環1≤r≤2、両円上で零Dirichlet、θ周期、Nr8/16/32・Nθ=2Nr。速度・ひずみ・物理牽引力・仕事・非零の全境界力を別々に検査します。Navier–Stokesや一般四辺形メッシュの検証ではありません。

#### 関連するテスト問題の図とコード

##### [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。

- [実行・検証：環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`) · [コードZIP：環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

この実行例の範囲：軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。




### 特殊相対論的理想MHD（SRMHD）

ID: `srmhd` · local-example

$$
\partial_\mu(\rho u^\mu)=0,\qquad \partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=(\rho h+b^2)u^\mu u^\nu+(p+b^2/2)\eta^{\mu\nu}-b^\mu b^\nu
$$

$$
\partial_t\boldsymbol B-\nabla\times(\boldsymbol v\times\boldsymbol B)=0,\quad \nabla\cdot\boldsymbol B=0,\quad h=1+\frac{\Gamma p}{(\Gamma-1)\rho}
$$

$$
K=\rho h+B_0^2(1+\eta_A^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta_A^2B_0^4}}
$$

c=4π=1、平坦時空・理想電気伝導・γ則EOSです。bμは流体静止系磁場4ベクトル。全磁気応力と誘導を含む7保存量を1Dで進め、原始変数は完全なRMHDのZ根で復元します。GRMHDとは区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/)

ρ=p=Bx=ηA=1、γ4/3の非線形円偏極厳密族、周期単位区間、N64/128/256、1周期。保存量セル平均・位相・振幅・全段の物理性を検査。一般RMHD衝撃波、極端な磁化/速度、多次元発散制御は対象外です。

#### 関連するテスト問題の図とコード

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。

- [実行・検証：SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) (`srmhd-alfven`) · [コードZIP：SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

この実行例の範囲：完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。




### 不連続係数・完全テンソル拡散の境界値問題

ID: `tensor-diffusion` · local-example

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/)

#### 関連するテスト問題の図とコード

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。

- [実行・検証：係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`) · [コードZIP：係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

この実行例の範囲：不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。


##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。

- [実行・検証：回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`) · [コードZIP：回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

この実行例の範囲：非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。




### Coulomb静電場と混合周期境界

ID: `coulomb-electrostatics` · local-example

$$
\phi(\boldsymbol r)=\sum_j\sum_{\boldsymbol n}^{\prime}\frac{q_j}{|\boldsymbol r-\boldsymbol r_j+\boldsymbol L\boldsymbol n|},\quad\boldsymbol F_i=-q_i\nabla\phi_i
$$

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V,\quad M_z=\sum_iq_iz_i
$$

中性系・Coulomb定数1。真の2周期の参照と、有限真空厚の3周期＋補正を区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-slab-ewald/)

#### 関連するテスト問題の図とコード

##### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#code-ja)

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。

- [実行・検証：中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`) · [コードZIP：中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

この実行例の範囲：4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。




### 静電Vlasov–Poisson方程式

ID: `vlasov-poisson` · local-example

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-warm-pic/)

#### 関連するテスト問題の図とコード

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

Poissonへのリンクは自己無撞着な静電場の部分です。粒子の運動・CIC補間を結合したPIC全体の式が一覧に揃っているわけではありません。

- [実行・検証：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja) (`pic`) · [コードZIP：CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

この実行例の範囲：1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

- [実行・検証：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja) (`pic-conservation`) · [コードZIP：PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

この実行例の範囲：冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

- [実行・検証：PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) (`pic-independent-spatial`) · [コードZIP：PIC空間演算の独立実装照合](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

この実行例の範囲：ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。


##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

![実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。

- [実行・検証：温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`) · [コードZIP：温かいPICの線形Landau減衰](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

この実行例の範囲：熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。


##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

![実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓\[12,20\]とは分けます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。

- [実行・検証：温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) (`thermal-two-stream`) · [コードZIP：温かいPICの二流初期成長](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

この実行例の範囲：温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。




### 剛体球Boltzmann輸送と壁・流入出

ID: `hard-sphere-boltzmann` · local-example

$$
\partial_t f+v_x\partial_x f=Q_{\rm HS}(f,f)
$$

$$
\sigma=1/\sqrt2,\quad\lambda(n)=1/(\sqrt2n\sigma)
$$

1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-wall/)

#### 関連するテスト問題の図とコード

##### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja) (`dsmc-couette`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#code-ja)

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。

- [実行・検証：硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja) (`dsmc-couette`) · [コードZIP：硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。


##### [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) (`dsmc-fourier`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#code-ja)

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。

- [実行・検証：硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja) (`dsmc-fourier`) · [コードZIP：硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。


##### [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#code-ja)

1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。

- [実行・検証：硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`) · [コードZIP：硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip)

この実行例の範囲：物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。




### 静止媒質の灰色輻射輸送・散乱・線形交換

ID: `static-grey-transfer` · local-example

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/)

#### 関連するテスト問題の図とコード

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。

- [実行・検証：等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`) · [コードZIP：等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

この実行例の範囲：正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。


##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

主検証は1997型の輻射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。

- [実行・検証：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`) · [コードZIP：Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

この実行例の範囲：物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。


##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [実行・検証：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`) · [コードZIP：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。


##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [実行・検証：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) (`opposing-beams2d`) · [コードZIP：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。




### Su–Olson1996の非平衡拡散・物質交換

ID: `non-equilibrium-diffusion-exchange` · local-example

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u-\frac{2}{\sqrt3}u_x=1\ (x=0),\quad \epsilon u+v\ \mathrm{is\ the\ weighted\ energy}
$$

x=√3κz。1997輸送のx=κzとは規格化も境界・参照も分けます。非単位epsilonの閉セル検査を別に行います。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/)

#### 関連するテスト問題の図とコード

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。

- [実行・検証：Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`) · [コードZIP：Su–Olson1996非平衡拡散](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

この実行例の範囲：実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。




### 静止媒質・平坦時空の灰色M1モーメント

ID: `static-grey-m1` · local-example

$$
E_t+\nabla\cdot\boldsymbol F=-\kappa E+S_E,\quad\boldsymbol F_t+\nabla\cdot\mathsf P=-\kappa\boldsymbol F+\boldsymbol S_F
$$

$$
\mathsf P=E[(1-\chi)\mathsf I_3/2+(3\chi-1)\boldsymbol n\boldsymbol n^T/2]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\boldsymbol F|/E
$$

c=1、2D空間で3D圧力のPzzを保持。等方・真空分岐、閉じたPDEの製造解、角度法とのビーム差を区別し、相対論的輻射流体とは扱いません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-geometry/)

#### 関連するテスト問題の図とコード

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [実行・検証：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`) · [コードZIP：2D吸収影と保存的M1輸送](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。


##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [実行・検証：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) (`opposing-beams2d`) · [コードZIP：2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

この実行例の範囲：保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。




### スカラーItô拡散：GBMとOU

ID: `scalar-ito-diffusion` · local-example

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-accuracy/)

#### 関連するテスト問題の図とコード

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

幾何Brown運動のItô SDE dX=μXdt+σXdW。既存46式にはSDEの専用項目がありません。

- [実行・検証：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) (`gbm-sde`) · [コードZIP：Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

この実行例の範囲：スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [実行・検証：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja) (`gbm-weak-moments`) · [コードZIP：GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

- [実行・検証：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja) (`gbm-milstein-strong`) · [コードZIP：同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。


##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

![調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

Hamilton系へのリンクは調和ポテンシャルの力学部分です。計算には摩擦・雑音またはCSVRの温度浴が追加されます。

- [実行・検証：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja) (`langevin-harmonic`) · [コードZIP：Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

この実行例の範囲：調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

- [実行・検証：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja) (`csvr-langevin-harmonic`) · [コードZIP：CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

- [実行・検証：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja) (`ou-weak-moments`) · [コードZIP：OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

この実行例の範囲：連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。




### Gaussian確率測度：尾確率と相関標的

ID: `gaussian-probability-model` · local-example

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/)

#### 関連するテスト問題の図とコード

##### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja) (`normal-tail-importance`)

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#code-ja)

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。

- [実行・検証：正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja) (`normal-tail-importance`) · [コードZIP：正規稀少尾の通常importance sampling](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

この実行例の範囲：通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。


##### [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja) (`correlated-gaussian-mcmc`)

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja#code-ja)

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。

- [実行・検証：相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja) (`correlated-gaussian-mcmc`) · [コードZIP：相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

この実行例の範囲：実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。




### 有限次元線形方程式と行列分解

ID: `finite-dimensional-linear-system` · local-example

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)

SPD三重対角・近特異rank1・Hilbert5・Wilkinson12、鞍点速度サイズ12/24。元残差・前進/後退誤差を分けます。

#### 関連するテスト問題の図とコード

##### [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`)

![保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#code-ja)

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。

- [実行・検証：部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`) · [コードZIP：部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。


##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。

- [実行・検証：対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`) · [コードZIP：対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。


##### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`)

![周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#code-ja)

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

- [実行・検証：定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`) · [コードZIP：定常多段RKの実空間モード減衰](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

この実行例の範囲：周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。




### 有限次元の行列固有値問題

ID: `finite-dimensional-eigenproblem` · local-example

$$
A x=\lambda x
$$

主対象は31×31の固定対称行列の標準固有値問題です。行列の離散スペクトルを参照し、連続PDEの空間収束を検査したとはしません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)

再始動長8/16、最大40cycle、shiftなし/0/950、元固有対残差1e−9。

#### 関連するテスト問題の図とコード

##### [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`)

![固有値比較に使う、保存した31×31 Dirichlet Laplacian。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#code-ja)

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。

- [実行・検証：明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`) · [コードZIP：明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。




### 固定端弦の固有値と整合質量FEM

ID: `dirichlet-string-eigenproblem` · local-example

$$
-T\phi^{\prime\prime}=\rho\lambda\phi,\quad 0<x<1
$$

$$
\phi(0)=\phi(1)=0,\quad T=\rho=1
$$

$$
\lambda_j=(j\pi)^2
$$

$$
\lambda_{j,h}=\frac{6(1-\cos\theta_j)}{h^2(2+\cos\theta_j)},\quad\theta_j=\frac{j\pi}{n+1}
$$

単位弦の定常振動形の固有値問題です。整合質量P1の代数固有値誤差と連続体への離散化誤差を分けます。時間発展を実行した例ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)

内部15/31/63点、M内積Krylovと実SciPy1.14.1 LOBPCGを閉離散固有値・generalized LAPACKへ照合。

#### 関連するテスト問題の図とコード

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。

- [実行・検証：整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`) · [コードZIP：整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

この実行例の範囲：整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。




### 線形Maxwell電磁場（真空・誘電体）

ID: `maxwell` · local-example

$$
\partial_t\mathbf B=-\nabla\times\mathbf E,\quad\partial_t\mathbf D=\nabla\times\mathbf H
$$

$$
\mathbf D=\varepsilon(\mathbf x)\mathbf E,\quad\mathbf B=\mathbf H
$$

代表式は3D線形電磁場です。今回の実装はz不変の円柱Ez/Hx/Hyに制限した真2D Yee計算です。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-cylinder/)

s=Ez（TMz、Hz=0）の無損失円柱。p=Hz（TEz、Ez=0）とは成分で区別し、呼称が異なる文献へ式を流用しません。

#### 関連するテスト問題の図とコード

##### [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`)

![保存した最細格子の実2D散乱電場phasorの実部。 図の中央の白抜きは診断用のr<0.4のマスクで、物理円柱の半径0.25とは区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#code-ja)

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。

- [実行・検証：2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`) · [コードZIP：2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

この実行例の範囲：実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。




### 受動Lorentz・Ohmic分散Maxwell場

ID: `maxwell-lorentz` · local-example

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-lorentz/)

sはEz/Hx/HyとPz/Jz、pはHz/Ex/Eyと両電場のPx/Py/Jx/Jy。任意の3D場や横方向多モードではありません。

#### 関連するテスト問題の図とコード

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`)

![保存したp偏光の実電場をky=4の周期y方向へ再構成した場。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#code-ja)

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。

- [実行・検証：Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`) · [コードZIP：Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

この実行例の範囲：有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。


##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`)

![保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#code-ja)

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。

- [実行・検証：分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`) · [コードZIP：分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

この実行例の範囲：80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。




### 有限次元非線形写像・根と微分作用

ID: `finite-dimensional-nonlinear-map` · local-example

$$
F:\mathbb R^n\longrightarrow\mathbb R^m
$$

$$
F(x)=0\quad(m=n\text{ for root controls})
$$

$$
J(x)v=DF(x)[v],\quad J(x)^\top w
$$

$$
H_f(x)v=D(\nabla f)(x)[v]\quad(f\text{ twice differentiable})
$$

有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-reverse-higher-ad/)

Rosenbrock/小Bratuの大域化、重複gather/broadcast矩形写像、固定HVP、正枝陰関数則とliteral停止規約。

#### 関連するテスト問題の図とコード

##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`)

![同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`) · [コードZIP：同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

この実行例の範囲：同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。


##### [独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja) (`reverse-vjp-duality`)

![独立矩形Jacobianと実際の逆微分誤差、固定wide写像の実測sweep数。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja) (`reverse-vjp-duality`) · [コードZIP：独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

この実行例の範囲：重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。


##### [HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja) (`hessian-vector-products`)

![保存HVPと独立参照、状態固定と陰関数全微分の二階曲率を区別した比較。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja) (`hessian-vector-products`) · [コードZIP：HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

この実行例の範囲：forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。


##### [非滑らか点・分岐・停止条件の微分範囲](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja) (`kink-branch-derivatives`)

![保存した非滑らか関数値と停止写像、古典微分が未定義な点とtrace微分を分けた表示。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja#code-ja)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [実行・検証：非滑らか点・分岐・停止条件の微分範囲](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja) (`kink-branch-derivatives`) · [コードZIP：非滑らか点・分岐・停止条件の微分範囲](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

この実行例の範囲：古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。




### 有限次元代数最適化と既知最小点

ID: `finite-dimensional-optimization` · local-example

$$
\min_{x\in\mathbb R^n} f(x)
$$

$$
\nabla f(x_*)=0\quad\text{(necessary for a smooth unconstrained local minimum)}
$$

$$
f_Q(x)=\tfrac12(x-x_*)^TA(x-x_*),\quad A=A^T>0
$$

$$
f_R(x,y)=100(y-x^2)^2+(1-x)^2
$$

8次元SPD二次関数と2変数Rosenbrockの無次元代数最適化です。物理空間・PDE境界を持たず、既知最小点と局所反復作用を比較します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-inverse-optimization/)

既知最小点、勾配、Wolfe/曲率ledger、現在保持する3組と現在γ0Iのdense作用参照。

#### 関連するテスト問題の図とコード

##### [既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`)

![実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#code-ja)

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。

- [実行・検証：既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`) · [コードZIP：既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

この実行例の範囲：8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。




### Robertson反応系

ID: `robertson-kinetics` · local-example

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=0.04y_1-10^4y_2y_3-3\times10^7y_2^2,\quad\dot y_3=3\times10^7y_2^2
$$

$$
y_1+y_2+y_3=1
$$

3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)

3成分の固定Robertson反応系を、短い時区間のODEと固定した粗い刻みの保存則DAEで検証します。DAEの未達の時間精度・収束目標もそのまま表示します。

#### 関連するテスト問題の図とコード

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

- [実行・検証：Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`) · [コードZIP：Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

- [実行・検証：Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) (`robertson-conservation-dae`) · [コードZIP：Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

この実行例の範囲：Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。




### van der Pol振動子

ID: `van-der-pol` · local-example

$$
\dot x=v,\qquad\dot v=\mu(1-x^2)v-x
$$

固定したμと短い時区間で硬さによる仕事量と誤差を比較します。完全な緩和振動周期の検証ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)

#### 関連するテスト問題の図とコード

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`)

![保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#code-ja)

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

- [実行・検証：van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`) · [コードZIP：van der Polの短時間剛性遷移](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。




### 有限次元の線形発展系

ID: `linear-evolution-system` · local-example

$$
\dot y=Ay+b
$$

減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)

#### 関連するテスト問題の図とコード

##### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) (`rk45-dense-events`)

![減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#code-ja)

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

- [実行・検証：RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja) (`rk45-dense-events`) · [コードZIP：RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。


##### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`)

![周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#code-ja)

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

- [実行・検証：定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`) · [コードZIP：定常多段RKの実空間モード減衰](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

この実行例の範囲：周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。




### 非同次境界を持つ線形反応拡散

ID: `inhomogeneous-reaction-diffusion` · local-example

$$
u_t=u_{xx}+u,\quad0<x<1,\quad u(0,t)=u(1,t)=1
$$

同じ非周期有限差分系に対する時間誤差と、連続厳密解に対する空間誤差を分けます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/)

#### 関連するテスト問題の図とコード

##### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`)

![実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#code-ja)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

- [実行・検証：Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`) · [コードZIP：Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。




### 半陽的index-1 DAE

ID: `index-one-dae` · local-example

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/)

#### 関連するテスト問題の図とコード

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

- [実行・検証：Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`) · [コードZIP：Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

この実行例の範囲：短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

- [実行・検証：Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) (`robertson-conservation-dae`) · [コードZIP：Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

この実行例の範囲：Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。


##### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`)

![既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#code-ja)

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

- [実行・検証：index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`) · [コードZIP：index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

この実行例の範囲：既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。




### 拘束付き平面振り子

ID: `constrained-pendulum` · local-example

$$
\dot q=p,\quad\dot p=(0,-1)-\lambda q,\quad q^Tq=1,\quad q^Tp=0
$$

元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/)

#### 関連するテスト問題の図とコード

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

- [実行・検証：振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) (`high-index-pendulum`) · [コードZIP：振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

この実行例の範囲：位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

- [実行・検証：SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja) (`shake-rattle-pendulum`) · [コードZIP：SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。




### Kepler二体問題

ID: `kepler-two-body` · local-example

$$
\dot q=p,\qquad\dot p=-q/\|q\|^3,\qquad H=\tfrac12p^Tp-1/\|q\|
$$

無次元化した平面楕円軌道で位相、角運動量、エネルギーと刻みの影響を分けます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)

#### 関連するテスト問題の図とコード

##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [実行・検証：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) (`gravity-kepler`) · [コードZIP：無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

この実行例の範囲：非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

- [実行・検証：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja) (`kepler-eccentricity`) · [コードZIP：離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。




### 二周波数の結合調和振動子

ID: `coupled-harmonic-oscillators` · local-example

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+q_1q_2
$$

連続正規モード、理想分割写像、保存した浮動小数点係数の写像、実際の反復丸めを区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)

#### 関連するテスト問題の図とコード

##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

- [実行・検証：結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`) · [コードZIP：結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

この実行例の範囲：2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。




### 有限・無限・多変数の定積分

ID: `definite-integrals` · local-example

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quadrature-controls/)

#### 関連するテスト問題の図とコード

##### [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja) (`quadpack-domain-selection`)

![活動Fourier周期の保存寄与と誤差・評価数 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成25件・未達2件・計算不能3件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#code-ja)

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

- [実行・検証：領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja) (`quadpack-domain-selection`) · [コードZIP：領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

この実行例の範囲：15本の特殊化求積と15本のSimpson対照を固定入力で比較します。


##### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`)

![保存された変換関数と有限窓誤差（連続tailは別量） 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#code-ja)

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

- [実行・検証：G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`) · [コードZIP：G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

この実行例の範囲：9本の適応GKと24本の固定DE和を比較します。


##### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`)

![実2次元節点と符号付き積分重み 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#code-ja)

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

- [実行・検証：2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`) · [コードZIP：2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

この実行例の範囲：滑らかな積と相互作用積の42本の固定cubatureを比較します。




### 格納節点の多項式補間

ID: `polynomial-interpolation` · local-example

$$
P_n(x_j)=y_j,\quad P_n\in\mathcal P_n
$$

$$
R(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)}
$$

閉形式重みと丸め節点の表現差、補間誤差と演算丸めを分けます。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/)

#### 関連するテスト問題の図とコード

##### [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`)

![Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#code-ja)

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

- [実行・検証：節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`) · [コードZIP：節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

この実行例の範囲：Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。




### 3次スプラインと形状保存補間

ID: `cubic-spline-pchip` · local-example

$$
S_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3
$$

$$
S\in C^2\ \text{for the natural/clamped spline};\quad P\in C^1\ \text{for PCHIP}
$$

端点条件を持つC2補間と単調な区分Hermite補間を区別します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/)

#### 関連するテスト問題の図とコード

##### [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja) (`spline-shape-controls`)

![平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#code-ja)

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

- [実行・検証：自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja) (`spline-shape-controls`) · [コードZIP：自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

この実行例の範囲：平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。




### 有限長信号の離散Haar変換

ID: `discrete-haar-transform` · local-example

$$
\binom{a^{\prime}}d=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom ab
$$

$$
S_NA_N=I_N,\quad\|A_Nx\|_2^2=\|x\|_2^2+\sum_\ell p_\ell^2
$$

奇数長の追加標本と切戻しを含む有限写像です。冗長拡張全体の直交性は仮定しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/)

#### 関連するテスト問題の図とコード

##### [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`)

![長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。 標本添字は物理空間の座標ではありません。境界処理を含む有限長信号の写像です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#code-ja)

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

- [実行・検証：Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`) · [コードZIP：Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

この実行例の範囲：長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。




### 閉鎖SEIR区画モデル

ID: `seir-compartment` · local-example

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
S+E+I+R=1
$$

出生死亡なし・全人口一定の教育用率です。初期過渡は2×2行列指数に比較し、感染症予測には使いません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-small-models/)

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。

#### 関連するテスト問題の図とコード

##### [SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja) (`seir-linearization`)

![人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja#code-ja)

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

- [実行・検証：SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja) (`seir-linearization`) · [コードZIP：SEIR保存則と初期線形化](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

この実行例の範囲：人口保存と2モードの初期線形化を別々に検査します。




### 2準位電子角と核のBO/CP型模型

ID: `two-state-bo-cp-model` · local-example

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

#### 関連するテスト問題の図とコード

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

![電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

- [実行・検証：2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) (`two-state-bo-cp-ou`) · [コードZIP：2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。




### 最小2電子模型のスピン非制限HF

ID: `unrestricted-hartree-fock-model` · local-example

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/)

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

#### 関連するテスト問題の図とコード

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [実行・検証：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP：H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

この実行例の範囲：孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

- [実行・検証：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja) (`h2-rhf-uhf-fci`) · [コードZIP：最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。




### 3平面波・非局所核と平均Fermi占有

ID: `finite-projector-fermi-model` · local-example

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/)

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

#### 関連するテスト問題の図とコード

##### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) (`finite-projector-fermi`)

![3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#code-ja)

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

- [実行・検証：3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja) (`periodic-projector-occupations`) · [コードZIP：3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

この実行例の範囲：3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。




### 移入–死亡反応と厳密過渡法則

ID: `immigration-death-model` · local-example

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/)

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

#### 関連するテスト問題の図とコード

##### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`)

![1本の軌跡と12,288本の固定アンサンブルを分けて検証します。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#code-ja)

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

- [実行・検証：移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`) · [コードZIP：移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

この実行例の範囲：1本の軌跡と12,288本の固定アンサンブルを分けて検証します。




### 外力・移流付きKeller–Segel製造問題

ID: `forced-keller-segel-model` · local-example

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

$$
n_*=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y)
$$

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-space-controls/)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

#### 関連するテスト問題の図とコード

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

![滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

- [実行・検証：Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`) · [コードZIP：Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

この実行例の範囲：滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。




### 2モードの決定論的温度浴

ID: `finite-mode-thermostat-model` · local-example

$$
U(q)=\sum_{i=1}^2(\omega_i^2q_i^2/2+\kappa q_i^4/4),\quad\omega=(1,1.7),\ \kappa=0,.2
$$

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostat-constraint-controls/)

単位質量,kBT=1、周波数1/1.7、quartic係数0/0.2。NH1/NHC3/Berendsen/速度固定、2結合・2刻み、正準256＋加熱128レプリカを固定します。

#### 関連するテスト問題の図とコード

##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

![弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

Hamilton系へのリンクは非調和ポテンシャルの力学部分です。確率温度浴を加えたCSVR・Langevinの分布検証を行います。

- [実行・検証：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja) (`csvr-langevin-quartic`) · [コードZIP：非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

この実行例の範囲：弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

- [実行・検証：NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja) (`deterministic-thermostat-contrasts`) · [コードZIP：NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

この実行例の範囲：同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。




### 固定線形拘束の正準運動量

ID: `projected-canonical-model` · local-example

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostat-constraint-controls/)

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

#### 関連するテスト問題の図とコード

##### [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja) (`projected-canonical-dof`)

![有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。 固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#code-ja)

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

- [実行・検証：拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja) (`projected-canonical-dof`) · [コードZIP：拘束・重心除去と正準統計](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

この実行例の範囲：有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。




### 球面上の所与速度スカラー移流

ID: `sphere-scalar-advection` · local-example

$$
q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r)
$$

$$
\mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)
$$

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/)

#### 関連するテスト問題の図とコード

##### [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`)

![所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#code-ja)

- [実行・検証：Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`) · [コードZIP：Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

この実行例の範囲：所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。




### 球面浅水波の軸対称部分問題

ID: `spherical-shallow-water` · local-example

$$
h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0
$$

$$
v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0
$$

$$
u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi
$$

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/)

#### 関連するテスト問題の図とコード

##### [球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja) (`sphere-zonal-balance`)

![球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja#code-ja)

- [実行・検証：球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja) (`sphere-zonal-balance`) · [コードZIP：球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

この実行例の範囲：球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。




### 静止灰色輻射のVEF・VETモーメント閉包

ID: `static-grey-variable-eddington-moments` · local-example

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_t I=\sigma_s E+q,\quad E=\langle I\rangle
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf D E)=0
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{\langle I\rangle},\quad\sigma_a=\sigma_t-\sigma_s
$$

c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/)

#### 関連するテスト問題の図とコード

##### [可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`)

![形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#code-ja)

- [実行・検証：可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`) · [コードZIP：可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

この実行例の範囲：形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。


##### [可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`)

![非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

[コード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#code-ja)

- [実行・検証：可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`) · [コードZIP：可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

この実行例の範囲：非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。




## English

### Linear advection

ID: `linear-advection` · local-example

$$
\partial_t u+a\,\partial_xu=0
$$

Transport at constant speed a: translation, numerical diffusion and stability.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)

Retain existing common advection examples. The additional FV WENO comparison uses q₀=cos(2πx)+.1sin³(2πx), periodic[0,1], speed1 and T1. Local critical polynomials are separate diagnostics; distinguish point values, cell means and time-step effects.

#### Related test problem figures and code

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [Run and validate: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en) (`advection-sine`) · [Code ZIP: Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

- [Run and validate: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP: WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Scope of this execution example: Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

- [Run and validate: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) (`fr-periodic-advection`) · [Code ZIP: 1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.


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

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

- [Run and validate: Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en) (`fno-periodic-heat`) · [Code ZIP: Tiny FNO on held-out heat problems](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Scope of this execution example: Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.


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


##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.

- [Run and validate: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) (`su-olson-transport1997`) · [Code ZIP: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Scope of this execution example: Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.


##### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`)

![Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#code-en)

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.

- [Run and validate: Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`) · [Code ZIP: Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Scope of this execution example: Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.


##### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`)

![Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#code-en)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

- [Run and validate: Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`) · [Code ZIP: Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.




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

Additional cases cover an L-shaped singularity with matched-DOF grading,warped squares,pure-Neumann compatibility/mean gauge and mixed Robin conditions. Existing Poisson examples remain; distinguish residuals from continuous error.

#### Related test problem figures and code

##### [1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

![Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

- [Run and validate: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`) · [Code ZIP: 1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.

- [Run and validate: Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en) (`pinn-poisson`) · [Code ZIP: Poisson PINN: independent grid error](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Scope of this execution example: Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.


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

- [Run and validate: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP: 2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Scope of this execution example: Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.


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

- [Run and validate: Ewald: asymmetric-cell energies and forces versus independent theta integration](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en) (`ewald-convergence`) · [Code ZIP: Ewald: asymmetric-cell energies and forces versus independent theta integration](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

- [Run and validate: SPME: mesh, interpolation order, mesh phase and conservation](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en) (`spme-convergence`) · [Code ZIP: SPME: mesh, interpolation order, mesh phase and conservation](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.


##### [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

![Stored potential/field errors for 128 fixed-seed particles with a 2D free-space log kernel: FMM orders 2/4/8/12 versus a separate all-pairs sum.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

A particle sum with the logarithmic Green kernel of 2D Poisson/Laplace, distinct from softened 3D 1/r gravity.

- [Run and validate: 2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en) (`fmm`) · [Code ZIP: 2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

- [Run and validate: FMM: direct and analytic references, order and tree depth](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en) (`fmm-convergence`) · [Code ZIP: FMM: direct and analytic references, order and tree depth](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.


##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

Poisson identifies the self-consistent electrostatic field; the registry does not list the complete coupled particle-motion/CIC PIC system.

- [Run and validate: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) (`pic`) · [Code ZIP: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

- [Run and validate: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en) (`pic-conservation`) · [Code ZIP: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

- [Run and validate: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) (`pic-independent-spatial`) · [Code ZIP: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

Scope of this execution example: Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.


##### [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.

- [Run and validate: L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en) (`lshape-fem`) · [Code ZIP: L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.


##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.

- [Run and validate: Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) (`poisson-neumann`) · [Code ZIP: Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Solve singular2D Poisson with compatibility/gauge and reject incompatible source.


##### [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.

- [Run and validate: 2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en) (`poisson-robin`) · [Code ZIP: 2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.




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

- [Run and validate: Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en) (`gsph-sod`) · [Code ZIP: Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Scope of this execution example: ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.


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

- [Run and validate: Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) (`euler-double-rarefaction-positivity`) · [Code ZIP: Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

Scope of this execution example: Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.


##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

Compressible Euler with the same Mach10 data and gamma1.4 is evolved over the full rectangle[0,4]×[0,1].

- [Run and validate: Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en) (`double-mach-reflection`) · [Code ZIP: Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

Scope of this execution example: Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.


##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

Two-dimensional Euler flow with gamma=1.4 and inflow rho=1.4,u=3,v=0,p=1 evolves to T=4 in [0,3]×[0,1] minus a step of height .2 starting at x=.6.

- [Run and validate: Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en) (`forward-step-m3`) · [Code ZIP: Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

Scope of this execution example: Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.


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

![Actual 2D Euler evolution at M∞=.01, 64² and T=.1. A central \[-3,3\]² crop of the full \[-10,10\]² computation compares ordinary and preconditioned Roe with MUSCL. Vorticity is derived by finite differences of saved velocity; arrows show velocity minus the background flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

- [Run and validate: Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en) (`low-mach-vortex`) · [Code ZIP: Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

Scope of this execution example: The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.


##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Density from an actual2D Cartesian Euler computation:full square128²,p0=0,gamma5/3,t=.6. White dashed circle is the exact shock. Axis/diagonal differences and origin heating remain visible, with links to earlier1D radial examples.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

Planar/cylindrical/spherical radial Euler and actual2D Cartesian Euler. The2D edition has no geometric source, radial reduction or symmetry boundary; all four edges prescribe cold inflow.

- [Run and validate: Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP: Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

Scope of this execution example: An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

- [Run and validate: Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) (`noh-cartesian-2d`) · [Code ZIP: Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

Scope of this execution example: A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.


##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

![A central-section view of saved one-dimensional spherical-radial Euler density:gamma5/3,E=rho0=1,p0=0,t=.05,512 shells and finite deposition radius.03. Point-source reference differences and shock errors remain visible; this is not an actual2D Cartesian computation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

Nondimensional spherical-radial Euler flow, evolving radial density, momentum and total energy with volume weighting.

- [Run and validate: Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) (`sedov-blast`) · [Code ZIP: Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

Scope of this execution example: A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.


##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

![A meridional-section display of saved one-dimensional spherical-radial Euler density: gamma=1.4, 512 shells, r in \[0,0.75\], Rs(-1)=0.6, t=-0.85. Compare the pre-collapse shock entering stationary zero-pressure upstream gas with a semi-analytic reference. This is not 2D Cartesian or post-collapse evolution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

Spherical-radial ideal-gas Euler flow, evolving density, radial momentum and total energy with shell-volume weighting and separately integrating the radial-momentum geometric source.

- [Run and validate: Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) (`guderley-implosion`) · [Code ZIP: Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

Scope of this execution example: An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.


##### [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`)

![Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#code-en)

- [Run and validate: Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`) · [Code ZIP: Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Scope of this execution example: Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.


##### [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`)

![Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#code-en)

- [Run and validate: Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`) · [Code ZIP: Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Scope of this execution example: Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.




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

Retain existing wet1D examples and linear rotating Fourier checks. The additional Ritter case is genuinely dry flat-bed flow with g9.81,[-10,10],hL1/hR0 and t.5. Bed-source lakes and Bernoulli flow link to the separate shallow-water-bed model.

#### Related test problem figures and code

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution example is registered.

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,800/1600/3200 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.

- [Run and validate: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`) · [Code ZIP: Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.




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

Retain existing MHD examples. Add a full-eight-state1D aligned CP wave and actual2D magnetic-loop/postshock Orszag–Tang cases. Independent Athena references for the latter two are finite-grid numerical solutions,not exact or generic validation.

#### Related test problem figures and code

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

- [Run and validate: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en) (`ct-glm-independent`) · [Code ZIP: Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Scope of this execution example: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

- [Run and validate: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en) (`ct-glm-ot-convergence`) · [Code ZIP: Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Scope of this execution example: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

- [Run and validate: Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) (`postshock-orszag-tang`) · [Code ZIP: Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.


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

- [Run and validate: Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) (`circular-alfven-refinement`) · [Code ZIP: Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.


##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

- [Run and validate: Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) (`magnetic-loop-independent`) · [Code ZIP: Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Scope of this execution example: Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.


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

Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/)

Retain existing periodic2D MAC projection/Taylor–Green examples. The additional nonperiodic Re100 cavity uses vorticity/streamfunction and Thom walls, comparing velocity centerlines with finite-grid Ghia tables. Pressure is eliminated; this adds no cavity-pressure, pressure-boundary or MAC-projection validation.

#### Related test problem figures and code

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

- [Run and validate: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

- [Run and validate: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) (`lbm-taylor-green`) · [Code ZIP: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

Scope of this execution example: Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.


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

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

Dimensionless unit square, viscosity.01, lid speed1, Re100. Top interior nodes haveu1; other walls and all four corners have zero velocity. Psi0 on every wall; initial interior vorticity0. Reapply Thom wall vorticity at every Heun stage.

- [Run and validate: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) (`cavity-ghia-re100`) · [Code ZIP: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

- [Run and validate: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) (`lbm-cavity-re100`) · [Code ZIP: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

Scope of this execution example: Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.


##### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

- [Run and validate: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`) · [Code ZIP: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

Scope of this execution example: Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.


##### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

- [Run and validate: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`) · [Code ZIP: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

Scope of this execution example: Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.




### Isothermal lattice BGK

ID: `bgk` · local-example

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/)

#### Related test problem figures and code

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

- [Run and validate: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en) (`taylor-green`) · [Code ZIP: Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Scope of this execution example: Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

- [Run and validate: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) (`lbm-taylor-green`) · [Code ZIP: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

Scope of this execution example: Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.


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

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

Dimensionless unit square, viscosity.01, lid speed1, Re100. Top interior nodes haveu1; other walls and all four corners have zero velocity. Psi0 on every wall; initial interior vorticity0. Reapply Thom wall vorticity at every Heun stage.

- [Run and validate: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) (`cavity-ghia-re100`) · [Code ZIP: Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

- [Run and validate: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) (`lbm-cavity-re100`) · [Code ZIP: LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

Scope of this execution example: Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.


##### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

- [Run and validate: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`) · [Code ZIP: Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

Scope of this execution example: Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.


##### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

- [Run and validate: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`) · [Code ZIP: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

Scope of this execution example: Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.




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

- [Run and validate: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en) (`ou-weak-moments`) · [Code ZIP: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.


##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

![Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

The Hamiltonian link identifies the anharmonic mechanical part; validation concerns distributions with added stochastic CSVR/Langevin heat baths.

- [Run and validate: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en) (`csvr-langevin-quartic`) · [Code ZIP: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

- [Run and validate: NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en) (`deterministic-thermostat-contrasts`) · [Code ZIP: NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

Scope of this execution example: Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.


##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Run and validate: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) (`gravity-kepler`) · [Code ZIP: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

- [Run and validate: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en) (`kepler-eccentricity`) · [Code ZIP: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.


##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

- [Run and validate: Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) (`high-index-pendulum`) · [Code ZIP: Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Scope of this execution example: Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

- [Run and validate: SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en) (`shake-rattle-pendulum`) · [Code ZIP: SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.


##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

- [Run and validate: Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) (`multifrequency-resonance`) · [Code ZIP: Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.




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


##### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#code-en)

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

- [Run and validate: Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`) · [Code ZIP: Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

Scope of this execution example: Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.


##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Run and validate: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) (`gravity-kepler`) · [Code ZIP: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

- [Run and validate: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en) (`kepler-eccentricity`) · [Code ZIP: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.


##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

- [Run and validate: Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) (`gravity-plummer-short`) · [Code ZIP: Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.




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


##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.

- [Run and validate: Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`) · [Code ZIP: Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Scope of this execution example: Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.


##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.

- [Run and validate: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`) · [Code ZIP: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Scope of this execution example: Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.


##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`)

![Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`) · [Code ZIP: Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

Scope of this execution example: Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.


##### [Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`)

![Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`) · [Code ZIP: Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

Scope of this execution example: Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.


##### [Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en) (`hessian-vector-products`)

![Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en) (`hessian-vector-products`) · [Code ZIP: Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

Scope of this execution example: Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.


##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.

- [Run and validate: Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`) · [Code ZIP: Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Scope of this execution example: At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.


##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.

- [Run and validate: Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`) · [Code ZIP: Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Scope of this execution example: Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.


##### [Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`)

![Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#code-en)

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.

- [Run and validate: Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`) · [Code ZIP: Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

Scope of this execution example: Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.


##### [Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`)

![Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#code-en)

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.

- [Run and validate: Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`) · [Code ZIP: Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

Scope of this execution example: Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.




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

ID: `srhd` · local-example

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

Ideal fluid in flat Cartesian spacetime,c=1. Add a mild fixed symmetric two-shock example with gamma-law EOS and primitive recovery; no general three-wave Riemann,extreme-Lorentz-factor or GR claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/#what-changes-from-the-existing-euler-examples)

rho1,p.1,v±.3,gamma5/3,96/192/384 cells,T.3,extrapolation boundaries. Compare independent Taub exact means,pressure-root SRHD recovery/flux,boundary budgets and all-stage admissibility.

#### Related test problem figures and code

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.

- [Run and validate: SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) (`srhd-collision`) · [Code ZIP: SRHD symmetric two-shock collision](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Scope of this execution example: Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.




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

ID: `bio-enzyme` · local-example

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Scoped executed example: These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#02-1913-michaelismenten-and-full-enzyme-kinetics)

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

#### Related test problem figures and code

##### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) (`enzyme-qssa`)

![Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#code-en)

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

- [Run and validate: Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en) (`enzyme-qssa`) · [Code ZIP: Enzyme conservation and QSSA](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Scope of this execution example: Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.




### Lotka–Volterra predator–prey

ID: `bio-lotka-volterra` · local-example

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

Coupled prey growth and predation; a phase-plane and long-time integration test. Scoped executed example: This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#03-1920-lotkavolterra-predatorprey)

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

#### Related test problem figures and code

##### [Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en) (`lotka-volterra`)

![Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en#code-en)

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

- [Run and validate: Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en) (`lotka-volterra`) · [Code ZIP: Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Scope of this execution example: Compare a positive orbit against an independently integrated log-coordinate reference.




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

ID: `bio-fisher-kpp` · local-example

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Not implementation of the entire model family. Fixed cases: Fisher–KPP: a special-speed exact front

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#06-1937-fisherkpp-invasion-front)

Not implementation of the entire model family. Fixed cases: Fisher–KPP: a special-speed exact front

#### Related test problem figures and code

##### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`)

![Separate profile, phase, grid, time and finite-boundary errors. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#code-en)

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.

- [Run and validate: Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`) · [Code ZIP: Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Scope of this execution example: Separate profile, phase, grid, time and finite-boundary errors.




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

ID: `bio-hodgkin-huxley` · local-example

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Not implementation of the entire model family. Fixed cases: Hodgkin–Huxley: clamps, rest and firing

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#08-1952-hodgkinhuxley-membrane-dynamics)

Not implementation of the entire model family. Fixed cases: Hodgkin–Huxley: clamps, rest and firing

#### Related test problem figures and code

##### [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`)

![Compare analytic clamp gates and a four-state system with segment-owned current. This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#code-en)

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.

- [Run and validate: Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`) · [Code ZIP: Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

Scope of this execution example: Compare analytic clamp gates and a four-state system with segment-owned current.




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

- [Run and validate: Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) (`reaction-diffusion-splitting`) · [Code ZIP: Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

Scope of this execution example: Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.




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

ID: `bio-keller-segel` · local-example

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Not implementation of the entire model family. Fixed cases: Keller–Segel: a manufactured coupled-flux solution

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#11-1970-kellersegel-chemotaxis)

Not implementation of the entire model family. Fixed cases: Keller–Segel: a manufactured coupled-flux solution

#### Related test problem figures and code

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

![Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

- [Run and validate: Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`) · [Code ZIP: Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Scope of this execution example: Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.




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

ID: `bio-chemical-master` · local-example

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Not implementation of the entire model family. Fixed cases: Immigration–death SSA: exact transient laws

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#14-1977-chemical-master-equation-and-gillespie-ssa)

Not implementation of the entire model family. Fixed cases: Immigration–death SSA: exact transient laws

#### Related test problem figures and code

##### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) (`immigration-death-ssa`)

![Separate one displayed path from12,288fixed ensemble paths. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#code-en)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

- [Run and validate: Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en) (`immigration-death-ssa`) · [Code ZIP: Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

Scope of this execution example: Separate one displayed path from12,288fixed ensemble paths.




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

A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. The earlier 1D case alone makes no general pattern-selection, biological-calibration or fluid-coupling claim. Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes

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

- [Run and validate: Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) (`reaction-diffusion-splitting`) · [Code ZIP: Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

Scope of this execution example: Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.


##### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`)

![Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#code-en)

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.

- [Run and validate: Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`) · [Code ZIP: Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Scope of this execution example: Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.




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

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#schrodinger)

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

#### Related test problem figures and code

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en)

- [Run and validate: Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`) · [Code ZIP: Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.


##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Run and validate: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

- [Run and validate: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en) (`atomic-reference-cards`) · [Code ZIP: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.


##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Run and validate: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Scope of this execution example: Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

- [Run and validate: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en) (`h2-rhf-uhf-fci`) · [Code ZIP: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.


##### [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en) (`quantum-box-ho`)

![Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity. Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#code-en)

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

- [Run and validate: Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en) (`quantum-box-ho`) · [Code ZIP: Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.


##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

![Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

- [Run and validate: A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) (`h3plus-mp2-fci`) · [Code ZIP: A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.




### Closed-shell Hartree–Fock equations

ID: `hartree-fock-model` · local-example

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-fock)

Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.

#### Related test problem figures and code

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Run and validate: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

- [Run and validate: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en) (`atomic-reference-cards`) · [Code ZIP: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.


##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Run and validate: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Scope of this execution example: Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

- [Run and validate: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en) (`h2-rhf-uhf-fci`) · [Code ZIP: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.


##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

![Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

- [Run and validate: A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) (`h3plus-mp2-fci`) · [Code ZIP: A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.




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

Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#kohn-sham-dft)

#### Related test problem figures and code

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Run and validate: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP: Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Scope of this execution example: Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

- [Run and validate: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en) (`atomic-reference-cards`) · [Code ZIP: Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.


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

- [Run and validate: Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en) (`periodic-he-reference-cards`) · [Code ZIP: Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.




### Time-dependent Kohn–Sham equations

ID: `time-dependent-kohn-sham` · reading

$$
i\partial_t\phi_i(\mathbf r,t)=[-\tfrac12\nabla^2+v_s[n](\mathbf r,t)]\phi_i(\mathbf r,t)
$$

Representative local time-dependent KS equations. Distinguish initial-state dependence, exchange-correlation memory and adiabatic approximations. No dedicated real-time or response implementation is published.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#tddft)

#### Related test problem figures and code

No associated test problem is registered for this entry.



### Two-dimensional rotational advection

ID: `rotational-advection` · local-example

$$
\partial_t q+\partial_x(aq)+\partial_y(bq)=0,\qquad a=-\omega(y-y_c),\quad b=\omega(x-x_c),\quad \partial_xa+\partial_yb=0
$$

A two-dimensional scalar conservation law in a prescribed rigid rotation. The continuum field returns after one turn, enabling mass, bounds and slotted-shape error checks.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-zalesak/)

A fixed two-dimensional scalar-advection example on the periodic unit square with prescribed divergence-free rigid rotation and a 0–1 slotted disk. Donor-cell upwind and minmod-limited MUSCL use SSPRK(3,3); one-turn runs use 64², 128² and 256² grids, with position and angle probes at 64². Analytic geometric cell averages provide the reference, and mass, bounds at every recorded stage and shape error are assessed separately. This does not validate FCT, Euler fluid dynamics or arbitrary velocity fields.

#### Related test problem figures and code

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

![Saved cell means on the finest grid of actual two-dimensional scalar transport. Zoom x in\[.28,.72\],y in\[.53,.97\] from the full unit square and compare donor-cell upwinding and minmod MUSCL after one revolution against geometric reference cell means. Slot diffusion remains visible; this is not an FCT algorithm or Euler-flow calculation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

This is scalar transport in a prescribed divergence-free rotation, not Euler-fluid evolution. It uses a Zalesak-type slotted-disk shape test without claiming implementation of Zalesak’s FCT algorithm. Pointwise indicator values and geometric conserved cell means are distinguished; numerical tails near periodic boundaries are also measured.

- [Run and validate: Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) (`zalesak-rotation`) · [Code ZIP: Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

Scope of this execution example: Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.




### Shallow-water equations with bed source

ID: `shallow-water-bed` · local-example

$$
\partial_t h+\partial_xq=0
$$

$$
\partial_tq+\partial_x\!\left(q^2/h+gh^2/2\right)=-gh\,\partial_x z,\qquad q=hu
$$

$$
u=0,\qquad h_i=\max(\eta_0-z_i,0)
$$

One-dimensional frictionless Saint–Venant flow without rainfall. Distinguish the continuous topography from represented piecewise-constant bed means when checking hydrostatic balance. At a genuinely dry state h=q=0, define the advective momentum flux q²/h as0.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/)

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

#### Related test problem figures and code

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

- [Run and validate: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) (`swashes-topography`) · [Code ZIP: SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Scope of this execution example: Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.




### Forced incompressible flow and wall manufactured solutions

ID: `forced-incompressible` · local-example

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\Delta\boldsymbol u+\boldsymbol f,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=(\nabla\times\boldsymbol f)_z,\quad-\Delta\psi=\omega,\quad(u,v)=(\psi_y,-\psi_x)
$$

$$
\psi_\star=8x^2(1-x)^2y^2(1-y)^2,\quad s=\boldsymbol u_\star\cdot\nabla\omega_\star-\nu\Delta\omega_\star
$$

$$
-\Delta p_{\mathrm{op},\star}=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p_{\mathrm{op},\star}=x^2+y^2+\sin(\pi x)\sin(\pi y)
$$

Constant-density-one forced incompressible flow. The actual solver uses the curl forcing in a pressure-eliminated vorticity/streamfunction form. p_op is a separate nonzero-Dirichlet Poisson/gradient manufactured operator problem, not a coupled flow pressure or cavity pressure.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/)

Unit square, viscosity.01 and17/33/65nodes. Evolve the manufactured flow with the same Thom closure as the cavity, comparing velocity, streamfunction and wall shear. Pressure is assessed only in a separate manufactured operator problem.

#### Related test problem figures and code

##### [Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

![Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

Unit square, viscosity.01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.

- [Run and validate: Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en) (`wall-manufactured`) · [Code ZIP: Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Scope of this execution example: Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.




### Level-set interface advection

ID: `level-set-advection` · local-example

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi<0\;\text{inside},\quad\phi>0\;\text{outside}
$$

$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$

Nonconservative transport of an implicit zero-contour interface. Dedicated circle translation and rigid rotation distinguish this from VOF fraction transport.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)

Prescribed circle translation and off-center full rotation only: 2D ENO2/Heun,32²/64²/128²,T1, optional redistancing, five common observations and anN64 CFL-halving sensitivity.

#### Related test problem figures and code

##### [Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

![Zero contours extracted from actual128² level-set fields: translation(left) and an off-center full rotation(right). Compare analytic interfaces against advection alone and simple redistancing. This is not a VOF calculation, and no area correction is applied.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [Run and validate: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en) (`level-set-translation`) · [Code ZIP: 2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

- [Run and validate: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en) (`level-set-rotation`) · [Code ZIP: 2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip)

Scope of this execution example: Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.




### Forced vorticity about a maintained shear layer

ID: `forced-vorticity` · local-example

$$
-\Delta\psi=\omega,\qquad (u,v)=(\psi_y,-\psi_x)
$$

$$
\omega_t+U(y)\omega_x+U^{\prime\prime}(y)\psi_x+u\omega_x+v\omega_y=\nu\Delta\omega
$$

$$
U(y)=\tanh(\sin y/\delta),\qquad \Omega_{\mathrm{total}}=-U^{\prime}(y)+\omega
$$

Explicit forcing maintains the analytic base shear; actual nonlinear2D dynamics evolve its perturbations. Pressure is eliminated. Distinguish this from sharp-interface infinite-domain or compressible KH dispersion.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/)

Fixed periodic[0,2pi]² initial-growth case,delta.25,nu.005,epsilon1e-5,32²/64²/128²,T1. Compare an independent Fourier–Galerkin linear IVP and separate timestep/amplitude probes; no late roll-up certification.

#### Related test problem figures and code

##### [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

![Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.

- [Run and validate: KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en) (`kh-initial-growth`) · [Code ZIP: KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Scope of this execution example: Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.




### Boussinesq vorticity with active buoyancy

ID: `boussinesq-buoyancy` · local-example

$$
-\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x),\quad b=b_0(y)+\theta
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+\theta_x
$$

$$
\theta_t+u\theta_x+v\theta_y+v b_0^{\prime}=\kappa\Delta\theta,\qquad b_0=.02\tanh(\sin y/\delta)
$$

Inertial density is constant; density contrast enters buoyancy only. Forcing maintains the base profile. The curl of vertical buoyancy yields theta_x; this is a perturbation Boussinesq system rather than variable-density Euler.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/)

Periodic[0,2pi]²,nu=kappa.005,delta.25,epsilon1e-5,32²/64²/128²,T2. Smooth double-layer initial growth is compared with an independent linear reference; no RT-turbulence or sharp-density-interface claim.

#### Related test problem figures and code

##### [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

![Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.

- [Run and validate: RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en) (`rt-initial-growth`) · [Code ZIP: RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Scope of this execution example: Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.




### ALE scalar conservation on moving cells

ID: `ale-scalar-transport` · local-example

$$
q_t+a q_x=0,\quad m_i(t)=\int_{x_{i-1/2}(t)}^{x_{i+1/2}(t)}q(x,t)\,dx
$$

$$
\dot m_i=-[(a-w)q]_{i-1/2}^{i+1/2},\qquad \dot V_i=w_{i+1/2}-w_{i-1/2}
$$

$$
x(\xi,t)=\xi+\frac{.2}{2\pi}\sin(2\pi\xi)\sin(2\pi t),\quad a=.7
$$

Prescribed nonuniform face positions and cell masses share Heun stages. Evaluate geometric conservation and nonuniform-wave transport separately; this is not an Euler-fluid Lagrange/remap scheme.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/)

Periodic unit interval,q0=1+.2sin(2pi x),N40/80/160,T1, plus constant-state GCL and fixed-N temporal refinement. Prescribed1D motion only; no Saltzman or general moving-mesh fluid claim.

#### Related test problem figures and code

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.

- [Run and validate: ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`) · [Code ZIP: ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Scope of this execution example: Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.




### Linear rotating shallow-water equations

ID: `linear-rotating-shallow-water` · local-example

$$
\eta_t+H(u_x+v_y)=0,\qquad u_t-fv=-g\eta_x,\qquad v_t+fu=-g\eta_y
$$

$$
g=H=f=1,\quad \widetilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2)
$$

$$
\omega_h^2=f^2C^2+gH(\widetilde k^2+\widetilde l^2)
$$

Actual2D staggered C-grid fields use RK4 on a planar linear f-plane. Separate continuous and semidiscrete references, checking mass,energy,inertial oscillation and discrete geostrophic balance.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/)

Periodic unit square,mode(1,2),height amplitude.01,N16/32/64,T.5, plus separate time refinement. No nonlinear shallow-water,spherical/global dynamics or Williamson test claim.

#### Related test problem figures and code

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.

- [Run and validate: Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`) · [Code ZIP: Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Scope of this execution example: Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.




### Variable-viscosity vector stress boundary-value problem

ID: `variable-viscosity-vector` · local-example

$$
-\nabla\cdot\boldsymbol\tau=\boldsymbol f,\quad \boldsymbol\tau=2\mu\boldsymbol\varepsilon(\boldsymbol u),\quad \boldsymbol\varepsilon(\boldsymbol u)=\tfrac12(\nabla\boldsymbol u+\nabla\boldsymbol u^T)
$$

$$
1<r<2,\quad \mu=1+r^2/5,\quad A=(r^2-1)(4-r^2),\quad \boldsymbol u_\star=A(1+xy,(x^2-y^2)/2)^T
$$

$$
\int_\Omega2\mu\,\boldsymbol\varepsilon(\boldsymbol u_h):\boldsymbol\varepsilon(\boldsymbol v_h)\,dA=\int_\Omega\boldsymbol f\cdot\boldsymbol v_h\,dA
$$

Linear stress-divergence BVP coupling two Cartesian components. Q1 basis functions in polar coordinates use the exact curved Jacobian and include variable-mu gradients and shear. There is no pressure,incompressibility constraint or advective term.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/)

Annulus1≤r≤2,zero Dirichlet on both circles,periodic theta,Nr8/16/32,Ntheta2Nr. Separately check velocity,strain,physical traction,work and nonzero net boundary force. No Navier–Stokes or general-quadrilateral certification.

#### Related test problem figures and code

##### [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.

- [Run and validate: Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en) (`annular-viscous-mms`) · [Code ZIP: Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Scope of this execution example: Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.




### Special-relativistic ideal MHD (SRMHD)

ID: `srmhd` · local-example

$$
\partial_\mu(\rho u^\mu)=0,\qquad \partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=(\rho h+b^2)u^\mu u^\nu+(p+b^2/2)\eta^{\mu\nu}-b^\mu b^\nu
$$

$$
\partial_t\boldsymbol B-\nabla\times(\boldsymbol v\times\boldsymbol B)=0,\quad \nabla\cdot\boldsymbol B=0,\quad h=1+\frac{\Gamma p}{(\Gamma-1)\rho}
$$

$$
K=\rho h+B_0^2(1+\eta_A^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta_A^2B_0^4}}
$$

Flat spacetime,ideal conductivity,gamma-law EOS,c=4pi=1; b^mu is the comoving magnetic four-vector. The1D solver evolves seven conserved variables with full magnetic stress and induction, using coupled RMHD Z recovery. Distinguish it from GRMHD.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/)

Nonlinear CP exact family rho=p=Bx=etaA1,gamma4/3,periodic unit interval,N64/128/256,one period. Check conserved means,phase,amplitude and stage physicality; no generic RMHD shocks,extreme magnetization/speeds or multidimensional divergence-control claim.

#### Related test problem figures and code

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.

- [Run and validate: SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) (`srmhd-alfven`) · [Code ZIP: SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Scope of this execution example: Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.




### Discontinuous and full-tensor diffusion BVP

ID: `tensor-diffusion` · local-example

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/)

#### Related test problem figures and code

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

- [Run and validate: Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`) · [Code ZIP: Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Scope of this execution example: Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.


##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

- [Run and validate: Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`) · [Code ZIP: Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Scope of this execution example: Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.




### Coulomb electrostatics with mixed periodic boundaries

ID: `coulomb-electrostatics` · local-example

$$
\phi(\boldsymbol r)=\sum_j\sum_{\boldsymbol n}^{\prime}\frac{q_j}{|\boldsymbol r-\boldsymbol r_j+\boldsymbol L\boldsymbol n|},\quad\boldsymbol F_i=-q_i\nabla\phi_i
$$

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V,\quad M_z=\sum_iq_iz_i
$$

Neutral system,Coulomb constant1. Distinguish genuine2P references from finite-vacuum3P plus correction.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-slab-ewald/)

#### Related test problem figures and code

##### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) (`neutral-slab-yb`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#code-en)

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

- [Run and validate: Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en) (`neutral-slab-yb`) · [Code ZIP: Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip)

Scope of this execution example: Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.




### Electrostatic Vlasov–Poisson equations

ID: `vlasov-poisson` · local-example

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/)

#### Related test problem figures and code

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

Poisson identifies the self-consistent electrostatic field; the registry does not list the complete coupled particle-motion/CIC PIC system.

- [Run and validate: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en) (`pic`) · [Code ZIP: Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Scope of this execution example: Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

- [Run and validate: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en) (`pic-conservation`) · [Code ZIP: PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Scope of this execution example: Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

- [Run and validate: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) (`pic-independent-spatial`) · [Code ZIP: Independently coded PIC spatial pipeline](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

Scope of this execution example: Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.


##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

- [Run and validate: Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) (`thermal-landau-damping`) · [Code ZIP: Warm PIC linear Landau damping](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Scope of this execution example: Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.


##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.

- [Run and validate: Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) (`thermal-two-stream`) · [Code ZIP: Warm PIC two-stream initial growth](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Scope of this execution example: Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.




### Hard-sphere Boltzmann transport,walls and reservoirs

ID: `hard-sphere-boltzmann` · local-example

$$
\partial_t f+v_x\partial_x f=Q_{\rm HS}(f,f)
$$

$$
\sigma=1/\sqrt2,\quad\lambda(n)=1/(\sqrt2n\sigma)
$$

1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/)

#### Related test problem figures and code

##### [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) (`dsmc-couette`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#code-en)

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

- [Run and validate: Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en) (`dsmc-couette`) · [Code ZIP: Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.


##### [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

- [Run and validate: Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en) (`dsmc-fourier`) · [Code ZIP: Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.


##### [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#code-en)

{"kind":"shock","cells":192,"length":16,"weight":0.005208333333333333,"dt":0.01,"burn_in":20,"sample_time":20,"blocks":5,"bins":64,"sample_every":10,"hist_velocity":[-4,7]} Twelve independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

- [Run and validate: Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`) · [Code ZIP: Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip)

Scope of this execution example: Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.




### Static grey radiative transfer,scattering and linear exchange

ID: `static-grey-transfer` · local-example

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/)

#### Related test problem figures and code

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.

- [Run and validate: Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`) · [Code ZIP: Isotropic scattering in a finite slab](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

Scope of this execution example: Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.


##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.

- [Run and validate: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) (`su-olson-transport1997`) · [Code ZIP: Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Scope of this execution example: Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.


##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Run and validate: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) (`shadow-absorber2d`) · [Code ZIP: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.


##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Run and validate: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) (`opposing-beams2d`) · [Code ZIP: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.




### Su–Olson1996 non-equilibrium diffusion and material exchange

ID: `non-equilibrium-diffusion-exchange` · local-example

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u-\frac{2}{\sqrt3}u_x=1\ (x=0),\quad \epsilon u+v\ \mathrm{is\ the\ weighted\ energy}
$$

x=sqrt(3)kappa*z,distinct from x=kappa*z in1997 transport. Boundary data and references remain separate; non-unit-epsilon closed cells are separate controls.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/)

#### Related test problem figures and code

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.

- [Run and validate: Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`) · [Code ZIP: Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Scope of this execution example: Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.




### Static grey M1 moments in flat spacetime

ID: `static-grey-m1` · local-example

$$
E_t+\nabla\cdot\boldsymbol F=-\kappa E+S_E,\quad\boldsymbol F_t+\nabla\cdot\mathsf P=-\kappa\boldsymbol F+\boldsymbol S_F
$$

$$
\mathsf P=E[(1-\chi)\mathsf I_3/2+(3\chi-1)\boldsymbol n\boldsymbol n^T/2]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\boldsymbol F|/E
$$

c=1,2D space with full3D pressure including Pzz. Separate isotropic/vacuum branches,closed-PDE MMS and beam defects against angular transport; no relativistic-fluid claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/)

#### Related test problem figures and code

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Run and validate: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) (`shadow-absorber2d`) · [Code ZIP: Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.


##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Run and validate: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) (`opposing-beams2d`) · [Code ZIP: Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Scope of this execution example: Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.




### Scalar Ito diffusion: GBM and OU

ID: `scalar-ito-diffusion` · local-example

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

Scalar SDEs with deterministic initial states. Separate weak moment bias,strong errors on shared Brownian paths and finite-sample MCSE. OU is a related bath-component check,not the full harmonic Langevin system.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/)

#### Related test problem figures and code

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

Geometric-Brownian Itô SDE dX=μXdt+σXdW; no SDE-specific entry exists among the 46 equations.

- [Run and validate: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) (`gbm-sde`) · [Code ZIP: Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Scope of this execution example: Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [Run and validate: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en) (`gbm-weak-moments`) · [Code ZIP: GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

- [Run and validate: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en) (`gbm-milstein-strong`) · [Code ZIP: Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.


##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

![Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

The Hamiltonian link identifies the harmonic mechanical part; the calculations add friction/noise or a CSVR heat bath.

- [Run and validate: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en) (`langevin-harmonic`) · [Code ZIP: Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Scope of this execution example: Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

- [Run and validate: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en) (`csvr-langevin-harmonic`) · [Code ZIP: CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

- [Run and validate: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en) (`ou-weak-moments`) · [Code ZIP: OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Scope of this execution example: Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.




### Gaussian probability measures: tails and correlated targets

ID: `gaussian-probability-model` · local-example

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/)

#### Related test problem figures and code

##### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en) (`normal-tail-importance`)

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#code-en)

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.

- [Run and validate: Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en) (`normal-tail-importance`) · [Code ZIP: Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

Scope of this execution example: Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.


##### [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en) (`correlated-gaussian-mcmc`)

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en#code-en)

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.

- [Run and validate: Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en) (`correlated-gaussian-mcmc`) · [Code ZIP: Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

Scope of this execution example: Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.




### Finite-dimensional linear systems and factorizations

ID: `finite-dimensional-linear-system` · local-example

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)

SPD tridiagonal, nearly singular rank-one, Hilbert 5 and Wilkinson 12 matrices, plus saddle velocity sizes 12 and 24. Residual, forward error and backward error are separate quantities.

#### Related test problem figures and code

##### [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`)

![The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#code-en)

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.

- [Run and validate: Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`) · [Code ZIP: Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.


##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.

- [Run and validate: Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`) · [Code ZIP: Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.


##### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`)

![Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#code-en)

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

- [Run and validate: Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`) · [Code ZIP: Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

Scope of this execution example: Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.




### Finite-dimensional matrix eigenproblems

ID: `finite-dimensional-eigenproblem` · local-example

$$
A x=\lambda x
$$

The primary case is a fixed 31 x 31 symmetric standard eigenproblem. Its discrete spectrum provides the reference; continuum PDE spatial convergence is not claimed.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)

Restart lengths 8 and 16, at most 40 cycles, shifts none/0/950, and an original eigenpair residual tolerance of 1e-9.

#### Related test problem figures and code

##### [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) (`restarted-shift-invert`)

![The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#code-en)

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.

- [Run and validate: Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en) (`restarted-shift-invert`) · [Code ZIP: Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.




### Fixed-end string eigenvalues and consistent-mass FEM

ID: `dirichlet-string-eigenproblem` · local-example

$$
-T\phi^{\prime\prime}=\rho\lambda\phi,\quad 0<x<1
$$

$$
\phi(0)=\phi(1)=0,\quad T=\rho=1
$$

$$
\lambda_j=(j\pi)^2
$$

$$
\lambda_{j,h}=\frac{6(1-\cos\theta_j)}{h^2(2+\cos\theta_j)},\quad\theta_j=\frac{j\pi}{n+1}
$$

A unit-string normal-mode eigenproblem separates consistent-mass P1 algebraic error from continuum discretization error. No time evolution is performed.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)

Use 15, 31 and 63 interior nodes. Compare M-inner-product Krylov and actual SciPy 1.14.1 LOBPCG with closed discrete eigenvalues and generalized LAPACK.

#### Related test problem figures and code

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.

- [Run and validate: Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) (`fem-mass-eigen`) · [Code ZIP: Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Scope of this execution example: Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.




### Linear Maxwell fields in vacuum and dielectrics

ID: `maxwell` · local-example

$$
\partial_t\mathbf B=-\nabla\times\mathbf E,\quad\partial_t\mathbf D=\nabla\times\mathbf H
$$

$$
\mathbf D=\varepsilon(\mathbf x)\mathbf E,\quad\mathbf B=\mathbf H
$$

The representative equations describe three-dimensional linear electromagnetics. This implementation is restricted to a z-invariant, genuinely two-dimensional Yee cylinder problem with Ez/Hx/Hy.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-cylinder/)

The cylinder uses s = Ez, often called TMz, with Hz = 0. Components distinguish it from p = Hz, often called TEz, with Ez = 0; naming conventions vary across the literature.

#### Related test problem figures and code

##### [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en) (`cylinder-mie2d`)

![Real part of the actual saved scattered electric phasor on the finest two-dimensional grid. The central white region is a diagnostic mask at r<0.4, distinct from the physical cylinder radius0.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#code-en)

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.

- [Run and validate: Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en) (`cylinder-mie2d`) · [Code ZIP: Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

Scope of this execution example: Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.




### Passive Lorentz–Ohmic Maxwell fields

ID: `maxwell-lorentz` · local-example

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-lorentz/)

The s mode evolves Ez/Hx/Hy and Pz/Jz. The p mode evolves Hz/Ex/Ey and both Px/Py/Jx/Jy material responses. This does not implement arbitrary three-dimensional fields or arbitrary transverse multimode data.

#### Related test problem figures and code

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`)

![Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#code-en)

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.

- [Run and validate: Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`) · [Code ZIP: Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

Scope of this execution example: Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.


##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`)

![Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#code-en)

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.

- [Run and validate: Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`) · [Code ZIP: Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

Scope of this execution example: Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.




### Finite-dimensional nonlinear maps, roots and differential actions

ID: `finite-dimensional-nonlinear-map` · local-example

$$
F:\mathbb R^n\longrightarrow\mathbb R^m
$$

$$
F(x)=0\quad(m=n\text{ for root controls})
$$

$$
J(x)v=DF(x)[v],\quad J(x)^\top w
$$

$$
H_f(x)v=D(\nabla f)(x)[v]\quad(f\text{ twice differentiable})
$$

Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-reverse-higher-ad/)

Fixed Rosenbrock/small-Bratu globalization, rectangular repeated-gather/broadcast maps, fixed-state HVPs, positive implicit rules and literal stopping conventions.

#### Related test problem figures and code

##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`)

![Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`) · [Code ZIP: Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

Scope of this execution example: Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.


##### [Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`)

![Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`) · [Code ZIP: Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

Scope of this execution example: Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.


##### [Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en) (`hessian-vector-products`)

![Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en) (`hessian-vector-products`) · [Code ZIP: Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

Scope of this execution example: Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.


##### [Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en) (`kink-branch-derivatives`)

![Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en#code-en)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Run and validate: Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en) (`kink-branch-derivatives`) · [Code ZIP: Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip)

Scope of this execution example: Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.




### Finite-dimensional algebraic optimization and known minima

ID: `finite-dimensional-optimization` · local-example

$$
\min_{x\in\mathbb R^n} f(x)
$$

$$
\nabla f(x_*)=0\quad\text{(necessary for a smooth unconstrained local minimum)}
$$

$$
f_Q(x)=\tfrac12(x-x_*)^TA(x-x_*),\quad A=A^T>0
$$

$$
f_R(x,y)=100(y-x^2)^2+(1-x)^2
$$

Dimensionless algebraic optimization of an eight-dimensional SPD quadratic and a two-variable Rosenbrock function. There is no physical spatial domain or PDE boundary; compare known minima and local iterative actions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-inverse-optimization/)

Known minima, gradients, Wolfe/curvature ledgers, and a dense reference using only the current last three pairs and current gamma0 I.

#### Related test problem figures and code

##### [BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`)

![Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#code-en)

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.

- [Run and validate: BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`) · [Code ZIP: BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

Scope of this execution example: An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.




### Robertson chemical kinetics

ID: `robertson-kinetics` · local-example

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=0.04y_1-10^4y_2y_3-3\times10^7y_2^2,\quad\dot y_3=3\times10^7y_2^2
$$

$$
y_1+y_2+y_3=1
$$

Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)

Fixed three-species Robertson examples cover a short-time ODE and a conservation DAE on a prescribed coarse schedule. The DAE unmet temporal accuracy/refinement targets remain visible.

#### Related test problem figures and code

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

- [Run and validate: Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`) · [Code ZIP: Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

- [Run and validate: Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) (`robertson-conservation-dae`) · [Code ZIP: Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Scope of this execution example: Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.




### Van der Pol oscillator

ID: `van-der-pol` · local-example

$$
\dot x=v,\qquad\dot v=\mu(1-x^2)v-x
$$

Compare work and error for fixed mu values over a short interval; this does not validate a full relaxation cycle.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)

#### Related test problem figures and code

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

- [Run and validate: Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`) · [Code ZIP: Van der Pol: an early stiffness transition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.




### Finite-dimensional linear evolution systems

ID: `linear-evolution-system` · local-example

$$
\dot y=Ay+b
$$

Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)

#### Related test problem figures and code

##### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) (`rk45-dense-events`)

![Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#code-en)

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

- [Run and validate: RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en) (`rk45-dense-events`) · [Code ZIP: RK45: embedded errors, dense output and events](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.


##### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`)

![Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#code-en)

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

- [Run and validate: Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`) · [Code ZIP: Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip)

Scope of this execution example: Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.




### Linear reaction-diffusion with inhomogeneous boundaries

ID: `inhomogeneous-reaction-diffusion` · local-example

$$
u_t=u_{xx}+u,\quad0<x<1,\quad u(0,t)=u(1,t)=1
$$

Separate temporal errors relative to the same nonperiodic finite-difference system from spatial errors relative to the continuous exact family.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/)

#### Related test problem figures and code

##### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`)

![Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#code-en)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

- [Run and validate: Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`) · [Code ZIP: Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.




### Semi-explicit index-one DAE

ID: `index-one-dae` · local-example

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/)

#### Related test problem figures and code

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

- [Run and validate: Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`) · [Code ZIP: Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Scope of this execution example: Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

- [Run and validate: Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) (`robertson-conservation-dae`) · [Code ZIP: Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Scope of this execution example: Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.


##### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`)

![Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#code-en)

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

- [Run and validate: Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`) · [Code ZIP: Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Scope of this execution example: Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.




### Constrained planar pendulum

ID: `constrained-pendulum` · local-example

$$
\dot q=p,\quad\dot p=(0,-1)-\lambda q,\quad q^Tq=1,\quad q^Tp=0
$$

Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/)

#### Related test problem figures and code

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

- [Run and validate: Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) (`high-index-pendulum`) · [Code ZIP: Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Scope of this execution example: Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

- [Run and validate: SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en) (`shake-rattle-pendulum`) · [Code ZIP: SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.




### Kepler two-body problem

ID: `kepler-two-body` · local-example

$$
\dot q=p,\qquad\dot p=-q/\|q\|^3,\qquad H=\tfrac12p^Tp-1/\|q\|
$$

Nondimensional planar ellipses separate phase, angular momentum, energy and step-selection effects.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)

#### Related test problem figures and code

##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Run and validate: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) (`gravity-kepler`) · [Code ZIP: Unsoftened Kepler two-body time error](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Scope of this execution example: Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

- [Run and validate: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en) (`kepler-eccentricity`) · [Code ZIP: Kepler eccentricity and time-step controls](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.




### Coupled two-frequency harmonic oscillators

ID: `coupled-harmonic-oscillators` · local-example

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+q_1q_2
$$

Separate continuous normal modes, the ideal split map, a map with stored floating-point coefficients, and repeated rounded updates.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)

#### Related test problem figures and code

##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

- [Run and validate: Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) (`multifrequency-resonance`) · [Code ZIP: Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Scope of this execution example: A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.




### Finite, improper and multivariate definite integrals

ID: `definite-integrals` · local-example

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quadrature-controls/)

#### Related test problem figures and code

##### [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`)

![Saved active Fourier contributions and actual errors/call counts The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 25 met, 2 unmet and 3 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#code-en)

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

- [Run and validate: QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`) · [Code ZIP: QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Scope of this execution example: Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.


##### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) (`gk15-double-exponential`)

![Saved transformed integrands and finite-window defects; continuous tails are distinct The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#code-en)

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

- [Run and validate: G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en) (`gk15-double-exponential`) · [Code ZIP: G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Scope of this execution example: Nine adaptive GK rows and twenty-four fixed DE sums are compared.


##### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`)

![Actual two-dimensional nodes and signed integration weights The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#code-en)

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

- [Run and validate: Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`) · [Code ZIP: Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Scope of this execution example: Forty-two fixed cubatures compare a smooth product and an interaction product.




### Polynomial interpolation on stored nodes

ID: `polynomial-interpolation` · local-example

$$
P_n(x_j)=y_j,\quad P_n\in\mathcal P_n
$$

$$
R(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)}
$$

Separate closed-weight representation on rounded nodes, interpolation error and evaluation rounding.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/)

#### Related test problem figures and code

##### [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`)

![Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#code-en)

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

- [Run and validate: Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`) · [Code ZIP: Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Scope of this execution example: Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.




### Cubic splines and shape-preserving interpolation

ID: `cubic-spline-pchip` · local-example

$$
S_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3
$$

$$
S\in C^2\ \text{for the natural/clamped spline};\quad P\in C^1\ \text{for PCHIP}
$$

Distinguish C2 interpolation with endpoint conditions from monotone piecewise Hermite interpolation.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/)

#### Related test problem figures and code

##### [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en) (`spline-shape-controls`)

![Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#code-en)

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

- [Run and validate: Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en) (`spline-shape-controls`) · [Code ZIP: Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Scope of this execution example: Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.




### Discrete Haar transforms of finite signals

ID: `discrete-haar-transform` · local-example

$$
\binom{a^{\prime}}d=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom ab
$$

$$
S_NA_N=I_N,\quad\|A_Nx\|_2^2=\|x\|_2^2+\sum_\ell p_\ell^2
$$

A finite map including odd-length padding and cropping; global orthogonality is not assumed for redundant extensions.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/)

#### Related test problem figures and code

##### [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`)

![Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays. Sample indices are not physical spatial coordinates. This is a finite-signal map with declared boundary handling.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#code-en)

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

- [Run and validate: Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`) · [Code ZIP: Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Scope of this execution example: Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.




### Closed SEIR compartment model

ID: `seir-compartment` · local-example

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
S+E+I+R=1
$$

Educational rates with no births or deaths and constant population. Compare the early transient with a full two-by-two matrix exponential; no disease forecast is made.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-small-models/)

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.

#### Related test problem figures and code

##### [SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en) (`seir-linearization`)

![Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en#code-en)

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

- [Run and validate: SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en) (`seir-linearization`) · [Code ZIP: SEIR conservation and initial linearization](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Scope of this execution example: Check population conservation and the full two-mode initial linearization separately.




### Two-state electronic-angle/nuclear BO and CP-type model

ID: `two-state-bo-cp-model` · local-example

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

#### Related test problem figures and code

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

![Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

- [Run and validate: A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) (`two-state-bo-cp-ou`) · [Code ZIP: A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.




### Unrestricted HF in a minimal two-electron model

ID: `unrestricted-hartree-fock-model` · local-example

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/)

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

#### Related test problem figures and code

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Run and validate: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP: H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Scope of this execution example: Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

- [Run and validate: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en) (`h2-rhf-uhf-fci`) · [Code ZIP: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.




### Three-wave nonlocal kernel and mean Fermi occupations

ID: `finite-projector-fermi-model` · local-example

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/)

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

#### Related test problem figures and code

##### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) (`finite-projector-fermi`)

![Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#code-en)

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

- [Run and validate: A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en) (`periodic-projector-occupations`) · [Code ZIP: A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Scope of this execution example: Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.




### Immigration–death reaction and exact transient law

ID: `immigration-death-model` · local-example

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

#### Related test problem figures and code

##### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) (`immigration-death-ssa`)

![Separate one displayed path from12,288fixed ensemble paths. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#code-en)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

- [Run and validate: Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en) (`immigration-death-ssa`) · [Code ZIP: Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

Scope of this execution example: Separate one displayed path from12,288fixed ensemble paths.




### Forced advective Keller–Segel manufactured problem

ID: `forced-keller-segel-model` · local-example

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

$$
n_*=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y)
$$

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-space-controls/)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

#### Related test problem figures and code

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

![Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

- [Run and validate: Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`) · [Code ZIP: Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Scope of this execution example: Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.




### Two-mode deterministic thermostat model

ID: `finite-mode-thermostat-model` · local-example

$$
U(q)=\sum_{i=1}^2(\omega_i^2q_i^2/2+\kappa q_i^4/4),\quad\omega=(1,1.7),\ \kappa=0,.2
$$

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostat-constraint-controls/)

Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas.

#### Related test problem figures and code

##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

![Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

The Hamiltonian link identifies the anharmonic mechanical part; validation concerns distributions with added stochastic CSVR/Langevin heat baths.

- [Run and validate: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en) (`csvr-langevin-quartic`) · [Code ZIP: Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip)

Scope of this execution example: Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

- [Run and validate: NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en) (`deterministic-thermostat-contrasts`) · [Code ZIP: NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

Scope of this execution example: Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.




### Canonical momentum under fixed linear constraints

ID: `projected-canonical-model` · local-example

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostat-constraint-controls/)

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.

#### Related test problem figures and code

##### [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en) (`projected-canonical-dof`)

![Separate effectiveDOF,momentum covariance,transient distributions and time correlations. These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#code-en)

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.

- [Run and validate: Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en) (`projected-canonical-dof`) · [Code ZIP: Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

Scope of this execution example: Separate effectiveDOF,momentum covariance,transient distributions and time correlations.




### Prescribed scalar advection on a sphere

ID: `sphere-scalar-advection` · local-example

$$
q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r)
$$

$$
\mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)
$$

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/)

#### Related test problem figures and code

##### [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`)

![Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#code-en)

- [Run and validate: Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`) · [Code ZIP: Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Scope of this execution example: Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.




### Axisymmetric spherical shallow-water subproblem

ID: `spherical-shallow-water` · local-example

$$
h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0
$$

$$
v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0
$$

$$
u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi
$$

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/)

#### Related test problem figures and code

##### [Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en) (`sphere-zonal-balance`)

![NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en#code-en)

- [Run and validate: Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en) (`sphere-zonal-balance`) · [Code ZIP: Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Scope of this execution example: NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.




### Static grey VEF/VET moment closure

ID: `static-grey-variable-eddington-moments` · local-example

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_t I=\sigma_s E+q,\quad E=\langle I\rangle
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf D E)=0
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{\langle I\rangle},\quad\sigma_a=\sigma_t-\sigma_s
$$

c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries.

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/)

#### Related test problem figures and code

##### [Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`)

![Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#code-en)

- [Run and validate: Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`) · [Code ZIP: Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

Scope of this execution example: Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.


##### [Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`)

![Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

[Code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#code-en)

- [Run and validate: Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`) · [Code ZIP: Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

Scope of this execution example: Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.
