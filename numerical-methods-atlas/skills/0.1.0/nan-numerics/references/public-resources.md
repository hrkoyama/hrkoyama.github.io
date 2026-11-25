# Public resource routes

The canonical origin is `https://hrkoyama.github.io/`. Atlas paths below are relative to `/numerical-methods-atlas/`. Use the current linked records rather than fixed inventory counts.

## Discover, then select

- The atlas home search and `test-cases/` find named problems. `test-cases/index.json` contains `problems` with stable IDs, names, reading links and execution bindings. Select matching objects programmatically rather than pasting the whole inventory into context.
- `methods/` lists methods and their availability. Each method page links its own `index.json` and `index.md`. These records may include extensive nested evidence: extract the task-relevant fields before presenting them to a model. `methods/reviewed.json` is a curated subset, not complete coverage.
- `gallery/` and `gallery/index.json` connect problem figures to equations, reference solutions and actual execution examples. Shared or illustrative figures are labelled separately from new computations.
- `equations/index.json` contains equation/model records. `solutions/index.json` contains reference-solution records. Follow the selected object's links; do not assume every model has runnable code.
- `validation/<case-id>/index.json` and `index.md` describe a supplemental execution example: assumptions, adopted algorithm, validation, limits and linked artifacts. Obtain the case ID from an existing link; problem IDs and execution-case IDs need not match.
- `code-and-data/examples.json` describes the earlier shared execution families. It is a different registry from `validation/releases.json`, which lists versioned supplemental ZIP releases. Select the registry linked by the actual example.
- `reading-resources.json` and each reading chapter's `resources.json`/`resources.md` connect explanations to their scoped methods and evidence.

If a problem hub or chapter resource list exposes only a forward solver while the task needs a different operation (for example an inverse problem), also check the relevant chapter body for its dedicated execution links. Discovery lists can omit a dated example. Verify the linked package itself and report the missing association; do not treat a nearby problem or method as evidence for an unrelated operation.

When a record links a versioned download, verify the linked manifest/archive hash before relying on it. Read the example's instructions before running it, and keep execution in a fresh task directory. The atlas does not require installing every example or recreating old, expensive reference studies.

## Read outcomes with their scope

For a selected execution record, inspect the input parameters, `measured` data, checks, original study goals and `limits`. Exact field shape varies by edition: follow the linked result and acceptance file rather than inventing missing values. A group's test count may be shared by several cases; it is not the count of independently solved physical problems.

A saved numerical reference may be qualified only for fixed meshes, times or observables. Refinement differences and stochastic confidence rules are not universal error bounds. Distinguish a freshly repeated calculation, a comparison against saved data, and a citation-only statement in the final report.
