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

積分が相殺で小さくなるときは、∫|f|/|∫f|のような相殺条件数も有用です。絶対誤差・相対誤差と、積分則内部の誤差推定値は別の量です。有限個の評価点が狭い山をすべて見逃す対照では、二つの近似の差が小さくても真の積分誤差が大きくなり得ます。 条件数を比べるときは入力摂動のノルムと摂動モデルを明示し、積分値が0なら相対条件数・相対誤差を未定義として絶対量で評価します。

## 検証するときに見る量

単項式の厳密積分で厳密次数を確認し、解析積分できる非多項式、特異点と細いピークでも試します。推定誤差と真の誤差、評価回数、分割上限到達の終了理由を分けて残します。

追加版では求積点数・許容誤差を変え、既知の積分値を持つ滑らかな関数、相殺を伴う関数、固定した狭い山の対照を独立参照と比較します。真の誤差、推定誤差、関数評価回数を分けて記録します。狭い山を明示的に分割して捉える計算と見逃す診断対照を区別し、全ての被積分関数への誤差保証とはしません。 端点で導関数が特異になる例は変数変換の前後を比較し、評価回数や再帰深さの上限への到達も終了状態として残します。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ

固定標的の計算例

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

Simpsonの局所推定は任意の関数に対する厳密な誤差上界ではありません。高周波の見落とし、特異点、丸め誤差の停滞を一般に解決する実装ではなく、Gauss–KronrodやQUADPACK全体の再実装でもありません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations/#gauss-adaptive-quadrature) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [テスト test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations/verification.json)

### 求積：狭いピーク・相殺・端点・誤差推定の盲点

固定標的の計算例

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

Simpsonの推定値は厳密誤差上界ではありません。盲点の検出に合格しても積分精度への合格ではありません。平方根の直接積分は深さ予算で未収束と表示し得ます。任意の振動・特異性の完全な探索や認証付き求積は主張しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations-conditioning/#quadrature-conditioning) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [コード fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [コード mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [テスト test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## 公開範囲

旧版の入力・測定値・公差を保持し、条件数・残差・収束の追加検証を別の配布版として案内します。診断対照の合格は、その対照で意図した限界を確認した意味を含み、一般的な成功や原論文全体の再現を意味しません。

## 文献

- Gene H. Golub and John H. Welsch (1969). Calculation of Gauss quadrature rules. https://doi.org/10.1090/s0025-5718-69-99647-1
- Robert Piessens and Elise de Doncker-Kapenga and Christoph W. Überhuber and David K. Kahaner (1983). QUADPACK: A Subroutine Package for Automatic Integration. https://doi.org/10.1007/978-3-642-61786-7
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://doi.org/10.1145/1824801.1824804
