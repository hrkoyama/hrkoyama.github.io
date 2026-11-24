# 小型学習モデルと生物ODEの独立検証

Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 1D Poisson PINNと独立格子誤差

3固定seedの49パラメータPINNを解析解・FDと比較します。

**使用手法**

- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) (`pinn-operators`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-algorithm)

x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。


**問題の図**

![1D Poisson PINNと独立格子誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-validation)

全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。

- [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja) (`pinn-poisson`; 関連モデルの参照 · 製造解)

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。
### 前提・単位・境界

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

**編集上の補足**

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

### 採用した計算法

x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

### 比較・検証

全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

### 確認の限界

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seed-8401:optimizer-converged": false,
    "seed-8401:solution_Linf": true,
    "seed-8401:PDE_normalized_RMS": true,
    "seed-8401:boundary_Linf": true,
    "seed-8402:optimizer-converged": false,
    "seed-8402:solution_Linf": true,
    "seed-8402:PDE_normalized_RMS": true,
    "seed-8402:boundary_Linf": true,
    "seed-8403:optimizer-converged": false,
    "seed-8403:solution_Linf": true,
    "seed-8403:PDE_normalized_RMS": true,
    "seed-8403:boundary_Linf": true,
    "fd-31:solution_Linf": true,
    "fd-63:solution_Linf": true,
    "fd-127:solution_Linf": true
  },
  "original_target_summary": {
    "met": 12,
    "total": 15,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "training_seeds": 3,
    "parameters": 49,
    "independent_grid_points": 257,
    "FD_runs": 3
  },
  "checks": {
    "seed-8401:finite-shape": true,
    "seed-8401:optimizer-return-status": true,
    "seed-8401:actual-work": true,
    "seed-8402:finite-shape": true,
    "seed-8402:optimizer-return-status": true,
    "seed-8402:actual-work": true,
    "seed-8403:finite-shape": true,
    "seed-8403:optimizer-return-status": true,
    "seed-8403:actual-work": true,
    "fd-31:true-residual": true,
    "fd-63:true-residual": true,
    "fd-127:true-residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/index.json

![3固定seedの49パラメータPINNを解析解・FDと比較します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson-preview.png)

3固定seedの49パラメータPINNを解析解・FDと比較します。 保存値だけを描画します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/pdf/1711.10561; review_level=selected-primary-body
Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 小型FNOの問題単位検証

同じ重みで32/64点・未見関数・OODを分けて評価します。

**使用手法**

- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) (`pinn-operators`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-algorithm)

入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。


**問題の図**

![小型FNOの問題単位検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-validation)

全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照 · 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja) (`fno-periodic-heat`; 関連モデルの参照 · 解析参照)

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。
### 前提・単位・境界

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

**編集上の補足**

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。 旧熱拡散primaryを保持し、今回の[0,2π)・問題単位データ族・νとTは別入力として示します。

### 採用した計算法

入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

### 比較・検証

全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

### 確認の限界

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seed-8501:optimizer-converged": false,
    "seed-8501:ID-N32-relative": true,
    "seed-8501:ID-N64-relative": true,
    "seed-8501:norm-control-absolute": true,
    "seed-8502:optimizer-converged": false,
    "seed-8502:ID-N32-relative": true,
    "seed-8502:ID-N64-relative": true,
    "seed-8502:norm-control-absolute": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 8,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "models": 2,
    "parameters_per_model": 93,
    "whole_problem_IDs": 46,
    "prediction_rows": 116,
    "nonlinear_dealiasing": "none",
    "restriction_discrepancy_scope": "Native-grid nonlinear/alias sensitivity, not continuum error"
  },
  "checks": {
    "seed-8501:finite-parameters": true,
    "seed-8501:optimizer-return-status": true,
    "seed-8501:actual-work": true,
    "seed-8501:relative-NA": true,
    "seed-8502:finite-parameters": true,
    "seed-8502:optimizer-return-status": true,
    "seed-8502:actual-work": true,
    "seed-8502:relative-NA": true,
    "disjoint-whole-problem-IDs": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/index.json

![同じ重みで32/64点・未見関数・OODを分けて評価します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat-preview.png)

同じ重みで32/64点・未見関数・OODを分けて評価します。 保存値だけを描画します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Fourier Neural Operator for Parametric Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/html/2010.08895v3; review_level=selected-primary-body
Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 酵素反応の保存と準定常近似

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

**使用手法**

- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) (`sdirk2`)
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) (`step-doubling`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-algorithm)

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

- [Michaelis–Mentenと完全酵素反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja) (`bio-enzyme`)

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。


**問題の図**

![酵素反応の保存と準定常近似：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) (`enzyme-qssa`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-validation)

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja) (`enzyme-qssa`; 同じ問題の参照 · 有限格子の数値参照)

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
### 前提・単位・境界

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

**編集上の補足**

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

### 採用した計算法

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

### 比較・検証

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

### 確認の限界

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "enzyme-01-r1e-06:integration": true,
    "enzyme-01-r1e-06:mass": true,
    "enzyme-01-r1e-06:negative-part": true,
    "enzyme-01-r1e-06:QSSA-model": true,
    "enzyme-01-r1e-08:integration": true,
    "enzyme-01-r1e-08:mass": true,
    "enzyme-01-r1e-08:negative-part": true,
    "enzyme-01-r1e-08:QSSA-model": true,
    "enzyme-002-r1e-06:integration": true,
    "enzyme-002-r1e-06:mass": true,
    "enzyme-002-r1e-06:negative-part": true,
    "enzyme-002-r1e-06:QSSA-model": true,
    "enzyme-002-r1e-08:integration": true,
    "enzyme-002-r1e-08:mass": true,
    "enzyme-002-r1e-08:negative-part": true,
    "enzyme-002-r1e-08:QSSA-model": true
  },
  "original_target_summary": {
    "met": 16,
    "total": 16,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "enzyme-01-r1e-06:completed-work": true,
    "enzyme-01-r1e-06:finite": true,
    "enzyme-01-r1e-08:completed-work": true,
    "enzyme-01-r1e-08:finite": true,
    "enzyme-002-r1e-06:completed-work": true,
    "enzyme-002-r1e-06:finite": true,
    "enzyme-002-r1e-08:completed-work": true,
    "enzyme-002-r1e-08:finite": true,
    "mm-200:finite": true,
    "mm-400:finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/index.json

![全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Rigorous estimates for the quasi-steady state approximation of the Michaelis–Menten reaction mechanism at low enzyme concentrations [accessed 2026-11-24]. https://arxiv.org/html/2305.12602v2; review_level=selected-primary-body
Selected §1 Eq(1)–(8) and selected discussion around transient-time estimates Eq(32); proofs and complete quantitative bounds unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Lotka–Volterra不変量と正値性

正の軌道を独立な対数座標参照と比較します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-algorithm)

固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

- [Lotka–Volterra捕食・被食](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja) (`bio-lotka-volterra`)

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。


**問題の図**

![Lotka–Volterra不変量と正値性：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja) (`lotka-volterra`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-validation)

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

- [Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lotka-volterra-ja) (`lotka-volterra`; 同じ問題の参照 · 有限格子の数値参照)

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
### 前提・単位・境界

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

**編集上の補足**

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

### 採用した計算法

固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

### 比較・検証

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

### 確認の限界

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "lv-400:state": true,
    "lv-400:invariant": true,
    "lv-800:state": true,
    "lv-800:invariant": true,
    "lv-1600:state": true,
    "lv-1600:invariant": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 6,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 3,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "lv-400:actual-grid-finite": true,
    "lv-800:actual-grid-finite": true,
    "lv-1600:actual-grid-finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/index.json

![正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Experiments in MATLAB, Chapter16: Predator-Prey Model [accessed 2026-11-24]. https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/exm/chapters/predprey.pdf; review_level=selected-primary-body
Selected extracted text pp3–6: normalized LV equations, equilibrium, periodic-orbit discussion and numerical illustration. No original Lotka/Volterra paper read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SEIR保存則と初期線形化

人口保存と2モードの初期線形化を別々に検査します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-algorithm)

全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

- [閉鎖SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#seir-compartment-ja) (`seir-compartment`)

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。


**問題の図**

![SEIR保存則と初期線形化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja) (`seir-linearization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-validation)

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

- [SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-seir-linearization-ja) (`seir-linearization`; 同じ問題の参照 · 有限格子の数値参照)

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。
### 前提・単位・境界

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

**編集上の補足**

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

### 採用した計算法

全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

### 比較・検証

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

### 確認の限界

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seir-1e-4-400:integration": true,
    "seir-1e-4-400:mass": true,
    "seir-1e-4-400:negative-part": true,
    "seir-1e-4-800:integration": true,
    "seir-1e-4-800:mass": true,
    "seir-1e-4-800:negative-part": true,
    "seir-1e-4-1600:integration": true,
    "seir-1e-4-1600:mass": true,
    "seir-1e-4-1600:negative-part": true,
    "seir-1e-4:early-linearization": true,
    "seir-5e-5-400:integration": true,
    "seir-5e-5-400:mass": true,
    "seir-5e-5-400:negative-part": true,
    "seir-5e-5-800:integration": true,
    "seir-5e-5-800:mass": true,
    "seir-5e-5-800:negative-part": true,
    "seir-5e-5-1600:integration": true,
    "seir-5e-5-1600:mass": true,
    "seir-5e-5-1600:negative-part": true,
    "seir-5e-5:early-linearization": true
  },
  "original_target_summary": {
    "met": 20,
    "total": 20,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "seir-1e-4-400:actual-grid-finite": true,
    "seir-1e-4-800:actual-grid-finite": true,
    "seir-1e-4-1600:actual-grid-finite": true,
    "seir-5e-5-400:actual-grid-finite": true,
    "seir-5e-5-800:actual-grid-finite": true,
    "seir-5e-5-1600:actual-grid-finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/index.json

![人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- The Mathematics of Infectious Diseases [accessed 2026-11-24]. https://math.uchicago.edu/~shmuel/Modeling/hethcote2000%20Mathematics%20of%20Infectious%20diseases.pdf; review_level=selected-primary-body
Header, selected introduction compartment definitions and §3.1 printedpp618–619, displayed mass-action numbers and Eq(3.1); search around3.2/SEIR limit. Not whole55pages or visual diagram audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
