"""Apply only explicit, receipt-backed availability overlays to the 22-model survey."""

def apply_biology_model_evidence(survey, biology, examples, supplements, reviewed_on):
    models = {model['id']: model for model in survey['models']}
    assert len(models) == len(survey['models']), 'Repeated biological survey identity'
    survey.update(checked_on=reviewed_on, scope=biology['scope']['en'])
    # Preserve the five existing scoped identities and their exact source rules.
    for model in survey['models']:
        ident = {'logistic': 'logistic-growth', 'sir': 'sir-epidemic'}.get(model['id'])
        if ident:
            model.update(status='scoped-educational-example', execution_examples=[ident],
                         implementation_scope=examples[ident]['scope'])
        extra = {'turing': ['turing-schnakenberg', 'schnakenberg-nonlinear', 'schnakenberg-pattern'],
                 'schnakenberg': ['turing-schnakenberg', 'schnakenberg-nonlinear', 'schnakenberg-pattern'],
                 'fitzhugh-nagumo': ['fitzhugh-nagumo']}.get(model['id'])
        if extra:
            scope = biology['schnakenberg_scope'] if model['id'] in ['turing', 'schnakenberg'] else supplements[extra[0]]['limits']
            model.update(status='scoped-educational-example', supplemental_examples=extra,
                         implementation_scope=scope, execution_url=supplements[extra[0]]['url'])
    protected = {'logistic', 'sir', 'turing', 'schnakenberg', 'fitzhugh-nagumo'}
    bindings = biology.get('model_supplements', {})
    assert isinstance(bindings, dict)
    for model_id, binding in bindings.items():
        assert model_id in models and model_id not in protected, 'Existing scoped source rule cannot be replaced'
        assert isinstance(binding, dict) and set(binding) == {'group', 'case_ids'}
        selected = binding['case_ids']
        assert isinstance(selected, list) and len(selected) == 1, 'One explicit case per new survey overlay'
        ident = selected[0]
        assert ident in biology.get('supplemental_examples', []), 'Model case must belong to the biology field'
        case = supplements[ident]  # Supplied only by the strict immutable-release loader.
        assert case['group'] == binding['group'], 'Model case belongs to a different release group'
        scope = case['limits']
        assert all(isinstance(scope.get(lang), str) and scope[lang].strip() for lang in ['ja', 'en'])
        models[model_id].update(status='scoped-educational-example', supplemental_examples=list(selected),
                                implementation_scope=dict(scope), execution_url=case['url'])
    return survey


def apply_canonical_biology_supplements(survey, biology, equations, supplements, case_equations):
    """Prime surveyed availability from explicit canonical model/case ownership.

    Records are supplied only by load_supplemental_examples, which verifies the
    immutable manifest, complete ZIP, saved flags and independent-extraction proof.
    Earlier common, 1D pattern and small-model source rules remain authoritative.
    """
    models = {row['id']: row for row in survey['models']}
    assert len(models) == len(survey['models'])
    rows = [row for row in equations if row['group'] == 'biology' and
            row.get('formula_source', {}).get('path') == 'numerical-methods-atlas/assets/biological-models.json']
    source_models = [row['formula_source']['model_id'] for row in rows]
    assert len(source_models) == len(set(source_models)), 'Ambiguous survey equation provenance'
    protected = {'logistic', 'sir', 'turing', 'fitzhugh-nagumo'}
    old_patterns = ['turing-schnakenberg', 'schnakenberg-nonlinear', 'schnakenberg-pattern']
    for equation in rows:
        selected = equation.get('supplemental_examples', [])
        assert isinstance(selected, list) and len(selected) == len(set(selected))
        mapped = [ident for ident in selected if ident in case_equations]
        if not mapped:
            continue  # Preserve earlier common/legacy source rules unchanged.
        model_id = equation['formula_source']['model_id']
        assert model_id in models and equation['id'] == 'bio-' + model_id
        assert equation['status'] == 'local-example'
        assert all(ident in biology.get('supplemental_examples', []) and ident in supplements for ident in selected)
        scope = equation['execution_scope']
        assert all(isinstance(scope.get(lang), str) and scope[lang].strip() for lang in ['ja', 'en'])
        for ident in mapped:
            binding = case_equations[ident]
            ids = binding['ids']
            assert isinstance(ids, list) and ids and len(ids) == len(set(ids))
            assert equation['id'] in ids, 'Supplement does not own this biological model'
        if model_id in biology.get('model_supplements', {}):
            # Keep batch78 enzyme/LV exact case limits and group bindings, not a
            # new model-family scope inferred from a later title or method.
            binding = biology['model_supplements'][model_id]
            assert selected == binding['case_ids'] == models[model_id]['supplemental_examples']
            assert models[model_id]['implementation_scope'] == scope
            assert all(supplements[ident]['group'] == binding['group'] for ident in selected)
            continue
        assert model_id not in protected, 'Earlier common/scoped source rule cannot be replaced'
        if model_id == 'schnakenberg':
            assert selected[:len(old_patterns)] == old_patterns and len(selected) == len(old_patterns) + 1
            assert mapped == selected[len(old_patterns):], 'Preserve all three earlier 1D pattern cases'
        else:
            assert selected == mapped and len(mapped) == 1, 'One explicit canonical case per added survey family'
        for ident in mapped:
            case = supplements[ident]
            assert case['id'] == ident and case['group'] in ['biology-ode-controls', 'biology-space-controls']
            paths = [path for path in case['source_sha256'] if path.startswith('code/validated-examples/') and
                     path.endswith('/' + case['group'] + '/cases.json')]
            assert len(paths) == 1, 'Unique verified case metadata source required'
            checksum = case['source_sha256'][paths[0]]
            assert isinstance(checksum, str) and len(checksum) == 64 and all(c in '0123456789abcdef' for c in checksum)
        models[model_id].update(status='scoped-educational-example', supplemental_examples=list(selected),
                                implementation_scope=dict(scope), execution_url=supplements[selected[0]]['url'])
    return survey
