# 可変Eddington因子・テンソルの軽量検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-variable-eddington-controls/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [可変Eddington因子（1D VEF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja>)

  形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
- [可変Eddingtonテンソル（VET）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja>)

  非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。
- [可変Eddington因子（1D VEF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja>)
- [可変Eddingtonテンソル（VET）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja>)

## 方程式

- [静止灰色輻射のVEF・VETモーメント閉包](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja>)

  c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [静止灰色輻射のVEF・VETモーメント閉包](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja>)

  c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-algorithm>)

  各反復でq+σs E_LOをFourier形式解へ入れ、f=Kxx/E_HOを抽出し、保存的な面流束を使う有限差分モーメント式を解きます。参照解は主計算の閉包へ渡しません。
- [静止灰色輻射のVEF・VETモーメント閉包](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja>)

  c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-algorithm>)

  形式的なFourier角度輸送→D=K_HO/E_HO→独立な有限差分モーメント式を反復します。Dxyの両交差微分を共有面流束へ含め、局所・大域の離散収支を確認します。

## 問題の図

- [可変エディントン因子：周期1D散乱源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png
- [可変エディントンテンソル：周期2D非平行源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png
- [可変エディントン因子：周期1D散乱源の固定検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png
- [可変エディントンテンソル：周期2D非平行源の固定検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png

## 厳密解・参照解

- [可変エディントン因子：周期1D散乱源の固定検証：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#references-ja>)

  正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
- [本例のために導出した周期1D VEFの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。 正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
- [可変エディントンテンソル：周期2D非平行源の固定検証：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#references-ja>)

  正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。
- [本例のために導出した周期2D VETの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。 正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。
- [本例のために導出した周期1D VEFの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja>)
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。
- [本例のために導出した周期2D VETの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja>)
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。
- [可変エディントン因子：周期1D散乱源の固定検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-validation>)

  N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。
- [本例のために導出した周期1D VEFの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。 正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
- [可変エディントンテンソル：周期2D非平行源の固定検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-validation>)

  17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。
- [本例のために導出した周期2D VETの連続Fourier応答](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。 正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

## コード・検証

- [可変エディントン因子：周期1D散乱源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja>)
  availability: run

  形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。
- [可変エディントンテンソル：周期2D非平行源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja>)
  availability: run

  非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。
