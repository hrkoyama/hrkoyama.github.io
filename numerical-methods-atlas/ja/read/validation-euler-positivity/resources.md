# Euler二重膨張波：段階ごとの正値性

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-euler-positivity/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Lax–Friedrichs法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [平均を保つ正値状態スケーリング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=ja>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-algorithm>)

  保存量の無制限中央線形再構築を行い、セル平均と左右2端点へ共通の係数θを用いて密度・圧力を正にします。端点平均は元の保存量平均のままです。共有LF流束による前進Euler更新をSSPRK(3,3)で凸結合し、各段の流束前に再構築と制限をやり直します。ε=10⁻¹³は再構築の目標で、密度・エネルギーを加えるfloorではありません。平均の修復・無言の刻み再試行は行いません。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png

## 厳密解・参照解

- [Euler二重膨張波：段階ごとの正値性：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-validation>)

  27単体検査と3格子73判定を実行前に固定します。スケーリング前に生じる負の端点圧力を保持し、制限後の端点・前進Euler平均・SSP凸結合平均、θ、全3保存量の境界流束収支を別々に測ります。閉形式の対称希薄波と既存の独立な対数圧力根探索を照合し、保存量のGauss8/16セル平均との誤差と格子細分化を記録します。
- [Euler／二重膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja>)
  relation: related-model
  reference_kind: semi-analytic

  半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。 γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

## コード・検証

- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja>)
  availability: run

  既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
