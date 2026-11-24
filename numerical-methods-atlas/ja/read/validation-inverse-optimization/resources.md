# Bratu逆問題の最適化・雑音・正則化

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-inverse-optimization/

この章に登録された手法・問題・実行例の関連資料です。 既存の合成観測を保持し、小さな固定例でGN/LM・準Newton・正則化選択を比較します。

## 手法

- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

  独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。
- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

  独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。
- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

  全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。
- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

## 方程式

- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。
- [有限次元代数最適化と既知最小点](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja>)

  8次元SPD二次関数と2変数Rosenbrockの無次元代数最適化です。物理空間・PDE境界を持たず、既知最小点と局所反復作用を比較します。 無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。
- [有限次元代数最適化と既知最小点](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja>)

  8次元SPD二次関数と2変数Rosenbrockの無次元代数最適化です。物理空間・PDE境界を持たず、既知最小点と局所反復作用を比較します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-algorithm>)

  独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-algorithm>)

  独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-algorithm>)

  全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

## 問題の図

- [GN・LMと有界最小二乗のBratu比較](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png
- [既知最小点でのBFGSと3組L-BFGS](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png
- [雑音・モデル差と有限γ経路の正則化](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png
- [GN・LMと有界最小二乗のBratu比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png
- [既知最小点でのBFGSと3組L-BFGS](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png
- [雑音・モデル差と有限γ経路の正則化](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png

## 厳密解・参照解

- [GN・LMと有界最小二乗のBratu比較：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#references-ja>)

  独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。
- [Bratu逆最小二乗の独立Thomas局所参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D零Dirichlet Bratuの31内点と5観測を用いる2係数逆問題。既存合成観測を再利用し、物理boxはa∈[1,2.8],b∈[-.5,.5]。目的正則化γ、LM減衰μ、変数尺度は別です。 小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。
- [既知最小点でのBFGSと3組L-BFGS：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#references-ja>)

  16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。
- [既知最小点と現在の有限記憶作用に対する解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元・非有界の代数最適化。8次元SPD二次関数とRosenbrockの3初期値を用い、L-BFGSは現在の最大3組だけを保持します。物理PDE境界条件はありません。 厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。
- [雑音・モデル差と有限γ経路の正則化：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#references-ja>)

  42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。
- [有限γ経路と局所線形雑音伝播のBratu参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 31内点、5観測、W=I/5、Σ=σ²I。既存の31/1023格子観測を再利用します。雑音の標準偏差σは1e-4と1e-3で、独立な基底雑音は2 seedです。尺度・格子文脈をまたぐ比較は同じ雑音ベクトルを共有します。γは固定5点です。 楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。
- [Bratu逆最小二乗の独立Thomas局所参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1D零Dirichlet Bratuの31内点と5観測を用いる2係数逆問題。既存合成観測を再利用し、物理boxはa∈[1,2.8],b∈[-.5,.5]。目的正則化γ、LM減衰μ、変数尺度は別です。
- [既知最小点と現在の有限記憶作用に対する解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja>)
  reference_kind: analytic

  解析解 無次元・非有界の代数最適化。8次元SPD二次関数とRosenbrockの3初期値を用い、L-BFGSは現在の最大3組だけを保持します。物理PDE境界条件はありません。
- [有限γ経路と局所線形雑音伝播のBratu参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 31内点、5観測、W=I/5、Σ=σ²I。既存の31/1023格子観測を再利用します。雑音の標準偏差σは1e-4と1e-3で、独立な基底雑音は2 seedです。尺度・格子文脈をまたぐ比較は同じ雑音ベクトルを共有します。γは固定5点です。
- [GN・LMと有界最小二乗のBratu比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-validation>)

  独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。
- [Bratu逆最小二乗の独立Thomas局所参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D零Dirichlet Bratuの31内点と5観測を用いる2係数逆問題。既存合成観測を再利用し、物理boxはa∈[1,2.8],b∈[-.5,.5]。目的正則化γ、LM減衰μ、変数尺度は別です。 小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。
- [既知最小点でのBFGSと3組L-BFGS：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-validation>)

  16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。
- [既知最小点と現在の有限記憶作用に対する解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元・非有界の代数最適化。8次元SPD二次関数とRosenbrockの3初期値を用い、L-BFGSは現在の最大3組だけを保持します。物理PDE境界条件はありません。 厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。
- [雑音・モデル差と有限γ経路の正則化：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-validation>)

  42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。
- [有限γ経路と局所線形雑音伝播のBratu参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 31内点、5観測、W=I/5、Σ=σ²I。既存の31/1023格子観測を再利用します。雑音の標準偏差σは1e-4と1e-3で、独立な基底雑音は2 seedです。尺度・格子文脈をまたぐ比較は同じ雑音ベクトルを共有します。γは固定5点です。 楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

## コード・検証

- [GN・LMと有界最小二乗のBratu比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja>)
  availability: run

  同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。
- [既知最小点でのBFGSと3組L-BFGS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja>)
  availability: run

  8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。
- [雑音・モデル差と有限γ経路の正則化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja>)
  availability: run

  2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。
