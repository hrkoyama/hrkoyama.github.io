# 別モデルとして調べる：2次元対数FMM

上の重力・PM・ツリーの本文と境界条件は保持します。以下のFMMは、2次元自由空間の負の対数核を一様四分木で評価する別の教育用モデルです。3次元Coulombや軟化重力の1/r核へ精度を移しません。

旧配布版を保持し、追加版では展開次数と木深さを分けてCartesian直接和・解析配置・保存診断と比較します。深さの単調収束や実測の計算量スケーリング、適応木・周期FMMを検証したとは表示しません。

## 2次元対数核のM2M・M2L・L2Lを持つFMM

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

3次元1/r核、適応木、周期FMM、特異積分、実測の計算量スケーリングは未検証です。2次元自由空間の教育用実装として表示します。

- [入力・結果・判定](/numerical-methods-atlas/validation/fmm/?lang=ja)
- [解説・式・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#fmm)
- [コード：run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [コード：electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [コード：fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [コード：transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [テスト：test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [配布ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)
- [保存結果](/code/validated-examples/2026-11-22/particles/results/result.json)
- [独立展開の追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

## FMM：直接和・解析配置と展開次数・木の深さ

96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

木の深さによる相互作用の分割は変わるので、一定次数で深さに対する単調収束は要求しません。対象粒子ごとの展開は厳密な作用反作用を保証せず、3次元・適応木・周期FMM・計算量スケーリングは未検証です。

- [入力・結果・判定](/numerical-methods-atlas/validation/fmm-convergence/?lang=ja)
- [解説・式・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#fmm-convergence)
- [コード：run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [コード：longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [コード：fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [コード：electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [コード：kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [コード：kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [テスト：test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [テスト：test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [テスト：test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [配布ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)
- [保存結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json)
- [独立展開の追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)
