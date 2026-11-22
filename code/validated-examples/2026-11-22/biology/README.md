# Nonlinear reaction–diffusion / 非線形反応拡散

Two small, deterministic 1D Schnakenberg experiments extend the earlier frozen onset test without changing that release. The first follows a finite-amplitude transient to **t=8**; the second follows a selected pattern to **t=100**. They share the existing `turing-schnakenberg` physical problem, rather than adding two independent model families. These adopted dimensionless coefficients are educational inputs, not a reproduction of Turing's or Schnakenberg's original numerical experiment, and not calibrated biology. No quantum calculation is performed.

既存の微小振幅・発生段階の凍結版を保持し、有限振幅の過渡（t=8）と選択した模様の近飽和（t=100）へ検証を進める小さな1D例です。物理問題は既存の `turing-schnakenberg` に再接続し、モデル数を重複加算しません。無次元係数は教育用に採用したもので、歴史的原著の数値実験や実生物の較正を再現したとは扱いません。量子計算は追加しません。

## Equations and selected symmetry / 方程式と選択対称性

On `0 <= x < 2*pi` with periodic boundaries,

```
u_t = 0.01 u_xx + 0.1 - u + u^2 v
v_t = 1.00 v_xx + 0.9     - u^2 v
u(x,0) = 1.0 + 0.08 cos(2x) + 0.010 cos(4x)
v(x,0) = 0.9 - 0.03 cos(2x) - 0.002 cos(4x).
```

The analytic IC, coordinates and output times are identical across methods and grids. The solution lies in a **reflection-even, pi-periodic invariant subspace**. A real cosine Fourier reference exploits this restriction; the primary FD code evolves the periodic grid. This is not a test of arbitrary phase perturbations, noise-driven wavelength selection, 2D spots, or general morphogenesis. No phase alignment is applied to errors.

解析的な初期値・座標原点・物理出力時刻を全手法・全格子で固定します。反射対称かつπ周期の不変部分空間を選択しており、cosine参照はこの限定を利用します。primaryは周期格子上で計算します。一般の位相安定性・乱数からの波数選択・2D斑点・形態形成全般は検証しません。誤差を小さくする位相合わせは行いません。

## Three separate error questions / 3種類の誤差を分離

1. **Primary method:** second-order centered FD in space. An FFT diagonalizes the **FD matrix**, whose eigenvalues are `-4*sin(pi*k/N)^2/dx^2`, not continuum `-k^2`. The temporal composition is exact FD diffusion half-step, implicit-midpoint reaction full-step, and exact FD diffusion half-step (Strang). Each local reaction equation uses a coupled2×2 Newton solve with a residual test and iteration cap. The method targets second order for smooth solutions; implicit midpoint is A-stable, not L-stable or unconditionally positivity preserving.
2. **Different space and time reference:** real cosine Fourier–Galerkin coefficients, continuum eigenvalues `-k^2`, and SciPy Radau IIA with an analytic Jacobian. Cubic `u^2*v` is evaluated/projected on `M=4*(K+1)>4K` periodic points, which exactly integrates retained cubic coefficients; quadratic-product3/2 padding would be insufficient. Compare K=32/64/96 and then tighten rtol/atol from2e-10/2e-12 to2e-12/2e-14. These are sensitivity measurements, not a rigorous global error bound.
3. **Time-only reference:** a separately assembled periodic FD matrix and nonlinear RHS, integrated by sparse-Jacobian Radau at the tight tolerance. This solves the **same FD semidiscretization** and therefore isolates splitting/time error; it is not an independent spatial reference. Use it to measure time convergence and the temporal contamination of the spatial series.

primaryは二次中心差分です。FFTはFD行列の対角化に用いるだけで、連続Fourier固有値へ置き換えません。Strang合成の反応部分にはimplicit midpointと局所2×2 Newtonを用います。全体の無条件正値性は仮定せず、全stepと受理された反応stageの最小濃度、Newton反復の最小値・残差を記録します。clipping・失敗時の黙った刻み変更はありません。

空間も時間も異なる参照は、cosine Fourier–Galerkinと5次Radauです。cubic投影にM>4Kを使い、K感度とODE公差感度を別に確認します。時間だけの参照は同じFD半離散方程式を別実装Radauで解いたものです。この2つを混同せず、primaryの空間誤差・時間誤差・参照の感度を分離します。

## Fixed protocol and first failure / 固定入力と初回不合格

All acceptance thresholds were written before the first numerical pilot. The first protocol (`inputs-initial.json`, SHA256 `aa97550f4d965505da9841d2e565b066a02e7af1d7585585e001bea0eb52accb`) used space-series h=.01 and time-series h=.1/.05/.025. It failed the time-error, time-contamination and observed-order checks. The nonlinear dynamics and independent reference already passed; coarse splitting error obscured the spatial error and sometimes cancelled it. The failed metrics are retained in `protocol-history.json`; the complete first result is retained in the project evidence directory.

The revised `inputs.json` changes **only temporal resolution**: space-series h=.00125 and time-series h=.0125/.00625/.003125. Every threshold, IC, physical time, grid, and reference setting is unchanged. SHA256: `375d70f40187400bf812dcd09d4beb0a8f7f3a79baf6a67c818b940bf82bbb84`. It is incorrect to call this an unchanged-first-attempt protocol. The longer run uses at most80,000 steps per spatial-series trajectory and a120-second total failure guard. The two fixed cases took about28 seconds on the development machine; hardware changes runtime.

受入基準は初回計算前に保存しました。粗い初回入力は時間誤差・空間系列への時間誤差混入・観測次数で不合格でした。失敗を残し、基準・格子・初期値・物理時刻・参照を変えず、時間刻みだけを細分しました。初回から変更なしとは表記しません。最大8万stepの系列と全体120秒の失敗guardを設けています。開発機では2例の全再計算が約28秒でした。

Raw errors are mean-absolute L1, RMS L2 and maximum L∞ **per species**, followed by the larger species error. They are normalized domain averages, not unnormalized sums or integrals. Every norm has its own two observed orders; the minimum must be>=1.7. Require reference spatial/tolerance sensitivities<=1e-5/1e-7 and their sum<=2% of the finest primary L∞ error. Require time contamination<=10% of the FD semidiscrete spatial L∞ error. Final absolute-error limits, positivity, Newton residuals and all other thresholds are in the input file. The observed near-pattern time orders are about1.75–2.02; the measurements are shown rather than declared exactly two.

Convergence norms and reference sensitivities are evaluated at each case's fixed final time; intermediate snapshot errors are separate evolution diagnostics.

L1は領域平均絶対値、L2はRMS、L∞は最大値を成分ごとに求め、悪い方を採用します。各ノルムの格子・時間次数を別に検査します。参照の空間/公差感度とprimary誤差の比、空間系列の時間誤差混入も合格条件です。近飽和例の実測時間次数は約1.75–2.02で、全てが厳密に2と丸めず表示します。

収束ノルムと参照感度は各例の固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

## Reaction balance and near-saturation / 反応収支と近飽和

The mean total concentration is **not conserved**:

```
d mean(u+v)/dt = a+b-mean(u)
S[n+1]-S[n] = h*(a+b-mean(u_midpoint)).
```

Each diffusion half-step preserves the mean. Accumulate the actual reaction midpoint source at every accepted step and compare with the total mean change. This checks a source/sink balance to Newton/roundoff precision; a coarse snapshot trapezoid integral is not used as its substitute. Finite concentrations and sampled positivity do not prove continuum positivity.

反応によりu+vの平均は保存しません。各反応midpointの源・吸込みを全stepで積算し、平均の変化と照合します。拡散半stepは平均を変えないので、Newton残差・丸めの精度で成立する収支です。粗い出力時刻の台形積分へ置き換えません。

The final pattern is called **near-saturated in the tested reference window**, using t=90→100 raw-field change<=1e-3, amplitude change<=1e-3, and the full physical PDE RHS<=1e-4 on1024 diagnostic points. The PDE residual uses Fourier second derivatives and the **unprojected** cubic reaction, so a small projected Galerkin RHS alone cannot hide omitted reaction modes. The projected RHS and the primary's separate FD RHS are also reported. The reference change is about5e-8 and full RHS about1.9e-9; the primary FD RHS decreases from about.0576 in the first coarse pilot to.00116 after refinement. These are different equations and diagnostics. This proves no exact steady state, nonlinear stability, or universal long-term attractor.

近飽和は参照の90→100の限定した窓で、場の変化・振幅変化・全PDE残差を用いて判定します。残差はFourier二階微分と**未投影**のcubic反応を用い、投影で高モードを落としたため小さく見えることを避けます。参照の全PDE残差・投影RHS・有限刻みprimaryのFD残差を区別して出力し、厳密定常解や非線形安定性の証明とは呼びません。

Amplitude, means and dominant mode are recorded across snapshots. The generated-harmonic ratio excludes initially seeded k=0,2,4; it measures the norm of k>=5 amplitudes divided by the k=2 amplitude (the first symmetry-allowed new mode is k=6). The nonlinear/linear diagnostic divides the L2 distance from a separate linearized matrix-exponential solution by the L2 nonlinear deviation from homogeneous equilibrium. It is **not** a numerical error: the late enormous ratio merely shows that the exponentially growing linearization has broken down.

新しい高調波の比は初期に存在するk4を除外し、k≥5の振幅ノルム/k2振幅で定義します（本対称性で最初の新モードはk6）。線形化との差は、非線形解の平衡からのL2偏差で正規化した診断値です。lateで巨大になる値は線形化の破綻を示し、数値誤差ではありません。

## Reproduce / 再実行

Python3.12 with the pinned NumPy/SciPy/pytest versions in `requirements.txt`; no network or private repository is needed for the numerical run. Set BLAS/OMP threads to1 for the bounded budget.

```
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error -m pytest -q -p no:cacheprovider
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error run.py --input inputs.json --output NEW_EMPTY_DIRECTORY
```

The tests use mathematical identities and a short finite-amplitude representative case, not repeated copies of the full fixed calculation. `run.py` executes both complete cases and every acceptance check. Optional `plot.py` requires matplotlib and reads **stored results only**; it does not run solvers. CSV/JSON retain convergence, reference refinement, reaction balance and representative profiles; a separate compact snapshot array supplies all plotted times. Array contractions use NumPy einsum without BLAS to avoid an observed NumPy2.0/macOS matmul floating-status warning; floating-point warnings are not suppressed.

To redraw the figures from an existing result, install the separately pinned plotting requirements and run:

```
python -m pip install -r requirements-plotting.txt
python plot.py --results NEW_EMPTY_DIRECTORY/result.json --output FIGURE_DIRECTORY
```

pytestは独立な数式・小さい代表過渡・失敗guardを検査し、全固定入力の長い反復を重複しません。全2例の受入判定はrun.pyと公開追試で実施します。任意のplot.pyは保存結果だけを読み、計算を再実行しません。matplotlibは図の生成用で数値追試の必須依存ではありません。

図の再描画は上記の別ファイル `requirements-plotting.txt` で依存を固定し、既存のresult.jsonを指定します。

## Sources and rights / 一次資料と権利

Full bibliographic details and exact reading scope are in `cases.json`: Turing1952 (selected original sections6–7), Schnakenberg1979 (official bibliography and publisher-indexed abstract; full text unavailable), Strang1968 (original pp.510–512), Hairer's author-hosted lecture (midpoint/order/splitting), and official versioned SciPy1.14.1 Radau documentation. Historical motivation, adopted equations, original algorithm implementation and numerical evidence are distinct. No article PDF or third-party code is redistributed. `LICENSE` applies to original software code only; prose/translations/inputs/figures/data/results follow the site's separate conditions.

書誌と実際の閲覧範囲はcases.jsonに日英で記録します。歴史的出典・採用モデル・独自実装・今回の数値検証を区別し、原著PDFや第三者コードは再配布しません。MITの対象は独自ソフトウェアコードのみで、本文・翻訳・入力・図・データ・結果にはサイトの別条件が適用されます。
