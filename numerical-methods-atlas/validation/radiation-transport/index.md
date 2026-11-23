# 純吸収平板の離散座標放射輸送

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-algorithm)

正のGauss–Legendre離散方向と1次風上有限体積の空間行進を使います。角度誤差だけを分ける系列では、一定セル内を指数関数で正確に伝播します。

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![純吸収平板の離散座標放射輸送：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純吸収平板の離散座標放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) (`absorbing-slab`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-validation)

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

光学的厚さ0.7の一様平板。正の半球から単位強度が入射し、逆向きの入射・散乱・内部放射はゼロです。

## 採用した計算法

正のGauss–Legendre離散方向と1次風上有限体積の空間行進を使います。角度誤差だけを分ける系列では、一定セル内を指数関数で正確に伝播します。

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

## 比較・検証

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

## 確認の限界

多重散乱、熱放射、周波数再分配、動的媒質、放射流体連成は未実装です。StamnesらのDISORTの全機能・安定化を再現したとは表示しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "ray_max_error": 0.012314628761692092,
    "spatial_flux_error": 0.0011230547235325794,
    "angular_flux_error": 4.558353694505968e-12,
    "balance_error": 9.769962616701378e-15,
    "refinement_ratio": 0.06309366514102617
  },
  "checks": {
    "ray_max_error": true,
    "spatial_flux_error": true,
    "angular_flux_error": true,
    "balance_error": true,
    "refinement_ratio": true,
    "positive_bounded_intensity": true,
    "angular_refines": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
出版社HTMLの書誌・抄録と基本の輸送式を確認。離散座標の背景として引用し、本例はDISORT全機能の実装ではありません。

- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
一般化指数積分の積分表示を公式資料で確認。年は確認年。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Discrete-ordinate radiation transport through an absorbing slab

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-algorithm)

Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Discrete-ordinate radiation transport through an absorbing slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en#radiation-transport-en-validation)

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

A uniform slab of optical depth 0.7 receives unit intensity over the positive hemisphere, with zero reverse inflow, scattering and emission.

## Adopted numerical method

Use positive Gauss–Legendre ordinates and first-order upstream finite-volume marching. A separate angular-error sweep uses exact exponential propagation within each constant cell.

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

## References and validation

With 32–512 cells, check all ray intensities, spatial flux error, positivity and discrete absorption balance. A separate 4–32-ordinate sweep compares exit flux with the analytic 2pi E3(tau) representation.

## Limits

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

## Stored measurements and decisions

```json
{
  "metrics": {
    "ray_max_error": 0.012314628761692092,
    "spatial_flux_error": 0.0011230547235325794,
    "angular_flux_error": 4.558353694505968e-12,
    "balance_error": 9.769962616701378e-15,
    "refinement_ratio": 0.06309366514102617
  },
  "checks": {
    "ray_max_error": true,
    "spatial_flux_error": true,
    "angular_flux_error": true,
    "balance_error": true,
    "refinement_ratio": true,
    "positive_bounded_intensity": true,
    "angular_refines": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
Publisher HTML bibliography, abstract and base transfer equation checked; cited as discrete-ordinate background, not full DISORT implementation.

- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
Official integral representation of the generalized exponential integral checked; year denotes access year.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
