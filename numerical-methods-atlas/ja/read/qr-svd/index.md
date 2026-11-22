# QR・SVD・最小二乗

最小二乗、低ランク近似、条件数の診断には、同じ行列でも異なる分解が役立ちます。QRは直交化と三角系へ、SVDは特異値と可解な方向へ問題を分けます。

## 対象と代表式

m≥nの実行列Aに対する薄いQRではQᵀQ=I、Rは上三角です。列フルランクなら最小二乗解はRx=Qᵀbで求まります。SVDのσᵢは非負の特異値で、閾値以下を切る疑似逆行列は、元と同じ問題ではなく正則化した問題を解きます。

$$
A=QR=U\Sigma V^T,\qquad \min_x\|Ax-b\|_2,\qquad A^+b=\sum_{\sigma_i>\tau}\frac{u_i^Tb}{\sigma_i}v_i\quad\text{(truncated)}.
$$

## 計算の流れ

Householder反射で列の下側を消すQRは、通常のGram–Schmidtより直交性を保ちやすい構成です。ランク診断には列ピボットやSVDを検討します。SVDは直交変換で二重対角へ落としてから処理する代表方式があり、正規方程式を明示的に作る必要はありません。

## 適用条件と落とし穴

2ノルムではκ₂(AᵀA)=κ₂(A)²となり、正規方程式は条件を悪化させます。小さい残差でも、悪条件やノイズがあれば係数は不確かです。ランクの閾値はスケール・丸め・観測誤差に応じて定め、単位の違う列のスケーリングも検討します。

## 検証するときに見る量

A−QR、QᵀQ−I、A−UΣVᵀの相対ノルム、最小二乗の正規性Aᵀ(Ax−b)を調べます。特異値が既知の行列とランク欠損例で、入力摂動に対する解の変化も比較します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- Alston S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://doi.org/10.1145/320941.320947
- G. H. Golub and C. Reinsch (1970). Singular value decomposition and least squares solutions. https://doi.org/10.1007/bf02163027
