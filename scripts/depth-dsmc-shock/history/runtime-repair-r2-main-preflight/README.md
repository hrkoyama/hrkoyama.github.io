# Hard-sphere DSMC shock — edition 2026-11-24 performance-only preflight

This new edition retains the original20pytest,all15fixed runs (12base seeds371001..371012 and the unchanged3companions),129scientific gates,and one externally enforced120second shared deadline for pytest plus all main inputs. No new115second internal limit is introduced. **The new-edition main has not run at this contract freeze.** Component equivalence is qualified; full saved-science equality and complete runtime remain pending.

The immutable previous edition is https://hrkoyama.github.io/numerical-methods-atlas/code/validated-examples/2026-11-23/dsmc-shock/ . Its original contract/README/case metadata/dsmc.py are retained in history/edition-2026-11-23; its R1/R2failed redesign histories and R3backend qualification remain unchanged. The original complete237file tree was copied; its manifest is retained. Saved results/ initially contain Nov23successful examples for inspection,not evidence of a new run.

The only numerical implementation change is in dsmc.py: cache immutable reservoir CDF coefficients in the original arithmetic order,reuse the already checked residual only when Newton breaks before another velocity update,and concatenate kept,left,right particle arrays once in exactly that order. Six-step exhaustion still evaluates the final updated velocity; all guards/tolerances and the original RNG call/order and pair law are retained. No collision core,initialize/simulate,physical model,seed,grid,weight,timestep,burn/sample window,uncertainty rule or acceptance limit is changed. Reservoir attributes are immutable during production; arbitrary external mutation after construction is outside the cache-equivalence claim.

Runtime qualification in runtime-qualification/ records163exact component byte/RNG/guard/source checks PASS and a separately bounded30s component-only execution (actual receipt2.251018166seconds). It calls no simulate/main/PDE and regenerates no reference. Its fixed-kernel timings do not predict complete-main or Linux success. Source/checker/native snapshots are inert text with exact SHA/pathmap; the binary profiler file is retained privately,not bundled.

The public Linux execution45197177345 on unchanged Nov23source passed the preceding37groups and this group's20tests,then timed out externally during its last half-dt run after14of15complete runs. Its actual failure/checkpoint evidence is retained in runtime-qualification/linux-timeout.json. The84completed per-run checks are not presented as a129gate pass. The original local complete successful Nov23result remains a distinct saved baseline.

Use the exact dependency pins in requirements.txt. Reproduce into a fresh output directory; bundled results/ are saved examples:

    python -W error -m pytest -q -p no:cacheprovider
    python -W error run.py --input inputs.json --output rerun-results
    python plot.py --results rerun-results --output rerun-results

The external parent/public verifier must enforce one120s deadline around pytest and allmain. Nonfinite state,majorant/probability violation,unresolved precision,stationarity failure or timeout fails; no retry,clipping,seed/window selection,output reduction or threshold relaxation. All immediate run checkpoints,NPZs,finite CSVs,history and particle fields remain unchanged. The qualified independent SPARTA finite-grid cache is reused: **reference regeneration0**. RH is only a far-state/full-flux reference,not an exact internal shock profile. See the preserved old README for normalized units,physical collision law,reference provenance,statistical limitations and all prior failed attempts. Newmain execution additionally requires the new contract and independent/root approval; after success a separate exact saved-science comparator must compare all16NPZs,15profileCSVs and JSON scientific fields,excluding only explicit source hashes and elapsed timing.

## 日本語

Nov24版は重複した純計算と配列コピーだけを減らす性能修正です。旧Nov23公開版・元契約・失敗履歴・参照資格を保持し、全20test/15計算/129科学判定・全seed/入力/科学公差・外部共有120秒を変えません。全乱数順・粒子順は成分163項目で厳密比較済みですが、新mainと全保存科学値の比較はこの事前契約時点で未実行です。元版の説明はhistory/edition-2026-11-23/README.mdへ保持しました。配布resultsは保存例であり、新規出力dirへ追試します。独立参照の再生成は行いません。
