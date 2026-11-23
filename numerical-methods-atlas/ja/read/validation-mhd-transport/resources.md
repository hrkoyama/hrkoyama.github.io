# MHD輸送・波・圧縮構造の独立比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-transport/

この章に登録された手法・問題・実行例の関連資料です。 全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。

## 手法

- [HLLDのMHDリーマン解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [制約輸送法／CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-algorithm>)

  全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。Bx一定の1次元有限体積更新。
- [理想MHD](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja>)

  透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-algorithm>)

  全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-algorithm>)

  全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。

## 問題の図

- [円偏波Alfvén波：全成分の格子収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png
- [磁場ループ：独立2次元参照と細分化](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png
- [後期Orszag–Tang：独立参照と圧縮構造](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png
- [円偏波Alfvén波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png
- [磁場ループの移流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png
- [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp

## 厳密解・参照解

- [円偏波Alfvén波：全保存変数の解析セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja>)
  reference_kind: analytic

  解析解 γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。横磁場と横運動量にはsinc(h)を掛け、E=.66を保ちます。独立Gauss16求積と照合します。図のx–tは1次元空間と保存時刻であり、斜め2次元伝播ではありません。
- [磁場ループ：固定Athena++の独立終端参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 [-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。未変更の公式生成器を固定コミット1395e2f…で実行し、Ny64/128と最細格子CFL半減で参照感度を確認します。比較は終端保存場のみで、保守的な粗視化後に評価します。
- [後期Orszag–Tang：独立有限格子の密度・圧力参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。
- [円偏波Alfvén波：全成分の格子収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-validation>)

  実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。
- [円偏波Alfvén波：全保存変数の解析セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。横磁場と横運動量にはsinc(h)を掛け、E=.66を保ちます。独立Gauss16求積と照合します。図のx–tは1次元空間と保存時刻であり、斜め2次元伝播ではありません。 γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。
- [磁場ループ：独立2次元参照と細分化：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-validation>)

  実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。
- [磁場ループ：固定Athena++の独立終端参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 [-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。未変更の公式生成器を固定コミット1395e2f…で実行し、Ny64/128と最細格子CFL半減で参照感度を確認します。比較は終端保存場のみで、保守的な粗視化後に評価します。 [-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。
- [後期Orszag–Tang：独立参照と圧縮構造：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-validation>)

  実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。
- [後期Orszag–Tang：独立有限格子の密度・圧力参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
- [円偏波Alfvén波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 円偏光Alfvén波の解析解を、一定の全エネルギーを含む保存変数セル平均で評価します。 実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。
- [円偏波Alfvén波：全保存変数の解析セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja>)
  relation: related-model
  reference_kind: analytic

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 解析解 γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。横磁場と横運動量にはsinc(h)を掛け、E=.66を保ちます。独立Gauss16求積と照合します。図のx–tは1次元空間と保存時刻であり、斜め2次元伝播ではありません。 γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。
- [磁場ループの移流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 弱磁場ループが1周期で戻る初期場との誤差、磁気エネルギー、配置固有の磁場発散を確認します。任意強度のMHDループの厳密解を主張しません。 実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。
- [磁場ループ：固定Athena++の独立終端参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja>)
  relation: related-model
  reference_kind: numerical-reference

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 有限格子の数値参照 [-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。未変更の公式生成器を固定コミット1395e2f…で実行し、Ny64/128と最細格子CFL半減で参照感度を確認します。比較は終端保存場のみで、保守的な粗視化後に評価します。 [-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。
- [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja>)

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 保存則・各離散配置に対応する磁場発散と、別実行のAthena++数値参照を確認します。この非線形MHD問題の厳密解を提供するものではありません。 実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。
- [後期Orszag–Tang：独立有限格子の密度・圧力参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja>)
  relation: related-model
  reference_kind: numerical-reference

  全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。 有限格子の数値参照 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。 γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

## コード・検証

- [円偏波Alfvén波：全成分の格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja>)
  availability: run

  全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。
- [磁場ループ：独立2次元参照と細分化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja>)
  availability: run

  実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。
- [後期Orszag–Tang：独立参照と圧縮構造](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja>)
  availability: run

  圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。
