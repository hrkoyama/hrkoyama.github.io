# AMG・行列分解・固有値・求積

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [QR・SVD・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)
- [QR・SVD・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja>)
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-algorithm>)

  各行の最大非対角係数に対する相対強度からグラフを作り、貪欲な星型集約と余剰節点の隣接集約への付着で暫定補間Tを作ります。P=(I−ωD⁻¹A)T、ω=4/(3ρ̄)、ρ̄はD⁻¹Aの絶対行和上界です。粗演算子はPᵀAP。前後2回のJacobi平滑化と最終小行列の直接解を用います。これは採用した小規模SA変種であり、原著の全構築法や収束定理の再現ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja#qr-svd-factorization-ja-algorithm>)

  Householder反射を左から蓄積してRを上三角化し、Qを構成します。Jacobi SVDは列対の内積を小さくする直交回転を繰り返し、回転した列の長さを特異値とします。AᵀAを作って固有値を求める方法ではありません。最小二乗はQRの後退代入、階数落ちでは打切りSVDで求めます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja#krylov-eigenvalues-ja-algorithm>)

  Lanczosの3項漸化式に2回の全再直交化を加え、Arnoldiは修正Gram–Schmidtを2回行います。小さな射影行列T/HだけをNumPyのeigh/eigで解き、元空間へRitzベクトルを戻します。大きな元行列の密固有値計算は参照側だけで使います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja#gauss-adaptive-quadrature-ja-algorithm>)

  Golub–Welschで対称Jacobi行列の固有値を節点、最初の固有ベクトル成分の平方の2倍を重みとします。適応Simpsonは区間を二分し、|S左+S右−S全|/15を局所推定として公差を配分します。評価回数と深さの上限を持ち、未達を成功としません。

## 問題の図

- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png
- [行列から粗視化するAMG：残差と解誤差を分ける](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png
- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png

## 厳密解・参照解

- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#references-ja>)

  独立NumPy/SciPy参照、行列再構成・直交性・特異値・階数・最小二乗残差を確認します。PDEの参照解カードとは別の線形代数検証です。 別版では条件数、右辺摂動、数値階数の閾値を変え、残差と係数の前進誤差を分けます。LAPACKと実際の二進入力から作る高精度参照の役割を区別し、QR／SVD全般や任意の悪条件行列の保証にはしません。
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#references-ja>)

  独立固有値参照と、各Ritz値・固有対の残差、直交性と反復収束を確認します。 別版では固有値間隔・非正規性・Krylov次元を分け、小さな残差と真の固有値誤差を区別します。近接固有値の部分空間比較を、個別ベクトルの精度や他の物理モデルの検証と同一視しません。
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#references-ja>)

  多項式モーメントの既知積分値と独立求積参照を使い、厳密性・推定誤差・評価回数制限を確認します。 別版では求積点数・許容誤差と相殺の感度を比較し、真の積分誤差と内部の推定誤差を区別します。狭い山を見逃す対照も診断対象であり、診断の合格は積分推定の成功と同じではありません。
- [行列から粗視化するAMG：残差と解誤差を分ける：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-validation>)

  正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja#qr-svd-factorization-ja-validation>)

  QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja#krylov-eigenvalues-ja-validation>)

  ||Av−λv||₂、独立密行列固有値との差、基底の直交性を保存し、Krylov次元を増やした末尾の改善を確認します。非対称Ritz値の単調収束は仮定しません。恒等行列のhappy breakdown、零初期ベクトル拒否、次元予算不足も検査します。
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja#gauss-adaptive-quadrature-ja-validation>)

  全指定次数の多項式モーメント、SciPy roots_legendreの節点・重みとの差、解析exp積分の次数収束、解析atan積分とSciPy quadへの一致を測ります。公差を厳しくしたときの評価数と誤差を示し、5評価の強制予算切れ、非有限関数値も検査します。

## コード・検証

- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja>)
  availability: run

  実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。
- [QR/SVD：既定特異値・摂動増幅・数値階数](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja>)
  availability: run

  二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。
- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja>)
  availability: run

  32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。
- [Krylov固有値：クラスター部分空間と非正規感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja>)
  availability: run

  48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。
- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja>)
  availability: run

  Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。
- [求積：狭いピーク・相殺・端点・誤差推定の盲点](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja>)
  availability: run

  Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。
- [行列から粗視化するAMG：残差と解誤差を分ける](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja>)
  availability: run

  正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。
