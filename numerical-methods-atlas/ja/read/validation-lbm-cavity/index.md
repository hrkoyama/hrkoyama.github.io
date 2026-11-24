# LBMのRe100蓋駆動キャビティ

LBMで四壁に囲まれたRe100の流れを進め、Ghiaの中心線と主渦に照合します。壁との運動量交換も記録します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## LBM Re100蓋駆動キャビティ：実2D場とGhia中心線

4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。

**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-algorithm)

標準D2Q9平衡分布とBGK衝突、非周期link streaming、q=.5の移動halfway反射。流出入分布ごとに壁impulseを加算し、密度補正や内部速度resetをしません。C++17を一時領域でcompileしPythonから呼びます。

$$
f_i^{eq}=w_i\rho[1+3c_i\cdot u+\frac92(c_i\cdot u)^2-\frac32|u|^2],\quad\nu_\ell=(\tau-1/2)/3
$$

$$
f_{\bar i}(x,t+1)=f_i^\star(x,t)-6w_i\rho_0c_i\cdot u_w,\quad\rho_0=1
$$

$$
\mathrm{Re}=UL/\nu=100,\quad t_\star=100
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。


**問題の図**

![LBM Re100蓋駆動キャビティ：実2D場とGhia中心線：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-validation)

各群22pytestと37判定。60k/80k/120k整数stepsでt*=100へ進み90/95/100を保存。最細u/v中心線最大誤差.03、主渦距離.06、95→100相対L2変化2e-4、質量・壁込み運動量ledgerを事前固定します。

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照 · 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照 · 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。
### 前提・単位・境界

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

**編集上の補足**

有限Machでの3格子教育例。Ghiaは丸めた独立数値参照で厳密解ではありません。蓋角は不連続で点ごとの二次精度や高Reを主張せず、他手法の既存キャビティ結果を本LBMの成功に流用しません。標準C++17compilerが必要です。

### 採用した計算法

標準D2Q9平衡分布とBGK衝突、非周期link streaming、q=.5の移動halfway反射。流出入分布ごとに壁impulseを加算し、密度補正や内部速度resetをしません。C++17を一時領域でcompileしPythonから呼びます。

$$
f_i^{eq}=w_i\rho[1+3c_i\cdot u+\frac92(c_i\cdot u)^2-\frac32|u|^2],\quad\nu_\ell=(\tau-1/2)/3
$$

$$
f_{\bar i}(x,t+1)=f_i^\star(x,t)-6w_i\rho_0c_i\cdot u_w,\quad\rho_0=1
$$

$$
\mathrm{Re}=UL/\nu=100,\quad t_\star=100
$$

### 比較・検証

各群22pytestと37判定。60k/80k/120k整数stepsでt*=100へ進み90/95/100を保存。最細u/v中心線最大誤差.03、主渦距離.06、95→100相対L2変化2e-4、質量・壁込み運動量ledgerを事前固定します。

### 確認の限界

有限Machでの3格子教育例。Ghiaは丸めた独立数値参照で厳密解ではありません。蓋角は不連続で点ごとの二次精度や高Reを主張せず、他手法の既存キャビティ結果を本LBMの成功に流用しません。標準C++17compilerが必要です。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest": {
      "n": 48,
      "steps": 120000,
      "tau": 0.5576,
      "dx": 0.020833333333333332,
      "dt": 0.0008333333333333334,
      "time": 100.0,
      "nu_physical": 0.01,
      "u_error": 0.007040567404226761,
      "v_error": 0.007012356068378106,
      "vortex_x": 0.6151785336174457,
      "vortex_y": 0.7373696566057102,
      "vortex_distance": 0.003592378973832659,
      "stationarity": 6.585547769458423e-13,
      "mass_drift": 1.1935933722876744e-11,
      "mass_ledger": 1.1934784256250985e-11,
      "momentum_ledger": 1.2265850980789804e-12,
      "max_mach": 0.06489965337111371,
      "min_rho": 0.9704718614269573,
      "max_rho": 1.030441007310979,
      "min_population": 0.020237879428496697,
      "wall_mass_exchange": -2.648371105751224e-12,
      "open_mass_exchange": 0.0,
      "final_lattice_momentum_x": -7.993605777301127e-14,
      "final_lattice_momentum_y": 5.898753707711535e-14
    },
    "reference": "Ghia1982 printed Re100 tables; limited precision, independent numerical reference"
  },
  "checks": {
    "Ghia printed table shape and anchors": true,
    "24 finite arrays": true,
    "24 positive density": true,
    "24 actual maximum Mach": true,
    "24 mass ledger": true,
    "24 wall-open momentum ledger": true,
    "24 all fixed integer steps": true,
    "24 declared physical endpoint": true,
    "24 closed cavity mass": true,
    "24 late stationarity": true,
    "24 vortex search residual distance": true,
    "32 finite arrays": true,
    "32 positive density": true,
    "32 actual maximum Mach": true,
    "32 mass ledger": true,
    "32 wall-open momentum ledger": true,
    "32 all fixed integer steps": true,
    "32 declared physical endpoint": true,
    "32 closed cavity mass": true,
    "32 late stationarity": true,
    "32 vortex search residual distance": true,
    "48 finite arrays": true,
    "48 positive density": true,
    "48 actual maximum Mach": true,
    "48 mass ledger": true,
    "48 wall-open momentum ledger": true,
    "48 all fixed integer steps": true,
    "48 declared physical endpoint": true,
    "48 closed cavity mass": true,
    "48 late stationarity": true,
    "48 vortex search residual distance": true,
    "finest nominal-lid u centerline": true,
    "finest nominal-lid v centerline": true,
    "finest primary vortex": true,
    "u error decreases coarse to fine": true,
    "v error decreases coarse to fine": true,
    "all three prescribed cavity grids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/index.json

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100-preview.png)

固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/verification.json

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
原著の選択部分を著者資料ミラーから読解。今回の2点線形補間は別導出・単step資格で確認し、2001原著全文を読んだとはしません。

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=existing-audited-primary-transcription
既存の監査済み原表転記と以前のPDF目視出典を再照合。この実装時に原PDFを再取得したとはしません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
