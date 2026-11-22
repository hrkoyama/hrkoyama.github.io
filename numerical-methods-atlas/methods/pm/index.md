# FFT particle–mesh forces / FFT粒子格子力

Status: educational-example

Deposit periodic 3D particle mass by CIC, FFT-solve Poisson after removing mean density, and interpolate acceleration back with matched CIC. The example uses the continuum Fourier symbol −4πG/k² and spectral derivatives.

周期3次元粒子の質量をCICで格子へ割り当て、平均密度を除いたPoisson方程式をFFTで解き、格子加速度を同じCICで粒子へ戻す。公開例は連続Fourier記号 −4πG/k² とスペクトル微分を使う。

A static PM-only example without direct short-range correction. CIC smoothing, grid anisotropy, aliasing and finite resolution remain; the continuum Fourier Green function is not the inverse symbol of a finite-difference Laplacian. No P3M, TreePM split, Ewald, PME/SPME, expansion or time integration is included.

Other names: PM法, particle mesh, 粒子格子法, particle mesh method


## 条件と確認範囲 (ja)

problem: 平均密度を差し引いた、周期粒子系の格子上重力Poisson問題と粒子加速度。

variant: 8点CIC割当て/補間、連続k²記号のFFT Poisson、k=0固定、スペクトル加速度。

use_when:
- 周期系で粒子と格子の結合、質量保存、零モードを調べるとき。
- 単一Fourierモードにより重力の符号・ゲージを確かめるとき。

avoid_when:
- 孤立境界や格子以下の近接力をこのまま必要とする場合。
- この例をEwald/PME/SPMEの誤差制御付き置換とみなす場合。

assumptions [specified]:
- 立方体の周期箱、正かつ有限の粒子質量、有限位置、立方n³格子でn≥4、L>0を使う。位置は各軸でLを法として折り返す。
- CICは8隅への積線形重みで密度を作り、格子体積で割る。粒子へ戻す補間も同じ重み。CIC窓の逆補正は行わない。
- ∇²φ=4πG(ρ−平均ρ)、φ̂(0)=0。非零モードは −4πG/k²、加速度は−∇φ。偶数格子の微分は各軸の対応Nyquistモードを零にして実の奇作用素を保つ。
CIC、Green関数、重力符号、零・Nyquistモードをコードで確認した。

units [specified]:
pm_accelerationはG=1固定の無次元例。L・位置には同じ長さ単位を使い、ρは質量/L³、φはGM/L、加速度はGM/L²に対応する。下位関数periodic_poissonのみ正のgravityを指定できる。
上位G=1と下位gravity指定を区別した。

boundary_conditions [specified]:
全方向周期、箱長L。平均密度を除くことで周期Poissonの整合性を満たし、k=0を零に固定してポテンシャルの加法定数を選ぶ。孤立境界の力とは同一問題でない。
周期折返し・平均除去・ポテンシャルのゲージを確認した。

limitations [specified]:
格子以下の近接力を直接補正しないPMのみの静的例。CIC平滑化、格子異方性・aliasing・有限解像度があり、連続Fourier Green関数を有限差分Laplacianの離散逆作用素と混同しない。P3M・TreePM分割・Ewald・PME/SPME・宇宙膨張・時間積分は含まない。
PMのみ・静的・格子有限解像度の範囲を明記した。

Review: cic_deposit/interpolate、periodic_poisson、pm_accelerationと、質量/周期折返し、正弦密度のφと引力符号、平均除去・ゲージ、CIC自己力・全内力の既存検査を読んだ。今回は再実行していない。

Not checked:
- 3次元のPM窓・aliasing・格子異方性の新しい定量誤差解析。
- 直接和やEwaldと異なる境界を揃えた独立の固定実行例、時間積分。

Evidence:
- cic_deposit, cic_interpolate, periodic_poisson, pm_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- periodic CIC mass/wrap, sinusoid/gauge/mean and matched-CIC self/total-force tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py

References:
- [formulation / primary-research] Eastwood, J. W. & Hockney, R. W. (1974). Shaping the force law in two-dimensional particle-mesh models. — https://doi.org/10.1016/0021-9991(74)90044-8
  PMのCICを含む割当てと格子の力の誤差に直接関係する一次研究。2次元の論文であり、本実装の3次元Green関数を検証する文献とはしない。
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata returned by web search; full text not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999174900448

## Conditions and review scope (en)

problem: Periodic particle gravity through the mesh Poisson problem for density contrast.

variant: Eight-vertex CIC deposition/interpolation, FFT Poisson with continuum k², fixed zero mode and spectral acceleration.

use_when:
- Studying particle/mesh coupling, mass conservation and the zero mode in a periodic system.
- Checking gravitational sign and gauge with a single Fourier mode.

avoid_when:
- Direct use for isolated boundaries or accurately resolved subgrid pair forces.
- Treating this example as an error-controlled Ewald/PME/SPME substitute.

assumptions [specified]:
- A cubic periodic box, positive finite particle masses, finite positions, cubic n³ mesh with n≥4 and L>0; coordinates wrap modulo L in every axis.
- CIC deposits to eight vertices with product-linear weights divided by cell volume; interpolation uses the same weights. No CIC-window deconvolution is applied.
- ∇²φ=4πG(ρ−meanρ), with φ̂(0)=0. Nonzero modes use −4πG/k² and acceleration is −∇φ. On even meshes, each derivative zeroes its own-axis Nyquist mode to retain a real odd operator.
Checked CIC, Green function, gravitational sign and zero/Nyquist modes in code.

units [specified]:
pm_acceleration is a dimensionless G=1 example. L and positions share a length unit; density, potential and acceleration scale as M/L³, GM/L and GM/L². Only the lower-level periodic_poisson accepts a positive gravity parameter.
Distinguished top-level G=1 from lower-level gravity selection.

boundary_conditions [specified]:
Periodic in all directions with box length L. Mean removal enforces periodic-Poisson compatibility, while zeroing k=0 fixes the additive potential gauge. This is not the isolated-force problem.
Checked periodic wrapping, mean removal and potential gauge.

limitations [specified]:
A static PM-only example without direct short-range correction. CIC smoothing, grid anisotropy, aliasing and finite resolution remain; the continuum Fourier Green function is not the inverse symbol of a finite-difference Laplacian. No P3M, TreePM split, Ewald, PME/SPME, expansion or time integration is included.
Specified PM-only static scope and finite grid resolution.

Review: Inspected cic_deposit/interpolate, periodic_poisson, pm_acceleration and existing mass/wrapping, sinusoidal potential/attraction sign, mean/gauge, CIC self-force and total-internal-force tests; no rerun.

Not checked:
- New quantitative 3D PM-window, aliasing or grid-anisotropy analysis.
- An independent fixed run matching boundaries to direct/Ewald references, and time integration.

Evidence:
- cic_deposit, cic_interpolate, periodic_poisson, pm_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- periodic CIC mass/wrap, sinusoid/gauge/mean and matched-CIC self/total-force tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py

References:
- [formulation / primary-research] Eastwood, J. W. & Hockney, R. W. (1974). Shaping the force law in two-dimensional particle-mesh models. — https://doi.org/10.1016/0021-9991(74)90044-8
  Directly supports PM assignment/CIC and mesh-force error context; this 2D paper is not a validation of the implemented 3D Green function.
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata returned by web search; full text not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999174900448


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py

- Reference: https://doi.org/10.1016/0021-9991(74)90044-8 — Primary PM charge-sharing/CIC and Fourier-force-shaping research in 2D; context for assignment and mesh-force errors, not a derivation of this 3D gravity implementation.

Common execution records: [{"id": "periodic-particles", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-particles-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-particles-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
