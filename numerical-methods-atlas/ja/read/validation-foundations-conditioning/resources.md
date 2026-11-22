# 基盤手法：条件数・残差・収束と独立参照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations-conditioning/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)
- [QR・SVD・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja>)
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-algorithm>)

  MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-algorithm>)

  Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-algorithm>)

  全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-algorithm>)

  Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

## 問題の図

- [AMGの条件数・異方性・残差と前進誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png
- [QR/SVD：既定特異値・摂動増幅・数値階数](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png
- [Krylov固有値：クラスター部分空間と非正規感度](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png
- [求積：狭いピーク・相殺・端点・誤差推定の盲点](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png

## 厳密解・参照解

- [AMGの条件数・異方性・残差と前進誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-validation>)

  真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。
- [QR/SVD：既定特異値・摂動増幅・数値階数：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-validation>)

  再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。
- [Krylov固有値：クラスター部分空間と非正規感度：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-validation>)

  解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。
- [求積：狭いピーク・相殺・端点・誤差推定の盲点：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-validation>)

  roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

## コード・検証

- [AMGの条件数・異方性・残差と前進誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja>)
  availability: run

  49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。
- [QR/SVD：既定特異値・摂動増幅・数値階数](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja>)
  availability: run

  二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。
- [Krylov固有値：クラスター部分空間と非正規感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja>)
  availability: run

  48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。
- [求積：狭いピーク・相殺・端点・誤差推定の盲点](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja>)
  availability: run

  Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。
