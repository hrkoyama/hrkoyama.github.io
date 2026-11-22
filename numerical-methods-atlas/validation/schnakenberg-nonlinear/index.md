# Schnakenberg有限振幅過渡：非線形性と独立参照

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) (`implicit-midpoint`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-algorithm)

二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Schnakenberg有限振幅過渡：非線形性と独立参照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja#schnakenberg-nonlinear-ja-validation)

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

1D周期x∈[0,2π)、a=.1,b=.9、D=(.01,1)。共通初期値u=1+.08cos2x+.01cos4x、v=.9−.03cos2x−.002cos4x。反射対称かつπ周期の不変部分空間で、原点を固定します。

**編集上の補足**

空間比較は別のFourier–Galerkin/Radau参照に、時間比較は同じ差分半離散系を別に解くRadau参照に照合します。後者を連続PDEの厳密解とは呼びません。最初の粗い時間刻みでは分割誤差が空間誤差を覆ったため、判定基準を維持して刻みを細かくしました。旧入力と失敗指標も配布版に残します。

## 採用した計算法

二次中心FD行列の固有値−4sin²(πk/N)/Δx²をFFTで対角化して拡散を厳密に半刻み進め、反応を各点2×2 Newtonのimplicit midpointで全刻み進めるStrang合成。FFT使用時も空間離散はFDです。未収束・予算超過は失敗とし、濃度のclippingはしません。

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

## 比較・検証

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

## 確認の限界

選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "spatial_finest_linf": 0.0027896112809786544,
    "temporal_finest_linf": 0.0006354301179647415,
    "minimum_spatial_order": 1.950418112212569,
    "minimum_temporal_order": 1.9845197964375065,
    "reference_spatial_linf": 3.255173908200959e-13,
    "reference_tolerance_linf": 4.4497738826976274e-13,
    "reference_to_primary_error_ratio": 2.7620148525480325e-10,
    "temporal_contamination_ratio": 0.03590744607345364,
    "minimum_concentration": 0.22446801668493407,
    "minimum_newton_iterate": 0.22446801668493407,
    "maximum_midpoint_residual": 1.9676968388004923e-13,
    "maximum_reaction_balance_error": 1.6764367671839864e-14,
    "maximum_newton_iterations": 3,
    "nonlinear_relative_difference": 0.7973947672828199,
    "pattern_amplitude": 1.584854307174442,
    "higher_harmonic_ratio": 0.23973709295898224,
    "dominant_mode_u": 2,
    "mean_u": 1.0212843245725893,
    "mean_v": 0.7809100883890534
  },
  "checks": {
    "spatial_finest_linf": true,
    "temporal_finest_linf": true,
    "reference_spatial_linf": true,
    "reference_tolerance_linf": true,
    "reference_to_primary_error_ratio": true,
    "temporal_contamination_ratio": true,
    "maximum_midpoint_residual": true,
    "maximum_reaction_balance_error": true,
    "minimum_spatial_order": true,
    "minimum_temporal_order": true,
    "positive_without_clipping": true,
    "nonlinear_relative_difference": true,
    "pattern_amplitude": true,
    "higher_harmonic_ratio": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

## 出典と確認範囲

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://www.mit.edu/~kardar/research/seminars/EPB/Turing.pdf; review_level=original-paper-selected-sections
  大学公開の原著スキャン第6–7節（印刷46–50頁）の環状系・線形化と書誌を確認。今回の係数・有限振幅参照・飽和形状の出典とは区別します。
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  PubMedの書誌・DOIと出版社索引の抄録を確認。原著本文は403で未取得。反応系の歴史的出典であり、a=.1,b=.9や今回の空間計算を原著の再現とは呼びません。
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://epubs.siam.org/doi/pdf/10.1137/0705041; review_level=original-paper-selected-nonlinear-composition
  原著510–512頁の半刻み合成と非線形問題の2次構成を確認。本モデルの正値性や任意刻みでの精度を保証する引用ではありません。
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=author-lecture-selected-midpoint-and-splitting
  著者公開講義の定理3・第5節でimplicit midpointの式・次数と対称分割を確認。Hamiltonian系のsymplectic性を本化学反応へ転用しません。
- The SciPy community (2024). SciPy1.14.1 solve_ivp and Radau reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-api-specification
  Radau IIAの5次式、rtol/atolの局所誤差制御、analytic Jacobian、終了状態の公式仕様を確認。ODE公差は連続PDEの全域誤差保証ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Finite-amplitude Schnakenberg transient: nonlinearity and independent reference

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-algorithm)

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-validation)

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

1D periodic x∈[0,2π), a=.1,b=.9,D=(.01,1). Common IC u=1+.08cos(2x)+.01cos(4x), v=.9−.03cos(2x)−.002cos(4x), restricted to a reflection-even, pi-periodic invariant subspace with a fixed origin.

**Editorial clarification**

Space refinement uses a separate Fourier–Galerkin/Radau reference; time refinement uses an independently integrated Radau solution of the same FD semidiscrete system, not an exact continuous-PDE solution. Splitting error masked spatial error in the first coarse-step pilot. Steps were refined while keeping the acceptance criteria; the original input and failed metrics remain in the release.

## Adopted numerical method

Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

## References and validation

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

## Limits

A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations.

## Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_finest_linf": 0.0027896112809786544,
    "temporal_finest_linf": 0.0006354301179647415,
    "minimum_spatial_order": 1.950418112212569,
    "minimum_temporal_order": 1.9845197964375065,
    "reference_spatial_linf": 3.255173908200959e-13,
    "reference_tolerance_linf": 4.4497738826976274e-13,
    "reference_to_primary_error_ratio": 2.7620148525480325e-10,
    "temporal_contamination_ratio": 0.03590744607345364,
    "minimum_concentration": 0.22446801668493407,
    "minimum_newton_iterate": 0.22446801668493407,
    "maximum_midpoint_residual": 1.9676968388004923e-13,
    "maximum_reaction_balance_error": 1.6764367671839864e-14,
    "maximum_newton_iterations": 3,
    "nonlinear_relative_difference": 0.7973947672828199,
    "pattern_amplitude": 1.584854307174442,
    "higher_harmonic_ratio": 0.23973709295898224,
    "dominant_mode_u": 2,
    "mean_u": 1.0212843245725893,
    "mean_v": 0.7809100883890534
  },
  "checks": {
    "spatial_finest_linf": true,
    "temporal_finest_linf": true,
    "reference_spatial_linf": true,
    "reference_tolerance_linf": true,
    "reference_to_primary_error_ratio": true,
    "temporal_contamination_ratio": true,
    "maximum_midpoint_residual": true,
    "maximum_reaction_balance_error": true,
    "minimum_spatial_order": true,
    "minimum_temporal_order": true,
    "positive_without_clipping": true,
    "nonlinear_relative_difference": true,
    "pattern_amplitude": true,
    "higher_harmonic_ratio": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

## Sources and review scope

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://www.mit.edu/~kardar/research/seminars/EPB/Turing.pdf; review_level=original-paper-selected-sections
  Checked the university-hosted original scan, sections 6–7 (printed pp.46–50), ring formulation/linearization and bibliography. Distinct from the adopted coefficients, finite-amplitude reference and mature shape.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  Checked official PubMed bibliography/DOI and publisher-indexed abstract. Full text returned403. Historical source for the reaction family, not a claim to reproduce original coefficients or experiments.
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://epubs.siam.org/doi/pdf/10.1137/0705041; review_level=original-paper-selected-nonlinear-composition
  Checked original pp.510–512 for half-step composition and nonlinear second-order construction. This does not guarantee positivity or accuracy at arbitrary steps in the adopted model.
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=author-lecture-selected-midpoint-and-splitting
  Checked theorem3 and section5 of the author-hosted lecture for implicit-midpoint formula/order and symmetric splitting. Hamiltonian symplectic claims are not transferred to this chemical model.
- The SciPy community (2024). SciPy1.14.1 solve_ivp and Radau reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-api-specification
  Checked official Radau IIA order5, local rtol/atol scaling, analytic Jacobians and termination status. ODE tolerances do not certify global continuum-PDE accuracy.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
