# 平行平板Poiseuille流 / Plane Poiseuille channel flow

https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/

## 日本語

[保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#channel-poiseuille)

### 方程式・問題の定義

格子BGK・体積力・半格子壁を使う計算と、巨視的な定常非圧縮流路解を結びます。

#### [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

#### [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

### 厳密解・参照解

半格子bounce-back壁とGuo体積力を使う格子単位の放物線速度が解析基準です。参照解一覧の単位幅・G=1の流路とは駆動力と長さが異なります。

#### [粘性チャネル／Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poiseuille)

解析解 · 関連モデルの参照

u(y) = G y(1−y)/(2ν); G=1, ν=0.1

十分に発達した平面定常チャネル、no-slip、単位密度。−dp/dx=G、または体積力加速度G。

放物線形は共通ですが、計算は格子幅ny・目標最大速度0.01に応じた体積力、カードは単位幅・G=1・ν=0.1です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Guo外力](https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [中間壁バウンスバック](https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_lbm_channel_halfway_wall_refinement`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_lbm_channel_halfway_wall_refinement
```

## English

[Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#channel-poiseuille-en)

### Equations and problem definitions

Links the lattice-BGK/body-force/halfway-wall calculation to its macroscopic steady incompressible channel solution.

#### [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

#### [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

### Exact and reference solutions

The analytic standard is the lattice-unit parabola with halfway bounce-back walls and Guo body forcing. The library unit-width channel with G=1 uses a different length and drive.

#### [Viscous channel / Poiseuille](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poiseuille)

Analytic reference · Related-model reference

u(y) = G y(1−y)/(2ν); G=1, ν=0.1

Fully developed planar steady channel, no slip, unit density; −dp/dx=G or body acceleration G.

Both have parabolic profiles, but the computation uses lattice height ny and forcing for peak speed 0.01; the card uses unit width, G=1 and ν=0.1.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Guo forcing](https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Half-way bounce-back](https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_lbm_channel_halfway_wall_refinement`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_lbm_channel_halfway_wall_refinement
```
