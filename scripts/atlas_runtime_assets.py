"""Emit the SPA's variable data and render its explicitly owned runtime template."""
import json
from search_assets import digest, render_templates


def build_atlas_runtime(root):
    descriptions = json.loads((root/'catalog/atlas-purpose.json').read_text())
    values = {
        'atlasIntroDescriptions': {language:row['meta_description'] for language,row in descriptions.items()},
        'atlasDocumentVersions': {language:digest(root/'numerical-methods-atlas'/('content.'+language+'.json'))[:12] for language in ['ja','en']},
    }
    data = root/'numerical-methods-atlas/atlas-runtime-data.mjs'
    data.write_text('// Generated from atlas-purpose.json and published language documents.\n'+''.join(
        'export const '+key+' = '+json.dumps(value,ensure_ascii=False,separators=(',',':'))+';\n' for key,value in values.items()))
    rows, _ = render_templates(root, {'numerical-methods-atlas/app.js':'frontend/atlas/app.js'}, 'scripts/atlas_runtime_assets.py')
    manifest = {'schema_version':1, 'generator':'scripts/atlas_runtime_assets.py', 'modules':rows,
                'data_sources':{name:digest(root/name) for name in ['catalog/atlas-purpose.json','numerical-methods-atlas/content.ja.json','numerical-methods-atlas/content.en.json']},
                'generated_data':{'url':'/numerical-methods-atlas/atlas-runtime-data.mjs','sha256':digest(data)}}
    (root/'numerical-methods-atlas/runtime-asset-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest
