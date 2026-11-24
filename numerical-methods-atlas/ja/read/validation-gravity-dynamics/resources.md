# 重力軌道：Keplerと軟化有限粒子

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/

この章に登録された手法・問題・実行例の関連資料です。 厳密なKepler軌道と、同じ軟化核を使う短時間の有限粒子ODE参照を区別します。

## 手法

- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。 独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の放射速度交差をbrentqで局在化。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。
- [Barnes–Hut八分木](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja>)

  直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)
- [Barnes–Hut八分木](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja>)

## 方程式

- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。
- [Kepler二体問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja>)

  無次元化した平面楕円軌道で位相、角運動量、エネルギーと刻みの影響を分けます。 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-algorithm>)

  位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-algorithm>)

  直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

## 問題の図

- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png

## 厳密解・参照解

- [無軟化Kepler二体の時間誤差：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#references-ja>)

  位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。 保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
- [冷たいPlummer密度由来32粒子の短時間力学：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#references-ja>)

  非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。 非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja>)
  reference_kind: analytic

  解析解 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。 非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。
- [無軟化Kepler二体の時間誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-validation>)

  位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。 保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
- [冷たいPlummer密度由来32粒子の短時間力学：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-validation>)

  非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。 非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

## コード・検証

- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja>)
  availability: run

  非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja>)
  availability: run

  e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja>)
  availability: run

  同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。
