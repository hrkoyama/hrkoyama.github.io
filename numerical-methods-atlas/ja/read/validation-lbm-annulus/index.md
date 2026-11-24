# 曲面LBMの環状Couette流

同じ物理条件で格子を細かくし、曲面補間と階段壁の速度・点ごとの圧力・トルクを解析解に照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 曲面LBMの環状Couette制御：速度・圧力・torque

実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。

**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-algorithm)

円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。


**問題の図**

![曲面LBMの環状Couette制御：速度・圧力・torque：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-validation)

群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。

- [曲面LBMの環状Couette制御：速度・圧力・トルク](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja) (`lbm-annular-couette-control`; 同じ問題の参照 · 解析参照)

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。
### 前提・単位・境界

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

**編集上の補足**

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

### 採用した計算法

円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

### 比較・検証

群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。

### 確認の限界

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_interpolated": {
      "variant": 0,
      "n": 240,
      "steps": 34560,
      "dx": 0.004166666666666667,
      "dt": 0.00011574074074074072,
      "time": 3.999999999999999,
      "tau": 0.7,
      "nu": 0.01,
      "velocity_error": 4.1181013570439095e-05,
      "pressure_error": 0.056576140457462176,
      "torque": -0.0006702247827550396,
      "exact_torque": -0.0006702064327658225,
      "torque_error": 2.7379607714759232e-05,
      "stationarity": 5.063686002269724e-08,
      "torque_drift": 4.646498909951803e-09,
      "mass_drift": 4.200271990063427e-07,
      "mass_ledger": 2.7512395413137817e-12,
      "momentum_ledger": 9.763298584209473e-13,
      "max_mach": 0.0009599923524199409,
      "min_rho": 0.9999997461691433,
      "max_rho": 1.0000004573310033,
      "min_population": 0.027712534590816466,
      "wall_mass_exchange": 0.00912977083678769,
      "open_mass_exchange": 0.0,
      "final_lattice_momentum_x": 4.615197113366776e-13,
      "final_lattice_momentum_y": 5.0622700475955185e-14
    },
    "finest_stair": {
      "variant": 1,
      "n": 240,
      "steps": 34560,
      "dx": 0.004166666666666667,
      "dt": 0.00011574074074074072,
      "time": 3.999999999999999,
      "tau": 0.7,
      "nu": 0.01,
      "velocity_error": 0.0056320234931158345,
      "pressure_error": 5.0386965555033765,
      "torque": -0.0006741976046875688,
      "exact_torque": -0.0006702064327658225,
      "torque_error": 0.005955138188207717,
      "stationarity": 2.173500599846503e-07,
      "torque_drift": 4.07061909864866e-07,
      "mass_drift": 2.7425432799505342e-12,
      "mass_ledger": 2.7517486245531947e-12,
      "momentum_ledger": 8.644174008350578e-13,
      "max_mach": 0.0009599923524199409,
      "min_rho": 0.9999925252188234,
      "max_rho": 1.000007128199855,
      "min_population": 0.027712460348227712,
      "wall_mass_exchange": -1.4606371667724716e-15,
      "open_mass_exchange": 0.0,
      "final_lattice_momentum_x": -3.0608848788915566e-13,
      "final_lattice_momentum_y": 5.230781086051906e-13
    },
    "reference_qualification": {
      "radial viscous equation": 5.551115123125783e-17,
      "radial pressure equation": 2.574980159653073e-19,
      "Cartesian divergence": 1.3877787807814457e-17,
      "Cartesian x momentum": 4.336808689942018e-19,
      "Cartesian y momentum": 2.168404344971009e-19,
      "inner wall speed": 0.0,
      "outer wall speed": 1.734723475976807e-18
    },
    "scope": "Stationary rotating-wall annulus only; does not substitute for actual cylinder flow."
  },
  "checks": {
    "analytic reference radial viscous equation": true,
    "analytic reference radial pressure equation": true,
    "analytic reference Cartesian divergence": true,
    "analytic reference Cartesian x momentum": true,
    "analytic reference Cartesian y momentum": true,
    "analytic reference inner wall speed": true,
    "analytic reference outer wall speed": true,
    "0-80 finite arrays": true,
    "0-80 positive density": true,
    "0-80 actual maximum Mach": true,
    "0-80 mass ledger": true,
    "0-80 wall-open momentum ledger": true,
    "0-80 all fixed integer steps": true,
    "0-80 declared physical endpoint": true,
    "0-80 total mass drift diagnostic bound": true,
    "0-80 late velocity stationarity": true,
    "0-80 late torque stationarity": true,
    "0-80 correct inner resisting torque sign": true,
    "0-160 finite arrays": true,
    "0-160 positive density": true,
    "0-160 actual maximum Mach": true,
    "0-160 mass ledger": true,
    "0-160 wall-open momentum ledger": true,
    "0-160 all fixed integer steps": true,
    "0-160 declared physical endpoint": true,
    "0-160 total mass drift diagnostic bound": true,
    "0-160 late velocity stationarity": true,
    "0-160 late torque stationarity": true,
    "0-160 correct inner resisting torque sign": true,
    "0-240 finite arrays": true,
    "0-240 positive density": true,
    "0-240 actual maximum Mach": true,
    "0-240 mass ledger": true,
    "0-240 wall-open momentum ledger": true,
    "0-240 all fixed integer steps": true,
    "0-240 declared physical endpoint": true,
    "0-240 total mass drift diagnostic bound": true,
    "0-240 late velocity stationarity": true,
    "0-240 late torque stationarity": true,
    "0-240 correct inner resisting torque sign": true,
    "1-80 finite arrays": true,
    "1-80 positive density": true,
    "1-80 actual maximum Mach": true,
    "1-80 mass ledger": true,
    "1-80 wall-open momentum ledger": true,
    "1-80 all fixed integer steps": true,
    "1-80 declared physical endpoint": true,
    "1-80 total mass drift diagnostic bound": true,
    "1-80 late velocity stationarity": true,
    "1-80 late torque stationarity": true,
    "1-80 correct inner resisting torque sign": true,
    "1-160 finite arrays": true,
    "1-160 positive density": true,
    "1-160 actual maximum Mach": true,
    "1-160 mass ledger": true,
    "1-160 wall-open momentum ledger": true,
    "1-160 all fixed integer steps": true,
    "1-160 declared physical endpoint": true,
    "1-160 total mass drift diagnostic bound": true,
    "1-160 late velocity stationarity": true,
    "1-160 late torque stationarity": true,
    "1-160 correct inner resisting torque sign": true,
    "1-240 finite arrays": true,
    "1-240 positive density": true,
    "1-240 actual maximum Mach": true,
    "1-240 mass ledger": true,
    "1-240 wall-open momentum ledger": true,
    "1-240 all fixed integer steps": true,
    "1-240 declared physical endpoint": true,
    "1-240 total mass drift diagnostic bound": true,
    "1-240 late velocity stationarity": true,
    "1-240 late torque stationarity": true,
    "1-240 correct inner resisting torque sign": true,
    "finest interpolated velocity": true,
    "finest interpolated pressure gauge": true,
    "finest interpolated torque": true,
    "interpolated velocity refinement": true,
    "interpolated pressure refinement": true,
    "interpolated improves finest stair velocity": true,
    "three grids with both boundary variants": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/index.json

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Qisu Zou and Xiaoyi He (1996). On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model. https://arxiv.org/abs/comp-gas/9611001; review_level=primary-selected-extracted-text
原著preprintの式と平面流入出境界・角・圧縮性の範囲を選択読解。特殊d2q9iの成功を本BGKへ流用しません。

- Pierre Lallemand and Li-Shi Luo (2003). Lattice Boltzmann method for moving boundaries. https://doi.org/10.1016/S0021-9991(02)00022-0; review_level=primary-selected-text-via-mirror
原著選択部分Eq12–15の2次補間・壁補正・運動量交換・mass非保存を読解。汎用Lagrange式の独立scalarで係数を資格。2001原著全文や局所PDFの画像確認は未実施です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
