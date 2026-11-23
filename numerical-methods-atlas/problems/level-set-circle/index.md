# レベルセットで表した円の移流 / Advection of a level-set circle

https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/

## 日本語

[実際の128²レベルセット場から抽出した円のゼロ等値線。左は平行移動、右は偏心円の一周回転。解析界面と移流単独・単純な再初期化ありを比較します。VOF計算ではなく、面積保存を補正していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#level-set-circle)

### 方程式・問題の定義

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

#### [レベルセット界面の移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja)

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi<0\;\text{inside},\quad\phi>0\;\text{outside}
$$

$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$

ゼロ等値線で界面を表す非保存形の移流式。円の平行移動・剛体回転を検証し、VOFの体積率輸送と区別します。

#### レベルセット円の2D平行移動：界面・面積・再初期化

補助実行例 · 実行例の定義・検証式

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

#### 偏心したレベルセット円の2D剛体回転

補助実行例 · 実行例の定義・検証式

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

### 厳密解・参照解

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

#### [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja)

解析解 · 同じ問題の参照

phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.3+0.2*t,0.35+0.1*t).

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

#### [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja)

解析解 · 同じ問題の参照

phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.5,0.5)+R(2*pi*t)(0.18,0).

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

#### レベルセット円の2D平行移動：界面・面積・再初期化

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja)

#### 偏心したレベルセット円の2D剛体回転

解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja)

### 計算法

専用の2D ENO2／Heunレベルセット移流。任意選択の単純なGodunov再初期化による面積変化も保存し、VOF実装を割り当てません。

- [レベルセット法](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [レベルセット円の2D平行移動：界面・面積・再初期化](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja)

補助実行例

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)
- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)

#### [偏心したレベルセット円の2D剛体回転](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja)

補助実行例

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)
- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)

## English

[Zero contours extracted from actual128² level-set fields: translation(left) and an off-center full rotation(right). Compare analytic interfaces against advection alone and simple redistancing. This is not a VOF calculation, and no area correction is applied.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#level-set-circle-en)

### Equations and problem definitions

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

#### [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en)

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi<0\;\text{inside},\quad\phi>0\;\text{outside}
$$

$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$

Nonconservative transport of an implicit zero-contour interface. Dedicated circle translation and rigid rotation distinguish this from VOF fraction transport.

#### 2D level-set circle translation: interface, area and redistancing

Supplementary execution example · Example definition or validation formula

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

#### 2D rigid rotation of an off-center level-set circle

Supplementary execution example · Example definition or validation formula

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

### Exact and reference solutions

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

#### [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en)

Analytic reference · Reference for the same problem

phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.3+0.2*t,0.35+0.1*t).

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

#### [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en)

Analytic reference · Reference for the same problem

phi(x,y,t)=sqrt((x-cx(t))^2+(y-cy(t))^2)-0.15; c(t)=(0.5,0.5)+R(2*pi*t)(0.18,0).

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

#### 2D level-set circle translation: interface, area and redistancing

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en)

#### 2D rigid rotation of an off-center level-set circle

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en)

### Numerical methods

Dedicated2D ENO2/Heun level-set advection. Optional simple Godunov redistancing retains measured area changes; no VOF implementation is assigned.

- [Level-set method](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [2D level-set circle translation: interface, area and redistancing](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en)

Supplementary execution example

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)
- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)

#### [2D rigid rotation of an off-center level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en)

Supplementary execution example

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/level-set/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py)
- [/code/validated-examples/2026-11-23/level-set/level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py)
- [/code/validated-examples/2026-11-23/level-set/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py)
- [/code/validated-examples/2026-11-23/level-set/test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py)
