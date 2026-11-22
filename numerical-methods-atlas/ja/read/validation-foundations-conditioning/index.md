# 基盤手法：条件数・残差・収束と独立参照

AMG、QR／SVD、Krylov固有値解法、求積を固定した条件系列で比較します。残差と前進誤差、行列と積分の条件の違いを測り、独立参照との一致だけでなく、収束の限界や診断の見落としも確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## AMGの条件数・異方性・残差と前進誤差

49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

**使用手法**

- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-algorithm)

MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![AMGの条件数・異方性・残差と前進誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-validation)

真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

正方格子から作るA=T⊗I+εI⊗T、n=7/15/31、ε=1/.1/.01です。これは既知解を持つ代数系の診断であり、連続PDEの精度検証は既存Poisson例に残します。同じnではκ₂はεによらず一定です。

**編集上の補足**

これは行列の代数的な条件と反復誤差の診断であり、旧Poisson製造解の連続PDE精度の確認とは別です。同じ格子の異方性と2ノルム条件数は一致する指標ではありません。残差、解誤差、反復予算切れを区別します。

### 採用した計算法

MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

### 比較・検証

真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。

### 確認の限界

固定した小規模な一定係数系列のみです。任意の係数ジャンプ、非構造格子、不定値系、最適計算量・一様収束を保証しません。異方性が常にκ₂を増やす、あるいは単調に収束を悪化させるとは主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_condition_2": 414.3450622319016,
    "maximum_actual_relative_residual": 9.213509371626832e-11,
    "maximum_actual_forward_error": 6.249776614864638e-11,
    "stress_budget_exhaustions": 0,
    "maximum_condition_gain_relative_error": 3.2097435820332976e-11
  },
  "checks": {
    "n7-eps1-true-residual": true,
    "n7-eps1-forward-bound": true,
    "n7-eps1-condition-gain": true,
    "n7-eps1-complexity": true,
    "n7-eps1-independent-dst": true,
    "n7-eps1-resolved": true,
    "n7-eps0.1-true-residual": true,
    "n7-eps0.1-forward-bound": true,
    "n7-eps0.1-condition-gain": true,
    "n7-eps0.1-complexity": true,
    "n7-eps0.1-independent-dst": true,
    "n7-eps0.1-stress-honest": true,
    "n7-eps0.01-true-residual": true,
    "n7-eps0.01-forward-bound": true,
    "n7-eps0.01-condition-gain": true,
    "n7-eps0.01-complexity": true,
    "n7-eps0.01-independent-dst": true,
    "n7-eps0.01-stress-honest": true,
    "n7-independent-spectrum": true,
    "n15-eps1-true-residual": true,
    "n15-eps1-forward-bound": true,
    "n15-eps1-condition-gain": true,
    "n15-eps1-complexity": true,
    "n15-eps1-independent-dst": true,
    "n15-eps1-resolved": true,
    "n15-eps0.1-true-residual": true,
    "n15-eps0.1-forward-bound": true,
    "n15-eps0.1-condition-gain": true,
    "n15-eps0.1-complexity": true,
    "n15-eps0.1-independent-dst": true,
    "n15-eps0.1-stress-honest": true,
    "n15-eps0.01-true-residual": true,
    "n15-eps0.01-forward-bound": true,
    "n15-eps0.01-condition-gain": true,
    "n15-eps0.01-complexity": true,
    "n15-eps0.01-independent-dst": true,
    "n15-eps0.01-stress-honest": true,
    "n15-independent-spectrum": true,
    "n31-eps1-true-residual": true,
    "n31-eps1-forward-bound": true,
    "n31-eps1-condition-gain": true,
    "n31-eps1-complexity": true,
    "n31-eps1-independent-dst": true,
    "n31-eps1-resolved": true,
    "n31-eps0.1-true-residual": true,
    "n31-eps0.1-forward-bound": true,
    "n31-eps0.1-condition-gain": true,
    "n31-eps0.1-complexity": true,
    "n31-eps0.1-independent-dst": true,
    "n31-eps0.1-stress-honest": true,
    "n31-eps0.01-true-residual": true,
    "n31-eps0.01-forward-bound": true,
    "n31-eps0.01-condition-gain": true,
    "n31-eps0.01-complexity": true,
    "n31-eps0.01-independent-dst": true,
    "n31-eps0.01-stress-honest": true,
    "n31-independent-spectrum": true,
    "short-budget-failure-explicit": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://ww3.math.ucla.edu/camreport/cam99-29.pdf; review_level=author-hosted original preprint abstract and opening text via official university search extraction
  弱近似性等の仮定に基づく理論と、教材の限られた行列系列での観測を区別します。任意異方性への頑健性は主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## QR/SVD：既定特異値・摂動増幅・数値階数

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

**使用手法**

- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja) (`qr-svd`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-algorithm)

Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![QR/SVD：既定特異値・摂動増幅・数値階数：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) (`matrix-factorization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-validation)

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

Hadamard直交因子U,Vとsⱼ=2⁻qj、q=0/4/8/12を使います。b=u₀とb+2⁻⁴⁰u_minを固定し、摂動増幅を測ります。q=0の重複特異値では個々の特異ベクトルは一意ではありません。

**編集上の補足**

再構成・直交性・後退誤差が小さくても、悪条件問題の前進誤差は大きくなり得ます。入力した浮動小数点行列と理想的に指定した特異値を区別し、数値階数の閾値も明記します。

### 採用した計算法

Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

### 比較・検証

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

### 確認の限界

LAPACKと教材の射影コアには共通の数値基盤が含まれます。mpmath SVDは別実装の二重対角化とQR反復、mpmath最小二乗は同じHouseholder群の別高精度実装です。どの高条件数行列にも微小特異値の相対高精度を保証するものではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "largest_condition_2": 68719476736.0,
    "maximum_backward_reconstruction": 6.074604146362075e-16,
    "maximum_forward_error": 0.0004920953373835635,
    "minimum_numerical_rank": 2,
    "reference_precision_digits": 120
  },
  "checks": {
    "q0-factorization": true,
    "q0-high-precision-spectrum": true,
    "q0-condition-aware-forward": true,
    "q0-lapack-reference": true,
    "q0-perturbation-gain": true,
    "q4-factorization": true,
    "q4-high-precision-spectrum": true,
    "q4-condition-aware-forward": true,
    "q4-lapack-reference": true,
    "q4-perturbation-gain": true,
    "q8-factorization": true,
    "q8-high-precision-spectrum": true,
    "q8-condition-aware-forward": true,
    "q8-lapack-reference": true,
    "q8-perturbation-gain": true,
    "q12-factorization": true,
    "q12-high-precision-spectrum": true,
    "q12-condition-aware-forward": true,
    "q12-lapack-reference": true,
    "q12-perturbation-gain": true,
    "cutoff1e-08-rank-aware": true,
    "cutoff1e-12-rank-aware": true,
    "cutoff1e-14-rank-aware": true,
    "exact-rank-deficiency": true,
    "sweep-budget-failure-explicit": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel, K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=primary publisher abstract and bibliographic metadata
  適切な停止規準と行列の成分ごとの条件に依存する相対精度の主張を確認しました。一般の高条件数行列における微小特異値の万能な相対精度とはしません。
- LAPACK authors (1999). Further Details: Error Bounds for Linear Least Squares Problems. https://netlib.org/lapack/lug/node83.html; review_level=official implementation documentation, error-analysis and numerical-rank sections
  小さな後退誤差と前進誤差を区別し、最小二乗では条件数だけでなく残差の角度にも依存すること、RCONDによる切捨ては数値階数の規約であることを確認しました。
- mpmath developers (2023). mpmath 1.3.0 matrix documentation and installed implementation. https://mpmath.org/doc/1.3.0/matrices.html; review_level=official matrix documentation and selected installed mpmath1.3.0 source (svd_r_raw, qr_solve), plus actual 80/120dps fixed-input execution
  SVDはHouseholder二重対角化とQR反復、最小二乗は別実装の高精度Householder QRです。後者は教材のQRと同じ数理的手法群であり、別の手法群とは呼びません。実際の二進浮動小数点入力を整数比で読み込み、生成専用環境で実行しました。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Krylov固有値：クラスター部分空間と非正規感度

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-algorithm)

全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Krylov固有値：クラスター部分空間と非正規感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja#krylov-eigen-conditioning-ja-validation)

解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

対称行列の上位2固有値の間隔は1/.1/.01です。非正規行列は実浮動小数点の上三角行列でK=10/1000とし、対角が既知固有値です。浮動小数点の相似変換後に名目スペクトルを厳密真値とは呼びません。

**編集上の補足**

固有対残差、固有値・不変部分空間の誤差、スペクトルの間隔と非正規性を区別します。構成した感度対照を実際のKrylov反復の出力や万能な失敗例と同一視しません。

### 採用した計算法

全再直交化Lanczosと2回MGSのArnoldiで縮約し、小さい射影行列だけを密に解きます。上位2ベクトルはQRで張る空間へ変換し、符号や回転に不変な射影行列差を測ります。

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

### 比較・検証

解析的対角固有値とSciPy密固有値、左右固有ベクトルによる条件数を照合します。別に構成した2×2擬固有対ではK=1000で残差約2.5×10⁻⁸に対し固有値誤差.005を示します。これは反復法が出力した失敗例ではなく、残差だけでは保証できないことを示す感度対照です。

### 確認の限界

NumPyの射影コアとSciPyの密参照はLAPACK基盤を共有し得るため、全面的に独立なバックエンドとはしません。解析固有値と独立構成対照を併用します。再始動、内部固有値、大規模疎行列、普遍的な単調収束は対象外です。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_basis_orthogonality": 6.813979303412138e-16,
    "largest_eigenvalue_condition": 100000.00000500213,
    "constructed_small_residual": 2.4999999999688053e-08,
    "constructed_forward_error": 0.004999999999999893
  },
  "checks": {
    "gap1-analytic-spectrum": true,
    "gap1-resolved": true,
    "gap1-basis": true,
    "gap0.1-analytic-spectrum": true,
    "gap0.1-resolved": true,
    "gap0.1-basis": true,
    "gap0.01-analytic-spectrum": true,
    "gap0.01-resolved": true,
    "gap0.01-basis": true,
    "K10-condition": true,
    "K10-analytic-spectrum": true,
    "K10-resolved": true,
    "K10-basis": true,
    "K1000-condition": true,
    "K1000-analytic-spectrum": true,
    "K1000-resolved": true,
    "K1000-basis": true,
    "pseudoK1-literal-formula": true,
    "pseudoK10-literal-formula": true,
    "pseudoK1000-literal-formula": true,
    "small-residual-does-not-certify-forward-error": true,
    "short-dimension-has-residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html; review_level=official implementation documentation, error-bound overview and cluster/invariant-subspace distinction
  非正規行列では小さな固有対残差と前進固有値誤差を同一視しません。固有値感度、個別固有ベクトル、固有値クラスターの不変部分空間を区別します。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 求積：狭いピーク・相殺・端点・誤差推定の盲点

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-algorithm)

Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![求積：狭いピーク・相殺・端点・誤差推定の盲点：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-validation)

roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

区間[0,1]、Gauss次数8/16/32/64/128、公差10⁻⁵/10⁻⁷/10⁻⁹です。Lorentz幅.1/.03/.01、相殺係数0/2¹²/2²⁴/2³⁶を固定します。零積分の相対条件数は未定義としてnullで保存します。

**編集上の補足**

適応推定値や計算間の一致は任意の被積分関数の厳密誤差上界ではありません。相殺時の絶対誤差と相対誤差、未検出の局所構造、評価予算を分けて記録します。

### 採用した計算法

Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

### 比較・検証

roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

### 確認の限界

Simpsonの推定値は厳密誤差上界ではありません。盲点の検出に合格しても積分精度への合格ではありません。平方根の直接積分は深さ予算で未収束と表示し得ます。任意の振動・特異性の完全な探索や認証付き求積は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_cancellation_condition": 68719476737.0,
    "blind_bump_actual_error": 0.008126984126984127,
    "blind_bump_reported_error": 0.0,
    "resolved_bump_actual_error": 1.0884418366607918e-12,
    "zero_integral_relative_condition": null
  },
  "checks": {
    "width0.1-reference": true,
    "n8-independent-rule": true,
    "n16-independent-rule": true,
    "n32-independent-rule": true,
    "n64-independent-rule": true,
    "n128-independent-rule": true,
    "width0.1-gauss-refinement": true,
    "width0.1-tol1e-05": true,
    "width0.1-tol1e-07": true,
    "width0.1-tol1e-09": true,
    "width0.03-reference": true,
    "width0.03-gauss-refinement": true,
    "width0.03-tol1e-05": true,
    "width0.03-tol1e-07": true,
    "width0.03-tol1e-09": true,
    "width0.01-reference": true,
    "width0.01-gauss-refinement": true,
    "width0.01-tol1e-05": true,
    "width0.01-tol1e-07": true,
    "width0.01-tol1e-09": true,
    "endpoint-tol1e-05": true,
    "endpoint-tol1e-07": true,
    "endpoint-tol1e-09": true,
    "C0-absolute-error": true,
    "C4096-absolute-error": true,
    "C1.67772e+07-absolute-error": true,
    "C6.87195e+10-absolute-error": true,
    "conditioned-input-perturbation-gain": true,
    "zero-integral-relative-condition-undefined": true,
    "heuristic-blind-spot-explicit": true,
    "known-support-companion-resolves": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://arxiv.org/abs/1006.3962; review_level=primary author paper, abstract and selected introduction/error-estimation text (§3)
  二つの近似積分値の差が偶然小さい場合の誤差推定失敗を原文の選択節で確認しました。今回のSimpson対照は教材独自の構成であり、同論文の新積分器を実装したとは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
