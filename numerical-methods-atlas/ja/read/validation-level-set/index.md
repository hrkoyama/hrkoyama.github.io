# レベルセット法：円の2D移流・剛体回転

符号付き距離のゼロ等値線を32²/64²/128²で数値移流し、再初期化の有無、解析的な界面位置、面積と格子・時間刻みの細分化を比較します。VOFは理論比較のみです。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## レベルセット円の2D平行移動：界面・面積・再初期化

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

**使用手法**

- [レベルセット法](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja) (`level-set`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-algorithm)

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja) (`level-set-advection`)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。


**問題の図**

![レベルセット円の2D平行移動：界面・面積・再初期化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-validation)

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja) (`level-set-translation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja) (`level-set-rotation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
### 前提・単位・境界

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

### 採用した計算法

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

### 比較・検証

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

### 確認の限界

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_grid": 128,
    "final_time": 1.0,
    "advection_observed_order": 1.8968704888340944,
    "advection_finest_interface_error": 0.00029557712133185254,
    "advection_finest_relative_area_error": 0.002182466628085633,
    "redistance_finest_interface_error": 0.0011428359418646783,
    "redistance_finest_relative_area_error": 0.00931654728247977,
    "redistance_maximum_area_jump": 0.0005264752370461312,
    "cfl_halving_band_phi_difference_n64": 1.4067607491909376e-05
  },
  "checks": {
    "advection_interface_refines": true,
    "advection_order_resolved": true,
    "advection_finest_interface": true,
    "advection_finest_area": true,
    "redistance_finest_interface": true,
    "redistance_finest_area": true,
    "shared_observation_times": true,
    "courant_bound": true,
    "time_step_sensitivity": true,
    "fixed_redistance_schedule": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs-initial.json

### 出典と確認範囲

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf; review_level=full-text
著者公開の原著から抄録・陰的な界面表現・Hamilton–Jacobi型の移流と法線運動の該当箇所を参照。論文全体の監査や原著の全計算の再現ではありません。

- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://www.sciencedirect.com/science/article/pii/0021999181901455; review_level=abstract-and-metadata
出版社の書誌・抄録を確認し、体積率による表現の原著として引用。原著全体やdonor–acceptor法の実装を監査・再現したとは主張しません。

- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://epubs.siam.org/doi/10.1137/S1064827596298245; review_level=abstract-and-metadata
公式の抄録・書誌を確認。距離関数の再構成とゼロ界面の保持を区別する資料であり、原著の制約付き高次法を今回の単純なGodunov反復と同一視しません。

- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf; review_level=full-text
著者公開PDFの302–305頁、式(1)–(6),(9),(12),(15)の界面幾何・囲まれた質量の誤差・体積率の保存を参照。本教材は内部を負とするため符号規約を反転。CLSVOFや二相流の原著実験は実行していません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 偏心したレベルセット円の2D剛体回転

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

**使用手法**

- [レベルセット法](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja) (`level-set`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-algorithm)

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja) (`level-set-advection`)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。


**問題の図**

![偏心したレベルセット円の2D剛体回転：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[レベルセットで表した円の移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja) (`level-set-circle`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-validation)

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja) (`level-set-translation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja) (`level-set-rotation`; 同じ問題の参照 · 解析参照)

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
### 前提・単位・境界

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

### 採用した計算法

移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

### 比較・検証

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

### 確認の限界

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_grid": 128,
    "final_time": 1.0,
    "advection_observed_order": 2.0215147988362197,
    "advection_finest_interface_error": 0.0013945082921070773,
    "advection_finest_relative_area_error": 0.010638924591504395,
    "redistance_finest_interface_error": 0.0021776855808661455,
    "redistance_finest_relative_area_error": 0.020243352863389963,
    "redistance_maximum_area_jump": 0.0005648260383181863,
    "cfl_halving_band_phi_difference_n64": 7.785529870305357e-06
  },
  "checks": {
    "advection_interface_refines": true,
    "advection_order_resolved": true,
    "advection_finest_interface": true,
    "advection_finest_area": true,
    "redistance_finest_interface": true,
    "redistance_finest_area": true,
    "shared_observation_times": true,
    "courant_bound": true,
    "time_step_sensitivity": true,
    "fixed_redistance_schedule": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs-initial.json

### 出典と確認範囲

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf; review_level=full-text
著者公開の原著から抄録・陰的な界面表現・Hamilton–Jacobi型の移流と法線運動の該当箇所を参照。論文全体の監査や原著の全計算の再現ではありません。

- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://www.sciencedirect.com/science/article/pii/0021999181901455; review_level=abstract-and-metadata
出版社の書誌・抄録を確認し、体積率による表現の原著として引用。原著全体やdonor–acceptor法の実装を監査・再現したとは主張しません。

- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://epubs.siam.org/doi/10.1137/S1064827596298245; review_level=abstract-and-metadata
公式の抄録・書誌を確認。距離関数の再構成とゼロ界面の保持を区別する資料であり、原著の制約付き高次法を今回の単純なGodunov反復と同一視しません。

- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf; review_level=full-text
著者公開PDFの302–305頁、式(1)–(6),(9),(12),(15)の界面幾何・囲まれた質量の誤差・体積率の保存を参照。本教材は内部を負とするため符号規約を反転。CLSVOFや二相流の原著実験は実行していません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
