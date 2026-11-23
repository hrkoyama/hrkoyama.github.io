# 温かいPICの線形Landau減衰 / Warm PIC linear Landau damping

https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/

## 日本語

[実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-warm-pic/#thermal-landau-damping) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#thermal-landau-damping)

### 方程式・問題の定義

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。

#### [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja)

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。

#### 温かいPICの線形Landau減衰

補助実行例 · 実行例の定義・検証式

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

### 厳密解・参照解

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

#### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-measurements)

半解析解 · 同じ問題の参照

D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

#### 温かいPICの線形Landau減衰

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja)

### 計算法

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja)

補助実行例

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)

## English

[Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/#thermal-landau-damping) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#thermal-landau-damping-en)

### Equations and problem definitions

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

#### [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en)

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope.

#### Warm PIC linear Landau damping

Supplementary execution example · Example definition or validation formula

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

### Exact and reference solutions

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

#### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-measurements)

Semi-analytic reference · Reference for the same problem

D(omega,k)=1+sum_s a_s[1+zeta_s Z(zeta_s)]/k²=0; e(t)=Phi(t)-integral_0^t s Phi(s)e(t-s)ds; Phi=exp[-(kt)²/2]cos(kut).

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

#### Warm PIC linear Landau damping

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en)

### Numerical methods

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en)

Supplementary execution example

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)
