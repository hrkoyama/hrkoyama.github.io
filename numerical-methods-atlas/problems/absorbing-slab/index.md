# 純吸収平板の離散座標輻射輸送 / Discrete-ordinate radiation transport through an absorbing slab

https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/

## 日本語

[光学的厚さ0.7の純吸収平板。32〜512セルのBeer–Lambert参照への空間誤差と、厳密セル内伝播を使う4〜32方向の角度誤差を分けた保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#radiation-transport) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#absorbing-slab)

### 方程式・問題の定義

定常離散座標輸送 μ∂xI=-κI、純吸収・指定流入。相対論的M1の式ではなく、既存一覧に同じ専用式はありません。

#### 純吸収平板の離散座標輻射輸送

補助実行例 · 実行例の定義・検証式

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

#### 輻射輸送：空間・角度収束と光子統計

補助実行例 · 実行例の定義・検証式

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

### 厳密解・参照解

純吸収・指定流入の平板に対する各方向の解析的な指数減衰と離散座標解を比較します。相対論的M1モーメント閉包とは別の輻射モデルです。 追加版は解析rayと連続角度参照を保持し、固定角度の空間誤差と厳密rayの角度誤差、流入・流出・体積吸収の収支を分けます。散乱や多次元閉包へ拡張しません。

#### 純吸収平板の離散座標輻射輸送

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja)

#### 輻射輸送：空間・角度収束と光子統計

16〜256セル・4〜64方向を別に収束させ、QUADPACK積分とE3を照合。64seed・1024/4096/16384光子で平均誤差、RMSE、二項標準偏差と95% Clopper–Pearson区間の実測被覆を記録します。全光子の出射＋吸収、正値性と離散フラックス収支を確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [輻射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja)

補助実行例

純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

光学的厚さ0.7の一様平板。正の半球から単位強度が入射し、逆向きの入射・散乱・内部輻射はゼロです。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

多重散乱、熱輻射、周波数再分配、動的媒質、輻射流体連成は未実装です。StamnesらのDISORTの全機能・安定化を再現したとは表示しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [輻射輸送：空間・角度収束と光子統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja)

補助実行例

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

定常一様平板、光学的厚さ.1/.7/3、正の半球から単位強度、逆入射・散乱・内部輻射0。フラックス基準の光子入射方向はpdf=2muです。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

区間被覆は有限の固定seedでの観測で、ちょうど95%の実測値や全seedの成功を保証しません。決定論的求積誤差を統計誤差へ含めず、多重散乱・周波数依存・熱輻射・輻射流体連成は未検証です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

## English

[Pure-absorption slab of optical depth 0.7: stored 32–512-cell spatial errors versus Beer–Lambert and a separate 4–32-ordinate angular sweep using exact cell propagation.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/#radiation-transport) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#absorbing-slab-en)

### Equations and problem definitions

Steady discrete-ordinate transport μ∂xI=-κI with pure absorption and specified inflow, distinct from relativistic M1 and absent as a dedicated registry equation.

#### Discrete-ordinate radiation transport through an absorbing slab

Supplementary execution example · Example definition or validation formula

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

#### Radiation transport: space/angle convergence and photon statistics

Supplementary execution example · Example definition or validation formula

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

### Exact and reference solutions

Compare discrete ordinates with analytic directional exponential attenuation through a purely absorbing slab with specified inflow. This differs from relativistic M1 moment closure. The companion retains analytic rays and a continuum-angle reference, separating fixed-ordinate spatial error, exact-ray angular error and inflow/outflow/volume-absorption balance. It does not extend to scattering or multidimensional closures.

#### Discrete-ordinate radiation transport through an absorbing slab

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en)

#### Radiation transport: space/angle convergence and photon statistics

Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en)

Supplementary execution example

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

A uniform slab of optical depth 0.7 receives unit intensity over the positive hemisphere, with zero reverse inflow, scattering and emission.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [Radiation transport: space/angle convergence and photon statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en)

Supplementary execution example

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

Steady uniform slab, optical depths .1/.7/3, unit incoming positive-hemisphere intensity, no reverse inflow/scattering/emission. Incoming photon directions for a flux estimator have density 2mu.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Coverage is observed over finite fixed seeds; neither exactly 95% empirical coverage nor all-seed success is guaranteed. Keep deterministic quadrature error separate from statistical error. Multiple scattering, frequency dependence, thermal emission and radiation hydrodynamics are unvalidated.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
