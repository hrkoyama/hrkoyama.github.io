# Smooth PME（SPME）

SPMEは滑らかなcardinal B-splineによってEwald構造因子を格子上で近似します。PMEの同義語としてではなく、補間と力の定義を伴う変種として扱います。

## 対象と代表式

各座標の格子単位での粒子位置をuᵢとし、次数ではなくorderがpのcardinal B-spline Mₚを用います。下式の積は3方向の局所割当を表します。FFTで得る構造因子には、B-splineのFourier応答に応じた補正が必要です。

$$
Q_{m_xm_ym_z}=\sum_iq_i\prod_{d\in\{x,y,z\}}M_p(u_{id}-m_d),\qquad \deg M_p=p-1.
$$

## 計算の流れ

電荷をp個ずつの近傍格子へ割り当て、FFTと補正済み逆空間核から格子エネルギーを求めます。解析的微分ではB-splineの微分を使って粒子の力を計算します。次数・格子と合わせて、解析的微分かFourier空間微分かを記録します。

## 適用条件と落とし穴

滑らかな補間だけで、エネルギー保存と総運動量保存が同時に保証されるわけではありません。境界・中性条件・自己項はEwaldから引き継ぎます。原PMEとの比較では、格子数だけでなく同じ許容誤差になるまで各方式の条件をそろえます。

## 検証するときに見る量

同じ直接Ewald参照に対して力の誤差を測定し、エネルギーの位置差分でも確認します。平行移動に伴う格子誤差と総力を別々に報告します。実空間打切りの誤差が支配していないかも調べます。

## 公開範囲

既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。

## 文献

- Essmann, Ulrich and Perera, Lalith and Berkowitz, Max L. and Darden, Tom and Lee, Hsing and Pedersen, Lee G. (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117
- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
