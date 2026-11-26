# 可変Eddington因子・テンソルの軽量検証

正の等方輻射源を持つ周期問題で、角度輸送と独立したモーメント解を反復し、解析参照・収支・空間と角度の誤差を分けて確認します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 可変エディントン因子：周期1D散乱源の固定検証

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

**使用手法**

- [可変Eddington因子（1D VEF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja) (`variable-eddington-factor`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-algorithm)

各反復でq+σs E_LOをFourier形式解へ入れ、f=Kxx/E_HOを抽出し、保存的な面流束を使う有限差分モーメント式を解きます。参照解は主計算の閉包へ渡しません。

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`)

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。


**問題の図**

![可変エディントン因子：周期1D散乱源の固定検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-validation)

N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。

- [本例のために導出した周期1D VEFの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja) (`vef-fourier-scattering1d`; 同じ問題の参照 · 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
### 前提・単位・境界

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。

**編集上の補足**

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

### 採用した計算法

各反復でq+σs E_LOをFourier形式解へ入れ、f=Kxx/E_HOを抽出し、保存的な面流束を使う有限差分モーメント式を解きます。参照解は主計算の閉包へ渡しません。

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

### 比較・検証

N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。

### 確認の限界

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 3.0084362898696935e-05,
    "finest_face_H_relative_rms_error": 0.0001843336208869165,
    "finest_mode_complex_relative_error": 0.00046313206947184505,
    "finest_D_component_max_abs_error": 2.562663219352057e-06,
    "E_error_refinement_ratio": 0.2575572363841145,
    "face_H_error_refinement_ratio": 0.25786212296040795,
    "HO_LO_gap_refinement_ratio": 0.2575572378802047,
    "angle_probe_E_relative_rms_difference": 7.903639960737542e-15,
    "angle_probe_D_max_abs_difference": 7.216449660063518e-15,
    "finest_nonconstant_f_span": 0.019387902446938998,
    "finest_max_abs_Dxy": 0.0,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/index.json

![保存した点値・面流束の誤差、空間細分化、角度プローブと反復履歴。一定源は別制御です。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d-diagnostics.png)

保存した点値・面流束の誤差、空間細分化、角度プローブと反復履歴。一定源は別制御です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations [accessed 2026-11-26]. https://academic.oup.com/mnras/article/149/1/65/2604466; review_level=primary-publisher-abstract-and-bibliography
選択箇所のみの読解です。出版社抄録・書誌のみ。原PDFの式・試験は未読であり、再現の主張はありません。

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers [accessed 2026-11-26]. https://arxiv.org/pdf/2111.12255; review_level=selected-primary-method-scope
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 可変エディントンテンソル：周期2D非平行源の固定検証

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

**使用手法**

- [可変Eddingtonテンソル（VET）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja) (`variable-eddington-tensor`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-algorithm)

形式的なFourier角度輸送→D=K_HO/E_HO→独立な有限差分モーメント式を反復します。Dxyの両交差微分を共有面流束へ含め、局所・大域の離散収支を確認します。

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`)

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。


**問題の図**

![可変エディントンテンソル：周期2D非平行源の固定検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-validation)

17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。

- [本例のために導出した周期2D VETの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja) (`vet-fourier-source2d`; 同じ問題の参照 · 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。
### 前提・単位・境界

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。

**編集上の補足**

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

### 採用した計算法

形式的なFourier角度輸送→D=K_HO/E_HO→独立な有限差分モーメント式を反復します。Dxyの両交差微分を共有面流束へ含め、局所・大域の離散収支を確認します。

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

### 比較・検証

17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。

### 確認の限界

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 0.00012228131179061114,
    "finest_face_H_relative_rms_error": 0.0010738390026674726,
    "finest_mode_complex_relative_error": 0.0017983436413314031,
    "finest_D_component_max_abs_error": 1.0250275895629102e-05,
    "E_error_refinement_ratio": 0.2655289724016241,
    "face_H_error_refinement_ratio": 0.26613409578253794,
    "HO_LO_gap_refinement_ratio": 0.2657021024383582,
    "angle_probe_E_relative_rms_difference": 2.3900276798110385e-07,
    "angle_probe_D_max_abs_difference": 2.4197709053153105e-07,
    "finest_nonconstant_f_span": 0.022629325122685784,
    "finest_max_abs_Dxy": 0.0052432003949135775,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/index.json

![保存した面流束誤差・Dzz・空間/角度比較と反復残差。全3×3テンソルを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d-diagnostics.png)

保存した面流束誤差・Dzz・空間/角度比較と反復残差。全3×3テンソルを保持します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2223; review_level=selected-primary-equations-and-test-description
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Radiation Transfer Solver for Athena using Short Characteristics [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2222; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method [accessed 2026-11-26]. https://arxiv.org/pdf/1306.0010; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
