# Chebyshev近似

Chebyshev近似は端点に密な節点と三角関数との関係を使う多項式近似です。Chebyshev補間、重み付き射影、最良一様近似は同じではありません。

## 対象と代表式

Tₖ(cosθ)=cos(kθ)とし、区間[−1,1]でf≈ΣaₖTₖを表します。Lobatto節点xⱼ=cos(jπ/n)を用いると離散cosine変換で補間係数を求められます。直交性の重みは(1−x²)⁻¹/²で、Legendreの重み1とは異なります。

$$
T_0(x)=1,\quad T_1(x)=x,\quad T_{k+1}(x)=2xT_k(x)-T_{k-1}(x),\qquad x_j=\cos(j\pi/n).
$$

## 計算の流れ

物理区間を[−1,1]へ写像し、節点で関数を評価して係数を求め、漸化式で級数を評価します。Clenshaw–Curtis積分はこの補間多項式を積分する方式で、一般の関数に対するGauss則とは節点も厳密次数も同一ではありません。

## 適用条件と落とし穴

解析的な関数では速い係数減衰が期待できますが、不連続にはGibbs振動が現れ、滑らかさが有限なら減衰も遅くなります。高階微分は係数誤差を増幅します。最高次付近の係数が小さいことだけで、未サンプルの細い構造がないとは言えません。

## 検証するときに見る量

Tₖ自身の再現と節点補間、exp(x)の誤差、絶対値や段差での収束の変化を調べます。節点とは異なる点で誤差を測り、区間変換の微分係数も確認します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- C. W. Clenshaw and A. R. Curtis (1960). A method for numerical integration on an automatic computer. https://doi.org/10.1007/bf01386223
- F. W. J. Olver and A. B. Olde Daalhuis and D. W. Lozier and B. I. Schneider and R. F. Boisvert and C. W. Clark and B. R. Miller and B. V. Saunders and H. S. Cohl and M. A. McClain (eds.) (2010). NIST Digital Library of Mathematical Functions. https://dlmf.nist.gov/
