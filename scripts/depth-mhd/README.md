# Independent fluid/MHD validation / 流体・MHDの独立比較

Small fixed-input comparisons reuse the atlas's MIT-licensed educational solvers.
They do not overwrite the original immutable `2026-11-22` code edition.

```
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

日英の条件・アルゴリズム・検証・除外範囲・一次文献は `cases.json`、
事前の数値判定幅は `inputs.json` に保存しています。参照計算はAthena++の
固定コミット1395e2f543f4368d448cb1a2cf92ba1f910e3416を別にコンパイルし、
実際に全解像度を実行しました。`references/*provenance.json` は入力・
原出力・保存データ・実行バイナリーのSHA、構築方法と実測時間を残します。

- OT: same continuous periodic data, CT/GLM at16/32/64; independent Athena++128/256.
  Native CT face-divergence and GLM centered divergence use distinct operators.
  Common centered diagnostics are reported too. Short planar t=.05 only.
- Brio–Wu: atlas128/256/512 versus independently executed Athena++2048/4096.
  Both use the HLLD flux family; this is independent code, not an exact solution.
- Shu–Osher: atlas100/200/400 versus Athena++2048/4096/8192. The first reference
  increment missed0.005, so the reference was refined; the miss remains recorded.
- Linear GLM: centered differences/RK4 versus a continuous Fourier matrix exponential.
  This isolated damping diagnostic is not a coupled nonlinear MHD certification.

## Regenerate an independent reference

Download the pinned official source (repository `PrincetonUniversity/athena`).
For OT configure `-b --prob=orszag_tang --flux=hlld --cxx=clang++`;
for Brio configure `-b --prob=shock_tube --flux=hlld --cxx=clang++`;
for Shu configure `--prob=shu_osher --flux=hllc --cxx=clang++` after applying
`references/athena-shu-initial-condition.patch`. Each configuration uses
`make clean` followed by `make -j2`. Solver code is unchanged; the Shu patch
only matches the atlas shock position and sine wavenumber.
Run each binary with the corresponding saved `references/athinput-*` file.
The official output is ASCII `tab` with16-digit precision. The stored `.npz`
contains its numeric table without modifying values. Routine runs use these
stored data and need neither C++ nor network access.

## Saved figures and terms

`python -m pip install -r requirements-plotting.txt` optionally enables
`python plot.py --results output/result.json --output output` using saved data.
Original Python code: MIT (`LICENSE`). Text, figures, inputs and generated data
are excluded from that code grant; consult https://hrkoyama.github.io/LICENSING.md
and https://hrkoyama.github.io/rights/. Athena++ and the problem-generator patch
retain BSD-3-Clause terms (`references/ATHENA-LICENSE.txt`). No third-party
paper PDF or external executable is redistributed.
