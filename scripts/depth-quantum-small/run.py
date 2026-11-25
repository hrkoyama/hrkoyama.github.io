"""DRAFT fixed-input runner. Requires exact root/peer-reviewed freeze first."""
import argparse
import csv
import hashlib
import json
import platform
import time
from pathlib import Path
import numpy as np
from io_utils import Checkpoints, plain
import coupled_md
import eigenpairs
import molecules
import periodic_projector

ROOT=Path(__file__).resolve().parent


def validate_freeze(path):
    freeze=json.loads(Path(path).read_text())
    if freeze.get('status')!='ROOT_PEER_REVIEWED_FROZEN':raise ValueError('Root and peer freeze required')
    for name,want in freeze['files_sha256'].items():
        target=ROOT/name
        if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=want:
            raise ValueError('Frozen source/input/reference changed: '+name)
    required={p.name for p in ROOT.glob('*.py')}|{'inputs.json','acceptance.json','provenance.json','cards.json','cases.json'}
    required|={str(p.relative_to(ROOT)) for p in (ROOT/'saved-data').glob('*.json')}
    if not required<=set(freeze['files_sha256']):raise ValueError('Freeze omits owned source/input/reference')
    if not freeze.get('root_review') or not freeze.get('independent_peer_review'):raise ValueError('Both reviews required')
    return freeze


def assess(results,criteria):
    checks=[]
    def le(name,value,limit,kind='required'):
        checks.append({'name':name,'value':float(value),'operator':'<=','limit':limit,'passed':bool(value<=limit),'kind':kind})
    def ge(name,value,limit):
        checks.append({'name':name,'value':float(value),'operator':'>=','limit':limit,'passed':bool(value>=limit),'kind':'required'})
    md=results['95'];c=criteria['95']
    for row in md['runs']:
        le('95 '+row['id']+' NVE extended energy drift',row['max_energy_drift'],c['max_BO_or_CP_NVE_energy_drift'],'accuracy_goal')
    for name in ['bo','cp-mu004']:
        row=next(x for x in md['runs'] if x['id']==name+'-2')
        le('95 '+name+' finest RK4 state comparison',row['reference_state_error'],c['finest_state_RK4_difference'],'accuracy_goal')
    for reference in md['reference_sensitivity']:
        le('95 '+reference['model']+' fixed RK4 companion sensitivity',reference['state_difference'],c['RK4_companion_state_difference'])
    le('95 OU extended energy minus measured heat',md['thermal_heat_ledger_error'],c['OU_heat_corrected_extended_energy_error'],'accuracy_goal')
    le('95 OU conditional temperature variance identity',md['OU_conditional_variance_identity_error'],c['OU_conditional_variance_identity_error'])
    le('95 normalized orbital',max(x['orbital_norm_error'] for row in md['runs'] for x in row['trajectory']),c['orbital_norm_error'])
    atom=results['96'];c=criteria['96']
    le('96 selected saved row count',abs(len(atom['cases'])-c['saved_rows']),0)
    for i,row in enumerate(atom['cases']):
        le('96 saved energy literal '+str(i),abs(row['energy']-c['energies_exact_saved_literals'][i]),0)
        le('96 basis functions '+str(i),abs(row['basis_size']-40),0)
        le('96 saved electron count '+str(i),abs(row['electron_count_overlap']-2),c['electron_number_saved_error'])
    c=criteria['97'];rows=results['97']['rows']
    for row in rows:
        for metric,key in [('native_norm_error','native_norm_error_before_conversion'),('physical_norm_error','physical_norm_error'),('orthogonality_error','orthogonality_error')]:le('97 '+row['id']+' '+metric,row[metric],c[key])
        for pair in row['pairs']:
            name='97 '+row['id']+' state'+str(pair['state'])
            le(name+' residual',pair['scaled_residual'],c['scaled_residual'])
            if row['model']=='box':le(name+' same-grid oracle',pair['same_grid_relative_error'],c['box_same_grid_relative_error'])
            else:le(name+' reflection parity',pair['parity_residual'],c['HO_parity_error'])
    boxes=[x for x in rows if x['model']=='box']
    for k in range(3):
        le('97 box finest relative continuum '+str(k),abs(boxes[-1]['pairs'][k]['signed_energy_error'])/boxes[-1]['pairs'][k]['continuum_energy'],c['box_finest_relative_continuum_error'],'accuracy_goal')
        for i in range(2):
            ratio=abs(boxes[i]['pairs'][k]['signed_energy_error']/boxes[i+1]['pairs'][k]['signed_energy_error'])
            ge('97 box reduction lower '+str((k,i)),ratio,c['box_doubling_error_ratio'][0]);le('97 box reduction upper '+str((k,i)),ratio,c['box_doubling_error_ratio'][1])
    finest=next(x for x in rows if x['model']=='HO' and x['M']==256)
    for pair in finest['pairs']:le('97 HO finest total error '+str(pair['state']),abs(pair['signed_energy_error']),c['HO_finest_absolute_total_error_goal'],'accuracy_goal')
    c=criteria['98'];m=results['98-99'];saved=results['saved_H2']['cases']
    for row in m['H2']:
        name='98 R'+str(row['bond']);oracle=row['oracle'];R=row['RHF'];U=row['UHF'];F=row['FCI']
        reference=next(x for x in saved if x['bond_bohr']==row['bond'])
        le(name+' saved PySCF RHF',abs(R['energy']-reference['energy_total']),c['saved_PySCF_RHF_energy_difference'])
        le(name+' UHF analytic paired ansatz',abs(U['energy']-oracle['UHF_symmetric_pair_variational_min']),c['H2_UHF_analytic_pair_oracle_error'])
        le(name+' finite-basis FCI analytic',abs(F['energy']-oracle['FCI_even_singlet']),c['H2_FCI_even_oracle_error'])
        le(name+' independent fermion assembly',F['operator_assembly_error'],c['FCI_operator_assembly_error']);le(name+' FCI residual',F['residual'],c['FCI_residual'])
        le(name+' UHF <= RHF',U['energy']-R['energy'],c['energy_ordering_slack']);le(name+' FCI <= UHF',F['energy']-U['energy'],c['energy_ordering_slack'])
        for method in ['RHF','UHF']:
            value=row[method];le(name+' '+method+' electron count',abs(value['electron_count']-2),c['electron_number_error'])
            le(name+' '+method+' orbital norm',value['overlap_orthogonality'],c['orbital_orthogonality_error']);le(name+' '+method+' SCF residual',value['commutator'],c['SCF_commutator'])
    stretched=m['H2'][-1]
    ge('98 stretched UHF energy lowering',stretched['RHF']['energy']-stretched['UHF']['energy'],c['stretched_UHF_lower_than_RHF_by'])
    ge('98 stretched UHF spin contamination',stretched['UHF']['spin_square'],c['stretched_spin_contamination_greater_than'])
    c=criteria['99'];v=m['H3plus'];F=v['FCI'];R=v['RHF']
    le('99 operator assembly',F['operator_assembly_error'],c['FCI_operator_assembly_error']);le('99 FCI residual',F['residual'],c['FCI_residual'])
    le('99 singlet spatial symmetry',F['singlet_spatial_symmetry_error'],c['FCI_singlet_spatial_symmetry_error'])
    le('99 MP2 determinant perturbation oracle',abs(v['MP2_correlation']-v['MP2_determinant_RS2_oracle']),c['MP2_RS2_oracle_difference'])
    ge('99 MP2 minimum denominator',v['minimum_MP2_gap'],c['min_MP2_denominator_gap']);le('99 FCI <= RHF',F['energy']-R['energy'],c['FCI_le_RHF_slack'])
    le('99 RHF electron count',abs(R['electron_count']-2),c['electron_number_error']);le('99 RHF SCF residual',R['commutator'],c['SCF_commutator'])
    he=results['100'];c=criteria['100'];old=he['acceptance_unchanged']
    for i,row in enumerate(he['finite_difference']['components']):
        recomputed=-(row['energy_plus']-row['energy_minus'])/(2*row['step_bohr'])
        le('100 saved FD arithmetic '+str(i),abs(recomputed-row['force_finite_difference']),c['recomputed_saved_FD_value_difference'])
        le('100 unchanged FD science bound '+str(i),abs(row['force_analytic']-recomputed),old['finite_difference_max_error'])
    for row in he['independent_cases']:
        error=float(np.max(abs(np.array(row['pyscf_forces_cartesian'])-np.array(row['dftk_forces_cartesian']))))
        le('100 unchanged Gaussian/PW force '+row['case_id'],error,row['force_acceptance'])
        le('100 unchanged Gaussian/PW energy '+row['case_id'],abs(row['pyscf_energy_per_cell']-row['dftk_energy_per_cell']),row['energy_acceptance'])
    c=criteria['101'];v=results['101'];center=v['center']
    for i,row in enumerate(center['rows']):
        le('101 Hermiticity '+str(i),row['hermiticity_error'],c['hermiticity_error']);le('101 residual '+str(i),row['residual'],c['eigenpair_residual']);le('101 independent cubic '+str(i),row['cubic_reference_error'],c['cubic_independent_eigenvalue_error'])
        le('101 fixed-case cubic clamp activation '+str(i),int(row['cubic_oracle_diagnostics']['roundoff_clamp_active']),0)
    le('101 fixed electron number',abs(center['thermo']['electrons']-1.5),c['electron_number_error'])
    ge('101 lower occupation',float(np.min(center['thermo']['f'])),0);le('101 upper occupation',float(np.max(center['thermo']['f'])),2)
    ge('101 nonnegative entropy',center['thermo']['entropy'],-c['entropy_nonnegative_slack'])
    le('101 finest free-energy force difference',v['force_differences'][-1]['error'],c['finest_force_free_energy_FD_error'],'accuracy_goal')
    return checks


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',default=str(ROOT/'freeze.json'));parser.add_argument('--input',default=str(ROOT/'inputs.json'));parser.add_argument('--output',required=True);args=parser.parse_args()
    freeze=validate_freeze(args.freeze);save=Checkpoints(args.output);start=time.monotonic()
    input_path=Path(args.input)
    input_sha=hashlib.sha256(input_path.read_bytes()).hexdigest()
    if input_sha!=freeze['files_sha256']['inputs.json']:raise ValueError('CLI input differs from frozen inputs')
    c=json.loads(input_path.read_text());criteria=json.loads((ROOT/'acceptance.json').read_text())
    save('execution-context',{'python':platform.python_version(),'numpy':np.__version__,
         'freeze_sha256':hashlib.sha256(Path(args.freeze).read_bytes()).hexdigest(),'frozen_files_sha256':freeze['files_sha256'],
         'input':c,'acceptance':criteria})
    results={}
    try:
        results['95']=coupled_md.run(c['md95'],save);save('95-result',results['95'])
        results['96']=json.loads((ROOT/'saved-data/atom-reference.json').read_text());save('96-result',results['96'])
        results['97']=eigenpairs.run(c['eigen97'],save);save('97-result',results['97'])
        results['98-99']=molecules.run(c['molecule98'],c['molecule99'],save);save('98-99-result',results['98-99'])
        results['saved_H2']=json.loads((ROOT/'saved-data/h2-rhf-reference.json').read_text())
        results['100']=json.loads((ROOT/'saved-data/periodic-he-reference.json').read_text());save('100-result',results['100'])
        results['101']=periodic_projector.run(c['periodic101'],save);save('101-result',results['101'])
        checks=assess(results,criteria);save('checks',checks)
        summary={'state':'completed','passed':all(x['passed'] for x in checks),'checks':checks,'elapsed_seconds':time.monotonic()-start,
                 'new_models':6,'saved_reference_only_sequences':[96,100],'new_trajectories':8,'quantum97_API_calls':8,
                 'original_heavy_tails_completed':False,'scope':'Small educational representatives plus immutable saved-reference audits; see cards.json for explicit method boundaries.'}
        save('summary',summary)
        case_records=[]
        case_ids={95:'two-state-bo-cp-ou',96:'atomic-reference-cards',97:'quantum-box-ho',98:'h2-rhf-uhf-fci',99:'h3plus-mp2-fci',100:'periodic-he-reference-cards',101:'periodic-projector-occupations'}
        checkpoint={95:'95-result.json',96:'96-result.json',97:'97-result.json',98:'98-99-result.json',99:'98-99-result.json',100:'100-result.json',101:'101-result.json'}
        for sequence,ident in case_ids.items():
            selected=[x for x in checks if x['name'].startswith(str(sequence)+' ')]
            case_checks={x['name']:x['passed'] for x in selected}
            case_records.append({'id':ident,'passed':all(case_checks.values()),'checks':case_checks,
                                 'metrics':{x['name']:x['value'] for x in selected},
                                 'records':{'saved_data':checkpoint[sequence],'sequence':sequence,
                                            'new_simulations':False if sequence in [96,100] else True,
                                            'scope_card':'cards.json#'+ident}})
        # Real per-check measurements, thresholds and decisions; not a placeholder.
        with (Path(args.output)/'measurements.csv').open('w',newline='') as handle:
            writer=csv.writer(handle);writer.writerow(['sequence','check_index','measurement','limit','passed','accuracy_goal'])
            for index,row in enumerate(checks):
                writer.writerow([int(row['name'].split()[0]),index,row['value'],row['limit'],int(row['passed']),int(row['kind']=='accuracy_goal')])
        save('result',{'schema_version':1,'passed':summary['passed'],'input_sha256':input_sha,
                       'checks':{row['id']:row['passed'] for row in case_records},'cases':case_records,
                       'termination':'completed_fixed_protocol',
                       'environment':{'python':platform.python_version(),'numpy':np.__version__},
                       'accuracy_goals':[x for x in checks if x['kind']=='accuracy_goal'],
                       'original_heavy_tails_completed':False,'new_simulation_model_families':6,
                       'reference_only_sequences':[96,100]})
        return 0 if summary['passed'] else 1
    except Exception as error:
        save('runner-exception',{'type':type(error).__name__,'message':str(error),'elapsed_seconds':time.monotonic()-start,'retained_sequences':list(results)})
        raise


if __name__=='__main__':raise SystemExit(main())
