# LBMの曲面壁とRe20円柱

Re20円柱流の曲面壁と流出境界を実計算し、抗力・圧力差・後流を独立な数値ベンチマークへ照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## LBMの実円柱Re20：Schäfer–Turek形状と明示出口

標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。

**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-algorithm)

標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。


**問題の図**

![LBMの実円柱Re20：Schäfer–Turek形状と明示出口：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-validation)

群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。

- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja) (`lbm-cylinder-re20`; 同じ問題の参照 · 有限格子の数値参照)

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。
### 前提・単位・境界

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

**編集上の補足**

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

### 採用した計算法

標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

### 比較・検証

群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。

### 確認の限界

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest": {
      "dx": 0.005,
      "dt": 0.0008333333333333334,
      "tau": 0.6,
      "steps": 36000,
      "time": 30.000000000000004,
      "Re": 20,
      "CD": 5.644519321602302,
      "CL": 0.011096755643135437,
      "stationarity": 0.0002032789456526155,
      "drag_drift": 0.000151098422030169,
      "lift_drift": 3.478689810392302e-06,
      "pressure_drift": 1.863260540397613e-06,
      "pressure_difference": 0.11872124659802585,
      "recirculation_length": 0.08386681527452555,
      "mass_drift": 0.0004002747565754678,
      "mass_ledger": 3.339112580809518e-12,
      "momentum_ledger": 3.37499434539968e-12,
      "max_mach": 0.1536578006651768,
      "min_rho": 0.9010633065006105,
      "max_rho": 1.1123850424542971,
      "min_population": 0.020454450201225206,
      "wall_mass_exchange": 16.570402727464682,
      "open_mass_exchange": -2.2019060198153952,
      "final_lattice_momentum_x": 1213.6393581371472,
      "final_lattice_momentum_y": 0.17207763765525091
    },
    "reference_scope": "Schäfer-Turek1996 Table3 estimated numerical-comparison ranges, not exact or rigorous enclosures. Original pp3/7 allow user-selected outflow. This source uses a declared all-nine poststream NEE pressure reservoir, not later FEATflow do-nothing; exact original-author NEE implementation is not claimed. Coarse LBM acceptance separately fixed before execution.",
    "outlet": "All-nine poststream NEE: rho1,adjacent-poststream velocity; finite reservoir,not later FEATflow do-nothing",
    "initial_pressure": "Straight Poiseuille-gradient guess, not a cylinder reference or imposed interior field"
  },
  "checks": {
    "original source definitions and interval anchors": true,
    "0.01 finite arrays": true,
    "0.01 positive density": true,
    "0.01 actual maximum Mach": true,
    "0.01 mass ledger": true,
    "0.01 wall-open momentum ledger": true,
    "0.01 all fixed integer steps": true,
    "0.01 declared physical endpoint": true,
    "0.01 velocity stationarity": true,
    "0.01 drag late block drift": true,
    "0.01 lift late block drift": true,
    "0.01 pressure late drift": true,
    "0.01 positive downstream drag": true,
    "0.01 pressure front exceeds back": true,
    "0.005 finite arrays": true,
    "0.005 positive density": true,
    "0.005 actual maximum Mach": true,
    "0.005 mass ledger": true,
    "0.005 wall-open momentum ledger": true,
    "0.005 all fixed integer steps": true,
    "0.005 declared physical endpoint": true,
    "0.005 velocity stationarity": true,
    "0.005 drag late block drift": true,
    "0.005 lift late block drift": true,
    "0.005 pressure late drift": true,
    "0.005 positive downstream drag": true,
    "0.005 pressure front exceeds back": true,
    "finest original range distance CD": true,
    "finest original range distance CL": true,
    "finest original range distance pressure_difference": true,
    "finest original range distance recirculation_length": true,
    "two-grid drag sensitivity": true,
    "both prescribed actual full-domain cylinder grids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/index.json

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json

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

- M. Schäfer and S. Turek (1996). Benchmark Computations of Laminar Flow Around a Cylinder. https://kent-and.github.io/mek4250/2021/SchaeferTurek1996.pdf; review_level=primary-selected-extracted-text
原論文の形状・定義・出口自由選択・表3の推定範囲を選択読解。公式リンク404後の講義ミラー配送を明記します。

- FEATflow benchmark project (2026). DFG flow around cylinder benchmark2D-1, Re20. https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark1_re20.html; review_level=official-benchmark-page
公式頁のBC・定義とNabhへの帰属を確認。Nabh原報未読で、採用出口と同一条件の厳密値とはしません。

- Zhaoli Guo,Chuguang Zheng and Baochang Shi (2002). Non-equilibrium extrapolation method for velocity and pressure boundary conditions in the lattice Boltzmann method. https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310; review_level=primary-official-abstract-only
公式の原著抄録のみ読解。全文の式は未読で、採用する全9成分poststream圧力reservoirは別導出・資格です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
