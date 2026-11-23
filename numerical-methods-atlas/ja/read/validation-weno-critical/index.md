# WENOの臨界点・ε依存性

セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 選んだ一次臨界多項式では微小εのJS・Zの局所次数はともに約5で、Zの主誤差が小さい結果です。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## WENO-JS／Z：臨界点とεの固定比較

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

**使用手法**

- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja) (`weno-js`)
- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) (`weno-z`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-algorithm)

3候補と線形重み(.1,.6,.3)、Jiang–Shu指標を共通にし、JSはd/(β+ε)²、Zはd[1+(|β₀−β₂|/(β+ε))²]を正規化します。ε=10⁻⁴⁰,10⁻⁶,h²です。輸送は共有風上面流束と古典RK4、Courant.1を使い、状態クリップ・再試行を行いません。

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`)

局所多項式のセル中心x=0、再構成面h/2、h=1/64…1/512を使います。輸送は[0,1]周期・速度1・q₀=cos(2πx)+.1sin³(2πx)、T=1、32/64/128セルです。全て有限体積セル平均であり、点値を誤差の参照にしません。


**問題の図**

![WENO-JS／Z：臨界点とεの固定比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-validation)

実行前契約で72局所再構成・24PDE計算・36pytestを固定します。解析セル平均を独立Gauss12求積と照合し、局所の誤差・重み、輸送のL1/L2/L∞・質量・全段有限性・中間時刻と保存流束を記録します。最細格子で6通りの刻み半減差が対応する連続解誤差の10%以下か確認します。

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照 · 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照 · 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。
### 前提・単位・境界

局所多項式のセル中心x=0、再構成面h/2、h=1/64…1/512を使います。輸送は[0,1]周期・速度1・q₀=cos(2πx)+.1sin³(2πx)、T=1、32/64/128セルです。全て有限体積セル平均であり、点値を誤差の参照にしません。

**編集上の補足**

一次臨界点の面再構成だけに次数判定を置き、二次臨界点は診断値として残します。固定εは解の振幅・単位に依存します。局所再構成の次数とPDE全体の次数、有限体積版と原著の有限差分版を区別します。衝撃波、Euler/MHD、一般の高次臨界点、任意入力の安定性・TVD・正値性は今回の保証に含めません。 選んだ一次臨界多項式では、微小εのJS・Zのどちらも最後の格子対の局所再構成次数は約5です。JSの絶対誤差は約9.77×10⁻⁹から2.88×10⁻¹³、Zは約2.12×10⁻⁹から5.70×10⁻¹⁴へ減少し、最細のZ/JS比は約.198です。この固定例が示すのは主誤差の減少であり、JSの次数低下やZによる普遍的な臨界点の次数回復を観測したという意味ではありません。二次臨界クラスの結果は別の診断として残します。

### 採用した計算法

3候補と線形重み(.1,.6,.3)、Jiang–Shu指標を共通にし、JSはd/(β+ε)²、Zはd[1+(|β₀−β₂|/(β+ε))²]を正規化します。ε=10⁻⁴⁰,10⁻⁶,h²です。輸送は共有風上面流束と古典RK4、Courant.1を使い、状態クリップ・再試行を行いません。

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

### 比較・検証

実行前契約で72局所再構成・24PDE計算・36pytestを固定します。解析セル平均を独立Gauss12求積と照合し、局所の誤差・重み、輸送のL1/L2/L∞・質量・全段有限性・中間時刻と保存流束を記録します。最細格子で6通りの刻み半減差が対応する連続解誤差の10%以下か確認します。

### 確認の限界

一次臨界点の面再構成だけに次数判定を置き、二次臨界点は診断値として残します。固定εは解の振幅・単位に依存します。局所再構成の次数とPDE全体の次数、有限体積版と原著の有限差分版を区別します。衝撃波、Euler/MHD、一般の高次臨界点、任意入力の安定性・TVD・正値性は今回の保証に含めません。

### 保存実測値と判定

```json
{
  "metrics": {
    "completed_pde_runs": 24,
    "local_reconstructions": 72,
    "maximum_transport_mass_error": 2.3288662664988635e-16
  },
  "checks": {
    "72 fixed local reconstructions": true,
    "24 fixed PDE runs completed": true,
    "independent analytic-cell quadrature": true,
    "convex normalized local weights": true,
    "first-critical weno-js fixed-1e-40 refinement n128": true,
    "first-critical weno-js fixed-1e-40 refinement n256": true,
    "first-critical weno-js fixed-1e-40 refinement n512": true,
    "first-critical weno-js fixed-1e-6 refinement n128": true,
    "first-critical weno-js fixed-1e-6 refinement n256": true,
    "first-critical weno-js fixed-1e-6 refinement n512": true,
    "first-critical weno-js h-squared refinement n128": true,
    "first-critical weno-js h-squared refinement n256": true,
    "first-critical weno-js h-squared refinement n512": true,
    "first-critical weno-z fixed-1e-40 refinement n128": true,
    "first-critical weno-z fixed-1e-40 refinement n256": true,
    "first-critical weno-z fixed-1e-40 refinement n512": true,
    "first-critical weno-z fixed-1e-6 refinement n128": true,
    "first-critical weno-z fixed-1e-6 refinement n256": true,
    "first-critical weno-z fixed-1e-6 refinement n512": true,
    "first-critical weno-z h-squared refinement n128": true,
    "first-critical weno-z h-squared refinement n256": true,
    "first-critical weno-z h-squared refinement n512": true,
    "first-critical tiny-epsilon Z/JS error": true,
    "first-critical last reconstruction order weno-z fixed-1e-40": true,
    "first-critical last reconstruction order weno-js h-squared": true,
    "weno-js-fixed-1e-40-n32: finite saved arrays": true,
    "weno-js-fixed-1e-40-n32: time reached": true,
    "weno-js-fixed-1e-40-n32: periodic mass": true,
    "weno-js-fixed-1e-40-n32: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n32: all requested snapshots": true,
    "weno-js-fixed-1e-40-n32: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n32: no clipping or retries": true,
    "weno-js-fixed-1e-40-n64: finite saved arrays": true,
    "weno-js-fixed-1e-40-n64: time reached": true,
    "weno-js-fixed-1e-40-n64: periodic mass": true,
    "weno-js-fixed-1e-40-n64: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n64: all requested snapshots": true,
    "weno-js-fixed-1e-40-n64: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n64: no clipping or retries": true,
    "weno-js-fixed-1e-40-n128: finite saved arrays": true,
    "weno-js-fixed-1e-40-n128: time reached": true,
    "weno-js-fixed-1e-40-n128: periodic mass": true,
    "weno-js-fixed-1e-40-n128: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n128: all requested snapshots": true,
    "weno-js-fixed-1e-40-n128: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n128: no clipping or retries": true,
    "weno-js-fixed-1e-6-n32: finite saved arrays": true,
    "weno-js-fixed-1e-6-n32: time reached": true,
    "weno-js-fixed-1e-6-n32: periodic mass": true,
    "weno-js-fixed-1e-6-n32: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n32: all requested snapshots": true,
    "weno-js-fixed-1e-6-n32: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n32: no clipping or retries": true,
    "weno-js-fixed-1e-6-n64: finite saved arrays": true,
    "weno-js-fixed-1e-6-n64: time reached": true,
    "weno-js-fixed-1e-6-n64: periodic mass": true,
    "weno-js-fixed-1e-6-n64: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n64: all requested snapshots": true,
    "weno-js-fixed-1e-6-n64: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n64: no clipping or retries": true,
    "weno-js-fixed-1e-6-n128: finite saved arrays": true,
    "weno-js-fixed-1e-6-n128: time reached": true,
    "weno-js-fixed-1e-6-n128: periodic mass": true,
    "weno-js-fixed-1e-6-n128: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n128: all requested snapshots": true,
    "weno-js-fixed-1e-6-n128: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n128: no clipping or retries": true,
    "weno-js-h-squared-n32: finite saved arrays": true,
    "weno-js-h-squared-n32: time reached": true,
    "weno-js-h-squared-n32: periodic mass": true,
    "weno-js-h-squared-n32: shared RHS flux balance": true,
    "weno-js-h-squared-n32: all requested snapshots": true,
    "weno-js-h-squared-n32: four stage evaluations per step": true,
    "weno-js-h-squared-n32: no clipping or retries": true,
    "weno-js-h-squared-n64: finite saved arrays": true,
    "weno-js-h-squared-n64: time reached": true,
    "weno-js-h-squared-n64: periodic mass": true,
    "weno-js-h-squared-n64: shared RHS flux balance": true,
    "weno-js-h-squared-n64: all requested snapshots": true,
    "weno-js-h-squared-n64: four stage evaluations per step": true,
    "weno-js-h-squared-n64: no clipping or retries": true,
    "weno-js-h-squared-n128: finite saved arrays": true,
    "weno-js-h-squared-n128: time reached": true,
    "weno-js-h-squared-n128: periodic mass": true,
    "weno-js-h-squared-n128: shared RHS flux balance": true,
    "weno-js-h-squared-n128: all requested snapshots": true,
    "weno-js-h-squared-n128: four stage evaluations per step": true,
    "weno-js-h-squared-n128: no clipping or retries": true,
    "weno-z-fixed-1e-40-n32: finite saved arrays": true,
    "weno-z-fixed-1e-40-n32: time reached": true,
    "weno-z-fixed-1e-40-n32: periodic mass": true,
    "weno-z-fixed-1e-40-n32: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n32: all requested snapshots": true,
    "weno-z-fixed-1e-40-n32: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n32: no clipping or retries": true,
    "weno-z-fixed-1e-40-n64: finite saved arrays": true,
    "weno-z-fixed-1e-40-n64: time reached": true,
    "weno-z-fixed-1e-40-n64: periodic mass": true,
    "weno-z-fixed-1e-40-n64: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n64: all requested snapshots": true,
    "weno-z-fixed-1e-40-n64: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n64: no clipping or retries": true,
    "weno-z-fixed-1e-40-n128: finite saved arrays": true,
    "weno-z-fixed-1e-40-n128: time reached": true,
    "weno-z-fixed-1e-40-n128: periodic mass": true,
    "weno-z-fixed-1e-40-n128: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n128: all requested snapshots": true,
    "weno-z-fixed-1e-40-n128: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n128: no clipping or retries": true,
    "weno-z-fixed-1e-6-n32: finite saved arrays": true,
    "weno-z-fixed-1e-6-n32: time reached": true,
    "weno-z-fixed-1e-6-n32: periodic mass": true,
    "weno-z-fixed-1e-6-n32: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n32: all requested snapshots": true,
    "weno-z-fixed-1e-6-n32: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n32: no clipping or retries": true,
    "weno-z-fixed-1e-6-n64: finite saved arrays": true,
    "weno-z-fixed-1e-6-n64: time reached": true,
    "weno-z-fixed-1e-6-n64: periodic mass": true,
    "weno-z-fixed-1e-6-n64: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n64: all requested snapshots": true,
    "weno-z-fixed-1e-6-n64: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n64: no clipping or retries": true,
    "weno-z-fixed-1e-6-n128: finite saved arrays": true,
    "weno-z-fixed-1e-6-n128: time reached": true,
    "weno-z-fixed-1e-6-n128: periodic mass": true,
    "weno-z-fixed-1e-6-n128: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n128: all requested snapshots": true,
    "weno-z-fixed-1e-6-n128: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n128: no clipping or retries": true,
    "weno-z-h-squared-n32: finite saved arrays": true,
    "weno-z-h-squared-n32: time reached": true,
    "weno-z-h-squared-n32: periodic mass": true,
    "weno-z-h-squared-n32: shared RHS flux balance": true,
    "weno-z-h-squared-n32: all requested snapshots": true,
    "weno-z-h-squared-n32: four stage evaluations per step": true,
    "weno-z-h-squared-n32: no clipping or retries": true,
    "weno-z-h-squared-n64: finite saved arrays": true,
    "weno-z-h-squared-n64: time reached": true,
    "weno-z-h-squared-n64: periodic mass": true,
    "weno-z-h-squared-n64: shared RHS flux balance": true,
    "weno-z-h-squared-n64: all requested snapshots": true,
    "weno-z-h-squared-n64: four stage evaluations per step": true,
    "weno-z-h-squared-n64: no clipping or retries": true,
    "weno-z-h-squared-n128: finite saved arrays": true,
    "weno-z-h-squared-n128: time reached": true,
    "weno-z-h-squared-n128: periodic mass": true,
    "weno-z-h-squared-n128: shared RHS flux balance": true,
    "weno-z-h-squared-n128: all requested snapshots": true,
    "weno-z-h-squared-n128: four stage evaluations per step": true,
    "weno-z-h-squared-n128: no clipping or retries": true,
    "weno-js-fixed-1e-40-time-half: finite saved arrays": true,
    "weno-js-fixed-1e-40-time-half: time reached": true,
    "weno-js-fixed-1e-40-time-half: periodic mass": true,
    "weno-js-fixed-1e-40-time-half: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-time-half: all requested snapshots": true,
    "weno-js-fixed-1e-40-time-half: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-time-half: no clipping or retries": true,
    "weno-js-fixed-1e-6-time-half: finite saved arrays": true,
    "weno-js-fixed-1e-6-time-half: time reached": true,
    "weno-js-fixed-1e-6-time-half: periodic mass": true,
    "weno-js-fixed-1e-6-time-half: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-time-half: all requested snapshots": true,
    "weno-js-fixed-1e-6-time-half: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-time-half: no clipping or retries": true,
    "weno-js-h-squared-time-half: finite saved arrays": true,
    "weno-js-h-squared-time-half: time reached": true,
    "weno-js-h-squared-time-half: periodic mass": true,
    "weno-js-h-squared-time-half: shared RHS flux balance": true,
    "weno-js-h-squared-time-half: all requested snapshots": true,
    "weno-js-h-squared-time-half: four stage evaluations per step": true,
    "weno-js-h-squared-time-half: no clipping or retries": true,
    "weno-z-fixed-1e-40-time-half: finite saved arrays": true,
    "weno-z-fixed-1e-40-time-half: time reached": true,
    "weno-z-fixed-1e-40-time-half: periodic mass": true,
    "weno-z-fixed-1e-40-time-half: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-time-half: all requested snapshots": true,
    "weno-z-fixed-1e-40-time-half: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-time-half: no clipping or retries": true,
    "weno-z-fixed-1e-6-time-half: finite saved arrays": true,
    "weno-z-fixed-1e-6-time-half: time reached": true,
    "weno-z-fixed-1e-6-time-half: periodic mass": true,
    "weno-z-fixed-1e-6-time-half: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-time-half: all requested snapshots": true,
    "weno-z-fixed-1e-6-time-half: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-time-half: no clipping or retries": true,
    "weno-z-h-squared-time-half: finite saved arrays": true,
    "weno-z-h-squared-time-half: time reached": true,
    "weno-z-h-squared-time-half: periodic mass": true,
    "weno-z-h-squared-time-half: shared RHS flux balance": true,
    "weno-z-h-squared-time-half: all requested snapshots": true,
    "weno-z-h-squared-time-half: four stage evaluations per step": true,
    "weno-z-h-squared-time-half: no clipping or retries": true,
    "weno-js fixed-1e-40 PDE refinement n64": true,
    "weno-js fixed-1e-40 PDE refinement n128": true,
    "weno-js fixed-1e-40 finest PDE L1": true,
    "weno-js fixed-1e-40 dt contamination fraction": true,
    "weno-js fixed-1e-6 PDE refinement n64": true,
    "weno-js fixed-1e-6 PDE refinement n128": true,
    "weno-js fixed-1e-6 finest PDE L1": true,
    "weno-js fixed-1e-6 dt contamination fraction": true,
    "weno-js h-squared PDE refinement n64": true,
    "weno-js h-squared PDE refinement n128": true,
    "weno-js h-squared finest PDE L1": true,
    "weno-js h-squared dt contamination fraction": true,
    "weno-z fixed-1e-40 PDE refinement n64": true,
    "weno-z fixed-1e-40 PDE refinement n128": true,
    "weno-z fixed-1e-40 finest PDE L1": true,
    "weno-z fixed-1e-40 dt contamination fraction": true,
    "weno-z fixed-1e-6 PDE refinement n64": true,
    "weno-z fixed-1e-6 PDE refinement n128": true,
    "weno-z fixed-1e-6 finest PDE L1": true,
    "weno-z fixed-1e-6 dt contamination fraction": true,
    "weno-z h-squared PDE refinement n64": true,
    "weno-z h-squared PDE refinement n128": true,
    "weno-z h-squared finest PDE L1": true,
    "weno-z h-squared dt contamination fraction": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/index.json

![保存した最細格子の実際の周期輸送場とセル平均誤差、別の局所多項式による一次臨界点の面再構成誤差。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon-preview.png)

保存した最細格子の実際の周期輸送場とセル平均誤差、別の局所多項式による一次臨界点の面再構成誤差。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- Guang-Shan Jiang and Chi-Wang Shu (1996). Efficient Implementation of Weighted ENO Schemes. https://ntrs.nasa.gov/api/citations/19960007052/downloads/19960007052.pdf; review_level=NASA-hosted ICASE95-73 preprint selected sections1–3: candidate Table1, optimal Table2, equations2.15–2.16 and3.1–3.9; text layer inspected, not full paper/numerical tables
  NASA公開プレプリントの節1–3で係数・重み・滑らかさ指標と有限差分の点値の規約を確認。原著の全実験やEuler特性分解を再現したとは表示しません。
- Rafael Borges, Monique Carmona, Bruno Costa and Wai Sun Don (2008). An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. https://scholars.hkbu.edu.hk/en/publications/an-improved-weighted-essentially-non-oscillatory-scheme-for-hyper-2/; review_level=Author-institution publication record and abstract inspected; publisher full text returned403; original full paper and numerical experiments not audited
  著者所属機関の書誌と抄録を確認。出版社全文は取得不能であり、全文読了・元の実験・指数1の再現は主張しません。実装する指数2の式は別の一次研究論文でも確認しました。
- Bart S. van Lith, Jan H. M. ten Thije Boonkkamp and Wilbert L. IJzerman (2017). Embedded WENO: A design strategy to improve existing WENO schemes. https://pure.tue.nl/ws/portalfiles/portal/53481949/embedded_WENO.pdf; review_level=Institution-hosted accepted manuscript section2 equations2–15 (PDF pages4–8) and selected section4.2 (PDF page22) text inspected; screenshot requests cache-missed; not a full-paper review
  機関公開の著者版でセル平均の式(2)–(3)、候補・線形重み(4)–(7)、JS指標と重み(8)–(13)、Z重み(15)、節4.2の指数2を確認。新規のembedded方式は実装せず、論文PDFも同梱しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
