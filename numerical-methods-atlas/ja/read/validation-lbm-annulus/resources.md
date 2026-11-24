# 曲面LBMの環状Couette流

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-annulus/

この章に登録された手法・問題・実行例の関連資料です。 同じ物理条件で格子を細かくし、曲面補間と階段壁の速度・点ごとの圧力・トルクを解析解に照合します。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。
- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

## 方程式

- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。 Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-algorithm>)

  円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

## 問題の図

- [曲面LBMの環状Couette制御：速度・圧力・torque](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png
- [曲面LBMの環状Couette制御：速度・圧力・torque](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png

## 厳密解・参照解

- [曲面LBMの環状Couette制御：速度・圧力・torque：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#references-ja>)

  群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。
- [曲面LBMの環状Couette制御：速度・圧力・トルク](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。 固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。
- [曲面LBMの環状Couette制御：速度・圧力・トルク](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja>)
  reference_kind: analytic

  解析解 Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。
- [曲面LBMの環状Couette制御：速度・圧力・torque：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-validation>)

  群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。
- [曲面LBMの環状Couette制御：速度・圧力・トルク](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。 固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

## コード・検証

- [曲面LBMの環状Couette制御：速度・圧力・torque](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja>)
  availability: run

  実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。
