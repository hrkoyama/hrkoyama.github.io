# 分散媒質の浅い入射角と長時間PML

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-grazing/

この章に登録された手法・問題・実行例の関連資料です。 80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

## 手法

- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)

  Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)

  Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

  Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。
- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

## 方程式

- [受動Lorentz・Ohmic分散Maxwell場](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja>)

  正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。 c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-algorithm>)

  Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。
- [受動Lorentz・Ohmic分散Maxwell場](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja>)

  正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。

## 問題の図

- [分散媒質の浅い入射角と長時間PML](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png
- [分散媒質の浅い入射角と長時間PML](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png

## 厳密解・参照解

- [分散媒質の浅い入射角と長時間PML：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#references-ja>)

  3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。
- [浅角度分散波束の長時間・同格子孤立境界参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 均質Lorentz媒質はPML内まで連続し、ε∞=1、Δε=0.2、ω0=12、γ=0または0.005。Ez偏光の有限kx Gaussianはcarrierω=6、中心位相角80度。512/768/1024点とpeak6/9/12を同時細分化し、垂直対照は6、弱減衰細格子対照は12。最終時刻は700です。 有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。
- [浅角度分散波束の長時間・同格子孤立境界参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 均質Lorentz媒質はPML内まで連続し、ε∞=1、Δε=0.2、ω0=12、γ=0または0.005。Ez偏光の有限kx Gaussianはcarrierω=6、中心位相角80度。512/768/1024点とpeak6/9/12を同時細分化し、垂直対照は6、弱減衰細格子対照は12。最終時刻は700です。
- [分散媒質の浅い入射角と長時間PML：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-validation>)

  3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。
- [浅角度分散波束の長時間・同格子孤立境界参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 均質Lorentz媒質はPML内まで連続し、ε∞=1、Δε=0.2、ω0=12、γ=0または0.005。Ez偏光の有限kx Gaussianはcarrierω=6、中心位相角80度。512/768/1024点とpeak6/9/12を同時細分化し、垂直対照は6、弱減衰細格子対照は12。最終時刻は700です。 有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

## コード・検証

- [分散媒質の浅い入射角と長時間PML](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja>)
  availability: run

  80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。
