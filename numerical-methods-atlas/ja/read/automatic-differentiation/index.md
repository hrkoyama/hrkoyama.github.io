# 自動微分

自動微分はプログラムの基本演算へ連鎖律を適用して導関数を計算します。数式の記号微分でも、有限差分で刻みを選ぶ数値微分でもありません。

## 対象と代表式

中間変数z=φ(x)に対し、forward modeは方向微分ż=φ_x ẋを、reverse modeは出力側の随伴量z̄からx̄へφ_xᵀz̄を足し戻します。浮動小数点の丸めを伴うため「完全に誤差ゼロ」ではありませんが、有限差分の打切り誤差は導入しません。

$$
\dot z=\frac{\partial\phi}{\partial x}\dot x,\qquad \bar x\mathrel{+}=\left(\frac{\partial\phi}{\partial x}\right)^T\bar z,\qquad w^T(Jv)=v^T(J^Tw).
$$

## 計算の流れ

計算を基本演算へ分解し、値とtangentまたは逆伝播に必要な履歴を記録します。少数入力ならforward、スカラー出力・多数入力ならreverseが有利な典型例です。暗黙に定まる収束解を微分する場合は、反復列の微分と暗黙関数の微分を区別します。

## 適用条件と落とし穴

分岐では実行された経路の微分を計算します。絶対値、max、limiters、接触やイベントでは微分不能性と採用した規約を確認します。stop-gradient、外部演算、反復停止条件の扱いにも注意します。丸め誤差を含む不連続なビット操作全体の古典微分を保証する技術ではありません。

## 検証するときに見る量

解析微分のある小関数、方向Taylor試験、forward/reverseの内積恒等式wᵀ(Jv)=vᵀ(Jᵀw)で検査します。有限差分との比較では丸めが支配するほど刻みを小さくしません。PDE残差への適用では境界・パラメータ依存も含めます。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- R. E. Wengert (1964). A simple automatic derivative evaluation program. https://doi.org/10.1145/355586.364791
- Seppo Linnainmaa (1976). Taylor expansion of the accumulated rounding error. https://doi.org/10.1007/bf01931367
