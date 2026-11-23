"""Validate the build contract before starting any generator."""
import json
from pathlib import PurePosixPath
import re
import sys


def commands(root):
    data = json.loads((root/'catalog/site-build-pipeline.json').read_text())
    if data.get('schema_version') != 1 or not isinstance(data.get('stages'), list) or not data['stages']:
        raise ValueError('Invalid site build pipeline')
    seen, result = set(), []
    for stage in data['stages']:
        ident = stage.get('id')
        if not isinstance(ident,str) or not re.fullmatch('[a-z0-9-]+', ident) or ident in seen:
            raise ValueError('Invalid or duplicate build-stage ID')
        dependencies = stage.get('depends_on')
        if not isinstance(dependencies,list) or len(dependencies) != len(set(dependencies)) or not set(dependencies) <= seen:
            raise ValueError('Missing, cyclic or forward build dependency: '+ident)
        script = stage.get('script','')
        path = PurePosixPath(script)
        if path.is_absolute() or '..' in path.parts or not script.startswith('scripts/') or not (root/script).is_file():
            raise ValueError('Invalid build script: '+script)
        runner = stage.get('runner')
        if runner not in ['python','node'] or not isinstance(stage.get('args'),list) or not all(isinstance(x,str) for x in stage['args']):
            raise ValueError('Invalid build command: '+ident)
        for key in ['inputs','outputs','checks']:
            values = stage.get(key, [])
            if not isinstance(values,list) or not all(isinstance(value,str) and value and not PurePosixPath(value).is_absolute() and '..' not in PurePosixPath(value).parts for value in values):
                raise ValueError('Invalid build annotation: '+ident+'/'+key)
            if key=='checks' and not all((root/value).is_file() for value in values):
                raise ValueError('Missing build check: '+ident)
        result.append([sys.executable if runner=='python' else 'node', script, *stage['args']])
        seen.add(ident)
    return result
