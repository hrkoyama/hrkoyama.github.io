# 非一様ALE輸送・2次元回転浅水波

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/

この章に登録された手法・問題・実行例の関連資料です。 非一様に動くセルの保存的ALE輸送とGCL、および2次元C格子の線形回転浅水波を時間発展させます。SaltzmanピストンとWilliamson球面問題は次段階の未実装項目です。

## 手法

- [ALE一様状態・幾何保存モデル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja>)

  実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。
- [ALE一様状態・幾何保存モデル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [移動セル上のALEスカラー保存式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja>)

  指定した非一様格子の面位置とセル質量を同じHeun段で更新し、幾何保存則と非一様な波の輸送を別々に評価します。Euler流体のLagrange/remap法ではありません。 周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。
- [線形回転浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja>)

  平面f-planeの線形波を実際の2D staggered C-gridでRK4時間発展します。連続分散と離散記号の参照を分け、質量・エネルギー・慣性振動・離散定常釣合いを確認します。 線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。
- [移動セル上のALEスカラー保存式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja>)

  指定した非一様格子の面位置とセル質量を同じHeun段で更新し、幾何保存則と非一様な波の輸送を別々に評価します。Euler流体のLagrange/remap法ではありません。
- [線形回転浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja>)

  平面f-planeの線形波を実際の2D staggered C-gridでRK4時間発展します。連続分散と離散記号の参照を分け、質量・エネルギー・慣性振動・離散定常釣合いを確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-algorithm>)

  実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-algorithm>)

  セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

## 問題の図

- [非一様移動格子で実際に運ぶALEスカラー](<https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png
- [2D C-grid回転浅水波の実時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png
- [非一様移動格子で実際に運ぶALEスカラー](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png
- [2D C-grid回転浅水波の実時間発展](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png

## 厳密解・参照解

- [非一様移動格子で実際に運ぶALEスカラー：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja>)

  解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。
- [ALE：実際の移動セル上の解析積分と時間参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。解析解q(x,t)=1+.2sin[2π(x−.7t)]を、主計算が保存した実際の面位置の間で積分します。解析面位置との幾何誤差を別記し、時間検査は同じFV ODEを二公差の独立DOP853で解きます。 1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。
- [2D C-grid回転浅水波の実時間発展：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#references-ja>)

  連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。
- [C-grid：連続Fourier解と離散記号の行列指数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。η₀=.01cos[2π(x+2y)]、u₀=v₀=0を、連続3×3 Fourier作用素と離散3×3記号の行列指数で別々に発展させます。主計算は実際の2次元staggered場を時間更新します。 線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。
- [ALE：実際の移動セル上の解析積分と時間参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja>)
  reference_kind: analytic

  解析解 周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。解析解q(x,t)=1+.2sin[2π(x−.7t)]を、主計算が保存した実際の面位置の間で積分します。解析面位置との幾何誤差を別記し、時間検査は同じFV ODEを二公差の独立DOP853で解きます。
- [C-grid：連続Fourier解と離散記号の行列指数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja>)
  reference_kind: analytic

  解析解 線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。η₀=.01cos[2π(x+2y)]、u₀=v₀=0を、連続3×3 Fourier作用素と離散3×3記号の行列指数で別々に発展させます。主計算は実際の2次元staggered場を時間更新します。
- [非一様移動格子で実際に運ぶALEスカラー：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-validation>)

  解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。
- [ALE：実際の移動セル上の解析積分と時間参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。解析解q(x,t)=1+.2sin[2π(x−.7t)]を、主計算が保存した実際の面位置の間で積分します。解析面位置との幾何誤差を別記し、時間検査は同じFV ODEを二公差の独立DOP853で解きます。 1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。
- [2D C-grid回転浅水波の実時間発展：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-validation>)

  連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。
- [C-grid：連続Fourier解と離散記号の行列指数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。η₀=.01cos[2π(x+2y)]、u₀=v₀=0を、連続3×3 Fourier作用素と離散3×3記号の行列指数で別々に発展させます。主計算は実際の2次元staggered場を時間更新します。 線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

## コード・検証

- [非一様移動格子で実際に運ぶALEスカラー](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja>)
  availability: run

  質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。
- [2D C-grid回転浅水波の実時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja>)
  availability: run

  実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。
