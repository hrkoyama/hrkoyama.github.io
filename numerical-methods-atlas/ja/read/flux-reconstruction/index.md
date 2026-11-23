# Flux Reconstruction法：流束補正とDG・1D周期移流

Flux Reconstruction法：流束補正とDG・1D周期移流

Flux Reconstruction（FR、流束再構成）は、要素ごとに持つ流束多項式へ界面の補正を加え、高次の保存則離散化を構成する枠組みです。要素間で解を連続にする代わりに数値流束で情報を交換します。補正関数の選び方が手法を決めるため、FRという名前だけで精度や安定性は決まりません。

解点・界面の数値流束を分ける


$$
u_t+a u_x=0,\quad x\in[0,1),\quad u(x+1,t)=u(x,t),\quad u_*(x,t)=0.4+\sin(2\pi(x-at))
$$

$$
u_h(\xi)=\sum_{j=0}^{p}u_j\ell_j(\xi),\qquad f^D(\xi)=\sum_{j=0}^{p}f(u_j)\ell_j(\xi)
$$
各区間をξ∈[−1,1]へ写し、p+1個の解点に値を置きます。要素内の多項式を左右端へ外挿すると、隣の要素と異なる二つの値が得られます。今回の一定速度ではa>0なら左側、a界面値を補正関数でつなぐ


$$
f^C(\xi)=f^D(\xi)+(f_L^*-f_L^D)g_L(\xi)+(f_R^*-f_R^D)g_R(\xi)
$$

$$
g_L(-1)=1,\ g_L(1)=0,\qquad g_R(-1)=0,\ g_R(1)=1,\qquad\dot u_i=-\frac{2}{h}\partial_\xi f^C(\xi_i)
$$
fDは要素内で作る流束、f*は界面の共有数値流束です。左右の差をgL・gRで内部へ配ると、補正した流束は端点でf*に一致します。その微分を解点で評価して時間発展させます。MUSCLやWENOの「再構成」と関連する語ですが、ここで構成している多項式・自由度・補正の対象を区別します。

Radau補正でDGを再現する設定


$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\qquad g_R=\frac12(P_p+P_{p+1})
$$

$$
M\dot{\mathbf u}=\frac{2}{h}\left[aD^TM\mathbf u-\mathbf t_R f_R^*+\mathbf t_L f_L^*\right],\qquad M=\operatorname{diag}(w_i)
$$
今回の解点はGauss点、補正は上式のRadau型です。MはGauss重みの対角行列、tL・tRは解点から端点への外挿ベクトル、Dは参照微分行列。この線形流束・アフィン区間の設定では、補正式は節点DGの弱形式に対応します。DG側をLegendre modal係数で表しても、同じ初期射影・流束・時間積分なら同じ多項式を表します。非線形流束のaliasing、別の求積や補正関数では条件を改めて確認する必要があります。

既存DG法との比較



既存DG法との比較

| 比較点 | 今回のFR | 既存のmodal DG |
| --- | --- | --- |
| 保持する自由度 | p+1個のGauss点の値 | p+1個のLegendre係数 |
| 要素の接続 | 共有流束との差をRadau関数で補正 | 弱形式の体積項と面流束 |
| 初期化 | 共通のGauss積分でL2射影 | 同じ射影規約 |
| 時間積分 | SSPRK(3,3) | 同じSSPRK(3,3)・刻み規約 |
| 今回の比較の意味 | 線形問題での対応を数値で確認 | 独立に既存コードを実行して照合 |
| 一般化の限界 | 全補正・非線形FRの保証ではない | 全DG変種との同値性ではない |

軽量実行例：周期正弦波を1/4周期だけ運ぶ

初期値0.4+sin(2πx)、速度1、T=.25。p=1/2、8/16/32セルを実行します。既存のDG関数をバイト一致で同梱し、各設定で実際に計算します。hを細分化する際はスケールしたCourant数(2p+1)|a|Δt/h≤.15にします。終了時の波は初期位置から移動しており、静止した初期図を成功例として使いません。

[](/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)保存された初期・最終場と判定。DGとの差と質量変化の軸は10⁻¹⁵程度の丸め誤差の大きさを表示しています。保存・散逸と時間誤差を別々に測る


$$
I_h=\sum_e\frac{h}{2}\sum_iw_iu_{e,i},\quad \frac{dI_h}{dt}=0,\qquad \frac{d}{dt}\frac12\|u_h\|_{L^2}^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$
Ihの共有面流束は周期境界で打ち消し合います。上流流束の半離散エネルギーは界面の跳びに応じて散逸します。これは任意の時間刻みでの安定性や、非線形のエントロピー安定性を保証する式ではありません。本例では全RK段階の質量と、完了した各ステップのエネルギーも測定します。


$$
\dot U=A_hU,\quad U_{\exp}(T)=\exp(TA_h)U(0),\quad E_t=\|U_{\rm RK3}(T)-U_{\exp}(T)\|_M
$$
連続L2誤差は追加のGauss点で積分します。hとΔtを同時に細分化した観測次数はp1で約1.99、p2で約3.00。FRと実際の既存DGの最大差は約4.0×10⁻¹⁵、最大段階質量変化は約3.6×10⁻¹⁵でした。

同じ空間演算子の指数作用を別の時間伝播器として計算し、RK3の時間誤差を分けます。p2/N32の時間誤差は約9.44×10⁻⁹、刻み半減では約1.18×10⁻⁹（比約.125）でした。この指数作用は独立した空間PDEソルバーではありません。初回の密行列指数の警告とJSON型変換の失敗は入力・元ソース・結果とともに保持し、数値受入条件を変更せず修正しています。

関連実装：PyFRと今回の適用範囲

[PyFR](https://www.pyfr.org/)はFRを使う流れのソフトウェアで、非構造格子やCPU/GPU向けの実装を紹介しています。公式資料と[公式ソース](https://github.com/PyFR/PyFR)へ進めます。今回の小さなPython例はPyFR本体の導入・実行・ベンチマークではありません。非線形流束、衝撃波、制限器、一般の補正族、曲線格子、多次元FRは別の検証が必要です。

[既存の不連続Galerkin法](/numerical-methods-atlas/methods/dg/?lang=ja) · [連続なスペクトル要素法との違い](/numerical-methods-atlas/ja/read/spectral-element/)

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### FR法の1D周期移流：Radau補正と既存DGの比較

固定標的の計算例

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。

このRadau/Gauss・線形一定流束・アフィン要素の設定がDGに対応します。全FRと全DGの同値性、非線形流束・衝撃波・制限器・多次元FRは保証しません。hとΔtの同時細分化と行列指数による空間誤差を分け、行列指数を独立した空間PDEソルバーとは呼びません。PyFR本体は未実行。

[入力・結果・受入条件](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-sem-fr/#fr-periodic-advection) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py) · [コード fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) · [コード polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py) · [コード advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py) · [コード riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py) · [コード equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py) · [コード limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py) · [コード sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) · [コード fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py) · [コード krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py) · [テスト test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py) · [ZIP](/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [結果](/code/validated-examples/2026-11-23/sem-fr/results/result.json) · [追試記録](/code/validated-examples/2026-11-23/sem-fr/verification.json)

## 公開範囲

この章に対応する専用の軽量コード・固定入力・保存場・判定と、ZIP独立展開で再実行した25検査を公開します。関連する外部ソフトは公式資料の紹介であり、導入・動作検証済みの表示ではありません。

## 文献

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://doi.org/10.2514/6.2007-4079
- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf
- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/
