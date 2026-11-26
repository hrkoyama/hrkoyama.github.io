"""Lightweight renderer fixture; uses saved metadata, never a scientific runner."""
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from atlas_reading_presentation import original_reading_document


def check_builder(module, source):
    source = Path(source)
    config = json.loads((source/module.CATALOG).read_text())
    chapter = config['chapter'] if 'chapter' in config else 'mhd'
    prefix = 'numerical-methods-atlas/'
    metadata = json.loads((source/prefix/'en/read'/chapter/'supplements.json').read_text())
    # These saved case records exercise presentation only. The production
    # loader and its scientific validation are unchanged and tested separately.
    cases = copy.deepcopy(metadata['supplements'])
    evidence = dict(metadata['source_sha256'])
    evidence.pop(module.CATALOG)
    evidence.pop('catalog/atlas-depth-expansion.json')
    for index, case in enumerate(cases):
        case['source_sha256'] = evidence if index == 0 else {}
    assert [case['id'] for case in cases] == config['supplemental_examples']
    names = [module.CATALOG, 'catalog/atlas-depth-expansion.json']
    names += [prefix+'content.'+language+'.json' for language in ['ja', 'en']]
    names += [prefix+'content.json']
    for language in ['ja', 'en']:
        directory = prefix+language+'/read/'+chapter+'/'
        names += [directory+'index.html', directory+'supplements.json']
        if (source/directory/'supplements.md').is_file():
            names.append(directory+'supplements.md')
    with tempfile.TemporaryDirectory(prefix='reading-overlay-presentation-') as temporary:
        root = Path(temporary)
        for name in names:
            path = root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((source/name).read_bytes())
        original = {name: (root/name).read_bytes() for name in names}
        def loader(actual_root, identifiers):
            assert Path(actual_root) == root
            assert identifiers == config['supplemental_examples']
            return copy.deepcopy(cases)
        def unchanged(expected):
            assert {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()} == set(expected)
            for name, value in expected.items():
                actual = (root/name).read_bytes()
                if name.endswith('.json') and not name.startswith('catalog/'):
                    # The existing builder writes pretty JSON; the final
                    # pipeline later compacts it. Keep that I/O behavior and
                    # compare every typed value here, with no ignored fields.
                    assert (json.dumps(json.loads(actual), sort_keys=True, allow_nan=False) ==
                            json.dumps(json.loads(value), sort_keys=True, allow_nan=False)), 'Renderer changed JSON typed values: '+name
                else:
                    assert actual == value, 'Renderer changed saved bytes: '+name
        with patch.object(module, 'load_supplemental_examples', side_effect=loader):
            # Reapply twice: HTML (including both TOCs) and Markdown are exact;
            # all JSON values are exact across the original formatting stage.
            for _ in range(2):
                module.build(root)
                unchanged(original)
            for language in ['ja', 'en']:
                name = prefix+language+'/read/'+chapter+'/index.html'
                current = original[name].decode()
                assert current.count(module.TOC_START) == 2
                assert current.count(module.TOC_END) == 2
                assert current.count(module.START) == 1
                # Both the moved title/lead and the retained article are still
                # subject to the unchanged historical SHA and marker checks.
                for mutated in [current.replace('</h1>', ' changed</h1>', 1),
                                current.replace('</article>', '<p>Unreviewed scientific body.</p></article>', 1),
                                current.replace('</article>', module.START+'</article>', 1)]:
                    (root/name).write_text(mutated)
                    try:
                        module.build(root)
                    except (AssertionError, ValueError):
                        pass
                    else:
                        raise AssertionError('Historical title/body/overlay tampering was accepted')
                    # A rejection may format identical content JSON, but it
                    # must change no JSON value or other existing byte.
                    unchanged({**original, name: mutated.encode()})
                    (root/name).write_bytes(original[name])
            # Old unconverted inputs retain that layout; the adapter must not
            # opt them in or change their original article or downloads.
            legacy = dict(original)
            for language in ['ja', 'en']:
                name = prefix+language+'/read/'+chapter+'/index.html'
                document, active = original_reading_document(original[name].decode())
                assert active
                legacy[name] = document.encode()
                (root/name).write_bytes(legacy[name])
            for _ in range(2):
                module.build(root)
                unchanged(legacy)
    return {'chapter': chapter, 'opening_first_runs': 2, 'legacy_runs': 2,
            'tampering_rejected': 6, 'HTML_layout_and_Markdown_byte_noop': True,
            'JSON_values_unchanged': True, 'final_JSON_bytes_require_pipeline_artifact': True}
