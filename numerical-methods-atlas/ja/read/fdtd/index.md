# Yee FDTD

Yee FDTD：周期平面波と完全導体空洞の実装・検証

2次元TMz（Ez、Hx、Hy）の自作教育用コードです。無次元の一様真空、電流・電荷源なしに限定し、周期平面波と完全導体（PEC）長方形空洞を連続解析解と比較しました。格子収束、数値分散、離散保存量、物理エネルギーの近似を別々に確認します。

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

コード・固定入力・再実行

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

2次元TMz・一様真空の周期平面波と長方形PEC空洞の教育用実装・固定入力検証です。解析解と独自に導いた離散モード・保存量を参照し、他のFDTDライブラリとの比較は行っていません。PML、反射・透過、散乱体、電荷・電流、分散媒質、3次元一般形状は未実装・未検証です。

## 文献

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
