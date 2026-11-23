# 重力軌道：Keplerと軟化有限粒子

厳密なKepler軌道と、同じ軟化核を使う短時間の有限粒子ODE参照を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 無軟化Kepler二体の時間誤差

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-algorithm)

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。


**問題の図**

![無軟化Kepler二体の時間誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-validation)

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照 · 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。
### 前提・単位・境界

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。

**編集上の補足**

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

### 採用した計算法

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

### 比較・検証

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

### 確認の限界

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_position_error": 0.0016120499258598436,
    "finest_energy_drift": 0.00017450491925918854,
    "period": 6.283185307179586
  },
  "checks": {
    "s128 finite synchronized fields": true,
    "s128 fixed final time": true,
    "s128 positive pair separation": true,
    "s128 momentum_drift": true,
    "s128 angular_drift": true,
    "s128 com_drift": true,
    "s128 Kepler root residual": true,
    "s128 independent final pair force": true,
    "s256 finite synchronized fields": true,
    "s256 fixed final time": true,
    "s256 positive pair separation": true,
    "s256 momentum_drift": true,
    "s256 angular_drift": true,
    "s256 com_drift": true,
    "s256 Kepler root residual": true,
    "s256 independent final pair force": true,
    "s512 finite synchronized fields": true,
    "s512 fixed final time": true,
    "s512 positive pair separation": true,
    "s512 momentum_drift": true,
    "s512 angular_drift": true,
    "s512 com_drift": true,
    "s512 Kepler root residual": true,
    "s512 independent final pair force": true,
    "analytic reference energy identity": true,
    "analytic reference angular identity": true,
    "analytic reference COM identity": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest Kepler position": true,
    "finest Kepler energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/index.json

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

固定入力を実際に計算した保存配列からの検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- JPL Keplerian-element formulas. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=official-selected-kepler-equation
Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 冷たいPlummer密度由来32粒子の短時間力学

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)
- [Barnes–Hut八分木](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja) (`barnes-hut`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-algorithm)

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。


**問題の図**

![冷たいPlummer密度由来32粒子の短時間力学：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-validation)

非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja) (`gravity-plummer-short`; 同じ問題の参照 · 有限格子の数値参照)

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。
### 前提・単位・境界

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。

**編集上の補足**

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

### 採用した計算法

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

### 比較・検証

非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。

### 確認の限界

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_tolerance_gap": 1.3339329640871256e-12,
    "finest_direct_error": 8.032388866139367e-09,
    "finest_energy_drift": 8.566574106443163e-09,
    "theta035_trajectory": 5.672453506265489e-07,
    "asymmetric_net_force": 2.3712429943822043e-05
  },
  "checks": {
    "independent ODE tolerance qualification": true,
    "independent reference energy": true,
    "independent reference momentum": true,
    "independent reference angular momentum": true,
    "antipodal initial COM": true,
    "direct-s20 finite synchronized fields": true,
    "direct-s20 fixed final time": true,
    "direct-s20 positive pair separation": true,
    "direct-s20 momentum_drift": true,
    "direct-s20 angular_drift": true,
    "direct-s20 com_drift": true,
    "direct-s40 finite synchronized fields": true,
    "direct-s40 fixed final time": true,
    "direct-s40 positive pair separation": true,
    "direct-s40 momentum_drift": true,
    "direct-s40 angular_drift": true,
    "direct-s40 com_drift": true,
    "direct-s80 finite synchronized fields": true,
    "direct-s80 fixed final time": true,
    "direct-s80 positive pair separation": true,
    "direct-s80 momentum_drift": true,
    "direct-s80 angular_drift": true,
    "direct-s80 com_drift": true,
    "theta0 finite synchronized fields": true,
    "theta0 fixed final time": true,
    "theta0 positive pair separation": true,
    "theta0 momentum_drift": true,
    "theta0 angular_drift": true,
    "theta0 com_drift": true,
    "theta0 trajectory reproduces direct": true,
    "theta0 same-position force identity": true,
    "theta0.35 finite synchronized fields": true,
    "theta0.35 fixed final time": true,
    "theta0.35 positive pair separation": true,
    "theta.35 trajectory error": true,
    "theta.35 same-position force error": true,
    "theta0.6 finite synchronized fields": true,
    "theta0.6 fixed final time": true,
    "theta0.6 positive pair separation": true,
    "theta.6 actual accepted nodes": true,
    "theta.6 same-position force error": true,
    "direct time refinement 1": true,
    "direct time refinement 2": true,
    "finest direct state error": true,
    "finest direct energy": true,
    "asymmetric diagnostics finite": true,
    "asymmetric tree approximation exercised": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/index.json

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

固定入力を実際に計算した保存配列からの検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- On the Problem of Distribution in Globular Star Clusters. https://academic.oup.com/mnras/article/71/5/460/972150; review_level=bibliography-only-original-unaccessed
Bibliography inherited from prior scoped source review; original full text not read. The finite32-body cold initial condition is density-derived, not an equilibrium Plummer DF or exact continuum flow.

- galpy official Plummer potential definition. https://docs.galpy.org/en/v1.11.0/reference/potentialplummer.html; review_level=official-potential-definition
Official potential normalization read in preparatory source review. No galpy execution; density scale1 and pair softening.05 are distinct parameters.

- SciPy1.14.1 solve_ivp. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-method-api
DOP853 order8, tolerance and t_eval semantics inspected; same softened finite-N ODE with independent scalar pair force. Not an exact analytic N-body solution.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
