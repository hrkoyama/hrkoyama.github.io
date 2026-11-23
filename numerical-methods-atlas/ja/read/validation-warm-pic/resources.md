# 熱的PIC：Landau減衰と二流不安定性

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-warm-pic/

この章に登録された手法・問題・実行例の関連資料です。 自己無撞着な全分布の重み付きPICを、独立な誘電分散式と線形Volterra初期値問題と比較します。

## 手法

- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)
- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

## 方程式

- [静電Vlasov–Poisson方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja>)

  1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。 vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。
- [静電Vlasov–Poisson方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja>)

  1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。 各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。
- [静電Vlasov–Poisson方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja>)

  1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-algorithm>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-algorithm>)

  正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

## 問題の図

- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png

## 厳密解・参照解

- [温かいPICの線形Landau減衰：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#references-ja>)

  31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの二流初期成長：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#references-ja>)

  31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja>)
  reference_kind: semi-analytic

  半解析解 vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja>)
  reference_kind: semi-analytic

  半解析解 各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの線形Landau減衰：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-validation>)

  31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
- [温かいPICの二流初期成長：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-validation>)

  31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。 31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

## コード・検証

- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja>)
  availability: run

  熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja>)
  availability: run

  温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。
