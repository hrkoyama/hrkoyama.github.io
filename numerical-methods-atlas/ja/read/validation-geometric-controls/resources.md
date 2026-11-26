# 拘束・軌道・多周波数の幾何積分

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-geometric-controls/

この章に登録された手法・問題・実行例の関連資料です。 SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。

## 手法

- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

  全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。
- [SHAKE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja>)
- [RATTLE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

## 方程式

- [二周波数の結合調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja>)

  連続正規モード、理想分割写像、保存した浮動小数点係数の写像、実際の反復丸めを区別します。 α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-algorithm>)

  独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
- [拘束付き平面振り子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja>)

  元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-algorithm>)

  独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の動径速度での交差をbrentqで局在化。
- [Kepler二体問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja>)

  無次元化した平面楕円軌道で位相、角運動量、エネルギーと刻みの影響を分けます。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-algorithm>)

  全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。
- [二周波数の結合調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja>)

  連続正規モード、理想分割写像、保存した浮動小数点係数の写像、実際の反復丸めを区別します。

## 問題の図

- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png
- [拘束付き振り子](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja>)

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja>)

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png

## 厳密解・参照解

- [結合した2周波数系と共鳴の有限窓：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#references-ja>)

  116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。 中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja>)
  reference_kind: semi-analytic

  半解析解 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja>)
  reference_kind: semi-analytic

  半解析解 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja>)
  reference_kind: semi-analytic

  半解析解 α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。
- [SHAKEとRATTLE：拘束と運動量の違い：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-validation>)

  独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。 原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
- [離心率を変えたKepler軌道と時間刻み：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-validation>)

  独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。 保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
- [結合した2周波数系と共鳴の有限窓：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-validation>)

  116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。 中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。
- [拘束付き振り子：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja>)

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。 独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 半解析解 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 半解析解 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。 原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
- [無軟化Kepler二体の時間誤差：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#references-ja>)

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja>)
  relation: same-problem
  reference_kind: analytic

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 解析解 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。 半解析解 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。 保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

## コード・検証

- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja>)
  availability: run

  2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja>)
  availability: run

  単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja>)
  availability: run

  e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。
