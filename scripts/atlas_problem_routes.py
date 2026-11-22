"""Resolve reverse model/reference routes from sources, without reading problem hubs."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlsplit

from atlas_execution_discovery import entry_url, load_discovery
from atlas_goal_availability import load_supplemental_examples
from atlas_problem_links import bilingual, problem_url, validate_catalog, validate_public_url

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('ja', 'en')


def invert_problem_routes(catalog, problems, equation_ids, reference_ids):
    """Invert reviewed edges only; names and shared model labels imply no edge."""
    equations = {ident: [] for ident in equation_ids}
    references = {ident: [] for ident in reference_ids}
    rows = catalog['problems']
    identifiers = [row['id'] for row in rows]
    if len(set(identifiers)) != len(identifiers) or set(identifiers) != set(problems):
        raise ValueError('Reverse routes must cover the current problem identities exactly once')
    for row in rows:
        problem = problems[row['id']]
        ids = row.get('equation_ids', [])
        if len(ids) != len(set(ids)) or not set(ids) <= equations.keys():
            raise ValueError('Unknown or repeated reverse equation edge: '+row['id'])
        for ident in ids:
            card = deepcopy(problem)
            if row.get('equation_note'):
                bilingual(row['equation_note'], 'reverse equation note')
                card['note'] = row['equation_note']
            equations[ident].append(card)
        edges = row.get('references', [])
        if len(edges) != len({edge['id'] for edge in edges}):
            raise ValueError('Repeated reverse reference edge: '+row['id'])
        for edge in edges:
            if edge['id'] not in references or edge.get('relation') not in {'same-problem', 'related-model'}:
                raise ValueError('Unknown reverse reference edge: '+row['id'])
            bilingual(edge.get('note'), 'reverse reference note')
            references[edge['id']].append({**deepcopy(problem), 'relation': edge['relation'], 'note': edge['note']})
    return {'equations': equations, 'references': references}


def load_problem_routes(root=ROOT):
    """Use inputs available before equation/solution generation, with no cycle."""
    root = Path(root).resolve()
    sources = {}

    def read(path):
        value = (root/path).read_bytes()
        sources[path] = sha256(value).hexdigest()
        return json.loads(value)

    def public(url):
        return validate_public_url(url, root)

    catalog = read('catalog/atlas-problem-links.json')
    inventory = read('numerical-methods-atlas/test-cases/index.json')
    previews = read('numerical-methods-atlas/gallery/preview-manifest.json')
    equation_ids = [row['id'] for row in read('catalog/atlas-equations.json')['equations']]
    reference_ids = [row['id'] for row in read('numerical-methods-atlas/assets/reference-solutions.json')['cases']]
    method_ids = [row['id'] for row in read('catalog/atlas-methods.json')['methods']]
    problem_ids = [row['id'] for row in inventory['problems']]
    validate_catalog(catalog, problem_ids, equation_ids, reference_ids, method_ids)
    visuals = {row['id']: row for row in previews['items']}
    if len(visuals) != len(previews['items']) or set(visuals) != set(problem_ids):
        raise ValueError('Reverse routes require the current saved problem pictures')

    discovery = load_discovery(root)
    read('catalog/atlas-execution-discovery.json')
    registry = read('numerical-methods-atlas/code-and-data/examples.json')
    receipt_url = public(registry['verification_receipt'])
    receipt = read(urlsplit(receipt_url).path.lstrip('/'))
    if receipt.get('passed') is not True or receipt['registry_sha256'] != sources['numerical-methods-atlas/code-and-data/examples.json']:
        raise ValueError('Reverse execution links require a successful current common receipt')
    passed = {row['id']: row['passed'] for row in receipt['examples']}
    common = {ident: [] for ident in problem_ids}
    for example in discovery['examples']:
        if example['problem_id'] not in common or passed.get(example['id']) is not True:
            raise ValueError('Unverified reverse common execution: '+example['id'])
        record = example['execution']
        common[example['problem_id']].append({
            'id': record['id'], 'kind': 'common', 'name': record['name'], 'scope': record['scope'],
            'guide': {lang: public(entry_url(record['id'], lang)) for lang in LANGUAGES},
            'input': public(record['inputs']['url']), 'download': public(record['release']['download']),
            'verification': receipt_url})
    expansion = read('catalog/atlas-depth-expansion.json')
    supplemental_ids = list(dict.fromkeys(extra['id'] for problem in inventory['problems'] for extra in problem.get('supplemental_examples', [])))
    supplements = {row['id']: row for row in load_supplemental_examples(root, supplemental_ids)}
    for case in supplements.values():
        sources.update(case['source_sha256'])

    cards = {}
    for problem in inventory['problems']:
        ident = problem['id']
        visual = visuals[ident]
        image_url = public(visual['image'])
        image = root/urlsplit(image_url).path.lstrip('/')
        if sha256(image.read_bytes()).hexdigest() != visual['image_sha256'] or min(visual['width'], visual['height']) <= 0:
            raise ValueError('Stale reverse-route picture: '+ident)
        bilingual(visual['caption'], 'picture caption')
        executions = list(common[ident])
        for extra in problem.get('supplemental_examples', []):
            case = supplements[extra['id']]
            if expansion['case_problem_ids'].get(case['id']) != ident or case['url'] != extra['url'] or case['title'] != extra['name']:
                raise ValueError('Unrelated reverse supplemental execution: '+case['id'])
            base = case['download'].rsplit('/', 1)[0]+'/'
            executions.append({
                'id': case['id'], 'kind': 'supplement', 'name': case['title'], 'scope': case['summary'],
                'guide': {lang: public(case['url']+'?lang='+lang) for lang in LANGUAGES},
                'input': public(base+'inputs.json'), 'download': public(case['download']),
                'verification': public(case['verification'])})
        cards[ident] = {
            'id': ident, 'name': problem['name'],
            'image': {'url': image_url, 'sha256': visual['image_sha256'], 'width': visual['width'], 'height': visual['height'],
                      'caption': visual['caption'], 'source_kind': visual['source_kind']},
            'hub': {lang: problem_url(ident, lang) for lang in LANGUAGES},
            'code': {lang: problem_url(ident, lang)+'#code-'+lang for lang in LANGUAGES},
            'executions': executions}
    return {'schema_version': 1, 'problems': cards, **invert_problem_routes(catalog, cards, equation_ids, reference_ids),
            'source_sha256': dict(sorted(sources.items()))}
