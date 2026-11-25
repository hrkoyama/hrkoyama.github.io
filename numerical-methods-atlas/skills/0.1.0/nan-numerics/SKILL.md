---
name: nan-numerics
description: Use NaN, the open numerical-methods atlas, to choose and adapt scientific algorithms with source-linked equations, runnable examples and explicit verification. Use when developing or checking numerical software with the atlas.
---

# Develop with NaN

Use the public [NaN atlas](https://hrkoyama.github.io/numerical-methods-atlas/) as evidence for the user's numerical task. Work in the user's chosen language and software environment; the atlas examples are starting points, not a required framework.

## Find a relevant example

Identify the equation, target observable, units, geometry, initial/boundary conditions and accuracy requirement that affect method choice. Infer these from the project when available. Search the atlas for the problem or method, then open only the relevant records. [Public resource routes](references/public-resources.md) explains the JSON/Markdown entry points; do not load the complete method registry into the model context.

Check the adopted variant and applicability limits before borrowing code. A planned method is not an available implementation. Null or unknown assumptions are missing curation, not unrestricted applicability. A gallery image is a route to evidence, not proof of correctness.

## Adapt and verify

Follow the chosen example to its fixed inputs, source manifest, versioned code, acceptance rules, reference provenance and recorded outcome. Distinguish continuous exact solutions, discrete exact solutions, manufactured solutions and finite numerical references. A paper for an algorithm need not be the source of the test problem or its reference solution.

Run a small relevant example when the task calls for executable work. Preserve its original criteria and outcome. For the user's changed problem, define suitable checks separately: residuals, conservation, refinement, independent comparisons or gradient checks as applicable. State which checks were actually run and which saved results were only inspected. Reproduction success does not imply every original accuracy or statistical goal was met.

Deliver the working change with the evidence needed to assess it: the selected method and conditions, source URLs and code edition, measured verification, and material limits. If the atlas does not cover the requested regime, say so and use appropriate primary sources rather than extending its claims. Do not imply measured speedups, reliability for arbitrary problems, or lower-cost-LLM effectiveness without corresponding evidence.
