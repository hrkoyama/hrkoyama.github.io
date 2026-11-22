# CSVRとLangevin：分布・揺らぎ・相関

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)

## 方程式

- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 Hamilton系へのリンクは非調和ポテンシャルの力学部分です。確率温度浴を加えたCSVR・Langevinの分布検証を行います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-algorithm>)

  平方完成した厳密CIR遷移を、標準正規Rと独立χ²(Nf−1)のSから作ります。同じRでglobal αの符号を決め、Nf=1ではS=0。単位方向と新しい半径からpを再構成し、極小KでKnew/Kを作りません。K=0は方向が未定義として拒否します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-algorithm>)

  両方式とも厳密な浴O(h/2)–velocity-Verlet–O(h/2)（OBABO）。CSVRは全運動量に同じ係数、Langevinは各成分に独立OU雑音を作用。γ=1/(2τ)で自由浴のK緩和時間をそろえます。以前のBAOAB例は変更せず別の分割として残します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-algorithm>)

  同じOBABO分割でglobal CSVRとlocal OUを比較。正準初期座標はGaussianを包絡にした独立棄却法、運動量はMaxwell分布から生成し、別の温度摂動初期集団も進めます。

## 問題の図

- [非調和CSVRとLangevin：Boltzmann求積との分布比較](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png
- [CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png
- [非調和CSVRとLangevin：Boltzmann求積との分布比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png

## 厳密解・参照解

- [非調和CSVRとLangevin：Boltzmann求積との分布比較：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja>)

  非調和ポテンシャルのBoltzmann分布を独立数値求積し、CSVR・Langevinの有限刻み分布とモーメントを比較します。厳密な確率軌道の比較ではありません。
- [CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-validation>)

  条件付き平均・分散は独立なCIR式、CDFの3確率点はSciPyの非心χ²分位点、定常KはGamma分布、浴単独ACFはexp(−t/τ)と照合。無雑音の平均緩和は分散を失う対照として別表示します。
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-validation>)

  正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。
- [非調和CSVRとLangevin：Boltzmann求積との分布比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-validation>)

  座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

## コード・検証

- [非調和CSVRとLangevin：Boltzmann求積との分布比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja>)
  availability: run

  弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。
- [CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja>)
  availability: run

  自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja>)
  availability: run

  異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。
