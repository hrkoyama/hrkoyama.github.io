# Krylov固有値解法

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja>)
  availability: run

  32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。
- [Krylov固有値：クラスター部分空間と非正規感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja>)
  availability: run

  48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。
- [Krylov固有値解法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
