# QR・SVD・最小二乗

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/qr-svd/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [QR・SVD・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja>)
  availability: run

  実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。
- [QR/SVD：既定特異値・摂動増幅・数値階数](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja>)
  availability: run

  二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。
- [QR・SVD・最小二乗：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
