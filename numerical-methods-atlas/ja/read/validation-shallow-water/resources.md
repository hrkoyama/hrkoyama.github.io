# 浅水流：地形・静止湖・乾燥床

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Godunov型有限体積法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja>)

  非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [Godunov型有限体積法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja>)

  同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [Godunov型有限体積法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja>)
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

## 方程式

- [地形源項付き浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja>)

  摩擦・降雨なしの1次元Saint–Venant系。連続の地形と、保存平均から表現した区分定数の床を区別し、静水再構成の釣合いを確認します。 真の乾燥状態h=q=0では運動量の移流流束q²/hを0と定義します。 1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。
- [浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja>)

  前2式は平坦床・摩擦なしの1次元系。後2行は水深Hまわりの線形回転系。非線形流れのテストと、回転系のFourier記号の検証を区別します。 平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、800/1600/3200セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。
- [地形源項付き浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja>)

  摩擦・降雨なしの1次元Saint–Venant系。連続の地形と、保存平均から表現した区分定数の床を区別し、静水再構成の釣合いを確認します。 真の乾燥状態h=q=0では運動量の移流流束q²/hを0と定義します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-algorithm>)

  非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-algorithm>)

  同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。
- [浅水方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja>)

  前2式は平坦床・摩擦なしの1次元系。後2行は水深Hまわりの線形回転系。非線形流れのテストと、回転系のFourier記号の検証を区別します。

## 問題の図

- [SWASHES地形上の静止湖・定常浅水流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png
- [乾燥床へのRitter破堤流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png
- [SWASHES地形流：静水と非零流量の定常解](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png
- [乾いた河床のダム破壊：実際のwetting/drying](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png

## 厳密解・参照解

- [SWASHES地形上の静止湖・定常浅水流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#references-ja>)

  31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。
- [静止湖：表現した床の上の湿潤・露出平衡](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 g9.81、[0,25]m、200セル。8<x<12の放物線床z=.2−.05(x−10)²をセルごとにGauss8で平均し、h_i=max(η₀−z_i,0)、q_i=0、η₀=.5/.1mを初期化します。静水再構成が保つのはこの表現した区分定数床の平衡であり、連続床上の水深平均をそのまま使う別問題ではありません。 静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
- [SWASHES定常流：非射流Bernoulli根](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 g9.81、[0,25]m、同じ放物線床、流量q4.42m²/s、下流h2m。h+z+q²/(2gh²)=2+q²/(8g)の非射流根を別の二分法で求め、セル平均求積を比較します。100/200/400セルのPDE計算は定常参照から初期化してt2まで進め、SWASHESの静止状態からの過渡計算そのものは再現しません。 静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
- [乾燥床へのRitter破堤流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#references-ja>)

  全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。
- [Ritter乾燥床破堤：g9.81の専用セル平均参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 平坦・摩擦なしの[-10,10]m、堰x0=0、hL1m/hR0、初速0、g9.81、t.5s。左波頭−sqrt(g)tと真の乾燥前縁2sqrt(g)tで分割して保存量(h,hu)をセル平均します。固定水深.001mの等値線も区別します。旧参照カードと重力・領域・時刻の異なる専用入力で、旧値は変更しません。 前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。
- [浅水／乾床への膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。 既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。
- [静止湖：表現した床の上の湿潤・露出平衡](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja>)
  reference_kind: analytic

  解析解 g9.81、[0,25]m、200セル。8<x<12の放物線床z=.2−.05(x−10)²をセルごとにGauss8で平均し、h_i=max(η₀−z_i,0)、q_i=0、η₀=.5/.1mを初期化します。静水再構成が保つのはこの表現した区分定数床の平衡であり、連続床上の水深平均をそのまま使う別問題ではありません。
- [SWASHES定常流：非射流Bernoulli根](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja>)
  reference_kind: semi-analytic

  半解析解 g9.81、[0,25]m、同じ放物線床、流量q4.42m²/s、下流h2m。h+z+q²/(2gh²)=2+q²/(8g)の非射流根を別の二分法で求め、セル平均求積を比較します。100/200/400セルのPDE計算は定常参照から初期化してt2まで進め、SWASHESの静止状態からの過渡計算そのものは再現しません。
- [Ritter乾燥床破堤：g9.81の専用セル平均参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja>)
  reference_kind: analytic

  解析解 平坦・摩擦なしの[-10,10]m、堰x0=0、hL1m/hR0、初速0、g9.81、t.5s。左波頭−sqrt(g)tと真の乾燥前縁2sqrt(g)tで分割して保存量(h,hu)をセル平均します。固定水深.001mの等値線も区別します。旧参照カードと重力・領域・時刻の異なる専用入力で、旧値は変更しません。
- [SWASHES地形流：静水と非零流量の定常解：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-validation>)

  31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。
- [静止湖：表現した床の上の湿潤・露出平衡](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 g9.81、[0,25]m、200セル。8<x<12の放物線床z=.2−.05(x−10)²をセルごとにGauss8で平均し、h_i=max(η₀−z_i,0)、q_i=0、η₀=.5/.1mを初期化します。静水再構成が保つのはこの表現した区分定数床の平衡であり、連続床上の水深平均をそのまま使う別問題ではありません。 静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
- [SWASHES定常流：非射流Bernoulli根](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 g9.81、[0,25]m、同じ放物線床、流量q4.42m²/s、下流h2m。h+z+q²/(2gh²)=2+q²/(8g)の非射流根を別の二分法で求め、セル平均求積を比較します。100/200/400セルのPDE計算は定常参照から初期化してt2まで進め、SWASHESの静止状態からの過渡計算そのものは再現しません。 静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
- [乾いた河床のダム破壊：実際のwetting/drying：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-validation>)

  全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。
- [Ritter乾燥床破堤：g9.81の専用セル平均参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 平坦・摩擦なしの[-10,10]m、堰x0=0、hL1m/hR0、初速0、g9.81、t.5s。左波頭−sqrt(g)tと真の乾燥前縁2sqrt(g)tで分割して保存量(h,hu)をセル平均します。固定水深.001mの等値線も区別します。旧参照カードと重力・領域・時刻の異なる専用入力で、旧値は変更しません。 前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。
- [浅水／乾床への膨張波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。 既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

## コード・検証

- [SWASHES地形流：静水と非零流量の定常解](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja>)
  availability: run

  水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。
- [乾いた河床のダム破壊：実際のwetting/drying](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja>)
  availability: run

  右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。
