# Minmod / Minmod

Status: educational-example

Read about Minmod, follow the original references and inspect related educational code and checks.

「Minmod」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: minmod法, minmod limiter, minmod制限関数, minmod勾配制限

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py

- Reference: https://doi.org/10.1137/0721062 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Minmod limits conserved-variable MUSCL slopes in this Noh edition's spherical series. Planar/cylindrical runs retain piecewise-constant states. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

このNoh配布の球対称系列で、保存量のMUSCL型再構築の傾きをminmodで制限します。平面・円筒は区分定数のままです。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

- Noh shocks: zero-pressure planar, cylindrical and spherical flow: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json

- Zalesak-type 2D rotation: conservation, bounds and shape error: https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/result.json

- SRHD symmetric two-shock collision: https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/
- SRMHD finite-amplitude circularly polarized Alfvén wave: https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json

Common execution records: [{"id": "noh-shock", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "zalesak-rotation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srhd-collision", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srmhd-alfven", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-square)
- [非粘性Burgers方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#burgers-ja) (`burgers`; burgers-shock, burgers-fan)
- [LWR交通流モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#traffic-ja) (`traffic`; traffic-jam, traffic-fan)
- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`; dam-break)
- [等温流体方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#isothermal-ja) (`isothermal`; isothermal-jump)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; nasa-wedge, forward-step, entropy-2d, noh)
- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`; zalesak)
- [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja) (`srhd`; srhd-collision)
- [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja) (`srmhd`; srmhd-alfven)

#### 問題の図 (`method-problems-ja`)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja) (`advection-square`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja) (`burgers-shock`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja) (`burgers-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja) (`traffic-jam`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja) (`traffic-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja) (`entropy-2d`)

![保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![実際の2次元Cartesian Euler計算の密度場。正方形全域128²セル、初期圧力ゼロ、γ=5/3、t=.6。白破線は厳密衝撃円。軸・対角方向の差と原点過熱を残し、1D半径例にも辿れます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

![実際の2次元スカラー輸送の最細格子の保存セル平均。全\[0,1\]²のうちx∈\[.28,.72\], y∈\[.53,.97\]の円盤周辺を拡大し、一回転後の一次風上とminmod MUSCLを幾何学的な参照セル平均と比較します。切り欠きの数値拡散を残した図で、FCT法やEuler流体の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

- [Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) (`zalesak-rotation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

- [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) (`srhd-collision`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

- [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) (`srmhd-alfven`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期矩形波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja) (`advection-square`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#references-ja) (`burgers-shock`)

- [Burgers／衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-shock-ja) (`burgers-shock`; 関連モデルの参照; 解析参照)

左右状態(1,0)、段差位置0.5、端点継続が一致します。点値とセル平均の評価は区別します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-shock)

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#references-ja) (`burgers-fan`)

- [Burgers／膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-fan-ja) (`burgers-fan`; 関連モデルの参照; 解析参照)

左右状態(0,1)、段差位置0.5、端点継続が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-fan)

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#references-ja) (`traffic-jam`)

- [交通流／上流へ進む衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-jam-ja) (`traffic-jam`; 関連モデルの参照; 解析参照)

流束ρ(1-ρ)、左右密度(0.3,0.9)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-jam)

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#references-ja) (`traffic-fan`)

- [交通流／渋滞解消の膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-fan-ja) (`traffic-fan`; 関連モデルの参照; 解析参照)

流束ρ(1-ρ)、左右密度(0.9,0.1)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-fan)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) (`dam-break`)

- [浅水流／水深が正のダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dam-break-ja) (`swe-dam-break`; 関連モデルの参照; 半解析参照)

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break)

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) (`isothermal-jump`)

- [等温流／密度跳躍](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isothermal-jump-ja) (`isothermal-jump`; 関連モデルの参照; 半解析参照)

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump)

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) (`nasa-wedge`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) (`forward-step`)

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照; 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements)

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) (`entropy-2d`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) (`noh`)

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照; 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

[既存の参照図](/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) (`zalesak`)

- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja) (`zalesak-rotation`; 同じ問題の参照; 解析参照)

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

[既存の参照図](/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-measurements)

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) (`srhd-collision`)

- [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja) (`srhd-collision`; 同じ問題の参照; 半解析参照)

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

[既存の参照図](/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-measurements)

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) (`srmhd-alfven`)

- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja) (`srmhd-alfven`; 同じ問題の参照; 解析参照)

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

[既存の参照図](/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算 (`noh-shock`)

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

##### Zalesak型2D回転輸送：保存・有界性・形状誤差 (`zalesak-rotation`)

[Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### SRHDの対称二衝撃波衝突 (`srhd-collision`)

[SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### SRMHDの有限振幅円偏極Alfvén波 (`srmhd-alfven`)

[SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

このNoh配布の球対称系列で、保存量のMUSCL型再構築の傾きをminmodで制限します。平面・円筒は区分定数のままです。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/tvd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_limiters.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-square)
- [Inviscid Burgers equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#burgers-en) (`burgers`; burgers-shock, burgers-fan)
- [LWR traffic model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#traffic-en) (`traffic`; traffic-jam, traffic-fan)
- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`; dam-break)
- [Isothermal flow equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#isothermal-en) (`isothermal`; isothermal-jump)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; nasa-wedge, forward-step, entropy-2d, noh)
- [Two-dimensional rotational advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en) (`rotational-advection`; zalesak)
- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`; srhd-collision)
- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`; srmhd-alfven)

#### Problem figures (`method-problems-en`)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en) (`advection-square`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

Methods used by the stored square-wave CIP and limiter comparisons.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en) (`burgers-shock`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en) (`burgers-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en) (`traffic-jam`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en) (`traffic-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en) (`entropy-2d`)

![Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Density from an actual2D Cartesian Euler computation:full square128²,p0=0,gamma5/3,t=.6. White dashed circle is the exact shock. Axis/diagonal differences and origin heating remain visible, with links to earlier1D radial examples.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

![Saved cell means on the finest grid of actual two-dimensional scalar transport. Zoom x in\[.28,.72\],y in\[.53,.97\] from the full unit square and compare donor-cell upwinding and minmod MUSCL after one revolution against geometric reference cell means. Slot diffusion remains visible; this is not an FCT algorithm or Euler-flow calculation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

- [Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) (`zalesak-rotation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

- [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) (`srhd-collision`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

- [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) (`srmhd-alfven`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic square-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en) (`advection-square`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#references-en) (`burgers-shock`)

- [Burgers / shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-shock-en) (`burgers-shock`; Related-model reference; Analytic reference)

States (1,0), jump position 0.5 and endpoint continuation match; distinguish point and cell-average evaluation. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-shock)

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#references-en) (`burgers-fan`)

- [Burgers / rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-fan-en) (`burgers-fan`; Related-model reference; Analytic reference)

States (0,1), jump position 0.5 and endpoint continuation match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-fan)

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#references-en) (`traffic-jam`)

- [Traffic / upstream shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-jam-en) (`traffic-jam`; Related-model reference; Analytic reference)

Flux ρ(1-ρ), left/right densities (0.3,0.9) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-jam)

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#references-en) (`traffic-fan`)

- [Traffic / clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-fan-en) (`traffic-fan`; Related-model reference; Analytic reference)

Flux ρ(1-ρ), left/right densities (0.9,0.1) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-fan)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) (`dam-break`)

- [Shallow water / wet dam break](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dam-break-en) (`swe-dam-break`; Related-model reference; Semi-analytic reference)

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break)

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) (`isothermal-jump`)

- [Isothermal / density jump](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isothermal-jump-en) (`isothermal-jump`; Related-model reference; Semi-analytic reference)

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump)

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) (`nasa-wedge`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) (`forward-step`)

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference; Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements)

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) (`entropy-2d`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) (`noh`)

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference; Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

[Existing reference profile](/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) (`zalesak`)

- [Zalesak-type slotted disk: rigid rotation and geometric cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en) (`zalesak-rotation`; Same-problem reference; Analytic reference)

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

[Existing reference profile](/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-measurements)

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) (`srhd-collision`)

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference; Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

[Existing reference profile](/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-measurements)

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) (`srmhd-alfven`)

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference; Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

[Existing reference profile](/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Noh shocks: zero-pressure planar, cylindrical and spherical flow (`noh-shock`)

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

##### Zalesak-type 2D rotation: conservation, bounds and shape error (`zalesak-rotation`)

[Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### SRHD symmetric two-shock collision (`srhd-collision`)

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### SRMHD finite-amplitude circularly polarized Alfvén wave (`srmhd-alfven`)

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Minmod limits conserved-variable MUSCL slopes in this Noh edition's spherical series. Planar/cylindrical runs retain piecewise-constant states. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/limiters.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/tvd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/tvd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_limiters.py
```
