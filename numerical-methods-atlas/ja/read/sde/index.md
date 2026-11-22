# 確率微分方程式

確率微分方程式では、Brown運動の増分が√Δtの大きさを持ちます。通常のODE法へ乱数を足すだけでは、確率積分の解釈と正しい収束次数を指定できません。

## 対象と代表式

下式はItô解釈の一次元SDEです。aはdrift、bはdiffusion係数、ΔWₙは独立な平均0・分散Δtの正規変数です。Euler–Maruyamaは両係数を時刻nで評価します。Stratonovich形へ変える場合は、係数に対応するdrift補正が必要です。

$$
dX=a(X,t)\,dt+b(X,t)\,dW,\qquad X_{n+1}=X_n+a(X_n,t_n)\Delta t+b(X_n,t_n)\Delta W_n.
$$

## 計算の流れ

Brown増分を生成し、driftと確率項を更新します。粗細2つの刻みを比較するstrong誤差試験では、粗いΔWを細かいΔWの和にして同じ経路を使います。weak誤差は試験関数の期待値の差で、1本の経路の差とは別です。

## 適用条件と落とし穴

大域Lipschitz性や十分なモーメント・滑らかさなどの仮定の下で、Euler–Maruyamaは典型的にstrong 1/2、weak 1です。超線形成長や正値制約では破綻する場合があり、専用の安定化や境界処理を検討します。weak誤差より標本化誤差が大きい場合もあります。

## 検証するときに見る量

幾何Brown運動の厳密解やOrnstein–Uhlenbeckのモーメントを使い、strong/weak収束を別々に測ります。刻み依存、乱数系列、標本数、信頼区間を記録し、負値や境界逸脱も隠さず報告します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- Gisiro Maruyama (1955). Continuous Markov processes and stochastic equations. https://doi.org/10.1007/bf02846028
- Desmond J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://doi.org/10.1137/s0036144500378302
