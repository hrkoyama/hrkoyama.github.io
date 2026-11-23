# 3Dの1/r核：展開・木・力の検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-fmm3d/

この章に登録された手法・問題・実行例の関連資料です。 真の3D展開でM2M・M2L・L2Lを通った非零の最終寄与と一意な相互作用割当てを確かめます。

## 手法

- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)

  P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。
- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)

## 方程式

- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-algorithm>)

  P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

## 問題の図

- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png
- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png

## 厳密解・参照解

- [真3D 1/r FMM：多段変換・力・適応所有権：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#references-ja>)

  有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。
- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。 有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。
- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。 有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。
- [真3D 1/r FMM：多段変換・力・適応所有権：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-validation>)

  有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。
- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。 有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

## コード・検証

- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja>)
  availability: run

  非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。
