# LBMのRe100蓋駆動キャビティ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-cavity/

この章に登録された手法・問題・実行例の関連資料です。 LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-algorithm>)

  標準D2Q9平衡分布とBGK衝突、非周期link streaming、q=.5の移動halfway反射。流出入分布ごとに壁impulseを加算し、密度補正や内部速度resetをしません。C++17を一時領域でcompileしPythonから呼びます。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

## 問題の図

- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png
- [Re100の蓋駆動キャビティ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja>)

  LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png

## 厳密解・参照解

- [LBMのRe100キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。
- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-validation>)

  各群22pytestと37判定。60k/80k/120k整数stepsでt*=100へ進み90/95/100を保存。最細u/v中心線最大誤差.03、主渦距離.06、95→100相対L2変化2e-4、質量・壁込み運動量ledgerを事前固定します。
- [Ghia Re100：原著の有限格子速度中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。 Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。
- [LBMのRe100キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。 物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。
- [Re100の蓋駆動キャビティ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja>)

  LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。 21単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。
- [Ghia Re100：原著の有限格子速度中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。 有限格子の数値参照 単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。 Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。
- [LBMのRe100キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja>)
  relation: related-model
  reference_kind: numerical-reference

  LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。 有限格子の数値参照 物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。 物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

## コード・検証

- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja>)
  availability: run

  4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。
