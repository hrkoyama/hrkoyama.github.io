# SRHD衝突・SRMHD非線形Alfvén波

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/

この章に登録された手法・問題・実行例の関連資料です。 SRHDの対向衝突をTaub関係の二衝撃波解と、全7保存量SRMHDの有限振幅円偏波を独立テンソル式・保存量平均と比較します。空間は1次元で、図のx–t表示は2D流れではありません。

## 手法

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

## 方程式

- [特殊相対論的流体（SRHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja>)

  c=1、平坦なCartesian時空の理想流体。γ則EOSと原始変数回復を使う穏やかな対称二衝撃波の固定例を追加。一般三波Riemann解、極端なLorentz因子、一般相対論を検証したとはしません。 c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。
- [特殊相対論的理想MHD（SRMHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja>)

  c=4π=1、平坦時空・理想電気伝導・γ則EOSです。bμは流体静止系磁場4ベクトル。全磁気応力と誘導を含む7保存量を1Dで進め、原始変数は完全なRMHDのZ根で復元します。GRMHDとは区別します。 平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。
- [特殊相対論的理想MHD（SRMHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja>)

  c=4π=1、平坦時空・理想電気伝導・γ則EOSです。bμは流体静止系磁場4ベクトル。全磁気応力と誘導を含む7保存量を1Dで進め、原始変数は完全なRMHDのZ根で復元します。GRMHDとは区別します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-algorithm>)

  同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。
- [特殊相対論的流体（SRHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja>)

  c=1、平坦なCartesian時空の理想流体。γ則EOSと原始変数回復を使う穏やかな対称二衝撃波の固定例を追加。一般三波Riemann解、極端なLorentz因子、一般相対論を検証したとはしません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-algorithm>)

  D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

## 問題の図

- [SRHDの対称二衝撃波衝突](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png
- [SRMHDの有限振幅円偏極Alfvén波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png
- [SRHDの対称二衝撃波衝突](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png
- [SRMHDの有限振幅円偏極Alfvén波](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png

## 厳密解・参照解

- [SRHDの対称二衝撃波衝突：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja>)

  群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。
- [相対論的対称衝突：特殊化した二衝撃波Taub参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。Taub断熱式と相対速度式の圧力根から静止した同一星状態と衝撃波速度を求め、保存変数の区分一定厳密場をセル積分します。接触面は退化し、一般三波Riemannソルバーではありません。 独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。
- [SRMHDの有限振幅円偏極Alfvén波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja>)

  非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。
- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。非線形Alfvén速度の閉じた式を使い、点の原始変数から独立なストレステンソルで保存量と流束を作り、Gauss積分と複素段階PDE残差で確認します。原著の2π周期を単位区間へ移しています。 原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。
- [相対論的対称衝突：特殊化した二衝撃波Taub参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja>)
  reference_kind: semi-analytic

  半解析解 c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。Taub断熱式と相対速度式の圧力根から静止した同一星状態と衝撃波速度を求め、保存変数の区分一定厳密場をセル積分します。接触面は退化し、一般三波Riemannソルバーではありません。
- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja>)
  reference_kind: analytic

  解析解 平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。非線形Alfvén速度の閉じた式を使い、点の原始変数から独立なストレステンソルで保存量と流束を作り、Gauss積分と複素段階PDE残差で確認します。原著の2π周期を単位区間へ移しています。
- [SRHDの対称二衝撃波衝突：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-validation>)

  群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。
- [相対論的対称衝突：特殊化した二衝撃波Taub参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。Taub断熱式と相対速度式の圧力根から静止した同一星状態と衝撃波速度を求め、保存変数の区分一定厳密場をセル積分します。接触面は退化し、一般三波Riemannソルバーではありません。 独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。
- [SRMHDの有限振幅円偏極Alfvén波：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-validation>)

  非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。
- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。非線形Alfvén速度の閉じた式を使い、点の原始変数から独立なストレステンソルで保存量と流束を作り、Gauss積分と複素段階PDE残差で確認します。原著の2π周期を単位区間へ移しています。 原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

## コード・検証

- [SRHDの対称二衝撃波衝突](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja>)
  availability: run

  相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。
- [SRMHDの有限振幅円偏極Alfvén波](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja>)
  availability: run

  完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。
