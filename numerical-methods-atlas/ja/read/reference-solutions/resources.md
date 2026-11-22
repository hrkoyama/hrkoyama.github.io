# 厳密解・参照解ライブラリ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

章固有の対応は未登録です。全体一覧：[手法・コードの対応表](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=ja)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  reference_kind: analytic

  解析解 単位区間の周期境界、一定移流速度1。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  reference_kind: analytic

  解析解 単位区間の周期境界、拡散係数0.02。
- [Burgers／衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-shock-ja>)
  reference_kind: analytic

  解析解 全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。
- [Burgers／膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-fan-ja>)
  reference_kind: analytic

  解析解 全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。
- [交通流／上流へ進む衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-jam-ja>)
  reference_kind: analytic

  解析解 全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。
- [交通流／渋滞解消の膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-fan-ja>)
  reference_kind: analytic

  解析解 全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。
- [Euler／Sod問題](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja>)
  reference_kind: semi-analytic

  半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。
- [Euler／Lax問題](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-lax-ja>)
  reference_kind: semi-analytic

  半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。
- [Euler／二重膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja>)
  reference_kind: semi-analytic

  半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。
- [Euler／生成される真空](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-vacuum-ja>)
  reference_kind: analytic

  解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。
- [浅水流／水深が正のダム崩壊](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dam-break-ja>)
  reference_kind: semi-analytic

  半解析解 平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。
- [浅水／乾床への膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja>)
  reference_kind: analytic

  解析解 平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。
- [浅水／中央の乾燥領域](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-vacuum-ja>)
  reference_kind: analytic

  解析解 平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。
- [等温流／密度跳躍](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isothermal-jump-ja>)
  reference_kind: semi-analytic

  半解析解 p = c_s² rho、一定の音速c_s。初期密度は厳密に正とし、真空状態とエネルギー方程式はありません。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。
- [粘性チャネル／Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-couette-ja>)
  reference_kind: analytic

  解析解 十分に発達した平面定常チャネル。壁速度u(0)=0、u(1)=1、圧力勾配ゼロ。
- [粘性チャネル／Poiseuille流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poiseuille-ja>)
  reference_kind: analytic

  解析解 十分に発達した平面定常チャネル、no-slip、単位密度。−dp/dx=G、または体積力加速度G。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  reference_kind: analytic

  解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。

## コード・検証

章固有の対応は未登録です。全体一覧：[コード・入力・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja)
