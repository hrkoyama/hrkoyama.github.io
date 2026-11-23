# Hard-sphere DSMC shock — edition 2026-11-24 performance-only preflight

This new edition retains the original20pytest,all15fixed runs (12base seeds371001..371012 and the unchanged3companions),129scientific gates,and one externally enforced120second shared deadline for pytest plus all main inputs. No new115second internal limit is introduced. **The new-edition main has not run at this contract freeze.** Component equivalence is qualified; full saved-science equality and complete runtime remain pending.

The immutable previous edition is https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/ . Its original contract/README/case metadata/dsmc.py are retained in history/edition-2026-11-23; its R1/R2failed redesign histories and R3backend qualification remain unchanged. The original complete237file tree was copied; its manifest is retained. Saved results/ initially contain Nov23successful examples for inspection,not evidence of a new run.

The only numerical implementation changes are four performance-only changes in dsmc.py: cache immutable reservoir CDF coefficients in their original arithmetic order; reuse a checked residual only when Newton breaks before another velocity update; concatenate kept,left,right particles once in exactly that order; and reversibly narrow only nonempty integer sort keys in0..255 to uint8 before the same stable argsort. All other keys keep their original dtype. The exact same permutation call,tie order,collision pairs,RNG trace and floating collision formulas are retained. Six-step exhaustion recomputes the residual of its final updated velocity. No core collision law,initialize/simulate,scientific input,seed,grid,weight,timestep,window,uncertainty rule,acceptance limit or diagnostic/output cadence changes. Reservoir attributes remain immutable during production.

Runtime qualification in runtime-qualification/ preserves the original163check component PASS for the first three changes. runtime-qualification/r3/ adds a separate348check R2-to-R3 exact matching/RNG/isolated-collision qualification,completed in 2.6937950840001577seconds under its unchanged30s outer cap. All348checks passed. Both studies call no simulate/main/PDE and regenerate no reference. Timings describe isolated fixed workloads and do not establish complete-main or Linux success. Exact source/checker/native snapshots are inert text with SHA/pathmaps; binary profiler files remain private.

The public Linux execution45197177345 on unchanged Nov23source passed the preceding37groups and this group's20tests,then timed out externally during its last half-dt run after14of15complete runs. Its actual failure/checkpoint evidence is retained in runtime-qualification/linux-timeout.json. The84completed per-run checks are not presented as a129gate pass. The original local complete successful Nov23result remains a distinct saved baseline.

Use the exact dependency pins in requirements.txt. Reproduce into a fresh output directory; bundled results/ are saved examples:

    python -W error -m pytest -q -p no:cacheprovider
    python -W error run.py --input inputs.json --output rerun-results
    python plot.py --results rerun-results --output rerun-results

The external parent/public verifier must enforce one120s deadline around pytest and allmain. Nonfinite state,majorant/probability violation,unresolved precision,stationarity failure or timeout fails; no retry,clipping,seed/window selection,output reduction or threshold relaxation. All immediate run checkpoints,NPZs,finite CSVs,history and particle fields remain unchanged. The qualified independent SPARTA finite-grid cache is reused: **reference regeneration0**. RH is only a far-state/full-flux reference,not an exact internal shock profile. See the preserved old README for normalized units,physical collision law,reference provenance,statistical limitations and all prior failed attempts. Newmain execution additionally requires the new contract and independent/root approval; after success a separate exact saved-science comparator must compare all16NPZs,15profileCSVs and JSON scientific fields,excluding only explicit source hashes and elapsed timing.

## 日本語

Nov24版は重複した純計算と配列コピーだけを減らす性能修正です。旧Nov23公開版・元契約・失敗履歴・参照資格を保持し、全20test/15計算/129科学判定・全seed/入力/科学公差・外部共有120秒を変えません。全乱数順・粒子順は元の成分163項目と別の追加348項目で厳密比較済みですが、新mainと全保存科学値の比較はこの事前契約時点で未実行です。元版の説明はhistory/edition-2026-11-23/README.mdへ保持しました。配布resultsは保存例であり、新規出力dirへ追試します。独立参照の再生成は行いません。
