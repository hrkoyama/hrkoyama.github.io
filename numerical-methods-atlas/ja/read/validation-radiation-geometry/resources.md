# 2Dの影・ビームとM1閉包

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-geometry/

この章に登録された手法・問題・実行例の関連資料です。 吸収体の影と衝突するビームを角度法とM1で計算し、M1自体の製造解による検査と分けて示します。

## 手法

- [放射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [放射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [放射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

## 方程式

- [静止媒質の灰色放射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを放射・物質の両交換項に掛けます。 2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。
- [静止媒質・平坦時空の灰色M1モーメント](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja>)

  c=1、2D空間で3D圧力のPzzを保持。等方・真空分岐、閉じたPDEの製造解、角度法とのビーム差を区別し、相対論的放射流体とは扱いません。 2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。
- [静止媒質の灰色放射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを放射・物質の両交換項に掛けます。 2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。
- [静止媒質・平坦時空の灰色M1モーメント](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja>)

  c=1、2D空間で3D圧力のPzzを保持。等方・真空分岐、閉じたPDEの製造解、角度法とのビーム差を区別し、相対論的放射流体とは扱いません。 2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。
- [静止媒質・平坦時空の灰色M1モーメント](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja>)

  c=1、2D空間で3D圧力のPzzを保持。等方・真空分岐、閉じたPDEの製造解、角度法とのビーム差を区別し、相対論的放射流体とは扱いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-algorithm>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。
- [静止媒質の灰色放射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを放射・物質の両交換項に掛けます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-algorithm>)

  風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

## 問題の図

- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png
- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png

## 厳密解・参照解

- [2D吸収影と保存的M1輸送：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja>)

  独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。
- [円形吸収体の特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。 6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
- [2D反向beamとM1閉包の情報損失：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja>)

  独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。
- [反向伝播packetの特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。 6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
- [円形吸収体の特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja>)
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。
- [反向伝播packetの特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja>)
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。
- [2D吸収影と保存的M1輸送：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-validation>)

  独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。
- [円形吸収体の特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。 6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
- [2D反向beamとM1閉包の情報損失：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-validation>)

  独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。
- [反向伝播packetの特性線参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。 6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

## コード・検証

- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja>)
  availability: run

  実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja>)
  availability: run

  保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
