# 純吸収平板の離散座標放射輸送 / Discrete-ordinate radiation transport through an absorbing slab

https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/

## 日本語

[光学的厚さ0.7の純吸収平板。32〜512セルのBeer–Lambert参照への空間誤差と、厳密セル内伝播を使う4〜32方向の角度誤差を分けた保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#radiation-transport) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#absorbing-slab)

### 方程式・問題の定義

定常離散座標輸送 μ∂xI=-κI、純吸収・指定流入。相対論的M1の式ではなく、既存一覧に同じ専用式はありません。

#### 純吸収平板の離散座標放射輸送

補助実行例 · 実行例の定義・検証式

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

### 厳密解・参照解

純吸収・指定流入の平板に対する各方向の解析的な指数減衰と離散座標解を比較します。相対論的M1モーメント閉包とは別の放射モデルです。

#### 純吸収平板の離散座標放射輸送

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja)

補助実行例

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

光学的厚さ0.7の一様平板。正の半球から単位強度が入射し、逆向きの入射・散乱・内部放射はゼロです。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

多重散乱、熱放射、周波数再分配、動的媒質、放射流体連成は未実装です。StamnesらのDISORTの全機能・安定化を再現したとは表示しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

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

### Exact and reference solutions

Compare discrete ordinates with analytic directional exponential attenuation through a purely absorbing slab with specified inflow. This differs from relativistic M1 moment closure.

#### Discrete-ordinate radiation transport through an absorbing slab

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en)

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
