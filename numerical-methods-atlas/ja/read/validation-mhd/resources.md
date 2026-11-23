# 流体・MHDの独立照合とCT／GLM

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [制約輸送法／CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja>)
- [GLM発散クリーニング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja>)
- [HLLDのMHDリーマン解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-algorithm>)

  公開済みの1次Rusanov/前進Eulerを再利用。CTは共有corner EMFの離散curl、GLMはcell中心Bと双曲・放物型cleaning。Athena++は別実装のHLLD+PLM+RK2。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-algorithm>)

  アトラス側はMC再構成とSSPRK2、参照は独立C++のHLLD・PLM・RK3。異なる実装ですがHLLDという数値流束の系列は共有します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-algorithm>)

  アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-algorithm>)

  ∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

## 問題の図

- [Orszag–Tang：CT・GLMと独立Athena++比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png
- [Brio–Wu：別実装HLLDとの照合](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png
- [Shu–Osher：独立参照と格子収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png
- [GLMの磁気単極子モード：解析的減衰](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png

## 厳密解・参照解

- [Orszag–Tang：CT・GLMと独立Athena++比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-validation>)

  16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。
- [後期Orszag–Tang：独立有限格子の密度・圧力参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
- [Brio–Wu：別実装HLLDとの照合：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-validation>)

  128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。
- [Shu–Osher：独立参照と格子収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-validation>)

  100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。
- [GLMの磁気単極子モード：解析的減衰：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-validation>)

  16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

## コード・検証

- [Orszag–Tang：CT・GLMと独立Athena++比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja>)
  availability: run

  同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。
- [Brio–Wu：別実装HLLDとの照合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja>)
  availability: run

  公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。
- [Shu–Osher：独立参照と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja>)
  availability: run

  衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。
- [GLMの磁気単極子モード：解析的減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja>)
  availability: run

  GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。
