# LBM38〜40：実行前の設計

状態は静的実装・未実行。PUBは読み取り専用。科学baselineはHR main
`9dde48159c568f985170506ef2eb0a7008f1c4ea`。既存配布物を変更しない。

3群案は `lbm-cavity`、`lbm-taylor-green`、`lbm-curved-boundary`。
case IDは草案の4件を保持し、annular controlだけを円柱実装完了と数えない。
標準D2Q9 isothermal BGK、rho=sum f、rho*u=sum c*f、cs²=1/3、nu=(tau-.5)/3。
独自のC++17 sourceを同梱しPython ctypesで呼ぶ。標準c++ compilerが追加要件。
`-O2 -std=c++17 -ffp-contract=off`、no fastmath、binは配布せずTMPDIRでcompile。
pytestとmainのcompileは各群共有120秒へ含める。目標はMac40秒程度以下。

## 壁・角・収支

outgoing方向c、fluid点x、壁までのlink割合qとする。
q<.5では `fbar_next(x)=2q*fpost_c(x)+(1-2q)*fpost_c(x-c)-6w_c*c.u_wall`。
q>=.5では `fbar_next(x)=fpost_c(x)/(2q)+(2q-1)/(2q)*fpost_bar(x)-3w_c/q*c.u_wall`。
rho_ref=1を壁補正に固定。2点の線形補間として独自に導出し、BFL型の曲面補間と
位置付ける。原著2001全文を読んだとは主張しない。2003原著のsec3の補間経路・
q=.5への縮約・壁補正とmomentum exchangeの読み取り、静止線形補間の独立導出、
moving-signと単stepの独立対照を組み合わせて資格確認する。q<.5のback点がない場合は
停止する。密度/分布clipやmass補正・曖昧なfallbackは行わない。

平面q=.5。cavityの同時上壁/側壁crossingは側壁が所有する。
open cylinderではx入口/出口のmissing linkが同時x/y crossingを所有する。
これはwet x-boundary nodeとhalfway y-wallとの端点近傍の有限格子規約であり、
角の点ごとの二次精度を主張しない。

linkごとの流体変化は dM=fin-fout、dP=-(fin+fout)c。
body力は反対符号、torqueは実交点（link平行移動なのでfluid点と同じcross product）。
曲面補間で生じる非零wall massを隠さずwall/open別ledgerに保存する。
閉cavityの質量保存と、曲面補間を含めたledger閉鎖は別の判定。
open境界はmissing incomingとoutgoingを全て実際のpopulationsから台帳化する。

## 固定入力案（main契約はcomponent後に別凍結）

38: cavity Re100、N24/32/48、nominal lid lattice .04、nu=.04N/100。
t*=100で60000/80000/120000整数steps、t*=90/95/100を保存。
未凍結草案N16/24/32から、near-half tauと最細格子精度の余裕を得るため実行前に変更した。
Ghia34点はnominal lidで正規化、主渦(.6172,.7344)、print tableを独立照合。
最細centerline max誤差.03、渦中心距離.06、95→100相対L2変化2e-4。
Ma<=.1、closed mass drift1e-8、wall込み運動量ledger scaled1e-10。

39: periodic [0,2pi)²、nu=.1、U=.2、N16/32/64、tau=.56、dt=.2dx²、
T=.2pi²、steps64/256/1024。N32でU=.4/.8のamplitude感度、同N32/U.2で
dt=.1dx²/tau.53/512stepsのcoupled step/Mach/tau感度。6runs。
u=U sinx cosy e^-2nuT、v=-U cosx siny e^-2nuT、
p=U²(cos2x+cos2y)e^-4nuT/4、mean kinetic energy U²e^-4nuT/4。
有限Mach・kinetic startupを含むcombined diffusive refinementと呼び、pure time orderと呼ばない。

40 control: annulus Rin.2/Rout.4、inner tangential physical speed.02、nu.01、
N40/60/80、tau.7、dt=(20/3)/N²、T4、steps960/2160/3840整数。
BFL型とstair-halfway各3runs。解析u_theta=Ar+B/rと圧力、torque4pi*nu*abs(B)。
初期は解析場のequilibrium。その後の更新で場をreset/forcingしない。

40 cylinder: original2D-1 geometry [0,2.2]x[0,.41]、(.2,.2)にR.05、
nu.001/rho1、peak inlet.3/mean.2/Re20。dx.01/.005、x wet nodes0..2.2、
y half-cell nodes、221x41/441x82、dt=dx/6、tau.55/.6、T30、steps18000/36000。
初期はparabolic profileとstraight-channel `p(x)=12nu*meanU/H²*(L-x)`、
`rho=1+3(dt/dx)²p`のequilibrium（circle内は非fluid）。円柱摂動は注入しない。
これは原典steady問題の初期guessであり、円柱の定常圧力参照ではない。
late physical T26/28/30を保存し、初期整合でも定常性を自動合格にしない。
入口はnominal parabolic Zou-He、出口rho1と前step内点uyのZou-He reconstruction。
これはFEATflow do-nothingの同一BCではない。

**原典の重要な追加確認:** Schäfer–Turek1996 printedp3 Fig1直下とp7のprotocolは
出口条件を使用者が選択できると明記する。したがってこの明示出口は原典自由選択の
限定実装として比較し、近年FEATflow/Nabh高精度値と同一BCの認証は主張しない。
原典Table3 printedp12の推定intervalは CD[5.57,5.59]、CL[.0104,.0110]、
La[.0842,.0852]、dp[.1172,.1176]。厳密な誤差区間ではない。
今回の粗LBMは別の事前教育用公差（CD距離5%、CL絶対距離.01、La絶対距離.025、
dp距離10%）とstationarity/finite-Mach/2grid差を判定する予定。
力は2F/(rho*meanU²D)、dpは(.15,.2)-(.25,.2)。
本componentは参照値を生成せず、両open境界のmomentsとledgerを一stepで資格確認する。

## この段階の実行境界

componentだけを別契約でrootレビュー。静的source・入力・公差・固定timing workloadを
先に凍結し、許可後に初めてcompile/import/単step検査する。
timingは毎回同じ有限入力へresetする一step操作で、mainの非定常軌道を作らない。
全main/pytestはまだ未実行。componentの推定時間はmain実測やLinux保証ではない。
