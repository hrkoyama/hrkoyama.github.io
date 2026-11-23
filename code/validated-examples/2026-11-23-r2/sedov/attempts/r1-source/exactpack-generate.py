"""Generate an independent pinned ExactPack comparison; no PDE solver import.

Supply the six unmodified official files listed below at the pinned commit.
This deliberately calls the documented-by-source _run method to choose npts;
it does not modify or transplant the external Sedov implementation.
"""
import argparse
import hashlib
import importlib
import json
import platform
import sys
from pathlib import Path
import numpy as np
import scipy

COMMIT = '9bacc477eb791e959c9621e771fc7a725db755fa'
EXPECTED = {
    'LICENSE.txt': '763767e730623814502f95054919a019f17f5257e0cd8d60aede203d9736dd40',
    'exactpack/__init__.py': 'fac5c9e93253890cff33124da6e7ea5259f5bc171ce45574d43a171fc852d7ff',
    'exactpack/base.py': 'ce8e37ee0ed97dedca174a2ac0d8fa01b8b416bc3b441afab4e3bea9fe4f922e',
    'exactpack/solvers/__init__.py': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'exactpack/solvers/sedov/__init__.py': '322616b5740f79d784b74d9f0f6d7ba514afa96cdab7808f4a322ff0bf3bc340',
    'exactpack/solvers/sedov/sedov.py': 'c2c91eb7b8674e6ad383356f0a3b7f29ff00c667c590e95b508f64e91eeafd00',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generate(upstream, output):
    upstream, output = Path(upstream).resolve(), Path(output).resolve()
    hashes = {name: digest(upstream/name) for name in EXPECTED}
    if hashes != EXPECTED:
        raise ValueError('Reference sources differ from the pinned upstream bytes')
    output.mkdir(parents=True, exist_ok=True)
    if (output/'exactpack-snapshot.json').exists() or (output/'exactpack-receipt.json').exists():
        raise ValueError('Refusing to overwrite a saved reference execution')
    sys.path.insert(0, str(upstream))
    module = importlib.import_module('exactpack.solvers.sedov.sedov')
    if Path(module.__file__).resolve() != upstream/'exactpack/solvers/sedov/sedov.py':
        raise ValueError('Unexpected ExactPack module import')
    import exactpack
    import reference_sedov as reference
    contract = json.loads((Path(__file__).parent/'reference-contract.json').read_text())
    time = contract['time']
    solver = module.Sedov(geometry=3, gamma=5./3., rho0=1., omega=0., eblast=1.)
    beta = solver.alpha**(-.2)
    shock = beta*time**.4
    xi = np.array(contract['exactpack_probes_xi'])
    radii = xi*shock
    own = np.column_stack(reference.point_state(radii, time))
    cases = []
    for npts in contract['exactpack_npts']:
        external = solver._run(radii, time, npts=npts, vtol=1.e-10)
        values = np.column_stack([external[key] for key in ['density', 'velocity', 'pressure']])
        error = float(np.max(np.abs(values-own)/np.maximum(1., np.abs(values))))
        cases.append({'npts': npts, 'vtol': 1.e-10, 'time': time,
                      'xi': xi.tolist(), 'radius': radii.tolist(),
                      'density': values[:,0].tolist(), 'radial_velocity': values[:,1].tolist(),
                      'pressure': values[:,2].tolist(), 'local_scaled_max_difference': error})
    metadata = reference.reference_metadata()
    checks = {
        'beta_resolution_relative': metadata['beta_resolution_relative_difference'] <= contract['criteria']['beta_resolution_relative'],
        'swept_mass_relative': metadata['swept_mass_relative_error'] <= contract['criteria']['swept_mass_relative'],
        'exactpack_beta_relative': abs(metadata['beta']/beta-1.) <= contract['criteria']['exactpack_beta_relative'],
        'exactpack_point_scaled_max': max(c['local_scaled_max_difference'] for c in cases) <= contract['criteria']['exactpack_point_scaled_max'],
    }
    snapshot = {'schema_version':1, 'reference':'LANL ExactPack selected Sedov evaluator',
                'commit':COMMIT, 'parameters':{'gamma':5./3.,'geometry':3,'rho0':1.,'eblast':1.,'omega':0.},
                'time':time, 'shock_radius':float(shock), 'shock_beta':float(beta),
                'upstream_alpha_energy_constant':float(solver.alpha), 'point_cases':cases,
                'scope':'Semi-analytic evaluator cross-check away from shock and center; no independent PDE engine or full ExactPack suite.'}
    target=output/'exactpack-snapshot.json'
    target.write_text(json.dumps(snapshot,indent=2,allow_nan=False)+'\n')
    receipt={'schema_version':1,'passed':all(checks.values()),'checks':checks,
             'criteria':contract['criteria'],'reference_commit':COMMIT,'source_files_sha256':hashes,
             'snapshot_sha256':digest(target),'reference_generator_sha256':digest(Path(__file__)),
             'local_reference_sha256':digest(Path(reference.__file__)),
             'reference_contract_sha256':digest(Path(__file__).parent/'reference-contract.json'),
             'local_reference_metadata':metadata,
             'errors':{'exactpack_beta_relative':abs(metadata['beta']/beta-1.),
                       'exactpack_point_scaled_max':max(c['local_scaled_max_difference'] for c in cases)},
             'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'exactpack':exactpack.__version__},
             'execution':'Unmodified hash-checked official selected Sedov module and package/base dependencies in isolated source directory; original Atlas FV solver is never imported.',
             'command':'python exactpack-generate.py --upstream /path/to/pinned-ExactPack --output /path/to/new-reference-output',
             'limitations':'Upstream double-precision Sedov implementation warns that central density/internal energy may be inaccurate. Probes exclude xi<.15 and the shock. Reference npts refinement is retained; no independent PDE execution or full library tests.'}
    (output/'exactpack-receipt.json').write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':receipt['passed'],'errors':receipt['errors'],'checks':checks}))
    if not receipt['passed']:
        raise ArithmeticError('Preregistered independent reference criteria did not pass')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    generate(args.upstream,args.output)
