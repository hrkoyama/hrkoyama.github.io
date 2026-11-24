"""Read only qualified portable cache: no SciPy reference generation in main."""
import hashlib
import json
from pathlib import Path
import numpy as np

DEPENDENCIES = ['inputs.json', 'acceptance.json', 'tableau.py', 'references/qualify.py',
                'references/reference_models.py', 'references/boundary_reference.py', 'references/coefficient_exact.py']


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Cache:
    def __init__(self, source):
        self.source = Path(source)
        self.directory = self.source/'references/cache'
        q = json.loads((self.directory/'qualification.json').read_text())
        if q.get('passed') is not True or len(q['checks']) != 52 or not all(type(v) is bool and v for v in q['checks'].values()):
            raise ValueError('Exact52 qualified reference checks required')
        if q['input_sha256'] != digest(self.source/'inputs.json') or q['acceptance_sha256'] != digest(self.source/'acceptance.json'):
            raise ValueError('Stale reference input/acceptance')
        if set(q['source_sha256']) != set(DEPENDENCIES) or any(q['source_sha256'][name] != digest(self.source/name) for name in DEPENDENCIES):
            raise ValueError('Stale reference generator/source')
        self.contract = json.loads((self.source/'pre-run-contract.json').read_text())

    def load(self, filename):
        relative = 'references/cache/'+filename
        path = self.directory/filename
        if filename != Path(filename).name or relative not in self.contract['files_sha256'] or digest(path) != self.contract['files_sha256'][relative]:
            raise ValueError('Unbound or changed reference cache')
        with np.load(path, allow_pickle=False) as packet:
            out = {name: packet[name].copy() for name in packet.files}
        if any(np.issubdtype(value.dtype, np.number) and not np.isfinite(value).all() for value in out.values()):
            raise ValueError('Nonfinite reference cache')
        return out

    def stiff(self, key):
        out = self.load(key+'-Radau-tight.npz')
        if out['times'][0] != 0 or np.any(np.diff(out['times']) <= 0):
            raise ValueError('Malformed reference time grid')
        return out

    def boundary(self, n):
        return self.load('boundary-'+str(n)+'.npz')
