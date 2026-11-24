"""Shared, stdlib-only contract for the English translation and frozen science."""
import ast
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'catalog/atlas-foundations-course.en.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(root=ROOT):
    d = json.loads((root/SOURCE).read_text())
    original = root/d['translation']['source'].lstrip('/')
    assert sha(original) == d['translation']['source_sha256'], 'Japanese source changed; review the translation'
    ja = json.loads(original.read_text())
    assert d['language'] == 'en' and len(d['chapters']) == 19
    assert [p['id'] for p in d['parts']] == [p['id'] for p in ja['parts']]
    for a,b in zip(ja['chapters'], d['chapters']):
        for key in ['id','n','part','readings']:
            assert a[key] == b[key], (a['id'],key)
        assert a['figure']['id'] == b['figure']['id']
        assert a['experiment']['data'] == b['experiment']['data']
        assert len(a['sections']) == len(b['sections'])
        for key in ['lead','goals','questions','pitfalls','summary']:
            assert len(a[key]) == len(b[key]), (a['id'],key)
        assert len(a['worked']['paragraphs']) == len(b['worked']['paragraphs'])
        for x,y in zip(a['sections'],b['sections']):
            assert len(x['paragraphs']) == len(y['paragraphs'])
            assert [z['tex'] for z in x['equations']] == [z['tex'] for z in y['equations']]
        if a['n'] < 19:
            assert ast.dump(ast.parse(a['worked']['code'])) == ast.dump(ast.parse(b['worked']['code']))
        else:
            commands = lambda c:[x for x in c.splitlines() if not x.startswith('#')]
            assert commands(a['worked']['code']) == commands(b['worked']['code'])
    assert not re.search('[ぁ-んァ-ン一-龯]', json.dumps(d,ensure_ascii=False)), 'Untranslated text'
    assert sum(len(c['questions']) for c in d['chapters']) == 38
    assert sum(len(s['equations']) for c in d['chapters'] for s in c['sections']) == 36
    return d

def fragments(d):
    result=[d['title'],d['subtitle'],*d['preface'],*d['lab_guide'],d['audience'],d['rights'],d['execution_scope']]
    for term,meaning in d['glossary']:result += [term,meaning]
    for r in d['references']:result += [r['title'],r['scope'],r['url']]
    for r in d['readings'].values():result += [r['title'],r['url']]
    for c in d['chapters']:
        result += [c['title'],*c['lead'],*c['goals'],*c['worked']['paragraphs'],c['worked']['result'],c['figure']['caption'],c['experiment']['instructions'],*c['pitfalls'],*c['summary']]
        for s in c['sections']:result += [s['title'],*s['paragraphs']]
        for q in c['questions']:result += [q['question'],q['answer']]
        result += [s.strip() for s in c['worked']['code'].splitlines() if s.strip()]
    return result

def verify_frozen(root=ROOT):
    d=load(root)
    edition=root/d['base'].lstrip('/')/d['edition']
    receipt=json.loads((edition/'book-verification.json').read_text())
    assert receipt['passed'] and receipt['source_sha256']==sha(root/SOURCE)
    for file,digest in receipt['assets'].items():assert sha(root/file)==digest,file
    assert receipt['chapters']==19 and receipt['questions_and_answers']==38
    return d,receipt
