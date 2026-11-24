# Su–Olson1997角度輸送の独立公開表比較

物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。

**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-algorithm)

全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

主検証は1997型の放射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

主検証は1997型の放射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。


**問題の図**

![Su–Olson1997角度輸送の独立公開表比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-validation)

5主計算で空間・32/64角・時間差と独立W/V誤差を分けます。参照表の有限性・因果零・一様解析source極限はmain前に資格済みです。 同じ初期・境界・sourceで別の連続空間角度行列と解析拡散極限を比較し、空間・角度・連続体極限誤差を分離。GL64/128、非単位容量の一様厳密解、独立DOP853で新参照141項目を先に資格します。

- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja) (`su-olson-transport1997`; 同じ問題の参照 · 有限格子の数値参照)

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。
## 前提・単位・境界

ε1、弾性散乱0、初期0、|x|<.5でQ1を時刻10まで。対称性でx0..8反射左・真空右。時刻.1/1/3.16228、13参照点x<6。 別制御は周期長2π、κ4/8/16、128/512/2048セル、ε1、Q0、I=V=1+.1cos xのセル平均です。

**編集上の補足**

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

## 採用した計算法

全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

## 比較・検証

5主計算で空間・32/64角・時間差と独立W/V誤差を分けます。参照表の有限性・因果零・一様解析source極限はmain前に資格済みです。 同じ初期・境界・sourceで別の連続空間角度行列と解析拡散極限を比較し、空間・角度・連続体極限誤差を分離。GL64/128、非単位容量の一様厳密解、独立DOP853で新参照141項目を先に資格します。

## 確認の限界

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

## 保存実測値と判定

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "pinned2023author-providedanalyticaltransporttable;original1997table not directly verified",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ],
    "matched_thick_limit_control": {
      "physical_mode_evolutions": 3,
      "mode_records": [
        {
          "id": "su-olson-transport1997-thick-k4",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k4.npz",
          "kappa": 4,
          "cells": 128,
          "ordinates": 32,
          "mean_free_path": 0.25,
          "kappa_h": 0.19634954084936207,
          "times": [
            0.0,
            0.25,
            0.5,
            1.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09998996042161418,
          "final_FV_space_error": 0.006406191708967511,
          "final_continuum_limit_error": 0.01484981145966009,
          "final_joint_energy_error": 0.009801905835372807,
          "final_joint_scaled_flux_error": 0.008805846751149496,
          "maximum_angular_sensitivity": 2.361755418510908e-15,
          "maximum_budget": 2.8398112908774138e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 9.096889908022376e-15
        },
        {
          "id": "su-olson-transport1997-thick-k8",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k8.npz",
          "kappa": 8,
          "cells": 512,
          "ordinates": 32,
          "mean_free_path": 0.125,
          "kappa_h": 0.09817477042468103,
          "times": [
            0.0,
            0.5,
            1.0,
            2.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999937250863256,
          "final_FV_space_error": 0.0029971556290815586,
          "final_continuum_limit_error": 0.0038430634683478773,
          "final_joint_energy_error": 0.0016548173640567698,
          "final_joint_scaled_flux_error": 0.0012410650258467806,
          "maximum_angular_sensitivity": 2.707688603804596e-15,
          "maximum_budget": 5.698441403484806e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 3.609851133290487e-14
        },
        {
          "id": "su-olson-transport1997-thick-k16",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k16.npz",
          "kappa": 16,
          "cells": 2048,
          "ordinates": 32,
          "mean_free_path": 0.0625,
          "kappa_h": 0.04908738521234052,
          "times": [
            0.0,
            1.0,
            2.0,
            4.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999996078172033,
          "final_FV_space_error": 0.0014774233739939713,
          "final_continuum_limit_error": 0.0009641878482973868,
          "final_joint_energy_error": 0.0011378880853298219,
          "final_joint_scaled_flux_error": 0.0005274719030461596,
          "maximum_angular_sensitivity": 5.828675392681093e-15,
          "maximum_budget": 1.0695349491031034e-14,
          "matrix_residual": 3.469446951953614e-18,
          "semidiscrete_global_RHS_residual": 8.391850078921443e-14
        }
      ],
      "reference_checks": 141,
      "same_operator": "kappa times actualtransport.rhs withkappa*h,bothrates",
      "time_role": "Exact-time semidiscrete Fourier control; originalSSPRK2tests/transientruns separate",
      "reference_role": "Independentcontinuum-space angularmatrixGL64/128plusDOP853qualifiers;sharedSciPysparseexpm_multiplydeclared",
      "diffusion": "D_rad1/(3kappa),D_eff1/[3kappa(epsilon+1)],matchedperiodiccellmeanIC",
      "scope": "ResolvedjointN~kappa^2limit; nofixed-gridAPorSSPRK2temporal-orderclaim. Initiallayerreportedallfourtimes;asymptoticgatesfinals.25only;nojointorderfit."
    }
  },
  "checks": {
    "su-olson-transport1997-n128/finite-positive": true,
    "su-olson-transport1997-n128/energy-budget": true,
    "su-olson-transport1997-n128/fixed-final-time": true,
    "su-olson-transport1997-n128/explicit-courant": true,
    "su-olson-transport1997-n256/finite-positive": true,
    "su-olson-transport1997-n256/energy-budget": true,
    "su-olson-transport1997-n256/fixed-final-time": true,
    "su-olson-transport1997-n256/explicit-courant": true,
    "su-olson-transport1997-n512/finite-positive": true,
    "su-olson-transport1997-n512/energy-budget": true,
    "su-olson-transport1997-n512/fixed-final-time": true,
    "su-olson-transport1997-n512/explicit-courant": true,
    "su-olson-transport1997-angular-64/finite-positive": true,
    "su-olson-transport1997-angular-64/energy-budget": true,
    "su-olson-transport1997-angular-64/fixed-final-time": true,
    "su-olson-transport1997-angular-64/explicit-courant": true,
    "su-olson-transport1997-half-dt/finite-positive": true,
    "su-olson-transport1997-half-dt/energy-budget": true,
    "su-olson-transport1997-half-dt/fixed-final-time": true,
    "su-olson-transport1997-half-dt/explicit-courant": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-angular-sensitivity": true,
    "separate-time-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true,
    "thick/4/finite-positive-fields": true,
    "thick/4/periodic-weighted-energy": true,
    "thick/4/actual-stencil-and-global-RHS": true,
    "thick/4/separate-FV-space-error": true,
    "thick/4/separate-angular-sensitivity": true,
    "thick/4/physical-initial-layer-retained": true,
    "thick/4/mean-free-path-resolved": true,
    "thick/8/finite-positive-fields": true,
    "thick/8/periodic-weighted-energy": true,
    "thick/8/actual-stencil-and-global-RHS": true,
    "thick/8/separate-FV-space-error": true,
    "thick/8/separate-angular-sensitivity": true,
    "thick/8/physical-initial-layer-retained": true,
    "thick/8/mean-free-path-resolved": true,
    "thick/16/finite-positive-fields": true,
    "thick/16/periodic-weighted-energy": true,
    "thick/16/actual-stencil-and-global-RHS": true,
    "thick/16/separate-FV-space-error": true,
    "thick/16/separate-angular-sensitivity": true,
    "thick/16/physical-initial-layer-retained": true,
    "thick/16/mean-free-path-resolved": true,
    "thick/space/k8": true,
    "thick/continuum-limit/k8": true,
    "thick/space/k16": true,
    "thick/continuum-limit/k16": true,
    "thick/finest-energy-limit": true,
    "thick/finest-scaled-flux-limit": true,
    "thick/wrong-flux-sign-negative-control": true,
    "thick/missing-one-third-negative-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/index.json

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

保存した実計算場の科学プレビュー。

![1次元周期・同じ実FV/S_N演算子の単一Fourierモードを時間厳密に進めた厚い極限制御。初期層と空間・角度・極限誤差を分離。固定格子AP性やSSPRK2時間積分の認証ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-thick-limit.png)

1次元周期・同じ実FV/S_N演算子の単一Fourierモードを時間厳密に進めた厚い極限制御。初期層と空間・角度・極限誤差を分離。固定格子AP性やSSPRK2時間積分の認証ではありません。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Aidan Crilly (2023). Learning closure relations using differentiable programming:an example in radiation transport;author-provided analytic benchmark data. https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData; review_level=primary-author-paper-selected-equations-and-pinned-data-qualification
Read official2023paperpage6Appendix4.1equations7-10,README,pinned W/Vtransport tables andMITlicense. Whether author tables were transcribed or regenerated is unstated. Original1997fulltext/tables not directly checked;not trained-model outputs. Shape,normalization,causal/homogeneous controls qualified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Su–Olson transport with an independently published analytical table

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-algorithm)

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.


**Problem figure**

![Su–Olson transport with an independently published analytical table: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-validation)

Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.

- [Su–Olson transport: primary2023author-provided analytical benchmark data](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en) (`su-olson-transport1997`; Same-problem reference · Finite-grid numerical reference)

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.
## Assumptions, units and boundaries

epsilon1,noelastic scattering,coldIC,Q1inside|x|<.5untiltau10. Symmetricx0..8withreflectingleft/vacuumright;times.1/1/3.16228and13referencepointsx<6. A separate periodic length2pi control uses kappa4/8/16,cells128/512/2048,epsilon1,Q0 and actual cell means of I=V=1+.1cos x.

**Editorial clarification**

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

## Adopted numerical method

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

## References and validation

Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.

## Limits

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

## Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "pinned2023author-providedanalyticaltransporttable;original1997table not directly verified",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ],
    "matched_thick_limit_control": {
      "physical_mode_evolutions": 3,
      "mode_records": [
        {
          "id": "su-olson-transport1997-thick-k4",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k4.npz",
          "kappa": 4,
          "cells": 128,
          "ordinates": 32,
          "mean_free_path": 0.25,
          "kappa_h": 0.19634954084936207,
          "times": [
            0.0,
            0.25,
            0.5,
            1.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09998996042161418,
          "final_FV_space_error": 0.006406191708967511,
          "final_continuum_limit_error": 0.01484981145966009,
          "final_joint_energy_error": 0.009801905835372807,
          "final_joint_scaled_flux_error": 0.008805846751149496,
          "maximum_angular_sensitivity": 2.361755418510908e-15,
          "maximum_budget": 2.8398112908774138e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 9.096889908022376e-15
        },
        {
          "id": "su-olson-transport1997-thick-k8",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k8.npz",
          "kappa": 8,
          "cells": 512,
          "ordinates": 32,
          "mean_free_path": 0.125,
          "kappa_h": 0.09817477042468103,
          "times": [
            0.0,
            0.5,
            1.0,
            2.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999937250863256,
          "final_FV_space_error": 0.0029971556290815586,
          "final_continuum_limit_error": 0.0038430634683478773,
          "final_joint_energy_error": 0.0016548173640567698,
          "final_joint_scaled_flux_error": 0.0012410650258467806,
          "maximum_angular_sensitivity": 2.707688603804596e-15,
          "maximum_budget": 5.698441403484806e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 3.609851133290487e-14
        },
        {
          "id": "su-olson-transport1997-thick-k16",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k16.npz",
          "kappa": 16,
          "cells": 2048,
          "ordinates": 32,
          "mean_free_path": 0.0625,
          "kappa_h": 0.04908738521234052,
          "times": [
            0.0,
            1.0,
            2.0,
            4.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999996078172033,
          "final_FV_space_error": 0.0014774233739939713,
          "final_continuum_limit_error": 0.0009641878482973868,
          "final_joint_energy_error": 0.0011378880853298219,
          "final_joint_scaled_flux_error": 0.0005274719030461596,
          "maximum_angular_sensitivity": 5.828675392681093e-15,
          "maximum_budget": 1.0695349491031034e-14,
          "matrix_residual": 3.469446951953614e-18,
          "semidiscrete_global_RHS_residual": 8.391850078921443e-14
        }
      ],
      "reference_checks": 141,
      "same_operator": "kappa times actualtransport.rhs withkappa*h,bothrates",
      "time_role": "Exact-time semidiscrete Fourier control; originalSSPRK2tests/transientruns separate",
      "reference_role": "Independentcontinuum-space angularmatrixGL64/128plusDOP853qualifiers;sharedSciPysparseexpm_multiplydeclared",
      "diffusion": "D_rad1/(3kappa),D_eff1/[3kappa(epsilon+1)],matchedperiodiccellmeanIC",
      "scope": "ResolvedjointN~kappa^2limit; nofixed-gridAPorSSPRK2temporal-orderclaim. Initiallayerreportedallfourtimes;asymptoticgatesfinals.25only;nojointorderfit."
    }
  },
  "checks": {
    "su-olson-transport1997-n128/finite-positive": true,
    "su-olson-transport1997-n128/energy-budget": true,
    "su-olson-transport1997-n128/fixed-final-time": true,
    "su-olson-transport1997-n128/explicit-courant": true,
    "su-olson-transport1997-n256/finite-positive": true,
    "su-olson-transport1997-n256/energy-budget": true,
    "su-olson-transport1997-n256/fixed-final-time": true,
    "su-olson-transport1997-n256/explicit-courant": true,
    "su-olson-transport1997-n512/finite-positive": true,
    "su-olson-transport1997-n512/energy-budget": true,
    "su-olson-transport1997-n512/fixed-final-time": true,
    "su-olson-transport1997-n512/explicit-courant": true,
    "su-olson-transport1997-angular-64/finite-positive": true,
    "su-olson-transport1997-angular-64/energy-budget": true,
    "su-olson-transport1997-angular-64/fixed-final-time": true,
    "su-olson-transport1997-angular-64/explicit-courant": true,
    "su-olson-transport1997-half-dt/finite-positive": true,
    "su-olson-transport1997-half-dt/energy-budget": true,
    "su-olson-transport1997-half-dt/fixed-final-time": true,
    "su-olson-transport1997-half-dt/explicit-courant": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-angular-sensitivity": true,
    "separate-time-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true,
    "thick/4/finite-positive-fields": true,
    "thick/4/periodic-weighted-energy": true,
    "thick/4/actual-stencil-and-global-RHS": true,
    "thick/4/separate-FV-space-error": true,
    "thick/4/separate-angular-sensitivity": true,
    "thick/4/physical-initial-layer-retained": true,
    "thick/4/mean-free-path-resolved": true,
    "thick/8/finite-positive-fields": true,
    "thick/8/periodic-weighted-energy": true,
    "thick/8/actual-stencil-and-global-RHS": true,
    "thick/8/separate-FV-space-error": true,
    "thick/8/separate-angular-sensitivity": true,
    "thick/8/physical-initial-layer-retained": true,
    "thick/8/mean-free-path-resolved": true,
    "thick/16/finite-positive-fields": true,
    "thick/16/periodic-weighted-energy": true,
    "thick/16/actual-stencil-and-global-RHS": true,
    "thick/16/separate-FV-space-error": true,
    "thick/16/separate-angular-sensitivity": true,
    "thick/16/physical-initial-layer-retained": true,
    "thick/16/mean-free-path-resolved": true,
    "thick/space/k8": true,
    "thick/continuum-limit/k8": true,
    "thick/space/k16": true,
    "thick/continuum-limit/k16": true,
    "thick/finest-energy-limit": true,
    "thick/finest-scaled-flux-limit": true,
    "thick/wrong-flux-sign-negative-control": true,
    "thick/missing-one-third-negative-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

Scientific preview from the actual saved numerical fields.

![Matched thick-limit control: exact-time single Fourier mode of the actual 1D periodic FV/S_N operator;initial layer and spatial/angular/limit errors separated. No fixed-grid AP or SSPRK2 time-integration certification.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-thick-limit.png)

Matched thick-limit control: exact-time single Fourier mode of the actual 1D periodic FV/S_N operator;initial layer and spatial/angular/limit errors separated. No fixed-grid AP or SSPRK2 time-integration certification.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Aidan Crilly (2023). Learning closure relations using differentiable programming:an example in radiation transport;author-provided analytic benchmark data. https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData; review_level=primary-author-paper-selected-equations-and-pinned-data-qualification
Read official2023paperpage6Appendix4.1equations7-10,README,pinned W/Vtransport tables andMITlicense. Whether author tables were transcribed or regenerated is unstated. Original1997fulltext/tables not directly checked;not trained-model outputs. Shape,normalization,causal/homogeneous controls qualified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
