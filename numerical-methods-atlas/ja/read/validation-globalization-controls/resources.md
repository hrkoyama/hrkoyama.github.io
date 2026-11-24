# 同じ初期値から線探索と信頼領域を比べる

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-globalization-controls/

この章に登録された手法・問題・実行例の関連資料です。 原残差・scaled meritと全試行の記録から、根・非根停留・上限終了を区別します。

## 手法

- [小固定系のdogleg信頼領域法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。
- [小固定系のdogleg信頼領域法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=ja>)

  原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

## 方程式

- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-algorithm>)

  原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。
- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

## 問題の図

- [同じ難しい初期値に対する線探索と信頼領域](<https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png
- [同じ難しい初期値に対する線探索と信頼領域](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png

## 厳密解・参照解

- [同じ難しい初期値に対する線探索と信頼領域：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#references-ja>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [同一初期値の大域化：解析対照と離散Bratu修正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 実数・無次元の固定系。Rosenbrockの2初期値と2残差スケール、31内点・λ=3の同次Dirichlet Bratuの3初期値を3法で比較します。状態半径はEuclideanで、残差スケールとは別です。 全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。
- [同一初期値の大域化：解析対照と離散Bratu修正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 実数・無次元の固定系。Rosenbrockの2初期値と2残差スケール、31内点・λ=3の同次Dirichlet Bratuの3初期値を3法で比較します。状態半径はEuclideanで、残差スケールとは別です。
- [同じ難しい初期値に対する線探索と信頼領域：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-validation>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [同一初期値の大域化：解析対照と離散Bratu修正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 実数・無次元の固定系。Rosenbrockの2初期値と2残差スケール、31内点・λ=3の同次Dirichlet Bratuの3初期値を3法で比較します。状態半径はEuclideanで、残差スケールとは別です。 全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

## コード・検証

- [同じ難しい初期値に対する線探索と信頼領域](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja>)
  availability: run

  同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。
- [小固定系のdogleg信頼領域法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
