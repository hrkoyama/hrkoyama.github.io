"""Read explicit, release-specific method coverage without changing science metadata."""

def depth_coverage_scope(method, language):
    """Use an explicit method scope or its exact primary-release profile."""
    if language not in ('ja', 'en'):
        raise ValueError('Unknown coverage language')
    if 'depth_scope' in method:
        scope = method['depth_scope']
        if not isinstance(scope, dict) or any(not isinstance(scope.get(lang), str) or not scope[lang].strip() for lang in ('ja', 'en')):
            raise ValueError('Invalid explicit method coverage scope')
        return scope[language]
    release = method.get('depth_release')
    if not isinstance(release, dict) or not all(release.get(k) for k in ('group', 'edition', 'case_ids')):
        raise ValueError('Missing primary release for coverage scope')
    matches = [row for row in method.get('supplemental_scope_profiles', []) if row.get('release') == release]
    if len(matches) != 1:
        raise ValueError('Primary release needs one explicit coverage profile')
    profile = matches[0]
    limits = profile.get('limits')
    if not isinstance(limits, list) or not limits:
        raise ValueError('Primary release needs explicit limits')
    for text in [profile.get('scope'), *limits]:
        if not isinstance(text, dict) or any(not isinstance(text.get(lang), str) or not text[lang].strip() for lang in ('ja', 'en')):
            raise ValueError('Primary release needs bilingual coverage and limits')
    return ' '.join([profile['scope'][language], *(row[language] for row in limits)])

