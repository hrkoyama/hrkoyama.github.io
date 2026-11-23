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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
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


Original code: MIT. Other materials: https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
