# AMG・行列分解・固有値・求積

小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 行列から粗視化するAMG：残差と解誤差を分ける

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

### 前提・単位・境界

無次元の単位正方形、一定正係数の−Δu=f、全周同次Dirichlet境界、5点差分です。階層構築には座標・格子幅・nを渡さず、係数行列と暗黙の定数近似核だけを使います。入力は実対称正定値を前提とし、任意の不定値行列を扱うソルバーではありません。

### 採用した計算法

各行の最大非対角係数に対する相対強度からグラフを作り、貪欲な星型集約と余剰節点の隣接集約への付着で暫定補間Tを作ります。P=(I−ωD⁻¹A)T、ω=4/(3ρ̄)、ρ̄はD⁻¹Aの絶対行和上界です。粗演算子はPᵀAP。前後2回のJacobi平滑化と最終小行列の直接解を用います。これは採用した小規模SA変種であり、原著の全構築法や収束定理の再現ではありません。

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

### 比較・検証

正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。

### 確認の限界

3格子の固定スカラー問題だけの確認です。係数の大きな不連続、強い異方性、弾性系、任意の非構造格子、最適計算量・格子独立収束を保証しません。小さい残差だけを小さい解誤差の証明としません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_relative_residual": 7.1395963390776e-11,
    "max_direct_solution_error": 2.0283080847857227e-11,
    "minimum_pde_order": 2.0020872697597354,
    "max_operator_complexity": 3.196752830591754
  },
  "checks": {
    "all_residual_targets": true,
    "independent_sparse_direct": true,
    "second_order_pde_refinement": true,
    "bounded_operator_complexity": true,
    "cycle_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Householder QRと片側Jacobi SVD：直交性・階数・最小二乗

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

### 前提・単位・境界

m≥nの小さな実行列が対象です。SVDの数値階数は最大特異値に対する相対しきい値10⁻¹²で定義し、零特異値方向を除くcompact因子を返します。QRは列ピボットなしで、階数判定には用いません。

### 採用した計算法

Householder反射を左から蓄積してRを上三角化し、Qを構成します。Jacobi SVDは列対の内積を小さくする直交回転を繰り返し、回転した列の長さを特異値とします。AᵀAを作って固有値を求める方法ではありません。最小二乗はQRの後退代入、階数落ちでは打切りSVDで求めます。

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

### 比較・検証

QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。

### 確認の限界

完全なLAPACK置換、複素行列、横長行列、任意の極端なスケール、最適な相対特異値精度を保証しません。10⁻¹²未満の特異値は入力した数値階数の規約で打ち切るため、数学的な厳密階数と区別します。Demmel–Veselićの精度定理の全条件を実証したとは主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_qr_reconstruction": 9.197631573723943e-16,
    "max_svd_reconstruction": 1.0519095898403626e-13,
    "max_singular_value_error": 3.399227299681105e-16,
    "max_least_squares_error": 9.164127590036862e-15,
    "max_orthogonality": 1.310421197476067e-15
  },
  "checks": {
    "all_jacobi_converged_and_ranks_match": true,
    "householder_reconstruction": true,
    "householder_orthogonality": true,
    "jacobi_reconstruction": true,
    "jacobi_orthogonality": true,
    "independent_lapack_singular_values": true,
    "independent_minimum_norm_least_squares": true,
    "qr_least_squares": true,
    "least_squares_stationarity": true,
    "sweep_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel and K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Lanczos・Arnoldi：Ritz値と固有対残差の収束

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

### 前提・単位・境界

対称問題では実対称行列、非対称問題では既知の分離した最大固有値5を持つ実行列を使います。初期ベクトルは固定seedです。非対称Ritz値は複素数を許し、最大実部で選びます。

### 採用した計算法

Lanczosの3項漸化式に2回の全再直交化を加え、Arnoldiは修正Gram–Schmidtを2回行います。小さな射影行列T/HだけをNumPyのeigh/eigで解き、元空間へRitzベクトルを戻します。大きな元行列の密固有値計算は参照側だけで使います。

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

### 比較・検証

||Av−λv||₂、独立密行列固有値との差、基底の直交性を保存し、Krylov次元を増やした末尾の改善を確認します。非対称Ritz値の単調収束は仮定しません。恒等行列のhappy breakdown、零初期ベクトル拒否、次元予算不足も検査します。

### 確認の限界

非再始動・小行列・分離した極端固有対の教材です。内部固有値、クラスタ、巨大な疎行列、強い非正規性、shift-invertやimplicitly restarted Arnoldiは対象外です。小さな固有対残差だけで非正規行列の固有値誤差の厳密上界とはしません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_final_eigenpair_residual": 1.4394924647739691e-12,
    "max_basis_orthogonality": 4.911536314397836e-16
  },
  "checks": {
    "independent_dense_eigenvalues_and_residuals": true,
    "krylov_basis_orthogonality": true,
    "dimension_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

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

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

### 前提・単位・境界

有限区間上の滑らかな実関数、無次元の積分です。固定Gauss次数2・4・8・16と、適応絶対公差10⁻⁵・10⁻⁷・10⁻⁹を別々に走査します。両端特異点・不連続・無限区間は今回の入力では扱いません。

### 採用した計算法

Golub–Welschで対称Jacobi行列の固有値を節点、最初の固有ベクトル成分の平方の2倍を重みとします。適応Simpsonは区間を二分し、|S左+S右−S全|/15を局所推定として公差を配分します。評価回数と深さの上限を持ち、未達を成功としません。

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

### 比較・検証

全指定次数の多項式モーメント、SciPy roots_legendreの節点・重みとの差、解析exp積分の次数収束、解析atan積分とSciPy quadへの一致を測ります。公差を厳しくしたときの評価数と誤差を示し、5評価の強制予算切れ、非有限関数値も検査します。

### 確認の限界

Simpsonの局所推定は任意の関数に対する厳密な誤差上界ではありません。高周波の見落とし、特異点、丸め誤差の停滞を一般に解決する実装ではなく、Gauss–KronrodやQUADPACK全体の再実装でもありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_polynomial_moment_error": 8.881784197001252e-16,
    "max_scipy_rule_error": 1.2490009027033011e-15,
    "gauss_final_exp_error": 0.0,
    "max_adaptive_error_over_tolerance": 0.01729971494390803,
    "budget_failure_evaluations": 5
  },
  "checks": {
    "gauss_polynomial_moments": true,
    "independent_scipy_gauss_rule": true,
    "gauss_nonsingular_refinement": true,
    "adaptive_exact_and_quad_references": true,
    "evaluation_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
