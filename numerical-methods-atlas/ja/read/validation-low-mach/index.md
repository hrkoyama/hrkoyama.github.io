# 低Mach等エントロピー渦：前処理Roe流束の軽量検証

同じ2次元Euler等エントロピー渦を、背景Mach数.1/.01、16²・32²・64²、T=.1で計算します。両流束に無制限の中心primitive MUSCL再構築を用い、通常Roeと数値散逸をMiczek系行列で前処理するRoeをSSPRK(3,3)で比較します。物理時間項と音響CFL=.2を保つ限定例です。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 低Mach等エントロピー渦：前処理Roe流束の軽量検証

同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。

**使用手法**

- [Roe法](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja) (`roe`)
- [低Mach数のPDE前処理](https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja) (`low-mach-preconditioning`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-algorithm)

同じ無制限の中心原始変数MUSCL再構築・有限体積・物理Euler流束・SSPRK(3,3)を使い、Roe散逸だけをD=P⁻¹|PA|で前処理します。Roe平均の全流速Machからμ=min(1,max(Mlocal,M∞))、δ=1/μ−1とし、原始変数のMiczek行列を保存量へ変換します。行列絶対値は特性値ũn,ũn±τの2次多項式で作用させ、別の密行列固有分解と照合します。物理時間微分・音速は変えず、音響CFL=.2を使います。再構築した両面と各3段の正のρ,pを確認し、limiter・floor・状態修復・隠れた再試行・疑似時間反復はありません。前進Eulerの増幅反例を示すため、SSP・TVD・非線形安定性を名前だけで保証しません。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

無外力の2次元理想気体Euler系を、元の保存変数・物理時間で更新します。γ=1.4、周期20×20領域、背景圧力をMach数に応じて変える等エントロピー渦が固定入力です。


**問題の図**

![低Mach等エントロピー渦：前処理Roe流束の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-validation)

初版の32単体検査は合格しましたが、区分定数空間離散化での143判定中、M∞=.01・最細格子の全領域圧力誤差.16537が事前閾値.1を超えました。初版ソース・契約・全12場・判定と、その全領域図を失敗のまま保存します。改訂では両流束を同じ無制限中心原始変数MUSCLにし、面状態の拒否・正しい再構築Fourier記号・独立行列を使う実RHSの線形化など3検査を追加しました。入力・物理時間・CFL・受入条件はバイト単位で不変です。新35検査と143条件の契約を改訂の実行前に固定しました。 Roe平均の保存量ジャンプと物理流束差、密行列の前処理散逸、3段更新・不正段保持を照合します。各背景Mach・流束で17²個の定数状態Fourierモードと、物理音響エネルギーで規格化した増幅行列の1/10/100乗を調べます。圧力誤差は大きなp∞ではなくρ∞|U∞|²で割り、速度誤差は渦の速度変動で規格化します。移動解析場に対する初期R_h−q_tも記録し、定常残差の収束とは区別します。 改訂の35検査・全12計算143判定は-W errorで合格し、元のMacで全計算は約4.4秒でした。最細M∞=.01の速度相対L1はRoe .07411、前処理 .01847、固定コアの圧力誤差は.04871/.0006325でした。一方、全領域の圧力誤差は.01194/.01260で前処理側がわずかに悪く、M∞=.1でも.0006653/.0006737と同様です。全4保存量の最大相対残差は4.24e-14。Gauss8/16の動的スケール最大差は4.08e-11、解析Euler代入残差は1.09e-16でした。指定したFourierモードのSSPRK3増幅半径とエネルギー規格化行列累乗ノルムは最大1。前進Eulerは両MUSCL流束で1を超え、M∞=.01の前処理側で約1.03560でした。

- [等エントロピー渦：低Mach比較に用いるEuler解析場](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja) (`isentropic-vortex`; 同じ問題の参照 · 解析参照)

同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。
### 前提・単位・境界

領域[-10,10]²、周期境界、γ=1.4、β=3、背景ρ∞=1とU∞=(1,.5)。p∞=|U∞|²/(γM∞²)とし、流速と渦強度を固定して背景Mach数を変えます。M∞は局所最大Mach数ではありません。全平面の移動等エントロピー渦を最小像座標で評価し、有限周期箱のGaussian裾の継ぎ目を別に評価します。保存量のセル平均は8点Gauss求積で初期化・比較し、16点と照合します。閉形式の厳密セル平均や一般の厳密周期渦とは呼びません。

**編集上の補足**

実装するのは数値流束の散逸行列D=P⁻¹|PA|の前処理です。擬似時間の定常反復・二重時間積分による加速や、対流刻みでの陽的安定性を検証するものではありません。SSPRK(3,3)という名称だけから強安定性や非線形正値性の定理を適用せず、固定実行と標本化した定数状態Fourierモードの範囲を区別します。 最細のM∞=.01では速度誤差と渦の運動エネルギー保持が改善しますが、全域の動圧規格化圧力L1は通常Roeの約.01194に対し前処理側は約.01260で、圧力誤差が常に小さくなる結果ではありません。図の渦度・背景流からの速度差は中心部分の表示で、誤差判定は全域と固定coreを区別します。

### 採用した計算法

同じ無制限の中心原始変数MUSCL再構築・有限体積・物理Euler流束・SSPRK(3,3)を使い、Roe散逸だけをD=P⁻¹|PA|で前処理します。Roe平均の全流速Machからμ=min(1,max(Mlocal,M∞))、δ=1/μ−1とし、原始変数のMiczek行列を保存量へ変換します。行列絶対値は特性値ũn,ũn±τの2次多項式で作用させ、別の密行列固有分解と照合します。物理時間微分・音速は変えず、音響CFL=.2を使います。再構築した両面と各3段の正のρ,pを確認し、limiter・floor・状態修復・隠れた再試行・疑似時間反復はありません。前進Eulerの増幅反例を示すため、SSP・TVD・非線形安定性を名前だけで保証しません。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

### 比較・検証

初版の32単体検査は合格しましたが、区分定数空間離散化での143判定中、M∞=.01・最細格子の全領域圧力誤差.16537が事前閾値.1を超えました。初版ソース・契約・全12場・判定と、その全領域図を失敗のまま保存します。改訂では両流束を同じ無制限中心原始変数MUSCLにし、面状態の拒否・正しい再構築Fourier記号・独立行列を使う実RHSの線形化など3検査を追加しました。入力・物理時間・CFL・受入条件はバイト単位で不変です。新35検査と143条件の契約を改訂の実行前に固定しました。 Roe平均の保存量ジャンプと物理流束差、密行列の前処理散逸、3段更新・不正段保持を照合します。各背景Mach・流束で17²個の定数状態Fourierモードと、物理音響エネルギーで規格化した増幅行列の1/10/100乗を調べます。圧力誤差は大きなp∞ではなくρ∞|U∞|²で割り、速度誤差は渦の速度変動で規格化します。移動解析場に対する初期R_h−q_tも記録し、定常残差の収束とは区別します。 改訂の35検査・全12計算143判定は-W errorで合格し、元のMacで全計算は約4.4秒でした。最細M∞=.01の速度相対L1はRoe .07411、前処理 .01847、固定コアの圧力誤差は.04871/.0006325でした。一方、全領域の圧力誤差は.01194/.01260で前処理側がわずかに悪く、M∞=.1でも.0006653/.0006737と同様です。全4保存量の最大相対残差は4.24e-14。Gauss8/16の動的スケール最大差は4.08e-11、解析Euler代入残差は1.09e-16でした。指定したFourierモードのSSPRK3増幅半径とエネルギー規格化行列累乗ノルムは最大1。前進Eulerは両MUSCL流束で1を超え、M∞=.01の前処理側で約1.03560でした。

### 確認の限界

T=.1だけの短時間・少数格子の検証で、渦の一周や長時間保存を確認したものではありません。Fourier検査は指定した一様背景・離散波数・増幅回数の範囲であり、全波数や可変状態の非線形安定性・正値性の証明ではありません。実計算では音響CFLを維持し、対流刻みで進めたとは主張しません。定常解の加速、dual time、衝撃波・接触の頑健性、一般格子やMach数全域は未検証です。解析場の有限周期箱、Gauss求積、セル平均からの原始変数評価を区別し、圧力のMach依存や局所誤差を成功値だけに置き換えません。 無制限MUSCLは滑らかなこの入力の選択であり、limiter・TVD法・一般的な正値性保証ではありません。初版で現れた箱全体の圧力波を角の切り取りだけで隠さず、追加図で全領域の失敗を示します。 速度や固定コアの改善を圧力全域へ一般化できません。最細の全領域圧力L1は前処理側が少し大きく、M∞を10分の1にすると前処理の全域圧力誤差も増えています。圧力精度のMach独立性はこの実測から主張しません。運動エネルギー比は保存セル平均から求めた速度変動の診断で、連続場の運動エネルギーの厳密保存ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_runs_completed": 12,
    "maximum_quadrature_dynamic_difference": 4.0745362639427176e-11,
    "maximum_point_Euler_residual": 1.0897087716081738e-16
  },
  "checks": {
    "all twelve fixed nonlinear runs completed": true,
    "M0.1/roe/N16: final time": true,
    "M0.1/roe/N16: minimum_density_all_stages": true,
    "M0.1/roe/N16: minimum_pressure_all_stages": true,
    "M0.1/roe/N16: state_floor_count": true,
    "M0.1/roe/N16: rejected_steps": true,
    "M0.1/roe/N16: mass periodic balance": true,
    "M0.1/roe/N16: x momentum periodic balance": true,
    "M0.1/roe/N16: y momentum periodic balance": true,
    "M0.1/roe/N16: total energy periodic balance": true,
    "M0.1/roe/N16: finite physical diagnostics": true,
    "M0.1/roe/N32: final time": true,
    "M0.1/roe/N32: minimum_density_all_stages": true,
    "M0.1/roe/N32: minimum_pressure_all_stages": true,
    "M0.1/roe/N32: state_floor_count": true,
    "M0.1/roe/N32: rejected_steps": true,
    "M0.1/roe/N32: mass periodic balance": true,
    "M0.1/roe/N32: x momentum periodic balance": true,
    "M0.1/roe/N32: y momentum periodic balance": true,
    "M0.1/roe/N32: total energy periodic balance": true,
    "M0.1/roe/N32: finite physical diagnostics": true,
    "M0.1/roe/N64: final time": true,
    "M0.1/roe/N64: minimum_density_all_stages": true,
    "M0.1/roe/N64: minimum_pressure_all_stages": true,
    "M0.1/roe/N64: state_floor_count": true,
    "M0.1/roe/N64: rejected_steps": true,
    "M0.1/roe/N64: mass periodic balance": true,
    "M0.1/roe/N64: x momentum periodic balance": true,
    "M0.1/roe/N64: y momentum periodic balance": true,
    "M0.1/roe/N64: total energy periodic balance": true,
    "M0.1/roe/N64: finite physical diagnostics": true,
    "M0.1/miczek/N16: final time": true,
    "M0.1/miczek/N16: minimum_density_all_stages": true,
    "M0.1/miczek/N16: minimum_pressure_all_stages": true,
    "M0.1/miczek/N16: state_floor_count": true,
    "M0.1/miczek/N16: rejected_steps": true,
    "M0.1/miczek/N16: mass periodic balance": true,
    "M0.1/miczek/N16: x momentum periodic balance": true,
    "M0.1/miczek/N16: y momentum periodic balance": true,
    "M0.1/miczek/N16: total energy periodic balance": true,
    "M0.1/miczek/N16: finite physical diagnostics": true,
    "M0.1/miczek/N32: final time": true,
    "M0.1/miczek/N32: minimum_density_all_stages": true,
    "M0.1/miczek/N32: minimum_pressure_all_stages": true,
    "M0.1/miczek/N32: state_floor_count": true,
    "M0.1/miczek/N32: rejected_steps": true,
    "M0.1/miczek/N32: mass periodic balance": true,
    "M0.1/miczek/N32: x momentum periodic balance": true,
    "M0.1/miczek/N32: y momentum periodic balance": true,
    "M0.1/miczek/N32: total energy periodic balance": true,
    "M0.1/miczek/N32: finite physical diagnostics": true,
    "M0.1/miczek/N64: final time": true,
    "M0.1/miczek/N64: minimum_density_all_stages": true,
    "M0.1/miczek/N64: minimum_pressure_all_stages": true,
    "M0.1/miczek/N64: state_floor_count": true,
    "M0.1/miczek/N64: rejected_steps": true,
    "M0.1/miczek/N64: mass periodic balance": true,
    "M0.1/miczek/N64: x momentum periodic balance": true,
    "M0.1/miczek/N64: y momentum periodic balance": true,
    "M0.1/miczek/N64: total energy periodic balance": true,
    "M0.1/miczek/N64: finite physical diagnostics": true,
    "M0.01/roe/N16: final time": true,
    "M0.01/roe/N16: minimum_density_all_stages": true,
    "M0.01/roe/N16: minimum_pressure_all_stages": true,
    "M0.01/roe/N16: state_floor_count": true,
    "M0.01/roe/N16: rejected_steps": true,
    "M0.01/roe/N16: mass periodic balance": true,
    "M0.01/roe/N16: x momentum periodic balance": true,
    "M0.01/roe/N16: y momentum periodic balance": true,
    "M0.01/roe/N16: total energy periodic balance": true,
    "M0.01/roe/N16: finite physical diagnostics": true,
    "M0.01/roe/N32: final time": true,
    "M0.01/roe/N32: minimum_density_all_stages": true,
    "M0.01/roe/N32: minimum_pressure_all_stages": true,
    "M0.01/roe/N32: state_floor_count": true,
    "M0.01/roe/N32: rejected_steps": true,
    "M0.01/roe/N32: mass periodic balance": true,
    "M0.01/roe/N32: x momentum periodic balance": true,
    "M0.01/roe/N32: y momentum periodic balance": true,
    "M0.01/roe/N32: total energy periodic balance": true,
    "M0.01/roe/N32: finite physical diagnostics": true,
    "M0.01/roe/N64: final time": true,
    "M0.01/roe/N64: minimum_density_all_stages": true,
    "M0.01/roe/N64: minimum_pressure_all_stages": true,
    "M0.01/roe/N64: state_floor_count": true,
    "M0.01/roe/N64: rejected_steps": true,
    "M0.01/roe/N64: mass periodic balance": true,
    "M0.01/roe/N64: x momentum periodic balance": true,
    "M0.01/roe/N64: y momentum periodic balance": true,
    "M0.01/roe/N64: total energy periodic balance": true,
    "M0.01/roe/N64: finite physical diagnostics": true,
    "M0.01/miczek/N16: final time": true,
    "M0.01/miczek/N16: minimum_density_all_stages": true,
    "M0.01/miczek/N16: minimum_pressure_all_stages": true,
    "M0.01/miczek/N16: state_floor_count": true,
    "M0.01/miczek/N16: rejected_steps": true,
    "M0.01/miczek/N16: mass periodic balance": true,
    "M0.01/miczek/N16: x momentum periodic balance": true,
    "M0.01/miczek/N16: y momentum periodic balance": true,
    "M0.01/miczek/N16: total energy periodic balance": true,
    "M0.01/miczek/N16: finite physical diagnostics": true,
    "M0.01/miczek/N32: final time": true,
    "M0.01/miczek/N32: minimum_density_all_stages": true,
    "M0.01/miczek/N32: minimum_pressure_all_stages": true,
    "M0.01/miczek/N32: state_floor_count": true,
    "M0.01/miczek/N32: rejected_steps": true,
    "M0.01/miczek/N32: mass periodic balance": true,
    "M0.01/miczek/N32: x momentum periodic balance": true,
    "M0.01/miczek/N32: y momentum periodic balance": true,
    "M0.01/miczek/N32: total energy periodic balance": true,
    "M0.01/miczek/N32: finite physical diagnostics": true,
    "M0.01/miczek/N64: final time": true,
    "M0.01/miczek/N64: minimum_density_all_stages": true,
    "M0.01/miczek/N64: minimum_pressure_all_stages": true,
    "M0.01/miczek/N64: state_floor_count": true,
    "M0.01/miczek/N64: rejected_steps": true,
    "M0.01/miczek/N64: mass periodic balance": true,
    "M0.01/miczek/N64: x momentum periodic balance": true,
    "M0.01/miczek/N64: y momentum periodic balance": true,
    "M0.01/miczek/N64: total energy periodic balance": true,
    "M0.01/miczek/N64: finite physical diagnostics": true,
    "M0.1: preconditioned velocity error decreases across grids": true,
    "M0.1: finest preconditioned velocity_relative_l1": true,
    "M0.1: finest preconditioned pressure_dynamic_l1": true,
    "M0.1: finest preconditioned core_pressure_dynamic_l1": true,
    "M0.1: finest preconditioned / Roe velocity error": true,
    "M0.01: preconditioned velocity error decreases across grids": true,
    "M0.01: finest preconditioned velocity_relative_l1": true,
    "M0.01: finest preconditioned pressure_dynamic_l1": true,
    "M0.01: finest preconditioned core_pressure_dynamic_l1": true,
    "M0.01: finest preconditioned / Roe velocity error": true,
    "Fourier M0.1/roe: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.1/roe: maximum_energy_scaled_power_norm": true,
    "Fourier M0.1/miczek: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.1/miczek: maximum_energy_scaled_power_norm": true,
    "Fourier M0.01/roe: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.01/roe: maximum_energy_scaled_power_norm": true,
    "Fourier M0.01/miczek: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.01/miczek: maximum_energy_scaled_power_norm": true,
    "forward Euler counterexample at the chosen acoustic step": true,
    "analytic qualification: maximum_point_Euler_residual": true,
    "analytic qualification: maximum_quadrature_dynamic_difference": true,
    "analytic qualification: periodic_seam_velocity_bound": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/index.json

![保存した初版の全領域圧力誤差。M∞=.01、N64、T=.1、区分定数空間離散化。Miczek側の平均動圧規格化誤差.16537は固定閾値.1に不合格でした。物理条件と判定を変えず、両流束を同じ滑らかなMUSCLへ改訂した経緯を全領域で示します。 下段には改訂後の全領域も同じ色尺度で並べ、現在も全域圧力では前処理が必ずしも有利でない点を示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-first-order.png)

保存した初版の全領域圧力誤差。M∞=.01、N64、T=.1、区分定数空間離散化。Miczek側の平均動圧規格化誤差.16537は固定閾値.1に不合格でした。物理条件と判定を変えず、両流束を同じ滑らかなMUSCLへ改訂した経緯を全領域で示します。 下段には改訂後の全領域も同じ色尺度で並べ、現在も全域圧力では前処理が必ずしも有利でない点を示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Fabian Miczek, Friedrich K. Röpke and Philipp V. F. Edelmann (2015). New numerical solver for flows at various Mach numbers. https://arxiv.org/html/1409.8289; review_level=selected-author-version-full-text: Section8 Eq56; Section4 explicit-RK3 discussion; AppendixA variable transforms; Section6 smooth piecewise-linear reconstruction without a limiter
著者版の前処理行列・散逸項とRK3への言及を確認。今回は等エントロピー渦の短い時間区間に適用し、原著のGresho実験や暗黙積分を再現したとは扱いません。 6節の滑らかな問題に対するlimiterなしの区分線形再構築も確認し、改訂の独立した根拠とします。

- Wasilij Barsukow, Philipp V. F. Edelmann, Christian Klingenberg, Fabian Miczek and Friedrich K. Röpke (2017). A Numerical Scheme for the Compressible Low-Mach Number Regime of Ideal Fluid Dynamics. https://arxiv.org/html/1612.03910; review_level=selected-full-text: Section3 Eqs21,31,32; Section5 Eq83 and Fourier-mode stability discussion
前処理散逸P⁻¹|PA|、原始変数行列と前進Eulerの厳しい刻み制限を確認。SSPRK33での本固定入力のFourier診断・実段検査は別に実施し、一般の非線形安定性やSSP保証を借用しません。

- Seth C. Spiegel, H. T. Huynh and James R. DeBonis (2015). A Survey of the Isentropic Euler Vortex Problem using High-Order Methods. https://ntrs.nasa.gov/citations/20150018403; review_level=selected-primary-report: parameterized vortex definitions and Sections IV.B/IV.C boundary discussion
一般化された渦の定義と周期境界の相互作用・せん断層の説明を確認。独自のβ3・流速(1,.5)・M∞.1/.01を明示し、全平面解と有限周期箱の違いを保持します。NASA/FRソルバーや論文図の転載ではありません。

- Sigal Gottlieb and Chi-Wang Shu (1998). Total Variation Diminishing Runge-Kutta Schemes. https://www.cfm.brown.edu/people/sg/SSP1.pdf; review_level=author-bibliography and indexed author-PDF excerpts; direct PDF fetch unavailable
著者の書誌と著者PDFの索引抜粋で書誌・3次TVD法の位置付けを確認。PDFを直接通読したとは記録しません。係数は次の著者レビューのSSPRK(3,3)表示とも照合します。

- Sigal Gottlieb, Chi-Wang Shu and Eitan Tadmor (2001). Strong Stability-Preserving High-Order Time Discretization Methods. https://math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf; review_level=selected-full-author-PDF: Section4 Proposition4.1 Eq4.2 printedp100/PDFpage12; Section2.2 Lemma2.1 printedp92/PDFpage4
3段3次の更新係数と、前進Eulerの強安定性を前提にするSSPの条件を確認。今回のMiczek流束についてSSP・TVD・非線形安定性を一般保証せず、指定したFourier行列と実際の段状態を別途確認します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
