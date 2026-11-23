"""Small, shared public method records for the two search entry points."""
import json


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
