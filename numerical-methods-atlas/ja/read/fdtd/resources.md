# Yee FDTD：基礎と検証例

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [2D誘電体円柱のMie散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja>)
  availability: run

  実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。
- [Lorentz分散板へのs/p斜め入射](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja>)
  availability: run

  有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。
- [分散媒質の浅い入射角と長時間PML](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja>)
  availability: run

  80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。
- [Yee FDTD：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
