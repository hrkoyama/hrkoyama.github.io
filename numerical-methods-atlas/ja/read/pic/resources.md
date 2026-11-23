# Particle-in-Cell（PIC）

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pic/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [CIC静電PICの冷たいプラズマ振動](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja>)
  availability: run

  1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。
- [PIC：格子・時間収束、保存量と粒子雑音](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja>)
  availability: run

  冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja>)
  availability: run

  ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja>)
  availability: run

  熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja>)
  availability: run

  温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。
- [Particle-in-Cell（PIC）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
