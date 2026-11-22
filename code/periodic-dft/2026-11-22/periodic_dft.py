"""Library-backed PySCF periodic KS-DFT driver for one fixed pedagogical He cell.

PySCF implements integrals, FFT density fitting, Libxc and SCF. This original
workflow records explicit sampling, independent residuals and acceptance data;
it is not a new DFT engine. Independent DFTK references are generated elsewhere.
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
    if type(n) is not int or n<1 or n>8:
        raise ValueError('Sampling count must be an integer between 1 and 8')
    coordinates=[i/n if i<=n//2 else (i-n)/n for i in range(n)]
    return np.array(list(itertools.product(coordinates,repeat=3)),dtype=float)


def build_cell(config,basis,mesh):
    if basis not in config['basis_sequence']:
        raise ValueError('Unregistered basis')
    if type(mesh) is not int or mesh<9 or mesh%2!=1:
        raise ValueError('FFT mesh must be an odd integer >=9')
    cell=gto.Cell()
    c=config['cell']
    cell.atom=[(c['element'],c['position_bohr'])]
    cell.a=c['lattice_bohr'];cell.unit='Bohr'
    cell.basis=basis;cell.pseudo={c['element']:c['pseudopotential']}
    cell.charge=c['charge'];cell.spin=c['spin']
    cell.mesh=[mesh]*3;cell.precision=config['integral_precision']
    cell.verbose=0;cell.max_memory=2000
    cell.build()
    if cell.nelectron!=2 or cell.spin!=0:
        raise ValueError('Only the registered two-electron closed-shell cell is implemented')
    return cell


def _norm(a):return float(np.sqrt(np.sum(np.abs(a)**2)))


def _mm(a,b):
    # Small diagnostic matrices: explicit contractions keep the residual
    # calculation separate from the electronic-structure library's BLAS path.
    return np.einsum('ij,jk->ik',a,b,optimize=False)


def solve(config,spec):
    if config['xc']['pyscf']!='LDA_X,LDA_C_VWN' or config['xc']['libxc']!=['lda_x','lda_c_vwn']:
        raise ValueError('Only the audited Dirac exchange plus VWN5 XC pair is implemented')
    for key in ['energy_tolerance','gradient_tolerance']:
        if not np.isfinite(spec[key]) or spec[key]<=0:
            raise ValueError('SCF tolerances must be finite and positive')
    if type(spec['max_cycles']) is not int or spec['max_cycles']<1:
        raise ValueError('At least one SCF cycle is required')
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='OpenMP is not available.*')
        lib.num_threads(1)
    cell=build_cell(config,spec['basis'],spec['fft_n'])
    fractional=np.asarray(config['kpoint_meshes'][str(spec['k_n'])],dtype=float)
    expected=fractional_points(spec['k_n'])
    if fractional.shape!=expected.shape or not np.allclose(np.array(sorted(map(tuple,fractional))),np.array(sorted(map(tuple,expected))),atol=1e-14,rtol=0):
        raise ValueError('Explicit equal-weight Gamma-centered mesh does not match registered convention')
    kpoints=cell.get_abs_kpts(fractional)
    mf=dft.KRKS(cell,kpoints)
    mf.xc=config['xc']['pyscf']
    mf.grids=gen_grid.UniformGrids(cell)
    mf.conv_tol=spec['energy_tolerance'];mf.conv_tol_grad=spec['gradient_tolerance']
    mf.max_cycle=spec['max_cycles'];mf.chkfile=None
    trace=[]
    def callback(env):
        trace.append(dict(cycle=int(env['cycle']),energy_total=float(env['e_tot']),
                          delta_energy=None if not trace else abs(float(env['e_tot'])-trace[-1]['energy_total']),
                          density_change=float(env.get('norm_ddm',0.)),gradient_norm=float(env.get('norm_gorb',0.))))
    mf.callback=callback
    start=time.perf_counter();energy=float(mf.kernel());elapsed=time.perf_counter()-start
    density=mf.make_rdm1();overlap=mf.get_ovlp();hcore=mf.get_hcore();veff=mf.get_veff(cell,density)
    fock=hcore+veff
    commutator=[];orbital=[];electron=[];orthogonality=[];condition=[];fixed_point=[];overlap_min=[]
    for s,f,p,c,eps in zip(overlap,fock,density,mf.mo_coeff,mf.mo_energy):
        w,u=eigh(s)
        if w[0]<=config['overlap_eigenvalue_floor']:
            raise ValueError('Overlap is nearly linearly dependent')
        x=_mm(u/np.sqrt(w),u.conj().T)
        commutator.append(_norm(_mm(_mm(x,_mm(_mm(f,p),s)-_mm(_mm(s,p),f)),x)))
        orbital.append(_norm(_mm(x,_mm(f,c)-_mm(_mm(s,c),np.diag(eps)))))
        electron.append(float(np.trace(_mm(p,s)).real))
        orthogonality.append(float(np.abs(_mm(_mm(c.conj().T,s),c)-np.eye(c.shape[1])).max()))
        condition.append(float(w[-1]/w[0]));overlap_min.append(float(w[0]))
        _,co=eigh(f,s)
        pout=2*_mm(co[:,:1],co[:,:1].conj().T)
        fixed_point.append(_norm(_mm(_mm(_mm(_mm(x,s),pout-p),s),x)))
    occupied=[float(e[o>0].max()) for e,o in zip(mf.mo_energy,mf.mo_occ)]
    unoccupied=[float(e[o==0].min()) for e,o in zip(mf.mo_energy,mf.mo_occ) if (o==0).any()]
    if len(unoccupied)!=len(kpoints):raise ValueError('Every sampled k point needs a conduction eigenvalue')
    gap=min(unoccupied)-max(occupied)
    if not np.isfinite([energy,gap,*commutator,*orbital,*electron,*orthogonality,*condition,*fixed_point]).all():
        raise FloatingPointError('Non-finite electronic state or diagnostic')
    return dict(id=spec['id'],sweep=spec['sweep'],k_n=spec['k_n'],kmesh=[spec['k_n']]*3,
                kpoints_fractional=fractional.tolist(),weights=[1/len(kpoints)]*len(kpoints),
                basis=spec['basis'],ao_count=cell.nao_nr(),fft_mesh=list(cell.mesh),
                energy_total=energy,energy_per_cell=energy,converged=bool(mf.converged),
                termination='converged' if mf.converged else 'maximum_cycles',iterations=len(trace),
                scf_commutator_norm=max(commutator),orbital_residual_norm=max(orbital),
                fixed_point_density_norm=max(fixed_point),electron_count=float(np.mean(electron)),
                electron_count_error=abs(float(np.mean(electron))-2),orthogonality_error=max(orthogonality),
                sampled_ks_gap=gap,overlap_condition_max=max(condition),overlap_min_eigenvalue=min(overlap_min),trace=trace,
                scf_options={k:spec[k] for k in ['energy_tolerance','gradient_tolerance','max_cycles']},
                energy_reconstruction_error=abs(float(mf.energy_tot(dm=density))-energy),
                environment={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'pyscf':pyscf.__version__,'libxc':libxc.__version__},
                duration_seconds=elapsed)
