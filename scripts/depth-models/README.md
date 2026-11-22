# Lightweight biological, stochastic and thermostat checks / 軽量な生物・確率・温度制御の検証

Original educational implementations in `models.py`; NumPy supplies array arithmetic and random draws. SciPy supplies separate references (`ndtr`, matrix exponential, discrete Lyapunov solve and DOP853), rather than the implemented Metropolis, BAOAB, finite differences or RK4 steps.

`models.py` は独自の教育用実装です。NumPyは配列と乱数、SciPyは独立した参照評価に使用します。原著のすべての計算や実験データを再現する教材ではありません。

```sh
python -m pip install -r requirements.txt
python -m pytest -q -p no:cacheprovider test_models.py
python run.py --input inputs.json --output output
# One lightweight case / 1例だけ
python run.py --input inputs.json --case gaussian-mcmc --output mcmc-output
# Optional plotting of stored records only / 保存記録だけを図示
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

Choose a new or empty output directory. Exit 0 means all requested numerical criteria passed; exit 1 means a numerical criterion failed; exit 2 means invalid input or an execution error. No network is used by the runner. Package installation is separate. `result.json` records each decision, metrics, table rows, the complete input SHA-256, environment and measured runtime; one CSV accompanies each case. Runtime fields vary between machines. MIT applies only to original implementation code. Explanatory text/translations, figures, inputs, numerical data and generated output have separate conditions under [LICENSING.md](https://hrkoyama.github.io/LICENSING.md) and the [published rights guide](https://hrkoyama.github.io/rights/); no new blanket reuse license is granted. References and dependencies retain their own conditions. No third-party paper is bundled.

出力先は新規または空のフォルダにします。終了コード0は指定した数値基準の全合格、1は数値判定の不合格、2は入力・実行エラーです。実行中のネット接続は不要です。`result.json` には判定、実測値、表、入力SHA-256、環境、実行時間を保存し、各例にCSVを出力します。実行時間は環境で変わります。MITは自作の実装コードだけに適用します。解説本文・翻訳、図、入力・数値データ・生成出力は `LICENSING.md` と公開の利用条件に従う別対象で、新しい一括許諾は追加しません。文献・依存ライブラリはそれぞれの条件を保持します。

## 1. Gaussian Metropolis / Gaussian標的のMetropolis法

Sample the dimensionless standard normal density with a symmetric Gaussian random-walk proposal. Thirty-two chains start at dispersed positions. Each uses a separate `SeedSequence.spawn` PCG64 stream; the master seed, burn-in, retained budget and proposal width are fixed in `inputs.json`. Compute mean/variance and the empirical CDF against the analytic Gaussian CDF. The sample-budget table measures RMSE of individual-chain mean estimates over the same fixed ensemble. Its observed decrease is not a theorem for every seed.

The mean-observable ESS uses the pooled, mean-centered within-chain autocovariance (FFT, denominator n) and Geyer's initial-positive paired sequence starting with gamma_0+gamma_1. We floor tau at one, conservatively excluding antithetic ESS above the raw count. Classical split-Rhat is reported alongside ESS; it is not rank-normalized Rhat or a proof of mixing. A separate stationary AR(1) experiment checks the diagnostic against exact tau=(1+rho)/(1-rho); the theoretical geometric ACF also tests the pairing identity to rounding accuracy. Fixed-seed statistical bounds do not promise a fixed false-positive rate or success for all seeds, targets or dimensions.

無次元標準正規分布を対称Gaussian提案で標本化します。32連鎖の初期値を分散させ、連鎖ごとに独立したPCG64疑似乱数ストリームを用います。平均・分散・CDF、標本予算を変えた連鎖平均のRMSE、初期正列の自己相関時間・ESS、古典的split-Rhatを記録します。ESSは平均という1つの観測量の診断で、混合の証明ではありません。既知のAR(1)自己相関時間とも比較します。固定seedと予算の検査であり、任意の分布や全seedでの保証ではありません。

## 2. Harmonic BAOAB / 調和振動子のLangevin温度制御

Use dq=p dt, dp=−omega²q dt−gamma p dt+sqrt(2 gamma T)dW, with mass and Boltzmann's constant one. BAOAB composes half force kick, half drift, exact Ornstein–Uhlenbeck momentum update, half drift and half force kick. Check independent replicas against (a) the analytic canonical Gaussian in (q,p) and exponential total-energy distribution and (b) the exact invariant covariance of the **discrete** linear stochastic map, solved by SciPy's discrete Lyapunov equation. The unit tests also check the explicit harmonic covariance diag(T/omega²,T(1−h²omega²/4)).

Finite-step momentum bias is real: configurational variance happens to be exact for this harmonic model, while momentum variance has an O(h²) bias. We test that deterministic bias across h=0.4,0.2,0.1 independently from finite-sample scatter; sampling errors need not decrease monotonically with h. The finite burn-in covariance deficit is evaluated with the exact map. Position autocorrelation is compared with both the discrete propagator and the continuous Langevin matrix exponential. The two CDFs and energy distribution refer to the finest step. No other thermostat, interacting particle system, molecular dynamics engine or long-time trajectory is certified.

質量とBoltzmann定数を1にした調和振動子をBAOABで進めます。正準分布の位置・運動量CDFとエネルギー分布、離散写像のLyapunov定常共分散、連続・離散の位置時間相関を分けて確認します。この調和モデルでは位置分散が正確でも運動量に刻み幅2次の偏りが残ります。刻み誤差の次数と標本のばらつきを区別し、burn-in後の過渡偏差も写像から算出します。Langevin法の限定例であり、他の温度制御法・一般分子系の検証には転用しません。

## 3. Scalar reaction–diffusion / スカラー反応拡散

On periodic x in [0,2pi), solve u_t=D u_xx+r u with u(0,x)=cos(kx), second-order centered differences and original RK4. The continuum Fourier solution exp((r−Dk²)t)cos(kx) measures **spatial** convergence. A separate time-step scan compares with the exact semidiscrete eigenvalue r−4D sin²(k dx/2)/dx², removing spatial error from the RK4 order measurement. Fixed N=16,32,64 shows second-order space error; a fixed N=16 time sequence shows fourth-order time error. This is a linear diffusion–reaction operator check, not a validated nonlinear front or biological model.

周期区間で線形反応拡散を中心差分とRK4で解きます。連続Fourier解を参照に空間収束、半離散の厳密な固有値を参照に時間収束を測り、空間2次・時間4次を分けて評価します。非線形の反応前線や実生物のモデル全体の検証ではありません。

## 4. Turing onset / Turing不安定性の発生段階

Adopt dimensionless Schnakenberg kinetics u_t=D_u u_xx+a−u+u²v, v_t=D_v v_xx+b−u²v. At a=0.1,b=0.9 the homogeneous fixed point is (1,0.9). Its reaction Jacobian is stable, while unequal diffusion (0.01,1) makes the selected k=2 mode grow. For the **linearized** PDE, compare original FD/RK4 evolution at N=32,64,128 with SciPy expm of the 2x2 continuum Fourier matrix. Measure spatial error and growth rate separately. A short nonlinear N=64 run retains positive concentrations and develops a small spatial pattern; compare it with the exact **semidiscrete linearized** solution to quantify the small-amplitude approximation. This verifies onset near one fixed point, not mature nonlinear morphology, wave-number selection from random noise, realistic biology, or Turing's original numerical experiment. Parameters are this atlas's fixed test, not values copied from the historical paper.

Schnakenberg型の2成分反応で、一様平衡は安定、異なる拡散係数を加えたk=2モードは不安定になる条件を固定します。線形化PDEは2×2 Fourier行列指数と照合し、空間収束と成長率を検査します。短い非線形計算では正濃度と小振幅パターンの成長を確認し、半離散の線形解との差を記録します。成熟した模様・任意の波数選択・実生物・原著の計算全体の再現は検証範囲外です。

## 5. FitzHugh–Nagumo excitation / 膜興奮の縮約モデル

Solve v'=v−v³/3−w+I, w'=(v+a−bw)/tau with a=0.7,b=0.8,tau=12.5. Start at the zero-current resting equilibrium. Apply I=0.8 from t=10 to20 and then allow recovery until t=80. Pulse boundaries are split exactly into autonomous segments for both implementations, avoiding artificial order reduction from a discontinuity inside an RK stage. Compare original RK4 at dt=0.1,0.05,0.025 against separately implemented SciPy DOP853 with tolerances 1e−11 and1e−13. Store the reference difference, error at every output time, observed order, peak voltage/time and final recovery distance. Times and voltages are dimensionless. This is an FHN/BVP-style reduced excitable ODE, not full Hodgkin–Huxley ion channels, a spatial axon, patient data or electrophysiological calibration.

無次元の2変数FHN型ODEに電流パルスを与え、興奮と休止状態への回復を確認します。パルスの境界で区間を明示的に分け、独自RK4と独立DOP853を照合します。時間3段階の全出力点誤差、参照公差への感度、ピークと回復距離を保存します。Hodgkin–Huxley全イオンチャネルや空間的な軸索、実測データの較正を実装したとは扱いません。

## Sources / 出典と確認範囲

Full bibliographic metadata, DOI/URL, roles and actual review scope are in `cases.json`. The Metropolis/Hastings/Geyer, BAOAB, Turing, Schnakenberg and FitzHugh sources are cited for their respective algorithms or model context. Access depth differs: publisher/official abstracts or metadata, selected original sections for the initial-positive sequence, the authors' BAOAB manuscript, and official SciPy API documentation. These are not claims of a complete audit of every original paper.

書誌・DOI・URLと実際の確認範囲は `cases.json` に保存します。抄録・書誌の確認、選択した原著箇所、著者稿、公式API資料を区別し、全文監査を一括で主張しません。
