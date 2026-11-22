"""Compact search connections from published registries and explicit bindings.

Search is a consumer at the end of the build. Neighbour prose, matching names
and shared source files never establish an entity or a verification claim.
"""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from atlas_execution_routes import load_execution_routes

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = ORIGIN+'/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')
GROUPS = ('methods', 'equations', 'figures', 'references', 'code')


def load_search_routes(root=ROOT):
    root = Path(root).resolve()
    executions = load_execution_routes(root)
    sources = dict(executions['source_sha256'])

    def read(path):
        raw = (root/path).read_bytes()
        sources[path] = sha256(raw).hexdigest()
        return json.loads(raw)

    methods = {row['id']: row for row in read('numerical-methods-atlas/methods/index.json')['methods']}
    problems = {row['id']: row for row in read('numerical-methods-atlas/problems/index.json')['problems']}
    equations = {row['id']: row for row in read('numerical-methods-atlas/equations/index.json')['equations']}
    references = {row['id']: row for row in read('numerical-methods-atlas/solutions/index.json')['cases']}
    bindings = {row['id']: row for row in read('catalog/atlas-problem-links.json')['problems']}
    common = {row['id']: row for row in read('catalog/atlas-execution-examples.json')['examples']}
    supplement_index = read('numerical-methods-atlas/validation/index.json')['cases']
    supplements = {row['id']: row for row in supplement_index}
    goals = read('catalog/atlas-goals.json')['goals']
    detailed = read('catalog/atlas-detailed-reading.json')['chapters']
    if set(common) | set(supplements) != set(executions['executions']):
        raise ValueError('Search connections require the complete current execution registry')

    def url_map(path, fragment=None):
        return {lang: BASE+path+'?lang='+lang+('#'+fragment(lang) if fragment else '') for lang in LANGUAGES}

    def pair(ja, en):
        return {'ja': ja, 'en': en}

    def note_join(*notes):
        return {lang: ' '.join(note[lang] for note in notes if note and note.get(lang)) for lang in LANGUAGES}

    def item(ident, name, urls, **extra):
        if not all(isinstance(name.get(lang), str) and name[lang].strip() for lang in LANGUAGES):
            raise ValueError('Missing bilingual search connection name: '+ident)
        for value in urls.values():
            parsed = urlsplit(value)
            if parsed.scheme != 'https' or parsed.netloc != 'hrkoyama.github.io' or '..' in parsed.path.split('/'):
                raise ValueError('Invalid search connection URL: '+value)
        return {'id': ident, 'name': deepcopy(name), 'url': urls, **deepcopy(extra)}

    def graph(kind, ident, note):
        return {'kind': kind, 'id': ident, 'note': note, 'groups': {key: [] for key in GROUPS}}

    def append(target, category, row):
        if not any(old['id'] == row['id'] and old['url'] == row['url'] and
                   old.get('context_problem_id') == row.get('context_problem_id') and
                   old.get('context_execution_id') == row.get('context_execution_id')
                   for old in target['groups'][category]):
            target['groups'][category].append(deepcopy(row))

    def combine(target, original, categories=GROUPS):
        for key in categories:
            for row in original['groups'][key]:
                append(target, key, row)

    def method_item(ident, **extra):
        method = methods[ident]
        return item(ident, method['name'], url_map('methods/'+ident+'/'), status=method['status'], **extra)

    def equation_item(ident, **extra):
        equation = equations[ident]
        return item(ident, equation['name'], url_map('equations/', lambda lang: ident+'-'+lang),
                    note=note_join(equation.get('note'), extra.pop('note', None)), **extra)

    def reference_item(ident, **extra):
        reference = references[ident]
        return item(ident, reference['title'], url_map('solutions/', lambda lang: 'solution-'+ident+'-'+lang),
                    reference_kind=reference['kind'],
                    note=note_join(reference['kind_label'], reference.get('assumptions'), reference.get('sampling_note'), extra.pop('note', None)), **extra)

    nodes = {}
    for ident, route in executions['executions'].items():
        result = graph('execution', ident, pair('この固定入力で使う手法・式・図・比較条件です。',
                                               'Methods, formulations, figures and comparisons for this fixed input.'))
        entry = ('code-and-data/examples/' if route['kind'] == 'common' else 'validation/')+ident+'/'
        for method in route['methods']:
            append(result, 'methods', method_item(method['id'], role='execution'))
        append(result, 'equations', item('formulation-'+ident, pair('この実行例の式と条件', 'This execution’s formulation and conditions'),
                                        route['formulation']['url'], note=route['formulation']['note'], role=route['formulation']['role']))
        for equation in route['equations']:
            append(result, 'equations', equation_item(equation['id']))
        figure = route['figure']
        figure_urls = route['problem']['hub'] if route['kind'] == 'common' else {lang: figure['url'] for lang in LANGUAGES}
        figure_note = (pair('問題の代表図です。固定入力の格子・時刻・初期値とは異なる場合があります。',
                            'A representative problem figure; its grid, time and initial data may differ from this fixed input.')
                       if route['kind'] == 'common' else pair('この実行例自身の保存済み検証図です。',
                                                                            'The saved validation figure for this execution itself.'))
        append(result, 'figures', item(ident, route['name'], figure_urls, image=figure, note=figure_note,
                                      problem_id=route['problem']['id'] if route['problem'] else None))
        append(result, 'references', item('validation-'+ident, pair('この実行例の参照・検証', 'References and checks for this execution'),
                                         route['references']['url'], note=route['references']['note'], role='execution'))
        for case in route['references']['cases']:
            append(result, 'references', reference_item(case['id'], relation=case['relation'], note=case['note'], context_execution_id=ident))
        append(result, 'code', item(ident, route['name'], url_map(entry), availability='run',
                                   method_ids=[row['id'] for row in route['methods']],
                                   note=(common.get(ident) or supplements[ident]).get('scope') if route['kind'] == 'common' else supplements[ident]['summary']))
        nodes['execution:'+ident] = result

    for ident, problem in problems.items():
        result = graph('problem', ident, pair('この問題に登録されたモデル・手法・図・参照・コードです。条件と出典は問題別ページで確認できます。',
                                             'Models, methods, figures, references and code registered to this problem; its page records conditions and provenance.'))
        for method in problem['methods']:
            append(result, 'methods', method_item(method['id'], role=method['role'], note=problem['method_note'], context_problem_id=ident))
        for equation in problem['equations']:
            append(result, 'equations', equation_item(equation['id'], note=problem.get('equation_note'), context_problem_id=ident))
        append(result, 'figures', item(ident, problem['name'], problem['hub'], image=problem['image'],
                                      note=pair('テスト問題の代表図。条件と出典は問題別ページで確認できます。',
                                                'Representative test-problem figure; the problem page records conditions and provenance.')))
        append(result, 'references', item('problem-'+ident, pair('この問題の参照・比較条件', 'References and comparison conditions for this problem'),
                                         url_map('problems/'+ident+'/', lambda lang: 'references-'+lang), note=problem['reference_note']))
        for edge in bindings[ident]['references']:
            append(result, 'references', reference_item(edge['id'], relation=edge['relation'], note=edge['note'], context_problem_id=ident))
        for execution in problem['executions']:
            combine(result, nodes['execution:'+execution['id']], ('code',))
        if problem.get('code_checks'):
            append(result, 'code', item('problem-'+ident, pair('この問題のコード・検証状況', 'Code and validation status for this problem'),
                                       url_map('problems/'+ident+'/', lambda lang: 'code-'+lang), availability='source',
                                       note=pair('対応する公開検査と配布版の条件を確認できます。',
                                                 'Inspect the corresponding public checks and distribution conditions.')))
        nodes['problem:'+ident] = result

    for ident, method in methods.items():
        result = graph('method', ident, pair('この手法に明示的に対応する資料です。問題ごとの条件と実行範囲を確認できます。',
                                            'Explicitly associated resources for this method, with problem-specific conditions and execution scope.'))
        append(result, 'methods', method_item(ident))
        navigation = method['problem_navigation']
        for equation in navigation['equations']:
            append(result, 'equations', equation_item(equation['id']))
        for problem in navigation['problems']:
            append(result, 'figures', item(problem['id'], problem['name'], problem['hub'], image=problem['image'],
                                          role=problem['role'], note=problem['method_note']))
            for execution in problem['executions']:
                if ident not in execution['method_ids']:
                    raise ValueError('Search cannot borrow a different method’s execution')
                combine(result, nodes['execution:'+execution['id']], ('code', 'references'))
        # The method page also carries independent editions (AD/adjoint/inverse,
        # FDTD, etc.) which are intentionally outside the common case registry.
        if method.get('reading') or method.get('references'):
            append(result, 'references', item('method-'+ident, pair('この手法の比較・参照資料', 'Comparison and reference material for this method'),
                                             url_map('methods/'+ident+'/', lambda lang: 'method-references-'+lang)))
        if method['status'] == 'educational-example' and (method.get('code_urls') or method.get('code_download')):
            append(result, 'code', item('method-'+ident, pair('この手法のコード・検証', 'Code and validation for this method'),
                                       url_map('methods/'+ident+'/', lambda lang: 'method-execution-'+lang), availability='source', method_ids=[ident],
                                       note=pair('手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。',
                                                 'Method-specific editions and related sources; fixed-input runs are listed separately.')))
        nodes['method:'+ident] = result

    entities = []
    for kind, records in [('equation', equations), ('reference', references)]:
        for ident, record in records.items():
            result = graph(kind, ident, record['note'] if kind == 'equation' else record['assumptions'])
            self_item = equation_item(ident) if kind == 'equation' else reference_item(ident)
            append(result, 'equations' if kind == 'equation' else 'references', self_item)
            # Reverse relations come from the reviewed problem binding table.
            for problem_id, binding in bindings.items():
                edge = (next((edge for edge in binding['references'] if edge['id'] == ident), None)
                        if kind == 'reference' else None)
                if (kind == 'equation' and ident not in binding['equation_ids']) or (kind == 'reference' and edge is None):
                    continue
                problem_graph = nodes['problem:'+problem_id]
                for category in GROUPS:
                    if category == ('equations' if kind == 'equation' else 'references'):
                        continue
                    for original in problem_graph['groups'][category]:
                        row = deepcopy(original)
                        row['id'] = problem_id+':'+row['id']
                        row['note'] = note_join(binding.get('equation_note') if kind == 'equation' else edge['note'], row.get('note'))
                        if edge:
                            row['relation'] = edge['relation']
                        elif category == 'code':
                            run_id = original['id']
                            direct = executions['executions'].get(run_id)
                            is_direct = direct and any(eq['id'] == ident for eq in direct['equations'])
                            row['relation'] = 'same-problem' if is_direct else 'related-model'
                            if not is_direct:
                                row['name'] = {lang: ('関連する検証：' if lang == 'ja' else 'Related validation: ')+row['name'][lang] for lang in LANGUAGES}
                        append(result, category, row)
            nodes[kind+':'+ident] = result
            title = record['name'] if kind == 'equation' else record['title']
            formula = record['formula']
            formula = ' '.join(formula) if isinstance(formula, list) else formula
            own_text = {lang: ' '.join([title[lang], formula, result['note'][lang],
                                      record.get('sampling_note', {}).get(lang, '')]) for lang in LANGUAGES}
            entities.append({'id': kind+'-'+ident, 'kind': kind, 'title': title,
                             'headings': {lang: [] for lang in LANGUAGES},
                             'keywords': [ident, *title.values(),
                                          *(['方程式', 'モデル', 'equation', 'model'] if kind == 'equation' else
                                            ['厳密解・参照解', '参照解', 'reference solution', *record['kind_label'].values()])],
                             'text': own_text, 'snippet': result['note'], 'routes': self_item['url'],
                             'origin': 'reviewed-search-connections', 'search_navigation': result})

    # Chapters connect only through explicitly registered reading assignments.
    chapters = {}

    def chapter_for(url):
        match = re.fullmatch(r'/numerical-methods-atlas/(?:ja|en)/read/([a-z0-9.-]+)/', urlsplit(url).path)
        return match[1] if match else None

    def chapter_add(chapter, original, categories=GROUPS):
        if not chapter:
            return
        result = chapters.setdefault(chapter, graph('chapter', chapter, pair('この章に登録された手法・問題・実行例の関連資料です。',
                                                                             'Resources explicitly registered to the methods, problems and executions of this chapter.')))
        combine(result, original, categories)

    for ident, method in methods.items():
        for chapter in {chapter_for(url) for url in method.get('reading', {}).values()}:
            chapter_add(chapter, nodes['method:'+ident], ('methods', 'code'))
    for chapter in detailed:
        for ident in chapter.get('methods', []):
            if ident not in methods:
                raise ValueError('Unknown explicit chapter method: '+ident)
            chapter_add(chapter['id'], nodes['method:'+ident], ('methods', 'code'))
    for ident, problem in problems.items():
        for chapter in {chapter_for(url) for url in problem.get('reading', {}).values()}:
            chapter_add(chapter, nodes['problem:'+ident])
    for ident, equation in equations.items():
        chapter_add(equation['chapter'], nodes['equation:'+ident], ('equations',))
    for ident, reference in references.items():
        for chapter in {chapter_for(url) for url in reference['reading'].values()}:
            chapter_add(chapter, nodes['reference:'+ident], ('references',))
    for ident, case in {**common, **supplements}.items():
        for chapter in {chapter_for(url) for url in case.get('reading', {}).values()}:
            chapter_add(chapter, nodes['execution:'+ident])
    nodes.update({'chapter:'+ident: value for ident, value in chapters.items()})

    # Purpose results never inherit an unrestricted method graph. Every group
    # is assembled from the allowed, method-specific fixed-input contexts.
    method_goals = {}
    for goal in goals:
        for candidate in [*[methods[ident] for ident in goal['methods']], *goal.get('resources', [])]:
            ident = candidate['id']
            result = graph('purpose', goal['id']+':'+ident, goal['scope'])
            if ident in methods:
                append(result, 'methods', method_item(ident))
            else:
                reading = candidate.get('reading', {})
                urls = {lang: ORIGIN+reading.get(lang, reading.get('en')) if reading.get(lang, reading.get('en', '')).startswith('/') else reading.get(lang, reading.get('en')) for lang in LANGUAGES}
                append(result, 'equations', item(ident, candidate['name'], urls, role='model'))
            allowed = set(goal['examples']) | set(goal.get('supplemental_examples', []))
            if isinstance(candidate.get('supplemental_examples'), list):
                allowed = set(goal['examples']) | (set(goal.get('supplemental_examples', [])) & set(candidate['supplemental_examples']))
            if candidate.get('resource_type') == 'model':
                allowed &= {row['id'] for row in candidate.get('execution_examples', [])} | set(candidate.get('supplemental_examples', []))
            if goal.get('availability') == 'reading-only':
                allowed.clear()
            for case_id in sorted(allowed):
                route = executions['executions'][case_id]
                if ident in methods and ident not in {method['id'] for method in route['methods']}:
                    continue
                combine(result, nodes['execution:'+case_id])
            result['allowed_execution_ids'] = [row['id'] for row in result['groups']['code']]
            result['restricted'] = goal.get('availability') == 'reading-only'
            method_goals.setdefault(ident, {})[goal['id']] = result

    return {'schema_version': 1, 'nodes': nodes, 'method_goals': method_goals,
            'entities': entities, 'source_sha256': dict(sorted(sources.items()))}
