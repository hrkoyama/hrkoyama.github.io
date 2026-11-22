# Particle Mesh Ewald（PME）

PMEはEwald法の逆空間項を粒子から格子へ移し、FFTを使う方法です。原PMEのLagrange補間と、後のSPMEのB-spline補間を区別して読みます。

## 対象と代表式

中性・3次元周期のCoulomb系で、格子点xₘに割り当てた電荷Qₘを考えます。Wₘは割当重み、ĜₕはEwaldのGaussian因子、格子規約、補間補正を含む逆空間作用素です。この模式式は逆空間部分だけで、実空間・自己項を置き換えません。

$$
Q_{\mathbf m}=\sum_iq_iW_{\mathbf m}(\mathbf r_i),\qquad\phi_h=\mathcal F_h^{-1}\!\left[\widehat G_h\,\mathcal F_h Q\right].
$$

## 計算の流れ

原法では局所Lagrange補間で電荷を格子へ割り当て、離散Fourier変換、格子上の畳み込み、逆変換を行います。力の微分方法と粒子への補間を一組として定義します。格子上で得た電場とエネルギー微分の力が、選んだ離散化で一致するとは限りません。

## 適用条件と落とし穴

格子を細かくする誤差、補間次数、Ewaldの打切り、力の微分規約を混ぜずに比較します。FFTの正規化とk=0、単位を明記します。O(N log N)は通常の格子増大の仮定を伴う計算量の説明で、精度の保証ではありません。

## 検証するときに見る量

同一の小さい中性セルについて、十分収束した直接Ewald和を参照にします。格子数・補間次数・分割定数を変え、エネルギーと力のRMS/最大誤差、平行移動依存性を調べます。重力PMの成功をPMEの検証に流用しません。

## 公開範囲

既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。

## 文献

- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
