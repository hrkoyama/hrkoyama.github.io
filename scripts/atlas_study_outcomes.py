# -*- coding: utf-8 -*-
"""Opt-in display projection of immutable typed study goals; no solver imports."""
import copy
import hashlib
from html import escape
import json
from pathlib import Path
import re


def _read_bound(path, expected):
    if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
        raise ValueError('Missing immutable display-source binding')
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('Missing or unsafe display-source file')
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Changed immutable study-goal display source')
    return raw


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate study-goal source key')
        result[key] = value
    return result


def project_study_outcomes(data, case_id, prefix, origin):
    """Only an explicit catalog prefix enables this projection.

    Read the actual manifest-bound result/acceptance bytes, not hardcoded counts
    or a cached case dictionary. Preserve raw records and true/false/null types.
    """
    if prefix is None:
        return None
    if not isinstance(prefix, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*/', prefix):
        raise ValueError('Study-goal prefix must be an explicit nonempty namespace')
    directory = Path(data['directory'])
    files = data['manifest']['files']
    result_sha = files['results/result.json']
    acceptance_sha = files['acceptance.json']
    raw = _read_bound(directory/'results/result.json', result_sha)
    _read_bound(directory/'acceptance.json', acceptance_sha)
    def invalid(value):
        raise ValueError('Nonfinite display-source JSON constant: '+value)
    source = json.loads(raw, object_pairs_hook=_unique, parse_constant=invalid)
    if source.get('acceptance_sha256')!=acceptance_sha:
        raise ValueError('Study outcomes belong to different acceptance criteria')
    if case_id not in {row['id'] for row in source['cases']}:
        raise ValueError('Study-goal case is not in the bound result')
    goals = source.get('study_goals')
    if not isinstance(goals, dict):
        raise ValueError('Opted-in result has no typed top-level study_goals')
    selected = [(name, raw) for name, raw in goals.items() if name.startswith(prefix)]
    if not selected:
        raise ValueError('Opted-in prefix selects no study goals')
    counts = {'met':0, 'unmet':0, 'unresolved':0, 'total':len(selected)}
    rows = []
    for name, value in selected:
        if isinstance(value, dict):
            if 'observed' not in value:
                raise ValueError('Study record lacks an explicit observed outcome')
            observed = value['observed']
        else:
            observed = value
        if observed is not None and type(observed) is not bool:
            raise ValueError('Study outcome must retain true, false or null')
        outcome = 'unresolved' if observed is None else ('met' if observed else 'unmet')
        counts[outcome] += 1
        rows.append({'name':name, 'observed':observed, 'outcome':outcome,
                     'stored':copy.deepcopy(value)})
    return {'schema_version':1, 'counts':counts, 'goals':rows,
            'classification_basis':'stored observed comparison; separate uncertainty classifications retained',
            'source':{'collection':'study_goals', 'json_pointer':'/study_goals', 'prefix':prefix,
                      'result_sha256':result_sha, 'acceptance_sha256':acceptance_sha,
                      'result_url':origin+data['base']+'results/result.json',
                      'acceptance_url':origin+data['base']+'acceptance.json'}}


def study_outcome_headline(outcomes, language):
    if outcomes is None:
        return ''
    c = outcomes['counts']
    if language=='ja':
        return f"調査した目標：達成{c['met']}・未達{c['unmet']}・未確定{c['unresolved']}（全{c['total']}）"
    return f"Study goals: {c['met']} met, {c['unmet']} unmet, {c['unresolved']} unresolved ({c['total']} total)"


def _label(outcome, language):
    return ({'met':'達成', 'unmet':'未達', 'unresolved':'未確定'}[outcome]
            if language=='ja' else outcome)


def study_outcomes_html(outcomes, language, heading_level=3):
    if outcomes is None:
        return ''
    ja = language=='ja'
    source = outcomes['source']
    rows = []
    for goal in outcomes['goals']:
        stored = json.dumps(goal['stored'], ensure_ascii=False, separators=(',', ':'), allow_nan=False)
        rows.append('<tr><th scope="row">'+escape(goal['name'])+'</th><td>'+_label(goal['outcome'], language)+
                    '</td><td><code>'+escape(stored)+'</code></td></tr>')
    text = ('必須の実行・整合性検査と、元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。別の不確かさ区分と未確定を保持し、記録にない実測値を補いません。'
            if ja else 'Mandatory qualification and study-goal attainment are separate. Met/unmet follow stored comparisons, not statistical certification. Separate uncertainty classifications and unresolved outcomes are retained; missing measurements are not invented.')
    title = study_outcome_headline(outcomes, language)
    return ('<section class="validation-scope validation-study-outcomes" data-typed-study-outcomes="true" data-result-sha256="'+source['result_sha256']+'" data-acceptance-sha256="'+source['acceptance_sha256']+'">'+
            '<h'+str(heading_level)+'>'+escape(title)+'</h'+str(heading_level)+'><p>'+text+'</p><p><a href="'+escape(source['result_url'], quote=True)+'">'+
            ('元の目標・保存結果 / JSON' if ja else 'Original goals and saved results / JSON')+'</a> · <a href="'+escape(source['acceptance_url'], quote=True)+'">'+
            ('固定した判定基準' if ja else 'Fixed acceptance criteria')+'</a></p><details><summary>'+('全目標の記録を読む' if ja else 'Read every study-goal record')+
            '</summary><div class="validation-table" tabindex="0" role="region" aria-label="'+escape(title, quote=True)+'"><table><thead><tr><th scope="col">'+
            ('目標' if ja else 'Goal')+'</th><th scope="col">'+('判定' if ja else 'Outcome')+'</th><th scope="col">'+('元の保存記録（nullも保持）' if ja else 'Original stored record (null retained)')+
            '</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div></details></section>')


def study_outcomes_markdown(outcomes, language, heading_level=3):
    if outcomes is None:
        return ''
    ja = language=='ja'
    headline = study_outcome_headline(outcomes, language)
    text = ('必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。'
            if ja else 'Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.')
    return ('#'*heading_level+' '+headline+'\n\n'+text+'\n\n['+('元の保存結果 / JSON' if ja else 'Original saved results / JSON')+']('+outcomes['source']['result_url']+')\n\n'+
            '<details><summary>'+('全目標の記録を読む' if ja else 'Read every study-goal record')+'</summary>\n\n```json\n'+
            json.dumps(outcomes, ensure_ascii=False, indent=2, allow_nan=False)+'\n```\n\n</details>\n\n')
