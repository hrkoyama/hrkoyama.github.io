# 分野ごとの小規模実装・検証をたどる

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## AMG・行列分解・固有値・求積

- [行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja): 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。
**使用手法**

- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-algorithm)

各行の最大非対角係数に対する相対強度からグラフを作り、貪欲な星型集約と余剰節点の隣接集約への付着で暫定補間Tを作ります。P=(I−ωD⁻¹A)T、ω=4/(3ρ̄)、ρ̄はD⁻¹Aの絶対行和上界です。粗演算子はPᵀAP。前後2回のJacobi平滑化と最終小行列の直接解を用います。これは採用した小規模SA変種であり、原著の全構築法や収束定理の再現ではありません。

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![行列から粗視化するAMG：残差と解誤差を分ける：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-validation)

正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja): 実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。
**使用手法**

- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja) (`qr-svd`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja#qr-svd-factorization-ja-algorithm)

Householder反射を左から蓄積してRを上三角化し、Qを構成します。Jacobi SVDは列対の内積を小さくする直交回転を繰り返し、回転した列の長さを特異値とします。AᵀAを作って固有値を求める方法ではありません。最小二乗はQRの後退代入、階数落ちでは打切りSVDで求めます。

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Householder QRと片側Jacobi SVD：直交性・階数・最小二乗：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) (`matrix-factorization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja#qr-svd-factorization-ja-validation)

QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja): 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。
**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja#krylov-eigenvalues-ja-algorithm)

Lanczosの3項漸化式に2回の全再直交化を加え、Arnoldiは修正Gram–Schmidtを2回行います。小さな射影行列T/HだけをNumPyのeigh/eigで解き、元空間へRitzベクトルを戻します。大きな元行列の密固有値計算は参照側だけで使います。

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Lanczos・Arnoldi：Ritz値と固有対残差の収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja#krylov-eigenvalues-ja-validation)

||Av−λv||₂、独立密行列固有値との差、基底の直交性を保存し、Krylov次元を増やした末尾の改善を確認します。非対称Ritz値の単調収束は仮定しません。恒等行列のhappy breakdown、零初期ベクトル拒否、次元予算不足も検査します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja): Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。
**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja#gauss-adaptive-quadrature-ja-algorithm)

Golub–Welschで対称Jacobi行列の固有値を節点、最初の固有ベクトル成分の平方の2倍を重みとします。適応Simpsonは区間を二分し、|S左+S右−S全|/15を局所推定として公差を配分します。評価回数と深さの上限を持ち、未達を成功としません。

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja#gauss-adaptive-quadrature-ja-validation)

全指定次数の多項式モーメント、SciPy roots_legendreの節点・重みとの差、解析exp積分の次数収束、解析atan積分とSciPy quadへの一致を測ります。公差を厳しくしたときの評価数と誤差を示し、5評価の強制予算切れ、非有限関数値も検査します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## MCMC・温度制御・生物モデル

- [Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja): 32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。
**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-algorithm)

log受理比でMetropolis更新。FFTによる連鎖内自己共分散を平均し、Geyerのgamma0+gamma1から始まる初期正ペア和から平均観測量のESSを求めます。古典的split-Rhatも併記します。

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Gaussian標的のMCMC：分布・自己相関・ESS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja) (`gaussian-mcmc`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-validation)

正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja): 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。
**使用手法**

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-algorithm)

力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Langevin温度制御：正準分布・刻み偏り・時間相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-validation)

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照 · 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja): 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-algorithm)

周期中心2階差分と独自RK4で進めます。空間系列は小さな同一時間刻み、時間系列は同じ空間演算子を用います。

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![反応拡散：空間2次と時間4次を分けて測る：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-validation)

連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja): Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-algorithm)

独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Turing不安定性：線形成長率と小振幅パターン：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-validation)

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja): 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。
**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-algorithm)

独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-validation)

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 粒子・静電場・運動論・放射輸送

- [中性周期セルのEwald和と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja): 3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。
**使用手法**

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) (`ewald`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja#ewald-ja-algorithm)

erfcで減衰する実空間和、Gaussian係数を持つ構造因子の逆格子和、−alpha/sqrt(pi) sum(q²)を加えます。力は各項の位置微分から求め、24成分を中心エネルギー差分と比較します。

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![中性周期セルのEwald和と独立theta積分：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja#ewald-ja-validation)

分割alphaを3点、実空間打切りを3点、逆空間打切りを4点で確認。NaClのMadelung定数は3次元和を呼ばない独立な1次元Jacobi-theta積分と照合し、求積の誤差推定も保存します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Bスプラインsmooth PMEの格子・次数収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja): 電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。
**使用手法**

- [Particle Mesh Ewald（PME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja) (`pme`)
- [Smooth PME（SPME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja) (`spme`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-algorithm)

4次または6次のcardinal Bスプラインのテンソル積で電荷を格子化し、節点スプラインの離散構造因子補正、Gaussian Green関数、3次元FFTを組み合わせます。格子エネルギーを重みの位置微分で解析的に微分します。

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Bスプラインsmooth PMEの格子・次数収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-validation)

16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja): 自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。
**使用手法**

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) (`fmm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja#fmm-ja-algorithm)

葉でP2M、上向きのM2M、相互作用リスト上のM2L、下向きのL2L、局所多項式の評価と近接P2Pを実装します。遠方を粒子ごとに開くBarnes–Hutへ置き換えず、移動演算回数と近接対数を記録します。

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![2次元対数核のM2M・M2L・L2Lを持つFMM：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) (`logarithmic-particles`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja#fmm-ja-validation)

固定seedの128粒子で次数2・4・8・12を走査し、別の全対直接和とポテンシャル・電場の全成分を照合します。2点の符号、順序不変性、ポテンシャル微分も検査します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja): 1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。
**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja#pic-ja-algorithm)

CIC電荷割当てと同じ重みの場補間、ゼロ平均のスペクトルPoisson解、速度Verletを組み合わせます。実数の奇微分の規約により、電場のNyquistモードはゼロにします。

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CIC静電PICの冷たいプラズマ振動：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja#pic-ja-validation)

32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照 · 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。
- [等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja): 等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。
**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-algorithm)

対の重心速度と相対速度の大きさを保持し、相対速度の方向を球面上で一様に選びます。roundは物理時刻ではなく衝突演算の回数です。 D=<vx²−(vy²+vz²)/2>と置くと、ランダムな相方の平均で重心の異方性が(N−2)/(2(N−1))倍になり、散乱後の相対方向の異方性期待値はゼロになるため、保存した期待減衰率が得られます。

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![等質DSMC衝突成分の保存則・Maxwell分布：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) (`maxwell-collisions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-validation)

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja): 純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-algorithm)

正のGauss–Legendre離散方向と1次風上有限体積の空間行進を使います。角度誤差だけを分ける系列では、一定セル内を指数関数で正確に伝播します。

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![純吸収平板の離散座標放射輸送：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) (`absorbing-slab`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-validation)

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 流体・MHDの独立照合とCT／GLM

- [Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja): 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。
**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-algorithm)

公開済みの1次Rusanov/前進Eulerを再利用。CTは共有corner EMFの離散curl、GLMはcell中心Bと双曲・放物型cleaning。Athena++は別実装のHLLD+PLM+RK2。

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Orszag–Tang：CT・GLMと独立Athena++比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-validation)

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照 · 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
- [Brio–Wu：別実装HLLDとの照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja): 公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。
**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-algorithm)

アトラス側はMC再構成とSSPRK2、参照は独立C++のHLLD・PLM・RK3。異なる実装ですがHLLDという数値流束の系列は共有します。

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Brio–Wu：別実装HLLDとの照合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) (`brio-wu`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-validation)

128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Shu–Osher：独立参照と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja): 衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。
**使用手法**

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-algorithm)

アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Shu–Osher：独立参照と格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-validation)

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [GLMの磁気単極子モード：解析的減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja): GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。
**使用手法**

- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-algorithm)

∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![GLMの磁気単極子モード：解析的減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-validation)

16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## CSVRとLangevin：分布・揺らぎ・相関

- [CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja): 自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。
**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-algorithm)

平方完成した厳密CIR遷移を、標準正規Rと独立χ²(Nf−1)のSから作ります。同じRでglobal αの符号を決め、Nf=1ではS=0。単位方向と新しい半径からpを再構成し、極小KでKnew/Kを作りません。K=0は方向が未定義として拒否します。

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-validation)

条件付き平均・分散は独立なCIR式、CDFの3確率点はSciPyの非心χ²分位点、定常KはGamma分布、浴単独ACFはexp(−t/τ)と照合。無雑音の平均緩和は分散を失う対照として別表示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja): 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。
**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-algorithm)

両方式とも厳密な浴O(h/2)–velocity-Verlet–O(h/2)（OBABO）。CSVRは全運動量に同じ係数、Langevinは各成分に独立OU雑音を作用。γ=1/(2τ)で自由浴のK緩和時間をそろえます。以前のBAOAB例は変更せず別の分割として残します。

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CSVRとLangevin：調和2自由度の分布・揺らぎ・相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-validation)

正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照 · 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja): 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。
**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-algorithm)

同じOBABO分割でglobal CSVRとlocal OUを比較。正準初期座標はGaussianを包絡にした独立棄却法、運動量はMaxwell分布から生成し、別の温度摂動初期集団も進めます。

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![非調和CSVRとLangevin：Boltzmann求積との分布比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-validation)

座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 非線形反応拡散・パターン形成の独立検証

- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja): t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) (`implicit-midpoint`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-algorithm)

二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Schnakenberg有限振幅過渡：非線形性と独立参照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-validation)

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja): t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) (`implicit-midpoint`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja#schnakenberg-pattern-ja-algorithm)

二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Schnakenberg飽和パターン：近定常性と格子・時間収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja#schnakenberg-pattern-ja-validation)

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 多峰性MCMC：混合不良と収束診断の独立検証

- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja): 同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。
**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-algorithm)

局所幅.8、mixedのみ確率.1でy=−x+.8Z、それ以外y=x+.8Z。混合率は状態非依存でq(y|x)=q(x|y)のため対数標的比でMH判定。各鎖は独立PCG64 stream、提案の適応・棄却の間引きなし。

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![多峰性MCMC：峰への閉じ込め・偽の安心・大域提案：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja) (`mcmc-bimodal-mixture`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-validation)

解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja): 同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。
**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-algorithm)

原著式から独自実装。odd長は中央1標本を落としてsplit、平均順位のBlom式は訂正済みS+1/4、fold後再rank、最大Rhatを採用。bulk ESSはrank split、tail ESSは元の全鎖のType7分位点を先に求めた≤indicatorをsplit。Geyer initial-positive/monotoneと宣言した端点処理・tau≥1/log10(total)を用い、反相関ESSをNへclipしません。

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-validation)

実鎖9組×3prefix×x/indicator＋8小fixtureの62組。同じbytesを再生成して照合し、通常の有限値Rhat/ESS/ACFと、定数・鎖内ゼロ分散・odd・ties・shift・scaleを検査。別の直接lag和、定常AR(1)の無限列tau=(1+rho)/(1−rho)で有限推定の誤差も測定します。routineは保存参照との照合で、ArviZのその場再実行は任意の別手順です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## CTとGLM：同条件の独立照合・格子・時間収束

- [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja): 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。
**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-algorithm)

両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CT・GLM：移動する磁気静力学平衡の格子・時間収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) (`advected-magnetostatic-equilibrium`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-validation)

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja): 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。
**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-algorithm)

主計算は固定α=ch=3のRusanovと前進Euler、GLMκ=2は格子に依存しません。独立C++ Athena++はHLLD・PLM・RK2・upwind CTです。同じ連続初期値を用いますが、Athenaのface/primitive離散化は主計算と完全同一ではありません。

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-validation)

密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照 · 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
- [CTの初期制約保持とGLMの能動的cleaning：非物理診断対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja): 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。
**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-algorithm)

同じ完全結合MHDコードを使用。y不変・By=vy=0ではGLMのBx/ψ系が流体応答から独立するため、離散Fourier記号の2×2行列と前進Euler行列冪を別に構成します。κ=2とκ=0を同じdt・LLF粘性で比較し、Bxだけの減少を物理減衰と取り違えません。

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CTの初期制約保持とGLMの能動的cleaning：非物理診断対照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-validation)

CT native divの初期違反保持、GLMのψ励起、Bx/ψ双方の独立FE参照一致、密度・圧力正値性、物理的総E/質量保存を確認。補助波エネルギーW=〈Bx²+ψ²/ch²〉のκ2/κ0比を判定し、半離散行列指数と連続Fourier解も区別して表示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 基盤手法：条件数・残差・収束と独立参照

- [AMGの条件数・異方性・残差と前進誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja): 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。
**使用手法**

- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-algorithm)

MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![AMGの条件数・異方性・残差と前進誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-validation)

真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [QR/SVD：既定特異値・摂動増幅・数値階数](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja): 二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。
**使用手法**

- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja) (`qr-svd`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-algorithm)

Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![QR/SVD：既定特異値・摂動増幅・数値階数：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) (`matrix-factorization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-validation)

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [Krylov固有値：クラスター部分空間と非正規感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja): 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。
**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-algorithm)

全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Krylov固有値：クラスター部分空間と非正規感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-validation)

解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [求積：狭いピーク・相殺・端点・誤差推定の盲点](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja): Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。
**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-algorithm)

Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![求積：狭いピーク・相殺・端点・誤差推定の盲点：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-validation)

roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 粒子・輸送：独立参照・保存則・統計誤差

- [Ewald：非対称周期セルのエネルギー・力と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja): 中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。
**使用手法**

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) (`ewald`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-algorithm)

erfcと逆空間和による主計算とは別に、1/rのGaussian積分と1次元theta関数の積を数値積分します。小さい積分変数ではPoisson変換と中性条件、大きい側では自己項を引いた像和を使い、力はthetaの解析微分から積分します。

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Ewald：非対称周期セルのエネルギー・力と独立theta積分：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-validation)

参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [SPME：格子・補間次数・格子位相と保存則](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja): BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。
**使用手法**

- [Particle Mesh Ewald（PME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja) (`pme`)
- [Smooth PME（SPME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja) (`spme`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja#spme-convergence-ja-algorithm)

16³/24³/40³格子と4/6次Bスプライン、3つの平行移動位相を用います。FFT逆空間エネルギーを割当て重みで位置微分し、実空間・自己項はEwald主計算と共有します。

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![SPME：格子・補間次数・格子位相と保存則：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja#spme-convergence-ja-validation)

独立thetaエネルギー・全力との差と、共有Ewald経路自体の誤差を明記します。分配の総和・導関数総和、電荷、エネルギー差分3成分、位相間の幅、有限格子の合力と粗い格子の対照を保存します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [FMM：直接和・解析配置と展開次数・木の深さ](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja): 96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。
**使用手法**

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) (`fmm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja#fmm-convergence-ja-algorithm)

P2M/M2M/M2L/L2Lと近接P2Pを保ち、次数2/4/8/12、深さ2/3を比較します。別のCartesian直接和、二点電荷の閉形式、正多角形の中心力と遠方ポテンシャルを参照にします。

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![FMM：直接和・解析配置と展開次数・木の深さ：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) (`logarithmic-particles`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja#fmm-convergence-ja-validation)

ポテンシャル・場の最大絶対誤差、実際の遠方移動演算、回転・平行移動誤差、電荷を掛けた力の合計を測ります。粗い展開の失敗対照も確認します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja): 冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。
**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-algorithm)

CIC割当て・同じ重みの場補間・スペクトルPoisson・速度Verlet。独立な時間積分法DOP853は同じ粒子格子RHSを積分し、参照自身の最大刻み感度を検査します。

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![PIC：格子・時間収束、保存量と粒子雑音：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-validation)

16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照 · 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。
- [DSMC衝突成分：有限N平衡・保存則・統計誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja): 有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。
**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-algorithm)

ランダムな完全対合と球面一様の散乱で、各対の運動量・エネルギーを保持します。別の標本生成ではGaussianを重心ゼロ部分空間へ射影し、半径を固定します。

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![DSMC衝突成分：有限N平衡・保存則・統計誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) (`maxwell-collisions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-validation)

全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
- [放射輸送：空間・角度収束と光子統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja): 純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja#radiation-convergence-ja-algorithm)

1次風上有限体積の空間更新とGauss–Legendre方向を使い、角度系列は正確な指数伝播で空間誤差を除きます。MCはmu=sqrt(U)と指数光学距離から生存・吸収を独立に判定します。

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![放射輸送：空間・角度収束と光子統計：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) (`absorbing-slab`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja#radiation-convergence-ja-validation)

16〜256セル・4〜64方向を別に収束させ、QUADPACK積分とE3を照合。64seed・1024/4096/16384光子で平均誤差、RMSE、二項標準偏差と95% Clopper–Pearson区間の実測被覆を記録します。全光子の出射＋吸収、正値性と離散フラックス収支を確認します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## 作用素分割：同じ反応拡散でLie–TrotterとStrangを比較

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja): 32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。
**使用手法**

- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) (`lie-trotter`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-algorithm)

Lie–Trotterは拡散h→反応h、Strangは拡散h/2→反応h→拡散h/2。どちらも更新後の状態を次へ渡します。拡散は2次中心FD行列の指数をFFTで厳密適用、反応は同じ陰的中点則・Newton公差2e−13・上限12評価を使用。反応流は厳密解ではなく2次近似です。クリッピング・自動刻み変更・代替解法への切替を行わず、未収束は失敗にします。

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![同じ非線形反応拡散でLie–TrotterとStrangを比較する：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-validation)

参照は同じFD半離散系を実空間の疎行列・別記述の反応RHSで組み、分割せずRadauで積分した数値解です。Radauの公差細分化と別のDOP853で参照自身の差を測り、最細Strang誤差との比を判定します。ノルムは成分ごとの平均L1・RMS L2・最大L∞を求めて悪い成分を採用し、4つの正の共通出力時刻の最大値で次数を測定。Newton公差感度、全副段階の正濃度、反応source/sink収支と逆順Lieの対照も記録します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。

## Noh衝撃波：厳密解・過熱誤差・格子収束

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja): 初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-algorithm)

Rusanov流束とSSPRK2（Heun）を使用します。平面・円筒は従来の区分定数再構築、球は保存量を体積重心の周りにMUSCL型線形再構築し、内部セルは重心間距離によるminmod傾きを使い、両端の境界セルは傾き0とします。各セル共通の係数θで左右面の全保存量傾きを縮小し、密度と内部エネルギーの面状態を検査します。セル平均の修正・圧力seed・floorは使いません。波速、Rusanov流束、数値応力P*=F_mom−((u_L+u_R)/2)F_massは同じ面状態から計算し、幾何CFLはV/(A_La_L+A_Ra_R)、指定値.35です。球では線形面応力の∫2rP*(r)drを厳密積分、平面・円筒は旧算術平均求積を保持します。反射面は再構築後の面状態を偶奇反転し、外側の冷たい流入は物理流束で与えます。各RK段の有限性・密度・内部エネルギーを検査し、不正なら失敗を記録します。

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

理想気体Eulerの平面・円筒・球の半径対称という限定した形です。幾何源・外側流入・初期圧力ゼロの条件は、この実行例の式・固定入力で定義します。


**問題の図**

![Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-validation)

旧平面・円筒の受入基準と59判定を保持し、球の追加基準・入力・ソースhashを初回の球PDE実行前に保存します。初回の円筒不合格はソース・全8本の診断ログ・不合格サマリーを保持し、同じ基準で面応力版を再検証した履歴です。厳密保存量セル平均は衝撃をまたぐ積分を分割し、p(平均U)と平均pを分けます。固定版LANL ExactPackの独立解析照合はd=1/2/3を含みます。球の新規PDE系列では全域r²重みL1/L2/L∞、原点を含むr≤.70rsの密度L1、原点・衝撃・plateauを別測定。各段の境界流入による離散保存収支と、連続解析総量との差を分け、M_h−M_exact=Σdt³/6、E_h−E_exact=Σdt³/12というSSPRK2境界求積の恒等式を検査します。 最初の球対称実行は旧算術平均源のまま105条件中2条件で不合格（最細衝撃位置3.923セル、plateau密度誤差11.03%）となり、全結果を保存しました。第2試行は球の面応力求積だけを変更しましたが、同じ2条件が未達（衝撃位置3.919セル、密度誤差11.018%）でした。第3試行はその求積を保ち、球だけMUSCL・minmod再構築を加えて、同じ105条件で比較します。 第3試行は28検査と全12格子計算を完了し、105条件すべてに合格しました。球N=512では全域密度L1=.0114343、衝撃位置誤差1.98856セル、plateau密度誤差5.2533%、原点込みcore密度L1=.0549503です。一方、中心最大比内部エネルギーの相対過剰は20.59%で、第2試行の15.52%より悪化しており、全指標の改善は主張しません。

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照 · 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

## Noh問題：2次元Cartesianと格子方向の誤差

- [Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja): 正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。
**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-algorithm)

区分定数のRusanov流束をx/y両方向の共有面に置く非分割更新とSSPRK2（Heun）です。CFL=.35を(max a_x+max a_y)/Δxに適用。外辺の冷たい物理流束は面内で解析積分し、時間に一次の流入をHeunの両段で積分します。セル平均の修復・圧力floor・seed・隠れた時間刻み再試行はなく、不正なRK段は配列を保存して失敗にします。

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

幾何源のない2次元Cartesian Euler系です。密度・2成分運動量・全エネルギーを正方形全域で更新します。


**問題の図**

![Noh問題：実際の2次元Cartesian Euler計算：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-validation)

実行前に入力・ソース・受入基準をhash保存。19単体検査と3格子・49判定が初回から合格しました。解析密度のセル積分は衝撃円の交差で区間を分割し、x=rs sinθによる64点Gauss求積で評価、128点との差と全質量の解析式で確認します。閉形式の厳密セル平均とは区別します。128²で密度全域L1=.09981、原点込みcore L1=.12231、衝撃位置は軸.968セル・対角1.469セルの誤差。離散収支の最大相対残差は約4.6e-15です。D4の鏡映・座標交換の保存量偶奇性と、連続回転対称性を区別して測ります。

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照 · 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

## Sedov–Taylor点爆発：球対称の軽量検証

- [Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja): 球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。
**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-algorithm)

球殻体積と面積を用いる区分定数Rusanov流束＋SSPRK2（Heun）です。半径運動量の幾何源p(A右−A左)/Vを同じRK段で積分し、静止した一様圧力との釣り合いも検査します。CFL=.4はmax((|u|+c)/(V/(A左+A右)))の逆数を使い、残り時間との比較を先に行います。圧力seed・floor・セル平均修復・隠れた刻み再試行はなく、不正な段は生の保存量と履歴を保存して失敗とします。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

理想気体Eulerの1次元球半径対称形。原点反射、幾何源、有限半径へのエネルギー投入と外側境界は、この例の固定入力で定義します。


**問題の図**

![Sedov–Taylor点爆発：球対称の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-validation)

初版r1はMacで22単体検査・48判定が合格しましたが、公開ZIPのLinux追試では警告を例外にする設定でCFL比のoverflowにより失敗しました。r2は代数的に等価な逆数最大率へ評価順を変更し、元の入力・参照・受入基準48条件を維持。r2専用の実行前hash契約を保存してから、警告を例外にした23検査と全4計算・48判定が合格しました。初版のソース・契約・Linux失敗記録も保存しています。参照は独立な相似ODEのDOP853積分、エネルギー規格化、中心ξ<.001の正則漸近形と衝撃位置で分割する殻求積です。16/32点求積・中心cutoff/ODE公差を別々に確認。固定commitの未改変ExactPackを6001/12001点で別実行し、中心とジャンプから離れた点を事前基準5e-4で照合しました。β=1.15166641793、Rs(.05)=.34746791233。原点・衝撃波を含むr≤1.2Rsの体積重み密度L1は.17257/.12785/.07458、圧力L1は.18148/.13939/.07615。512セルの衝撃位置誤差は1.096セル、最大離散収支残差は約8.89e-16です。

- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja) (`sedov`; 同じ問題の参照 · 半解析参照)

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

## Double Mach反射：多格子の軽量検証

- [Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja): 既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。
**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-algorithm)

既存Numartの区分定数HLL流束と非分割x/y発散、Heun/SSPRK(2,2)を独立した小型配布物にし、両段の境界流束・状態確認を追加しました。CFL=.4を各方向の最大音響速度の和に適用し、上辺は各RK段の実時刻で更新します。状態floor、セル修復、隠れた刻み再試行はなく、不正段の生配列と履歴を残して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の2次元圧縮性Euler保存系。Mach10の入射衝撃波、流入・流出・反射壁・移動衝撃波を与える上端境界は、この例の固定入力で定義します。


**問題の図**

![Double Mach反射：多格子の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-validation)

初回事前契約の20単体検査は合格。全3格子の実行前の読み取りレビューで、衝撃探索窓に前線が無い場合を拒否する診断ガードと1検査を追加し、旧契約・ソースを保持して改訂契約を固定しました。その21検査と全3計算・40判定が-W errorで合格しました。参照はRKDGキットで既に独立実行済みの、別実装primitive MUSCL/generalized-minmod θ=1.5/HLL/HeunのNy64/128データを再利用し、今回は参照PDEを再実行していません。Ny128保存量を保守的に制限して比較した密度L1は.08431/.05802/.03503、圧力L1は.09556/.06798/.04156。参照64/128増分は.00955/.01250で、最細主計算差の約.273/.301です。4保存量の境界収支の最大相対残差は約4.60e-13でした。

- [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja) (`double-mach`; 同じ問題の参照 · 有限格子の数値参照)

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

## Mach 3前向きステップ：軽量な2次元検証

- [Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja): 実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。
**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-algorithm)

既存Numartの区分定数HLL・非分割x/y発散・Heun/SSPRK(2,2)を小型配布物にし、6種類の境界ごとに両RK段で実際に使う流束を同じ重みで積算します。CFL=.4、各格子の上限20000刻み。全予測・更新段の正の密度と圧力を確認し、状態floor・修復・隠れた再試行はしません。不正段は生配列と完了履歴を保持して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の2次元圧縮性Euler保存系。Mach 3の一様流入と、段差・流路上下の反射壁、右端の流出境界を固定入力に定義します。


**問題の図**

![Mach 3前向きステップ：壁面収支と多格子検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-validation)

入力・受入基準・24単体検査・数値ソースを主計算の初回検査・PDE実行前に固定しました。解析的なMach3垂直衝撃波のRankine–Hugoniot関係、一様な平行流路、壁の質量・エネルギー流束ゼロ、段差の圧力力の向き、実際の4成分収支、不正段の保持を検査します。別実装のC++17 MUSCL/generalized-minmod θ1.5/HLL/HeunによるNy80/160の参照を新規に実行し、保存量を保守的に制限して密度・圧力の全流体領域L1を比較します。参照の再計算は通常の公開ZIP追試には含めず、保存データ・ソース・契約・実行記録を同梱します。 最初の参照Ny160は事前固定の120秒上限で停止した記録を保持し、診断文字列の不要なメモリ割当てだけを除く参照改訂を、主計算の初回実行前に再固定しました。入力・演算・CFL・判定値は変更していません。 24検査と全3計算・45判定が-W errorで合格。主計算の密度L1は.14754/.12878/.10265、圧力L1は.19373/.16015/.12242、密度の最後の2格子の傾きは.327。参照80/160増分は.02636/.03063で、最細主計算差の約.257/.250。全4成分の境界収支の最大相対残差は2.99e-13、全壁の積分質量・エネルギー流束は0でした。主計算3格子は元のMacで約46秒、性能改訂後の参照80/160は約8/65秒です。

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照 · 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

## 低Mach等エントロピー渦：前処理Roe流束の軽量検証

- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja): 同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。
**使用手法**

- [Roe法](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja) (`roe`)
- [低Mach数のPDE前処理](https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja) (`low-mach-preconditioning`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-algorithm)

同じ無制限の中心原始変数MUSCL再構築・有限体積・物理Euler流束・SSPRK(3,3)を使い、Roe散逸だけをD=P⁻¹|PA|で前処理します。Roe平均の全流速Machからμ=min(1,max(Mlocal,M∞))、δ=1/μ−1とし、原始変数のMiczek行列を保存量へ変換します。行列絶対値は特性値ũn,ũn±τの2次多項式で作用させ、別の密行列固有分解と照合します。物理時間微分・音速は変えず、音響CFL=.2を使います。再構築した両面と各3段の正のρ,pを確認し、limiter・floor・状態修復・隠れた再試行・疑似時間反復はありません。前進Eulerの増幅反例を示すため、SSP・TVD・非線形安定性を名前だけで保証しません。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

無外力の2次元理想気体Euler系を、元の保存変数・物理時間で更新します。γ=1.4、周期20×20領域、背景圧力をMach数に応じて変える等エントロピー渦が固定入力です。


**問題の図**

![低Mach等エントロピー渦：前処理Roe流束の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-validation)

初版の32単体検査は合格しましたが、区分定数空間離散化での143判定中、M∞=.01・最細格子の全領域圧力誤差.16537が事前閾値.1を超えました。初版ソース・契約・全12場・判定と、その全領域図を失敗のまま保存します。改訂では両流束を同じ無制限中心原始変数MUSCLにし、面状態の拒否・正しい再構築Fourier記号・独立行列を使う実RHSの線形化など3検査を追加しました。入力・物理時間・CFL・受入条件はバイト単位で不変です。新35検査と143条件の契約を改訂の実行前に固定しました。 Roe平均の保存量ジャンプと物理流束差、密行列の前処理散逸、3段更新・不正段保持を照合します。各背景Mach・流束で17²個の定数状態Fourierモードと、物理音響エネルギーで規格化した増幅行列の1/10/100乗を調べます。圧力誤差は大きなp∞ではなくρ∞|U∞|²で割り、速度誤差は渦の速度変動で規格化します。移動解析場に対する初期R_h−q_tも記録し、定常残差の収束とは区別します。 改訂の35検査・全12計算143判定は-W errorで合格し、元のMacで全計算は約4.4秒でした。最細M∞=.01の速度相対L1はRoe .07411、前処理 .01847、固定コアの圧力誤差は.04871/.0006325でした。一方、全領域の圧力誤差は.01194/.01260で前処理側がわずかに悪く、M∞=.1でも.0006653/.0006737と同様です。全4保存量の最大相対残差は4.24e-14。Gauss8/16の動的スケール最大差は4.08e-11、解析Euler代入残差は1.09e-16でした。指定したFourierモードのSSPRK3増幅半径とエネルギー規格化行列累乗ノルムは最大1。前進Eulerは両MUSCL流束で1を超え、M∞=.01の前処理側で約1.03560でした。

- [等エントロピー渦：低Mach比較に用いるEuler解析場](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja) (`isentropic-vortex`; 同じ問題の参照 · 解析参照)

同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。

## Guderley収束衝撃波：球対称の軽量検証

- [Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja): 冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。
**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-algorithm)

面積4πr²と球殻体積4πΔ(r³)/3を用いた第一次数の球対称有限体積法です。共有HLL面流束の発散に、半径方向運動量の圧力幾何項p_iΔA/Vを加え、Heun法・CFL=.4で更新します。中心は面積ゼロの反射条件、外側は各RK段の実時刻に評価した相似場です。全3保存量について実際の境界面流束と幾何ソースを同じHeun重みで積分します。状態floor、圧力修復、時間刻みの隠れた再試行はありません。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

未衝撃上流の圧力ゼロ・γ=1.4の理想気体Euler系の1次元球半径対称形。原点到達前の時区間、相似初期場、境界条件、球殻平均はこの固定入力で定義します。


**問題の図**

![Guderley収束衝撃波：球対称の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-validation)

33単体検査と3格子55判定を実行前に固定し、警告をエラーにする設定で合格しました。冷たい上流でのゼロ音速HLL分岐、幾何的な静止圧力釣合い、共有流束の収支、実際の2段の境界時刻、不正段の生配列保持を確認します。全体積L1と、あらかじめr≥.8Rsとした衝撃・非零流れ領域のL1を並べ、冷たい内側で誤差を薄めないようにします。密度・圧力の最大差と保存した時系列からの衝撃軌道も残します。半解析参照は固定LANL ExactPackの相似指数固有値ルーチンとODEを使い、反射後分岐を計算しないキャッシュ付きアダプターです。独自に再実装した相似ODEとは表示しません。別に実装したEuler有限体積計算と参照を比較します。 全体積の密度L1は.02345/.01339/.007722、圧力L1は.03277/.01743/.009477でした。r≥.8Rsの密度L1も.02414/.01378/.007948と減少します。最細の衝撃位置は.530273、相似参照は.533989で、差は約2.54セルです。最大の全3成分収支残差は8.85e-16、全段の最小内部エネルギーと音速専用丸めガード回数はともに0でした。参照のEuler差分代入残差は8.24e-9、有限オフセットの移動衝撃ジャンプ残差は4.40e-8。旧版で固有値を新規計算した全3計算は元のMacで約44.6秒でした。 公開r2のLinuxでは33検査は96.34秒で合格しましたが、検査と本計算を合わせた120秒枠の残り23.31秒で本計算が時間切れになりました。この公開追試の失敗記録と旧ソースを保持します。改訂では、既に実際のExactPack射撃法で求め、出典ソース・資格確認とSHAで結んだ固有値を再利用し、通常実行の各プロセスで射撃法を重複計算しません。臨界位相のCdiff残差と相似ODEは新しく評価します。入力・数値判定・Eulerソルバー・実行入口・120秒枠は変えません。 改訂版では33単体検査と全3入力55判定を共通120秒枠で続け、Macで計約.912秒で完了しました。全3格子の初期値・最終値・参照値・保存履歴の配列は公開r2とビット一致し、固有値の再利用で物理結果が変わらないことを別に照合しました。

- [Guderley収束衝撃波：固有値と球対称の半解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja) (`guderley`; 同じ問題の参照 · 半解析参照)

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

## Euler二重膨張波：段階ごとの正値性

- [Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja): 既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
**使用手法**

- [Lax–Friedrichs法](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja) (`lax-friedrichs`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [平均を保つ正値状態スケーリング](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=ja) (`positive-scaling`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-algorithm)

保存量の無制限中央線形再構築を行い、セル平均と左右2端点へ共通の係数θを用いて密度・圧力を正にします。端点平均は元の保存量平均のままです。共有LF流束による前進Euler更新をSSPRK(3,3)で凸結合し、各段の流束前に再構築と制限をやり直します。ε=10⁻¹³は再構築の目標で、密度・エネルギーを加えるfloorではありません。平均の修復・無言の刻み再試行は行いません。

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の無外力1次元Euler保存系。セル平均の密度・運動量・全エネルギーを、線形保存量MUSCL再構成と共有Lax–Friedrichs流束で更新します。


**問題の図**

![Euler二重膨張波：段階ごとの正値性：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-validation)

27単体検査と3格子73判定を実行前に固定します。スケーリング前に生じる負の端点圧力を保持し、制限後の端点・前進Euler平均・SSP凸結合平均、θ、全3保存量の境界流束収支を別々に測ります。閉形式の対称希薄波と既存の独立な対数圧力根探索を照合し、保存量のGauss8/16セル平均との誤差と格子細分化を記録します。

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照 · 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

## Zalesak型2D回転輸送：保存・有界性・形状誤差

- [Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja): スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
**使用手法**

- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-algorithm)

解析的な発散ゼロの法線面速度と、隣接セルで共有する上流数値流束を用います。区分定数donor-cellと、方向別minmod勾配による平均保存型MUSCLを、どちらもSSPRK(3,3)で進めます。4面中点の平均がセル平均に等しいことと、各面のCourant数≤1/4による凸結合を使い、実際の値.20を各FE段で確認します。セル平均のクリップ、状態floor、刻み棄却・再試行は行いません。

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`)

qの2次元保存形輸送。速度a=−ω(y−yc), b=ω(x−xc)は与えられ、∂xa+∂yb=0です。面で共有する速度・数値流束を使い、スカラーのセル平均を更新します。


**問題の図**

![Zalesak型2D回転輸送：保存・有界性・形状誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-validation)

26単体検査と8固定計算158判定を実行前に固定します。全FE候補・SSP凸結合のmin/max、共有流束による質量収支、再構築の平均保存、3格子のL1/L∞・相対L2を保存します。円と凸多角形の交差面積から独立に作る厳密輸送のセル平均を、SciPyの鉛直切片求積と面積・一次モーメントで照合します。1/4・1/2・3/4回転の誤差と重心も検査し、回転方向や速度の誤りが一回転のreturnだけで隠れないようにします。

- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja) (`zalesak-rotation`; 同じ問題の参照 · 解析参照)

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

## WENOの臨界点・ε依存性

- [WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja): 同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
**使用手法**

- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja) (`weno-js`)
- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) (`weno-z`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-algorithm)

3候補と線形重み(.1,.6,.3)、Jiang–Shu指標を共通にし、JSはd/(β+ε)²、Zはd[1+(|β₀−β₂|/(β+ε))²]を正規化します。ε=10⁻⁴⁰,10⁻⁶,h²です。輸送は共有風上面流束と古典RK4、Courant.1を使い、状態クリップ・再試行を行いません。

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`)

局所多項式のセル中心x=0、再構成面h/2、h=1/64…1/512を使います。輸送は[0,1]周期・速度1・q₀=cos(2πx)+.1sin³(2πx)、T=1、32/64/128セルです。全て有限体積セル平均であり、点値を誤差の参照にしません。


**問題の図**

![WENO-JS／Z：臨界点とεの固定比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-validation)

実行前契約で72局所再構成・24PDE計算・36pytestを固定します。解析セル平均を独立Gauss12求積と照合し、局所の誤差・重み、輸送のL1/L2/L∞・質量・全段有限性・中間時刻と保存流束を記録します。最細格子で6通りの刻み半減差が対応する連続解誤差の10%以下か確認します。

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照 · 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照 · 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照 · 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

## 浅水流：地形・静止湖・乾燥床

- [SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja): 水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。
**使用手法**

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) (`forward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-algorithm)

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

- [地形源項付き浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja) (`shallow-water-bed`)

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。


**問題の図**

![SWASHES地形流：静水と非零流量の定常解：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-validation)

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

- [静止湖：表現した床の上の湿潤・露出平衡](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja) (`lake-at-rest-bed`; 同じ問題の参照 · 解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

- [SWASHES定常流：非射流Bernoulli根](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja) (`swashes-bernoulli`; 同じ問題の参照 · 半解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
- [乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja): 右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。
**使用手法**

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) (`forward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-algorithm)

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`)

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、1600/3200/6400セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。


**問題の図**

![乾いた河床のダム破壊：実際のwetting/drying：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-validation)

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。

- [Ritter乾燥床破堤：g9.81の専用セル平均参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja) (`ritter-dry-bed`; 同じ問題の参照 · 解析参照)

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

- [浅水／乾床への膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja) (`swe-dry-bed`; 関連モデルの参照 · 解析参照)

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

## 非周期壁面：キャビティと製造解

- [Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja): 非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-algorithm)

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。


**問題の図**

![Re=100蓋駆動キャビティ：Ghia中心線との比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-validation)

22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照 · 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照 · 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。
- [非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja): キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-algorithm)

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja) (`forced-incompressible`)

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。


**問題の図**

![非周期壁面の製造解：速度・剪断・圧力演算子：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-validation)

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

- [壁面製造解：多項式速度と独立した圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja) (`wall-mms`; 同じ問題の参照 · 製造解)

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

## レベルセット法：円の2D移流・剛体回転

- [レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja): 中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。
**使用手法**

- [レベルセット法](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja) (`level-set`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-algorithm)

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja) (`level-set-advection`)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。


**問題の図**

![レベルセット円の2D平行移動：界面・面積・再初期化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-validation)

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja) (`level-set-translation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja) (`level-set-rotation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja): 中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。
**使用手法**

- [レベルセット法](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja) (`level-set`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-algorithm)

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja) (`level-set-advection`)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。


**問題の図**

![偏心したレベルセット円の2D剛体回転：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-validation)

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja) (`level-set-translation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja) (`level-set-rotation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

## スペクトル要素法とFR：既存FEM・DGとの軽量比較

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja): 単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。
**使用手法**

- [スペクトル要素法（SEM）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja) (`spectral-element`)
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-algorithm)

SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。


**問題の図**

![スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-validation)

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja): 0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。
**使用手法**

- [Flux Reconstruction法（FR法）](https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=ja) (`flux-reconstruction`)
- [不連続Galerkin法／Legendre](https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=ja) (`dg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-algorithm)

p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。


**問題の図**

![FR法の1D周期移流：Radau補正と既存DGの比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-validation)

追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照 · 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照 · 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照 · 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

## KH・RTの初期成長と独立線形参照

- [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja): 実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-algorithm)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [維持されたせん断層の強制渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja) (`forced-vorticity`)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。


**問題の図**

![KHの初期成長：滑らかな周期せん断層：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) (`kh-initial-growth`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-validation)

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [KH初期成長：独立した線形Fourier–Galerkin参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja) (`kh-initial-growth`; 同じ問題の参照 · 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
- [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja): 密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-algorithm)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [能動浮力を伴うBoussinesq渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja) (`boussinesq-buoyancy`)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。


**問題の図**

![RTの初期成長：滑らかなBoussinesq二層：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) (`rt-initial-growth`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-validation)

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [RT初期成長：Boussinesq二層の線形IVP参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja) (`rt-initial-growth`; 同じ問題の参照 · 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

## MHD輸送・波・圧縮構造の独立比較

- [円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja): 全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。
**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-algorithm)

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。Bx一定の1次元有限体積更新。

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。


**問題の図**

![円偏波Alfvén波：全成分の格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照 · 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。
- [磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja): 実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。
**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-algorithm)

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。


**問題の図**

![磁場ループ：独立2次元参照と細分化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

- [磁場ループ：固定Athena++の独立終端参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja) (`magnetic-loop-independent`; 関連モデルの参照 · 有限格子の数値参照)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。
- [後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja): 圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。
**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-algorithm)

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。


**問題の図**

![後期Orszag–Tang：独立参照と圧縮構造：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照 · 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

## 角特異性・曲線座標・Neumann／Robin境界

- [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja): 再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。
**使用手法**

- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-algorithm)

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。


**問題の図**

![L字領域P1特異解：graded格子と歪みの分離：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) (`lshape-fem`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-validation)

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

- [L字角の特異解：調和場と別の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja) (`lshape-fem`; 同じ問題の参照 · 解析参照)

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。
- [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja): 軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。
**使用手法**

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) (`q1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-algorithm)

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [可変粘性のベクトル応力境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja) (`variable-viscosity-vector`)

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。


**問題の図**

![環状領域の可変粘性・真2DベクトルMMS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-validation)

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

- [環状粘性ベクトルMMS：独立応力微分で外力を確認](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja) (`annular-viscous-mms`; 同じ問題の参照 · 製造解)

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。
- [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja): 特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-algorithm)

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。


**問題の図**

![純Neumannの互換条件と平均値ゲージ：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-validation)

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

- [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja) (`poisson-neumann`; 同じ問題の参照 · 製造解)

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。
- [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja): 2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-algorithm)

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。


**問題の図**

![2D混合Robinの製造解と境界流束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-validation)

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

- [混合Robin：2次元解析場と独立な法線流束](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja) (`poisson-robin`; 同じ問題の参照 · 製造解)

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

## 非一様ALE輸送・2次元回転浅水波

- [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja): 質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。
**使用手法**

- [ALE一様状態・幾何保存モデル](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja) (`ale`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-algorithm)

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`)

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。


**問題の図**

![非一様移動格子で実際に運ぶALEスカラー：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-validation)

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

- [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja) (`ale-nonuniform-transport`; 同じ問題の参照 · 解析参照)

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。
- [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja): 実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。
**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-algorithm)

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

- [線形回転浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja) (`linear-rotating-shallow-water`)

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。


**問題の図**

![2D C-grid回転浅水波の実時間発展：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-validation)

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

- [C-grid：連続Fourier解と離散記号の行列指数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja) (`cgrid-rotating-wave`; 同じ問題の参照 · 解析参照)

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

## SRHD衝突・SRMHD非線形Alfvén波

- [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja): 相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。
**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-algorithm)

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

- [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja) (`srhd`)

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。


**問題の図**

![SRHDの対称二衝撃波衝突：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-validation)

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

- [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja) (`srhd-collision`; 同じ問題の参照 · 半解析参照)

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。
- [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja): 完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。
**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-algorithm)

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

- [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja) (`srmhd`)

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。


**問題の図**

![SRMHDの有限振幅円偏極Alfvén波：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-validation)

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja) (`srmhd-alfven`; 同じ問題の参照 · 解析参照)

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

## 係数ジャンプ・回転異方性のMG／AMG

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja): 不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。
**使用手法**

- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) (`multigrid`)
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-algorithm)

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`)

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。


**問題の図**

![係数ジャンプ拡散：共有流束とMG・AMG：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-validation)

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja) (`checkerboard-diffusion`; 同じ問題の参照 · 有限格子の数値参照)

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja): 非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。
**使用手法**

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) (`q1-fem`)
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) (`multigrid`)
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-algorithm)

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`)

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。


**問題の図**

![回転異方性拡散：完全テンソルQ1とMG・AMG：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-validation)

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja) (`rotated-anisotropic-diffusion`; 同じ問題の参照 · 製造解)

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

## 中性スラブ：3周期補正と真の2周期参照

- [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja): 4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。
**使用手法**

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) (`ewald`)
- [スラブ静電場と2次元周期Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=ja) (`slab-ewald`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-algorithm)

全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

- [Coulomb静電場と混合周期境界](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja) (`coulomb-electrostatics`)

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。


**問題の図**

![中性長方形スラブ：真2P参照とYB補正：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-validation)

参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。

- [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja) (`neutral-slab-yb`; 同じ問題の参照 · 半解析参照)

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

## 3Dの1/r核：展開・木・力の検証

- [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja): 非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。
**使用手法**

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) (`fmm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-algorithm)

P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。


**問題の図**

![真3D 1/r FMM：多段変換・力・適応所有権：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-validation)

有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。

- [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja) (`fmm3d-inverse-r`; 同じ問題の参照 · 有限格子の数値参照)

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

## 重力軌道：Keplerと軟化有限粒子

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja): 非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。
**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-algorithm)

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。


**問題の図**

![無軟化Kepler二体の時間誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-validation)

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照 · 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja): 同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。
**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)
- [Barnes–Hut八分木](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja) (`barnes-hut`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-algorithm)

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。


**問題の図**

![冷たいPlummer密度由来32粒子の短時間力学：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-validation)

非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja) (`gravity-plummer-short`; 同じ問題の参照 · 有限格子の数値参照)

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

## 熱的PIC：Landau減衰と二流不安定性

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja): 熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。
**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-algorithm)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`)

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。


**問題の図**

![温かいPICの線形Landau減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-validation)

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja) (`thermal-landau-damping`; 同じ問題の参照 · 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja): 温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。
**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-algorithm)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`)

各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。


**問題の図**

![温かいPICの二流初期成長：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-validation)

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja) (`thermal-two-stream`; 同じ問題の参照 · 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

## PICの独立空間実装との照合

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja): ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。
**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-algorithm)

独立側はPythonスカラー配置、明示的な複素DFT和、独自の補間ループを所有します。主側のFFT・配置・補間を呼びません。数学上のCIC、Nyquist規約、velocity-Verlet法、初期配列は共通です。

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。


**問題の図**

![PIC空間演算の独立実装照合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-validation)

19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照 · 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

## 有限Knudsen数のCouette・Fourier流

- [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja): 物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-algorithm)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja) (`hard-sphere-boltzmann`)

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。


**問題の図**

![硬球DSMCの有限Kn Couette流：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja) (`dsmc-couette`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-validation)

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

- [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-couette-ja) (`dsmc-couette`; 同じ問題の参照 · 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja): 物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-algorithm)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja) (`hard-sphere-boltzmann`)

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。


**問題の図**

![硬球DSMCの有限Kn Fourier熱伝導：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) (`dsmc-fourier`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-validation)

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

- [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja) (`dsmc-fourier`; 同じ問題の参照 · 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

## 剛体球DSMCのMach2平面衝撃波

- [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja): 物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-algorithm)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。 2026-11-24版は固定reservoir係数、同一vで既評価の逆CDF残差、keep→left→right順の連結の再利用と、範囲確認した整数sort keyだけの可逆uint8圧縮を行う性能修正版です。元の乱数呼出順・安定sortの同値粒子順位・衝突対・科学設定を保ち、前3点の成分資格163項目に加え、sort keyを含む別348項目でbit/RNG一致を確認しました。いずれも成分検査であり、新mainと全保存科学値の一致はまだ未判定です。

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja) (`hard-sphere-boltzmann`)

1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。


**問題の図**

![硬球DSMCのMach2平面衝撃波：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-validation)

各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 Nov23保存成功と全15計算・129判定の厳密比較を行う新mainは、本契約の時点で未実行です。20pytestと全mainの外部共有上限120秒、全診断・NPZ・CSVを維持します。

- [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja) (`dsmc-planar-shock`; 同じ問題の参照 · 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

## LBMのRe100蓋駆動キャビティ

- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja): 4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。
**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-algorithm)

標準D2Q9平衡分布とBGK衝突、非周期link streaming、q=.5の移動halfway反射。流出入分布ごとに壁impulseを加算し、密度補正や内部速度resetをしません。C++17を一時領域でcompileしPythonから呼びます。

$$
f_i^{eq}=w_i\rho[1+3c_i\cdot u+\frac92(c_i\cdot u)^2-\frac32|u|^2],\quad\nu_\ell=(\tau-1/2)/3
$$

$$
f_{\bar i}(x,t+1)=f_i^\star(x,t)-6w_i\rho_0c_i\cdot u_w,\quad\rho_0=1
$$

$$
\mathrm{Re}=UL/\nu=100,\quad t_\star=100
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。


**問題の図**

![LBM Re100蓋駆動キャビティ：実2D場とGhia中心線：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-validation)

各群22pytestと37判定。60k/80k/120k整数stepsでt*=100へ進み90/95/100を保存。最細u/v中心線最大誤差.03、主渦距離.06、95→100相対L2変化2e-4、質量・壁込み運動量ledgerを事前固定します。

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照 · 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照 · 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

## LBMのTaylor–Green渦と低Mach誤差

- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja): 周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。
**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-algorithm)

標準BGKと完全周期streaming。p=cs²(rho−平均rho)(dx/dt)²で圧力単位とゲージを揃えます。解析場は初期値以外に注入せず、微分を独立Fourier演算で資格確認します。

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。


**問題の図**

![LBM Taylor–Green渦：格子・刻み・Machの結合感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-validation)

22pytestと79判定、6固定発展。最細速度相対L2.03、圧力.08、combined速度次数1.5以上、エネルギー.03、発散・周期質量・平均運動量を判定。解析PDE5資格を区別して保存します。 最粗N16の初回エネルギー誤差5.0018%未達を保持し、同じ3%基準へ最粗だけN24へ細分化。次数は最細32/64対だけで評価します。

- [粘性流／2次元Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja) (`taylor-green`; 関連モデルの参照 · 解析参照)

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja) (`lbm-taylor-green`; 関連モデルの参照 · 解析参照)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

## 曲面LBMの環状Couette流

- [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja): 実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。
**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-algorithm)

円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。


**問題の図**

![曲面LBMの環状Couette制御：速度・圧力・torque：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-validation)

群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。

- [曲面LBMの環状Couette制御：速度・圧力・トルク](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja) (`lbm-annular-couette-control`; 同じ問題の参照 · 解析参照)

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

## LBMの曲面壁とRe20円柱

- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja): 標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。
**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-algorithm)

標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。


**問題の図**

![LBMの実円柱Re20：Schäfer–Turek形状と明示出口：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-validation)

群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。

- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja) (`lbm-cylinder-re20`; 同じ問題の参照 · 有限格子の数値参照)

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

## 等方散乱平板と連続角度参照

- [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja): 正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-algorithm)

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。


**問題の図**

![等方散乱平板の反射・透過・吸収：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-validation)

独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。

- [等方散乱平板：連続角Fredholm流束参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja) (`isotropic-scattering-slab`; 同じ問題の参照 · 半解析参照)

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

## 非平衡放射：拡散と輸送を分ける

- [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja): 実際の放射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-algorithm)

保存的FVと後退Euler。放射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

- [Su–Olson1996の非平衡拡散・物質交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja) (`non-equilibrium-diffusion-exchange`)

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。


**問題の図**

![Su–Olson1996非平衡拡散：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-validation)

独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。

- [Su–Olson1996拡散：固定版の独立積分評価関数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja) (`su-olson-diffusion1996`; 同じ問題の参照 · 半解析参照)

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。
- [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja): 物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-algorithm)

全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

主検証は1997型の放射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

主検証は1997型の放射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。


**問題の図**

![Su–Olson1997角度輸送の独立公開表比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-validation)

5主計算で空間・32/64角・時間差と独立W/V誤差を分けます。参照表の有限性・因果零・一様解析source極限はmain前に資格済みです。 同じ初期・境界・sourceで別の連続空間角度行列と解析拡散極限を比較し、空間・角度・連続体極限誤差を分離。GL64/128、非単位容量の一様厳密解、独立DOP853で新参照141項目を先に資格します。

- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja) (`su-olson-transport1997`; 同じ問題の参照 · 有限格子の数値参照)

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

## 2Dの影・ビームとM1閉包

- [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja): 実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-algorithm)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。


**問題の図**

![2D吸収影と保存的M1輸送：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-validation)

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

- [円形吸収体の特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja) (`shadow-absorber2d`; 同じ問題の参照 · 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
- [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja): 保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-algorithm)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。


**問題の図**

![2D反向beamとM1閉包の情報損失：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-validation)

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

- [反向伝播packetの特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja) (`opposing-beams2d`; 同じ問題の参照 · 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

## SDEの弱誤差・強誤差と標本誤差

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja): 連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-algorithm)

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。


**問題の図**

![GBMのweak誤差とMonte Carlo標準誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-validation)

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照 · 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照 · 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja): 連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-algorithm)

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。


**問題の図**

![OUのweakモーメントと同時Brownian結合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-validation)

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照 · 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja): 補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。
**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-algorithm)

Milsteinは.5σ²X(dW²-h)を追加。全法・刻みでfine driverと厳密端点1配列を共有。負状態を修復しません。

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。


**問題の図**

![同じBrownian経路のMilstein・EM strong比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-validation)

相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照 · 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照 · 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

## 重要度サンプリングと相関Gaussian診断

- [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja): 通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。
**使用手法**

- [Monte Carlo積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja) (`monte-carlo`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-algorithm)

Y=1(X>a)exp(-aX+a²/2)の通常平均。ランダムな重み総和で割らず、proposal調整なし。直接MCの無hitは0のまま保存しCP区間を付けます。

$$
\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}
$$

$$
\mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)
$$

- [Gaussian確率測度：尾確率と相関標的](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja) (`gaussian-probability-model`)

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。


**問題の図**

![正規稀少尾の通常importance sampling：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja) (`normal-tail-importance`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-validation)

1〜4次モーメントを独立正の積分で資格。既知分散による5SE校正、seed間分散、解析分散低減、重み欠落負例。既知分散normal95%のIS区間の被覆は閾値/prefixごと64反復で別記。

- [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-normal-tail-importance-ja) (`normal-tail-importance`; 同じ問題の参照 · 解析参照)

重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。
- [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja): 実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。
**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-algorithm)

対称random-walk MH、拒否状態も保持。8観測量それぞれのoriginal-scale meanESS/MCSEを計算し、rankbulkESSを流用しません。

$$
\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]
$$

$$
\operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}
$$

- [Gaussian確率測度：尾確率と相関標的](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja) (`gaussian-probability-model`)

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。


**問題の図**

![相関2変量Gaussianのjoint標的とMCSE：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja) (`correlated-gaussian-mcmc`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-validation)

4つのpreconditioned最終prefix全観測量にRhat/ESS/MCSE/既知moment条件。同じ128scalararrayを別ArviZ0.20過程へ渡した640値資格と全データSHAで照合。標的は解析Gaussianモーメントで別検査。 640比較は不変な同一データfixture上で行い、別に生成する8組のfresh軌道で物理・混合判定を行います。環境を跨ぐ生成配列のbit一致は要求しません。

- [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-correlated-gaussian-mcmc-ja) (`correlated-gaussian-mcmc`; 同じ問題の参照 · 有限格子の数値参照)

診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。

# Explore small implemented validations by field

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## AMG, factorizations, eigenvalues and quadrature

- [Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en): Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.
**Methods used**

- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-algorithm)

A graph based on row-relative off-diagonal strength supplies greedy star aggregates; leftover nodes attach to adjacent aggregates. Smooth tentative T via P=(I−ωD⁻¹A)T with ω=4/(3ρ̄), where ρ̄ bounds the absolute row sums of D⁻¹A. Coarse operators are PᵀAP. V-cycles use two pre/post Jacobi sweeps and a terminal dense direct solve. This is a small adopted SA variant, not every construction or convergence theorem in the original paper.

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Matrix-based AMG: distinguish residual and solution error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-validation)

Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en): Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.
**Methods used**

- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en) (`qr-svd`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en#qr-svd-factorization-en-algorithm)

Householder reflectors triangularize R while accumulating Q. The SVD repeatedly rotates column pairs toward orthogonality and uses their resulting lengths as singular values; it does not diagonalize AᵀA. Least squares uses triangular back substitution for QR and truncated compact SVD for deficient rank.

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) (`matrix-factorization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en#qr-svd-factorization-en-validation)

Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en): Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.
**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en#krylov-eigenvalues-en-algorithm)

Lanczos uses its three-term recurrence plus two passes of full reorthogonalization; Arnoldi uses two-pass modified Gram–Schmidt. Only the small projected T/H is solved by NumPy eigh/eig before lifting Ritz vectors. A full dense solve of the original matrix is used only on the reference side.

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en#krylov-eigenvalues-en-validation)

Store ||Av−λv||₂, differences from independently solved dense eigenvalues and basis orthogonality; verify final improvement as Krylov dimension grows. Nonsymmetric Ritz convergence is not assumed monotone. Tests include identity-matrix happy breakdown, zero-start rejection and insufficient dimension budgets.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en): Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.
**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en#gauss-adaptive-quadrature-en-algorithm)

Golub–Welsch obtains nodes from a symmetric Jacobi matrix and weights from twice the squared first eigenvector components. Adaptive Simpson bisects intervals and allocates tolerances using |Sleft+Sright−Swhole|/15 as a local estimate. Evaluation and depth limits report unmet targets explicitly.

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en#gauss-adaptive-quadrature-en-validation)

Measure polynomial moments for every chosen order, node/weight differences from SciPy roots_legendre, order refinement for the analytic exponential integral, and agreement with analytic arctangent and SciPy quad references. Store evaluation counts/errors as tolerance tightens; test forced exhaustion after five evaluations and nonfinite integrands.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## MCMC, temperature control and biological models

- [Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en): Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.
**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-algorithm)

Use a log-acceptance Metropolis update. Pool FFT within-chain autocovariances and obtain mean-observable ESS from Geyer initial-positive pairs starting at gamma0+gamma1. Also report classical split-Rhat.

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Gaussian-target MCMC: distribution, autocorrelation and ESS: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en) (`gaussian-mcmc`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-validation)

Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en): Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.
**Methods used**

- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-algorithm)

Compose force B and drift A half steps with exact OU noise O in B-A-O-A-B order. Record covariance, three CDFs, energy mean/variance and position correlation.

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Langevin thermostat: canonical distributions, timestep bias and correlation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-validation)

Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference · Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en): Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en#reaction-diffusion-fourier-en-algorithm)

Advance original periodic second-centered differences with RK4. The spatial sequence uses one small time step; the temporal sequence fixes the spatial operator.

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Reaction-diffusion: separate second-order space and fourth-order time: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en#reaction-diffusion-fourier-en-validation)

Measure spatial order against r-Dk² and temporal order against r-4Dsin²(kdx/2)/dx². Both are independent analytic references, rather than a finer-grid run of the same solver.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en): Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-algorithm)

Advance the linearized and short nonlinear PDEs using original centered differences/RK4. Record mode amplitudes/growth on three grids, minimum concentrations and early-pattern amplification.

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Turing instability: linear growth and small-amplitude patterns: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-validation)

Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en): Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.
**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-algorithm)

Use original RK4 with steps 0.1/0.05/0.025, splitting time intervals exactly at pulse discontinuities. At output spacing 0.1, measure the peak and distance from rest.

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-validation)

Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Particles, electrostatics, kinetic and radiative transport

- [Neutral-cell Ewald sums and an independent theta integral](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en): Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.
**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-algorithm)

Combine an erfc-screened image sum, Gaussian-damped reciprocal structure factors and the self correction. Differentiate each term and check all 24 force components against central energy differences.

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Neutral-cell Ewald sums and an independent theta integral: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en#ewald-en-validation)

Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Mesh/order convergence of B-spline smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en): A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.
**Methods used**

- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) (`pme`)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) (`spme`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-algorithm)

Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Mesh/order convergence of B-spline smooth PME: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-validation)

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en): Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.
**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-algorithm)

Implement leaf P2M, upward M2M, interaction-list M2L, downward L2L, local-polynomial evaluation and near-field P2P. Record translation and near-pair counts; this is not a Barnes–Hut traversal relabeled as FMM.

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![2D logarithmic FMM with M2M, M2L and L2L: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en#fmm-en-validation)

For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en): Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.
**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-algorithm)

Combine CIC deposition and matching field gathering, a mean-zero spectral Poisson solve and velocity Verlet. Set the field Nyquist mode to zero for a real skew-adjoint spectral derivative.

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Cold-plasma oscillation with electrostatic CIC PIC: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en#pic-en-validation)

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference · Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en): Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.
**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-algorithm)

Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Conservation and Maxwell relaxation in a homogeneous DSMC collision component: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-validation)

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en): Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-algorithm)

Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Discrete-ordinate radiation transport through an absorbing slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-validation)

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Independent fluid/MHD comparisons and CT/GLM

- [Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en): Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.
**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-algorithm)

Reuse the published first-order Rusanov/forward-Euler solvers: shared corner-EMF discrete curl for CT and cell-centered hyperbolic/parabolic GLM cleaning. Independent Athena++ uses HLLD, PLM and RK2.

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Orszag–Tang: CT, GLM and independent Athena++: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-validation)

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
- [Brio–Wu against an independent HLLD implementation](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en): Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.
**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-algorithm)

Atlas uses MC reconstruction and SSPRK2; the independent C++ reference uses HLLD, PLM and RK3. Implementations differ while sharing the HLLD flux family.

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Brio–Wu against an independent HLLD implementation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) (`brio-wu`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-validation)

Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Shu–Osher: independent reference and mesh refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en): Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.
**Methods used**

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-algorithm)

Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Shu–Osher: independent reference and mesh refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-validation)

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [GLM longitudinal mode: analytic damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en): Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution.
**Methods used**

- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-algorithm)

Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![GLM longitudinal mode: analytic damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-validation)

Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## CSVR and Langevin: distributions, fluctuations and correlations

- [Exact CSVR bath: conditional laws, fluctuations and kinetic correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en): Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations.
**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-algorithm)

Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-validation)

Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en): Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.
**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-algorithm)

Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-validation)

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference · Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en): Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.
**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-algorithm)

Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-validation)

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Independent validation of nonlinear reaction–diffusion and pattern formation

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en): Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-algorithm)

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-validation)

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en): Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-algorithm)

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-validation)

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Multimodal MCMC: independent checks of poor mixing and convergence diagnostics

- [Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en): Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.
**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-algorithm)

Local scale.8; mixed uses y=−x+.8Z with probability.1, otherwise y=x+.8Z. The state-independent mixture is symmetric q(y|x)=q(x|y), so MH uses the log-target ratio. Chains use independent PCG64 streams, with no adaptation or removal of rejected states.

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Multimodal MCMC: trapping, false reassurance and a global proposal: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en) (`mcmc-bimodal-mixture`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-validation)

Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en): Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.
**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-algorithm)

Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-validation)

62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## CT and GLM: matched controls, independent checks and grid/time convergence

- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en): Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.
**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-algorithm)

Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) (`advected-magnetostatic-equilibrium`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-validation)

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en): Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.
**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-algorithm)

Primary runs use fixed alpha=ch=3 Rusanov/forward Euler and grid-independent GLM kappa2. Independent C++ Athena++ uses HLLD/PLM/RK2/upwind CT. Continuous initial fields agree; Athena’s face/primitive discretization is not identical.

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Orszag–Tang: matched CT/GLM and converged independent references: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-validation)

Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
- [Initial-constraint preservation by CT and active GLM cleaning: nonphysical control](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en): Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.
**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-algorithm)

Use the same fully coupled MHD code. With y-invariance andBy=vy=0, the GLM Bx/psi subsystem decouples from fluid feedback, allowing a separately constructed2x2 discrete Fourier symbol and forward-Euler matrix power. Compare kappa2/0 at identical dt and LLF viscosity, separating B/psi phase exchange from physical damping.

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-validation)

Check preservation of the initial CT defect, nonzero GLM psi, independent FE agreement for bothBx/psi, positive density/pressure, and conserved physical E/mass. Test the kappa2/0 ratio of auxiliary wave energy W=mean(Bx²+psi²/ch²), separating FE, semidiscrete-exponential and continuum-Fourier references.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Numerical foundations: conditioning, residuals, convergence and independent references

- [AMG: conditioning, anisotropy, residual and forward error](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en): Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.
**Methods used**

- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-algorithm)

Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![AMG: conditioning, anisotropy, residual and forward error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-validation)

Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en): Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.
**Methods used**

- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en) (`qr-svd`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-algorithm)

Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![QR/SVD: prescribed spectra, perturbation gain and numerical rank: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) (`matrix-factorization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-validation)

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en): Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.
**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-algorithm)

Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-validation)

Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en): Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.
**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-algorithm)

Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-validation)

Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Particles and transport: independent references, conservation and statistical error

- [Ewald: asymmetric-cell energies and forces versus independent theta integration](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en): Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.
**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-algorithm)

Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Ewald: asymmetric-cell energies and forces versus independent theta integration: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-validation)

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [SPME: mesh, interpolation order, mesh phase and conservation](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en): Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.
**Methods used**

- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) (`pme`)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) (`spme`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-algorithm)

Use 16³/24³/40³ meshes, orders four/six and three translations relative to the mesh. Differentiate FFT reciprocal energy through assignment weights; real/self terms share the primary Ewald implementation.

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![SPME: mesh, interpolation order, mesh phase and conservation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en#spme-convergence-en-validation)

Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [FMM: direct and analytic references, order and tree depth](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en): Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.
**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-algorithm)

Retain P2M/M2M/M2L/L2L and near P2P; compare orders 2/4/8/12 and depths two/three. References include independent Cartesian direct sums, a closed-form charge pair and regular-polygon radial/far-field identities.

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![FMM: direct and analytic references, order and tree depth: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en#fmm-convergence-en-validation)

Measure maximum absolute potential/field errors, actual far translations, rotation/translation differences and net charge-weighted force. Detect an inaccurate low-order control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en): Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.
**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-algorithm)

CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![PIC: mesh/time convergence, invariants and particle noise: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-validation)

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference · Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.
- [DSMC collision component: finite-N equilibrium, invariants and statistical error](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en): Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.
**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-algorithm)

Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![DSMC collision component: finite-N equilibrium, invariants and statistical error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-validation)

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
- [Radiation transport: space/angle convergence and photon statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en): Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-algorithm)

Use upstream finite volumes and Gauss-Legendre ordinates; exact exponential propagation removes spatial error in the angle series. Monte Carlo independently tracks survival/absorption using mu=sqrt(U) and exponential optical paths.

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Radiation transport: space/angle convergence and photon statistics: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en#radiation-convergence-en-validation)

Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Operator splitting: Lie–Trotter and Strang on the same reaction–diffusion problem

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en): Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.
**Methods used**

- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) (`lie-trotter`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-algorithm)

Lie–Trotter uses diffusion(h) then reaction(h); Strang uses diffusion(h/2), reaction(h), diffusion(h/2), always passing the updated state. Both apply the exact exponential of the centered-FD diffusion matrix by FFT and the same implicit-midpoint reaction/Newton tolerance 2e−13 with at most 12 residual evaluations. The reaction flow is a second-order approximation, not exact. No clipping, adaptive steps or fallback; nonconvergence is failure.

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-validation)

The reference independently assembles the SAME FD semidiscretization with a real-space sparse matrix and separately written reaction RHS, then integrates it unsplit with Radau. Tighter Radau and separate DOP853 runs measure reference sensitivity relative to the finest Strang error. Norms are per-species mean L1, RMS L2 and maximum L∞, then the worse species; refinement uses the maximum across the four common positive observation times. Also record Newton-tolerance sensitivity, positive tested substeps, reaction source/sink balance and reversed-Lie ordering.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.

## Noh shocks: exact reference, origin heating and refinement

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en): An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm)

Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The scoped planar, cylindrical-radial and spherical-radial forms of ideal-gas Euler. This example defines the geometric source, outer inflow and exactly zero initial pressure in its formulas and fixed input.


**Problem figure**

![Noh shocks: zero-pressure planar, cylindrical and spherical flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation)

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

## Noh:2D Cartesian flow and grid orientation error

- [Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en): A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.
**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-algorithm)

Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional Cartesian Euler without a geometric source, evolving density, both momenta and energy over the full square.


**Problem figure**

![Noh problem: an actual 2D Cartesian Euler calculation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-validation)

Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

## Sedov–Taylor point blast: lightweight spherical-radial validation

- [Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en): A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.
**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-algorithm)

Piecewise-constant Rusanov fluxes on spherical shells with SSPRK2/Heun. The radial-momentum source p(A_right-A_left)/V is integrated at the same RK stages, with a stationary uniform-pressure balance test. CFL.4 uses the reciprocal maximum (|u|+c)/(V/(A_left+A_right)), comparing with the remaining interval before division. No pressure seed, floor, cell repair or hidden timestep retry; an invalid stage retains raw conserved values and history and fails.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The one-dimensional spherical-radial ideal-gas Euler system. This example defines origin reflection, geometric source, finite-radius energy deposition and outer boundary in its fixed input.


**Problem figure**

![Sedov–Taylor point blast: lightweight spherical-radial validation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-validation)

Original r1 passed22 tests and48 gates on Mac, but its public-ZIP Linux run failed when warnings-as-errors raised a cold-tail CFL overflow. Revision r2 uses the algebraically equivalent reciprocal maximum-rate evaluation while preserving the original inputs, reference and48 acceptance gates. A new r2-specific pre-execution hash contract precedes23 tests and all four calculations/48 gates passing with warnings as errors. Original sources, contract and actual Linux-failure evidence remain archived. The independent reference integrates the similarity ODE with DOP853, normalizes energy, uses a regular asymptote for xi<.001 and split shell quadrature at the shock. Orders16/32, core cutoff and ODE tolerance are checked separately. The unmodified pinned ExactPack evaluator was independently run at6001/12001 points and compared away from the center/jump with its preregistered5e-4 criterion. Beta=1.15166641793, Rs(.05)=.34746791233. Origin/shock-inclusive volume-weighted density L1 within r<=1.2Rs is.17257/.12785/.07458 and pressure L1 is.18148/.13939/.07615. Finest shock error is1.096 cells; maximum relative discrete-budget residual is about8.89e-16.

- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en) (`sedov`; Same-problem reference · Semi-analytic reference)

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

## Double Mach reflection: lightweight grid verification

- [Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en): Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.
**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-algorithm)

The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional compressible Euler conservation laws with gamma1.4. This example fixes the Mach10 incident shock, inflow/outflow, reflecting wall and moving-shock top boundary.


**Problem figure**

![Double Mach reflection: lightweight grid verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-validation)

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference · Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

## Mach-3 forward-facing step: lightweight 2D verification

- [Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en): Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.
**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-algorithm)

Published Numart piecewise-constant HLL, unsplit x/y divergence and Heun/SSPRK(2,2) become a standalone package. Six boundary categories integrate the actual fluxes at both RK stages with identical weights. CFL.4, at most20000steps per grid. Every predictor/update checks positive density and pressure. No state floor, repair or hidden retry; invalid stages retain raw arrays/completed history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional compressible Euler conservation laws with gamma=1.4. Fixed inputs define uniform Mach-3 inflow, reflecting channel/step walls and right outflow.


**Problem figure**

![Mach3 forward step: wall budgets and grid verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-validation)

Inputs, acceptance,24 unit checks and numerical source were frozen before the first primary test/PDE execution. Checks cover analytic Mach3 normal-shock Rankine-Hugoniot identities, uniform parallel-channel flow, zero stationary-wall mass/energy flux, step-pressure force orientation, actual four-component budgets and raw failure retention. Newly executed separate C++17 MUSCL/generalized-minmod theta1.5/HLL/Heun references atNy80/160 are conservatively restricted for whole-fluid density/pressure L1 comparison. Ordinary public-ZIP verification reads saved reference data; reference source, contracts and execution records are bundled. The first referenceNy160 exhausted its preregistered120second budget; that actual timeout is preserved. A reference revision removed only unnecessary diagnostic-string allocation and was repinned before first primary execution; physical inputs,arithmetic,CFL and acceptance values did not change. All24 tests, three final-time runs and45 gates passed with-W error. Primary density L1=.14754/.12878/.10265, pressure L1=.19373/.16015/.12242 and last-pair density slope=.327. Reference80/160 increments=.02636/.03063, about.257/.250 of the finest primary differences. Maximum four-component relative boundary-budget residual=2.99e-13; all integrated wall mass/energy fluxes are zero. The three primary grids took about46seconds on the original Mac; revised reference80/160 took about8/65seconds.

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference · Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

## Low-Mach isentropic vortex: preconditioned Roe flux verification

- [Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en): The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.
**Methods used**

- [Roe](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en) (`roe`)
- [Low-Mach PDE preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en) (`low-mach-preconditioning`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-algorithm)

Both finite-volume variants use the same unlimited centered primitive-MUSCL reconstruction,  the physical Euler flux and SSPRK(3,3); only Roe dissipation is replaced by D=P^-1|PA|. At each Roe state use the total-speed Mach with mu=min(1,max(M_local,M_infinity)) and delta=1/mu-1, applying the primitive Miczek matrix through conserved-variable Jacobians. A degree-two characteristic polynomial applies the matrix absolute value; a separate dense eigendecomposition checks it. Physical time and sound speed are unchanged; acoustic CFL=0.2 remains. Reconstructed faces and all three stages check positive density and pressure, without limiters, floors, repair, hidden retries or pseudo-time iteration. A forward-Euler amplification counterexample prevents claiming SSP/TVD or general nonlinear stability from the integrator name.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Unforced 2D ideal-gas Euler is advanced in the original conservative variables and physical time. Fixed inputs use gamma=1.4, a periodic 20×20 box and a consistently scaled isentropic vortex with Mach-dependent background pressure.


**Problem figure**

![Low-Mach isentropic vortex: preconditioned Roe flux verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-validation)

The original 32 unit tests passed, but one of 143 first-order spatial gates failed: finest M_infinity=0.01 whole-domain dynamic pressure error 0.16537 exceeded the fixed 0.1 threshold. Original sources, contract, all twelve fields and the failed global pressure plot are retained. Revision 2 gives both fluxes the same unlimited centered primitive MUSCL and adds three checks for reconstruction, raw face failure and actual-RHS linearization against independent matrices. Inputs, physical time, CFL and acceptance bytes are unchanged; the revised 35-test/143-gate contract was frozen before revision execution.  Checks cover Roe conserved jumps and physical-flux differences, dense-matrix dissipation, the three stages and raw invalid-stage retention. Each background Mach/flux has 17^2 constant-state Fourier modes and powers 1/10/100 in stated physical acoustic-energy variables. Pressure errors divide by rho_infinity*|U_infinity|^2 rather than the large p_infinity; velocity errors divide by analytic vortex perturbations. Initial R_h-q_t for the translating analytic field is retained as truncation error, not converged steady residual. Revision 2 passed all 35 tests, twelve runs and 143 gates with -W error, taking about 4.4 seconds on the original Mac. At finest M_infinity=0.01, relative velocity L1 was 0.07411 for Roe and 0.01847 for preconditioning; fixed-core pressure errors were 0.04871/0.0006325. Whole-domain pressure errors were instead 0.01194/0.01260, slightly worse with preconditioning; M_infinity=0.1 similarly gave 0.0006653/0.0006737. Maximum relative conserved-budget residual was 4.24e-14. Dynamic-scale Gauss8/16 maximum difference was 4.08e-11 and analytic Euler substitution residual 1.09e-16. Sampled SSPRK3 spectral radii and stated energy-scaled matrix powers had maximum 1. Forward Euler exceeded 1 for both MUSCL variants, reaching about 1.03560 for preconditioning at M_infinity=0.01.

- [Isentropic vortex: analytic Euler field for low-Mach comparisons](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en) (`isentropic-vortex`; Same-problem reference · Analytic reference)

Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.

## Guderley converging shock: lightweight spherical-radial verification

- [Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en): An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.
**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-algorithm)

First-order spherical finite volumes use face area4pi*r^2 and shell volume4pi*delta(r^3)/3. Shared HLL flux divergence plus the radial-momentum pressure source p_i*delta(A)/V is advanced by Heun at CFL0.4. The center is reflecting with zero face area; the outer similarity state is evaluated at both actual RK times. All three conserved budgets integrate the actual boundary flux and geometric source using the same Heun weights. There are no state floors, pressure repairs or hidden step retries.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The one-dimensional spherical-radial ideal-gas Euler system with zero upstream pressure and gamma=1.4. The fixed input defines a pre-collapse interval, similarity initial field, boundaries and shell averaging.


**Problem figure**

![Guderley converging shock: lightweight spherical-radial verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-validation)

The33 unit checks and55 gates over three refinements were fixed before execution and passed with warnings treated as errors. Checks cover the zero-sound-speed cold HLL branch, geometric static-pressure balance, shared-flux budgets, actual two-stage boundary times and raw failed-stage retention. Full-volume L1 is shown alongside the predetermined r>=0.8*Rs shock/nonzero-flow region, so cold inner gas does not hide active errors. Maximum density/pressure differences and the saved shock trajectory remain visible. The semi-analytic reference uses the pinned LANL ExactPack eigenvalue routine and ODE through a cached pre-collapse-only adapter. It is not an independently reimplemented similarity ODE; the separately implemented finite-volume Euler evolution is compared against that reference. Full-volume density L1 is0.02345/0.01339/0.007722 and pressure L1 is0.03277/0.01743/0.009477. Density L1 in the predetermined r>=0.8*Rs region also decreases:0.02414/0.01378/0.007948. The finest measured shock radius is0.530273 against similarity0.533989, about2.54 cells apart. The maximum scaled three-component budget residual is8.85e-16. Minimum internal energy and sound-speed-only roundoff guard evaluations are both0. The smooth-reference Euler finite-difference residual is8.24e-9 and finite-offset moving-jump residual4.40e-8. The older three-run execution with a newly computed similarity eigenvalue took about44.6 seconds on the original Mac. Public r2 passed all33 Linux tests in96.34 seconds, but its fixed-input runner timed out after the remaining23.31 seconds of the combined120-second test-plus-run budget. That failed replay and its sources are retained. The revision reuses the eigenvalue already obtained by actual ExactPack shooting, bound by SHA to its source and qualification, instead of shooting again in both normal processes. The critical-phase Cdiff residual and similarity ODE are freshly evaluated. Inputs, numerical criteria, Euler solver, fixed-input runner and120-second budget are unchanged. In the revision,33 unit tests and all three fixed inputs with55 gates completed sequentially within one120-second budget in about0.912s on the Mac. Initial,final,reference and saved-history arrays for all three grids were bit-identical to published r2, separately checking that reuse of the eigenvalue preserved the physical results.

- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en) (`guderley`; Same-problem reference · Semi-analytic reference)

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

## Euler double rarefaction: positivity at every stage

- [Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en): Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.
**Methods used**

- [Lax–Friedrichs](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en) (`lax-friedrichs`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Mean-preserving positive-state scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=en) (`positive-scaling`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-algorithm)

Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Unforced one-dimensional ideal-gas Euler at gamma=1.4 evolves cell means of density, momentum and total energy using linear conservative MUSCL reconstruction and shared Lax–Friedrichs fluxes.


**Problem figure**

![Euler double rarefaction: positivity at every stage: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-validation)

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference · Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

## Zalesak-type 2D rotation: conservation, bounds and shape error

- [Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en): Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
**Methods used**

- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-algorithm)

Use analytic divergence-free normal face averages and one shared upwind flux per interface. Both piecewise-constant donor-cell and mean-preserving directional-minmod MUSCL use SSPRK(3,3). The four face-midpoint mean equals the cell mean; individual outgoing-face Courant<=1/4 gives a convex FE update. Check the actual .20 bound at every stage. No transported-state clipping/floors or rejected/retried steps are used.

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

- [Two-dimensional rotational advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en) (`rotational-advection`)

Two-dimensional conservative transport of q with prescribed a=-omega(y-yc), b=omega(x-xc), whose divergence is zero. Shared face velocities and numerical fluxes update scalar cell means.


**Problem figure**

![Zalesak-type 2D rotation: conservation, bounds and shape error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-validation)

Freeze26 unit checks and158 gates across eight fixed runs before execution. Retain min/max of every FE candidate/SSP convex mean, shared-flux mass budgets, reconstruction mean preservation and three-grid L1/Linf/relative-L2 errors. Independent circle/convex-polygon intersection means are qualified against SciPy vertical-slice quadrature, total area and first moments. Also check quarter/half/three-quarter-turn errors and centroids so a wrong direction or speed cannot hide behind a full-turn return.

- [Zalesak-type slotted disk: rigid rotation and geometric cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en) (`zalesak-rotation`; Same-problem reference · Analytic reference)

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

## WENO critical points and epsilon dependence

- [WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en): Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.
**Methods used**

- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en) (`weno-js`)
- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) (`weno-z`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-algorithm)

Share three candidates, linear weights(.1,.6,.3) and JS indicators. Normalize JS d/(beta+epsilon)² or Z d[1+(|beta0−beta2|/(beta+epsilon))²]. Use epsilon10⁻⁴⁰,10⁻⁶,h². Actual transport uses shared upwind face fluxes and classical RK4 at Courant.1 without state clipping/retries.

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`)

Local polynomials have center x=0 and target h/2, h=1/64…1/512. Transport uses periodic[0,1], unit speed, q₀=cos(2πx)+.1sin³(2πx), T=1 and32/64/128 cells. All evolved states/references are FV cell means, not point samples.


**Problem figure**

![WENO-JS/Z: fixed critical-point and epsilon comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-validation)

Pre-run contract fixes72 local reconstructions,24 PDE runs and36 pytest checks. Qualify analytic means against independent Gauss12 quadrature; retain local errors/weights, transport L1/L2/Linf, mass, stage finiteness, intermediate times and shared-flux budgets. Six finest-grid half-dt differences must be at most10% of corresponding continuum errors.

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference · Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference · Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference · Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## Shallow water: topography, lakes and dry beds

- [SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en): Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.
**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-algorithm)

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

- [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en) (`shallow-water-bed`)

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.


**Problem figure**

![SWASHES topographic flow: lakes and nonzero steady discharge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-validation)

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

- [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en) (`lake-at-rest-bed`; Same-problem reference · Analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

- [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en) (`swashes-bernoulli`; Same-problem reference · Semi-analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
- [Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en): Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.
**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-algorithm)

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`)

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.


**Problem figure**

![Dry-bed dam break: actual wetting and dry states: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-validation)

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en) (`ritter-dry-bed`; Same-problem reference · Analytic reference)

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

- [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en) (`swe-dry-bed`; Related-model reference · Analytic reference)

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

## Nonperiodic walls: cavity and manufactured flow

- [Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en): March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-algorithm)

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.


**Problem figure**

![Re100 lid-driven cavity: Ghia centerline comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-validation)

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference · Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference · Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
- [Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en): Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-algorithm)

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en) (`forced-incompressible`)

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.


**Problem figure**

![Nonperiodic wall MMS: velocity, shear and pressure operator: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-validation)

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

- [Wall manufactured solution: polynomial velocity and separate pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en) (`wall-mms`; Same-problem reference · Manufactured solution)

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

## Level sets: 2D circle translation and rigid rotation

- [2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en): Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.
**Methods used**

- [Level-set method](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en) (`level-set`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-algorithm)

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en) (`level-set-advection`)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.


**Problem figure**

![2D level-set circle translation: interface, area and redistancing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-validation)

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en) (`level-set-translation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en) (`level-set-rotation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
- [2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en): Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.
**Methods used**

- [Level-set method](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en) (`level-set`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-algorithm)

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en) (`level-set-advection`)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.


**Problem figure**

![2D rigid rotation of an off-center level-set circle: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-validation)

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en) (`level-set-translation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en) (`level-set-rotation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

## Spectral elements and FR: small comparisons with existing FEM/DG

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en): Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.
**Methods used**

- [Spectral element method (SEM)](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en) (`spectral-element`)
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-algorithm)

C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.


**Problem figure**

![2D spectral-element Poisson: P1 FEM comparison and h/p refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en#sem-poisson-2d-en-validation)

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
- [1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en): Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.
**Methods used**

- [Flux reconstruction (FR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en) (`flux-reconstruction`)
- [Discontinuous Galerkin / Legendre](https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en) (`dg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-algorithm)

p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.


**Problem figure**

![1D periodic FR advection: Radau correction and published DG comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-validation)

Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference · Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference · Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference · Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## KH/RT initial growth and independent linear references

- [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en): Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en) (`forced-vorticity`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.


**Problem figure**

![KH initial growth in a smooth periodic shear layer: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [KH initial growth: independent linear Fourier-Galerkin reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en) (`kh-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
- [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en): Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en) (`boussinesq-buoyancy`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.


**Problem figure**

![RT initial growth in smooth Boussinesq double layers: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [RT initial growth: linear Boussinesq double-layer IVP reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en) (`rt-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

## Independent MHD transport, waves and compression comparisons

- [Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en): Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.
**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.


**Problem figure**

![Circular Alfven wave: full-state refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference · Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.
- [Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en): Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.
**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.


**Problem figure**

![Magnetic loop: independent 2D reference and refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Magnetic loop: pinned independent Athena++ final-field reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en) (`magnetic-loop-independent`; Related-model reference · Finite-grid numerical reference)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.
- [Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en): Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.
**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.


**Problem figure**

![Late Orszag-Tang: independent reference and compression structure: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

## Corner singularities, curved coordinates and Neumann/Robin boundaries

- [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en): Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.
**Methods used**

- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-algorithm)

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.


**Problem figure**

![L-corner P1 FEM: grading and separate mesh distortion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-validation)

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

- [L-corner singularity: harmonic field and separate smooth MMS](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en) (`lshape-fem`; Same-problem reference · Analytic reference)

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
- [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en): Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.
**Methods used**

- [Q1 FEM for scalar diffusion and mapped vector BVPs](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-algorithm)

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [Variable-viscosity vector stress boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en) (`variable-viscosity-vector`)

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.


**Problem figure**

![Annular variable-viscosity vector PDE MMS: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-validation)

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

- [Annular vector-viscous MMS: force qualified by independent stress differentiation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en) (`annular-viscous-mms`; Same-problem reference · Manufactured solution)

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
- [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en): Solve singular2D Poisson with compatibility/gauge and reject incompatible source.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-algorithm)

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.


**Problem figure**

![Pure Neumann compatibility and mean gauge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-validation)

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

- [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en) (`poisson-neumann`; Same-problem reference · Manufactured solution)

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
- [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en): Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-algorithm)

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.


**Problem figure**

![2D mixed Robin MMS and boundary flux: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-validation)

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

- [Mixed Robin: 2D analytic field and independent normal flux](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en) (`poisson-robin`; Same-problem reference · Manufactured solution)

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

## Nonuniform ALE transport and2D rotating shallow-water waves

- [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en): Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.
**Methods used**

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) (`ale`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-algorithm)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`)

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.


**Problem figure**

![ALE scalar transport on genuinely nonuniform moving cells: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-validation)

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference · Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
- [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en): Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.
**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-algorithm)

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

- [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en) (`linear-rotating-shallow-water`)

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.


**Problem figure**

![Actual2D C-grid rotating shallow-water time advance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-validation)

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

- [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en) (`cgrid-rotating-wave`; Same-problem reference · Analytic reference)

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

## SRHD collision and nonlinear SRMHD Alfven wave

- [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en): Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.
**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-algorithm)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`)

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.


**Problem figure**

![SRHD symmetric two-shock collision: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-validation)

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference · Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.
- [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en): Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.
**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-algorithm)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`)

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.


**Problem figure**

![SRMHD finite-amplitude circularly polarized Alfvén wave: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-validation)

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference · Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

## MG/AMG for coefficient jumps and rotated anisotropy

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en): Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.
**Methods used**

- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-algorithm)

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.


**Problem figure**

![Checkerboard diffusion: shared flux, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-validation)

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en) (`checkerboard-diffusion`; Same-problem reference · Finite-grid numerical reference)

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.
- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en): Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.
**Methods used**

- [Q1 FEM for scalar diffusion and mapped vector BVPs](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-algorithm)

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.


**Problem figure**

![Rotated diffusion: full-tensor Q1, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-validation)

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en) (`rotated-anisotropic-diffusion`; Same-problem reference · Manufactured solution)

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

## Neutral slabs: corrected3P and genuine2P references

- [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en): Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.
**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)
- [Slab electrostatics and 2D-periodic Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=en) (`slab-ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-algorithm)

Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

- [Coulomb electrostatics with mixed periodic boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en) (`coulomb-electrostatics`)

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.


**Problem figure**

![Neutral rectangular slab: genuine2P reference and YB: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en) (`neutral-slab-yb`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-validation)

Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.

- [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en) (`neutral-slab-yb`; Same-problem reference · Semi-analytic reference)

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

## 3D1/r kernels: expansions,trees and force checks

- [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en): Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.
**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-algorithm)

Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.


**Problem figure**

![Actual3D1/r FMM: multilevel translations, force and ownership: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-validation)

Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.

- [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en) (`fmm3d-inverse-r`; Same-problem reference · Finite-grid numerical reference)

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

## Gravitational trajectories: Kepler and softened finite particles

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en): Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.
**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-algorithm)

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.


**Problem figure**

![Unsoftened Kepler two-body time error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-validation)

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference · Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en): Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.
**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)
- [Barnes–Hut octree](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en) (`barnes-hut`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-algorithm)

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.


**Problem figure**

![Short-time32body dynamics from a cold Plummer-density sample: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-validation)

Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en) (`gravity-plummer-short`; Same-problem reference · Finite-grid numerical reference)

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

## Warm PIC: Landau damping and two-stream instability

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en): Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.
**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-algorithm)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.


**Problem figure**

![Warm PIC linear Landau damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en) (`thermal-landau-damping`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en): Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.
**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-algorithm)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.


**Problem figure**

![Warm PIC two-stream initial growth: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en) (`thermal-two-stream`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

## PIC checks against independent spatial kernels

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en): Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.
**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-algorithm)

The independent path owns scalar deposition, explicit complex DFT sums and scalar gathering; it imports no primary spatial routines. Mathematical CIC, Nyquist convention, velocity-Verlet and initial arrays are intentionally shared.

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.


**Problem figure**

![Independently coded PIC spatial pipeline: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-validation)

19pytest and58/58fixed gates passed. Compare six pairs=twelve self-consistent trajectories at all13states; maximum differences:x8.88e-16,v3.33e-16,E8.33e-16,rho2.89e-15. Shared pytest+main.392s. Initial small pytest retained17/18with a periodic-index failure; integer wrapping was corrected before the first fixed main batch.

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference · Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

## Finite-Knudsen Couette and Fourier flows

- [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en): Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`)

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC finite-Kn Couette flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) (`dsmc-couette`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-validation)

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Finite-Kn hard-sphere Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en) (`dsmc-couette`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
- [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en): Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`)

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC finite-Kn Fourier heat conduction: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-validation)

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Finite-Kn hard-sphere Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en) (`dsmc-fourier`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

## Mach2 planar shock with hard-sphere DSMC

- [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en): Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories. Edition2026-11-24 only reuses immutable reservoir coefficients and an inverse-CDF residual at unchanged v,fuses concatenation in unchanged keep-left-right order,and reversibly narrows range-checked integer sort keys to uint8 before the same stable sort. Original permutation/RNG calls,equal-key particle order,collision pairs and scientific inputs remain unchanged. The first three changes passed163component checks; a separate348check study qualifies the sort-key composition with exact byte/RNG comparisons. Neither is a new main run; full saved-science equality remains pending.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`)

{"kind":"shock","cells":192,"length":16,"weight":0.005208333333333333,"dt":0.01,"burn_in":20,"sample_time":20,"blocks":5,"bins":64,"sample_every":10,"hist_velocity":[-4,7]} Twelve independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC Mach2 planar shock: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-validation)

Predeclare20pytest per group and15new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run. Preserve all81old gates and add48new-run gates=129. Primary12seed t95 usesdf11,reference4seed usesdf3; descriptive approximate-normal whole-seed intervals,not unconditional adaptive-study coverage. This new edition main has not run at contract freeze. Retain all20pytest,15runs,129gates and the original shared120s outer deadline,then compare every saved scientific array/history/metric with the immutable successful Nov23baseline. No independent reference is regenerated.

- [Mach2 planar hard-sphere shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en) (`dsmc-planar-shock`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

## LBM lid-driven cavity at Re100

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en): Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.
**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-algorithm)

Standard D2Q9equilibrium/BGK collision, nonperiodic link streaming and moving halfway reflection atq=.5. Sum actual population wall impulses without density repair/interior reset. Compile shipped C++17temporarily and call fromPython.

$$
f_i^{eq}=w_i\rho[1+3c_i\cdot u+\frac92(c_i\cdot u)^2-\frac32|u|^2],\quad\nu_\ell=(\tau-1/2)/3
$$

$$
f_{\bar i}(x,t+1)=f_i^\star(x,t)-6w_i\rho_0c_i\cdot u_w,\quad\rho_0=1
$$

$$
\mathrm{Re}=UL/\nu=100,\quad t_\star=100
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.


**Problem figure**

![LBM Re100 cavity: actual2D fields and Ghia centerlines: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-validation)

22pytest and37case gates. Fixed60k/80k/120ksteps reach t*=100with90/95/100saved. Finest u/v max error.03,vortex distance.06,late relativeL2 change2e-4andmass/wall-inclusive momentum gates are frozen.

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference · Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference · Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

## LBM Taylor–Green vortex and finite-Mach errors

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en): Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.
**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-algorithm)

Standard BGK and fully periodic streaming. Convert/gauge pressure ascs²(rho−meanrho)(dx/dt)². No analytic field injection after initialization; independently qualify the continuum field by Fourier differentiation.

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.


**Problem figure**

![LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-validation)

22pytest and79gates,sixfixed evolutions. Require finest velocity relativeL2.03,pressure.08,combined velocity order≥1.5,energy.03anddivergence/periodic mass/mean momentum. Save five analyticPDEqualifiers distinctly. Retain the initial N16energy failure5.0018%; refine only thatcoarsegrid to24against the unchanged3%gate. Report order only for thefinest32/64pair.

- [Viscous flow / 2D Taylor–Green](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en) (`taylor-green`; Related-model reference · Analytic reference)

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en) (`lbm-taylor-green`; Related-model reference · Analytic reference)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

## Annular Couette control for curved-wall LBM

- [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en): Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.
**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-algorithm)

Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.


**Problem figure**

![Curved LBM annular Couette control: velocity,pressure andtorque: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-validation)

Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.

- [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en) (`lbm-annular-couette-control`; Same-problem reference · Analytic reference)

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

## LBM curved walls and a Re20 cylinder

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en): Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.
**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-algorithm)

StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.


**Problem figure**

![Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-validation)

Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en) (`lbm-cylinder-re20`; Same-problem reference · Finite-grid numerical reference)

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

## Isotropically scattering slabs and continuum-angle references

- [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en): Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-algorithm)

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.


**Problem figure**

![Isotropic scattering in a finite slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-validation)

Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.

- [Isotropically scattering slab: continuous-angle Fredholm flux reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en) (`isotropic-scattering-slab`; Same-problem reference · Semi-analytic reference)

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

## Non-equilibrium radiation: distinct diffusion and transport

- [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en): Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-algorithm)

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

- [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en) (`non-equilibrium-diffusion-exchange`)

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.


**Problem figure**

![Su–Olson1996 non-equilibrium diffusion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-validation)

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

- [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en) (`su-olson-diffusion1996`; Same-problem reference · Semi-analytic reference)

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.
- [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en): Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-algorithm)

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.


**Problem figure**

![Su–Olson transport with an independently published analytical table: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-validation)

Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.

- [Su–Olson transport: primary2023author-provided analytical benchmark data](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en) (`su-olson-transport1997`; Same-problem reference · Finite-grid numerical reference)

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

## 2D shadows,beams and M1 closure

- [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en): Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-algorithm)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.


**Problem figure**

![Two-dimensional absorber shadow and M1 transport: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-validation)

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference · Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
- [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en): Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.
**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-algorithm)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.


**Problem figure**

![Opposing beams and information loss in the M1 closure: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-validation)

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en) (`opposing-beams2d`; Same-problem reference · Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

## Weak/strong SDE errors and sampling uncertainty

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en): Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-algorithm)

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.


**Problem figure**

![GBM weak bias and Monte Carlo error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-validation)

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference · Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference · Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en): Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-algorithm)

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.


**Problem figure**

![OU weak moments with joint Brownian coupling: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-validation)

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference · Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en): Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.
**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-algorithm)

Milstein adds.5sigma²X(dW²-h). All methods/levels share the fine driver and one exact terminal array. No state repair.

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.


**Problem figure**

![Milstein and EM on identical Brownian paths: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-validation)

Qualify cancellation-prone analytic MSE by Decimal80/120and independent one-step GH. Gate squared-error5SE calibration,fixed-three-level RMS rates and finest advantage.64paired path-block jackknife describes slope uncertainty.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference · Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference · Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

## Importance sampling and correlated-Gaussian diagnostics

- [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en): Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.
**Methods used**

- [Monte Carlo integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en) (`monte-carlo`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-algorithm)

Ordinary mean ofY=1(X>a)exp(-aX+a²/2),without random weight normalization or proposal tuning. Retain direct zero-hit counts with Clopper-Pearson intervals.

$$
\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}
$$

$$
\mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)
$$

- [Gaussian probability measures: tails and correlated targets](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en) (`gaussian-probability-model`)

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.


**Problem figure**

![Ordinary importance sampling of a normal rare tail: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en) (`normal-tail-importance`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-validation)

Qualify moments1..4 by independent positive quadrature. Gate known-variance5SE,batch variance,analytic variance reduction and omitted-weight negative control. Report known-variance normal95IScoverage separately for64trials per threshold/prefix.

- [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-normal-tail-importance-en) (`normal-tail-importance`; Same-problem reference · Analytic reference)

Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.
- [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en): Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.
**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-algorithm)

Symmetric random-walk MH retains rejected states. Compute original-scale meanESS/MCSE separately for8observables;rank bulkESS is not substituted.

$$
\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]
$$

$$
\operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}
$$

- [Gaussian probability measures: tails and correlated targets](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en) (`gaussian-probability-model`)

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.


**Problem figure**

![Joint target and MCSE for a correlated bivariate Gaussian: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en) (`correlated-gaussian-mcmc`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-validation)

Gate all full-prefix observables in4preconditioned chainsets by Rhat/ESS/MCSE/knownmoments. Match exact dataSHAand640values from128scalar arrays in a separateArviZ0.20process. Target law is separately checked by analytic Gaussian moments. All640comparisons use the immutable same-data fixture;8freshchainsets independently receive the unchanged physical/mixing gates. No portable generated-byte-identity claim.

- [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-correlated-gaussian-mcmc-en) (`correlated-gaussian-mcmc`; Same-problem reference · Finite-grid numerical reference)

Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.


Original code: MIT. Other materials: https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
