"""Draw original textbook figures from saved CSVs (optional reportlab 4.4.9)."""
import argparse, csv, json, math, subprocess
from pathlib import Path
from reportlab.graphics.shapes import Drawing, Line, PolyLine, Rect, Circle, String
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib.colors import HexColor, Color, white
import lab
C = ['#176c78', '#bc5a32', '#5c558e', '#607b3e']
INK = HexColor('#243536')
GRID = HexColor('#d9e1df')

def data(base, name):
    with (base / (name + '.csv')).open() as f:
        return list(csv.DictReader(f))

def lines(title, xlabel, ylabel, series, logx=False, logy=False, limits=None):
    d = Drawing(760, 350)
    d.add(Rect(0, 0, 760, 350, fillColor=white, strokeColor=None))
    (L, B, W, H) = (82, 66, 646, 222)
    xx = [x for s in series for (x, y) in s[1] if (not logx or x > 0) and (not logy or y > 0)]
    yy = [y for s in series for (x, y) in s[1] if (not logx or x > 0) and (not logy or y > 0)]
    tx = (lambda x: math.log10(x)) if logx else lambda x: x
    ty = (lambda y: math.log10(y)) if logy else lambda y: y
    (xmin, xmax) = (min(map(tx, xx)), max(map(tx, xx)))
    (ymin, ymax) = (min(map(ty, yy)), max(map(ty, yy)))
    if limits:
        (ymin, ymax) = map(ty, limits)
    if xmin == xmax:
        xmin -= 0.5
        xmax += 0.5
    if ymin == ymax:
        ymin -= 0.5
        ymax += 0.5
    padx = (xmax - xmin) * 0.025
    pady = (ymax - ymin) * 0.08
    xmin -= padx
    xmax += padx
    if not limits:
        ymin -= pady
        ymax += pady
    X = lambda x: L + (tx(x) - xmin) / (xmax - xmin) * W
    Y = lambda y: B + (ty(y) - ymin) / (ymax - ymin) * H
    for j in range(6):
        vx = xmin + (xmax - xmin) * j / 5
        vy = ymin + (ymax - ymin) * j / 5
        d.add(Line(L + j * W / 5, B, L + j * W / 5, B + H, strokeColor=GRID, strokeWidth=0.6))
        d.add(Line(L, B + j * H / 5, L + W, B + j * H / 5, strokeColor=GRID, strokeWidth=0.6))
        a = 10 ** vx if logx else vx
        b = 10 ** vy if logy else vy
        fmt = lambda z: format(z, '.2g')
        d.add(String(L + j * W / 5, B - 21, fmt(a), fontSize=12, textAnchor='middle', fillColor=INK))
        d.add(String(L - 9, B + j * H / 5 - 4, fmt(b), fontSize=12, textAnchor='end', fillColor=INK))
    d.add(Rect(L, B, W, H, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    d.add(String(380, 327, title, fontSize=18, textAnchor='middle', fillColor=INK))
    d.add(String(L + W / 2, 15, xlabel, fontSize=14, textAnchor='middle', fillColor=INK))
    d.add(String(8, 310, ylabel + (' (log)' if logy else ''), fontSize=12, fillColor=INK))
    for (i, (name, pts)) in enumerate(series):
        good = [(x, y) for (x, y) in pts if (not logx or x > 0) and (not logy or y > 0)]
        flat = [z for (x, y) in good for z in (X(x), Y(y))]
        if len(flat) >= 4:
            d.add(PolyLine(flat, strokeColor=HexColor(C[i % len(C)]), strokeWidth=1.8, fillColor=None))
        if len(good) < 20:
            for (x, y) in good:
                d.add(Circle(X(x), Y(y), 2.8, fillColor=HexColor(C[i % len(C)]), strokeColor=None))
        ly = H + B - 15 - i * 17
        d.add(Line(L + 12, ly, L + 37, ly, strokeColor=HexColor(C[i % len(C)]), strokeWidth=2))
        d.add(String(L + 43, ly - 4, name, fontSize=12, fillColor=INK))
    return d

def boundary_diagram():
    d = Drawing(760, 350)
    d.add(Rect(0, 0, 760, 350, fillColor=white, strokeColor=None))
    d.add(String(380, 323, 'Boundary data: value, outward derivative, or a combination', fontSize=17, textAnchor='middle', fillColor=INK))
    for (k, (name, eq)) in enumerate([('Dirichlet', 'u = g'), ('Neumann', 'normal derivative = g'), ('Robin', 'alpha u + beta normal derivative = g')]):
        y = 250 - k * 92
        d.add(String(30, y + 18, name, fontSize=16, fillColor=INK))
        d.add(Line(160, y, 690, y, strokeColor=INK, strokeWidth=2))
        for i in range(9):
            d.add(Circle(160 + i * 530 / 8, y, 3.5, fillColor=HexColor(C[0]), strokeColor=None))
        for (x, sign) in [(160, -1), (690, 1)]:
            d.add(Line(x, y - 18, x + sign * 30, y - 18, strokeColor=HexColor(C[1]), strokeWidth=1.5))
            d.add(Line(x + sign * 30, y - 18, x + sign * 23, y - 14, strokeColor=HexColor(C[1])))
            d.add(Line(x + sign * 30, y - 18, x + sign * 23, y - 22, strokeColor=HexColor(C[1])))
        d.add(String(425, y + 20, eq, fontSize=13, textAnchor='middle', fillColor=INK))
        d.add(String(160, y - 40, 'x=0, n=-1', fontSize=12, textAnchor='middle', fillColor=INK))
        d.add(String(690, y - 40, 'x=1, n=+1', fontSize=12, textAnchor='middle', fillColor=INK))
    return d

def stability_regions():
    d = Drawing(760, 350)
    d.add(Rect(0, 0, 760, 350, fillColor=white, strokeColor=None))
    d.add(String(380, 325, 'Absolute stability regions in z = lambda dt', fontSize=18, textAnchor='middle', fillColor=INK))
    for (i, name) in enumerate(['Forward Euler', 'Backward Euler', 'Trapezoidal']):
        x = 24 + i * 250
        y = 62
        s = 34
        W = 204
        H = 204
        X = lambda a: x + (a + 4) * s
        Y = lambda b: y + (b + 3) * s
        d.add(Rect(x, y, W, H, fillColor=HexColor('#e7f0ed') if i == 1 else white, strokeColor=None))
        if i == 0:
            d.add(Circle(X(-1), Y(0), s, fillColor=HexColor('#d2e8e2'), strokeColor=HexColor(C[0]), strokeWidth=1.5))
        elif i == 1:
            d.add(Circle(X(1), Y(0), s, fillColor=white, strokeColor=HexColor(C[0]), strokeWidth=1.5))
        else:
            d.add(Rect(x, y, 4 * s, H, fillColor=HexColor('#d2e8e2'), strokeColor=None))
        d.add(Line(X(0), y, X(0), y + H, strokeColor=INK, strokeWidth=0.7))
        d.add(Line(x, Y(0), x + W, Y(0), strokeColor=INK, strokeWidth=0.7))
        d.add(Rect(x, y, W, H, fillColor=None, strokeColor=INK, strokeWidth=0.8))
        d.add(String(x + W / 2, 286, name, fontSize=15, textAnchor='middle', fillColor=INK))
        d.add(String(x + W / 2, 30, 'Re z: -4 to 2', fontSize=12, textAnchor='middle', fillColor=INK))
        d.add(String(x + 4, 52, 'Im z: -3 to 3', fontSize=11, fillColor=INK))
    d.add(String(380, 5, 'Shaded = |R(z)| <= 1. Stability is not accuracy.', fontSize=13, textAnchor='middle', fillColor=INK))
    return d

def generate(base, out):
    out.mkdir(parents=True, exist_ok=True)
    result = json.loads((base / 'result.json').read_text())
    figs = {}
    group = lambda records, key, x, y: [(name, [(float(r[x]), float(r[y])) for r in records if r[key] == name]) for name in dict.fromkeys((r[key] for r in records))]
    r = data(base, 'derivative')
    figs[1] = lines('Truncation and roundoff: centered derivative', 'difference width h', 'absolute derivative error', [('sin(x), x=1', [(float(z['h']), float(z['error'])) for z in r])], True, True)
    r = data(base, 'norms')
    figs[2] = lines('One-cell error of height 1: different norms', 'number of cells N', 'error norm', [(k, [(float(z['n']), float(z[k])) for z in r]) for k in ['l1', 'l2', 'linf']], True, True)
    m = result['metrics']['conditioning']
    figs[3] = lines('Small residual does not imply small solution error', 'diagnostic: 1 residual, 2 solution, 3 backward', 'relative magnitude', [('ill-conditioned 2x2', [(1, m['residual_relative_inf']), (2, m['forward_relative_inf']), (3, m['backward_error'])])], False, True)
    r = data(base, 'advection')
    figs[4] = lines('Measured grid convergence at fixed final time', 'grid width h', 'L2 error', group(r, 'method', 'h', 'l2_error'), True, True)
    r = data(base, 'unstable')
    figs[5] = lines('Two deliberately unstable controls', 'number of steps', 'norm / initial norm', group(r, 'method', 'step', 'norm_ratio'), False, True)
    figs[6] = stability_regions()
    r = [r for r in data(base, 'stiff') if r['method'] != 'forward']
    ss = group(r, 'method', 'time', 'value')
    ss.append(('exact exp(-40 t)', [(j * 0.01, math.exp(-40 * j * 0.01)) for j in range(201)]))
    figs[7] = lines('A-stable methods: stiff transient at dt=0.25', 'time t', 'solution value', ss, limits=[-0.8, 1.05])
    r = data(base, 'symbols')
    ss = group(r, 'method', 'theta_over_pi', 'amplitude')
    ss.append(('FTCS (nu=0.6)', [(j / 64, abs(lab.symbol('ftcs', math.pi * j / 64, 0.6))) for j in range(1, 64)]))
    figs[8] = lines('Fourier amplification at Courant number 0.6', 'resolved wave number theta / pi', 'one-step amplitude |G|', ss)
    r = data(base, 'unstable')
    figs[9] = lines('CFL is not sufficient: FTCS also grows at nu=0.6', 'number of steps', 'norm / initial norm', group(r, 'method', 'step', 'norm_ratio'), False, True)
    r = data(base, 'symbols')
    ss = group(r, 'method', 'theta_over_pi', 'amplitude')
    ss.append(('exact advection', [(0, 1), (1, 1)]))
    figs[10] = lines('Numerical dissipation: amplitude response', 'resolved wave number theta / pi', 'one-step amplitude |G|', ss)
    ss = []
    for method in ['upwind', 'lax-wendroff']:
        for (key, label) in [('phase_speed_ratio', 'phase'), ('group_speed_ratio', 'group')]:
            ss.append((method + ' ' + label, [(float(z['theta_over_pi']), float(z[key])) for z in r if z['method'] == method]))
    figs[11] = lines('Numerical dispersion: phase and group velocities', 'resolved wave number theta / pi', 'speed / exact advection speed', ss)
    r = data(base, 'advection-field')
    ss = []
    for method in ['upwind', 'lax-wendroff']:
        ss.append((method, [(float(z['x']), float(z['numerical']) - float(z['reference'])) for z in r if z['method'] == method]))
    figs[12] = lines('Bounded field errors are distinct from unstable growth', 'position x', 'numerical minus exact field', ss)
    figs[13] = boundary_diagram()
    r = [z for z in data(base, 'boundary') if z['kind'].startswith('mixed')]
    figs[14] = lines('Boundary closure changes the global observed order', 'grid width h', 'maximum field error', group(r, 'kind', 'h', 'linf_error'), True, True)
    r = [z for z in data(base, 'boundary-field') if z['kind'] == 'neumann']
    figs[15] = lines('Pure Neumann: fix a mean to select one solution', 'position x', 'field u', [('numerical, zero mean', [(float(z['x']), float(z['numerical'])) for z in r]), ('exact, zero mean', [(float(z['x']), float(z['reference'])) for z in r]), ('exact +1, same derivative data', [(float(z['x']), float(z['reference']) + 1) for z in r])])
    r = data(base, 'heat-time')
    figs[16] = lines('Time refinement at fixed space: two reference targets', 'time step dt', 'L2 error', [(key, [(float(z['dt']), float(z[key])) for z in r]) for key in ['semidiscrete_l2_error', 'continuum_l2_error']], True, True)
    r = data(base, 'splitting')
    figs[17] = lines('Same oscillator, exact subflows, same final time', 'time step dt', 'state error', group(r, 'method', 'dt', 'state_error'), True, True)
    r = [z for z in data(base, 'oscillator') if z['method'] in ['symplectic', 'verlet'] and round(float(z['time']) * 10) % 20 == 0]
    figs[18] = lines('Physical energy is not exactly conserved (dt=0.1)', 'time t', 'physical energy / initial energy', group(r, 'method', 'time', 'energy_fraction'), limits=[0.94, 1.06])
    vals = [('derivative', min(result['metrics']['derivative']['orders'])), ('upwind', min(result['metrics']['advection']['upwind']['orders'])), ('L-W', min(result['metrics']['advection']['lax-wendroff']['orders'])), ('heat', min(result['metrics']['heat']['joint_orders'])), ('Robin', min(result['metrics']['boundary']['robin']['orders'])), ('Lie', min(result['metrics']['splitting']['lie']['orders'])), ('Strang', min(result['metrics']['splitting']['strang']['orders']))]
    figs[19] = lines('Observed orders for these fixed smooth examples only', '1 derivative / 2 upwind / 3 L-W / 4 heat / 5 Robin / 6 Lie / 7 Strang', 'observed refinement order', [('measured', [(i + 1, v) for (i, (k, v)) in enumerate(vals)])], limits=[0, 2.2])
    for (n, d) in figs.items():
        stem = out / f'figure-{n:02d}'
        renderSVG.drawToFile(d, str(stem) + '.svg')
        renderPDF.drawToFile(d, str(stem) + '.pdf')
        subprocess.run(['pdftoppm', '-singlefile', '-scale-to', '1600', '-png', str(stem) + '.pdf', str(stem)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    print('Drew19figuresfromsavedCSV;SVG/PDFsharethevectorDrawing.')
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    generate(a.results, a.output)
