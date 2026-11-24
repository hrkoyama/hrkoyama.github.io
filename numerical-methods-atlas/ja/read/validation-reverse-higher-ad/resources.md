# 逆モード・HVP・非滑らか分岐の微分

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-reverse-higher-ad/

この章に登録された手法・問題・実行例の関連資料です。 小さい独自tapeを独立手計算と照合し、状態固定の偏微分・陰関数全微分・実行分岐を分けます。

## 手法

- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

  逆topological順のcotangent加算と独立の前向き方向計算です。
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

  値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

  strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

## 方程式

- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。 小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。
- [有限次元非線形写像・根と微分作用](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja>)

  有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-algorithm>)

  逆topological順のcotangent加算と独立の前向き方向計算です。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-algorithm>)

  値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-algorithm>)

  strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。

## 問題の図

- [独自逆モードVJPとJVP/VJP双対性](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png
- [HVPと状態固定・陰関数全微分の区別](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png
- [非滑らか点・分岐・停止条件の微分範囲](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png
- [独自逆モードVJPとJVP/VJP双対性](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png
- [HVPと状態固定・陰関数全微分の区別](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png
- [非滑らか点・分岐・停止条件の微分範囲](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png

## 厳密解・参照解

- [独自逆モードVJPとJVP/VJP双対性：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja#references-ja>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [離散非線形写像の独立Jacobian・JVP・VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-reverse-vjp-duality-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 固定R4→R3写像は重複gather[0,0,2]とscalar broadcastを含みます。wide写像と固定Bratu状態はサイズ7/31。Euclidean pullbackと指定SPD計量の随伴を区別します。 一般のNumPy/JAX置換や複素数ADではありません。
- [HVPと状態固定・陰関数全微分の区別：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja#references-ja>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [固定状態HVPと二階陰関数則の独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hessian-vector-products-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 4変数のdyadic二次関数とサイズ7/31の固定Bratu energyを用います。別の正枝陰関数u²−θ=0はθ=4、初期値u=3から解き、状態固定偏微分と全微分を分けます。 一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。
- [非滑らか点・分岐・停止条件の微分範囲：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja#references-ja>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [非滑らかな離散写像：一方向微分と実行trace](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kink-branch-derivatives-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 abs・ReLU・clip・多項式分岐の固定7点と方向±1を用います。停止反復はx0=0、更新前に|xk−θ|≤1/8を検査し最大5更新。θ=1/4,1/2,1は切替点です。 選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。
- [離散非線形写像の独立Jacobian・JVP・VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-reverse-vjp-duality-ja>)
  reference_kind: analytic

  解析解 固定R4→R3写像は重複gather[0,0,2]とscalar broadcastを含みます。wide写像と固定Bratu状態はサイズ7/31。Euclidean pullbackと指定SPD計量の随伴を区別します。
- [固定状態HVPと二階陰関数則の独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hessian-vector-products-ja>)
  reference_kind: analytic

  解析解 4変数のdyadic二次関数とサイズ7/31の固定Bratu energyを用います。別の正枝陰関数u²−θ=0はθ=4、初期値u=3から解き、状態固定偏微分と全微分を分けます。
- [非滑らかな離散写像：一方向微分と実行trace](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kink-branch-derivatives-ja>)
  reference_kind: analytic

  解析解 abs・ReLU・clip・多項式分岐の固定7点と方向±1を用います。停止反復はx0=0、更新前に|xk−θ|≤1/8を検査し最大5更新。θ=1/4,1/2,1は切替点です。
- [独自逆モードVJPとJVP/VJP双対性：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-validation>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [離散非線形写像の独立Jacobian・JVP・VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-reverse-vjp-duality-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 固定R4→R3写像は重複gather[0,0,2]とscalar broadcastを含みます。wide写像と固定Bratu状態はサイズ7/31。Euclidean pullbackと指定SPD計量の随伴を区別します。 一般のNumPy/JAX置換や複素数ADではありません。
- [HVPと状態固定・陰関数全微分の区別：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-validation>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [固定状態HVPと二階陰関数則の独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hessian-vector-products-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 4変数のdyadic二次関数とサイズ7/31の固定Bratu energyを用います。別の正枝陰関数u²−θ=0はθ=4、初期値u=3から解き、状態固定偏微分と全微分を分けます。 一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。
- [非滑らか点・分岐・停止条件の微分範囲：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-validation>)

  固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。
- [非滑らかな離散写像：一方向微分と実行trace](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kink-branch-derivatives-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 abs・ReLU・clip・多項式分岐の固定7点と方向±1を用います。停止反復はx0=0、更新前に|xk−θ|≤1/8を検査し最大5更新。θ=1/4,1/2,1は切替点です。 選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。

## コード・検証

- [独自逆モードVJPとJVP/VJP双対性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja>)
  availability: run

  重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。
- [HVPと状態固定・陰関数全微分の区別](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja>)
  availability: run

  forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。
- [非滑らか点・分岐・停止条件の微分範囲](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja>)
  availability: run

  古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。
