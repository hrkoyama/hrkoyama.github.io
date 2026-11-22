# Particle/transport convergence / 粒子・輸送の収束と保存則

Six small experiments deepen the existing Ewald/SPME, 2D FMM, cold PIC,
homogeneous collision and absorbing-slab examples. Independent references,
shared numerical paths, truncation error, approximate conservation and
independent-seed uncertainty are distinguished. The old `particles` edition,
its inputs, tolerances and successful records remain unchanged. No quantum
calculation is run.

## Run / 実行

Use Python 3.12. Routine execution needs exactly the three pinned dependencies
in `requirements.txt`: NumPy 2.0.2, SciPy 1.14.1 and pytest 8.3.5.

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output results
```

Choose a new or empty output directory. The runner retains `result.json`, six
case JSON files and six measurement CSV files. The report records the actual
environment, input SHA, every check and metric, raw per-seed measurements,
reference diagnostics and termination reason. Returned cases are saved incrementally;
an unexpected exception may stop before the final `result.json`. Exit status is
0 when all declared checks pass,
1 for completed failed checks, and nonzero for invalid inputs, existing
nonempty output or an exhausted budget. Passing a coarse/failure-control
check means its inaccuracy was detected; it does not certify that coarse
approximation as accurate.

Inputs and criteria were locked before the first primary or reference run.
`protocol-history.json` records that sequence; `longrange-design.json` and
`kinetic-design.json` retain the reviewed designs. Fixed input SHA256:

```text
c90c95405e1622affc84c3feaffc50a7f5599fc868741823e26c7840eeda288b
```

This runner accepts that fixed recipe. It is not an arbitrary-allocation
interface. The post-import wall-time budget is 105 seconds, excluding package
installation and plotting. The development run completed in approximately
0.73 seconds after imports on Python 3.12.16; this is an observation, not a
portable speed guarantee. The 75 scientific, provenance and CLI tests passed
with warnings treated as errors.

Plotting is optional and reads saved JSON only; `plot.py` imports no solver or
experiment module and performs no reference regeneration:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results results/result.json --output results
```

The optional plotting dependency is Matplotlib 3.9.4. Six two-panel PNGs use
the case IDs as filenames. Logarithmic display floors do not alter saved
measurements. See `cases.json` for detailed Japanese/English assumptions,
equations, references, actual source-review scope and limitations.

## Scope and reference independence

- **Ewald:** The same asymmetric neutral eight-charge cubic cell, 3D periodic
  tin-foil boundary, Coulomb constant one. Full energy and all 24 force
  components are checked against a separately coded Gaussian/theta integral,
  with no calls to the primary Ewald, real-space or reciprocal helpers.
  Combined quadrature/theta/image/switch refinement and the separate
  integration-upper-limit change 32 to 40 are recorded. The latter is measured
  sensitivity, not a rigorous tail bound for arbitrary configurations.
  Split parameters, separate real/reciprocal cutoffs, translation,
  permutation, net force and three energy derivatives are checked.
- **SPME:** Essmann-type B-spline, energy-gradient SPME, meshes 16/24/40,
  orders four/six and three translation phases. Real/self terms share the
  primary Ewald path, which is explicitly checked against theta integration.
  Charge partition, its derivative, total charge, energy derivatives and
  phase errors are measured. This finite-mesh variant has **nonzero net
  force**; energy consistency is not exact momentum conservation. It is not
  the original Lagrange-interpolation PME implementation.
- **FMM:** Uniform-tree free-space **2D `-log(r)`**, with orders 2/4/8/12 and
  depths two/three. A separately coded Cartesian pair loop supplies potential
  and field; closed two-source and finite regular-polygon identities add
  analytic probes. Record order/depth error, actual far translations,
  rotation/translation error and charge-weighted net force. Fixed-order depth
  changes can be nonmonotone. There is no 3D Coulomb, adaptive/periodic FMM,
  exact action/reaction or asymptotic-complexity validation.
- **PIC:** Cold 1D periodic electrostatic plasma, amplitude .001 and final
  time 1.6. Mesh refinement fixes 2048 particles and dt=.004; time refinement
  fixes 32 cells and 256 particles. The continuum linear mode is `cos(t)`.
  DOP853 is independent **only as a time integrator of the same CIC RHS**,
  with reference maximum-step sensitivity measured. Matched CIC deposition/
  gathering and a skew spectral field conserve charge and momentum much
  more tightly than energy. Resolved-mode Gauss consistency excludes the
  Nyquist null mode, whose charge is separately reported. Random-load
  time-zero noise is a separate 64-seed study: actual CIC grid-mode power
  has expectation `(2+cos(2*pi/grid))/(3*N)`. It does not validate noise after
  long plasma evolution or warm/electromagnetic/relativistic PIC.
- **DSMC collision component:** Homogeneous equal-mass isotropic Maxwell
  scattering, N=16/64/256 and 64 independent seeds. Pair collisions conserve
  momentum and energy; rounds have no calibrated physical time. With zero
  total momentum and `sum|v|^2=3*N`, equilibrium has
  `energy/[1.5*(N-1)] ~ Beta(1.5,1.5*(N-2))` and
  `E[vx^4]=9*(N-1)/(3*N-1)`. Gaussian projection into the zero-momentum
  subspace and radius normalization supplies independent equilibrium samples.
  For `D=mean(vx^2)-[mean(vy^2)+mean(vz^2)]/2`, the two-beam initial condition
  has `E[D_round]=3*[(N-2)/(2*(N-1))]^round`. CDF/moment/anisotropy uncertainty
  uses **seed-level** standard errors; particles within a seed are correlated.
  Finite-N Maxwell bias is distinct from sampling error. The fixed 64-seed
  checks do not guarantee all seeds or give iid-particle KS p-values. Spatial
  transport and hard-sphere velocity-dependent collision selection are absent.
- **Radiation:** Steady pure-absorption slab, optical depths .1/.7/3.
  Separate space refinement against fixed exact rays from angular refinement
  against a characteristic flux integral. Adaptive QUADPACK and `E3` agree
  independently of upstream marching and Gauss-Legendre rays. Analog photons
  sample incident-flux directions `mu=sqrt(U)` and exponential optical paths:
  survival probability is `2*E3(tau)` and outgoing flux is `pi*survival`.
  Store seed-level means, RMSE, exact binomial deviations, Clopper-Pearson
  intervals, observed coverage and absorbed/escaped count balance. Fixed-seed
  coverage is a diagnostic, not an all-ensemble guarantee. No scattering or
  full DISORT implementation is claimed.

Observed development diagnostics illustrate the distinctions: Ewald maximum
force error was `1.24e-14`; finest SPME worst-phase force error `7.86e-6` with
net force `1.92e-5`; FMM maximum field error `1.31e-4` with absolute net force
`1.16e-4`. PIC maximum relative energy drift over all declared mesh/time runs
was `9.97e-3`, while charge and momentum errors were below `8e-16` and `7e-19`.
Collision relative energy error was below `8e-16`; the largest finite-N CDF
bias from the Maxwell limit was `.0138`. Slab balance error was below `8e-16`
and minimum observed 95% interval coverage was `.9375`. These observations do
not replace the unrounded criteria or certify arbitrary inputs.

## 日本語

既存6例の独立参照・収束・保存量・統計誤差を深めた小規模な固定入力版です。
通常依存は上記3つだけで、75テストと科学計算CLIを警告エラー化で確認しました。
入力・判定基準は初回計算前に固定し、旧配布版の値や公差を変更していません。
出力先は新規または空のディレクトリを使います。保存結果の照合、今回の固定6例の
再実行、任意条件の大規模な収束検証は別です。量子計算は含みません。

Ewaldの独立theta積分は全エネルギー・全力を返す別実装です。積分上限の感度を
任意配置の厳密な裾誤差保証とは呼びません。SPMEはBスプライン型で、実空間・自己項は
Ewaldと共有します。有限格子では合力が残るため、エネルギー勾配との一致を厳密な
運動量保存へ読み替えません。FMMは自由空間2次元対数核だけで、木の深さに対する
単調収束・厳密な作用反作用・3次元や計算量スケーリングは未検証です。

PICでは同じ粒子数で格子だけを変える系列と、同じ格子・粒子数で時間刻みだけを
変える系列を分けます。DOP853は同じCIC右辺の時間参照であり、独立空間実装では
ありません。Gauss則の解像モードとNyquist零モード、電荷・運動量と有限のエネルギー
誤差、quiet-startと時刻0のrandom-load雑音を分けて記録します。

衝突例では有限N・運動量0の球面平衡をMaxwell極限と区別します。保存量は全履歴の
最大誤差、CDF・4次モーメント・異方性は独立seed間の標準誤差で確認します。
同一seed内の粒子を独立標本とせず、固定64seedの結果を全seedへ一般化しません。
輻射例では空間・角度誤差を分け、入射フラックスの重みで光子を発射します。
二項分布の厳密区間と実測被覆率を残し、被覆率やRMSEの観測を普遍的保証としません。

`plot.py`は保存済みJSONだけから6枚の図を作り、ソルバーや参照計算を起動しません。
詳しい式・単位・境界・一次文献と確認範囲は日英の`cases.json`を参照してください。

## Rights / 利用条件

The accompanying MIT license applies only to original Python source code.
Adapted kernels retain their copyright and attribution. Text, figures, fixed
inputs and numerical data retain separate conditions in
[LICENSING.md](https://hrkoyama.github.io/LICENSING.md) and
[Rights & AI policy](https://hrkoyama.github.io/rights/).
Libraries and third-party papers retain their own terms. No blanket permission
for non-code material or third-party sources is added.

MITはオリジナルPythonコードのみです。本文・図・固定入力・数値データ、依存ライブラリ、
第三者文献の条件を区別し、論文全文の監査や全アルゴリズムの再現を主張しません。
