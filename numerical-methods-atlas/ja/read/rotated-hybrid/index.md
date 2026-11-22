# 回転ハイブリッド・リーマンソルバー

回転Riemann法では、セル面の法線以外の方向も使って散逸を構成します。Ren（2003）のrotated Roeと、Nishikawa–Kitamura（2008）のrotated-hybridは関連しますが同一の方式ではありません。

## 対象と代表式

2次元Euler状態U_L,U_Rと単位面法線nを考えます。直交単位ベクトルn₁,n₂でn=α₁n₁+α₂n₂と分解し、各方向の流束を組み合わせます。下式は本アトラスの教育用HLLE/Roe実験の定義であり、2008年論文の最適化された散逸式そのものではありません。

$$
\mathbf n=\alpha_1\mathbf n_1+\alpha_2\mathbf n_2,\qquad\widehat F(\mathbf n)=\alpha_1\widehat F_{\rm HLLE}(\mathbf n_1)+\alpha_2\widehat F_{\rm Roe}(\mathbf n_2).
$$

## 計算の流れ

実装ではn₁を速度差に合わせ、面法線との内積が非負になるよう向きをそろえます。速度差が小さい場合は面の接線をn₁に選びます。同じ左右状態を各局所座標へ回し、HLLE/Roeを評価し、運動量流束を元の座標へ戻して足します。圧力センサーによる単純な流束ブレンドとは異なります。

## 適用条件と落とし穴

Roe（1981）は構成要素となる近似Riemannソルバーの原論文です。2003年のrotated法の論文はY.-X. Ren単著、2008年のrotated-hybridは西川・北村です。Roe・Nishikawa・Ismail・Scalabrin（2005）はcarbuncleの関連研究で、この2008年論文の著者・年とは混同しません。一般のcarbuncle除去や正値性を保証する主張はしません。

## 検証するときに見る量

一定状態の整合性、左右交換と法線反転による流束の符号、座標回転を調べます。法線方向の圧縮と純接線せん断を分け、摂動した強い平面衝撃波と鈍頭物体でも条件を固定して比較します。既存配布版の検査・結果の範囲は元の記録へリンクし、新しい論文再現を実施したとは表示しません。

## 公開範囲

既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。

## 文献

- Yu-Xin Ren (2003). A robust shock-capturing scheme based on rotated Riemann solvers. https://doi.org/10.1016/s0045-7930(02)00114-7
- Nishikawa, Hiroaki and Kitamura, Keiichi (2008). Very simple, carbuncle-free, boundary-layer-resolving, rotated-hybrid Riemann solvers. https://doi.org/10.1016/j.jcp.2007.11.003
- Philip Roe and Hiroaki Nishikawa and Farzad Ismail and Leonardo Scalabrin (2005). On Carbuncles and Other Excrescences. https://doi.org/10.2514/6.2005-4872
- Roe, Philip L. (1981). Approximate Riemann solvers, parameter vectors, and difference schemes. https://doi.org/10.1016/0021-9991(81)90128-5
