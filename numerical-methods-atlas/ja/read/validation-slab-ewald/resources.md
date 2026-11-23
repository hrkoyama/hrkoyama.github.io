# 中性スラブ：3周期補正と真の2周期参照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-slab-ewald/

この章に登録された手法・問題・実行例の関連資料です。 長方形の周期箱と非周期zの分枝を固定し、Yeh–Berkowitz補正を真の2周期の自己項・零モード込みの参照と照合します。

## 手法

- [Ewald法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja>)

  全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。
- [スラブ静電場と2次元周期Ewald](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=ja>)

  全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。
- [Ewald法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja>)
- [スラブ静電場と2次元周期Ewald](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=ja>)

## 方程式

- [Coulomb静電場と混合周期境界](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja>)

  中性系・Coulomb定数1。真の2周期の参照と、有限真空厚の3周期＋補正を区別します。 Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。
- [Coulomb静電場と混合周期境界](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja>)

  中性系・Coulomb定数1。真の2周期の参照と、有限真空厚の3周期＋補正を区別します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-algorithm>)

  全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

## 問題の図

- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png
- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png

## 厳密解・参照解

- [中性長方形スラブ：真2P参照とYB補正：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#references-ja>)

  参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。
- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。 参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。
- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja>)
  reference_kind: semi-analytic

  半解析解 Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。 参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。
- [中性長方形スラブ：真2P参照とYB補正：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-validation>)

  参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。
- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。 参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

## コード・検証

- [中性長方形スラブ：真2P参照とYB補正](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja>)
  availability: run

  4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。
