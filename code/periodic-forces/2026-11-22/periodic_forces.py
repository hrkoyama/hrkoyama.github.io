"""Auditable library-backed periodic nuclear forces for a fixed two-He model.

PySCF supplies KRKS, FFTDF, Libxc, analytic pseudopotential and Ewald gradients,
including the overlap (Pulay) contribution of atom-centred Gaussian orbitals.
This module supplies model restrictions, diagnostics and a BO-force interface;
it is not a separately implemented DFT engine.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import itertools
import platform
import time
import warnings
import numpy as np
import scipy
from scipy.linalg import eigh
import pyscf
from pyscf import lib
from pyscf.dft import libxc
from pyscf.pbc import gto, dft
from pyscf.pbc.dft import gen_grid


def fractional_points(n):
    if type(n) is not int or not 1 <= n <= 4:
        raise ValueError('Sampling count must be an integer between 1 and 4')
    coordinates=[i/n if i<=n//2 else (i-n)/n for i in range(n)]
    return np.array(list(itertools.product(coordinates,repeat=3)),dtype=float)


def validate_model(config, positions_bohr=None):
    c=config['cell']
    if c['element']!='He' or c['charge']!=0 or c['spin']!=0:
        raise ValueError('Only the registered neutral two-He closed-shell model is supported')
    if c['pseudopotential']!=[[2],.2,2,[-9.1120234,1.69836797],0]:
        raise ValueError('The audited local He-GTH-PADE-q2 coefficients are required')
    if config['xc']['pyscf']!='LDA_X,LDA_C_VWN' or config['xc']['libxc']!=['lda_x','lda_c_vwn']:
        raise ValueError('Only Dirac exchange plus VWN5 correlation is supported')
    lattice=np.asarray(c['lattice_bohr'],dtype=float)
    if lattice.shape!=(3,3) or not np.array_equal(lattice,np.eye(3)*5):
        raise ValueError('The registered cubic 5-bohr lattice is required')
    positions=np.asarray(c['positions_bohr'] if positions_bohr is None else positions_bohr,dtype=float)
    if positions.shape!=(2,3) or not np.isfinite(positions).all():
        raise ValueError('Two finite Cartesian positions in bohr are required')
    displacement=positions[1]-positions[0];displacement-=np.rint(displacement/5)*5
    if np.linalg.norm(displacement)<.5:
        raise ValueError('Coincident or near-coincident nuclei are outside the registered model')
    return positions.copy()


def build_cell(config,spec,positions_bohr=None):
    positions=validate_model(config,positions_bohr)
    if spec['basis'] not in config['basis_sequence']:
        raise ValueError('Unregistered Gaussian orbital basis')
    mesh=spec['fft_n']
    if type(mesh) is not int or mesh<9 or mesh%2!=1:
        raise ValueError('FFT mesh must be an odd integer >=9')
    cell=gto.Cell()
    cell.atom=[('He',p) for p in positions]
    cell.a=config['cell']['lattice_bohr'];cell.unit='Bohr'
    cell.basis=spec['basis'];cell.pseudo={'He':config['cell']['pseudopotential']}
    cell.charge=0;cell.spin=0;cell.mesh=[mesh]*3
    cell.precision=config['integral_precision'];cell.verbose=0;cell.max_memory=2000
    cell.build()
    if cell.nelectron!=4:raise ValueError('Exactly four valence electrons are required')
    return cell


def _norm(a):return float(np.sqrt(np.sum(np.abs(a)**2)))
def _mm(a,b):return np.einsum('ij,jk->ik',a,b,optimize=False)


def solve(config,spec,positions_bohr=None,*,with_forces=True,density_guess=None,return_density=False):
    """Solve a fresh SCF; optionally use a density only as an initial guess.

    Raw diagnostics can represent a failed SCF for rejection tests. The BO-facing
    energy_and_forces function refuses to pass an unconverged state to nuclei.
    Forces are Cartesian minus-energy derivatives in Eh/bohr, including ions.
    """
    for key in ['energy_tolerance','gradient_tolerance']:
        if not np.isfinite(spec[key]) or spec[key]<=0:raise ValueError('SCF tolerances must be finite and positive')
    if type(spec['max_cycles']) is not int or spec['max_cycles']<1:raise ValueError('At least one SCF cycle is required')
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='OpenMP is not available.*')
        lib.num_threads(1)
    cell=build_cell(config,spec,positions_bohr)
    fractional=np.asarray(config['kpoint_meshes'][str(spec['k_n'])],dtype=float)
    expected=fractional_points(spec['k_n'])
    if fractional.shape!=expected.shape or not np.allclose(sorted(map(tuple,fractional)),sorted(map(tuple,expected)),rtol=0,atol=1e-14):
        raise ValueError('Explicit complete equal-weight Gamma-containing mesh is required')
    kpts=cell.get_abs_kpts(fractional)
    mf=dft.KRKS(cell,kpts);mf.xc=config['xc']['pyscf'];mf.grids=gen_grid.UniformGrids(cell)
    mf.conv_tol=spec['energy_tolerance'];mf.conv_tol_grad=spec['gradient_tolerance'];mf.max_cycle=spec['max_cycles'];mf.chkfile=None
    trace=[]
    def callback(env):
        energy=float(env['e_tot'])
        trace.append(dict(cycle=int(env['cycle']),energy_total=energy,delta_energy=None if not trace else abs(energy-trace[-1]['energy_total']),density_change=float(env.get('norm_ddm',0.)),gradient_norm=float(env.get('norm_gorb',0.))))
    mf.callback=callback
    start=time.perf_counter();energy=float(mf.kernel(dm0=density_guess));scf_seconds=time.perf_counter()-start
    density=mf.make_rdm1();overlap=mf.get_ovlp();fock=mf.get_hcore()+mf.get_veff(cell,density)
    commutator=[];orbital=[];electron=[];orthogonality=[];condition=[];overlap_min=[]
    for s,f,p,c,eps in zip(overlap,fock,density,mf.mo_coeff,mf.mo_energy):
        w,u=eigh(s)
        if w[0]<=config['overlap_eigenvalue_floor']:raise ValueError('Nearly linearly dependent Gaussian basis')
        x=_mm(u/np.sqrt(w),u.conj().T)
        commutator.append(_norm(_mm(_mm(x,_mm(_mm(f,p),s)-_mm(_mm(s,p),f)),x)))
        orbital.append(_norm(_mm(x,_mm(f,c)-_mm(_mm(s,c),np.diag(eps)))))
        electron.append(float(np.trace(_mm(p,s)).real))
        orthogonality.append(float(np.abs(_mm(_mm(c.conj().T,s),c)-np.eye(c.shape[1])).max()))
        condition.append(float(w[-1]/w[0]));overlap_min.append(float(w[0]))
    occupied=[float(e[o>0].max()) for e,o in zip(mf.mo_energy,mf.mo_occ)]
    unoccupied=[float(e[o==0].min()) for e,o in zip(mf.mo_energy,mf.mo_occ) if (o==0).any()]
    if len(unoccupied)!=len(kpts):raise ValueError('Every k point needs a sampled conduction state')
    gap=min(unoccupied)-max(occupied)
    gradient_seconds=0.
    if with_forces:
        start=time.perf_counter();forces=-np.asarray(mf.nuc_grad_method().kernel());gradient_seconds=time.perf_counter()-start
        if forces.shape!=(2,3) or not np.isfinite(forces).all():raise FloatingPointError('Non-finite analytic nuclear force')
    else:forces=None
    if not np.isfinite([energy,gap,*commutator,*orbital,*electron,*orthogonality,*condition]).all():
        raise FloatingPointError('Non-finite electronic state diagnostic')
    row=dict(id=spec['id'],sweep=spec['sweep'],k_n=spec['k_n'],kmesh=[spec['k_n']]*3,kpoints_fractional=fractional.tolist(),kpoint_weights=[1/len(kpts)]*len(kpts),basis=spec['basis'],ao_count=cell.nao_nr(),fft_mesh=list(cell.mesh),positions_bohr=cell.atom_coords().tolist(),energy_per_cell=energy,forces_cartesian=None if forces is None else forces.tolist(),converged=bool(mf.converged),termination='converged' if mf.converged else 'maximum_cycles',iterations=len(trace),scf_commutator_norm=max(commutator),orbital_residual_norm=max(orbital),electron_count=float(np.mean(electron)),electron_count_error=abs(float(np.mean(electron))-4),orthogonality_error=max(orthogonality),sampled_ks_gap=gap,overlap_condition_max=max(condition),overlap_min_eigenvalue=min(overlap_min),trace=trace,scf_options={k:spec[k] for k in ['energy_tolerance','gradient_tolerance','max_cycles']},energy_reconstruction_error=abs(float(mf.energy_tot(dm=density))-energy),net_force_max=None if forces is None else float(np.abs(forces.sum(axis=0)).max()),environment={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'pyscf':pyscf.__version__,'libxc':libxc.__version__},scf_seconds=scf_seconds,gradient_seconds=gradient_seconds)
    return (row,density) if return_density else row


def require_converged(row,maximum_commutator=1e-6):
    if not row['converged'] or not np.isfinite(row['scf_commutator_norm']) or row['scf_commutator_norm']>maximum_commutator:
        raise RuntimeError('Electronic SCF has not converged sufficiently for a BO force step')
    if row['forces_cartesian'] is not None and not np.isfinite(row['forces_cartesian']).all():
        raise FloatingPointError('BO force is non-finite')
    return row


def energy_and_forces(config,spec,positions_bohr,*,density_guess=None):
    """Stateless BOMD callback: Cartesian bohr -> energy(Eh) and forces(Eh/bohr).

    Lattice, basis, k points, electron number and XC are fixed in config/spec.
    Each geometry is independently re-converged. An optional density is only an
    initial guess, never a substitute for SCF. Incomplete SCF raises an error.
    """
    return require_converged(solve(config,spec,positions_bohr,density_guess=density_guess))
