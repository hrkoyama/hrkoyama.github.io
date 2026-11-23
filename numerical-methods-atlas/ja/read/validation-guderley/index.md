# Guderley収束衝撃波：球対称の軽量検証

圧力ゼロの静止上流へ進むGuderley収束衝撃波を、γ=1.4、r∈[0,.75]、t=-1から-.85、128/256/512球殻のHLL＋Heunで計算します。R_s(-1)=.6の相似場から初期化し、原点到達前の衝撃軌道・保存量の球殻平均・保存収支を半解析参照と比較します。図は1D半径結果の2D断面表示です。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Guderley収束衝撃波：球対称の軽量検証

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-algorithm)

面積4πr²と球殻体積4πΔ(r³)/3を用いた第一次数の球対称有限体積法です。共有HLL面流束の発散に、半径方向運動量の圧力幾何項p_iΔA/Vを加え、Heun法・CFL=.4で更新します。中心は面積ゼロの反射条件、外側は各RK段の実時刻に評価した相似場です。全3保存量について実際の境界面流束と幾何ソースを同じHeun重みで積分します。状態floor、圧力修復、時間刻みの隠れた再試行はありません。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

未衝撃上流の圧力ゼロ・γ=1.4の理想気体Euler系の1次元球半径対称形。原点到達前の時区間、相似初期場、境界条件、球殻平均はこの固定入力で定義します。


**問題の図**

![Guderley収束衝撃波：球対称の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-validation)

33単体検査と3格子55判定を実行前に固定し、警告をエラーにする設定で合格しました。冷たい上流でのゼロ音速HLL分岐、幾何的な静止圧力釣合い、共有流束の収支、実際の2段の境界時刻、不正段の生配列保持を確認します。全体積L1と、あらかじめr≥.8Rsとした衝撃・非零流れ領域のL1を並べ、冷たい内側で誤差を薄めないようにします。密度・圧力の最大差と保存した時系列からの衝撃軌道も残します。半解析参照は固定LANL ExactPackの相似指数固有値ルーチンとODEを使い、反射後分岐を計算しないキャッシュ付きアダプターです。独自に再実装した相似ODEとは表示しません。別に実装したEuler有限体積計算と参照を比較します。 全体積の密度L1は.02345/.01339/.007722、圧力L1は.03277/.01743/.009477でした。r≥.8Rsの密度L1も.02414/.01378/.007948と減少します。最細の衝撃位置は.530273、相似参照は.533989で、差は約2.54セルです。最大の全3成分収支残差は8.85e-16、全段の最小内部エネルギーと音速専用丸めガード回数はともに0でした。参照のEuler差分代入残差は8.24e-9、有限オフセットの移動衝撃ジャンプ残差は4.40e-8。固有値計算を含む全3計算は元のMacで約44.6秒でした。

- [Guderley収束衝撃波：固有値と球対称の半解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja) (`guderley`; 同じ問題の参照 · 半解析参照)

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。ExactPackに基づく参照実装と有限体積PDE計算の役割を分け、独立した相似解実装どうしの照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。
### 前提・単位・境界

γ=1.4、球対称3次元の半径r∈[0,.75]、衝撃半径Rs(−1)=.6、時間t∈[−1,−.85]を固定します。衝撃前方の内側はρ0=1、u0=p0=0です。外側には初めから衝撃後の相似場があり、領域全体が冷たい一様気体という初期条件ではありません。初期保存量は衝撃位置で積分区間を分けた16点Gauss球殻体積平均とし、32点と照合します。圧力参照はp(保存量平均)で、原始圧力の体積平均とは区別します。

**編集上の補足**

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。ExactPackに基づく参照実装と有限体積PDE計算の役割を分け、独立した相似解実装どうしの照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。 全体積の密度・圧力L1と、事前固定したr≥.8R_sの活性領域L1は3格子で減少しましたが、衝撃層の密度・圧力L∞やセル幅単位の衝撃位置差は単調減少しません。原点への収束や細部の高次収束は主張しません。冷たい上流を含め最小内部エネルギー密度は今回0で、許容帯内の音速平方根ガードも全3計算で0回でした。

### 採用した計算法

面積4πr²と球殻体積4πΔ(r³)/3を用いた第一次数の球対称有限体積法です。共有HLL面流束の発散に、半径方向運動量の圧力幾何項p_iΔA/Vを加え、Heun法・CFL=.4で更新します。中心は面積ゼロの反射条件、外側は各RK段の実時刻に評価した相似場です。全3保存量について実際の境界面流束と幾何ソースを同じHeun重みで積分します。状態floor、圧力修復、時間刻みの隠れた再試行はありません。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

### 比較・検証

33単体検査と3格子55判定を実行前に固定し、警告をエラーにする設定で合格しました。冷たい上流でのゼロ音速HLL分岐、幾何的な静止圧力釣合い、共有流束の収支、実際の2段の境界時刻、不正段の生配列保持を確認します。全体積L1と、あらかじめr≥.8Rsとした衝撃・非零流れ領域のL1を並べ、冷たい内側で誤差を薄めないようにします。密度・圧力の最大差と保存した時系列からの衝撃軌道も残します。半解析参照は固定LANL ExactPackの相似指数固有値ルーチンとODEを使い、反射後分岐を計算しないキャッシュ付きアダプターです。独自に再実装した相似ODEとは表示しません。別に実装したEuler有限体積計算と参照を比較します。 全体積の密度L1は.02345/.01339/.007722、圧力L1は.03277/.01743/.009477でした。r≥.8Rsの密度L1も.02414/.01378/.007948と減少します。最細の衝撃位置は.530273、相似参照は.533989で、差は約2.54セルです。最大の全3成分収支残差は8.85e-16、全段の最小内部エネルギーと音速専用丸めガード回数はともに0でした。参照のEuler差分代入残差は8.24e-9、有限オフセットの移動衝撃ジャンプ残差は4.40e-8。固有値計算を含む全3計算は元のMacで約44.6秒でした。

### 確認の限界

収束点t=0から離れた短い時間窓の1次元球対称検証です。原点の特異点、原点反射後、円筒対称、他のγ、一般摂動や非球対称の安定性は未検証です。2次元の図は保存した球殻平均を子午面へ表示したもので、2次元Cartesian計算ではありません。半解析場もODEと求積を数値評価した参照であり、閉形式の厳密セル平均ではありません。冷たい上流では圧力ゼロを許し、64epsの絶対内部エネルギー密度までの丸めによる負値を記録します。許容帯だけの音速平方根ガードは状態修復と分けて回数・最小圧力を残し、非線形正値性の一般保証は主張しません。 衝撃位置のセル単位誤差は1.13/2.27/2.54と単調に減りません。半径の絶対誤差は最初の2格子で同じ約.00665、最細で約.00372です。密度L∞差は.258/.271/.266、圧力L∞差は.492/.494/.466で、いずれも単調な減少を主張できません。L1の減少を衝撃内部の点ごとの解像や原点付近の収束へ拡張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 512,
    "time": -0.85,
    "steps": 285,
    "density_l1": 0.00772161862650073,
    "pressure_l1": 0.00947688731818041,
    "active_density_l1": 0.007948322269523746,
    "active_pressure_l1": 0.009476887318180412,
    "density_linf": 0.26559799254635363,
    "pressure_linf": 0.4664641041357883,
    "maximum_velocity_error": 0.2918302634973315,
    "active_volume_fraction": 0.8145022392272949,
    "active_inner_radius": 0.4271911929633472,
    "shock_radius": 0.5302734375,
    "reference_shock_radius": 0.533988991204184,
    "shock_error_cells": 2.536484662056258,
    "maximum_history_shock_error_cells": 2.536484662056258,
    "minimum_density_all_stages": 1.0,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_energy_all_stages": 0.0,
    "sound_speed_roundoff_guard_evaluations": 0,
    "minimum_pressure_at_sound_speed_guard": 0.0,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "minimum_dt": 0.0004970499254967065,
    "maximum_dt": 0.000537015606799512,
    "reference_quadrature_density_l1": 4.607326285502161e-15,
    "reference_quadrature_pressure_l1": 8.295849629501113e-15,
    "initial_reference_quadrature_density_l1": 1.4522743666682576e-15,
    "initial_reference_quadrature_pressure_l1": 3.208009534299476e-15
  },
  "checks": {
    "all three fixed spherical runs completed": true,
    "N128: final time before collapse": true,
    "N128: strictly positive density all stages": true,
    "N128: minimum_internal_energy_all_stages": true,
    "N128: minimum_pressure_at_sound_speed_guard": true,
    "N128: state_floor_count": true,
    "N128: rejected_steps": true,
    "N128: mass discrete balance": true,
    "N128: radial momentum including geometric source discrete balance": true,
    "N128: energy discrete balance": true,
    "N128: reference_quadrature_density_l1": true,
    "N128: reference_quadrature_pressure_l1": true,
    "N128: initial_reference_quadrature_density_l1": true,
    "N128: initial_reference_quadrature_pressure_l1": true,
    "N128: maximum and trajectory diagnostics retained": true,
    "N256: final time before collapse": true,
    "N256: strictly positive density all stages": true,
    "N256: minimum_internal_energy_all_stages": true,
    "N256: minimum_pressure_at_sound_speed_guard": true,
    "N256: state_floor_count": true,
    "N256: rejected_steps": true,
    "N256: mass discrete balance": true,
    "N256: radial momentum including geometric source discrete balance": true,
    "N256: energy discrete balance": true,
    "N256: reference_quadrature_density_l1": true,
    "N256: reference_quadrature_pressure_l1": true,
    "N256: initial_reference_quadrature_density_l1": true,
    "N256: initial_reference_quadrature_pressure_l1": true,
    "N256: maximum and trajectory diagnostics retained": true,
    "N512: final time before collapse": true,
    "N512: strictly positive density all stages": true,
    "N512: minimum_internal_energy_all_stages": true,
    "N512: minimum_pressure_at_sound_speed_guard": true,
    "N512: state_floor_count": true,
    "N512: rejected_steps": true,
    "N512: mass discrete balance": true,
    "N512: radial momentum including geometric source discrete balance": true,
    "N512: energy discrete balance": true,
    "N512: reference_quadrature_density_l1": true,
    "N512: reference_quadrature_pressure_l1": true,
    "N512: initial_reference_quadrature_density_l1": true,
    "N512: initial_reference_quadrature_pressure_l1": true,
    "N512: maximum and trajectory diagnostics retained": true,
    "similarity qualification: maximum_scaled_euler_residual": true,
    "similarity qualification: maximum_scaled_jump_residual": true,
    "similarity exponent agrees with tabulated lambda": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "finest active_density_l1": true,
    "finest active_pressure_l1": true,
    "finest shock_error_cells": true,
    "density_l1 decreases across the three grids": true,
    "active_density_l1 decreases across the three grids": true,
    "pressure_l1 decreases across the three grids": true,
    "last-pair active density L1 slope": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/atlas-guderley-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. Guderley (1942). Starke kugelige und zylindrische Verdichtungsstöße in der Nähe des Kugelmittelpunktes bzw. der Zylinderachse. https://raw.githubusercontent.com/lanl/ExactPack/9bacc477eb791e959c9621e771fc7a725db755fa/doc/source/references.rst; review_level=bibliographic attribution only: year/volume/first page in pinned ExactPack bibliography, title in Lazarus1981 publisher bibliography; original1942 article not inspected
  原問題の歴史的出典。固定ExactPackの書誌で著者・年・巻・開始頁302を、Lazarus1981の出版社参考文献で題名を確認。原著1942本文は未閲覧で、相似場の式や今回の実測を原著から直接再現したとは主張しません。
- Scott D. Ramsey, James R. Kamm and John H. Bolstad (2012). The Guderley problem revisited. https://laro.lanl.gov/esploro/outputs/journalArticle/The-Guderley-problem-revisited/9916364702403761; review_level=primary institutional bibliographic record and abstract; actual implementation equations reviewed in pinned ExactPack source, not full original paper
  LANLの書誌・抄録で収束側の相似指数と反射後の軌道係数が別の固有値問題であることを確認。原論文の全文通読や原著のPDE計算再現とは扱わず、今回の場は固定ExactPackソースを実際に用いて構成します。
- Roger B. Lazarus (1981). Self-Similar Solutions for Converging Shocks and Collapsing Cavities. https://epubs.siam.org/doi/10.1137/0718022; review_level=publisher bibliographic record/abstract plus equations2.5,2.8,2.9 and sphericalTable6.5 as explicitly transcribed in pinned ExactPack; original full text not inspected
  出版社の書誌・抄録と、ExactPackが明示する式2.5/2.8/2.9・球対称表6.5の転記を確認。λ=1.3943607838の表値はコード内の転記値で、元論文を独立に再転記した値とは区別します。
- R. F. Chisnell (1998). An analytic description of converging shock waves. https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/an-analytic-description-of-converging-shock-waves/1D3D7014FF4C6297A5F6DC9BCFDBE0E8; review_level=publisher bibliographic record/abstract and equation3.1 implementation/comments in actual pinned ExactPack eexp source
  出版社の書誌・抄録と、ExactPack eexpが採用する臨界点の位相差・式3.1の実装を確認。相似指数は寸法解析から固定せず、固定コードの固有値計算で求めます。
- Jasper Thrussell and Jim Michael Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://www.osti.gov/servlets/purl/2204208; review_level=primary OSTI accepted manuscript/search text; software metadata and Guderley registry; selected actual source files pinned separately
  ExactPackのソフトウェア論文とGuderley収録を参照。論文記載版1.7.5と今回用いるソースの固定コミットは区別し、配布物内にソース・SHA・BSDライセンスを保存します。
- Los Alamos National Laboratory / ExactPack contributors (2025). ExactPack Guderley solver, pinned source. https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/guderley; review_level=selected source files and license inspected; eexp,ramsey.state/g,interp_laz and official test fixtures; actual execution recorded separately
  固定版のeexp・ramseyの前収束ODEとstate、表の転記、公式回帰値、BSD3条項を確認。全ExactPackテストを実行したとは扱いません。参照の実行成否はqualification.jsonに別記します。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
