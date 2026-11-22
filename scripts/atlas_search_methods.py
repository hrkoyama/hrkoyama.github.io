"""Small, shared public method records for the two search entry points."""
import json
import hashlib
import re


def search_methods(root, navigation=None):
    if navigation is None:
        from atlas_search_routes import load_search_routes
        navigation = load_search_routes(root)
    methods = json.loads((root / 'numerical-methods-atlas/methods/index.json').read_text())['methods']
    fields = ('id', 'name', 'aliases', 'group', 'summary', 'status', 'url', 'reading',
              'reading_label', 'code_urls', 'test_urls', 'run_commands',
              'code_mapping_scope', 'execution_examples')
    records = [{key: method[key] for key in fields if key in method} for method in methods]
    # Prefer the individual, published input/run/check page over a long guide.
    for record in records:
        record['search_navigation'] = navigation['nodes']['method:' + record['id']]
        record['search_navigation_by_goal'] = navigation['method_goals'].get(record['id'], {})
        record['execution_examples'] = [dict(example) for example in record.get('execution_examples', [])]
        for example in record['execution_examples']:
            path = root / 'numerical-methods-atlas/code-and-data/examples' / example['id'] / 'index.json'
            if path.is_file():
                data = json.loads(path.read_text())
                example['name'] = data.get('name', {'ja': example['id'], 'en': example['id']})
                example['guide'] = {lang: '/numerical-methods-atlas/code-and-data/examples/' + example['id'] + '/?lang=' + lang for lang in ['ja', 'en']}
    return records


def version_navigation_imports(root, text):
    """Version callers after the shared navigation module and its CSS are ready."""
    digest = hashlib.sha256((root / 'search/navigation.mjs').read_bytes()).hexdigest()[:12]
    return re.sub(r"(from ['\"](?:[.]/|[.][.]/search/)navigation[.]mjs)(?:\?v=[a-f0-9]+)?(['\"])",
                  lambda match: match[1] + '?v=' + digest + match[2], text)


def version_method_search(root):
    navigation = root / 'search/navigation.mjs'
    navigation_css_hash = hashlib.sha256((root / 'search/navigation.css').read_bytes()).hexdigest()[:12]
    navigation.write_text(re.sub(
        r"new URL\('./navigation[.]css(?:\?v=[a-f0-9]+)?',import.meta.url\)",
        "new URL('./navigation.css?v=" + navigation_css_hash + "',import.meta.url)", navigation.read_text()))
    module = root / 'search/method-search.mjs'
    css_hash = hashlib.sha256((root / 'search/methods.css').read_bytes()).hexdigest()[:12]
    text=re.sub(r"new URL\('./methods[.]css(?:\?v=[a-f0-9]+)?',import.meta.url\)", "new URL('./methods.css?v=" + css_hash + "',import.meta.url)", module.read_text())
    goal_hash=hashlib.sha256((root/'search/goals-data.mjs').read_bytes()).hexdigest()[:12]
    text=re.sub(r"from './goals-data[.]mjs(?:\?v=[a-f0-9]+)?'", "from './goals-data.mjs?v="+goal_hash+"'",text)
    text=version_navigation_imports(root, text)
    module.write_text(text)
    return hashlib.sha256(module.read_bytes()).hexdigest()[:12]
