# Markov連鎖Monte Carlo

MCMCは目的分布を不変分布に持つMarkov連鎖を作り、独立標本を直接生成しにくい積分を推定します。不変性と、有限時間で十分探索できることは別の条件です。

## 対象と代表式

非正規化密度π(x)と提案密度q(y|x)に対し、Metropolis–Hastings受理確率を使います。πの未知の正規化定数は比で消えます。対称なqでは提案比が消えますが、非対称提案でこれを省略すると目的分布を変えます。

$$
a(x,y)=\min\!\left(1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right),\qquad N_{\rm eff}\approx\frac{N}{1+2\sum_{k\ge1}\rho_k}.
$$

## 計算の流れ

候補yを引いて受理/棄却し、棄却時にも現在の状態を標本に残します。初期過渡を評価し、複数の異なる初期値から鎖を動かします。自己相関ρₖを使う有効標本数N_effの近似は、定常性と自己相関の推定が妥当な場合に解釈します。

## 適用条件と落とし穴

詳細釣合いだけでは既約性や非周期性は保証されません。多峰性、強い相関、境界で混合が遅くなります。高い受理率だけを目標にすると微小移動に終わり得ます。鎖の間引きは、固定した計算量で情報を増やす一般的な解決策ではありません。

## 検証するときに見る量

Gaussianなど既知分布で平均・分散・分位点を確認し、非対称提案の補正と棄却標本も試験します。多峰性の例では鎖間比較・自己相関・有効標本数・期待値の不確かさを報告し、見た目の定常性だけで収束としません。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- Nicholas Metropolis and Arianna W. Rosenbluth and Marshall N. Rosenbluth and Augusta H. Teller and Edward Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://doi.org/10.1093/biomet/57.1.97
