# Yee FDTD

Yee FDTD：基礎と検証例

Maxwell方程式を電場・磁場の位置と時刻をずらして解くYee法です。基本式を先に読み、必要な検証例を選べます。最新の第6版は一次元の損失・Lorentz分散媒質を扱います。

[基本モデル](#model) · [損失・分散媒質](#interface-loss-dispersion) · [Fresnel界面](#interface) · [四辺・角PML](#pml-corners) · [斜め入射](#interface-oblique) · [p偏光・Brewster・全反射](#interface-p-polarization)

2次元TMz（Ez、Hx、Hy）の自作教育用コードです。初版の検証では無次元の一様真空・電流/電荷源なしに限定し、周期平面波と完全導体（PEC）長方形空洞を連続解析解と比較しました。格子収束、数値分散、離散保存量、物理エネルギーの近似を別々に確認します。

モデル・単位・適用範囲


$$
\partial_t E_z=\partial_xH_y-\partial_yH_x,\qquad \partial_tH_x=-\partial_yE_z,\qquad \partial_tH_y=\partial_xE_z,\quad \epsilon=\mu=c=1.
$$
長さ・時間・場を規格化し、ε=μ=c=1とします。計算領域はLx=1、Ly=1.5、モード番号(m,l)=(1,1)。矩形・斜めの周期モードを使い、軸の入れ替えや磁場の符号を見逃さない構成です。この初版の真空例には分散・損失・界面・外部励起を含みません。界面と損失・分散は各追加例で別に扱います。

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

第6版：損失・分散媒質

真空に挟まれた有限厚の板へ垂直に入射する一次元波束を計算します。導電損失の板と、減衰を持つ単一共鳴Lorentz板の2例です。Ez・分極P・分極電流Jを整数時刻、Hyを半時刻に置き、磁場のYee更新後にE/P/Jを局所陰的中点法で進めます。


$$
\begin{gathered}\epsilon_\infty\partial_t E=\partial_xH-\sigma E-J,\quad\partial_tH=\partial_xE,\\\partial_tP=J,\quad\partial_tJ=fE-\omega_0^2P-\gamma J,\quad f=\Delta\epsilon\,\omega_0^2,\\\epsilon(\omega)=\epsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega},\quad e^{-i\omega t}.\end{gathered}
$$
σは通常の電流σEの係数です。f=0ではP=J=0として振動子項を除きます。外端は遠方のPECで、ここではPMLを使いません。界面の電場制御体積ではε∞・σ・fを半体積で平均します。

板内の多重反射と複素波数を含む解析解を、実際の入射スペクトルで重み付けします。数値のR/Tは外側のPoynting流束、Aは導電・分極電流の散逸を直接積算して求めます。吸収と媒質内の一時的な蓄積を分け、エネルギー収支と格子・時間の収束を照合します。

最細格子の有限窓測定と帯域重み付き解析値。板数値R数値T直接A解析R / T / Aohmic0.04217920.1631050.7947160.0422517 / 0.163222 / 0.794527lorentz0.1210680.05543760.8234950.121356 / 0.0555188 / 0.823125[](/numerical-methods-atlas/assets/fdtd-loss-dispersion.png)[結果・全判定JSON](/code/fdtd/2026-11-22-r6/results/loss-dispersion/result.json) · [convergence.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/convergence.csv) · [図を開いて拡大](/numerical-methods-atlas/assets/fdtd-loss-dispersion.png)[第6版コードZIP：損失・分散＋既存7入力](/code/fdtd/2026-11-22-r6/fdtd-2026-11-22-r6.zip) · [日英の実行手順](/code/fdtd/2026-11-22-r6/README.md)

範囲は線形・等方・非磁性の一次元垂直入射、指定した帯域と有限時間です。Drude、多共鳴、分散媒質への斜め入射、分散媒質とPMLの併用、一般2/3次元は未検証です。

式の導出・全格子の結果・再現資料を開く
$$
\begin{gathered}n=\sqrt{\epsilon},\quad\Re n\ge0,\quad\Im n\ge0,\quad\rho=\frac{1-n}{1+n},\quad z=e^{2in\omega d},\\r=\frac{\rho(1-z)}{1-\rho^2z},\quad t=\frac{(1-\rho^2)e^{in\omega d}}{1-\rho^2z},\\R=|r|^2,\quad T=|t|^2,\quad A=1-R-T,\\A_{\rm volume}=\int_0^d\!\left(\sigma+\frac{\gamma\omega^2f}{|\omega_0^2-\omega^2-i\gamma\omega|^2}\right)|E(x)|^2\,dx.\end{gathered}
$$
tは板の出口面での電場振幅です。両外側が真空なのでT=|t|²です。体積積分のE(x)は入射振幅1の内部場です。解析A=1−R−Tはこの独立した散逸積分とも照合します。搬送波の係数、帯域平均、有限窓DFTの差を別に保存します。


$$
\begin{gathered}U_*^n=\tfrac12\|E^n\|_{\epsilon_\infty,h}^2+\tfrac12\Re\langle H^{n-1/2},H^{n+1/2}\rangle_h+U_{\rm mat}^n,\\U_{\rm mat}=\sum_{f_j>0}\frac{|J_j|^2+\omega_0^2|P_j|^2}{2f_j}\Delta x,\\\Delta W_\sigma=\Delta t\sum_j\sigma_j|\bar E_j|^2\Delta x,\quad\Delta W_\gamma=\Delta t\sum_{f_j>0}\frac{\gamma|\bar J_j|^2}{f_j}\Delta x,\\U_*^n+W_\sigma^n+W_\gamma^n=U_*^0.\end{gathered}
$$
複素場は二つの実直交成分を表し、全エネルギー・流束は同じ規約です。WσとWγは中点場から直接計算し、Uの減少や1−R−Tから逆算しません。修正離散エネルギー恒等式と、中心化磁場を使う物理的な局所Poynting収支は別々に判定します。中点の内積でE–Jの交換項が相殺し、PEC外端では離散curlの組が相殺するため、この恒等式を得ます。厳密CFL条件は静的誘電率ではなくε∞を使うΔt/Δx<min(1,√ε∞)です。振動子の蓄積は吸収率へ足しません。

同じ物理時刻での3格子。板Nx場の相対L2R誤差T誤差A誤差物理流束残差ohmic30720.120280.001165190.001887640.003052830.00215611ohmic61440.03010150.0002903310.0004686340.0007589650.00053856ohmic122880.0075267.2522e-050.0001169550.0001894770.000134611lorentz30720.104430.004686770.001302980.005989750.00215381lorentz61440.02633820.001157060.0003250520.001482110.000537989lorentz122880.006597650.0002883548.12193e-050.0003695730.000134468Lorentz板の最細格子で分極Pと電流Jの相対L2誤差は 0.011884 と 0.0124923 です。

ohmicの観測次数：場 1.99849, 1.99988; R 2.0048, 2.00121; T 2.01005, 2.0025; A 2.00804, 2.00201; 複素r 2.00255, 2.00077; 複素t 2.00708, 2.0018; 物理流束収支 2.00126, 2.00032; 物理エネルギー 2.00565, 2.00141。固定空間での時間刻み半減の自己収束次数：2.00388

lorentzの観測次数：場 1.9873, 1.99713; R 2.01813, 2.00455; T 2.00307, 2.00078; A 2.01484, 2.00372; 複素r 1.99893, 2.00058; 複素t 2.00077, 2.00052; 物理流束収支 2.00124, 2.00031; 物理エネルギー 2.00952, 2.00236; P 2.02312, 2.00687; J 2.02239, 2.00672。固定空間での時間刻み半減の自己収束次数：2.00371

保存・散逸・残留蓄積・参照制御を分離。板修正収支の最大相対残差|R+T+A−1|終時刻の物質蓄積 / 入射窓内参照fluence差参照周期倍増の場の差ohmic1.64405e-133.04201e-1403.33067e-161.28307e-09lorentz1.76686e-131.09499e-103.10325e-126.24744e-111.92765e-09場の精度は波束と板が相互作用する保存時刻で判定し、流束・吸収の積分は後の終時刻まで続けます。初期Eは入射波束、Hは同じYee分散で半時刻へ合わせ、P=J=0とします。同じYee法の真空対照で反射を分離します。省略した連続散乱場・分極の初期裾、外端、正周波数帯域の切り落とし、参照周期と空間求積の倍増、有限窓DFTの差はJSONへ記録します。時間の自己収束は固定空間離散内の検査であり、独立PDEソルバーとの比較ではありません。

[dispersive.py](/code/fdtd/2026-11-22-r6/dispersive.py) · [run_dispersive.py](/code/fdtd/2026-11-22-r6/run_dispersive.py) · [test_dispersive.py](/code/fdtd/2026-11-22-r6/test_dispersive.py) · [固定入力・許容値](/code/fdtd/2026-11-22-r6/inputs/loss-dispersion.json) · [energy.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/energy.csv) · [solution.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/solution.csv) · [spectrum.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/spectrum.csv) · [waveforms-ohmic.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/waveforms-ohmic.csv) · [waveforms-lorentz.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/waveforms-lorentz.csv) · [SHA-256 manifest](/code/fdtd/2026-11-22-r6/source-manifest.json) · [旧版の同一性](/code/fdtd/2026-11-22-r6/provenance.json) · [108テスト成功・独立追試](/code/fdtd/2026-11-22-r6/verification.json)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py test_dispersive.py
python run_dispersive.py --input inputs/loss-dispersion.json --output output-lossZIPを独立展開し、全テストと全8入力を再実行して指標・全CSVの一致を確認しました。旧7入力の数値ソース・テストと過去5配布版は不変です。共通実行台帳や他分野の件数へ加算しません。Lorentzモデルの参照はMeep公式資料の該当節であり、Meepの導電率規約・陽的ADEと本実装を区別します。

初版の詳しい検証：周期波・導体空洞固定入力と実測結果


$$
e_h=\left(\frac{\lVert E_h-E\rVert_h^2+\lVert H_h-H\rVert_h^2}{\mathcal N^2}\right)^{1/2},\qquad p=\frac{\log(e_h/e_{h/2})}{\log 2}.
$$
格子16×24、32×48、64×96を使用。連続解析解との場の誤差は、時間刻みを調整して厳密に到達する1.1周期の時刻で照合します。Hの誤差はEより半刻み前の実時刻で比較します。全場誤差の分母𝒩²は連続場の一定ノルム（周期波LxLy、空洞LxLy/4）です。電場・磁場の個別誤差もJSONに保存します。

固定入力の実測値。誤差と周波数は連続解析解に対して評価。問題格子 Nx × Ny全場の相対L²誤差観測次数相対周波数誤差離散エネルギー最大相対変動周期波16 × 240.021645—0.00312712.22e-16周期波32 × 480.00539262.00490.000779622.22e-16周期波64 × 960.00133092.01860.000192442.22e-16導体空洞16 × 240.0055511—0.000779624.441e-16導体空洞32 × 480.00135142.03830.000192444.441e-16導体空洞64 × 960.000333262.01974.7804e-052.22e-16周期平面波 · [JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/periodic-wave/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/periodic-wave/energy.csv)完全導体空洞 · [JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/pec-cavity/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/pec-cavity/energy.csv)許容値は固定入力のacceptanceに保存しています。全場誤差0.01以下、観測次数1.8以上、相対周波数誤差0.002以下、離散分散一致誤差10⁻⁹以下、U*相対変動2×10⁻¹¹以下を別々に判定します。壁上の電場0、磁場の初期発散の保存、Usyncの解析的全エネルギーに対する最大相対誤差0.003以下、およびその約2次の細分化も別々に判定します。Usyncの変動幅は診断値として保存します。

第2版の詳しい検証：界面・左右PML誘電体界面：Fresnelの振幅とエネルギー


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
python run_scattering.py --input inputs/pml-pulse.json --output output-pml第2版の範囲は界面への垂直入射と、真空帯領域の左右x方向PMLです。四辺・角のPMLは以下の第3版で追加しました。界面への斜め入射、非常に浅い入射、分散物質、一般形状、3次元は別の課題です。

第3版の詳しい検証：四辺・角PML第3版：四辺と角のPML

方向別の減衰と角の重なり


$$
\begin{aligned}E_z&=E_x+E_y,\\\partial_t E_x+\gamma_{x,E}E_x&=\partial_xH_y,&\partial_t E_y+\gamma_{y,E}E_y&=-\partial_yH_x,\\\partial_t H_x+\gamma_{y,H}H_x&=-\partial_yE_z,&\partial_t H_y+\gamma_{x,H}H_y&=\partial_xE_z,\quad\epsilon=\mu=1.\end{aligned}
$$
真空の2次元TMz正方形で、左右にγx、上下にγyのPMLを置き、四つの外端は完全導体（PEC）とします。角の領域ではγxとγyが同時に非ゼロになります。Eₓ,EᵧはEzの補助分割で、電場の物理的なx,y成分ではありません。各減衰率は電場節点・磁場の半格子位置でそれぞれ評価し、時間方向の減衰は台形則で更新します。

辺へ向かう波の組と、斜めに角へ向かう波の組を分けます。単に全体のエネルギーが減るだけでなく、四辺それぞれの流出と、四つの角で減衰が実際に働いた根拠を調べます。層の物理厚さ・強度・形状は格子を細かくしても保持し、解く物理条件を変えません。

参照波形と反射の意味

境界のない同じ離散Maxwell方程式をFourierモードで進めた参照波形と比較し、通常の格子上の伝播誤差を境界の効果から切り分けます。この参照の更新・時刻配置を、別の小規模な周期格子のYee更新と照合します。参照の周期長と、初期層内の物理場・補助分割場の微小な裾を別に確認し、有限周期の像を反射と取り違えないようにします。外部ライブラリによる独立ソルバーとの比較ではありません。

ここでの反射指標は、物理領域のPML場と境界なし参照の差を入射場で規格化した「境界による場差」です。有限層と初期のPML/補助分割場の裾の影響を含み、純粋な理想PMLの反射係数とは呼びません。有限厚・外端PECの系では、十分細かい格子でも有限の戻り波が残り得ます。戻り波の絶対値と、格子を細分化したときの波形の変化を区別し、観測窓の外や任意の角度に反射ゼロを保証しません。

初期場は有限Fourierモード和の定在波束です。軸向きの搬送波は(±6, 0), (0, ±6)、斜め向きは(±4, ±4)を中心に持ち、時間発展で四方向へ分かれます。斜め波の中心方向は45度ですが、有限帯域を持つので単一角度の単色平面波ではありません。

4観測点は、辺向きで(c±a,c),(c,c±a)、斜め向きで(c±a,c±a)です。c=8、a=2。各格子の保存時刻集合Tₕ上で下式を評価し、自己収束のノルムも観測窓内の時間最大・4点RMSとします。


$$
\begin{gathered}A_{\mathrm{inc},h}=\max_{t\in\mathcal T_h,\,0\le t独立に求める仕事と四辺の流束


$$
\begin{aligned}W_n={}&\Delta t\langle\bar E_n,\gamma_{x,E}\bar E_{x,n}+\gamma_{y,E}\bar E_{y,n}\rangle_h\\&+\frac{\Delta t}{2}\langle H_x^{n+1/2},\gamma_{y,H}(\bar H_{x,n}+\bar H_{x,n+1})\rangle_h\\&+\frac{\Delta t}{2}\langle H_y^{n+1/2},\gamma_{x,H}(\bar H_{y,n}+\bar H_{y,n+1})\rangle_h,\\U_*^{n+1}-U_*^n+W_n={}&0.\end{aligned}
$$
平均場の定義と修正離散エネルギーU*は前節と同じですが、仕事には電場x/yと磁場x/yの全4項を含めます。磁場は3つの連続した半時刻を用います。各項は場と減衰率から直接集計し、エネルギー差から逆算しません。局所的には符号付きの補助場の仕事であり、正の物理発熱とは区別します。任意の分割場に対する一般的な安定性定理を新しく証明したという主張でもありません。


$$
\begin{gathered}S_x=-E_zH_y,\quad S_y=E_zH_x,\\\Phi(t)=\int_{y_B}^{y_T}(S_x(x_R,y,t)-S_x(x_L,y,t))\,dy+\int_{x_L}^{x_R}(S_y(x,y_T,t)-S_y(x,y_B,t))\,dx,\\U_{\rm physical}(t)-U_{\rm physical}(0)+\int_0^t\Phi(\tau)\,d\tau=0.\end{gathered}
$$
PMLの内側の物理矩形では、右−左と上−下のPoynting流束を加え、内部エネルギーとの収支を測ります。角の電場節点には1/4、辺には1/2の積分重みを使い、共有点を重複加算しません。全領域の厳密な離散仕事恒等式と、補間・時間積分を含む物理領域の近似収支は別の判定です。

固定入力と実測結果

計算領域は一辺 16 の正方形、物理PML厚さ 2、最大減衰率 8、プロファイル次数 3 です。初期波束の中心は(8, 8)、幅は 1。格子は 128×128, 256×256, 512×512、観測はt=24まで、戻り波の窓はt=8以降です。

参照Fourier周期は 64、波数間隔Δk=0.098175。要求した打切り波数 14 を最寄りのモード番号へ丸めるため、実際の各軸最大波数は 14.039 です。係数スロット数 20736（DC成分はゼロ）を使う有限和であり、無限帯域の厳密なGaussianとは区別します。

第3版の固定入力。各条件の数値判定と参照情報は結果JSONに保存。波の組格子早期の場の相対誤差境界による場差（初期化含む）エネルギー＋仕事の残差四辺の流束収支残差辺へ向かう波128 × 1280.113280.000272455.8233e-160.029017辺へ向かう波256 × 2560.0302560.000338388.5458e-160.0075302辺へ向かう波512 × 5120.00758380.000362772.5493e-150.0019002斜めに角へ向かう波128 × 1280.0392119.7478e-065.8085e-160.02655斜めに角へ向かう波256 × 2560.0105171.0326e-058.5392e-160.0067585斜めに角へ向かう波512 × 5120.00265931.0584e-058.4959e-160.0016973辺への波の観測次数：早期の場 1.9046, 1.9962、四辺の流束収支 1.9461, 1.9865、戻り波の自己収束 1.66。参照周期を2倍にした差／入射振幅は 8.6937e-11。

斜めの角への波の観測次数：早期の場 1.8986, 1.9836、四辺の流束収支 1.9739, 1.9935、戻り波の自己収束 1.8964。参照周期を2倍にした差／入射振幅は 6.6332e-10。

最細格子の四辺からの累積流出／初期物理領域エネルギー。波の組左辺右辺下辺上辺辺への波0.249530.249530.249530.24953斜め角への波0.249580.249580.249580.24958斜めの波の組での角の累積絶対仕事増分／初期全エネルギー：SW=0.11008, SE=0.11008, NW=0.11008, NE=0.11008。各時刻で角領域の仕事を合計してから絶対値を取り、その値を時間方向に足した量です。局所仕事密度の絶対値の積分とは異なります。

axis：最細格子で初期層内の場をゼロにした制御計算とのモニター差／入射振幅 3.4327e-09、標準入力の戻り信号に対する比は 9.4624e-06（判定値 0.01 以下）。物理領域の初期波束は保持し、層内の微小な物理場・補助場だけを変えた感度確認です。別の初期条件であり、これを標準入力の誤差上界とは呼びません。

diagonal：最細格子で初期層内の場をゼロにした制御計算とのモニター差／入射振幅 7.8814e-09、標準入力の戻り信号に対する比は 0.00074467（判定値 0.01 以下）。物理領域の初期波束は保持し、層内の微小な物理場・補助場だけを変えた感度確認です。別の初期条件であり、これを標準入力の誤差上界とは呼びません。

戻り場の自己収束次数はこの波束・層プロファイル・3格子で観測した値です。全ての入射・格子範囲で同じ次数になるという意味ではありません。

格子間の波形差は同じ物理時刻へ揃えて比較します。自己収束から得た次数やRichardson型の見積もりは経験的な指標であり、厳密な誤差上界ではありません。全ての生の戻り波がゼロへ向かうこととは区別します。


$$
\delta_h=\|r_h-\mathcal I r_{h/2}\|_{\mathcal W},\qquad p_h=\frac{\log(\delta_h/\delta_{h/2})}{\log2}.
$$
第3版の取得と再実行

[](/numerical-methods-atlas/assets/fdtd-pml-corners.png)[四辺・角PMLの結果JSON](/code/fdtd/2026-11-22-r3/results/pml-corners/result.json) · [convergence.csv](/code/fdtd/2026-11-22-r3/results/pml-corners/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r3/results/pml-corners/energy.csv)[第3版：旧4例＋四辺・角PMLのコードZIP](/code/fdtd/2026-11-22-r3/fdtd-2026-11-22-r3.zip)

[日英の取得・実行手順](/code/fdtd/2026-11-22-r3/README.md)

[corner.py](/code/fdtd/2026-11-22-r3/corner.py)

[run_corner.py](/code/fdtd/2026-11-22-r3/run_corner.py)

[test_corner.py](/code/fdtd/2026-11-22-r3/test_corner.py)

[固定入力・許容値](/code/fdtd/2026-11-22-r3/inputs/pml-corners.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r3/source-manifest.json)

[旧版との同一性・来歴](/code/fdtd/2026-11-22-r3/provenance.json)

[57テスト成功・独立展開記録](/code/fdtd/2026-11-22-r3/verification.json)



python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py
python run_corner.py --input inputs/pml-corners.json --output output-cornersZIPを別フォルダへ独立展開し、全テストと旧4入力・新入力の全5例を再実行して、数値指標とCSVの一致を確認しました。旧版の数値ソース・入力・テストは同一バイト列で保持しています。共通22実行例・固有67問題とは別の補助配布版です。

第3版の対象は指定した真空2次元TMz波束・正方形・有限時間です。媒質界面への斜め入射は以下の第4版で別に検証します。掠れ入射全般、分散・異方性物質、3次元や一般曲面のPMLには、この結果をそのまま適用しません。

第4版の詳しい検証：斜め界面入射第4版：媒質界面への斜め入射

TMzとs偏光・Fresnel係数

x=aを境界とする非磁性・無損失・非分散の誘電体を扱います。入射面はxy、電場Ezはその面に垂直なので、ここでのTMzは光学のs/TE偏光です。y方向は周期境界です。PMLによる損失と混同しないよう、この例はPMLを使わず、x外端のPECから主要な戻り波が来る前の時間窓で検証します。


$$
\omega^2=(k^2+k_y^2)/\epsilon_1,\quad q=\sqrt{\epsilon_2\omega^2-k_y^2},\quad n_1\sin\theta_i=n_2\sin\theta_t,\quad\mu_1=\mu_2=1.
$$

$$
r_s(k)=\frac{k-q}{k+q},\quad t_s(k)=\frac{2k}{k+q},\quad R_s=|r_s|^2,\quad T_s=\frac{q}{k}|t_s|^2,\quad R_s+T_s=1.
$$
正の法線波数kについて、周波数ωと接線波数kyを界面の左右で等しくします。式は透過波が伝播する低屈折率側から高屈折率側への入射に限定します。小文字r,tは符号付き電場振幅、大文字R,Tは法線方向のエネルギー流の比です。透過率はt²だけではなくq/kを含みます。

有限帯域波束の解析参照


$$
\begin{aligned}E_i&=\Re\int_0^\infty A(k)e^{i[k(x-c)+k_y y-\omega t]}\,dk,\\E_r&=\Re\int_0^\infty A(k)r_s(k)e^{i[k(2a-x-c)+k_y y-\omega t]}\,dk,\\E_t&=\Re\int_0^\infty A(k)t_s(k)e^{i[k(a-c)+q(x-a)+k_y y-\omega t]}\,dk.\end{aligned}
$$

$$
\begin{aligned}R_{\rm packet}&=\frac{\int_0^\infty |A(k)|^2R_s(k)\,dk}{\int_0^\infty |A(k)|^2\,dk},\\T_{\rm packet}&=\frac{\int_0^\infty |A(k)|^2T_s(k)\,dk}{\int_0^\infty |A(k)|^2\,dk},\qquad\frac{dq}{dk}=\frac{\epsilon_2 k}{\epsilon_1 q}.\end{aligned}
$$

$$
A(k)=\frac{w}{\sqrt{2\pi}}e^{-w^2(k-k_0)^2/2},\quad a_m=A(k_m)\Delta k,\quad\Delta k=2\pi/P,\quad n_j=\sqrt{\epsilon_j},\qquad U_{\rm inc}=\pi\epsilon_1 L_y\int_0^\infty |A(k)|^2\,dk\approx\frac{\epsilon_1 L_yP}{2}\sum_m a_m^2.
$$
初期中心cの正k波束を各モードのFresnel解で重ね合わせます。磁場は各成分の符号付き波数kxを使ってHx=(ky/ω)E、Hy=−(kx/ω)Eから求め、EとHをそれぞれのYee位置・時刻で評価します。Gaussian型のスペクトル積分を有限波数の求積で計算し、求積間隔を半分にした比較と有限領域で積分した参照エネルギーで確認します。透過波のqは非等間隔なので、参照周期Pは透過波がx周期であるという主張ではありません。

中心角の単色係数と、波束全体のR,Tを区別します。後者は|A(k)|²で重み付けしたFresnel係数の積分です。透過波数への変換のJacobianを含めると、波束エネルギーにもq/kの係数が現れます。数値R,Tは左右の物理エネルギーを入射波束のParseval求積で割った値であり、初期数値エネルギー比は別に保存します。


$$
g_r=\frac{\sum_{xa,y}E_{\rm num}E_{t,\rm ref}}{\sum_{x>a,y}E_{t,\rm ref}^2},\qquad g_r,g_t\to1.
$$
反射・透過の振幅確認には、終時刻の左右それぞれで数値Ezを符号込みの解析波束へ射影した倍率gを使います。目標は1であり、これを搬送波のr,tの実測値とは呼びません。波形のL2誤差も別に保存するため、倍率だけで位相・形の誤差を隠しません。

独立したエネルギーと流束の確認


$$
\begin{gathered}U_*^n=\tfrac12\bigl(\langle E^n,\epsilon E^n\rangle_h+\langle H^{n-1/2},H^{n+1/2}\rangle_h\bigr),\quad U_*^n=U_*^0,\\S_x=-E_zH_y,\quad U_{[x_L,x_R]}(t)-U_{[x_L,x_R]}(0)+\int_0^t\!\int_0^{L_y}[S_x(x_R,y,\tau)-S_x(x_L,y,\tau)]\,dy\,d\tau=0.\end{gathered}
$$
全領域では誘電率を含む修正離散エネルギーの保存を測ります。物理エネルギーは磁場を整数時刻へ平均し、界面をまたぐ内部区間で左右のPoynting流束を場から直接計算して台形積分します。流束をエネルギー差で定義しません。物理エネルギー・流束の近似収支と、厳密な離散保存量は別の判定です。界面の電場節点には従来どおり誘電率の算術平均を置きます。

固定入力と格子収束の実測

ε₁=1、ε₂=4、領域 32×1.5708、初期中心c=8、界面a=16、幅 1.2、搬送波kx=6。ky=0, 4、格子 1024×16, 2048×32, 4096×64、終時刻 18 です。流束区間は [12.0, 20.0]。

参照求積はP=64、Δk=0.0981748、要求打切り波数 14 を最寄りのモード番号へ丸めた実際の最大波数 14.039 を使います。

全3格子。R/Tの差は同じ入力のスペクトルFresnel参照と比較する。ky格子場の相対L2誤差数値R数値T局所流束収支残差01024×160.3666450.1069330.8913670.0022301702048×320.09196090.1100750.88950.00056024104096×640.02297510.1108530.8890410.00014023341024×160.5483710.1503810.8471720.0024363942048×320.1385210.1558540.8435330.00061187744096×640.03462150.1572090.8426380.000153143中心角の値と有限帯域波束の値を区別する。中心入射角°中心透過角°中心r中心t中心R波束解析R波束解析T00-0.3333330.6666670.1111110.1111110.88888933.690116.1021-0.3956610.6043390.1565480.1576590.842341ky=0：場の観測次数 1.99529, 2.00095、反射エネルギー 2.01165, 2.0029、透過エネルギー 2.02059, 2.00515、流束収支 1.99303, 1.99822。最細格子の振幅倍率(gᵣ,gₜ)=(0.998868, 0.999845)。

ky=4：場の観測次数 1.98505, 2.00037、反射エネルギー 2.01151, 2.00285、透過エネルギー 2.01829, 2.00455、流束収支 1.99343, 1.99836。最細格子の振幅倍率(gᵣ,gₜ)=(0.998485, 0.999572)。

全格子の修正離散エネルギー最大相対変動 4.44089e-16。終時刻の比較で参照求積を倍密度化したときの、全格子における場の最大相対差 5.30355e-13、有限領域の参照R/Tとスペクトル積分との差 8.66989e-11。初期の二次場（反射・透過側の裾）の重み付き格子場ノルム二乗比は最大 2.30339e-21、解析場の外端Ezの最大値は 1.24222e-06 です。時刻のずれた場のノルムと、同時刻の物理エネルギーを区別します。

初期PEC条件への切り詰めの重み付き格子場ノルム二乗比は最大 2.29928e-22、同時刻の連続参照による初期エネルギー／入射求積の1からの差は最大 2.22045e-16。終時刻の界面上の参照Ez最大値 1.4462e-05 も保存し、左右のエネルギー分割時に界面上に残る場の大きさを示します。

ky=0：初期数値物理エネルギー／入射求積 0.999894、終時刻の|R+T−1| 0.000106367。

ky=4：初期数値物理エネルギー／入射求積 0.999847、終時刻の|R+T−1| 0.000153186。

R+Tの微小な1からの差は、初期数値物理エネルギーと解析入射求積の差も含みます。この例には吸収やPMLがなく、修正離散エネルギーは保存されます。物理エネルギーの補間・求積誤差が格子とともに減少することと、物理的な散逸を区別します。

第4版の取得と再実行

[](/numerical-methods-atlas/assets/fdtd-dielectric-oblique.png)[斜め界面入射の結果JSON](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/result.json) · [spectrum.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/spectrum.csv) · [convergence.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/energy.csv)[第4版：旧5例＋斜め界面入射のコードZIP](/code/fdtd/2026-11-22-r4/fdtd-2026-11-22-r4.zip)

[日英の取得・実行手順](/code/fdtd/2026-11-22-r4/README.md)

[oblique.py](/code/fdtd/2026-11-22-r4/oblique.py)

[run_oblique.py](/code/fdtd/2026-11-22-r4/run_oblique.py)

[test_oblique.py](/code/fdtd/2026-11-22-r4/test_oblique.py)

[固定入力・許容値](/code/fdtd/2026-11-22-r4/inputs/dielectric-oblique.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r4/source-manifest.json)

[旧版との同一性・来歴](/code/fdtd/2026-11-22-r4/provenance.json)

[71テスト成功・独立展開記録](/code/fdtd/2026-11-22-r4/verification.json)



python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py
python run_oblique.py --input inputs/dielectric-oblique.json --output output-obliqueZIPを別フォルダへ独立展開し、全テストと全6入力を再実行して数値指標・CSVの一致を確認しました。旧5入力・数値ソース・テストと、過去3配布版は保持しています。これはFDTD専用の補助配布版で、共通実行台帳や他分野の検証件数には加算しません。

第4版の対象は指定した無損失・非磁性のs偏光波束、伝播する透過波、3格子と有限時間です。p偏光・Brewster条件・全反射は以下の第5版で別に検証します。損失や分散・3次元は引き続き別の範囲です。参照は解析式と数値積分で、外部FDTDソルバーとの比較ではありません。

第5版の詳しい検証：p偏光・Brewster・全反射第5版：p偏光・Brewster条件・全反射

TEzの格子配置とp偏光


$$
\partial_t H_z=\partial_yE_x-\partial_xE_y,\qquad\epsilon\partial_tE_x=\partial_yH_z,\qquad\epsilon\partial_tE_y=-\partial_xH_z,\quad\mu=1.
$$
Hzをセル中心・整数時刻、Ex/Eyを各辺・半時刻に置く新しいTEz更新です。入射面xyに磁場が垂直なので、光学のp偏光に対応します。ここでのEx/Eyは物理的な電場成分で、前節TMz-PMLのEzの補助分割とは異なります。界面に接するEyには誘電率の算術平均を置き、法線Exにはそのセルの媒質の値を使います。界面の逆誘電率2/(ε₁+ε₂)は、左右の逆誘電率の調和平均です。左右の外端はPEC、y方向は周期境界で、ここにはPMLを入れません。


$$
\begin{gathered}\partial_y\longmapsto iK_y,\qquad K_y=\frac{2}{\Delta y}\sin\frac{k_y\Delta y}{2},\\\int_0^{L_y}\Re(Ae^{ik_yy})\Re(Be^{ik_yy})\,dy=\frac{L_y}{2}\Re(AB^*),\\k_yL_y=2\pi m,\qquad 0固定例は正の単一kyモードへ厳密に縮約して実行します。連続微分ikyへ置き換えるのではなく、同じYee差分の記号iKyを使います。一般の2次元配列更新との同値性を別に検査し、固定実行ではdxとdyを同時に細分化します。各固定実行でNx×Nyの全配列を時間発展させたという意味ではありません。

磁場振幅のFresnel係数と二つの角度


$$
\begin{gathered}\omega^2=(k^2+k_y^2)/\epsilon_1,\quad q=\sqrt{\epsilon_2\omega^2-k_y^2},\quad\Re q\ge0,\ \Im q\ge0,\\Y_1=k/\epsilon_1,\quad Y_2=q/\epsilon_2,\quad r_H=\frac{Y_1-Y_2}{Y_1+Y_2},\quad t_H=1+r_H,\\R=|r_H|^2,\qquad T=\frac{\Re Y_2}{Y_1}|t_H|^2,\quad E_x=-\frac{k_y}{\epsilon\omega}H_z,\quad E_y=\frac{k_x}{\epsilon\omega}H_z.\end{gathered}
$$

$$
\tan\theta_B=\sqrt{\epsilon_2/\epsilon_1},\quad r_H(\theta_B)=0;\qquad\theta_c=\sin^{-1}\sqrt{\epsilon_2/\epsilon_1}\quad(\epsilon_1>\epsilon_2).
$$
時間・空間の規約はexp[i(kx x+ky y−ωt)]です。rH,tHはHzの振幅係数で、反射波では符号付きkx=−k、透過波ではkx=qを電場の式へ使います。接線Eyの反射成分の符号を、偏光基底で定義した振幅係数と取り違えないようにします。全反射ではq=iκ（κ>0）を選んで右向きに減衰させます。


$$
\begin{gathered}u=(k-k_0)/b,\\A_H(k)=\begin{cases}C\exp\!\left[-\frac{w^2(k-k_0)^2}{2}-\frac{u^8}{1-u^2}\right],&|u|入力のコンパクトな正k帯域を上式の滑らかな形で重み付けし、各モードへFresnel解を適用します。固定入力ではC=1で、実際の求積係数はスペクトルCSVに保存します。Hzを規格化するこの入射エネルギーには、前節のEz波束のようなε₁の係数は付きません。搬送波を解析的Brewster角へ置いても、角度分布を持つ有限帯域波束のR∞は一般にゼロではありません。これは既知のBrewster条件での検証で、角度を走査して独立に零点を探索した計算ではありません。

弱い反射の取り出しと有限時間の測定


$$
\begin{gathered}\Phi_X(t)=\frac{L_y}{2}\Re\!\left[E_{y,X}^{\rm centred}(t)H_X(t)^*\right],\\R_{\cal W}=-\frac{\int_{\cal W}\Phi_{\rm ref}\,dt}{\int_{\cal W}\Phi_{\rm inc}\,dt},\qquad T_{\cal W}=\frac{\int_{\cal W}\Phi_{\rm tr}\,dt}{\int_{\cal W}\Phi_{\rm inc}\,dt}.\end{gathered}
$$
界面ありと一様媒質の同じYee更新を並行して進め、左モニターでH/Eの差を取って反射成分を取り出します。連続入射場を引くだけの場合に残る通常の格子分散が、弱いBrewster反射を覆わないためです。左の入射・反射成分と右の透過成分のPoynting流束を時間積分します。磁場は面へ空間平均し、電場は整数時刻へ平均します。有限窓Wの比と、無限時間のスペクトル参照R∞,T∞との差を別に保存します。


$$
\begin{gathered}\widehat H(\omega_0)=\int_{\cal W}H(t)e^{i\omega_0t}\,dt,\\r_{H,h}^{\rm DFT}=\frac{\widehat H_{\rm ref}}{\widehat H_{\rm inc}}e^{-2ik_hd},\\\kappa_h=-\frac{\log|\widehat H(x_2)/\widehat H(x_1)|}{x_2-x_1}.\end{gathered}
$$

$$
\begin{gathered}\Omega_0=\frac{2}{\Delta t}\sin(\omega_0\Delta t/2),\\k_h=\frac{2}{\Delta x}\sin^{-1}\!\left[\frac{\Delta x}{2}\sqrt{\epsilon_1\Omega_0^2-K_y^2}\right].\end{gathered}
$$
左モニターは界面から距離dにあり、複素反射係数は同じ離散分散関係のkhで界面へ位相を戻します。透過振幅には面上の磁場平均に対応する補正も含めます。全反射のκは右の2観測点の時間Fourier成分から測ります。格子収束の比較先は、同じ有限時間窓を通した連続Fresnel参照です。参照と理想単色係数・理想κの差も表示し、時間窓の誤差を格子誤差と混同しません。

全反射の場・蓄積・正味流束

全反射の入力は帯域全体が臨界角より上にあり、各モードのR=1、法線方向の時間平均T=0です。それでも透過側にはエバネッセント場と一時的なエネルギーが存在します。パルスが界面を通過する間に出入りする符号付き流束、透過側の最大蓄積、最終蓄積を別々に記録し、右側の蓄積エネルギーを透過率とは呼びません。


$$
\begin{gathered}U_*^n=\tfrac12\bigl(\|H^n\|_h^2+\langle E^{n-1/2},\epsilon E^{n+1/2}\rangle_h\bigr),\quad U_*^n=U_*^0,\\\bar E^n=(E^{n-1/2}+E^{n+1/2})/2,\quad U_{\rm phys}^n-U_*^n=\tfrac18\|E^{n+1/2}-E^{n-1/2}\|_{\epsilon,h}^2,\\\Delta U_{[x_L,x_R]}+\int(\Phi_{x_R}-\Phi_{x_L})\,dt=0.\end{gathered}
$$
全領域の修正離散エネルギーと、電場を中心時刻へ平均した物理エネルギーを区別します。界面をまたぐ区間の流束は場から直接計算し、エネルギー差から逆算しません。界面上のEyエネルギーを左右へ分けるときは、それぞれε₁/2、ε₂/2を使い、全体のε平均との整合を保ちます。場の精度は界面との相互作用中の固定時刻で判定し、エネルギーと流束はより遅い終時刻まで追います。終時刻の場の誤差も別に掲載します。

固定入力と保存した測定値

参照求積の周期パラメータP=256、Δk=0.0245437、Courant係数 0.65。各入力の場の判定時刻と、流束・エネルギーを追う終時刻を以下に分けます。結果JSONには実際の保存時刻も記録します。

propagating：ε₁=1→ε₂=4、領域 80×3.14159、初期中心 36、界面 48、(k₀,ky)=(3,2)、中心入射角 33.6901°、k帯域 [0.5, 5.5]、w=2、b=2.5。場の時刻 18、流束の終時刻 48、モニター距離d=3、収支区間 [42.0, 54.0]、格子 1280×64, 2560×128, 5120×256。

brewster：ε₁=1→ε₂=4、領域 112×3.14159、初期中心 40、界面 56、(k₀,ky)=(2,4)、中心入射角 63.4349°、k帯域 [0.3, 3.7]、w=4、b=1.7。場の時刻 44、流束の終時刻 96、モニター距離d=2、収支区間 [52.0, 60.0]、格子 1792×64, 3584×128, 7168×256。

tir：ε₁=4→ε₂=1、領域 80×3.14159、初期中心 28、界面 40、(k₀,ky)=(4,4)、中心入射角 45°、k帯域 [1.5, 6.5]、w=1.2、b=2.5。場の時刻 40、流束の終時刻 100、モニター距離d=0.75、収支区間 [37.0, 43.0]、格子 1280×64, 2560×128, 5120×256。

全3格子。場の誤差は相対L2、流束比は一様媒質の数値入射fluenceで規格化。例格子場の保存時刻相互作用中の場誤差終時刻の場誤差R_WT_W（符号付き）複素rH誤差／有限窓参照propagating1280×64180.1474550.8705790.06595690.9340430.00909874propagating2560×128180.03683170.2266380.06964630.9303540.00222338propagating5120×256180.009204090.05672690.07055870.9294410.000552736brewster1792×64440.4963441.832030.001378760.9986220.0131163brewster3584×128440.1253730.5825640.001156280.9988440.00318401brewster7168×256440.03132320.1474880.001139560.9988610.000790283tir1280×64400.2421050.5859371-1.22848e-090.0101086tir2560×128400.06073630.1494281-1.22624e-090.00250989tir5120×256400.0151880.03740621-1.22729e-090.00062594無限時間のスペクトル値、有限窓の連続参照、数値の比較先を明示。例解析R∞解析T∞解析有限窓R_W解析有限窓T_W参照DFT→理想rHの差数値DFT→理想rHの差propagating0.0708620.9291380.0708620.9291386.9802e-070.00055212brewster0.001137230.9988630.001137230.9988637.30357e-060.000786266tir101-1.23752e-090.000187080.00055515propagatingの観測次数：場: 2.00125, 2.0006; 反射流束: 2.01258, 2.00318; 透過流束: 2.01258, 2.00318; 複素rH／有限窓: 2.03291, 2.00809; 複素tH／有限窓: 2.03288, 2.00808; 局所流束収支: 1.99738, 1.99935; 過渡透過流束波形: 2.03289, 2.00826。

brewsterの観測次数：場: 1.98512, 2.00092; 反射流束: 3.66482, 3.03245; 透過流束: 3.66482, 3.03245; 複素rH／有限窓: 2.04244, 2.0104; 複素tH／有限窓: 2.03468, 2.00847; 局所流束収支: 2.00677, 2.00163; 過渡透過流束波形: 2.05672, 2.01386。

tirの観測次数：場: 1.995, 1.99963; 反射流束: 2.22383, 3.59628; 複素rH／有限窓: 2.00988, 2.00353; 複素tH／有限窓: 2.00848, 2.00541; 局所流束収支: 1.99629, 1.99909; κ／有限窓: 2.00522, 2.03305; 過渡透過流束波形: 2.00779, 2.00251。

これらは選んだ3格子・波束・時間窓での観測次数です。特定の小さな誤差や打消しから、更新式全体を高次法と呼び替えません。

Brewster条件と全反射の数値的な確認

Brewster例：中心角 63.4349°で、最細格子の|rH,DFT|=0.000786266、有限帯域の反射流束比 0.00113956、スペクトルFresnel参照 0.00113723。単色条件の零点と、波束の非ゼロの反射を別々に確認します。

全反射例：中心角 45°、臨界角 30°、入力帯域内の最小角は 31.6075°より大きい値です。数値rH=-0.777569-0.629054i。右の観測点はx=40.75 と 41.5。数値κ=2.82793、有限窓参照κ=2.82867、理想単色κ=2.82843 です。

全反射の正味Tの参照との差：9.05206e-12, 1.12867e-11, 1.02261e-11、その生の見かけの次数：-0.318305, 0.142363。この微小な差の床へ次数の合格条件を課さず、符号を保った過渡透過流束波形の相対L2誤差 0.160827, 0.0399902, 0.0099802 と、その格子収束を別に判定します。

最細格子の右側最大蓄積／解析入射エネルギー 0.0577621（t=33.6529）。同時刻の連続参照 0.0577265、相対差 0.000616712、終時刻の蓄積 6.10545e-09。右モニター流束／入射エネルギーは最小 -0.000223958、最大 0.000220947 で、出入りする符号を保っています。

最細格子の保存量・物理収支・規格化は別の確認。例修正離散エネルギー変動局所流束収支残差|R_W+T_W−1|数値入射fluence／解析エネルギーの誤差propagating5.55112e-166.40756e-058.52962e-120.000128161brewster6.66134e-167.98332e-053.80685e-070.000195978tir8.88178e-163.93668e-052.07714e-077.96698e-05参照の周期倍増による場の最大相対差（相互作用時刻と終時刻） 7.11693e-12、初期の二次場の重み付きノルム二乗比 7.50501e-08。外端Eyの参照監査は各実行につき最大2049点の時刻で行い、最大値は 0.000266315。これは指定した窓の制御で、任意の長時間や角度への反射ゼロの保証ではありません。

初期PEC条件への切り詰めによる重み付き格子場ノルム二乗比は最大 5.78842e-13。初期場、参照求積、時間窓の制御は、それぞれ結果JSONに残しています。

第5版の取得と再実行

[](/numerical-methods-atlas/assets/fdtd-p-polarization.png)[p偏光・全反射の結果JSON](/code/fdtd/2026-11-22-r5/results/p-polarization/result.json) · [spectrum.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/spectrum.csv) · [convergence.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/energy.csv)[第5版：旧6例＋p偏光・Brewster・全反射のコードZIP](/code/fdtd/2026-11-22-r5/fdtd-2026-11-22-r5.zip)

[日英の取得・実行手順](/code/fdtd/2026-11-22-r5/README.md)

[polarization.py](/code/fdtd/2026-11-22-r5/polarization.py)

[run_polarization.py](/code/fdtd/2026-11-22-r5/run_polarization.py)

[test_polarization.py](/code/fdtd/2026-11-22-r5/test_polarization.py)

[固定入力・許容値](/code/fdtd/2026-11-22-r5/inputs/p-polarization.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r5/source-manifest.json)

[旧版との同一性・来歴](/code/fdtd/2026-11-22-r5/provenance.json)

[85テスト成功・独立展開記録](/code/fdtd/2026-11-22-r5/verification.json)



全時刻の複素モニターCSV：[propagating](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-propagating.csv) · [brewster](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-brewster.csv) · [tir](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-tir.csv)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py
python run_polarization.py --input inputs/p-polarization.json --output output-pZIPを別フォルダへ独立展開し、全テストと全7入力を再実行して数値指標・全CSVの一致を確認しました。旧6入力の数値ソース・テストと過去4配布版は保持しています。FDTD専用の補助配布版であり、共通実行台帳や他分野の検証件数へ加算しません。

検証範囲は指定した無損失・非磁性の平面界面、周期yの単一モード、有限帯域と時間窓です。第5版は無損失です。損失・分散の垂直入射は第6版で別に検証します。異方性、任意の横方向スペクトル、3次元やエバネッセント場のPML吸収は対象外です。

初版の配布物と再現手順初版の真空2例：コード・再実行

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

教育用Yee FDTD。真空・Fresnel界面・s/p偏光・PMLの既存例を保持し、第6版で一次元垂直入射のOhmic・受動Lorentz板を追加。帯域解析解、反射・透過・直接散逸・物質蓄積、修正離散収支・物理流束と格子・時間収束を分けて検査。一般分散、多共鳴、斜め分散入射、分散PML、一般2/3次元の包括的検証ではない。

## 文献

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
- Jean-Pierre Bérenger (1994). A Perfectly Matched Layer for the Absorption of Electromagnetic Waves. https://doi.org/10.1006/jcph.1994.1159
- Steven G. Johnson (2021). Notes on Perfectly Matched Layers (PMLs). https://arxiv.org/abs/2108.05348v1
- Markus Zahn (2003). Electromagnetic Field Theory: A Problem Solving Approach. https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/
- Meep developers (2026). Materials — Meep Documentation. https://meep.readthedocs.io/en/latest/Materials/
