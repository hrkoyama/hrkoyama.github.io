# 有限Knudsen数のCouette・Fourier流

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-wall/

この章に登録された手法・問題・実行例の関連資料です。 物理時間の剛体球衝突、壁の流束重み付き再放出、保存収支を独立SPARTA参照と比較します。

## 手法

- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

## 方程式

- [剛体球Boltzmann輸送と壁・流入出](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja>)

  1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。
- [剛体球Boltzmann輸送と壁・流入出](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja>)

  1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。
- [剛体球Boltzmann輸送と壁・流入出](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja>)

  1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-algorithm>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-algorithm>)

  セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

## 問題の図

- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png
- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png

## 厳密解・参照解

- [硬球DSMCの有限Kn Couette流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#references-ja>)

  各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。
- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-couette-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Fourier熱伝導：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#references-ja>)

  各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-couette-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Couette流：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-validation>)

  各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。
- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-couette-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
- [硬球DSMCの有限Kn Fourier熱伝導：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-validation>)

  各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

## コード・検証

- [硬球DSMCの有限Kn Couette流](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja>)
  availability: run

  物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
- [硬球DSMCの有限Kn Fourier熱伝導](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja>)
  availability: run

  物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。
