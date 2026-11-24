# 分散媒質の浅い入射角と長時間PML / Long-time grazing PML in a dispersive medium

https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/

## 日本語

[保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-grazing/#dispersive-grazing-pml) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#dispersive-grazing-pml)

### 方程式・問題の定義

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。

#### [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja)

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。

#### 分散媒質の浅い入射角と長時間PML

補助実行例 · 実行例の定義・検証式

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

### 厳密解・参照解

3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。

#### [浅角度分散波束の長時間・同格子孤立境界参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\widehat U^n(k_x)=M(k_x,\Delta t)^n\widehat U^0(k_x),\quad K_y=2\sin(k_y\Delta y/2)/\Delta y

均質Lorentz媒質はPML内まで連続し、ε∞=1、Δε=0.2、ω0=12、γ=0または0.005。Ez偏光の有限kx Gaussianはcarrierω=6、中心位相角80度。512/768/1024点とpeak6/9/12を同時細分化し、垂直対照は6、弱減衰細格子対照は12。最終時刻は700です。

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

#### 分散媒質の浅い入射角と長時間PML

3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja)

### 計算法

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja)

補助実行例

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

## English

[Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-grazing/#dispersive-grazing-pml) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#dispersive-grazing-pml-en)

### Equations and problem definitions

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.

#### [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en)

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation.

#### Long-time grazing PML in a dispersive medium

Supplementary execution example · Example definition or validation formula

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

### Exact and reference solutions

Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.

#### [Isolated same-grid reference for a long grazing dispersive packet](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\widehat U^n(k_x)=M(k_x,\Delta t)^n\widehat U^0(k_x),\quad K_y=2\sin(k_y\Delta y/2)/\Delta y

The homogeneous Lorentz medium continues through the PML: epsilon_inf = 1, delta_epsilon = 0.2, omega_0 = 12, gamma = 0 or 0.005. An Ez-polarized finite-kx Gaussian has carrier omega = 6 and central phase angle 80 degrees. Joint grid/layer refinement uses peaks 6/9/12 on 512/768/1024 cells; the normal control uses 6 and damped fine companion 12. Final time is 700.

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

#### Long-time grazing PML in a dispersive medium

Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en)

### Numerical methods

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en)

Supplementary execution example

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)
