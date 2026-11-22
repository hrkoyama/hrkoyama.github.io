"""Run the fixed periodic He KS-LDA workflow. Exit0 pass,1 unmet,2 error.

The driver uses PySCF, not an independently written electronic-structure engine.
DFTK reference generation is a separate operation and is never imported here.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from periodic_dft import solve

ROOT=Path(__file__).resolve().parent
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()


def run_cases(config):
    results=[]
    for spec in config['cases']:
        row=solve(config,spec);results.append(row)
        print('Completed '+row['id']+': '+format(row['energy_per_cell'],'.12f')+' Eh/cell',file=sys.stderr,flush=True)
    return results


def validate_reference(config,reference):
    """Audit recorded independent evidence rather than trusting saved pass flags."""
    if config['xc']['pyscf']!='LDA_X,LDA_C_VWN' or config['xc']['libxc']!=['lda_x','lda_c_vwn']:
        raise ValueError('Only the audited Dirac exchange plus VWN5 XC pair is implemented')
    if reference['cell']!=config['cell'] or reference['xc']!=config['xc']['libxc']:
        raise ValueError('Independent model or XC convention differs')
    if reference.get('engine')!='DFTK' or reference.get('energy_offset_applied')!=0 or reference.get('energy_unit')!='hartree/cell':
        raise ValueError('Unshifted independent DFTK energies per cell required')
    refs=reference['comparisons'];conv=reference['cutoff_convergence']
    if len(refs)!=2 or {r['k_n'] for r in refs}!={1,2}:
        raise ValueError('Independent Gamma and 2x2x2 comparisons required')
    target=conv['target_hartree_per_cell']
    if not np.isfinite(target) or not 0<target<=1e-4:
        raise ValueError('Independent plane-wave cutoff target must be <=0.1mEh')
    expected_cutoffs=config['reference']['ecut_hartree'];changes=[]
    for ref in refs:
        n=ref['k_n'];expected=np.asarray(config['kpoint_meshes'][str(n)]);weights=np.full(len(expected),1/len(expected))
        records=sorted([r for r in conv['records'] if r['k_n']==n],key=lambda r:r['ecut_hartree'])
        if [r['ecut_hartree'] for r in records]!=expected_cutoffs or len(records)<2:
            raise ValueError('Independent cutoff records are incomplete or duplicated')
        for record in [ref,*records]:
            points=np.asarray(record['kpoints_fractional']);actual_weights=np.asarray(record['kpoint_weights'])
            if points.shape!=expected.shape or actual_weights.shape!=weights.shape:
                raise ValueError('Independent k coordinates or weights have the wrong shape')
            # Match weights to complete triples, independent of order.
            order=sorted(range(len(points)),key=lambda i:tuple(points[i]))
            expected_order=sorted(range(len(expected)),key=lambda i:tuple(expected[i]))
            if not np.allclose(points[order],expected[expected_order],atol=1e-14,rtol=0) or not np.allclose(actual_weights[order],weights,atol=1e-14,rtol=0):
                raise ValueError('Independent k coordinates or weights differ')
            if not np.isfinite(record['energy_per_cell']):raise ValueError('Non-finite independent energy')
        for record in records:
            scalars=[record[k] for k in ['density_residual','electron_count','max_orthogonality_error','sampled_ks_gap_hartree']]
            scalars.extend(record['energy_components'].values())
            if not np.isfinite(scalars).all() or record['density_residual']<0 or record['max_orthogonality_error']<0:
                raise ValueError('Non-finite or negative independent state diagnostic')
            if not record['converged'] or record['density_residual']>1e-9:
                raise ValueError('Independent SCF record has not converged')
            if abs(record['electron_count']-2)>1e-8 or record['max_orthogonality_error']>1e-8:
                raise ValueError('Independent electronic state failed consistency checks')
            if abs(sum(record['energy_components'].values())-record['energy_per_cell'])>1e-9:
                raise ValueError('Independent total energy does not reconstruct')
        if ref['ecut_hartree']!=records[-1]['ecut_hartree'] or abs(ref['energy_per_cell']-records[-1]['energy_per_cell'])>1e-12:
            raise ValueError('Independent comparison is not the final cutoff result')
        changes.append(abs(records[-1]['energy_per_cell']-records[-2]['energy_per_cell']))
    if len(conv['records'])!=sum(len(expected_cutoffs) for _ in refs):raise ValueError('Unexpected independent cutoff records')
    return bool(max(changes)<=target)


def summarize(config,rows,reference,input_hash,reference_hash):
    cutoff_passed=validate_reference(config,reference)
    indexed={r['id']:r for r in rows};a=config['acceptance'];convergence={}
    for name,ids in config['convergence_groups'].items():
        selected=[indexed[i] for i in ids];energies=[r['energy_per_cell'] for r in selected]
        differences=[abs(e2-e1) for e1,e2 in zip(energies,energies[1:])]
        target=a[name+'_last_change']
        convergence[name]=dict(case_ids=ids,energies_per_cell=energies,adjacent_changes=differences,last_change=differences[-1],target=target,target_reached=bool(differences[-1]<=target))
    comparisons=[]
    for ref in reference['comparisons']:
        row=indexed['k-'+str(ref['k_n'])]
        if row['kpoints_fractional']!=ref['kpoints_fractional']:
            if not np.allclose(sorted(row['kpoints_fractional']),sorted(ref['kpoints_fractional']),atol=1e-14,rtol=0):
                raise ValueError('Independent reference samples different k points')
        difference=abs(row['energy_per_cell']-ref['energy_per_cell'])
        comparisons.append(dict(case_id=row['id'],k_n=ref['k_n'],pyscf_energy_per_cell=row['energy_per_cell'],dftk_energy_per_cell=ref['energy_per_cell'],absolute_difference=difference,acceptance=a['reference_energy_difference'],passed=bool(difference<=a['reference_energy_difference'])))
    if not comparisons or {c['k_n'] for c in comparisons}!={1,2}:
        raise ValueError('Independent Gamma and 2x2x2 comparisons required')
    # The reference file must carry the exact scientific model. Basis representations differ.
    if reference['cell']!=config['cell'] or reference['xc']!=config['xc']['libxc']:
        raise ValueError('Independent model or XC convention differs')
    metrics=dict(max_reference_energy_error=max(c['absolute_difference'] for c in comparisons),
                 max_scf_commutator=max(r['scf_commutator_norm'] for r in rows),
                 max_orbital_residual=max(r['orbital_residual_norm'] for r in rows),
                 max_electron_count_error=max(r['electron_count_error'] for r in rows),
                 max_orthogonality_error=max(r['orthogonality_error'] for r in rows),
                 max_energy_reconstruction_error=max(r['energy_reconstruction_error'] for r in rows),
                 min_sampled_ks_gap=min(r['sampled_ks_gap'] for r in rows),
                 max_overlap_condition=max(r['overlap_condition_max'] for r in rows),
                 min_overlap_eigenvalue=min(r['overlap_min_eigenvalue'] for r in rows),
                 max_tight_scf_commutator=max(r['scf_commutator_norm'] for r in rows if r['sweep']!='scf'),
                 **{name+'_last_change':c['last_change'] for name,c in convergence.items()})
    checks=dict(all_scf_converged=all(r['converged'] for r in rows),
                positive_sampled_gap=metrics['min_sampled_ks_gap']>=a['min_sampled_ks_gap'],
                electron_count=metrics['max_electron_count_error']<=a['max_electron_count_error'],
                orthogonality=metrics['max_orthogonality_error']<=a['max_orthogonality_error'],
                overlap_condition=metrics['max_overlap_condition']<=a['max_overlap_condition'],
                energy_reconstruction=metrics['max_energy_reconstruction_error']<=a['max_energy_reconstruction_error'],
                tight_scf_residual=metrics['max_tight_scf_commutator']<=a['max_commutator'],
                independent_reference=all(c['passed'] for c in comparisons),
                independent_cutoff_convergence=cutoff_passed,
                **{name+'_convergence':c['target_reached'] for name,c in convergence.items()})
    checks={key:bool(value) for key,value in checks.items()}
    return dict(schema_version=1,case='periodic-he-dft',input_sha256=input_hash,reference_sha256=reference_hash,
                environment=rows[0]['environment'],scope=config['scope'],cell=config['cell'],xc=config['xc'],
                implementation='Original reproducibility/validation driver using PySCF periodic KRKS, FFTDF and Libxc; not a new DFT engine.',
                energy_convention='Hartree per neutral primitive cell including the ionic Ewald contribution, without fitted constant shifts.',
                cases=rows,convergence=convergence,independent_comparison=dict(engine='DFTK',cases=comparisons,cutoff_convergence=reference['cutoff_convergence'],scope='Two independently implemented engines with different finite orbital representations; compare total per-cell energies within a stated finite-basis budget, not bitwise equality.'),
                metrics=metrics,checks=checks,passed=all(checks.values()),termination='fixed_sweeps_completed' if all(r['converged'] for r in rows) else 'scf_not_converged')


def write_outputs(output,result,config):
    output.mkdir(parents=True,exist_ok=True)
    (output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    basis={b:i for i,b in enumerate(config['basis_sequence'])}
    with (output/'solution.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['case_index','k_n','basis_index','ao_count','fft_n','energy_per_cell','commutator','sampled_ks_gap','iterations'])
        for i,r in enumerate(result['cases']):writer.writerow([i,r['k_n'],basis[r['basis']],r['ao_count'],r['fft_mesh'][0],r['energy_per_cell'],r['scf_commutator_norm'],r['sampled_ks_gap'],r['iterations']])
    with (output/'scf.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['case_index','cycle','energy_per_cell','has_previous_energy','delta_energy','density_change','gradient_norm'])
        for i,r in enumerate(result['cases']):
            for h in r['trace']:writer.writerow([i,h['cycle'],h['energy_total'],int(h['delta_energy'] is not None),h['delta_energy'] or 0.,h['density_change'],h['gradient_norm']])


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    try:
        if a.output.exists() and any(a.output.iterdir()):raise ValueError('Output must be new or empty')
        config=json.loads(a.input.read_text());ref=ROOT/'reference-dftk.json';reference=json.loads(ref.read_text())
        validate_reference(config,reference)
        result=summarize(config,run_cases(config),reference,sha(a.input),sha(ref));write_outputs(a.output,result,config)
        print(json.dumps(dict(passed=result['passed'],metrics=result['metrics'])))
        return 0 if result['passed'] else 1
    except Exception as exc:
        print(type(exc).__name__+': '+str(exc),file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
