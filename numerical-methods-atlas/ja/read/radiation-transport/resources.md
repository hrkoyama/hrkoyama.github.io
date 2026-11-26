# 輻射輸送・モーメント法

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [純吸収平板の離散座標輻射輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja>)
  availability: run

  純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。
- [輻射輸送：空間・角度収束と光子統計](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja>)
  availability: run

  純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。
- [等方散乱平板の反射・透過・吸収](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja>)
  availability: run

  正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。
- [Su–Olson1996非平衡拡散](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja>)
  availability: run

  実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja>)
  availability: run

  物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。
- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja>)
  availability: run

  実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja>)
  availability: run

  保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
- [輻射輸送・モーメント法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
