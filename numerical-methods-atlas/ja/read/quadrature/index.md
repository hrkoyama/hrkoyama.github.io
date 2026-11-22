# Gauss求積・適応積分

Gauss求積は重みに適合する節点と重みを選び、少ない点数で多項式積分を正確にします。適応積分は区間ごとの誤差推定を使って評価点を配分する別の考え方です。

## 対象と代表式

正の重みw(x)に対するn点Gauss則は、条件が整えば次数2n−1以下の多項式に厳密です。直交多項式の三項漸化係数で作るJacobi行列Jの固有値が節点、正規化固有ベクトルvの第1成分の二乗とμ₀=∫wが求積重みになります。

$$
\int_a^b f(x)w(x)\,dx\approx\sum_{j=1}^n\omega_jf(x_j),\qquad Jv_j=x_jv_j,\quad\omega_j=\mu_0(v_j)_1^2.
$$

## 計算の流れ

Golub–Welsch法はこの対称三重対角固有値問題を解きます。適応Gauss–Kronrod型では入れ子の2つの則の差を局所誤差の指標にし、区間を分割して絶対/相対許容誤差と照合します。両者の差は厳密な誤差上界とは限りません。

## 適用条件と落とし穴

点特異性、不連続、高速振動、広い領域の細いピークでは、評価点が構造を見落とします。既知の不連続で区間を分け、必要なら変数変換や重み付き則を使います。積分値が0に近いと相対誤差だけの停止判定は不適切です。

## 検証するときに見る量

単項式の厳密積分で厳密次数を確認し、解析積分できる非多項式、特異点と細いピークでも試します。推定誤差と真の誤差、評価回数、分割上限到達の終了理由を分けて残します。

## 公開範囲

既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。

## 文献

- Gene H. Golub and John H. Welsch (1969). Calculation of Gauss quadrature rules. https://doi.org/10.1090/s0025-5718-69-99647-1
- Robert Piessens and Elise de Doncker-Kapenga and Christoph W. Überhuber and David K. Kahaner (1983). QUADPACK: A Subroutine Package for Automatic Integration. https://doi.org/10.1007/978-3-642-61786-7
