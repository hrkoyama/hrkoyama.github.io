# Oblique s/p incidence on a Lorentz-dispersive slab

One small fixed educational case. Actual completion is recorded by the
immutable verification receipt and results/result.json, not by prototype
module labels. Historical UNEXECUTED docstrings remain byte-preserved where
the qualified original kernels are intentionally unchanged.

```sh
python -m pytest -q
python run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-figures
```

Runtime/test pins: NumPy2.0.2, SciPy1.14.1 and pytest8.3.5 only. Plotting
additionally uses Matplotlib and reads saved fields; it never evolves them.
The shared public group deadline remains120seconds for pytest plus main.
Use fresh output; preserve failures and never retry or extend a window
automatically. All complete candidates are saved before later diagnostics.

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

The first T = 36 experiment completed 12 evolutions with 53/57 scientific gates passing. Retain all three s-polarized tail failures and the finest s RTA failure. The revised fixed T = 60 window must satisfy every original criterion. Gaussian tails are noncompact; diagnostics still decide window and cap adequacy.

## 日本語

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

初回T36は12進行を完了し57判定中53合格。s偏光の末尾3件と最細RTA1件の未達を全て保持します。新しい固定窓T60で元の全基準を再検査し、Gaussianの非コンパクト尾とcapの影響は診断で判断します。

## References and retained first experiment

Primary-source URLs and exact selected reading scopes are in cases.json.
Original Yee, Berenger and Roden-Gedney papers are not claimed as read.
The existing r6 FDTD code/eight inputs/108 tests remain unchanged.
The old165-component result alone did not complete these full candidates.

history/first-full-main contains compact scientific results and old
changed-source texts. All complete original source and failed native NPZ
arrays remain in the retained private attempt. This compact public history
does not claim to contain every failed native field.
