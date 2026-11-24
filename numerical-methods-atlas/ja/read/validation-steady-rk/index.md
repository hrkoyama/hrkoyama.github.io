# 定常多段RKのモード減衰

16成分の周期線形場で擬似時間の残差減衰を測り、安定・非減衰・発散の対照を示します。非線形非定常問題の4次精度とは区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 定常多段RKの実空間モード減衰

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。

**使用手法**

- [Jameson型の定常多段Runge–Kutta](https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=ja) (`jameson-steady-rk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-algorithm)

全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`)

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`)

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。


**問題の図**

![定常多段RKの実空間モード減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja) (`jameson-steady-linear-modes`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-validation)

元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。

- [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-jameson-steady-linear-modes-ja) (`jameson-steady-linear-modes`; 同じ問題の参照 · 解析参照)

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。
### 前提・単位・境界

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

**編集上の補足**

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

### 比較・検証

元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。

### 確認の限界

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

### 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "reference:h32-mode4:expanded-vs-stages": true,
    "reference:h32-mode4:prior-classification": true,
    "reference:h32-mode8:expanded-vs-stages": true,
    "reference:h32-mode8:prior-classification": true,
    "reference:h16-mode4:expanded-vs-stages": true,
    "reference:h16-mode4:prior-classification": true,
    "reference:h16-mode8:expanded-vs-stages": true,
    "reference:h16-mode8:prior-classification": true,
    "reference:neutral:expanded-vs-stages": true,
    "reference:neutral:prior-classification": true,
    "reference:expanding:expanded-vs-stages": true,
    "reference:expanding:prior-classification": true,
    "reference:rational-stencil-mode4": true,
    "reference:rational-stencil-mode8": true,
    "stable-h32:finite": true,
    "stable-h32:stage-count": true,
    "stable-h32:spurious-mode": true,
    "stable-h32:true-residual-reference": true,
    "stable-h32:field-error": true,
    "stable-h32:residual-reduction": true,
    "stable-h32:nonzero-mode4": true,
    "stable-h16:finite": true,
    "stable-h16:stage-count": true,
    "stable-h16:spurious-mode": true,
    "stable-h16:true-residual-reference": true,
    "stable-h16:field-error": true,
    "stable-h16:residual-reduction": true,
    "stable-h16:nonzero-mode4": true,
    "neutral-constant:finite": true,
    "neutral-constant:stage-count": true,
    "neutral-constant:spurious-mode": true,
    "neutral-constant:true-residual-reference": true,
    "neutral-constant:neutrality": true,
    "expanding-nyquist:finite": true,
    "expanding-nyquist:stage-count": true,
    "expanding-nyquist:spurious-mode": true,
    "expanding-nyquist:true-residual-reference": false,
    "expanding-nyquist:expected-expansion": true,
    "expanding-nyquist:normalized-error": true,
    "steady-fixed-point": true,
    "four-record-identities": true
  },
  "original_target_summary": {
    "met": 40,
    "total": 41,
    "all_met": false,
    "acceptance_sha256": "af846323a4e4235d968ecb431eea825fbee40f7a1047e65b18c70b7d4a83fe00"
  }
}
```

### 保存実測値と判定

```json
{
  "metrics": {
    "stable-h32:field-error": 3.3306690738754696e-16,
    "stable-h32:residual-reduction": 6.446370751486289e-09,
    "stable-h32:nonzero-mode4": 1.5238393618337132e-08,
    "stable-h16:field-error": 2.220446049250313e-16,
    "stable-h16:residual-reduction": 6.6210787709662455e-09,
    "stable-h16:nonzero-mode4": 1.5381125809623605e-08,
    "neutral-constant:neutrality": 0.0,
    "expanding-nyquist:expected-expansion": 1875.5948651814128,
    "expanding-nyquist:normalized-error": 3.634886991251329e-16,
    "max_field_error": 6.821210263296962e-13,
    "original_targets_met": 40,
    "original_targets_total": 41
  },
  "checks": {
    "reference:h32-mode4:expanded-vs-stages": true,
    "reference:h32-mode4:prior-classification": true,
    "reference:h32-mode8:expanded-vs-stages": true,
    "reference:h32-mode8:prior-classification": true,
    "reference:h16-mode4:expanded-vs-stages": true,
    "reference:h16-mode4:prior-classification": true,
    "reference:h16-mode8:expanded-vs-stages": true,
    "reference:h16-mode8:prior-classification": true,
    "reference:neutral:expanded-vs-stages": true,
    "reference:neutral:prior-classification": true,
    "reference:expanding:expanded-vs-stages": true,
    "reference:expanding:prior-classification": true,
    "reference:rational-stencil-mode4": true,
    "reference:rational-stencil-mode8": true,
    "stable-h32:finite": true,
    "stable-h32:stage-count": true,
    "stable-h32:spurious-mode": true,
    "stable-h32:true-residual-reference": true,
    "stable-h32:field-error": true,
    "stable-h32:residual-reduction": true,
    "stable-h32:nonzero-mode4": true,
    "stable-h16:finite": true,
    "stable-h16:stage-count": true,
    "stable-h16:spurious-mode": true,
    "stable-h16:true-residual-reference": true,
    "stable-h16:field-error": true,
    "stable-h16:residual-reduction": true,
    "stable-h16:nonzero-mode4": true,
    "neutral-constant:finite": true,
    "neutral-constant:stage-count": true,
    "neutral-constant:spurious-mode": true,
    "neutral-constant:true-residual-reference": true,
    "neutral-constant:neutrality": true,
    "expanding-nyquist:finite": true,
    "expanding-nyquist:stage-count": true,
    "expanding-nyquist:spurious-mode": true,
    "expanding-nyquist:expected-expansion": true,
    "expanding-nyquist:normalized-error": true,
    "steady-fixed-point": true,
    "four-record-identities": true,
    "verification:original-target-inventory": true,
    "verification:all-original-decisions-recomputed": true,
    "verification:measured-records-match-saved-arrays": true,
    "verification:frozen-original-input-and-acceptance": true,
    "verification:independent-reference-integrity": true,
    "verification:actual-target-summary": true,
    "verification:retained-first-attempt-history": true,
    "verification:only-declared-study-goals-are-nonmandatory": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/index.json

![周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- PERFORM time integration schemes [accessed 2026-11-24]. https://perform.readthedocs.io/en/latest/solver/timeschemes.html; review_level=official-documentation-selected-equations
Selected four-stage base-state recurrence. No full JST 1981 paper reading or compressible-flow implementation claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
