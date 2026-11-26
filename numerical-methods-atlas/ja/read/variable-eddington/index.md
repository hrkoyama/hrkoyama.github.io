# 可変Eddington因子・テンソル：角度輸送でモーメントを閉じる

VEFは角度輸送からEddington閉包を求め、別のモーメント方程式と反復する方法です。1Dではスカラー因子f、多次元ではテンソルDを使います。VETはこのテンソル形を指し、VEFと無関係な別の物理モデルという意味ではありません。

## 灰色近似・拡散・M1との違い

灰色近似は周波数を積分する選択です。一方、VEF/VETは角度分布から圧力閉包を求めます。灰色であることだけでは、拡散近似やM1、VEFのどれを使うかは決まりません。

ここでは静止媒質、一定の全減衰係数σtと等方散乱係数σs、正の等方輻射源qを扱います。角度平均をdΩ/(4π)、c=1とし、E・H・Kは規格化したエネルギー・流束・圧力モーメントです。通常の角度積分による物理量には共通の4π因子を戻します。

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad\langle g\rangle=\frac{1}{4\pi}\int_{S^2}g\,d\Omega
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{E},\quad\mathsf K=\mathsf DE,\quad f= D_{xx}
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf DE)=0,\quad\sigma_a=\sigma_t-\sigma_s
$$

## 角度輸送とモーメント解の反復

現在のモーメント解Eからq+σsEを作り、角度ごとの輸送方程式を解きます。その強度からDを計算し、別に離散化したモーメント方程式を解いてEを更新します。Dを図にするだけでなく、この更新を角度輸送へ戻します。

本例の形式解は周期Fourier表現です。低次系には共有面流束を持つ有限差分を使い、Dxyを含む交差微分も保持します。原典のshort characteristicsや高次混合有限要素をそのまま再現した実装ではありません。

内側の線形残差と、外側のE・Dの更新量を別々に確認します。角度輸送とモーメントは異なる空間離散化なので、固定格子で両者のEが完全一致することを停止条件にはしません。

$$
\sigma_t\sigma_aE-\sum_{i,j}\partial_i\partial_j(D_{ij}E)=\sigma_tq
$$

## 1D VEF：周期散乱場

単位周期でq=1+0.3cos(2πx)、σt=4、σs=3を固定します。角度分布I(x,μ)からf(x)=Kxx/Eを求め、独立したスカラー・モーメント解を解析参照と比較します。

図の縦軸μは方向余弦であり、第2の物理的な空間座標ではありません。f=1/3に固定した対照計算と区別し、空間格子の比較と角度点数の比較を別の行として保存します。

[1D VEFの図・固定入力・解析参照・実行コード](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja)

## 2D VET：非平行な輻射源モード

単位周期正方形でq=1+0.3cos(2πx)+0.2sin(2π(x+y))を固定します。異なる方向の2モードによりDxyが非零となり、場所によってテンソルの主軸が変わります。

空間は2Dでも角度測度は球面S²です。Dzzを含む3×3テンソルを保持し、対称性・跡1・正値性・角度分布の実現可能性を確認します。局所的なEとHから作るM1テンソルは診断用の比較であり、この例でM1の時間発展ソルバーを実装したとは表示しません。

[2D VETの図・固定入力・解析参照・実行コード](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja)

## 独立な解析参照

正の等方輻射源を先に指定し、各Fourierモードの連続角度積分から参照解を導きます。強度や閉包を先に選んで外力を逆算した製造解ではありません。一次コードは解析参照を読み込んでDを作りません。

kの方向を極軸に取り、1/(σt+ikμ)を積分するとR(k)=atan(k/σt)/kです。散乱の自己結合を解いた振幅AからE・H・Kを別モジュールで評価します。sinモードの複素位相も比較し、一定の背景値だけで誤差が小さく見えないようにします。

$$
R(k)=\frac{\tan^{-1}(k/\sigma_t)}{k},\quad A_m=\frac{b_m}{1-\sigma_sR(|\boldsymbol k_m|)},\quad E_{\rm ref}=\frac{q_0}{\sigma_a}+\operatorname{Re}\sum_m A_mR(|\boldsymbol k_m|)e^{i\boldsymbol k_m\cdot\boldsymbol x}
$$

## 確認する範囲と限界

2つの固定問題は、静止・灰色・線形等方散乱・一定係数・周期境界に限定します。流入境界のVEF境界因子、真空境界、強い吸収体の影、交差ビーム、気体連成、時間発展、多周波数や相対論的輸送を検証するものではありません。

原典からは方程式・閉包・反復の該当箇所を参照します。原典の全実験やAthenaの再現、普遍的な収束次数・高速化率、固定格子での拡散極限のAP性を主張しません。

## 結果を確認する順序

まず強度とEの正値性、テンソルの跡・固有値、面流束の収支を確認します。次に線形残差と外側反復の収束を見て、解析参照との場・モード振幅・位相の誤差を比べます。

空間格子を変えた行と角度を変えた行を混ぜず、HO/LOの格子依存の差も保存します。定数解、交差微分の符号、散乱フィードバックの省略、固定1/3閉包の対照を使い、単に残差が小さいだけでは合格しないようにします。各版の実測値と判定は、下の実行入口と配布ZIPの記録で確認できます。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 可変エディントン因子：周期1D散乱源の固定検証

固定標的の計算例

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-variable-eddington-controls/#vef-fourier-scattering1d) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py) · [コード primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py) · [コード analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py) · [テスト test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py) · [ZIP](/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [結果](/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json) · [追試記録](/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

### 可変エディントンテンソル：周期2D非平行源の固定検証

固定標的の計算例

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-variable-eddington-controls/#vet-fourier-source2d) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py) · [コード primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py) · [コード analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py) · [テスト test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py) · [ZIP](/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [結果](/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json) · [追試記録](/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

## 公開範囲

1群・2つの軽量な固定検証例です。VEFとVETはスカラー形とテンソル形の関係を持ち、格子・角度・対照計算の行数を独立した物理問題数には数えません。

## 文献

- L. H. Auer and Dimitri Mihalas (1970). On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations. https://doi.org/10.1093/mnras/149.1.65
- Samuel Olivier and Terry S. Haut (2023). High-Order Mixed Finite Element Variable Eddington Factor Methods. https://arxiv.org/pdf/2301.04758
- Samuel Olivier and Will Pazner and Terry S. Haut and Ben C. Yee (2023). A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers. https://doi.org/10.1016/j.jcp.2022.111747
- Yan-Fei Jiang and James M. Stone and Shane W. Davis (2012). A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor. https://doi.org/10.1088/0067-0049/199/1/14
- Shane W. Davis and James M. Stone and Yan-Fei Jiang (2012). A Radiation Transfer Solver for Athena using Short Characteristics. https://arxiv.org/pdf/1201.2222
- M. Aaron Skinner and Eve C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method. https://doi.org/10.1088/0067-0049/206/2/21
