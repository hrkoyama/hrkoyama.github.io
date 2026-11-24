# Mie scattering width of a two-dimensional dielectric cylinder

This is one small fixed educational example. The numerical inputs and all
acceptance criteria are bound before its first full execution. No parameters
or tolerances are selected from a successful result. NumPy 2.0.2, SciPy 1.14.1
and pytest 8.3.5 are the only required runtime/test dependencies.

```sh
python -m pytest -q
python run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-figures
```

The plot command additionally uses Matplotlib and reads saved numerical data;
it never executes a solver. It accepts either result.json or its directory.
The public verifier provides the unchanged shared 120-second group deadline.
Every complete candidate is saved before reference diagnostics. Failures and
partial states are retained; output must be fresh and there is no retry loop.

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.

Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution and a vacuum control at the five saved times, and compare scattering width and exterior fields with the cylindrical series.

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

Retain the first 99/100 qualification and its coarse-grid 2.771% error from two-point H collocation. Preserve the original diagnostic, add a separate four-point diagnostic and requalify against the unchanged 2% criterion.

## 日本語

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。

Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

The old r6 eight-input/108-test FDTD release and its scientific bytes are
unchanged. The earlier 165-component qualification is retained separately;
that result alone did not complete any of these three full candidates.
Primary-source URLs and the exact selected reading scope are in cases.json.
Original Yee, Berenger and Roden-Gedney papers are not claimed as read.
