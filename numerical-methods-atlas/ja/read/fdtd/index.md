# Yee FDTD

Yee FDTD：真空モード・媒質界面・PMLの実装と検証

初版の真空2例に、第2版の誘電体界面と左右x方向PMLを追加しました。前半は真空の解析モード、後半は垂直入射のFresnel比較と、垂直・斜めパルスの境界反射を扱います。旧版のコード・図・数値は保持しています。

2次元TMz（Ez、Hx、Hy）の自作教育用コードです。初版の検証では無次元の一様真空・電流/電荷源なしに限定し、周期平面波と完全導体（PEC）長方形空洞を連続解析解と比較しました。格子収束、数値分散、離散保存量、物理エネルギーの近似を別々に確認します。

モデル・単位・適用範囲


$$
\partial_t E_z=\partial_xH_y-\partial_yH_x,\qquad \partial_tH_x=-\partial_yE_z,\qquad \partial_tH_y=\partial_xE_z,\quad \epsilon=\mu=c=1.
$$
長さ・時間・場を規格化し、ε=μ=c=1とします。計算領域はLx=1、Ly=1.5、モード番号(m,l)=(1,1)。矩形・斜めの周期モードを使い、軸の入れ替えや磁場の符号を見逃さない構成です。分散媒質、損失、誘電体界面、外部励起は含みません。

Yee格子と時間をずらした更新


$$
\begin{aligned}H_{x,i,j+1/2}^{n+1/2}&=H_{x,i,j+1/2}^{n-1/2}-\frac{\Delta t}{\Delta y}(E_{i,j+1}^{n}-E_{i,j}^{n}),\\H_{y,i+1/2,j}^{n+1/2}&=H_{y,i+1/2,j}^{n-1/2}+\frac{\Delta t}{\Delta x}(E_{i+1,j}^{n}-E_{i,j}^{n}),\\E_{i,j}^{n+1}&=E_{i,j}^{n}+\Delta t\left(\frac{H_{y,i+1/2,j}^{n+1/2}-H_{y,i-1/2,j}^{n+1/2}}{\Delta x}-\frac{H_{x,i,j+1/2}^{n+1/2}-H_{x,i,j-1/2}^{n+1/2}}{\Delta y}\right).\end{aligned}
$$
Ezを格子点・整数時刻、Hxをy方向の半格子・半整数時刻、Hyをx方向の半格子・半整数時刻に置きます。各ステップは磁場を先に更新し、その磁場で電場を更新します。時刻0の電場と−Δt/2の磁場を解析式から初期化し、初期時刻のずれによる1次誤差を避けます。

周期境界では重複端点を持たず、差分が周期的につながります。PECでは壁上の接線電場Ez=0を固定し、電場の内部点のみを更新します。壁上に置かれた磁場成分の内積には半分の端点重みを与え、離散部分積分とエネルギー式を整合させます。

周期平面波の連続解析解


$$
\begin{gathered}k_x=2\pi m/L_x,\quad k_y=2\pi l/L_y,\quad\omega=\sqrt{k_x^2+k_y^2},\quad\phi=k_xx+k_yy-\omega t,\\ E_z=\cos\phi,\quad H_x=(k_y/\omega)\cos\phi,\quad H_y=-(k_x/\omega)\cos\phi.\end{gathered}
$$
電場と2成分の磁場を、それぞれの格子位置・時刻で評価します。位相速度の誤差は周波数から測り、場の誤差とは別に保存します。空間にサンプルした連続磁場は離散発散が厳密に0とは限らないため、磁場発散は初期値からの変化を調べます。

完全導体空洞の連続固有モード


$$
\begin{gathered}k_x=m\pi/L_x,\quad k_y=l\pi/L_y,\quad\omega=\sqrt{k_x^2+k_y^2},\\E_z=\sin(k_xx)\sin(k_yy)\cos(\omega t),\\H_x=-\frac{k_y}{\omega}\sin(k_xx)\cos(k_yy)\sin(\omega t),\quad H_y=\frac{k_x}{\omega}\cos(k_xx)\sin(k_yy)\sin(\omega t).\end{gathered}
$$
4辺の壁でEz=0となる定在波です。周期波とは異なる境界実装を使い、壁上の最大電場、固有角周波数、場の誤差を確認します。ここでの「空洞」はz方向に変化のない2次元断面であり、3次元の全固有モードを扱うものではありません。

CFL条件と離散分散関係


$$
\frac{\sin^2(\omega_h\Delta t/2)}{\Delta t^2}=\frac{\sin^2(k_x\Delta x/2)}{\Delta x^2}+\frac{\sin^2(k_y\Delta y/2)}{\Delta y^2},\qquad S=\Delta t\sqrt{\Delta x^{-2}+\Delta y^{-2}}入力ではCourant数の上限を0.7とし、S≥1は拒否します。解析解との比較時刻を厳密に1.1周期に合わせるため、必要な整数ステップ数を切り上げ、実際の時間刻みとSをわずかに小さくします。格子とともに時間刻みも細分化するため、示す次数は空間・時間を同時に細分化した収束です。空間次数と時間次数を個別に実測したという意味ではありません。

時間発展したモードの投影係数から3時刻の漸化式で周波数を測定し、連続ωへの近づき方と離散ωhとの一致を分けます。別テストでは離散波数に整合する磁場振幅で初期化し、離散固有モードが丸め誤差程度で再現されることを調べます。

離散保存量と物理エネルギーを分ける


$$
\begin{aligned}U_*^n&=\frac12\lVert E^n\rVert_h^2+\frac12\langle H^{n-1/2},H^{n+1/2}\rangle_h=\mathrm{constant},\\\bar H^n&=(H^{n-1/2}+H^{n+1/2})/2,\\ U_{\rm sync}^n&=\tfrac12(\lVert E^n\rVert_h^2+\lVert\bar H^n\rVert_h^2),\\ U_*^n&=U_{\rm sync}^n-\frac{\Delta t^2}{8}\lVert\operatorname{curl}_h E^n\rVert_h^2.\end{aligned}
$$
内積には格子面積とPECの境界重みを含めます。異なる半時刻の磁場の積を使うU*は、閉じた周期／PEC系で丸め誤差を除き保存されます。厳密なCFL不等式はこの修正エネルギーの正定値性にも関係します。整数時刻へ平均した磁場によるUsyncは物理エネルギーの2次近似ですが、厳密な保存量ではありません。

単位振幅の連続場では、周期進行波の全エネルギーはLxLy/2、空洞定在波ではLxLy/8です。12周期にわたってU*の相対変動とUsyncの変動幅を記録し、後者と解析的な全エネルギーとの差が格子・刻みの細分化で約2次に減ることを確認します。固有モードだけでなく、乱数で作った適合する場でもU*の保存をテストします。

固定入力と実測結果


$$
e_h=\left(\frac{\lVert E_h-E\rVert_h^2+\lVert H_h-H\rVert_h^2}{\mathcal N^2}\right)^{1/2},\qquad p=\frac{\log(e_h/e_{h/2})}{\log 2}.
$$
格子16×24、32×48、64×96を使用。連続解析解との場の誤差は、時間刻みを調整して厳密に到達する1.1周期の時刻で照合します。Hの誤差はEより半刻み前の実時刻で比較します。全場誤差の分母𝒩²は連続場の一定ノルム（周期波LxLy、空洞LxLy/4）です。電場・磁場の個別誤差もJSONに保存します。

固定入力の実測値。誤差と周波数は連続解析解に対して評価。問題格子 Nx × Ny全場の相対L²誤差観測次数相対周波数誤差離散エネルギー最大相対変動周期波16 × 240.021645—0.00312712.22e-16周期波32 × 480.00539262.00490.000779622.22e-16周期波64 × 960.00133092.01860.000192442.22e-16導体空洞16 × 240.0055511—0.000779624.441e-16導体空洞32 × 480.00135142.03830.000192444.441e-16導体空洞64 × 960.000333262.01974.7804e-052.22e-16周期平面波 · [JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/periodic-wave/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/periodic-wave/energy.csv)完全導体空洞 · [JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/pec-cavity/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/pec-cavity/energy.csv)許容値は固定入力のacceptanceに保存しています。全場誤差0.01以下、観測次数1.8以上、相対周波数誤差0.002以下、離散分散一致誤差10⁻⁹以下、U*相対変動2×10⁻¹¹以下を別々に判定します。壁上の電場0、磁場の初期発散の保存、Usyncの解析的全エネルギーに対する最大相対誤差0.003以下、およびその約2次の細分化も別々に判定します。Usyncの変動幅は診断値として保存します。

誘電体界面：Fresnelの振幅とエネルギー


$$
\eta_j=\sqrt{\mu_j/\epsilon_j},\quad r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\quad t=\frac{2\eta_2}{\eta_1+\eta_2},\qquad R=|r|^2,\quad T=\frac{\eta_1}{\eta_2}|t|^2,\quad R+T=1.
$$
非磁性・無損失・非分散媒質ε₁=1、ε₂=4、μ=1の平坦な界面へ、Gaussianパルスを垂直入射させます。x=8の界面を電場節点に一致させ、その点の誘電率を算術平均します。y方向には一様な2次元TMzの縮約です。解析値はr=−1/3、t=2/3、R=1/9、T=8/9です。

領域は16×1、初期中心x=4、幅0.5、比較時刻t=8、x格子160/320/640、y格子4です。入射波・反射波・透過波を連続解析式で別に評価し、電場振幅を射影で測ります。パケットエネルギーR,Tはε|E|²と磁場を含む積分から求め、振幅の二乗だけとは区別します。界面節点の重みを左右へ半分ずつ配り、重複加算を避けます。

固定入力の界面比較。R,Tはパケットエネルギー比。Nx場の相対L²誤差r（実測）t（実測）R（積分）T（積分）|R+T−1|1600.075366-0.329790.665410.108750.890350.00090293200.0184-0.332490.666750.110530.889220.000251836400.0045536-0.333120.666710.110960.888976.5291e-05実測収束次数：場 2.0342, 2.0146、反射振幅誤差 2.0682, 2.0162、透過振幅誤差 3.9033, 0.91765、エネルギー収支 1.8421, 1.9475。透過振幅では先頭誤差の打消しがあるため、全ての指標が各格子対で同じ2次を示すとは主張しません。

左右x方向PML：垂直・斜めパルス


$$
\begin{aligned}E_z&=E_x+E_y,\\\partial_t E_x+\gamma_E E_x&=\epsilon^{-1}\partial_xH_y,& \partial_t E_y&=-\epsilon^{-1}\partial_yH_x,\\\partial_t H_y+\gamma_H H_y&=\partial_xE_z,& \partial_t H_x&=-\partial_yE_z,\\\gamma_E&=\sigma_e/\epsilon,\quad\gamma_H=\sigma_m/\mu,\qquad\gamma_E(x)=\gamma_H(x),\quad\mu=1.\end{aligned}
$$

$$
\frac{u^{n+1}-u^n}{\Delta t}+\gamma\frac{u^{n+1}+u^n}{2}=D_hv,\qquad u^{n+1}=\frac{1-\gamma\Delta t/2}{1+\gamma\Delta t/2}u^n+\frac{\Delta t}{1+\gamma\Delta t/2}D_hv.
$$
Eₓ,Eᵧは電場Ezの補助的な分割変数で、物理的なx,y成分ではありません。y周期のTMz帯領域の左右x方向だけに、電場Eₓと磁場Hyの減衰率を整合させたBérenger型の分割場PMLを置きます。外端はPECです。電磁場を一律に減衰させる等方的なスポンジとは異なります。

PMLの物理厚さ2、3次の減衰プロファイル、最大減衰率10は固定し、格子384×16、768×32、1536×64で比較します。領域は12×π/4。kx>0の511個の連続FourierモードをGaussian重みで足し、kxの中心12、ky=0/8とします。中心波数の角度は0°/約33.690°ですが、有限帯域のパルスには角度分布があります。各モードは連続Maxwell方程式の厳密解であり、同じ有限和を解析参照として使います。

早い時刻の場を連続モード和と比較し、伝播誤差の格子収束を調べます。境界の反射は、同じ格子幅・時間刻み・Yee法で5倍の長さのPMLなし領域を計算し、x=6のモニター差から測ります。この広領域参照は境界の影響を分離するもので、別ライブラリの独立ソルバー比較ではありません。


$$
\rho_h=\frac{\max_{t\in\mathcal W}\|E_{\rm PML}(x_m,\cdot,t)-E_{\rm wide}(x_m,\cdot,t)\|_{\rm RMS,y}}{\max_t\|E_{\rm wide}(x_m,\cdot,t)\|_{\rm RMS,y}}.
$$
反射率ρはy方向RMSの戻り電場の最大値を、入射電場のRMS最大値で規格化した振幅指標です。測定窓は入力のt=8から18まで。ρ²は二乗振幅の診断値であり、広帯域パルスの積分反射エネルギーの上界とは呼びません。層の厚さ・入射スペクトル・窓を固定した収束です。

固定物理厚さのPML。早期誤差・戻り波・仕事は別の指標。格子中心角度（度）早期の場の相対誤差戻り振幅ρ解析戻り振幅解析戻り波との差修正エネルギー＋仕事の残差物理領域の流束収支残差384 × 1600.0540893.9856e-054.5515e-052.5487e-051.2897e-150.0053219768 × 3200.0136064.4119e-054.5368e-056.7622e-064.1583e-150.00133991536 × 6400.00338484.509e-054.5412e-051.7049e-062.5538e-150.00033546384 × 1633.690.053840.000195850.000202720.000138368.0989e-160.0076616768 × 3233.690.0135210.0002010.000202773.5686e-052.5619e-150.00192441536 × 6433.690.00336250.000202340.000202798.9538e-061.9159e-150.00048154ky=0の実測次数：早期の場 1.9911, 2.0071、解析戻り波との差 1.9142, 1.9878、物理領域の流束収支 1.9898, 1.9979。

ky=8の実測次数：早期の場 1.9935, 2.0076、解析戻り波との差 1.955, 1.9948、物理領域の流束収支 1.9933, 1.9987。

有限厚のPMLの理想的な戻り波も解析的に計算します。G=γmax d/(m+1)とすると、各波数の往復減衰はexp[−2(kx/ω)G]、PECでの電場反射は−1です。全モードの位相を含めて戻り波を足し、実測との差の最大RMSを入射振幅で規格化します。生の戻り波がゼロへ収束することは要求せず、この解析戻り波との差を細分化して評価します。単一反射の時間窓に限定し、初期層内エネルギーと外端の初期場もJSONへ保存します。


$$
\omega_k=\sqrt{k^2+k_y^2},\quad G=\int_{L-d}^{L}\gamma(x)\,dx=\frac{\gamma_{\max}d}{m+1},\quad E_{\rm ret}(x,y,t)=\operatorname{Re}\sum_{k>0}-A_k e^{i[k(2L-x-x_0)+k_y y-\omega_k t]}e^{-2(k/\omega_k)G}.
$$
エネルギー収支と第2版の再実行


$$
U_*^n=\tfrac12\lVert E_n\rVert_{\epsilon,h}^2+\tfrac12\langle H^{n-1/2},H^{n+1/2}\rangle_{\mu,h},\quad\mu=1.
$$

$$
\begin{aligned}\bar E_n&=(E_{n+1}+E_n)/2,\quad\bar E_{x,n}=(E_{x,n+1}+E_{x,n})/2,\\\bar H_{y,n}&=(H_y^{n-1/2}+H_y^{n+1/2})/2,\\W_n&=\Delta t\langle\bar E_n,\epsilon\gamma_E\bar E_{x,n}\rangle_h+\frac{\Delta t}{2}\langle H_y^{n+1/2},\gamma_H(\bar H_{y,n}+\bar H_{y,n+1})\rangle_h,\\U_*^{n+1}-U_*^n+W_n&=0.\end{aligned}
$$
上式のU*は誘電率の重みを含む修正離散エネルギーです。Hの半時刻を3つ使う磁場の仕事と、平均電場・分割電場の仕事を、場と係数から直接集計します。仕事を「エネルギー差の符号を変えた値」として定義しないため、別々に求めた量で収支を照合できます。分割電場の仕事は局所的には符号を持ち、正の物理的なOhm発熱を意味しません。強い減衰を持つ任意の補助場に、真空のCFLだけで正定値性を保証するとも主張しません。


$$
S_x=-E_zH_y,\qquad U_{\rm physical}(t)-U_{\rm physical}(0)+\int_0^t\!\int_0^{L_y}[S_x(x_R,y,\tau)-S_x(x_L,y,\tau)]\,dy\,d\tau=0.
$$
粗い格子では長い往復伝播の位相誤差が漸近的な収束域に入らなかったため、最終入力では384×16、768×32、1536×64を採用しました。古い試行を合格へ変更せず、同じ物理層・同じ許容値で細分化しています。

PMLのない物理領域については、補間した物理エネルギーとPoynting流束を別に測ります。閉じた全計算領域の厳密な離散仕事恒等式と、物理領域の流束・補間に伴う誤差を区別します。各固定入力に許容値、時間窓、格子、停止条件を保存し、JSONには個々の数値判定と参照条件を記録します。

第2版ZIPを独立展開して、旧2例を含む4入力と全テストを再実行し、数値指標とCSVの一致を確認しました。旧版の真空ソルバー・入力・テストは同一バイト列で保持します。共通実行台帳22例とは別の補助配布版であり、過去の検証結果へ加算しません。

[第2版：4例のコード・入力・図・結果ZIP](/code/fdtd/2026-11-22-r2/fdtd-2026-11-22-r2.zip)

[日英の取得・再実行手順](/code/fdtd/2026-11-22-r2/README.md)

[scattering.py](/code/fdtd/2026-11-22-r2/scattering.py)

[run_scattering.py](/code/fdtd/2026-11-22-r2/run_scattering.py)

[test_scattering.py](/code/fdtd/2026-11-22-r2/test_scattering.py)

[旧版との同一性・来歴](/code/fdtd/2026-11-22-r2/provenance.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r2/source-manifest.json)

[43テスト成功・独立展開記録](/code/fdtd/2026-11-22-r2/verification.json)



[](/numerical-methods-atlas/assets/fdtd-dielectric-interface.png)[dielectric-interface result.json](/code/fdtd/2026-11-22-r2/results/dielectric-interface/result.json) · [fixed input](/code/fdtd/2026-11-22-r2/inputs/dielectric-interface.json) · [energy.csv](/code/fdtd/2026-11-22-r2/results/dielectric-interface/energy.csv) · [convergence.csv](/code/fdtd/2026-11-22-r2/results/dielectric-interface/convergence.csv)[](/numerical-methods-atlas/assets/fdtd-pml-pulse.png)[pml-pulse result.json](/code/fdtd/2026-11-22-r2/results/pml-pulse/result.json) · [fixed input](/code/fdtd/2026-11-22-r2/inputs/pml-pulse.json) · [energy.csv](/code/fdtd/2026-11-22-r2/results/pml-pulse/energy.csv) · [convergence.csv](/code/fdtd/2026-11-22-r2/results/pml-pulse/convergence.csv)python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py
python run_scattering.py --input inputs/dielectric-interface.json --output output-interface
python run_scattering.py --input inputs/pml-pulse.json --output output-pmlこの版で検証したのは媒質界面への垂直入射と、真空帯領域の左右x方向PMLです。界面への斜め入射、四辺・角のPML、非常に浅い入射、分散・異方性物質、任意形状、3次元は今後の範囲です。

初版の真空2例：コード・再実行

新しい不変配布版を独立したフォルダへ展開し、ネットワークも元の作業コピーも使わず、テストと両入力を再実行しました。保存済みの数値指標・CSVとの一致を確認しています。既存の共通実行台帳22例とは別の補助配布版であり、過去の検証件数へ加算しません。

[コード・入力・結果ZIP](/code/fdtd/2026-11-22/fdtd-2026-11-22.zip)

[日英の取得・実行手順](/code/fdtd/2026-11-22/README.md)

[solver.py](/code/fdtd/2026-11-22/solver.py)

[run.py](/code/fdtd/2026-11-22/run.py)

[test_fdtd.py](/code/fdtd/2026-11-22/test_fdtd.py)

[ファイル目録・SHA-256](/code/fdtd/2026-11-22/source-manifest.json)

[24検査成功・独立展開記録](/code/fdtd/2026-11-22/verification.json)



固定入力：periodic-wave

[inputs/periodic-wave.json](/code/fdtd/2026-11-22/inputs/periodic-wave.json) · [数値判定・結果JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [場の分布CSV](/code/fdtd/2026-11-22/results/periodic-wave/solution.csv)

固定入力：pec-cavity

[inputs/pec-cavity.json](/code/fdtd/2026-11-22/inputs/pec-cavity.json) · [数値判定・結果JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [場の分布CSV](/code/fdtd/2026-11-22/results/pec-cavity/solution.csv)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py
python run.py --input inputs/periodic-wave.json --output output-periodic
python run.py --input inputs/pec-cavity.json --output output-cavity空でない出力先は拒否します。終了コードは0=数値条件合格、1=数値条件不合格、2=入力・実行エラー。JSONには入力SHA-256、環境、誤差・収束・保存量の指標、各判定、終了理由が入ります。自作コードは同梱MIT License、本文・図・データはサイトの項目別利用条件を参照してください。

## 公開範囲

2次元TMzの教育用実装。初版の一様真空の周期波・PEC空洞に加え、ε₁=1、ε₂=4の界面への垂直入射と、y周期・左右x方向PMLでの垂直/斜めパルスを固定入力で検証。Fresnel解・連続Fourierモード和・広領域の同じYee法を区別して参照。四辺/角PML、媒質界面への斜め入射、分散物質、3次元は未検証。

## 文献

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
- Jean-Pierre Bérenger (1994). A Perfectly Matched Layer for the Absorption of Electromagnetic Waves. https://doi.org/10.1006/jcph.1994.1159
- Steven G. Johnson (2021). Notes on Perfectly Matched Layers (PMLs). https://arxiv.org/abs/2108.05348v1
- Markus Zahn (2003). Electromagnetic Field Theory: A Problem Solving Approach. https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/
