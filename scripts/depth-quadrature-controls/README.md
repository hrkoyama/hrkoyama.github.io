# Fixed quadrature controls / 固定求積対照

This educational group has three cases and105 fixed primary algorithm rows (30+33+42), not105 physical systems. Independent reference/component qualification is separate:188 checks and30 analytic targets. It is never counted as another primary105-row run. Main and pytest share an external120-second limit. The reference-only budget is30 seconds; desired aggregate local time36 seconds is unmeasured until execution.

The source implements explicit SciPy QUADPACK dispatch, the unchanged existing adaptive Simpson function, own G7/K15 bisection, finite-[0,1] tanh-sinh, and small tensor/Smolyak Clenshaw-Curtis rules. G7 and K15 have polynomial degrees13 and23. Printed coefficients share QUADPACK origin. Existing bump blindness, square-root endpoint, cancellation and Legendre moment evidence is retained as related prior scope, not newly counted.

The independent scalar cache uses directed Decimal80/120 intervals with analytic Taylor/alternating remainders. Precision agreement alone is not its error proof. Finite Gaussian integration uses a true interval target between sqrt(pi)-exp(-36)/6 and sqrt(pi); no unqualified erf point value is substituted. Cache installation binds all reference algorithms, inputs, acceptance and qualification hashes.

For finite-interval DE, I-Q=(I-IT)+(IT-Q). The first term is the continuous omitted integral; the second includes full endpoint weights in the finite sum. These are not an omitted infinite-grid discrete-sum bound. Own improper-domain exp-sinh/sinh-sinh remain unimplemented. Signed sparse weights, non-monotone errors and unresolved interaction products at L<d remain visible. Estimated convergence, actual accuracy goals, protocol controls and required checks have separate fields.

Run `python -B -W error -m pytest -q -p no:cacheprovider` and `python -B -W error run.py --input inputs.json --output results` only under the reviewed outer wrapper. `plot.py --results results/result.json --output results` reads saved data only and imports Matplotlib there, never from scientific main. The public numerical dependencies are exactly the three pins in requirements.txt.

Completed candidates and owned callback prefixes are saved before reference diagnostics. Every512 completed callbacks refresh a raw checkpoint; finally saves the latest prefix on Python exceptions. SIGKILL can preserve only previously flushed points. Raw NPZ can preserve invalid workspace values while finite JSON uses explicit pointers; no NaN/Inf is inserted into public metrics or numeric CSV.

これは3論理例・105固定行の教育用検証です。推定収束、解析精度目標、未解像対照、必須の再現判定を分離します。有限Gaussianは区間参照、DEは連続tailと有限全端点和の誤差を区別し、疎格子の未達目標を合格精度へ読み替えません。元の入力・公差・成功失敗と出典閲覧範囲を保持します。

Source reading is selected and explicitly limited in source-reading.json. Complete QUADPACK/Smolyak books or original proofs were not audited. Rendered Takahasi-Mori equation access failed; extracted selected original passages were read. Software/report versions and access dates are not unverified initial publication dates.
