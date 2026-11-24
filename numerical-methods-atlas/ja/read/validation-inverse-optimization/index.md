# Bratu逆問題の最適化・雑音・正則化

既存の合成観測を保持し、小さな固定例でGN/LM・準Newton・正則化選択を比較します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## GN・LMと有界最小二乗のBratu比較

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-algorithm)

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。


**問題の図**

![GN・LMと有界最小二乗のBratu比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-validation)

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

- [Bratu逆最小二乗の独立Thomas局所参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja) (`bratu-gn-lm-bounds`; 同じ問題の参照 · 有限格子の数値参照)

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。
### 前提・単位・境界

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。

**編集上の補足**

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

### 採用した計算法

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

### 比較・検証

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

### 確認の限界

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 17,
    "completed_fits": 17,
    "expected_fits": 17,
    "forward_evaluations": 234,
    "maximum_stationarity_inf": 9.69771818404297e-10,
    "reference_scope": "independent Thomas state/Jacobian; shared local TRF optimizer; no global optimum proof"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-objective-reference": true,
    "fit-0-data-rank": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-objective-reference": true,
    "fit-1-data-rank": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-objective-reference": true,
    "fit-2-data-rank": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-objective-reference": true,
    "fit-3-data-rank": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-objective-reference": true,
    "fit-4-data-rank": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-objective-reference": true,
    "fit-5-data-rank": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-objective-reference": true,
    "fit-6-data-rank": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-objective-reference": true,
    "fit-7-data-rank": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-objective-reference": true,
    "fit-8-data-rank": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-objective-reference": true,
    "fit-9-data-rank": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-objective-reference": true,
    "fit-10-data-rank": true,
    "fit-10-feasible": true,
    "fit-10-active-constraint": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-objective-reference": true,
    "fit-11-data-rank": true,
    "fit-11-feasible": true,
    "fit-11-active-constraint": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-objective-reference": true,
    "fit-12-data-rank": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-objective-reference": true,
    "fit-13-data-rank": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-objective-reference": true,
    "fit-14-data-rank": true,
    "fit-14-feasible": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-objective-reference": true,
    "fit-15-data-rank": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-objective-reference": true,
    "fit-16-data-rank": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/index.json

![保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 既知最小点でのBFGSと3組L-BFGS

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-algorithm)

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

- [有限次元代数最適化と既知最小点](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja) (`finite-dimensional-optimization`)

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。


**問題の図**

![既知最小点でのBFGSと3組L-BFGS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-validation)

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

- [既知最小点と現在の有限記憶作用に対する解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja) (`bfgs-lbfgs-controls`; 同じ問題の参照 · 解析参照)

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。
### 前提・単位・境界

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。

**編集上の補足**

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

### 採用した計算法

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

### 比較・検証

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

### 確認の限界

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。

### 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 16,
    "completed_fits": 16,
    "expected_fits": 16,
    "objective_evaluations": 722,
    "maximum_gradient_inf": 9.090384658211326e-08,
    "independent_target": "known analytic minima; current-scaling retained-pair dense action"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-point": true,
    "fit-0-gradient": true,
    "fit-0-strong-wolfe": true,
    "fit-0-resolved-curvature": true,
    "fit-0-inverse-symmetry": true,
    "fit-0-inverse-spd": true,
    "fit-1-complete": true,
    "fit-1-point": true,
    "fit-1-gradient": true,
    "fit-1-strong-wolfe": true,
    "fit-1-resolved-curvature": true,
    "fit-1-retained-dense-oracle": true,
    "fit-2-complete": true,
    "fit-2-point": true,
    "fit-2-gradient": true,
    "fit-3-complete": true,
    "fit-3-point": true,
    "fit-3-gradient": true,
    "fit-4-complete": true,
    "fit-4-point": true,
    "fit-4-gradient": true,
    "fit-4-objective": true,
    "fit-4-strong-wolfe": true,
    "fit-4-resolved-curvature": true,
    "fit-4-inverse-symmetry": true,
    "fit-4-inverse-spd": true,
    "fit-5-complete": true,
    "fit-5-point": true,
    "fit-5-gradient": true,
    "fit-5-objective": true,
    "fit-5-strong-wolfe": true,
    "fit-5-resolved-curvature": true,
    "fit-5-retained-dense-oracle": true,
    "fit-6-complete": true,
    "fit-6-point": true,
    "fit-6-gradient": true,
    "fit-6-objective": true,
    "fit-7-complete": true,
    "fit-7-point": true,
    "fit-7-gradient": true,
    "fit-7-objective": true,
    "fit-8-complete": true,
    "fit-8-point": true,
    "fit-8-gradient": true,
    "fit-8-objective": true,
    "fit-8-strong-wolfe": true,
    "fit-8-resolved-curvature": true,
    "fit-8-inverse-symmetry": true,
    "fit-8-inverse-spd": true,
    "fit-9-complete": true,
    "fit-9-point": true,
    "fit-9-gradient": true,
    "fit-9-objective": true,
    "fit-9-strong-wolfe": true,
    "fit-9-resolved-curvature": true,
    "fit-9-retained-dense-oracle": true,
    "fit-10-complete": true,
    "fit-10-point": true,
    "fit-10-gradient": true,
    "fit-10-objective": true,
    "fit-11-complete": true,
    "fit-11-point": true,
    "fit-11-gradient": true,
    "fit-11-objective": true,
    "fit-12-complete": true,
    "fit-12-point": true,
    "fit-12-gradient": true,
    "fit-12-objective": true,
    "fit-12-strong-wolfe": true,
    "fit-12-resolved-curvature": true,
    "fit-12-inverse-symmetry": true,
    "fit-12-inverse-spd": true,
    "fit-13-complete": true,
    "fit-13-point": true,
    "fit-13-gradient": true,
    "fit-13-objective": true,
    "fit-13-strong-wolfe": true,
    "fit-13-resolved-curvature": true,
    "fit-13-retained-dense-oracle": true,
    "fit-14-complete": true,
    "fit-14-point": true,
    "fit-14-gradient": true,
    "fit-14-objective": true,
    "fit-15-complete": true,
    "fit-15-point": true,
    "fit-15-gradient": true,
    "fit-15-objective": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/index.json

![実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- On the limited memory BFGS method for large scale optimization [accessed 2026-11-24]. https://users.iems.northwestern.edu/~nocedal/PDFfiles/limited-memory.pdf; review_level=selected-primary-scope
Author-hosted PDF selected physical pages 3–5 (printed 2–4), rendered locally and visually inspected: limited storage, deletion of oldest correction, Eq. (2.1) inverse-BFGS, Algorithm 2.1 and Eq. (2.6) retained-update construction. No full-paper/proof/experiment or Section 4 scaling review. The selected original uses weak Wolfe; this study deliberately uses a separately specified strong-Wolfe line search. Current-gamma least-squares scaling is independently derived here, not attributed to unread text.

- SciPy 1.14.1 line_search documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.line_search.html; review_level=selected-primary-scope
Signature, c1/c2, descent-direction requirement, returned failure None and evaluation counts. Cited textbook pages were not read.

- SciPy 1.14.1 BFGS documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-bfgs.html; review_level=selected-primary-scope
Options gtol, norm, c1/c2, hess_inv0 and precision-loss notes; no claim of reading a BFGS original paper.

- SciPy 1.14.1 L-BFGS-B documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-lbfgsb.html; review_level=selected-primary-scope
Options maxcor, ftol, gtol/projected-gradient convention, maxfun, maxiter and maxls.

- A new approach to variable metric algorithms. https://academic.oup.com/comjnl/article-abstract/13/3/317/345520?login=false; review_level=bibliography-only-original-unread
Prior saved publisher metadata/abstract-search record only. Original article full text remains unavailable/unread; no new request was made and no derivation is claimed to have been checked against it.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 雑音・モデル差と有限γ経路の正則化

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-algorithm)

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。


**問題の図**

![雑音・モデル差と有限γ経路の正則化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-validation)

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

- [有限γ経路と局所線形雑音伝播のBratu参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja) (`bratu-noise-regularization`; 同じ問題の参照 · 有限格子の数値参照)

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。
### 前提・単位・境界

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。

**編集上の補足**

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

### 採用した計算法

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

### 比較・検証

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

### 確認の限界

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

### 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 42,
    "completed_fits": 42,
    "expected_fits": 42,
    "independent_base_noise_vectors": 2,
    "coupled_gamma_paths": 8,
    "forward_evaluations": 339,
    "maximum_stationarity_inf": 2.8491609072034407e-10,
    "covariance_scope": "fixed-gamma Gauss–Newton local-linear-model plug-in; no selection-event covariance or coverage claim",
    "detailed_fit_records": "case67-all-fits.json"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-feasible": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-feasible": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-feasible": true,
    "path-0-complete": true,
    "path-0-selection": true,
    "path-0-covariance-eligibility-and-psd": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-feasible": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-feasible": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-feasible": true,
    "path-1-complete": true,
    "path-1-selection": true,
    "path-1-covariance-eligibility-and-psd": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-feasible": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-feasible": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-feasible": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-feasible": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-feasible": true,
    "path-2-complete": true,
    "path-2-selection": true,
    "path-2-covariance-eligibility-and-psd": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-feasible": true,
    "fit-17-complete": true,
    "fit-17-final-forward-residual": true,
    "fit-17-stationary": true,
    "fit-17-feasible": true,
    "fit-18-complete": true,
    "fit-18-final-forward-residual": true,
    "fit-18-stationary": true,
    "fit-18-feasible": true,
    "fit-19-complete": true,
    "fit-19-final-forward-residual": true,
    "fit-19-stationary": true,
    "fit-19-feasible": true,
    "path-3-complete": true,
    "path-3-selection": true,
    "path-3-covariance-eligibility-and-psd": true,
    "fit-20-complete": true,
    "fit-20-final-forward-residual": true,
    "fit-20-stationary": true,
    "fit-20-feasible": true,
    "fit-21-complete": true,
    "fit-21-final-forward-residual": true,
    "fit-21-stationary": true,
    "fit-21-feasible": true,
    "fit-22-complete": true,
    "fit-22-final-forward-residual": true,
    "fit-22-stationary": true,
    "fit-22-feasible": true,
    "fit-23-complete": true,
    "fit-23-final-forward-residual": true,
    "fit-23-stationary": true,
    "fit-23-feasible": true,
    "fit-24-complete": true,
    "fit-24-final-forward-residual": true,
    "fit-24-stationary": true,
    "fit-24-feasible": true,
    "path-4-complete": true,
    "path-4-selection": true,
    "path-4-covariance-eligibility-and-psd": true,
    "fit-25-complete": true,
    "fit-25-final-forward-residual": true,
    "fit-25-stationary": true,
    "fit-25-feasible": true,
    "fit-26-complete": true,
    "fit-26-final-forward-residual": true,
    "fit-26-stationary": true,
    "fit-26-feasible": true,
    "fit-27-complete": true,
    "fit-27-final-forward-residual": true,
    "fit-27-stationary": true,
    "fit-27-feasible": true,
    "fit-28-complete": true,
    "fit-28-final-forward-residual": true,
    "fit-28-stationary": true,
    "fit-28-feasible": true,
    "fit-29-complete": true,
    "fit-29-final-forward-residual": true,
    "fit-29-stationary": true,
    "fit-29-feasible": true,
    "path-5-complete": true,
    "path-5-selection": true,
    "path-5-covariance-eligibility-and-psd": true,
    "fit-30-complete": true,
    "fit-30-final-forward-residual": true,
    "fit-30-stationary": true,
    "fit-30-feasible": true,
    "fit-31-complete": true,
    "fit-31-final-forward-residual": true,
    "fit-31-stationary": true,
    "fit-31-feasible": true,
    "fit-32-complete": true,
    "fit-32-final-forward-residual": true,
    "fit-32-stationary": true,
    "fit-32-feasible": true,
    "fit-33-complete": true,
    "fit-33-final-forward-residual": true,
    "fit-33-stationary": true,
    "fit-33-feasible": true,
    "fit-34-complete": true,
    "fit-34-final-forward-residual": true,
    "fit-34-stationary": true,
    "fit-34-feasible": true,
    "path-6-complete": true,
    "path-6-selection": true,
    "path-6-covariance-eligibility-and-psd": true,
    "fit-35-complete": true,
    "fit-35-final-forward-residual": true,
    "fit-35-stationary": true,
    "fit-35-feasible": true,
    "fit-36-complete": true,
    "fit-36-final-forward-residual": true,
    "fit-36-stationary": true,
    "fit-36-feasible": true,
    "fit-37-complete": true,
    "fit-37-final-forward-residual": true,
    "fit-37-stationary": true,
    "fit-37-feasible": true,
    "fit-38-complete": true,
    "fit-38-final-forward-residual": true,
    "fit-38-stationary": true,
    "fit-38-feasible": true,
    "fit-39-complete": true,
    "fit-39-final-forward-residual": true,
    "fit-39-stationary": true,
    "fit-39-feasible": true,
    "path-7-complete": true,
    "path-7-selection": true,
    "path-7-covariance-eligibility-and-psd": true,
    "fit-40-complete": true,
    "fit-40-final-forward-residual": true,
    "fit-40-stationary": true,
    "fit-40-feasible": true,
    "fit-41-complete": true,
    "fit-41-final-forward-residual": true,
    "fit-41-stationary": true,
    "fit-41-feasible": true,
    "linear-control-covariance": true,
    "linear-control-bias": true,
    "linear-control-data-shift": true,
    "linear-control-symmetry": true,
    "linear-control-psd": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/index.json

![保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Regularization Tools, Version 4.1 for Matlab 7.3 [accessed 2026-11-24]. https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf; review_level=selected-primary-scope
Official author manual: selected text around Section 2.5 and Section 2.9; physical pages 20 and 37 (printed 18 and 35) rendered locally and visually inspected. L-curve residual/solution norm tradeoff and discrepancy equation (2.61) were read. Four-point chord curvature here is a finite-list diagnostic, not the manual spline/corner algorithm, a theorem of optimal regularization or coverage. Original software (1994) and later article (2007) are separate bibliographic works and were not read.

- SciPy 1.14.1 curve_fit documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.curve_fit.html; review_level=selected-primary-scope
sigma/absolute_sigma and covariance interpretation sections. The penalized sandwich covariance in this study is derived independently; it is not presented as curve_fit output.

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
