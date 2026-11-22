"""Small, shared public method records for the two search entry points."""
import json
import hashlib
import re


def search_methods(root):
    methods = json.loads((root / 'numerical-methods-atlas/methods/index.json').read_text())['methods']
    fields = ('id', 'name', 'aliases', 'group', 'summary', 'status', 'url', 'reading',
              'reading_label', 'code_urls', 'test_urls', 'run_commands',
              'code_mapping_scope', 'execution_examples')
    records = [{key: method[key] for key in fields if key in method} for method in methods]
    # Prefer the individual, published input/run/check page over a long guide.
    for record in records:
        record['execution_examples'] = [dict(example) for example in record.get('execution_examples', [])]
        for example in record['execution_examples']:
            path = root / 'numerical-methods-atlas/code-and-data/examples' / example['id'] / 'index.json'
            if path.is_file():
                data = json.loads(path.read_text())
                example['name'] = data.get('name', {'ja': example['id'], 'en': example['id']})
                example['guide'] = {lang: '/numerical-methods-atlas/code-and-data/examples/' + example['id'] + '/?lang=' + lang for lang in ['ja', 'en']}
    return records


def version_method_search(root):
    module = root / 'search/method-search.mjs'
    css_hash = hashlib.sha256((root / 'search/methods.css').read_bytes()).hexdigest()[:12]
    text=re.sub(r"new URL\('./methods[.]css(?:\?v=[a-f0-9]+)?',import.meta.url\)", "new URL('./methods.css?v=" + css_hash + "',import.meta.url)", module.read_text())
    goal_hash=hashlib.sha256((root/'search/goals-data.mjs').read_bytes()).hexdigest()[:12]
    text=re.sub(r"from './goals-data[.]mjs(?:\?v=[a-f0-9]+)?'", "from './goals-data.mjs?v="+goal_hash+"'",text)
    module.write_text(text)
    return hashlib.sha256(module.read_bytes()).hexdigest()[:12]
