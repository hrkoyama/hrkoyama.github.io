# Hiroshi Koyama — Research profile and archives

https://hrkoyama.github.io/

GitHub Pages serves the static files on `main` from the repository root. Existing dissertation and Academic Roots pages are retained.

For current atlas counts, editing sources, validation and publication, see [MAINTENANCE.md](MAINTENANCE.md). Earlier maintenance records are preserved in [maintenance history](docs/maintenance-history/README.md).

## Archives

- `/gordon-bell/`: Gordon Bell Prize Paper Archive（ゴードン・ベル賞 論文アーカイブ）, including the original research dataset and search/export interface. Centered on finalist and prize-winning papers, with a separate historical competition-entry index; some entries are not confirmed finalists or single papers.
- `/notebooks/`: the existing public notebook viewing collection, with redactions unchanged.
- `/hpci-policy/`: bilingual Computing Policy Archive and history/budget pages.

The three archives were transferred on 2026-11-16. Their previous public paths were removed without redirects or migration links. No private notebook originals or old repository history were imported.

Preview: `python3 -m http.server 4180 --bind 127.0.0.1`.

## Notebook viewing release

The reviewed notebook collection is published at `/notebooks/`: 41 notebooks and 1,170 selected pages, with pixel-level redactions retained. Only the existing public viewing assets and licensing notices are included. Private originals, OCR audit records and the original repository history remain outside this repository. `notebooks/public-manifest.json` records the viewing file hashes. Publish new notebook material only after the same allowlist, redaction and metadata checks.

## Add to the Computing Policy Archive

1. Edit `hpci-policy/content.json`. Add Japanese and English text to a record and list its public sources in `sources`. Connect records to `first` or `second` only when the relevant secondment is known; use an empty `periods` array when that relationship is awaiting confirmation.
2. Mark a source `read` only after its text has been reviewed. Use `indexed-only` with a note when only an index or reference has been verified. Update the source's `checked` date and the archive's `updated` date after research.
3. Run `node scripts/build-policy.mjs`. Commit the generated `hpci-policy/index.html` together with the data. The generator checks source and period references and escapes content; Japanese text is readable without JavaScript. The deployed site needs no runtime dependencies or build service.
4. Preview `/hpci-policy/?lang=ja` and `/hpci-policy/?lang=en`. Check search, period filters, source links, and both narrow and wide layouts after content changes.

The page-specific interface translations are in `hpci-policy/site.js` and its layout is in `hpci-policy/style.css`. The supplied career document is used only as background for the requested career facts; the document itself and personal contact details are not included in this repository. The second secondment's start month follows the supplied CV; its end month and both roles were confirmed by the author.

The confirmed committee directory is in `hpci-policy/committees.json`. Each entry contains a bilingual summary and public milestone, its original MEXT or NDL WARP link, optional additional evidence, and any parent committee or detailed-record association. `retrievedUrl` records the archived document frame read during research. `verification: "read"` means the landing-page content was read, rather than every document linked from it. Entries can be filtered by topic and searched independently of the detailed responsibilities. Only assign a `periods` value when the personal assignment period is known.

The author excluded eight entries from the initial MEXT list: 071, 059, 035, 034, 027, 019, 017, and 016. These are not included in the personal directory. The source list's contradictory FY2015 end-date label is not copied as a personal assignment date. The legal context is in `content.json` under `framework`; historical assignments should use the version of the law and policy applicable at the time.

## Committee relationships, timeline and budgets

The bilingual [`hpci-policy/history.html`](https://hrkoyama.github.io/hpci-policy/history.html) is generated from `hpci-policy/history.json`. It connects institutional context to the 19 confirmed committees and includes six relationship views, an evidence panel, a filterable timeline, a 2006–2025 budget-overview chart, individual award examples, and political advocacy context. A relationship is typed as `parent`, `report` or `sequence`: do not turn a reporting relationship or chronological progression into a formal hierarchy. In particular, the post-2019 Information Committee is directly under the science council, and the exploratory projects sub-working group is under the priority-projects WG. Institutional context does not add personal involvement claims.

Run both generators after editing:

```sh
node scripts/build-policy.mjs
node scripts/build-history.mjs
```

`history-render.mjs` provides the shared server/browser bilingual rendering; `history.js` supplies interactions; `budget-chart.mjs` renders the financial chart. Commit the generated HTML and `hpci-policy/budget-data.csv` with the data and scripts. The deployed site has no package/CDN dependencies. The builder checks source IDs, diagram endpoints, all committee relationships, annual coverage, monetary values and review-sheet arithmetic.

### Financial scope and provenance

The chart is a **major direct-program budget overview**, not an exhaustive total of all supercomputing-related MEXT spending. Operating block grants are excluded at the author’s explicit request. Earth Simulator and SINET are separate programs outside this series. All 20 fiscal years have an overview observation; FY2006–2013 are source-rounded totals, FY2014 is labeled “budget” by the source, and FY2019 currently uses a proposal. Reconciliation into one consistent accounting boundary is incomplete. Requests, supplementary budgets and expenditure are explicitly partial. Missing years are not zero.

Preserve each record's `kind`, `sourceAmountType`, `basis`, `precision`, `year`, `series`, `sourceIds` and bilingual notes. `millionYen` is nominal JPY million; the chart converts to JPY 100 million. Keep the budget-overview and administrative-review accounting scopes distinct, and retain carry-in, carry-out and reserve adjustments in `reviewComparison`. Never add award or subcontract records to a program total, multi-year commitments to annual appropriations, or compute-resource allocations to monetary allocations. Grant decisions are not final settlements or actual institutional expenditure. The individual award list is a verified starting sample, not all selected projects.

### Recipient, purpose and researcher employment

The `spending` dataset in `history.json` contains independently bounded cases. It separates recipient classification from expenditure purpose: a computer purchase is also a company payment, so those categories cannot be summed as one partition. The FY2022 RIKEN operations example uses source blocks A and I (14,424 and 12,530 JPY million). The Tokyo University fluid-prediction example uses the largest recipient in block G (84 JPY million, including 18 million personnel), not every institution or the entire project. Ratios are computed from the published rounded amounts. Remaining expenses are not inferred to be salaries.

`spending-render.mjs` renders those cases with their own denominators. PI salary-charging records are separately labeled and do not establish new employment. Aggregate equipment and newly hired researcher shares stay `null` until matching source accounts exist. The builder validates case totals and source references. The author requested operating block grants to stay outside the analysis.

The history builder hashes the shared modules and styles, emits versioned asset URLs and a matching import map, so an already-open browser receives updated renderers along with new data.

### Official links

The history page’s `#links` section groups nine official destinations for community recommendations, HPCI access and selection results, operating/support organizations, and policy/institutional documents. Edit bilingual titles, descriptions, URLs and check dates in `history.json` → `relatedLinks`; the builder validates these records. This directory is separate from the evidence index and does not add personal involvement claims.

## Japan–U.S. supercomputer comparison

The HPCI archive itself includes an interactive comparison at [`/hpci-policy/?lang=ja#japan-us`](https://hrkoyama.github.io/hpci-policy/?lang=ja#japan-us), without changes to the personal homepage. Tabs cover a 13-system timeline, published costs, a two-system comparison, decision-making and 30 primary sources. The archive’s existing Japanese/English switch also controls this section.

- `hpci-policy/comparison.json` preserves system-specific milestone definitions, cost scopes, historical source dates, evidence links and English descriptions. `cost` is in the explicitly declared `costUnit` (JPY 100 million or USD million), not base currency.
- `comparison-render.mjs` shares static and interactive rendering and validates source references and data. `comparison.js` handles scoped controls, keyboard-operable tabs and language changes. `comparison.css` uses a separate `sc-` namespace.
- Run `node scripts/build-policy.mjs` to regenerate the archive HTML and `comparison-data.csv`. The CSV exports **base currency** in `amount_native_currency`, preserves missing totals, and distinguishes future targets. Versioned module/style URLs prevent stale combinations. The deployed page has no framework or CDN dependency; chart content remains available without JavaScript.

Costs and intervals are intentionally heterogeneous historical observations, not a reconciled lifecycle-cost or development-efficiency ranking. The Summit/Sierra joint amount is not divided between systems. FugakuNEXT annual funding is not treated as a full project total. The comparison does not add personal involvement claims to the archive.


## Licensing

Original implementation code is MIT; text, figures, scans, PDFs and data have separate terms. See `LICENSING.md`, `THIRD_PARTY_NOTICES.md` and `/rights/`. Archive-specific notices take precedence.

## Shared language, navigation and site policy

`site.css` and `site.js` provide common navigation and rights notices. The explicit `?lang=ja` / `?lang=en` parameter wins over the stored preference (`hrkoyama.home.language`); language selection follows internal HTML links while preserving other query parameters and fragments. Profile, dissertation and rights pages include both languages in static HTML. Their language sections remain readable without JavaScript. Japanese Academic Roots/notebook content and the English Gordon Bell archive retain their original languages, identified in the common header.

After editing static HTML or the shared chrome, run `node scripts/build-site-chrome.mjs`. Both HPCI generators also call the shared decorator so rebuilds retain the navigation and notices. The chrome build refreshes only the existing public notebook manifest receipts; scans, redactions and PDFs must remain unchanged.

The shared decorator also assigns the site-wide `favicon.svg`: a navy H monogram with a gold star, distinct from the old portfolio's green orbital mark. Its URL includes the icon content hash so browsers can fetch an updated icon. Rebuild the shared chrome and then the local guide snapshot after changing the icon.

`/rights/`, `LICENSING.md`, the notebook notice, `/robots.txt` and `/llms.txt` must agree: welcome AI search, indexing, summaries, source-linked quotation and research/learning analysis; distinguish original code (MIT), content, visitor data and third-party rights. Do not claim blanket redistribution rights over linked papers or notebook content. The AI guide is a resource index, not a full text mirror or proof of source verification.

## Numerical methods, thermal instability and Research Compass (2026-11-16)

- `/guide/`: bilingual, browser-local retrieval over 159 public text pages and two project overviews. Source links, exports and knowledge packs use this site's URLs. It hosts no LLM and never sends questions to the operator.
- `/numerical-methods-atlas/`: the reviewed public numerical-methods website, including its static English/Japanese reading rooms and interactive experiments.
- `/the-art-of-thermal-instability/`: the reviewed English archive, figures, data, code and movie-gallery assets. Prototype and validation limits are preserved.

The upstream source archives are retained privately at `https://github.com/koyamarium/numerical-methods-atlas` and `https://github.com/koyamarium/the-art-of-thermal-instability`. The main public HTML rebuilt from those sources matched the previous production HTML byte for byte before URL/navigation adaptation. `research-imports.json` records the source commits and hashes for unchanged binary/download assets. Only the reviewed `website/dist/` and `dist/` artifacts were imported; numerical experiments were not rerun. The original project Pages sites are unpublished after this deployment was verified. No redirect or migration link is added on the previous portfolio.

To refresh reviewed publication artifacts:

```sh
python3 scripts/import-research-sites.py --numerical-dist /absolute/path/to/numerical/website/dist --thermal-dist /absolute/path/to/thermal/dist
node scripts/build-site-chrome.mjs
python3 scripts/build-guide.py --local-site .
node --test scripts/guide.test.mjs scripts/research-model.test.mjs
```

Retain upstream licensing notices and KaTeX/Marked notices. Refresh the root sitemap when pages are added or removed. Shared navigation changes require rebuilding the guide afterward so its per-page source hashes describe the exact HTML.

## Complete astrophysics textbook migration (2026-11-16)

`/astronomy-step-by-step/ja/` and `/astronomy-step-by-step/en/` host the entire bilingual textbook: 16 foundation chapters, 35 advanced worked chapters, the solution library, textbook guide, numbers-and-units supplement and teaching principles. The later full-site request superseded the paused three-section proposal; the supplement is included as part of the complete textbook.

`astronomy-import.json` records the upstream source commit and original public-file hashes. Build the upstream `astronomy-step-by-step` repository with `node scripts/check.mjs`, `node scripts/build.mjs`, and `node scripts/check-static.mjs`, then run:

```sh
node scripts/import-astronomy.mjs /absolute/path/to/astronomy-step-by-step/dist
node scripts/build-site-chrome.mjs
```

The importer rebases site URLs, preserves all educational model modules and SVG figures, and connects the textbook's language controls to the shared site navigation while preserving interactive control values. Upstream source: `https://github.com/koyamarium/astronomy-step-by-step`. Its old Pages publication is stopped after verifying the new copy. No migration link or redirect is added to the old portfolio.

Add changed entry pages to the root sitemap when refreshing the textbook. This migration does not add astrophysics to the two-domain Research Compass corpus.

## Search Console verification

Keep `google0b2aef3d9ae4b856.html` at the site root. This is the Google-issued HTML ownership verification file for `https://hrkoyama.github.io/`; removing it can invalidate ownership verification. The submitted discovery entry point is `https://hrkoyama.github.io/sitemap.xml`.

## Public contact information

The rights page, licensing notices, bibliography and AI guide do not publish an individual email address. Keep Japanese and English wording aligned. Importers direct legacy contact references to the published rights policy; do not restore a contact address or advertise an unavailable inquiry form. Author attribution is retained.


## Site-wide search

The shared header provides a search field on every content page. /search/ searches only public same-site HTML listed in the root sitemap, public Gordon Bell metadata and the notebook catalog. It does not index image/PDF contents, unpublished files, external pages or browser-local user data. Queries stay in the URL fragment and are not sent to an external search provider or to the hosting server. The two-domain Research Compass retains its separate scope.

After adding or editing searchable pages, run the shared chrome build, rebuild the local Research Compass snapshot, then run python3 scripts/build-search.py. Commit the generated /search/index.json and the versioned search page/module links together. The search builder takes no network input and performs no OCR. Search result URLs are restricted to this site and results render using text nodes.

## Maintenance and public resource guidance

See [MAINTENANCE.md](MAINTENANCE.md) for the single refresh/check/publish sequence and bundle-based recovery. Run `python3 scripts/refresh-site.py` after any import or content change, followed by `node --test scripts/*.test.mjs`. Public usage and citation guidance is at `/using/`. The public thermal work record is generated from `catalog/thermal-work-queue.json`; its JSON, progress and download pages are regenerated from reviewed public content. Supplemental catalog sources and versioned Python editions are kept outside imported website trees so a refresh does not delete the editing source.
