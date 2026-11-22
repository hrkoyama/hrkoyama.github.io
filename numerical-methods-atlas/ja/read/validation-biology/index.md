# 非線形反応拡散・パターン形成の独立検証

Schnakenbergの1次元周期系で、有限振幅の過渡から成長後のパターンまでをたどります。別の数値解法で得た参照に照合し、格子・時間刻み・参照自身の誤差を分けて調べます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Schnakenberg有限振幅過渡：非線形性と独立参照

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

### 前提・単位・境界

1D周期x∈[0,2π)、a=.1,b=.9、D=(.01,1)。共通初期値u=1+.08cos2x+.01cos4x、v=.9−.03cos2x−.002cos4x。反射対称かつπ周期の不変部分空間で、原点を固定します。

**編集上の補足**

空間比較は別のFourier–Galerkin/Radau参照に、時間比較は同じ差分半離散系を別に解くRadau参照に照合します。後者を連続PDEの厳密解とは呼びません。最初の粗い時間刻みでは分割誤差が空間誤差を覆ったため、判定基準を維持して刻みを細かくしました。旧入力と失敗指標も配布版に残します。

### 採用した計算法

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

### 比較・検証

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

### 確認の限界

選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。

### 保存実測値と判定

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

### 取得・実行

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

初回の不合格と刻み細分化の記録：https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

### 出典と確認範囲

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

## Schnakenberg飽和パターン：近定常性と格子・時間収束

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

### 前提・単位・境界

1D周期x∈[0,2π)、a=.1,b=.9、D=(.01,1)。共通初期値u=1+.08cos2x+.01cos4x、v=.9−.03cos2x−.002cos4x。反射対称かつπ周期の不変部分空間で、原点を固定します。

**編集上の補足**

近定常の判定は高精度のGalerkin参照に対する有限時間の確認です。有限刻みの分割法の固定点と、半離散PDEの定常解は一般に一致しないため、主計算のfull RHS残差を別に示します。線形化との差の大きさは非線形化の指標であり、精度や定常性の証明には使いません。選んだ反射対称・π周期の部分空間での確認です。

### 採用した計算法

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

### 比較・検証

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

### 確認の限界

選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。 近飽和は参照の90→100の検査窓に対する判定で、厳密定常解・非線形安定性・長期吸引の証明ではありません。lateの巨大な線形差は線形化の破綻診断で、精度誤差ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "spatial_finest_linf": 0.0027421513094392225,
    "temporal_finest_linf": 0.0004451357306107795,
    "minimum_spatial_order": 2.0947550434887137,
    "minimum_temporal_order": 1.7547591906992372,
    "reference_spatial_linf": 5.154365823045737e-11,
    "reference_tolerance_linf": 1.496580637194711e-12,
    "reference_to_primary_error_ratio": 1.9342564607967953e-08,
    "temporal_contamination_ratio": 0.020832217157728455,
    "minimum_concentration": 0.11412754265070092,
    "minimum_newton_iterate": 0.11412754265070092,
    "maximum_midpoint_residual": 1.9676968388004923e-13,
    "maximum_reaction_balance_error": 7.109035582431034e-13,
    "maximum_newton_iterations": 3,
    "nonlinear_relative_difference": 1.1426000574491519e+21,
    "pattern_amplitude": 1.9621659199933201,
    "higher_harmonic_ratio": 0.32273224487596686,
    "dominant_mode_u": 2,
    "mean_u": 1.0000000000005342,
    "mean_v": 0.7497600594170122,
    "saturation_change": 5.0330260847886166e-08,
    "saturation_rhs": 1.8773358978485533e-09,
    "saturation_projected_rhs": 1.877346373585754e-09,
    "saturation_fd_rhs": 0.0011586974655886095,
    "saturation_amplitude_change": 2.517517927458357e-08
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
    "higher_harmonic_ratio": true,
    "saturation_change": true,
    "saturation_rhs": true,
    "saturation_amplitude_change": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/index.json

### 取得・実行

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

初回の不合格と刻み細分化の記録：https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs-initial.json

### 出典と確認範囲

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
