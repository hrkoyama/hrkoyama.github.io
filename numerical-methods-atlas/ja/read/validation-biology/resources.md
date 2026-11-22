# 非線形反応拡散・パターン形成の独立検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-algorithm>)

  二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja#schnakenberg-pattern-ja-algorithm>)

  二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。

## 問題の図

- [Schnakenberg有限振幅過渡：非線形性と独立参照](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png

## 厳密解・参照解

- [Schnakenberg有限振幅過渡：非線形性と独立参照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-validation>)

  空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja#schnakenberg-pattern-ja-validation>)

  空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

## コード・検証

- [Schnakenberg有限振幅過渡：非線形性と独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja>)
  availability: run

  t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja>)
  availability: run

  t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
