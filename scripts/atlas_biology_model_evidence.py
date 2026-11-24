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
