# 剛体球DSMCのMach2平面衝撃波

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-shock/

この章に登録された手法・問題・実行例の関連資料です。 流入出を持つ1D空間・3D速度の衝撃波で、RH遠方状態と内部の独立な数値参照を区別します。

## 手法

- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

## 方程式

- [剛体球Boltzmann輸送と壁・流入出](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja>)

  1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。 1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-algorithm>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。
- [剛体球Boltzmann輸送と壁・流入出](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja>)

  1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。

## 問題の図

- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock-preview.png
- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock.png

## 厳密解・参照解

- [硬球DSMCのMach2平面衝撃波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#references-ja>)

  各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。
- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。 各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。 各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCのMach2平面衝撃波：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-validation>)

  各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。
- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。 各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

## コード・検証

- [硬球DSMCのMach2平面衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja>)
  availability: run

  物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
