# 非平衡輻射：拡散と輸送を分ける

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/

この章に登録された手法・問題・実行例の関連資料です。 Su–Olsonの拡散問題と輸送問題を規格化・境界・出典で分け、同条件の周期Fourier制御による拡散極限も別に確認します。

## 手法

- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。
- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。
- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [Su–Olson1996の非平衡拡散・物質交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja>)

  x=√3κz。1997輸送のx=κzとは規格化も境界・参照も分けます。非単位epsilonの閉セル検査を別に行います。 無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。
- [静止媒質の灰色輻射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。 主検証は1997型の輻射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 主検証は1997型の輻射輸送・物質交換です。熱・拡散方程式への関連は、別の周期Fourier制御におけるE約V、拡散係数1/[3κ(ε+1)]の極限に限ります。1996Marshak境界や輸送全体の厳密解とは区別します。
- [静止媒質の灰色輻射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。
- [Su–Olson1996の非平衡拡散・物質交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja>)

  x=√3κz。1997輸送のx=κzとは規格化も境界・参照も分けます。非単位epsilonの閉セル検査を別に行います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-algorithm>)

  保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-algorithm>)

  全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

## 問題の図

- [Su–Olson1996非平衡拡散](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png
- [Su–Olson1996非平衡拡散](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png

## 厳密解・参照解

- [Su–Olson1996非平衡拡散：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#references-ja>)

  独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。
- [Su–Olson1996拡散：固定版の独立積分評価関数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 初期の輻射・物質変数が0、ε=1の半無限Marshak拡散です。無次元評価関数を直接用い、物理単位の質量吸収係数ラッパーに起因する曖昧な規約は持ち込みません。 1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。
- [Su–Olson1997角度輸送の独立公開表比較：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#references-ja>)

  5主計算で空間・32/64角・時間差と独立W/V誤差を分けます。参照表の有限性・因果零・一様解析source極限はmain前に資格済みです。 同じ初期・境界・sourceで別の連続空間角度行列と解析拡散極限を比較し、空間・角度・連続体極限誤差を分離。GL64/128、非単位容量の一様厳密解、独立DOP853で新参照141項目を先に資格します。
- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無限領域の対称1次元角度輸送と物質交換で、ε=1、弾性散乱なし、低温の零初期状態です。Q=1を|x|<0.5、0<τ<10に与えます。主計算は左反射・十分遠い右入射真空の半領域で、比較時刻は境界の影響前です。別の同条件比較用の周期セル平均制御は、物理座標x∈[0,2π)、c=ε=1、κ=4/8/16、N=128/512/2048、Q=0、初期I=V=1+0.1cos(x)、s=0/.0625/.125/.25に対するt=κsを用います。この制御は1997のsource駆動問題とは初期・境界・sourceが異なり、制御内のFV・連続角度参照・拡散比較に同じ入力を用います。 原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。
- [Su–Olson1996拡散：固定版の独立積分評価関数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja>)
  reference_kind: semi-analytic

  半解析解 初期の輻射・物質変数が0、ε=1の半無限Marshak拡散です。無次元評価関数を直接用い、物理単位の質量吸収係数ラッパーに起因する曖昧な規約は持ち込みません。
- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 無限領域の対称1次元角度輸送と物質交換で、ε=1、弾性散乱なし、低温の零初期状態です。Q=1を|x|<0.5、0<τ<10に与えます。主計算は左反射・十分遠い右入射真空の半領域で、比較時刻は境界の影響前です。別の同条件比較用の周期セル平均制御は、物理座標x∈[0,2π)、c=ε=1、κ=4/8/16、N=128/512/2048、Q=0、初期I=V=1+0.1cos(x)、s=0/.0625/.125/.25に対するt=κsを用います。この制御は1997のsource駆動問題とは初期・境界・sourceが異なり、制御内のFV・連続角度参照・拡散比較に同じ入力を用います。
- [Su–Olson1996非平衡拡散：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-validation>)

  独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。
- [Su–Olson1996拡散：固定版の独立積分評価関数](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 初期の輻射・物質変数が0、ε=1の半無限Marshak拡散です。無次元評価関数を直接用い、物理単位の質量吸収係数ラッパーに起因する曖昧な規約は持ち込みません。 1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。
- [Su–Olson1997角度輸送の独立公開表比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-validation>)

  5主計算で空間・32/64角・時間差と独立W/V誤差を分けます。参照表の有限性・因果零・一様解析source極限はmain前に資格済みです。 同じ初期・境界・sourceで別の連続空間角度行列と解析拡散極限を比較し、空間・角度・連続体極限誤差を分離。GL64/128、非単位容量の一様厳密解、独立DOP853で新参照141項目を先に資格します。
- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無限領域の対称1次元角度輸送と物質交換で、ε=1、弾性散乱なし、低温の零初期状態です。Q=1を|x|<0.5、0<τ<10に与えます。主計算は左反射・十分遠い右入射真空の半領域で、比較時刻は境界の影響前です。別の同条件比較用の周期セル平均制御は、物理座標x∈[0,2π)、c=ε=1、κ=4/8/16、N=128/512/2048、Q=0、初期I=V=1+0.1cos(x)、s=0/.0625/.125/.25に対するt=κsを用います。この制御は1997のsource駆動問題とは初期・境界・sourceが異なり、制御内のFV・連続角度参照・拡散比較に同じ入力を用います。 原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

## コード・検証

- [Su–Olson1996非平衡拡散](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja>)
  availability: run

  実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja>)
  availability: run

  物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。
