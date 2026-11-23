# 低Mach等エントロピー渦：前処理Roe流束の軽量検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-low-mach/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [直交座標の原KEEP分割流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [Roe法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [低Mach数のPDE前処理](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。
- [Roe法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja>)
- [低Mach数のPDE前処理](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-algorithm>)

  同じ無制限の中心原始変数MUSCL再構築・有限体積・物理Euler流束・SSPRK(3,3)を使い、Roe散逸だけをD=P⁻¹|PA|で前処理します。Roe平均の全流速Machからμ=min(1,max(Mlocal,M∞))、δ=1/μ−1とし、原始変数のMiczek行列を保存量へ変換します。行列絶対値は特性値ũn,ũn±τの2次多項式で作用させ、別の密行列固有分解と照合します。物理時間微分・音速は変えず、音響CFL=.2を使います。再構築した両面と各3段の正のρ,pを確認し、limiter・floor・状態修復・隠れた再試行・疑似時間反復はありません。前進Eulerの増幅反例を示すため、SSP・TVD・非線形安定性を名前だけで保証しません。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [周期移動等エントロピー渦](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png
- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png

## 厳密解・参照解

- [周期移動等エントロピー渦：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja>)

  従来KEEPの等エントロピー渦と同じ解析解族に、背景Mach数.1/.01の整合した圧力・密度スケーリングを加えた比較です。解析場は全平面Eulerの移動解で、有限周期箱の微小な裾と保存量セル平均の数値求積は別に資格確認します。
- [等エントロピー渦：低Mach比較に用いるEuler解析場](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 全平面Eulerの移動等エントロピー渦を、γ=1.4、β=3、背景密度1、背景速度U=(1,.5)で定義します。背景Mach数Mに対してp∞=1.25/(1.4M²)とし、θ=1−(γ−1)β²exp(1−r²)/(8γπ²p∞)、ρ=θ^(1/(γ−1))、p=p∞θ^(γ/(γ−1))です。Uとともに動く座標を[-10,10]²へ折り返します。解析式は全平面の厳密なEuler解ですが、有限周期箱の継ぎ目にはゼロでないGaussianの裾があり、滑らかな周期トーラスの厳密解とは区別します。4保存量のセル平均をGauss8で求積しGauss16と照合した後、圧力・速度へ変換します。閉形式の厳密セル平均やprimitive変数の平均ではありません。低Mach固定例はM=.1/.01、T=.1。p∞=1で従来KEEPの場へ戻ります。 同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。
- [等エントロピー渦：低Mach比較に用いるEuler解析場](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja>)
  reference_kind: analytic

  解析解 全平面Eulerの移動等エントロピー渦を、γ=1.4、β=3、背景密度1、背景速度U=(1,.5)で定義します。背景Mach数Mに対してp∞=1.25/(1.4M²)とし、θ=1−(γ−1)β²exp(1−r²)/(8γπ²p∞)、ρ=θ^(1/(γ−1))、p=p∞θ^(γ/(γ−1))です。Uとともに動く座標を[-10,10]²へ折り返します。解析式は全平面の厳密なEuler解ですが、有限周期箱の継ぎ目にはゼロでないGaussianの裾があり、滑らかな周期トーラスの厳密解とは区別します。4保存量のセル平均をGauss8で求積しGauss16と照合した後、圧力・速度へ変換します。閉形式の厳密セル平均やprimitive変数の平均ではありません。低Mach固定例はM=.1/.01、T=.1。p∞=1で従来KEEPの場へ戻ります。
- [低Mach等エントロピー渦：前処理Roe流束の軽量検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-validation>)

  初版の32単体検査は合格しましたが、区分定数空間離散化での143判定中、M∞=.01・最細格子の全領域圧力誤差.16537が事前閾値.1を超えました。初版ソース・契約・全12場・判定と、その全領域図を失敗のまま保存します。改訂では両流束を同じ無制限中心原始変数MUSCLにし、面状態の拒否・正しい再構築Fourier記号・独立行列を使う実RHSの線形化など3検査を追加しました。入力・物理時間・CFL・受入条件はバイト単位で不変です。新35検査と143条件の契約を改訂の実行前に固定しました。 Roe平均の保存量ジャンプと物理流束差、密行列の前処理散逸、3段更新・不正段保持を照合します。各背景Mach・流束で17²個の定数状態Fourierモードと、物理音響エネルギーで規格化した増幅行列の1/10/100乗を調べます。圧力誤差は大きなp∞ではなくρ∞|U∞|²で割り、速度誤差は渦の速度変動で規格化します。移動解析場に対する初期R_h−q_tも記録し、定常残差の収束とは区別します。 改訂の35検査・全12計算143判定は-W errorで合格し、元のMacで全計算は約4.4秒でした。最細M∞=.01の速度相対L1はRoe .07411、前処理 .01847、固定コアの圧力誤差は.04871/.0006325でした。一方、全領域の圧力誤差は.01194/.01260で前処理側がわずかに悪く、M∞=.1でも.0006653/.0006737と同様です。全4保存量の最大相対残差は4.24e-14。Gauss8/16の動的スケール最大差は4.08e-11、解析Euler代入残差は1.09e-16でした。指定したFourierモードのSSPRK3増幅半径とエネルギー規格化行列累乗ノルムは最大1。前進Eulerは両MUSCL流束で1を超え、M∞=.01の前処理側で約1.03560でした。
- [等エントロピー渦：低Mach比較に用いるEuler解析場](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 全平面Eulerの移動等エントロピー渦を、γ=1.4、β=3、背景密度1、背景速度U=(1,.5)で定義します。背景Mach数Mに対してp∞=1.25/(1.4M²)とし、θ=1−(γ−1)β²exp(1−r²)/(8γπ²p∞)、ρ=θ^(1/(γ−1))、p=p∞θ^(γ/(γ−1))です。Uとともに動く座標を[-10,10]²へ折り返します。解析式は全平面の厳密なEuler解ですが、有限周期箱の継ぎ目にはゼロでないGaussianの裾があり、滑らかな周期トーラスの厳密解とは区別します。4保存量のセル平均をGauss8で求積しGauss16と照合した後、圧力・速度へ変換します。閉形式の厳密セル平均やprimitive変数の平均ではありません。低Mach固定例はM=.1/.01、T=.1。p∞=1で従来KEEPの場へ戻ります。 同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。

## コード・検証

- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja>)
  availability: run

  同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。
