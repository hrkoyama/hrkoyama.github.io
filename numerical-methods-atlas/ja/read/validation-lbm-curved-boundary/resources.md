# LBMの曲面壁とRe20円柱

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-curved-boundary/

この章に登録された手法・問題・実行例の関連資料です。 Re20円柱流の曲面壁と流出境界を実計算し、抗力・圧力差・後流を独立な数値ベンチマークへ照合します。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。
- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

## 方程式

- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。 [0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 [0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-algorithm>)

  標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

## 問題の図

- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png
- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png

## 厳密解・参照解

- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#references-ja>)

  群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。
- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。 原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。
- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。
- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-validation>)

  群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。
- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。 原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

## コード・検証

- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja>)
  availability: run

  標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。
