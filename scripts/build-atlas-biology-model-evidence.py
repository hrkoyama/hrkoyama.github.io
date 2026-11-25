#!/usr/bin/env python3
"""Prime biological model evidence before equation/survey strict cross-checks."""
from pathlib import Path
import json
from atlas_goal_availability import load_supplemental_examples
from atlas_biology_model_evidence import apply_biology_model_evidence, apply_canonical_biology_supplements

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'catalog/atlas-depth.json').read_text())
biology = next(field for field in data['fields'] if field['id'] == 'biology')
registry = json.loads((ROOT / 'numerical-methods-atlas/code-and-data/examples.json').read_text())
examples = {row['id']: row for row in registry['examples']}
# The loader verifies the exact manifest, ZIP, stored numerical flags and independent rerun receipt.
identifiers = list(dict.fromkeys(['turing-schnakenberg', 'schnakenberg-nonlinear', 'schnakenberg-pattern', 'fitzhugh-nagumo'] +
                              [ident for row in biology.get('model_supplements', {}).values() for ident in row['case_ids']] + biology.get('supplemental_examples', [])))
supplements = {row['id']: row for row in load_supplemental_examples(ROOT, identifiers)}
path = ROOT / 'numerical-methods-atlas/assets/biological-models.json'
survey = json.loads(path.read_text())
apply_biology_model_evidence(survey, biology, examples, supplements, data['reviewed_on'])
equations = json.loads((ROOT / 'catalog/atlas-equations.json').read_text())['equations']
case_equations = json.loads((ROOT / 'catalog/atlas-depth-expansion.json').read_text())['case_equations']
apply_canonical_biology_supplements(survey, biology, equations, supplements, case_equations)
path.write_text(json.dumps(survey, ensure_ascii=False, indent=2) + '\n')
print('Primed strict biological model evidence from explicit verified cases.')
