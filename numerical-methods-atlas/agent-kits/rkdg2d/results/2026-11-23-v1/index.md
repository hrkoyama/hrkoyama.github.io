# RKDGプロンプトの実測結果

日本語版テンプレートで、組み立てと不合格からの修正を各1試行。両候補が元48科学ケース＋波形4診断に合格し、実測した故障負例も棄却しました。

- starterから組み立て: 元48＋波形4 合格・負例棄却; 2回修正、約49分 (2949.835 s); SHA256 `c8c6b11b688a50a3082a9dedb6b8a663b55a7cd5358aa4ac20166b672299cc2a`.
- 欠陥を入れた候補を修正: 元48＋波形4 合格・負例棄却; 1回修正、約48分 (2866.545 s); SHA256 `4ed984a01c42fe9bb657c09c61361b086682d6aa611e9f478bf996c0b29b81d4`.

修正回数は数値ソルバーへの変更を数え、初回実装を除きます。環境設定や補助スクリプトの修正は別に記録しました。所要時間は準備・実装/修正・新規計算・検証を含む報告値です。2試行は同じMacで並行しており、モデル速度の比較には使いません。

費用金額・課金トークン・詳細なモデルIDは取得できませんでした。金額は未取得であり、0円ではありません。安価なモデルとの比較、アトラスなしとの比較、費用削減の実証は今回の範囲外です。

- 各候補を--solverで選び、斜めエントロピー波12、x/yのSod・Shu–Osher24、Double Mach9、時間収束3の元48判定行を新規計算しました。時間比較の追加参照1本を含む実PDE出力は各49配列です。

- 波形4診断はp2/p3・x/yの保存出力から局所誤差、標準偏差比、相関を判定します。追加の4本のPDE計算ではありません。

- 別に保持した配布物の固定評価器で元48・波形4を再判定し、各49配列から240指標を再計算して一致を確認しました。元の配布295項目・判定基準・参照値は変更していません。故障版のyフラックスを実際に計算し、固定精度基準で棄却しました。

- 斜め波の最細格子間L₂次数は両候補とも2.0013 / 2.9747 / 4.0088。衝撃波のある全領域に2・3・4次収束を主張せず、Double Machは独立FV参照との広域構造比較です。正値性は指定した求積点・面・頂点の範囲です。

公開した日本語MD本文に固定の課題文を添え、会話履歴を引き継がない別エージェントで各1回実行しました。取得と環境準備は監督側が担当し、AIが実装・修正・実行を担当しました。

組み立ては未実装starterからSSPRK(5,4)・特性TVB・厳密1D入力の縮約を実装。短時間の方向差を見つけ、2回の修正後に全試験へ進みました。修正試験は事前に入れたSSPRK係数誤り1件で、原因を伏せて失敗JSONを渡しました。定数ODEの増分0.99dtから係数整合性を診断し、1回で修正しました。

完成ソースの参照は禁止しましたが、OSによる読取隔離ではありません。各1試行であり、一般的な成功率や任意のバグ修正能力は測っていません。

x/yの厳密1D入力は解析的縮約を使います。完全2D結合は斜め波とDouble Machで確認。既知の反転x追加試験は5/6合格のまま、今回の対象外です。MPI実行・他言語PDE・量子化学の追加計算は行っていません。

配布版をimportするpytest162件は未実装候補でも通ったため、候補そのものの合格には--solver指定の新規計算と固定評価器を使いました。

NumPy2.0.2の参照remap行列積で警告を保存。別プロセスでも再現しましたが、入力・出力は有限で、einsum経路との差は0でした。

監督側の追加照合v1はcallback時刻を完全一致とし、修正候補で失敗しました。配布ソルバー既存の終端処理（4eps×max(1,|T|)以内を最終時刻へ丸める）に合わせたv2で両候補を再照合。初回失敗を保持し、科学計算の基準や出力は変えていません。

Linuxの追加照合v2は、ほぼゼロの誤差ノルムを相対64epsだけで比較して24指標が不一致となりました（最大絶対差2.36×10⁻¹⁶未満）。元48・波形4の科学判定は合格です。別配布のv3は非ゼロの無次元指標に絶対64epsの丸め誤差床を加え、ゼロは完全一致を維持します。元ZIP・配列・記録値・科学判定基準は変更せず、初回失敗を保存しています。

[Portable audit v3](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot-audit3/verify_saved_portable.py) / [SHA256](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot-audit3/verify_saved_portable.py.sha256) / [Linux audit v2 failure](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/results/2026-11-23-v1/evidence/linux-audit-v2-failure.json)

## 保存データの再判定

baseキットr2と結果ZIPをそれぞれSHA256確認後に展開し、結果フォルダで次を実行します。NumPy2.0.2を使い、出力先は未使用フォルダにします。これは保存配列の再判定で、新しい全PDE計算ではありません。 別配布の照合v3を取得しSHA256を確認してください。元ZIPのv2は変更せず保持しています。

```sh
python verify_saved_portable.py --bundle /path/to/atlas-rkdg-agent-pilot --trial assembly --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit
python verify_saved_portable.py --bundle /path/to/atlas-rkdg-agent-pilot --trial repair --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit
```

[ZIP](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot1/atlas-rkdg-agent-pilot.zip) / [SHA256](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot1/atlas-rkdg-agent-pilot.zip.sha256)

[Source kit / primary references](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/?lang=ja)
