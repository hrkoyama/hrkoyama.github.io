# Lorentz分散板へのs/p斜め入射

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Lorentz分散板へのs/p斜め入射

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

**使用手法**

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) (`fdtd`)
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) (`leapfrog`)
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) (`implicit-midpoint`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-algorithm)

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

- [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja) (`maxwell-lorentz`)

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。


**問題の図**

![Lorentz分散板へのs/p斜め入射：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-validation)

s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。

- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja) (`lorentz-oblique-sp`; 同じ問題の参照 · 解析参照)

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。
### 前提・単位・境界

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。

**編集上の補足**

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。

### 採用した計算法

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

### 比較・検証

s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。

### 確認の限界

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "completed_matched_pairs": 6,
    "completed_primary_and_vacuum_evolutions": 12,
    "spatial_dimensions": 2,
    "spatial_restriction": "Actual single-ky Yee evolution with both p electric ADE components.",
    "material_energy_included": true,
    "direct_absorption_not_defined_by_RT": true,
    "final_time": 60.0,
    "finite_window": "One final carrier period is checked; Gaussian tails remain noncompact.",
    "maximum_energy_budget_defect": 1.0729586483899446e-12,
    "maximum_vacuum_calibration_error": 2.7424705908990964e-13,
    "finest_complex_rt_errors": {
      "s": 0.011507167077779438,
      "p": 0.012023386314063115
    },
    "finest_RTA_errors": {
      "s": 0.004990411900537867,
      "p": 0.0022696015641971365
    }
  },
  "checks": {
    "fixed-reference-and-components-qualified": true,
    "lorentz-s-n960/finite": true,
    "lorentz-s-n960/closed-PEC-direct-work-budget": true,
    "lorentz-s-n960/vacuum-energy-budget": true,
    "lorentz-s-n960/nonnegative-material-work": true,
    "lorentz-s-n960/initial-slab-tail": true,
    "lorentz-s-n960/last-carrier-period-monitor-energy": true,
    "lorentz-s-n960/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n960/independent-direct-spectral-work-budget": true,
    "lorentz-s-n1920/finite": true,
    "lorentz-s-n1920/closed-PEC-direct-work-budget": true,
    "lorentz-s-n1920/vacuum-energy-budget": true,
    "lorentz-s-n1920/nonnegative-material-work": true,
    "lorentz-s-n1920/initial-slab-tail": true,
    "lorentz-s-n1920/last-carrier-period-monitor-energy": true,
    "lorentz-s-n1920/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n1920/independent-direct-spectral-work-budget": true,
    "lorentz-s-n3840/finite": true,
    "lorentz-s-n3840/closed-PEC-direct-work-budget": true,
    "lorentz-s-n3840/vacuum-energy-budget": true,
    "lorentz-s-n3840/nonnegative-material-work": true,
    "lorentz-s-n3840/initial-slab-tail": true,
    "lorentz-s-n3840/last-carrier-period-monitor-energy": true,
    "lorentz-s-n3840/independent-finite-window-vacuum-DTFT": true,
    "lorentz-s-n3840/independent-direct-spectral-work-budget": true,
    "s/finest-complex-rt": true,
    "s/finest-RTA": true,
    "s/refinement-n1920": true,
    "s/refinement-n3840": true,
    "lorentz-p-n960/finite": true,
    "lorentz-p-n960/closed-PEC-direct-work-budget": true,
    "lorentz-p-n960/vacuum-energy-budget": true,
    "lorentz-p-n960/nonnegative-material-work": true,
    "lorentz-p-n960/initial-slab-tail": true,
    "lorentz-p-n960/last-carrier-period-monitor-energy": true,
    "lorentz-p-n960/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n960/independent-direct-spectral-work-budget": true,
    "lorentz-p-n1920/finite": true,
    "lorentz-p-n1920/closed-PEC-direct-work-budget": true,
    "lorentz-p-n1920/vacuum-energy-budget": true,
    "lorentz-p-n1920/nonnegative-material-work": true,
    "lorentz-p-n1920/initial-slab-tail": true,
    "lorentz-p-n1920/last-carrier-period-monitor-energy": true,
    "lorentz-p-n1920/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n1920/independent-direct-spectral-work-budget": true,
    "lorentz-p-n3840/finite": true,
    "lorentz-p-n3840/closed-PEC-direct-work-budget": true,
    "lorentz-p-n3840/vacuum-energy-budget": true,
    "lorentz-p-n3840/nonnegative-material-work": true,
    "lorentz-p-n3840/initial-slab-tail": true,
    "lorentz-p-n3840/last-carrier-period-monitor-energy": true,
    "lorentz-p-n3840/independent-finite-window-vacuum-DTFT": true,
    "lorentz-p-n3840/independent-direct-spectral-work-budget": true,
    "p/finest-complex-rt": true,
    "p/finest-RTA": true,
    "p/refinement-n1920": true,
    "p/refinement-n3840": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/index.json

![保存したp偏光の実電場をky=4の周期y方向へ再構成した場。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

保存したp偏光の実電場をky=4の周期y方向へ再構成した場。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Meep developers (n.d.). Meep Materials documentation [accessed 2026-11-24]. https://meep.readthedocs.io/en/latest/Materials/; review_level=primary-official-documentation-selected-sections
Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
