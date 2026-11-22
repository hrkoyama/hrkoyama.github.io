"""Fixed-input molecular RHF execution and validation. 0=pass, 1=unmet, 2=error."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import platform
import sys
import numpy as np
import scipy
from molecular_hf import solve


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def calculate(path,max_cycles=None):
    config=json.loads(path.read_text());reference_path=Path(__file__).parent/'reference-pyscf.json';reference=json.loads(reference_path.read_text())
    if reference['input_sha256']!=sha(path):raise ValueError('Reference input SHA-256 differs; regenerate independent reference for changed scientific inputs')
    if max_cycles is not None:config['scf']['max_cycles']=max_cycles
    basis={x['id']:x for x in config['basis_definitions']};rows=[]
    for bond in config['bonds_bohr']:
        for definition in basis.values():
            row=solve(definition,bond,config['scf']);ref=next(x for x in reference['cases'] if x['bond_bohr']==bond and x['basis_id']==definition['id'])
            row.update(reference_energy=ref['energy_total'],energy_error=abs(row['energy_total']-ref['energy_total']))
            rows.append(row)
    sweep=[];spec=config['tolerance_sweep']
    target=next(r for r in rows if r['bond_bohr']==spec['bond_bohr'] and r['basis_id']==spec['basis_id'])
    for level in spec['levels']:
        options={**config['scf'],**{k:v for k,v in level.items() if k!='id'}}
        row=solve(basis[spec['basis_id']],spec['bond_bohr'],options)
        row.update(level=level['id'],options=options,energy_error_to_tight=abs(row['energy_total']-target['energy_total']))
        sweep.append(row)
    refinements=[]
    for bond in config['bonds_bohr']:
        nested=[r for r in rows if r['bond_bohr']==bond and basis[r['basis_id']]['family']=='nested-s-only']
        delta=[b['energy_total']-a['energy_total'] for a,b in zip(nested,nested[1:])]
        refinements.append(dict(bond_bohr=bond,basis_ids=[r['basis_id'] for r in nested],energies=[r['energy_total'] for r in nested],energy_changes=delta,last_absolute_change=abs(delta[-1]),
                                last_two_changes_max=max(abs(d) for d in delta[-2:]),target=config['basis_convergence_target']['two_successive_additions_max_change'],
                                target_reached=bool(max(abs(d) for d in delta[-2:])<=config['basis_convergence_target']['two_successive_additions_max_change'])))
    metric_fields={'max_reference_energy_error':'energy_error','max_scf_commutator':'scf_commutator_norm','max_orbital_residual':'orbital_residual_norm',
                   'max_orthogonality_error':'orthogonality_max','max_electron_count_error':'error_electron_count','max_energy_consistency_error':'energy_consistency_error','max_idempotency_error':'idempotency_norm'}
    metrics={key:max(row[field] for row in rows) for key,field in metric_fields.items()}
    metrics.update(basis_energy_increase_max=max(0.,max(d for r in refinements for d in r['energy_changes'])),
                   last_basis_energy_change_max=max(r['last_absolute_change'] for r in refinements),
                   last_two_basis_changes_max=max(r['last_two_changes_max'] for r in refinements),
                   scf_tolerance_energy_error_max=max(r['energy_error_to_tight'] for r in sweep),
                   scf_tolerance_errors=[r['energy_error_to_tight'] for r in sweep],max_overlap_condition_number=max(r['overlap_condition_number'] for r in rows))
    a=config['acceptance'];checks={key:bool(value<=a[key]) for key,value in metrics.items() if key in a}
    checks.update(basis_monotone=metrics['basis_energy_increase_max']<=a['max_basis_energy_increase'],
                  last_basis_change=metrics['last_basis_energy_change_max']<=a['max_last_basis_energy_change'],
                  scf_tolerance_accuracy=metrics['scf_tolerance_energy_error_max']<=a['max_tolerance_sweep_energy_error'],
                  all_scf_converged=all(r['converged'] for r in rows+sweep),
                  basis_target_reached=all(r['target_reached'] for r in refinements),
                  scf_tolerance_refinement=all(b['energy_error_to_tight']<=a['energy_error_to_tight']+1e-12 for a,b in zip(sweep,sweep[1:])))
    return dict(schema_version=1,case='h2-rhf',input_sha256=sha(path),reference_sha256=sha(reference_path),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),scope=config['scope'],execution_options=config['scf'],
                basis_definitions=config['basis_definitions'],cases=rows,tolerance_sweep=sweep,basis_refinement=refinements,
                metrics=metrics,checks=checks,passed=all(checks.values()),termination='fixed_sweep_completed' if all(r['converged'] for r in rows+sweep) else 'scf_not_converged')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,default=Path('inputs.json'));p.add_argument('--output',type=Path,required=True);p.add_argument('--max-cycles',type=int,help='Diagnostic SCF budget override; recorded in output');a=p.parse_args()
    try:
        if a.output.exists() and any(a.output.iterdir()):raise ValueError('Output directory must be new or empty')
        result=calculate(a.input,a.max_cycles);a.output.mkdir(parents=True,exist_ok=True)
        (a.output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
        with (a.output/'solution.csv').open('w',newline='') as f:
            writer=csv.writer(f);writer.writerow(['bond_bohr','basis_index','nbf','energy_total','reference_energy','absolute_error','iterations','commutator','overlap_condition'])
            indices={b['id']:i for i,b in enumerate(result['basis_definitions'])}
            for r in result['cases']:writer.writerow([r['bond_bohr'],indices[r['basis_id']],r['nbf'],r['energy_total'],r['reference_energy'],r['energy_error'],r['iterations'],r['scf_commutator_norm'],r['overlap_condition_number']])
        with (a.output/'scf.csv').open('w',newline='') as f:
            writer=csv.writer(f);writer.writerow(['bond_bohr','basis_index','iteration','energy_total','delta_energy','density_change','commutator'])
            for r in result['cases']:
                for t in r['trace']:writer.writerow([r['bond_bohr'],indices[r['basis_id']],t['iteration'],t['energy_total'],t['delta_energy'] if t['delta_energy'] is not None else 0.,t['density_change'] if t['density_change'] is not None else 0.,t['scf_commutator_norm']])
        print(json.dumps({'passed':result['passed'],'metrics':result['metrics']}))
        return 0 if result['passed'] else 1
    except Exception as exc:
        print(str(exc),file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
