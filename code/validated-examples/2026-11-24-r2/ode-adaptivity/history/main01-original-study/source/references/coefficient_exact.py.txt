"""Exact rational audit of source literals, without importing production code."""
import ast
from fractions import Fraction as F
from pathlib import Path


def fraction(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return F(str(node.value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -fraction(node.operand)
    if isinstance(node, ast.BinOp):
        a, b = fraction(node.left), fraction(node.right)
        if isinstance(node.op, ast.Div): return a/b
        if isinstance(node.op, ast.Mult): return a*b
        if isinstance(node.op, ast.Add): return a+b
        if isinstance(node.op, ast.Sub): return a-b
    if isinstance(node, (ast.List, ast.Tuple)):
        return [fraction(n) for n in node.elts]
    raise ValueError('Unrecognized coefficient expression')


def literals(path):
    out = {}
    for node in ast.parse(Path(path).read_text()).body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ('A', 'B', 'C', 'E', 'P'):
            out[node.targets[0].id] = fraction(node.value.args[0])
    if set(out) != set(('A', 'B', 'C', 'E', 'P')):
        raise ValueError('Exact five coefficient blocks required')
    return out


def audit(path):
    data = literals(path)
    a, b, c, e, p = [data[k] for k in ('A', 'B', 'C', 'E', 'P')]
    dot = lambda left, right: sum((x*y for x, y in zip(left, right)), F(0))
    check = {}
    check['explicit-shapes'] = len(a) == len(b) == len(c) == 6 and len(e) == len(p) == 7 and all(len(row) == 4 for row in p) and all(all(value == 0 for value in row[i:]) for i, row in enumerate(a))
    check['A-row-sums-C'] = all(sum(row) == ci for row, ci in zip(a, c))
    check['B-consistency'] = sum(b) == 1
    check['E-constant-zero'] = sum(e) == 0
    for power in (1, 2, 3, 4):
        check['B-C-moment-'+str(power)] = dot(b, [x**power for x in c]) == F(1, power+1)
    ac = [dot(row, c) for row in a]
    check['B-A-C'] = dot(b, ac) == F(1, 6)
    rates = []
    for i in range(6):
        rate = [F(1)]+[F(0)]*6
        for j in range(i):
            for k in range(6):rate[k+1] += a[i][j]*rates[j][k]
        rates.append(rate)
    stability = [F(1)]+[F(0)]*6
    for j in range(6):
        for k in range(6):stability[k+1] += b[j]*rates[j][k]
    check['scalar-stability-through-six'] = stability == [F(1), F(1), F(1,2), F(1,6), F(1,24), F(1,120), F(1,600)]
    check['dense-left-derivative'] = [row[0] for row in p] == [F(1)]+[F(0)]*6
    check['dense-right-state'] = [sum(row) for row in p] == b+[F(0)]
    check['dense-right-derivative'] = [sum((j+1)*value for j, value in enumerate(row)) for row in p] == [F(0)]*6+[F(1)]
    check['FSAL-appended-endpoint'] = c[-1] == 1 and len(b+[F(0)]) == 7 and e[-1] == F(1,40)
    return check, {k: str(v) for k, v in check.items()}
