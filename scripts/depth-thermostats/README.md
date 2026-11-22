# Small CSVR / Langevin comparisons — 小規模なCSVR・Langevin比較

Original educational code, three fixed cases, no network during execution, no quantum calculation. The original 2026-11-22 BAOAB model supplement remains unchanged.

独自の教育用コードと3つの固定ケースです。実行中のネットワーク接続や量子計算は不要です。既存の2026-11-22 BAOAB配布版は変更しません。

## Run / 実行

Python 3.12 and the three pinned requirements are used for the recorded checks:

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Parameters are validated before allocating experiment states. Excessive replica/step budgets are rejected by a declared scalar-work cap of 200 million; this is a workload guard, not a wall-clock guarantee.

Choose a new or empty output directory. `--case ID` runs one case for inspection; omitting it runs every case. JSON contains all scalar acceptance checks, measured records, equilibrium references, run environment, fixed-input SHA-256 and the completion reason. Each case also has a CSV. The first complete three-case run took about 5.5 s on the development host; this is a measured observation, not a runtime guarantee.

出力先は新規または空のフォルダを選びます。`--case ID`は1ケースの確認用、省略時は3件すべてを計算します。JSONに判定・測定値・参照・環境・入力ハッシュ・終了理由を保存し、CSVも出力します。初回3ケースの計算本体は開発機で約5.5秒でしたが、実行時間の保証ではありません。

Optional saved-data-only plotting:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

Matplotlib is not needed for scientific execution. Plotting only reads stored results; it does not repeat the experiments.

## Cases / ケース

- `csvr-kinetic-kernel`: bath-only diagnostic at Nf=1,2,6; conditional moments, noncentral-chi-square transition CDF, stationary Gamma fluctuations and kinetic ACF.
- `csvr-langevin-harmonic`: two harmonic modes with frequencies (1,1.7), comparing global CSVR with local Langevin, distributions, fluctuations and q,p,K,H correlation estimates.
- `csvr-langevin-quartic`: the same modes with an added 0.2 q⁴/4 per coordinate. Equilibrium distributions and moments come from independent Boltzmann quadrature, including a full physical-energy CDF.

浴の診断は独立した物理問題として数えません。調和例は既存Langevin調和問題の補助比較、四次非調和例が新しい物理問題です。

## Exact signed rescaling / 符号付きの厳密更新

For kB=1, target temperature T and Nf unconstrained momentum degrees of freedom, define Kbar=Nf*T/2, c=exp(-h/tau), A=T*(1-c)/2. With independent R~Normal(0,1), S~chi-square(Nf-1),

```
r = sqrt(c*K) + sqrt(A)*R
Knew = r*r + A*S
alpha = sign(r)*sqrt(Knew/K)
pnew = alpha*p
```

The same R determines magnitude and sign. For Nf=1, S is exactly zero; changing the sign can be essential. The code uses a mass-weighted unit direction and a new radius, rather than forming Knew/K, to avoid overflow for tiny nonzero momenta. Global rescaling with K=0 cannot specify a direction and is explicitly rejected. h=0 is an identity.

同じRを大きさと符号に使います。Nf=1ではS=0で、負のalphaを省くとOUの有限時間更新になりません。極小の非零運動量にも対応するよう、質量で重み付けした単位方向と新しい半径から再構成します。K=0は方向が未定義なので拒否し、勝手に熱浴方向を追加しません。拘束・COM除去を暗黙に適用せず、この例のNfは明示した2です。

The 2007 paper supplies the exact kinetic propagator; the 2008 paper supplies the signed-alpha prescription. Direct NumPy chi-square draws avoid the 2007 gamma-generation typo documented by Bussi. The code is original; official source implementations are not copied.

## Fair splitting and coupling / 分割と結合時間

Both new MD integrators use

```
O(h/2) -> B(h/2) -> A(h) -> B(h/2) -> O(h/2)
```

Here O is either exact global CSVR or component-wise exact OU, while B/A are velocity-Verlet force/drift updates. This symmetric OBABO composition is the adopted variant. The earlier BAOAB example is a separate integrator and is not silently substituted.

Langevin friction gamma=1/(2*tau) matches the **bath-only kinetic-energy relaxation time**. It does not imply matching position/momentum/full-MD energy correlations. Both methods sample the same equilibrium target while changing trajectories differently. Physical transport coefficients and unthermostatted dynamics are not validated here.

両方式で同じOBABO分割を使い、浴の違いと分割順序の違いを混同しません。gamma=1/(2*tau)は自由浴のK緩和をそろえる規約です。力のある系の相関がexp(-t/tau)になる、あるいは両方式で一致するとは要求しません。

## Independent references and uncertainty / 独立参照と標本誤差

The bath-only kinetic process is checked against separate CIR conditional mean/variance equations and SciPy's noncentral-chi-square quantiles. Stationary K~Gamma(Nf/2,T), Var(K)=Nf*T²/2 and Var(Tinst)=2*T²/Nf. Only this bath-only K correlation has the exact exp(-lag/tau) reference. A noiseless mean-relaxation control illustrates that the mean temperature can be right while fluctuations collapse; it is not a separately implemented Berendsen MD method.

For harmonic OBABO, velocity Verlet preserves the quadratic shadow energy

```
Hh = 1/2 * sum[p_i² + omega_i²*(1-h²*omega_i²/4)*q_i²].
```

Both baths preserve Maxwell momenta. Therefore an invariant shadow density has q variance T/[omega²*(1-h²*omega²/4)] and p variance T. An independently constructed affine-map Lyapunov solve confirms this expression. The deterministic variance bias at h=.2/.1/.05 is second order. Stochastic runs at h=.1/.05 are reported with sampling uncertainty; a measured noisy difference is not used to claim a temporal order.

For the quartic case, one-dimensional adaptive Boltzmann integrals provide normalizers, coordinate CDFs and U moments. Since Nf=2, K is exponential. Integrating its CDF over the bounded two-dimensional positional Boltzmann density gives the full physical-H CDF. Tolerances 2e-10 and 2e-12 are compared, and an independent static rejection ensemble checks the reference. H is not approximated by a harmonic Gamma distribution.

MD CDF errors are maxima at **five declared thresholds**, not whole-line Kolmogorov–Smirnov distances. Bath diagnostics use their separate three conditional-probability and four stationary-Gamma checkpoints. The reference momenta and total-energy observables are those at the completed OBABO step. q,p,K,H correlations use canonical reference centers/normalizers. Consequently finite-step zero-lag estimates need not equal exactly one. H's harmonic discrete correlation includes the squared finite-step mean shift when centered at the physical canonical mean.

相関の標準誤差は独立複製ごとの積の標本分散から計算します。同じ軌道の連続時刻を独立な標本と扱いません。図の誤差帯は±2標準誤差で、同時信頼帯や一般の偽陽性確率を保証するものではありません。四次系の全相関には独立な厳密動力学参照がなく、そこで参照誤差ゼロとは表示しません。

## Initial ensembles and scope / 初期集団と確認範囲

Each MD comparison keeps 8192 independent canonical initial replicas and 4096 separately initialized replicas whose q and p are scaled by 1.4. Both evolve for t=20 before measurement. The former checks finite-step preservation of a known ensemble, while the latter provides one finite-time equilibration check. Neither establishes general ergodicity.

Global rescaling does not randomize directions. The tests explicitly retain a separable invariant-axis counterexample: a coordinate with q=p=0 stays unexcited under global CSVR, even while total kinetic energy has nonzero noise. Nondegenerate frequencies and a weak quartic term in the comparison do not remove this general limitation.

新例は固定した少自由度の古典系・seed・予算・受入基準だけを検証します。成熟した分子系、拘束、相転移、輸送係数、BOMD/CPMD、量子系へ根拠を移しません。条件・予算・公差は`inputs.json`に先に置き、失敗を隠すために緩めません。

## Primary sources / 一次資料

1. G. Bussi, D. Donadio and M. Parrinello, *Canonical sampling through velocity rescaling*, J. Chem. Phys. **126**, 014101 (2007), DOI [10.1063/1.2408420](https://doi.org/10.1063/1.2408420). [Author manuscript, theory and Appendix A](https://arxiv.org/html/0803.4060v1). The manuscript was posted in 2008; that is not the journal publication year. SISSA's publisher PDF could not be fetched during this work.
2. G. Bussi and M. Parrinello, *Stochastic thermostats: comparison of local and global schemes*, Computer Physics Communications **179**, 26–29 (2008), DOI [10.1016/j.cpc.2008.01.006](https://doi.org/10.1016/j.cpc.2008.01.006). [Author manuscript sections I–II, Eqs. 8–9](https://arxiv.org/html/0803.4397v1).
3. [Bussi's official algorithm notes](https://sites.google.com/site/giovannibussi/Research/algorithms): correction concerning generation of Gaussian-square sums in the original appendix. Accessed 2026-11-22.

Review depth is stated in `cases.json`. This work reads selected original theory/algorithm sections and implements independent small experiments; it does not reproduce the papers' molecular applications.

## Rights / 利用条件

Original code is MIT; see `LICENSE`. Text, figures, fixed inputs, numerical data and third-party materials retain their separate conditions under [LICENSING.md](https://hrkoyama.github.io/LICENSING.md) and [rights](https://hrkoyama.github.io/rights/). The article PDFs and third-party code are not redistributed here. No blanket new license is granted to those materials.
