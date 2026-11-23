# KH・RTの初期成長と独立線形参照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/

この章に登録された手法・問題・実行例の関連資料です。 小振幅の非線形2D計算を、別に導出した連続Fourier–Galerkin線形初期値問題と比較します。有限時間の成長、格子・時間・振幅の影響を分けます。

## 手法

- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [維持されたせん断層の強制渦度系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja>)

  解析的な基底せん断を明示的外力で維持し、微小摂動を実際の非線形2D渦度系で進めます。圧力は消去され、鋭い界面・無限領域・可圧縮KHの分散式とは区別します。 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。
- [能動浮力を伴うBoussinesq渦度系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja>)

  慣性密度を一定とし、密度差は浮力だけに残します。基底浮力を外力で維持した摂動形です。全浮力bの鉛直力のcurlがθxを与え、可変密度Euler系とは異なります。 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。
- [維持されたせん断層の強制渦度系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja>)

  解析的な基底せん断を明示的外力で維持し、微小摂動を実際の非線形2D渦度系で進めます。圧力は消去され、鋭い界面・無限領域・可圧縮KHの分散式とは区別します。
- [能動浮力を伴うBoussinesq渦度系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja>)

  慣性密度を一定とし、密度差は浮力だけに残します。基底浮力を外力で維持した摂動形です。全浮力bの鉛直力のcurlがθxを与え、可変密度Euler系とは異なります。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-algorithm>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-algorithm>)

  点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

## 問題の図

- [KHの初期成長：滑らかな周期せん断層](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png
- [RTの初期成長：滑らかなBoussinesq二層](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png
- [KHの初期成長：滑らかな周期せん断層](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png
- [RTの初期成長：滑らかなBoussinesq二層](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png

## 厳密解・参照解

- [KHの初期成長：滑らかな周期せん断層：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#references-ja>)

  群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。
- [KH初期成長：独立した線形Fourier–Galerkin参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。主計算は非線形2次元の点サンプルで、参照はkx=1の連続線形化IVPです。K24/40/56の切断を比較し、基底の微分は独立Fourier係数から評価します。鋭い界面の分散式を流用しません。 線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
- [RTの初期成長：滑らかなBoussinesq二層：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#references-ja>)

  群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。
- [RT初期成長：Boussinesq二層の線形IVP参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。参照は同じ滑らかな基底のkx=1連続線形化をFourier–Galerkin K24/40/56で解きます。慣性密度は一定、浮力偏差θだけが鉛直力へ入り、周期二層の一方が不安定です。 線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
- [KH初期成長：独立した線形Fourier–Galerkin参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。主計算は非線形2次元の点サンプルで、参照はkx=1の連続線形化IVPです。K24/40/56の切断を比較し、基底の微分は独立Fourier係数から評価します。鋭い界面の分散式を流用しません。
- [RT初期成長：Boussinesq二層の線形IVP参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。参照は同じ滑らかな基底のkx=1連続線形化をFourier–Galerkin K24/40/56で解きます。慣性密度は一定、浮力偏差θだけが鉛直力へ入り、周期二層の一方が不安定です。
- [KHの初期成長：滑らかな周期せん断層：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-validation>)

  群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。
- [KH初期成長：独立した線形Fourier–Galerkin参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。主計算は非線形2次元の点サンプルで、参照はkx=1の連続線形化IVPです。K24/40/56の切断を比較し、基底の微分は独立Fourier係数から評価します。鋭い界面の分散式を流用しません。 線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
- [RTの初期成長：滑らかなBoussinesq二層：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-validation>)

  群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。
- [RT初期成長：Boussinesq二層の線形IVP参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。参照は同じ滑らかな基底のkx=1連続線形化をFourier–Galerkin K24/40/56で解きます。慣性密度は一定、浮力偏差θだけが鉛直力へ入り、周期二層の一方が不安定です。 線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

## コード・検証

- [KHの初期成長：滑らかな周期せん断層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja>)
  availability: run

  実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。
- [RTの初期成長：滑らかなBoussinesq二層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja>)
  availability: run

  密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。
