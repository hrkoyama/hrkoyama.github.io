"""Availability of resources for a specific goal, without promoting catalog status."""
def goal_methods(goal, methods):
    rows = [dict(methods[ident]) for ident in goal['methods']] + [dict(x) for x in goal.get('resources', [])]
    for row in rows:
        if goal.get('availability') == 'reading-only':
            row.update(status='reading-only', code_urls=[], test_urls=[], execution_examples=[])
    return rows


def goal_label(goal, methods, lang):
    rows = goal_methods(goal, methods)
    if any(row['status'] == 'educational-example' for row in rows):
        pair = ('固定入力で実行', 'Runnable fixed inputs') if goal['examples'] else ('関連コード・テストあり', 'Related code and tests')
    elif rows and all(row['status'] == 'planned' for row in rows):
        pair = ('解説あり・実装予定', 'Reading; implementation planned')
    else:
        pair = ('解説のみ・専用実装なし', 'Reading only; no implementation')
    return pair[0 if lang == 'ja' else 1]
