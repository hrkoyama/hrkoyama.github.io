# 分野を超えて使う 数値計算の基礎 — 小さな計算室

2026-11-24版。Python 3.12の標準ライブラリだけで計算・25単体テスト・34固定判定・15CSVの照合を実行できます。NumPy、ネット接続、乱数、外部ソルバーは不要です。

```sh
python verify_release.py
python lab.py --input inputs.json --output my-results
python -m unittest discover -s . -p test_lab.py -v
```

`my-results`は新しい、または空のディレクトリにしてください。`results`は配布時の保存結果です。`inputs.json`は実行前に固定した入力と合格条件、`review.json`は自己レビューの導出と適用範囲、`contract.json`は固定時のSHAです。第三者による独立レビューの実施を主張しません。

`history/attempt-01`は最初の粗い移流格子系列で観測次数の条件に届かなかった入力・コード・結果です。失敗を成功として数えません。`development-history.json`に改訂理由を残しました。合格基準は緩めず、格子だけ細かくしています。

意図的に不安定なFTCSとCFL違反、低次の境界閉鎖、前進Eulerの長時間エネルギー増大も含みます。それらは異常を検出する対照例で、精度のよい解法としての合格ではありません。

図の再生成だけはReportLab 4.4.9とPopplerのpdftoppmが必要です。

```sh
python -m pip install reportlab==4.4.9
python plot.py --results results --output figures-new
```

全19章は同じ一次元問題・小さな行列を再利用します。図19枚を19個の独立した物理検証とは数えません。入力を変えた探索結果は、この配布版の固定検証とは分けて保存してください。クロスOSの数値比較は入力に固定した相対1e-9・絶対1e-10を使います。図の再生成バイト一致は要求しません。

本文・Web・PDF: https://hrkoyama.github.io/numerical-methods-atlas/learn/numerical-foundations/

コードはMIT License。参照先の教科書・講義資料は同梱していません。
