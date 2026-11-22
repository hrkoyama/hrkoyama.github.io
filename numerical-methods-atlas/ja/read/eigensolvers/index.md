# Krylov固有値解法

Krylov固有値法は、巨大な行列全体を対角化せず、少数の固有対を小さい部分空間から近似します。Arnoldi、対称問題のLanczos、シフト反転では必要な仮定が異なります。

## 対象と代表式

初期ベクトルvからKₘ(A,v)=span{v,Av,…,Aᵐ⁻¹v}を作ります。直交基底Vₘと上Hessenberg行列HₘのArnoldi関係から、Hₘy=θyを解いてx=VₘyをRitzベクトルとします。最後の基底ベクトルとhₘ₊₁,ₘが残差を表します。

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T,\qquad \|Ax-\theta x\|_2=|h_{m+1,m}e_m^Ty|\quad(\|y\|_2=1).
$$

## 計算の流れ

行列ベクトル積と直交化で基底を伸ばし、小さい固有値問題を解き、必要に応じて再スタートします。AがHermitianならLanczosの三項漸化式が使えます。内部固有値には(A−σI)⁻¹を作用させる方法がありますが、各作用は線形系の解法を必要とします。

## 適用条件と落とし穴

有限精度では直交性の喪失により重複した見かけの固有値が出ます。非正規行列の小残差は小さい固有値誤差を保証しません。一般化問題Ax=λBxではBの性質と内積を明記し、シフト反転の内部許容誤差も評価します。

## 検証するときに見る量

正規化した残差∥Ax−θx∥/(∥A∥+|θ|)、直交性、既知固有対、縮退/近接固有値を確認します。対称問題ではRayleigh商も比較し、再スタート数や初期ベクトル依存を記録します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792
- C. Lanczos (1950). An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. https://doi.org/10.6028/jres.045.026
