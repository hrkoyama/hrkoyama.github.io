"""Independent H2 reference. PySCF integrals/SCF; no educational imports.

Only geometry and explicit basis parameters are shared through the input JSON.
Saved finite-basis RHF values are numerical references, not exact H2 energies.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy
import pyscf
from pyscf import gto,scf,lib


def calculate(path):
    config=json.loads(path.read_text());lib.num_threads(1);rows=[]
    for bond in config['bonds_bohr']:
        for basis in config['basis_definitions']:
            shells=[[0,*[[float(a),float(c)] for a,c in zip(shell['exponents'],shell['coefficients'])]] for shell in basis['shells']]
            mol=gto.M(atom=[('H',(0,0,-bond/2)),('H',(0,0,bond/2))],unit='Bohr',basis={'H':shells},spin=0,charge=0,verbose=0)
            mf=scf.RHF(mol);mf.conv_tol=config['reference']['energy_tolerance'];mf.conv_tol_grad=config['reference']['gradient_tolerance'];mf.max_cycle=config['reference']['max_cycles']
            energy=float(mf.kernel())
            if not mf.converged:raise RuntimeError('Independent PySCF SCF did not converge')
            S=mf.get_ovlp();H=mf.get_hcore();dm=mf.make_rdm1();F=mf.get_fock(dm=dm)
            rows.append(dict(bond_bohr=bond,basis_id=basis['id'],nbf=mol.nao_nr(),energy_total=energy,converged=bool(mf.converged),
                             nuclear_repulsion=float(mol.energy_nuc()),electron_count=float(np.einsum('ij,ji',dm,S)),
                             scf_commutator_ao_norm=float(np.linalg.norm(np.einsum('ij,jk,kl->il',F,dm,S)-np.einsum('ij,jk,kl->il',S,dm,F))),
                             overlap_eigenvalues=np.linalg.eigvalsh(S).tolist(),core_eigenvalues=np.linalg.eigvalsh(H).tolist()))
    return dict(schema_version=1,source='Independent PySCF RHF, libcint analytic integrals and PySCF SCF',
                input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,pyscf=pyscf.__version__),
                scope='Same explicitly supplied finite s-Gaussian spaces and geometries; not a correlated, polarized or complete-basis H2 reference.',cases=rows)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,default=Path('inputs.json'));p.add_argument('--output',type=Path,default=Path('reference-pyscf.json'));a=p.parse_args()
    if a.output.exists():raise SystemExit('Existing reference preserved; choose a new output path')
    a.output.write_text(json.dumps(calculate(a.input),indent=2,allow_nan=False)+'\n')
