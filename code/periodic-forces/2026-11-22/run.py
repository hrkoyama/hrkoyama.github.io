"""Run fixed two-He periodic force, convergence and BO-interface checks.

Exit 0: every criterion met; 1: a numerical criterion failed; 2: invalid input
or runtime error. DFTK regeneration is separate, never a hidden Python fallback.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from periodic_forces import solve, energy_and_forces, require_converged, validate_model
from bomd import velocity_verlet_step

ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
maximum=lambda a:float(np.max(np.abs(a)))


def validate_reference(config,reference):
    """Recompute reference acceptance from saved numbers, not saved pass flags."""
    validate_model(config)
    if reference.get('engine')!='DFTK' or reference['cell']!=config['cell'] or reference['xc']!=config['xc']['libxc']:
        raise ValueError('Independent engine/model/XC mismatch')
    if reference.get('energy_unit')!='hartree/cell' or reference.get('force_unit')!='hartree/bohr' or reference.get('energy_offset_applied')!=0 or reference.get('force_offset_applied')!=0:
        raise ValueError('Unshifted hartree/cell energy and Cartesian hartree/bohr forces required')
    if reference.get('input_sha256')!=sha(ROOT/'inputs.json'):
        raise ValueError('Independent reference was not generated from this frozen input')
    for key,path in [('pseudopotential_sha256',ROOT/'He.gth'),('script_sha256',ROOT/'reference.jl'),('project_sha256',ROOT/'reference-environment/Project.toml'),('manifest_sha256',ROOT/'reference-environment/Manifest.toml')]:
        if reference.get(key)!=sha(path):raise ValueError('Independent reference provenance hash mismatch: '+key)
    comparisons=reference['comparisons'];conv=reference['cutoff_convergence'];records=conv['records']
    if {r['k_n'] for r in comparisons}!={1,2} or len(comparisons)!=2:raise ValueError('Independent Gamma and 2-cubed force comparisons required')
    force_changes=[];energy_changes=[]
    for ref in comparisons:
        n=ref['k_n'];expected=np.asarray(config['kpoint_meshes'][str(n)])
        points_count=len(expected);expected_weights=np.full(points_count,1/points_count)
        group=sorted([r for r in records if r['k_n']==n],key=lambda r:r['ecut_hartree'])
        if [r['ecut_hartree'] for r in group]!=config['reference']['ecut_hartree']:raise ValueError('Incomplete or duplicated independent cutoff scan')
        for record in [ref,*group]:
            actual_positions=np.asarray(record['positions_bohr'])
            if actual_positions.shape!=(2,3) or not np.allclose(actual_positions,config['cell']['positions_bohr'],rtol=0,atol=1e-14):raise ValueError('Independent nominal-state geometry mismatch')
            points=np.asarray(record['kpoints_fractional']);weights=np.asarray(record['kpoint_weights'])
            if points.shape!=expected.shape or weights.shape!=expected_weights.shape:raise ValueError('Independent mesh shape mismatch')
            order=sorted(range(points_count),key=lambda i:tuple(points[i]));expected_order=sorted(range(points_count),key=lambda i:tuple(expected[i]))
            if not np.allclose(points[order],expected[expected_order],rtol=0,atol=1e-14) or not np.allclose(weights[order],expected_weights,rtol=0,atol=1e-14):raise ValueError('Independent k coordinates or weights differ')
            f=np.asarray(record['forces_cartesian'])
            if f.shape!=(2,3) or not np.isfinite(f).all() or not np.isfinite(record['energy_per_cell']):raise ValueError('Invalid independent force or energy')
        for record in group:
            diagnostics=[record[k] for k in ['density_residual','electron_count','max_orthogonality_error']]+list(record['energy_components'].values())
            if not np.isfinite(diagnostics).all():raise ValueError('Non-finite independent electronic-state diagnostic')
            if not record['converged'] or not np.isfinite(record['density_residual']) or not 0<=record['density_residual']<=1e-9:raise ValueError('Independent SCF is not converged')
            if abs(record['electron_count']-4)>1e-8 or not 0<=record['max_orthogonality_error']<=1e-8:raise ValueError('Independent electronic-state consistency failure')
            if abs(sum(record['energy_components'].values())-record['energy_per_cell'])>1e-9:raise ValueError('Independent energy does not reconstruct')
        if ref['ecut_hartree']!=group[-1]['ecut_hartree'] or maximum(np.asarray(ref['forces_cartesian'])-group[-1]['forces_cartesian'])>1e-12 or abs(ref['energy_per_cell']-group[-1]['energy_per_cell'])>1e-12:raise ValueError('Independent comparison must use final cutoff')
        force_changes.append(maximum(np.asarray(group[-1]['forces_cartesian'])-group[-2]['forces_cartesian']))
        energy_changes.append(abs(group[-1]['energy_per_cell']-group[-2]['energy_per_cell']))
    if len(records)!=2*len(config['reference']['ecut_hartree']):raise ValueError('Unexpected cutoff records')
    ft=config['reference']['force_cutoff_tolerance'];et=config['reference']['energy_cutoff_tolerance']
    if not (np.isfinite([ft,et]).all() and 0<ft<=1e-5 and 0<et<=1e-4):raise ValueError('Independent convergence criteria too weak')
    # Saved independent finite differences supplement the analytical-force
    # cross-engine comparison. Acceptance is recalculated below when available.
    fd=reference['finite_difference'];records=fd['records']
    steps=config['reference']['finite_difference_steps_bohr'];smallest=min(steps)
    expected_keys={(0,0,h) for h in steps}|{(i,j,smallest) for i in range(2) for j in range(3)}
    keys=[(r['atom_index'],r['component'],r['step_bohr']) for r in records]
    if set(keys)!=expected_keys or len(keys)!=len(expected_keys):
        raise ValueError('Independent finite differences require the full six components and registered h scan')
    fd_errors=[];ref0=next(r for r in comparisons if r['k_n']==1)
    for record in records:
        values=[record[k] for k in ['energy_plus','energy_minus','step_bohr','analytic_force','central_difference_force']]
        if not np.isfinite(values).all() or record['step_bohr']<=0:raise ValueError('Invalid independent finite-difference data')
        numerical=-(record['energy_plus']-record['energy_minus'])/(2*record['step_bohr'])
        if abs(numerical-record['central_difference_force'])>1e-10:raise ValueError('Independent finite difference does not reconstruct')
        if abs(record['analytic_force']-ref0['forces_cartesian'][record['atom_index']][record['component']])>1e-12:raise ValueError('Independent finite difference uses a different analytic force')
        displaced=record['displaced_records']
        if len(displaced)!=2:raise ValueError('Independent displaced electronic states missing')
        for sign,state,energy in zip([-1,1],displaced,[record['energy_minus'],record['energy_plus']]):
            target=np.asarray(config['cell']['positions_bohr']).copy()
            target[record['atom_index'],record['component']]+=sign*record['step_bohr']
            actual=np.asarray(state['positions_bohr'])
            diagnostics=[state[k] for k in ['energy_per_cell','density_residual','electron_count','max_orthogonality_error']]+list(state['energy_components'].values())
            if actual.shape!=(2,3) or not np.allclose(actual,target,rtol=0,atol=1e-14):raise ValueError('Independent displaced geometry mismatch')
            if not np.isfinite(diagnostics).all() or not state['converged'] or state['density_residual']>1e-9 or state['density_residual']<0:raise ValueError('Independent displaced SCF failed')
            if abs(state['electron_count']-4)>1e-8 or not 0<=state['max_orthogonality_error']<=1e-8:raise ValueError('Independent displaced state consistency failure')
            if abs(state['energy_per_cell']-energy)>1e-12 or abs(sum(state['energy_components'].values())-energy)>1e-9:raise ValueError('Independent displaced energy mismatch')
            if state['k_n']!=1 or state['ecut_hartree']!=config['reference']['ecut_hartree'][-1] or state['kpoints_fractional']!=ref0['kpoints_fractional'] or state['kpoint_weights']!=ref0['kpoint_weights']:raise ValueError('Independent displaced numerical model differs')
        fd_errors.append(abs(numerical-record['analytic_force']))
    return dict(passed=bool(max(force_changes)<=ft and max(energy_changes)<=et and max(fd_errors)<=config['reference']['finite_difference_tolerance']),max_cutoff_force_change=max(force_changes),max_cutoff_energy_change=max(energy_changes),max_finite_difference_error=max(fd_errors))


def run_cases(config):
    rows=[];baseline_density=None
    for spec in config['cases']:
        row,density=solve(config,spec,return_density=True);rows.append(row)
        if spec['id']==config['finite_difference']['case_id']:baseline_density=density
        print('CASE '+row['id']+' E='+format(row['energy_per_cell'],'.12f')+' maxF='+format(maximum(row['forces_cartesian']),'.9f'),file=sys.stderr,flush=True)
    return rows,baseline_density


def finite_differences(config,baseline,density):
    fd=config['finite_difference'];spec=next(c for c in config['cases'] if c['id']==fd['case_id']);positions=np.asarray(config['cell']['positions_bohr']);forces=np.asarray(baseline['forces_cartesian']);cache={}
    evaluations=[]
    def pair(atom,axis,h):
        key=(atom,axis,h)
        if key in cache:return cache[key]
        energies=[]
        for sign in [-1,1]:
            moved=positions.copy();moved[atom,axis]+=sign*h
            row=solve(config,spec,moved,with_forces=False,density_guess=density);require_converged(row)
            energies.append(row['energy_per_cell'])
            evaluations.append(dict(atom=atom,axis=axis,step_bohr=h,sign=sign,energy_per_cell=row['energy_per_cell'],iterations=row['iterations'],scf_commutator_norm=row['scf_commutator_norm'],converged=row['converged']))
        numerical=-(energies[1]-energies[0])/(2*h)
        result=dict(atom=atom,axis=axis,step_bohr=h,energy_minus=energies[0],energy_plus=energies[1],force_analytic=float(forces[atom,axis]),force_finite_difference=numerical,absolute_error=abs(numerical-forces[atom,axis]))
        cache[key]=result
        print('FD atom='+str(atom)+' axis='+str(axis)+' h='+str(h)+' error='+format(result['absolute_error'],'.3e'),file=sys.stderr,flush=True)
        return result
    components=[pair(i,j,fd['all_components_step_bohr']) for i in range(2) for j in range(3)]
    steps=[pair(fd['scan_atom'],fd['scan_axis'],h) for h in fd['steps_bohr']]
    return dict(case_id=fd['case_id'],step_bohr=fd['all_components_step_bohr'],components=components,steps=steps,evaluations=evaluations,max_component_error=max(r['absolute_error'] for r in components),scan_max_error=max(r['absolute_error'] for r in steps),initial_guess='Every displaced SCF starts from the same converged undisplaced density; no displaced energy is reused as a solution.')


def bomd_smoke(config,baseline,density):
    b=config['bomd'];spec=next(c for c in config['cases'] if c['id']==b['case_id']);positions=np.asarray(config['cell']['positions_bohr']);velocities=np.asarray(b['velocities_bohr_per_atomic_time']);masses=np.asarray(b['mass_electron_masses']);dt=b['total_time_atomic_units'];evaluations=[]
    def provider(r):
        # A fixed warm-start density changes iteration counts, never the model,
        # tolerance, electronic occupations or the converged energy definition.
        row=energy_and_forces(config,spec,r,density_guess=density);evaluations.append(row)
        return row
    full=velocity_verlet_step(provider,positions,velocities,masses,dt,initial_record=baseline)
    half=velocity_verlet_step(provider,positions,velocities,masses,dt/2,initial_record=baseline)
    halves=velocity_verlet_step(provider,half['positions_bohr'],half['velocities_bohr_per_atomic_time'],masses,dt/2,initial_record=half['electronic_state'])
    initial_energy=baseline['energy_per_cell']+float(.5*np.sum(masses[:,None]*velocities*velocities))
    return dict(scope=b['scope'],case_id=b['case_id'],total_time_atomic_units=dt,mass_electron_masses=masses.tolist(),initial_velocities_bohr_per_atomic_time=velocities.tolist(),initial_energy_hartree=initial_energy,full_step=full,two_half_steps=halves,position_max_difference=maximum(np.asarray(full['positions_bohr'])-halves['positions_bohr']),velocity_max_difference=maximum(np.asarray(full['velocities_bohr_per_atomic_time'])-halves['velocities_bohr_per_atomic_time']),full_step_energy_defect=abs(full['total_energy_hartree']-initial_energy),two_half_steps_energy_defect=abs(halves['total_energy_hartree']-initial_energy),electronic_force_evaluations=evaluations)


def summarize(config,rows,fd,bomd,reference,input_hash,reference_hash):
    audit=validate_reference(config,reference);indexed={r['id']:r for r in rows};a=config['acceptance'];convergence={}
    if len(indexed)!=len(config['cases']) or set(indexed)!={r['id'] for r in config['cases']}:raise ValueError('Missing or duplicate fixed case')
    for name,ids in config['convergence_groups'].items():
        forces=[indexed[i]['forces_cartesian'] for i in ids];changes=[maximum(np.asarray(y)-x) for x,y in zip(forces,forces[1:])];target=a[name+'_last_change']
        convergence[name]=dict(case_ids=ids,forces_cartesian=forces,adjacent_changes=changes,last_change=changes[-1],target=target,target_reached=bool(changes[-1]<=target))
    comparisons=[]
    for ref in reference['comparisons']:
        row=indexed[config['reference']['comparison_cases'][str(ref['k_n'])]]
        if row['k_n']!=ref['k_n']:raise ValueError('Independent comparison k-mesh mismatch')
        ferr=maximum(np.asarray(row['forces_cartesian'])-ref['forces_cartesian']);eerr=abs(row['energy_per_cell']-ref['energy_per_cell'])
        comparisons.append(dict(case_id=row['id'],k_n=ref['k_n'],pyscf_forces_cartesian=row['forces_cartesian'],dftk_forces_cartesian=ref['forces_cartesian'],pyscf_energy_per_cell=row['energy_per_cell'],dftk_energy_per_cell=ref['energy_per_cell'],max_absolute_force_difference=ferr,energy_absolute_difference=eerr,force_acceptance=a['reference_force_difference'],energy_acceptance=a['reference_energy_difference'],passed=bool(ferr<=a['reference_force_difference'] and eerr<=a['reference_energy_difference'])))
    extra=fd['evaluations']+bomd['electronic_force_evaluations']
    metrics=dict(max_reference_force_error=max(c['max_absolute_force_difference'] for c in comparisons),max_reference_energy_error=max(c['energy_absolute_difference'] for c in comparisons),finite_difference_max_error=fd['max_component_error'],finite_difference_scan_max_error=fd['scan_max_error'],max_tight_scf_commutator=max([r['scf_commutator_norm'] for r in rows if r['sweep']!='scf']+[r['scf_commutator_norm'] for r in extra]),max_scf_commutator=max(r['scf_commutator_norm'] for r in rows),max_electron_count_error=max(r['electron_count_error'] for r in rows),max_orthogonality_error=max(r['orthogonality_error'] for r in rows),max_energy_reconstruction_error=max(r['energy_reconstruction_error'] for r in rows),min_sampled_ks_gap=min(r['sampled_ks_gap'] for r in rows),max_overlap_condition=max(r['overlap_condition_max'] for r in rows),finest_net_force=indexed['fft-47']['net_force_max'],bomd_position_step_difference=bomd['position_max_difference'],bomd_full_step_energy_defect=bomd['full_step_energy_defect'],bomd_two_half_steps_energy_defect=bomd['two_half_steps_energy_defect'],reference_cutoff_force_change=audit['max_cutoff_force_change'],reference_finite_difference_max_error=audit['max_finite_difference_error'],**{k+'_last_change':v['last_change'] for k,v in convergence.items()})
    checks=dict(all_scf_converged=all(r['converged'] for r in rows+extra),tight_scf_residual=metrics['max_tight_scf_commutator']<=a['max_tight_commutator'],finite_difference=fd['max_component_error']<=a['finite_difference_max_error'],finite_difference_scan=fd['scan_max_error']<=a['finite_difference_scan_max_error'],independent_reference=all(r['passed'] for r in comparisons),independent_reference_self_checks=audit['passed'],electron_count=metrics['max_electron_count_error']<=a['max_electron_count_error'],orthogonality=metrics['max_orthogonality_error']<=a['max_orthogonality_error'],energy_reconstruction=metrics['max_energy_reconstruction_error']<=a['max_energy_reconstruction_error'],positive_sampled_gap=metrics['min_sampled_ks_gap']>=a['min_sampled_ks_gap'],overlap_condition=metrics['max_overlap_condition']<=a['max_overlap_condition'],finest_translation_balance=metrics['finest_net_force']<=a['finest_net_force'],bomd_local_step=metrics['bomd_position_step_difference']<=a['bomd_position_step_difference'],bomd_local_energy=max(bomd['full_step_energy_defect'],bomd['two_half_steps_energy_defect'])<=a['bomd_energy_defect'],**{k+'_convergence':v['target_reached'] for k,v in convergence.items()})
    checks={k:bool(v) for k,v in checks.items()}
    return dict(schema_version=1,case=config['case'],input_sha256=input_hash,reference_sha256=reference_hash,environment=rows[0]['environment'],scope=config['scope'],implementation='Original validation/BO-interface workflow backed by PySCF KRKS+FFTDF analytical Gaussian/Pulay and ionic Ewald forces; not a new electronic-structure engine.',energy_unit='hartree/cell',force_unit='hartree/bohr',force_sign='F_I = -d E_total / d R_I, Cartesian coordinates, including ion-ion Ewald energy.',cell=config['cell'],xc=config['xc'],cases=rows,finite_difference=fd,convergence=convergence,independent_comparison=dict(engine='DFTK',cases=comparisons,cutoff_convergence=reference['cutoff_convergence'],reference_audit=audit,scope='Two independently implemented Hamiltonian/SCF/force engines; Libxc functional formulas shared. Different finite Gaussian and plane-wave orbital spaces, no fitted force or energy shifts.'),bomd=bomd,metrics=metrics,checks=checks,passed=all(checks.values()),termination='fixed_force_checks_completed' if all(r['converged'] for r in rows+extra) else 'scf_not_converged')


def write_outputs(output,result,config):
    output.mkdir(parents=True,exist_ok=True);(output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (output/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['case_index','k_n','basis_index','fft_n','atom','fx','fy','fz','energy_per_cell','scf_commutator'])
        for i,r in enumerate(result['cases']):
            for atom,force in enumerate(r['forces_cartesian']):w.writerow([i,r['k_n'],config['basis_sequence'].index(r['basis']),r['fft_mesh'][0],atom,*force,r['energy_per_cell'],r['scf_commutator_norm']])
    with (output/'finite-difference.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['atom','axis','step_bohr','force_analytic','force_finite_difference','absolute_error','energy_minus','energy_plus'])
        for r in result['finite_difference']['components']+result['finite_difference']['steps']:w.writerow([r[k] for k in ['atom','axis','step_bohr','force_analytic','force_finite_difference','absolute_error','energy_minus','energy_plus']])
    with (output/'scf.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['case_index','cycle','energy_per_cell','has_previous_energy','delta_energy','density_change','gradient_norm'])
        for i,r in enumerate(result['cases']):
            for h in r['trace']:w.writerow([i,h['cycle'],h['energy_total'],int(h['delta_energy'] is not None),h['delta_energy'] or 0.,h['density_change'],h['gradient_norm']])


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    try:
        if args.output.exists() and any(args.output.iterdir()):raise ValueError('Output must be new or empty')
        config=json.loads(args.input.read_text());refpath=ROOT/'reference-dftk.json';reference=json.loads(refpath.read_text());validate_reference(config,reference)
        rows,density=run_cases(config);baseline=next(r for r in rows if r['id']==config['finite_difference']['case_id']);fd=finite_differences(config,baseline,density);bomd=bomd_smoke(config,baseline,density)
        result=summarize(config,rows,fd,bomd,reference,sha(args.input),sha(refpath));write_outputs(args.output,result,config)
        print(json.dumps(dict(passed=result['passed'],metrics=result['metrics'],checks=result['checks'])));return 0 if result['passed'] else 1
    except Exception as exc:
        print(type(exc).__name__+': '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':sys.exit(main())
