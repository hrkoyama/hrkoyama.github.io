"""Saved-data-only main and gallery figures; no neural/ODE solver imports."""
import argparse
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw(result_file, output):
    path = Path(result_file)
    if path.is_dir():
        path = path/'result.json'
    root = path.parent; output = Path(output); output.mkdir(parents=True, exist_ok=True)
    result = json.loads(path.read_text())
    for case in result['cases']:
        ident = case['id']; fig, axes = plt.subplots(2, 2, figsize=(11, 7))
        a, b, c, d = axes.ravel()
        if ident == 'pinn-poisson':
            for seed in [8401, 8402, 8403]:
                x = np.load(root/f'pinn-{seed}.npz')
                a.plot(x['x'], x['u'], label=f'PINN {seed}')
                b.plot(x['x'], x['u']-x['exact'], label=str(seed))
                c.plot(x['x'], x['pde_residual'], label=str(seed))
            a.plot(x['x'], x['exact'], 'k--', label='analytic')
            fd = [r for r in case['records'] if r['kind'] == 'FD2']
            d.loglog([r['nodes'] for r in fd], [r['solution_Linf'] for r in fd], 'o-', label='FD2')
            a.set(xlabel='x', ylabel='u'); b.set(xlabel='x', ylabel='solution error')
            c.set(xlabel='x', ylabel='PDE residual'); d.set(xlabel='interior nodes', ylabel='FD error')
            title = 'Poisson PINN: independent grid and finite differences'
        elif ident == 'fno-periodic-heat':
            for seed in [8501, 8502]:
                x = np.load(root/f'fno-{seed}-profiles.npz'); grid = 2*np.pi*np.arange(64)/64
                a.plot(grid, x['u850300_64'], label=f'FNO {seed}')
                b.plot(grid, x['u850300_64']-x['y850300_64'], label=str(seed))
            a.plot(grid, x['y850300_64'], 'k--', label='analytic heat')
            with (root/'fno-evaluations.csv').open() as stream:
                rows = list(csv.DictReader(stream))
            for j, split in enumerate(['test', 'ood-nu', 'ood-spectrum']):
                values = [float(r['absolute_RMS']) for r in rows if r['split'] == split and r['N'] == '64']
                c.plot(np.full(len(values), j), values, 'o', label=split)
            transfer = [float(r['restriction_discrepancy_RMS']) for r in rows if r.get('restriction_discrepancy_RMS')]
            d.plot(np.arange(len(transfer)), transfer, 'o', label='same-weight restriction')
            a.set(xlabel='periodic x', ylabel='u(T)'); b.set(xlabel='periodic x', ylabel='solution error')
            c.set_xticks(range(3), ['ID', 'nu OOD', 'spectrum OOD']); c.set_ylabel('absolute RMS error')
            d.set(xlabel='fixed test function/model index', ylabel='N64 restricted - N32 RMS')
            title = 'Tiny FNO: held-out functions, grid transfer and OOD'
        elif ident == 'enzyme-qssa':
            for label in ['01', '002']:
                x = np.load(root/f'enzyme-{label}-r1e-08.npz'); total = .01 if label == '01' else .002
                theta = x['t']*total
                a.plot(theta, x['y'][:, 0], label=f'full free S, Etotal={total}')
                a.plot(theta, x['mm'], '--', label=f'QSSA free S, {total}')
                b.plot(theta, x['reference'][:, 0]-x['mm'], label=str(total))
                ya = x['accepted_y']; c.plot(x['accepted_t']*total, ya[:, 1], label=f'C, {total}')
                d.plot(x['accepted_t']*total, ya[:, 0]+ya[:, 1]+ya[:, 3]-1, label=str(total))
            a.set(xlabel='slow time theta', ylabel='free substrate S'); b.set(xlabel='theta', ylabel='QSSA modeling error')
            c.set(xlabel='theta', ylabel='full-model complex C'); d.set(xlabel='theta', ylabel='S+C+P - 1')
            title = 'Enzyme kinetics: initial layer and separate QSSA error'
        elif ident == 'lotka-volterra':
            x = np.load(root/'lv-1600.npz'); y = x['y']
            a.plot(y[:, 0], y[:, 1], label='RK4'); a.plot(x['reference'][:, 0], x['reference'][:, 1], '--', label='log-coordinate reference')
            b.plot(x['t'], y[:, 0], label='prey'); b.plot(x['t'], y[:, 1], label='predator')
            c.plot(x['t'], x['invariant']-x['invariant'][0], label='H-H(0)')
            d.loglog([r['steps'] for r in case['records']], [r['state_Linf'] for r in case['records']], 'o-', label='state error')
            a.set(xlabel='prey x', ylabel='predator y'); b.set(xlabel='time', ylabel='population')
            c.set(xlabel='time', ylabel='invariant drift'); d.set(xlabel='steps', ylabel='state Linf error')
            title = 'Lotka-Volterra: positive orbit, invariant and actual error'
        else:
            x = np.load(root/'seir-1e-4-1600.npz')
            for j, name in enumerate(['S', 'E', 'I', 'R']):
                a.plot(x['t'], x['y'][:, j], label=name)
            for j, name in enumerate(['E', 'I']):
                b.plot(x['early_t'], x['early_reference'][:, j+1], label=name+' full')
                b.plot(x['early_t'], x['early_linear'][:, j], '--', label=name+' linear')
            c.plot(x['t'], x['y'].sum(axis=1)-1, label='population defect')
            rows = [r for r in case['records'] if r['steps'] == 1600]
            d.plot([r['eta'] for r in rows], [r['early_deviation_over_eta_squared'] for r in rows], 'o-', label='full - linear / eta squared')
            a.set(xlabel='time', ylabel='population fraction'); b.set(xlabel='early time', ylabel='exposed/infectious fraction')
            c.set(xlabel='time', ylabel='total population - 1'); d.set(xlabel='initial eta', ylabel='scaled modeling deviation')
            title = 'SEIR: conservation and full two-mode initial linearization'
        for ax in [a, b, c, d]:
            ax.grid(True, alpha=.25); ax.legend(fontsize=7)
        summary = case['original_target_summary']
        fig.suptitle(title)
        fig.text(.5, .005, f"Original study goals met: {summary['met']}/{summary['total']}. Reproduction checks are separate.", ha='center', fontsize=9)
        fig.tight_layout(rect=(0, .035, 1, .96))
        for suffix in ['', '-preview']:
            for ext in ['png', 'svg', 'pdf']:
                fig.savefig(output/(ident+suffix+'.'+ext), dpi=150, bbox_inches='tight')
        plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--results', required=True); parser.add_argument('--output', required=True)
    args = parser.parse_args(); draw(args.results, args.output)

